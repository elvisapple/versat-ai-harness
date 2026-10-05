"""Exercise deterministic workflow commands locally; never claim remote execution."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import yaml
from support import PACKAGE, runner, sdd, write_config, simple_test
sys.path.insert(0, str(PACKAGE/'tests/validators'))
import test_sdd_v3


class CiTests(unittest.TestCase):
    def step(self):
        workflow = yaml.safe_load((PACKAGE/'.github/workflows/validate.yml').read_text())
        return next(s['run'] for s in workflow['jobs']['structural-validation']['steps']
                    if s.get('name') == 'Validate repository contracts')

    def run_step(self, root, baseline='trusted-base', archive='false'):
        return subprocess.run(['bash', '-e', '-c', self.step()], cwd=root,
                              env={**os.environ, 'SDD_BASELINE':baseline, 'SDD_REQUIRE_ARCHIVE':archive},
                              capture_output=True, text=True)

    def test_structural_workflow_executes_baseline_and_archive_branches(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder); script=root/'scripts/validate/run.sh'; script.parent.mkdir(parents=True)
            script.write_text('#!/bin/sh\nprintf "%s\\n" "$@" > observed.txt\n'); script.chmod(0o755)
            for flag in ('true','false'):
                process=self.run_step(root, archive=flag)
                self.assertEqual(process.returncode,0,process.stderr)
                self.assertEqual((root/'observed.txt').read_text().splitlines(),['--baseline','trusted-base']+(['--require-archive'] if flag=='true' else []))

    def test_missing_baseline_does_not_launch_validation(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            self.assertNotEqual(self.run_step(root, baseline='').returncode, 0)
            self.assertFalse((root/'observed.txt').exists())

    def test_validation_failure_propagates_in_both_workflow_branches(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder); script=root/'scripts/validate/run.sh'; script.parent.mkdir(parents=True)
            script.write_text('#!/bin/sh\nexit 23\n'); script.chmod(0o755)
            for flag in ('true','false'):
                self.assertEqual(self.run_step(root, archive=flag).returncode, 23)

    def test_reference_ci_runs_full_new_and_retained_suites_and_exposes_failure(self):
        workflow=yaml.safe_load((PACKAGE/'project-templates/artifacts/validation/python/.github/workflows/validate.yml').read_text())
        command=next(s['run'] for s in workflow['jobs']['tests']['steps'] if s.get('name')=='Run every required suite')
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder); config=write_config(root); simple_test(root)
            (root/'regressions').mkdir()
            (root/'regressions/test_old.py').write_text('import unittest\nclass Old(unittest.TestCase):\n    def test_old(self): self.fail("retained regression")\n')
            retained=dict(config['suites'][0],id='regressions',argv=['{python}','-m','unittest','discover','-s','regressions'])
            config['suites'].append(retained); config['required_suites'].append('regressions'); config['inputs']['include'].append('regressions')
            (root/'.versat/validation.yaml').write_text(yaml.safe_dump(config))
            script=root/'scripts/validate/run.sh'; script.parent.mkdir(parents=True)
            script.write_text('#!/bin/sh\nexec "'+sys.executable+'" "'+str(PACKAGE/'scripts/testing/run.py')+'" run --root . "$@"\n')
            process=subprocess.run(['bash','-e','-c',command],cwd=root,capture_output=True,text=True)
            self.assertEqual(process.returncode,1,process.stderr)
            import json
            report=json.loads(Path(json.loads(process.stdout)['report']).read_text())
            self.assertEqual(report['scope'],'full'); self.assertEqual(report['execution'],'ci')
            self.assertEqual([s['result'] for s in report['suites']],['pass','fail'])

    def test_missing_or_unverified_supervised_evidence_blocks_delivery(self):
        fixture=test_sdd_v3.V3Tests('test_partial_v3_planning_and_all_gate_states')
        fixture.setUp(); self.addCleanup(fixture.doCleanups)
        fixture.data['design']['validation'][0]['method']={'kind':'review','procedure':'Observe supervised fixture behavior and independent replay.','reason':'Supervised local evidence.'}
        fixture.approved_plan()
        missing=sdd.validate_repository(fixture.root,'delivery',fixture.change_id)
        self.assertTrue(any(f['code']=='VALIDATION_MISSING' for f in missing['findings']))
        # A declared unverified supervised result must remain a gap too.
        check=fixture.data['design']['validation'][0]
        digest=sdd.input_digest(fixture.root,fixture.change,check)
        evidence=fixture.root/'supervised.txt'; evidence.write_text('Runtime observation unavailable.\n')
        fixture.data['tasks']['validation']['plan_digest']=sdd.stage_digest(fixture.change,'tasks')
        fixture.data['tasks']['validation']['results']=[{'check':check['id'],'result':'unverified','evidence':'supervised.txt','revision':'synthetic local attempt','input_digest_before':digest,'input_digest_after':digest,'context':{'execution':'local','environment':'synthetic test','observed':True}}]
        fixture.write('tasks')
        unverified=sdd.validate_repository(fixture.root,'delivery',fixture.change_id)
        self.assertTrue(any(f['code']=='VALIDATION_MISSING' for f in unverified['findings']))
