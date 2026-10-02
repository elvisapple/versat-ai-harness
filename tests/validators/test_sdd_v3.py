"""Behavioral acceptance/regression contracts using synthetic repositories."""
from __future__ import annotations
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

import test_sdd as original
from test_sdd import VALIDATOR, VALIDATOR_PATH


class V3Tests(unittest.TestCase):
    review = staticmethod(original.SddValidationTests.review)
    write = original.SddValidationTests.write
    begin = original.SddValidationTests.begin
    digest = original.SddValidationTests.digest
    approve = original.SddValidationTests.approve
    approved_plan = original.SddValidationTests.approved_plan
    complete = original.SddValidationTests.complete
    ready = original.SddValidationTests.ready
    assert_status = original.SddValidationTests.assert_status

    def bind_v2_fixture(self):
        pass

    def setUp(self):
        original.SddValidationTests.setUp(self)
        for data in self.data.values():
            data['sdd_version'] = 3
        self.body['proposal'] += '\n## Baseline\nThe existing button displays a greeting.\n'
        self.data['proposal']['impact'] = {'state': 'assessed', 'summary': 'New isolated greeting behavior; no earlier contracts affected.', 'items': []}
        check = self.data['design']['validation'][0]
        check.update(method={'kind': 'automated', 'procedure': 'Run the greeting interaction test; expect Hello world.'},
                     inputs={'include': ['src', 'tests', 'fixtures', 'config.txt'], 'exclude': []}, outputs=['docs/evidence'], execution='local')
        self.data['design'].update(coverage=[{'scenario': {'requirement': 'REQ-001', 'scenario': 1}, 'applicability': 'required', 'checks': ['CHECK-001']}], regression=[])
        self.data['tasks']['validation'].update(assessments=[], findings=[])
        (self.root/'src').mkdir()
        (self.root/'src/greeting.py').write_text('def greet(): return "Hello world"\n')
        (self.root/'tests').mkdir()
        (self.root/'tests/case.txt').write_text('Activate greeting and observe Hello world.\n')
        (self.root/'config.txt').write_text('locale=en\n')
        (self.root/'fixtures').mkdir()
        (self.root/'fixtures/greeting.txt').write_text('synthetic greeting input\n')

    def result(self, phase='planning', change_id=None):
        return VALIDATOR.validate_repository(self.root, phase, change_id or self.change_id)

    def passing_evidence(self):
        original.SddValidationTests.passing_evidence(self)
        val = self.data['tasks']['validation']
        val.update(assessments=[], findings=[])
        result = val['results'][0]
        digest = VALIDATOR.input_digest(self.root, self.change, self.data['design']['validation'][0])
        result.update(input_digest_before=digest, input_digest_after=digest,
                      context={'execution': 'local', 'environment': 'Synthetic fixture runtime', 'observed': True})
        for row in self.data['design']['coverage']:
            val['assessments'].append({'obligation': {'local': row['scenario']}, 'result': 'pass' if row['applicability'] == 'required' else 'not-applicable',
                                      'checks': row['checks'], 'evidence': result['evidence'], 'explanation': 'Synthetic observed interaction; not a production execution claim.'})
        for row in self.data['design']['regression']:
            val['assessments'].append({'obligation': {'regression': row['obligation']}, 'result': 'pass', 'checks': row['checks'],
                                      'evidence': result['evidence'], 'explanation': 'Retained behavior observed in the synthetic fixture.'})
        self.write('tasks')

    def add_origin(self, identifier='old-greeting', effect='preserve'):
        directory = self.root/'specs/archive'/identifier
        directory.mkdir(parents=True)
        source_data = copy.deepcopy(self.data['requirements'])
        source_data['change'] = identifier
        import yaml
        source = directory/'requirements.md'
        source.write_text('---\n' + yaml.safe_dump(source_data, sort_keys=False) + '---\n# Historical source\n')
        digest = VALIDATOR.sdd_assurance.requirements_digest(VALIDATOR, VALIDATOR._read_artifact(source))
        self.data['proposal']['impact']['items'].append({
            'source': {'change': identifier, 'requirement': 'REQ-001', 'scenarios': [1], 'requirements_digest': digest},
            'current_contract': {'change': self.change_id, 'artifact': 'proposal', 'locator': '## Baseline'},
            'effect': effect, 'targets': ['REQ-001'], 'reason': 'Preserve the existing observable greeting unless explicitly replaced.'})
        if effect != 'supersede':
            self.data['design']['regression'].append({'obligation': {'impact': len(self.data['proposal']['impact']['items']), 'scenario': 1},
                                                    'checks': ['CHECK-001'], 'rationale': 'Existing test covers the retained behavior.'})
        return source

    def codes(self, result):
        return {f['code'] for f in result['findings']}

    def test_partial_v3_planning_and_all_gate_states(self):
        self.begin()
        self.assert_status('pass')
        self.assert_status('fail', 'implementation')
        self.approved_plan()
        self.assert_status('pass', 'implementation')
        self.complete(); self.passing_evidence()
        self.assert_status('pass', 'delivery')

    def test_schema_rejects_unknown_v3_fields(self):
        self.data['proposal']['impact']['invented'] = True
        self.begin()
        self.assertIn('SCHEMA', self.codes(self.assert_status('fail')))

    def test_mixed_version_cannot_downgrade(self):
        self.begin()
        self.data['requirements']['sdd_version'] = 2
        self.write('requirements')
        self.assertIn('MIXED_VERSION', self.codes(self.assert_status('fail')))

    def test_unknown_v2_not_admitted(self):
        self.data['proposal']['sdd_version'] = 2
        self.data['proposal'].pop('impact')
        self.data['requirements']['sdd_version'] = 2
        self.begin()
        self.assertIn('V2_UNLISTED', self.codes(self.assert_status('fail')))

    def test_many_scenarios_can_share_one_check(self):
        self.data['requirements']['requirements'][0]['acceptance'].append('Empty name keeps the greeting usable.')
        self.data['design']['coverage'].append({'scenario': {'requirement':'REQ-001','scenario':2},'applicability':'required','checks':['CHECK-001']})
        self.ready()
        self.assert_status('pass','delivery')

    def test_happy_path_does_not_hide_missing_boundary_coverage(self):
        self.data['requirements']['requirements'][0]['acceptance'].append('Handle an empty input.')
        self.ready()
        self.assertIn('TRACEABILITY', self.codes(self.assert_status('fail','delivery')))

    def test_missing_assessment_is_unverified_even_when_tasks_complete(self):
        self.ready(); self.data['tasks']['validation']['assessments']=[]; self.write('tasks')
        self.assertIn('ASSESSMENT_MISSING',self.codes(self.assert_status('unable-to-verify','delivery')))

    def test_failed_and_unverified_acceptance(self):
        self.ready()
        for outcome, status in [('fail','fail'),('unverified','unable-to-verify')]:
            self.data['tasks']['validation']['assessments'][0]['result']=outcome; self.write('tasks')
            self.assert_status(status,'delivery')

    def test_unapproved_exclusion_is_rejected(self):
        self.ready(); self.data['tasks']['validation']['assessments'][0]['result']='not-applicable'; self.write('tasks')
        self.assertIn('ASSESSMENT_EXCLUSION',self.codes(self.assert_status('fail','delivery')))

    def test_exclusion_requires_reason(self):
        self.data['design']['coverage'][0]['applicability']='not-applicable'; self.approved_plan()
        self.assertIn('COVERAGE_EXCLUSION',self.codes(self.assert_status('fail')))

    def test_reviewed_exclusion_is_not_counted_as_pass(self):
        self.data['design']['coverage'][0].update(applicability='not-applicable',reason='Synthetic platform has no optional display path.')
        self.ready()
        report=self.assert_status('pass','delivery')
        self.assertEqual('not-applicable',report['metrics'][self.change_id]['requirements']['REQ-001'])

    def test_duplicate_and_out_of_range_scenario_refs(self):
        self.data['design']['coverage'].append(copy.deepcopy(self.data['design']['coverage'][0]));self.approved_plan()
        self.assert_status('fail')
        self.data['design']['coverage'][1]['scenario']['scenario']=99;self.approve('design');self.approve('tasks')
        self.assert_status('fail')

    def test_scenario_reorder_invalidates_approval(self):
        self.ready(); self.data['requirements']['requirements'][0]['acceptance'].insert(0,'New first scenario.');self.write('requirements')
        self.assertIn('APPROVAL_STALE',self.codes(self.assert_status('fail')))

    def test_unresolved_impact_blocks_approval_readiness(self):
        self.data['proposal']['impact']['state']='unresolved';self.begin();self.assert_status('pass')
        self.approved_plan();self.assert_status('unable-to-verify','implementation')

    def test_archived_source_and_reused_regression(self):
        self.add_origin();self.ready();self.assert_status('pass','delivery')

    def test_same_req_id_in_two_sources_is_unambiguous(self):
        self.add_origin('first-source');self.add_origin('second-source');self.ready()
        self.assertEqual(2,self.assert_status('pass','delivery')['metrics'][self.change_id]['regression_obligations'])

    def test_missing_origin_is_not_no_impact(self):
        source=self.add_origin();self.ready();source.unlink()
        self.assert_status('unable-to-verify','delivery')

    def test_changed_origin_digest_is_unverified(self):
        source=self.add_origin();self.ready();source.write_text(source.read_text()+'Changed history.\n')
        self.assertIn('IMPACT_SOURCE',self.codes(self.assert_status('unable-to-verify','delivery')))

    def test_source_move_does_not_change_identity(self):
        source=self.add_origin();self.ready();source.parent.rename(self.root/'specs/changes/old-greeting')
        self.assert_status('pass','delivery')

    def test_missing_regression_mapping_cannot_hide_behind_current_check(self):
        self.add_origin();self.data['design']['regression']=[];self.ready();self.assert_status('fail','delivery')

    def test_supersession_uses_local_replacement(self):
        self.add_origin(effect='supersede');self.ready();self.assert_status('pass','delivery')

    def test_baseline_only_impact_without_fabricated_history(self):
        self.add_origin();self.data['proposal']['impact']['items'][0].pop('source')
        self.data['design']['regression'][0]['obligation']['scenario']=0
        self.ready();self.assert_status('pass','delivery')

    def test_manual_check_needs_reason_and_observed_result(self):
        self.data['design']['validation'][0]['method']['kind']='manual';self.approved_plan();self.assert_status('fail')
        self.data['design']['validation'][0]['method']['reason']='Review-only documentary behavior.'
        self.approve('design');self.approve('tasks');self.complete();self.passing_evidence();self.assert_status('pass','delivery')

    def test_old_evidence_cannot_be_relabelled_ci(self):
        self.ready();self.data['tasks']['validation']['results'][0]['context']['execution']='ci';self.write('tasks')
        self.assert_status('unable-to-verify','delivery')

    def test_unobserved_execution_is_not_pass(self):
        self.ready();self.data['tasks']['validation']['results'][0]['context']['observed']=False;self.write('tasks')
        self.assert_status('unable-to-verify','delivery')

    def test_mutations_to_all_declared_inputs_invalidate_results(self):
        self.ready()
        for name in ('src/greeting.py','tests/case.txt','fixtures/greeting.txt','config.txt'):
            path=self.root/name;original=path.read_bytes();path.write_bytes(original+b'changed')
            self.assertIn('INPUT_STALE',self.codes(self.assert_status('unable-to-verify','delivery')))
            path.write_bytes(original)
        self.assert_status('pass','delivery')

    def test_new_and_deleted_files_and_executable_bit_change_snapshot(self):
        self.ready();extra=self.root/'src/new.py';extra.write_text('new')
        self.assert_status('unable-to-verify','delivery');extra.unlink();self.assert_status('pass','delivery')
        file=self.root/'src/greeting.py';original=file.read_bytes();file.unlink();self.assert_status('unable-to-verify','delivery');file.write_bytes(original)
        file.chmod(0o755);self.assert_status('unable-to-verify','delivery')

    def test_missing_input_marker_detects_later_creation(self):
        self.data['design']['validation'][0]['inputs']['include'].append('optional.txt');self.ready();self.assert_status('pass','delivery')
        (self.root/'optional.txt').write_text('enabled');self.assert_status('unable-to-verify','delivery')

    def test_during_execution_change_invalidates_pass(self):
        self.ready();self.data['tasks']['validation']['results'][0]['input_digest_before']='0'*64;self.write('tasks')
        self.assert_status('unable-to-verify','delivery')

    def test_evidence_output_changes_do_not_invalidate(self):
        self.ready();(self.root/'docs/evidence/greeting.txt').write_text('Reformatted observed report.');self.assert_status('pass','delivery')

    def test_wide_scope_requires_explicit_output_exclusion(self):
        check=self.data['design']['validation'][0];check['inputs']={'include':['.'],'exclude':[]}
        self.approved_plan();self.assert_status('fail')
        check['inputs']['exclude']=['docs/evidence'];self.approve('design');self.approve('tasks');self.complete();self.passing_evidence();self.assert_status('pass','delivery')

    def test_path_escape_symlink_and_special_file_are_rejected(self):
        self.ready();check=self.data['design']['validation'][0]
        for value in ('../secret','/tmp/secret'):
            check['inputs']['include']=[value];self.approve('design');self.approve('tasks');self.assert_status('fail')
        check['inputs']['include']=['src'];self.approve('design');self.approve('tasks')
        link=self.root/'src/link';link.symlink_to('/tmp');self.assert_status('fail');link.unlink()
        os.mkfifo(self.root/'src/pipe');self.assert_status('fail')

    def test_explicit_source_cannot_be_output(self):
        self.data['design']['validation'][0]['outputs']=['src'];self.approved_plan();self.assert_status('fail')

    def test_archive_inventory_is_historical_but_selected_delivery_is_live(self):
        self.ready();archive=self.root/'specs/archive'/self.change_id;archive.parent.mkdir(parents=True);self.change.rename(archive);self.change=archive
        (self.root/'src/greeting.py').write_text('changed current code')
        self.assert_status('pass');self.assert_status('unable-to-verify','delivery')

    def test_archive_move_alone_preserves_snapshot(self):
        self.ready();archive=self.root/'specs/archive'/self.change_id;archive.parent.mkdir(parents=True);self.change.rename(archive);self.change=archive
        self.assert_status('pass','delivery')

    def finding(self):
        return {'id':'FIND-001','source':{'local':{'requirement':'REQ-001','scenario':1}},'category':'partial','state':'open',
                'evidence':'docs/evidence/greeting.txt','description':'Required error path is missing.','tasks':['TASK-001'],'checks':['CHECK-001']}

    def test_open_findings_block_and_resolution_requires_evidence(self):
        self.ready();finding=self.finding();self.data['tasks']['validation']['findings']=[finding];self.write('tasks');self.assert_status('fail','delivery')
        finding.update(state='resolved');self.write('tasks');self.assert_status('unable-to-verify','delivery')
        finding['resolution']='Existing task corrected the missing path and check reran.';self.write('tasks');self.assert_status('pass','delivery')

    def test_duplicate_open_findings_and_unknown_correction_tasks_fail(self):
        self.ready();a=self.finding();b=copy.deepcopy(a);b['id']='FIND-002';self.data['tasks']['validation']['findings']=[a,b];self.write('tasks')
        self.assertIn('FINDING_DUPLICATE',self.codes(self.assert_status('fail')))
        b['tasks']=['TASK-999'];self.write('tasks');self.assertIn('FINDING_REFERENCE',self.codes(self.assert_status('fail')))

    def test_new_task_content_reopens_approval(self):
        self.ready();self.data['tasks']['tasks'][0]['description']='Changed work';self.write('tasks')
        self.assertIn('APPROVAL_STALE',self.codes(self.assert_status('fail','implementation')))

    def test_input_digest_cli_and_unknown_check(self):
        self.approved_plan()
        args=[sys.executable,str(VALIDATOR_PATH),'--root',str(self.root),'--change',self.change_id,'--input-digest']
        good=subprocess.run(args+['CHECK-001'],capture_output=True,text=True)
        self.assertEqual(0,good.returncode,good.stdout+good.stderr)
        self.assertEqual(64,len(good.stdout.strip()))
        bad=subprocess.run(args+['CHECK-999'],capture_output=True,text=True)
        self.assertEqual(1,bad.returncode)

    def test_input_digest_requires_approval(self):
        self.begin()
        result=subprocess.run([sys.executable,str(VALIDATOR_PATH),'--root',str(self.root),'--change',self.change_id,'--input-digest','CHECK-001'],capture_output=True,text=True)
        self.assertEqual(1,result.returncode)

    def git(self,*args):
        result=subprocess.run(['git','-C',str(self.root),*args],capture_output=True,text=True)
        self.assertEqual(0,result.returncode,result.stderr)
        return result.stdout.strip()

    def baseline(self):
        self.git('init','-q');self.git('config','user.name','Synthetic');self.git('config','user.email','synthetic@example.invalid')
        self.git('add','.');self.git('commit','-qm','Synthetic baseline')
        return self.git('rev-parse','HEAD')

    def test_baseline_selects_new_archive_and_checks_live(self):
        self.ready();base=self.baseline();archive=self.root/'specs/archive'/self.change_id;archive.parent.mkdir(parents=True);self.change.rename(archive);self.change=archive
        (self.root/'src/greeting.py').write_text('regressed')
        result=VALIDATOR.validate_repository(self.root,baseline=base)
        self.assertEqual([self.change_id],result['live_archives'])
        self.assertEqual('unable-to-verify',result['status'])

    def test_missing_or_option_baseline_fails(self):
        self.begin();self.baseline()
        for ref in ('not-a-ref','--help'):
            report=VALIDATOR.validate_repository(self.root,baseline=ref)
            self.assertEqual('fail',report['status'])
            self.assertIn('BASELINE',self.codes(report))

    def test_unchanged_archive_is_not_selected(self):
        self.ready();archive=self.root/'specs/archive'/self.change_id;archive.parent.mkdir(parents=True);self.change.rename(archive);self.change=archive;base=self.baseline()
        (self.root/'src/greeting.py').write_text('later valid change')
        result=VALIDATOR.validate_repository(self.root,baseline=base)
        self.assertEqual('pass',result['status']);self.assertEqual([],result['live_archives'])

    def test_deleted_archive_requires_review(self):
        self.ready();archive=self.root/'specs/archive'/self.change_id;archive.parent.mkdir(parents=True);self.change.rename(archive);self.change=archive;base=self.baseline()
        import shutil
        shutil.rmtree(archive)
        result=VALIDATOR.validate_repository(self.root,baseline=base)
        self.assertIn('ARCHIVE_REMOVED',self.codes(result))

    def test_broad_scope_archive_move_preserves_snapshot(self):
        self.data['design']['validation'][0]['inputs'] = {'include': ['.'], 'exclude': ['docs/evidence']}
        self.ready()
        archive = self.root / 'specs/archive' / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        self.assert_status('pass', 'delivery')

    def test_v3_upstream_reopening_retains_superseded_drafts(self):
        self.approved_plan()
        self.data['proposal']['review'].update(state='awaiting-approval', approval=None, revision=2)
        self.data['requirements']['requirements'][0]['statement'] = 'Display a personalized greeting.'
        self.write('requirements')
        self.write('proposal')
        for stage in ('design', 'tasks'):
            self.data[stage]['review'].update(state='superseded', approval=None)
            self.write(stage)
        self.assert_status('pass')
        self.assert_status('fail', 'implementation')

    def test_snapshot_does_not_execute_method_text(self):
        self.data['design']['validation'][0]['method']['procedure'] = 'touch NEVER_EXECUTE'
        self.approved_plan()
        result = subprocess.run([sys.executable, str(VALIDATOR_PATH), '--root', str(self.root), '--change', self.change_id,
                                 '--input-digest', 'CHECK-001'], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertFalse((self.root / 'NEVER_EXECUTE').exists())

    def test_source_digest_cli_matches_qualified_source(self):
        self.add_origin()
        self.begin()
        result = subprocess.run([sys.executable, str(VALIDATOR_PATH), '--root', str(self.root), '--change', 'old-greeting',
                                 '--source-digest'], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual(self.data['proposal']['impact']['items'][0]['source']['requirements_digest'], result.stdout.strip())

    def test_many_to_many_mapping(self):
        self.data['requirements']['requirements'].append({'id': 'REQ-002', 'statement': 'Retain usability.', 'acceptance': ['Repeated action is usable.']})
        self.data['design']['requirements'].append('REQ-002')
        self.data['tasks']['tasks'][0]['requirements'].append('REQ-002')
        first = self.data['design']['validation'][0]
        first['requirements'].append('REQ-002')
        second = copy.deepcopy(first)
        second.update(id='CHECK-002', required=False)
        self.data['design']['validation'].append(second)
        self.data['design']['coverage'][0]['checks'].append('CHECK-002')
        self.data['design']['coverage'].append({'scenario': {'requirement': 'REQ-002', 'scenario': 1},
                                             'applicability': 'required', 'checks': ['CHECK-001', 'CHECK-002']})
        self.ready()
        self.assert_status('pass', 'delivery')

    def test_missing_required_regression_result_is_unverified(self):
        self.add_origin()
        extra = copy.deepcopy(self.data['design']['validation'][0])
        extra['id'] = 'CHECK-002'
        self.data['design']['validation'].append(extra)
        self.data['design']['regression'][0]['checks'] = ['CHECK-002']
        self.ready()
        self.assertIn('ACCEPTANCE_UNVERIFIED', self.codes(self.assert_status('unable-to-verify', 'delivery')))

    def test_duplicate_finding_identity_is_rejected(self):
        self.ready()
        first = self.finding()
        second = copy.deepcopy(first)
        second['category'] = 'contradicts'
        self.data['tasks']['validation']['findings'] = [first, second]
        self.write('tasks')
        self.assertIn('DUPLICATE_ID', self.codes(self.assert_status('fail')))

    def test_origin_in_both_stores_is_rejected(self):
        source = self.add_origin()
        import shutil
        shutil.copytree(source.parent, self.root / 'specs/changes/old-greeting')
        self.ready()
        self.assertIn('DUPLICATE_CHANGE', self.codes(self.assert_status('fail')))

    def test_live_contract_must_resolve_before_approval(self):
        self.add_origin()
        item = self.data['proposal']['impact']['items'][0]
        item['current_contract'] = {'path': 'docs/absent.md', 'locator': '## Contract', 'digest': '0' * 64}
        self.begin()
        self.assertIn('IMPACT_BASELINE', self.codes(self.assert_status('unable-to-verify')))

    def test_ignored_files_are_still_inputs(self):
        self.ready()
        (self.root / '.gitignore').write_text('src/ignored.txt\n')
        (self.root / 'src/ignored.txt').write_text('Relevant ignored content')
        self.assert_status('unable-to-verify', 'delivery')

    def test_duplicate_assessment_and_unknown_fields_fail(self):
        self.ready()
        assessments = self.data['tasks']['validation']['assessments']
        assessments.append(copy.deepcopy(assessments[0]))
        self.write('tasks')
        self.assertIn('ASSESSMENT_REFERENCE', self.codes(self.assert_status('fail')))
        assessments.pop()
        assessments[0]['invented'] = True
        self.write('tasks')
        self.assertIn('SCHEMA', self.codes(self.assert_status('fail')))

    def test_archive_modification_selected_without_code_change(self):
        self.ready()
        archive = self.root / 'specs/archive' / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        base = self.baseline()
        self.data['tasks']['validation']['assessments'] = []
        self.write('tasks')
        result = VALIDATOR.validate_repository(self.root, baseline=base)
        self.assertEqual([self.change_id], result['live_archives'])
        self.assertEqual('unable-to-verify', result['status'])

    def test_historical_inventory_retains_stored_snapshot_consistency(self):
        self.ready()
        archive = self.root / 'specs/archive' / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        self.data['tasks']['validation']['results'][0]['input_digest_before'] = '0' * 64
        self.write('tasks')
        self.assert_status('unable-to-verify')

    def test_historical_v2_bytes_and_scope(self):
        fixture = original.SddValidationTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.ready()
        files = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in fixture.change.glob('*.md')}
        manifest = fixture.root / 'sdd/compatibility.json'
        manifest.write_text(json.dumps({'version': 1, 'historical': {fixture.change_id: {'reason': 'Synthetic historical record.', 'files': files}}, 'in_flight': {}}))
        fixture.assert_status('pass')
        fixture.assert_status('unable-to-verify', 'delivery')
        fixture.body['tasks'] += '\n## Progress\nHistorical byte mutation.\n'
        fixture.write('tasks')
        # The old fixture writer maintains only its synthetic in-flight manifest.
        manifest.write_text(json.dumps({'version': 1, 'historical': {fixture.change_id: {'reason': 'Synthetic historical record.', 'files': files}}, 'in_flight': {}}))
        self.assertIn('HISTORY_CHANGED', self.codes(fixture.assert_status('fail')))

    def test_compatibility_unknown_overlap_and_wrong_version(self):
        fixture = original.SddValidationTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.ready()
        manifest = fixture.root / 'sdd/compatibility.json'
        data = json.loads(manifest.read_text())
        data['in_flight']['absent-change'] = copy.deepcopy(data['in_flight'][fixture.change_id])
        manifest.write_text(json.dumps(data))
        self.assertIn('COMPATIBILITY_MANIFEST', self.codes(fixture.assert_status('fail')))
        data['in_flight'].pop('absent-change')
        data['historical'][fixture.change_id] = {'reason': 'Duplicate exception.', 'files': {n + '.md': '0' * 64 for n in VALIDATOR.ARTIFACTS}}
        manifest.write_text(json.dumps(data))
        self.assertIn('COMPATIBILITY_MANIFEST', self.codes(fixture.assert_status('fail')))
        data['historical'] = {}
        manifest.write_text(json.dumps(data))
        for name in VALIDATOR.ARTIFACTS:
            fixture.data[name]['sdd_version'] = 3
            fixture.write(name)
        fixture.assert_status('fail')


    def test_templates_adopt_v3_with_strict_stage_shapes(self):
        root = VALIDATOR_PATH.parents[2]
        validators = VALIDATOR._schemas()
        for name in VALIDATOR.ARTIFACTS:
            data = VALIDATOR._read_artifact(root / 'sdd/templates' / (name + '.md'))['metadata']
            for stage in data.get('review', {}).get('upstream', {}):
                data['review']['upstream'][stage] = 'a' * 64
            self.assertEqual(3, data['sdd_version'])
            self.assertEqual([], list(validators['v3_' + name].iter_errors(data)))

    def test_changed_executable_flags_are_distinguished(self):
        path = self.root / 'src/greeting.py'
        path.chmod(0o744)
        self.ready()
        path.chmod(0o654)
        self.assert_status('unable-to-verify', 'delivery')

    def test_disjoint_origin_scenarios_can_have_distinct_dispositions(self):
        self.data['requirements']['requirements'][0]['acceptance'].append('Old secondary behavior.')
        source = self.add_origin()
        self.data['requirements']['requirements'][0]['acceptance'].pop()
        second = copy.deepcopy(self.data['proposal']['impact']['items'][0])
        second.update(effect='supersede', reason='Replace only the secondary historical scenario.')
        second['source']['scenarios'] = [2]
        self.data['proposal']['impact']['items'].append(second)
        self.ready()
        self.assert_status('pass', 'delivery')
        second['source']['scenarios'] = [1]
        self.approve('proposal')
        self.approve('design')
        self.approve('tasks')
        self.assertIn('IMPACT_SOURCE', self.codes(self.assert_status('fail')))

    def test_baseline_selection_is_not_hidden_by_explicit_change_filter(self):
        self.ready()
        base = self.baseline()
        archive = self.root / 'specs/archive' / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        (self.root / 'src/greeting.py').write_text('new content')
        # An unknown explicit selection still cannot hide the changed archive.
        result = VALIDATOR.validate_repository(self.root, change_id='another-change', baseline=base)
        self.assertIn(self.change_id, result['checked'])
        self.assertIn('INPUT_STALE', self.codes(result))


    def test_executable_reviewer_walkthrough_preserves_behavioral_boundaries(self):
        from review_sdd_walkthrough import run_walkthrough
        report = run_walkthrough()
        self.assertEqual(7, len(report['steps']))
        self.assertEqual(['pass', 'fail', 'fail'], [r['outcome'] for r in report['steps'][0]['checks']])
        self.assertEqual('pass', report['steps'][1]['validator']['status'])
        self.assertEqual('unable-to-verify', report['steps'][5]['validator']['status'])

    def test_snapshot_can_refresh_execution_after_reapproved_task_plan(self):
        self.ready()
        self.data['tasks']['tasks'][0]['description'] = 'Revised synthetic deliverable after renewed review.'
        self.approve('tasks')
        self.assertIn('VALIDATION_STALE', self.codes(self.assert_status('unable-to-verify', 'delivery')))
        result = subprocess.run([sys.executable, str(VALIDATOR_PATH), '--root', str(self.root), '--change', self.change_id,
                                 '--input-digest', 'CHECK-001'], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout)
        # Taking a digest alone never changes the old result or grants readiness.
        self.assert_status('unable-to-verify', 'delivery')

    def test_historical_scope_conflicts_still_fail_without_reading_old_inputs(self):
        self.ready()
        archive = self.root / 'specs/archive' / self.change_id
        archive.parent.mkdir(parents=True)
        self.change.rename(archive)
        self.change = archive
        self.data['design']['validation'][0]['outputs'] = ['src']
        self.approve('design')
        self.approve('tasks')
        self.assertIn('INPUT_SCOPE', self.codes(self.assert_status('fail')))

    def prepare_archive(self):
        self.data['tasks']['closure'] = 'prepared'
        self.write('tasks')
        archive = self.root / 'specs/archive' / self.change_id
        archive.parent.mkdir(parents=True, exist_ok=True)
        self.change.rename(archive)
        self.change = archive

    def test_pr_submission_rejects_completed_active_dossier(self):
        self.ready()
        self.assert_status('pass', 'delivery')
        report = VALIDATOR.validate_repository(self.root, change_id=self.change_id, require_archive=True)
        self.assertEqual('fail', report['status'])
        self.assertIn('ARCHIVE_REQUIRED', self.codes(report))
        self.assertIn('CLOSURE_REQUIRED', self.codes(report))

    def test_pr_submission_requires_location_and_prepared_closure(self):
        self.ready()
        self.data['tasks']['closure'] = 'prepared'
        self.write('tasks')
        report = VALIDATOR.validate_repository(self.root, change_id=self.change_id, require_archive=True)
        self.assertIn('ARCHIVE_REQUIRED', self.codes(report))
        self.prepare_archive()
        self.data['tasks']['closure'] = 'active'
        self.write('tasks')
        report = VALIDATOR.validate_repository(self.root, change_id=self.change_id, require_archive=True)
        self.assertIn('CLOSURE_REQUIRED', self.codes(report))

    def test_pr_submission_uses_live_delivery_without_git(self):
        self.ready()
        self.prepare_archive()
        report = VALIDATOR.validate_repository(self.root, change_id=self.change_id, require_archive=True)
        self.assertEqual('pass', report['status'], report)
        (self.root / 'src/greeting.py').write_text('changed after checks')
        report = VALIDATOR.validate_repository(self.root, change_id=self.change_id, require_archive=True)
        self.assertEqual('unable-to-verify', report['status'])
        self.assertIn('INPUT_STALE', self.codes(report))

    def test_pr_submission_still_requires_completion_and_results(self):
        self.approved_plan()
        self.prepare_archive()
        report = VALIDATOR.validate_repository(self.root, change_id=self.change_id, require_archive=True)
        self.assertEqual('fail', report['status'])
        self.assertIn('TASK_INCOMPLETE', self.codes(report))
        self.assertIn('VALIDATION_MISSING', self.codes(report))

    def test_pr_baseline_cannot_skip_changed_active_dossier(self):
        self.begin()
        base = self.baseline()
        self.approved_plan()
        self.complete()
        self.passing_evidence()
        report = VALIDATOR.validate_repository(self.root, baseline=base, require_archive=True)
        self.assertEqual([self.change_id], report['archive_required'])
        self.assertIn('ARCHIVE_REQUIRED', self.codes(report))
        self.prepare_archive()
        report = VALIDATOR.validate_repository(self.root, baseline=base, require_archive=True)
        self.assertEqual('pass', report['status'], report)

    def test_draft_planning_inventory_does_not_require_archival(self):
        self.begin()
        base = self.baseline()
        self.body['proposal'] += '\nFurther planning detail.\n'
        self.write('proposal')
        report = VALIDATOR.validate_repository(self.root, baseline=base)
        self.assertEqual('pass', report['status'])
        self.assertEqual([], report['archive_required'])
        report = VALIDATOR.validate_repository(self.root, baseline=base, require_archive=True)
        self.assertEqual('fail', report['status'])

    def test_pr_submission_missing_or_empty_selection_fails(self):
        self.ready()
        report = VALIDATOR.validate_repository(self.root, require_archive=True)
        self.assertIn('ARCHIVE_SELECTION', self.codes(report))
        base = self.baseline()
        report = VALIDATOR.validate_repository(self.root, baseline=base, require_archive=True)
        self.assertIn('ARCHIVE_SELECTION', self.codes(report))
        report = VALIDATOR.validate_repository(self.root, baseline='missing-base', require_archive=True)
        self.assertIn('BASELINE', self.codes(report))

    def test_pr_submission_cannot_delete_active_dossier_to_avoid_guard(self):
        self.begin()
        base = self.baseline()
        import shutil
        shutil.rmtree(self.change)
        report = VALIDATOR.validate_repository(self.root, baseline=base, require_archive=True)
        self.assertIn('ARCHIVE_REQUIRED', self.codes(report))

    def test_pr_baseline_leaves_unchanged_active_planning_in_inventory(self):
        self.ready()
        other = self.root / 'specs/changes/other-plan'
        other.mkdir()
        import yaml
        for name in ('proposal', 'requirements'):
            data = copy.deepcopy(self.data[name])
            data['change'] = 'other-plan'
            if name == 'proposal':
                data['review'] = self.review()
            (other / (name + '.md')).write_text('---\n' + yaml.safe_dump(data) + '---\n# Other draft\n')
        base = self.baseline()
        self.prepare_archive()
        report = VALIDATOR.validate_repository(self.root, baseline=base, require_archive=True)
        self.assertEqual('pass', report['status'], report)
        self.assertEqual([self.change_id], report['archive_required'])
        self.assertIn('other-plan', report['checked'])

    def test_pr_cli_requires_archive_and_cannot_be_digest_only(self):
        self.ready()
        args = [sys.executable, str(VALIDATOR_PATH), '--root', str(self.root), '--change', self.change_id, '--require-archive']
        result = subprocess.run(args, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
        self.assertIn('ARCHIVE_REQUIRED', result.stdout)
        self.prepare_archive()
        result = subprocess.run(args, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout)
        result = subprocess.run(args + ['--digest', 'tasks'], capture_output=True, text=True)
        self.assertNotEqual(0, result.returncode)

    def test_ci_draft_transition_dispatches_archive_guard(self):
        import yaml
        workflow = yaml.load((VALIDATOR_PATH.parents[2] / '.github/workflows/validate.yml').read_text(), Loader=yaml.BaseLoader)
        events = workflow['on']['pull_request']['types']
        self.assertIn('ready_for_review', events)
        self.assertIn('converted_to_draft', events)
        steps = workflow['jobs']['structural-validation']['steps']
        step = next(item for item in steps if item.get('name') == 'Validate repository contracts')
        self.assertIn('github.event.pull_request.draft', step['env']['SDD_REQUIRE_ARCHIVE'])
        stub = self.root / 'scripts/validate/run.sh'
        stub.parent.mkdir(parents=True)
        stub.write_text('#!/bin/sh\nprintf "%s\\n" "$@" > observed-arguments.txt\n')
        stub.chmod(0o755)
        for flag in ('true', 'false'):
            result = subprocess.run(['bash', '-e', '-c', step['run']], cwd=self.root,
                                    env={**os.environ, 'SDD_BASELINE': 'trusted-test-base', 'SDD_REQUIRE_ARCHIVE': flag}, capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)
            arguments = (self.root / 'observed-arguments.txt').read_text().splitlines()
            self.assertEqual(['--baseline', 'trusted-test-base'] + (['--require-archive'] if flag == 'true' else []), arguments)


if __name__ == '__main__':
    unittest.main()
