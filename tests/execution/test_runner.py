import copy
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
import yaml
from support import PACKAGE, runner, contract, write_config, simple_test


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name); self.config=write_config(self.root); simple_test(self.root)
    def save(self):
        (self.root/'.versat/validation.yaml').write_text(yaml.safe_dump(self.config))
    def test_full_and_targeted_have_different_readiness(self):
        full,path=runner.run_project(self.root)
        self.assertEqual(full['result'],'pass'); self.assertTrue(full['readiness'])
        self.assertEqual(full['suites'][0]['counts']['executed'],1)
        targeted,new=runner.run_project(self.root,['unit'])
        self.assertFalse(targeted['readiness']); self.assertNotEqual(path,new)
        self.assertTrue((path/'result.json').exists())
    def test_existing_failure_is_not_hidden_by_new_success(self):
        (self.root/'tests/test_regression.py').write_text('import unittest\nclass Regression(unittest.TestCase):\n def test_duplicate(self): self.assertEqual(2,1)\n')
        result,_=runner.run_project(self.root)
        self.assertEqual(result['result'],'fail'); self.assertEqual(result['suites'][0]['counts']['failed'],1)
    def test_optional_unavailable_suite_does_not_block_required_run(self):
        optional=copy.deepcopy(self.config['suites'][0]); optional.update(id='optional',kind='check',result='exit-code',argv=['missing-optional-tool'])
        self.config['suites'].append(optional); self.save()
        self.assertEqual(runner.run_project(self.root)[0]['result'],'pass')
        with self.assertRaises(FileNotFoundError): runner.run_project(self.root,['optional'])
    def test_mixed_subtest_skip_and_execution_counts_cases(self):
        for action,expected in [('self.assertTrue(True)','pass'),('self.fail("defect")','fail')]:
            (self.root/'tests/test_sample.py').write_text('import unittest\nclass Case(unittest.TestCase):\n def test_subtests(self):\n  with self.subTest(i=0): self.skipTest("fixture")\n  with self.subTest(i=1): '+action+'\n')
            result,_=runner.run_project(self.root)
            self.assertEqual(result['result'],expected)
            self.assertEqual(result['suites'][0]['counts']['executed'],1)
    def test_empty_and_all_skipped_are_failures(self):
        (self.root/'tests/test_sample.py').unlink()
        for source in ['', 'import unittest\n@unittest.skip("fixture")\nclass Case(unittest.TestCase):\n def test_skip(self): pass\n']:
            (self.root/'tests/test_sample.py').write_text(source)
            result,_=runner.run_project(self.root)
            self.assertEqual(result['result'],'fail')
    def test_bad_configuration_never_launches(self):
        variants=[]
        c=copy.deepcopy(self.config); c['required_suites']=['missing']; variants.append(c)
        c=copy.deepcopy(self.config); c['suites']*=2; variants.append(c)
        c=copy.deepcopy(self.config); c['suites'][0]['result']='exit-code'; variants.append(c)
        c=copy.deepcopy(self.config); c['suites'][0]['argv']=['{unknown}']; variants.append(c)
        c=copy.deepcopy(self.config); c['suites'][0]['environment']=['CODEX_API_KEY']; variants.append(c)
        for c in variants:
            with self.subTest(config=c):
                (self.root/'.versat/validation.yaml').write_text(yaml.safe_dump(c))
                with self.assertRaises(ValueError): runner.run_project(self.root)
        self.assertFalse((self.root/'.versat/validation-runs').exists())
    def test_duplicate_yaml_keys_rejected(self):
        path=self.root/'.versat/validation.yaml'; path.write_text(path.read_text()+'schema_version: 1\n')
        with self.assertRaises(ValueError): contract.load_config(self.root)
    def test_missing_runtime_is_unverified_cli(self):
        self.config['suites'][0].update(kind='check',result='exit-code',argv=['missing-versat-executable']); self.save()
        p=subprocess.run([sys.executable,str(PACKAGE/'scripts/testing/run.py'),'run','--root',str(self.root)],capture_output=True,text=True)
        self.assertEqual(p.returncode,2); self.assertEqual(json.loads(p.stdout)['result'],'unverified')
    def test_timeout_is_bounded_and_recorded(self):
        self.config['suites'][0].update(kind='check',result='exit-code',argv=['{python}','-c','import time; time.sleep(20)'],timeout_seconds=1); self.save()
        result,_=runner.run_project(self.root)
        self.assertEqual(result['result'],'fail'); self.assertEqual(result['suites'][0]['reason'],'timeout')
    def test_input_mutation_invalidates_run(self):
        self.config['suites'][0].update(kind='check',result='exit-code',argv=['{python}','-c','from pathlib import Path; Path("src/new.py").write_text("new")']); self.save()
        result,_=runner.run_project(self.root)
        self.assertEqual(result['result'],'fail'); self.assertFalse(result['fresh'])
    def test_safe_output_and_snapshot_exclusion(self):
        for value in ['../escape','/tmp/escape','tests/evidence']:
            with self.subTest(value=value), self.assertRaises(ValueError): runner.run_project(self.root,output=value)
        outside=self.root/'outside'; outside.mkdir()
        (self.root/'linked').symlink_to(outside,target_is_directory=True)
        with self.assertRaises(ValueError): runner.run_project(self.root,output='linked/output')
    def test_argument_data_is_not_shell_expanded(self):
        self.config['suites'][0].update(kind='check',result='exit-code',argv=['{python}','-c','import sys; print(sys.argv[1])','$(touch marker)']); self.save()
        result,path=runner.run_project(self.root)
        self.assertEqual(result['result'],'pass'); self.assertFalse((self.root/'marker').exists())
        self.assertIn('$(touch marker)',(path/'unit/stdout.txt').read_text())
    def test_bad_report_and_nonzero_exit_never_pass(self):
        counts={'schema_version':1,'collected':1,'executed':1,'skipped':0,'failed':0,'errors':0}
        (self.root/'scripts').mkdir()
        for output,code in [('{}',0),(json.dumps(counts),3)]:
            (self.root/'scripts/report.py').write_text(f'import pathlib,sys\npathlib.Path(sys.argv[1]).write_text({output!r})\nsys.exit({code})\n')
            self.config['suites'][0].update(result='json-v1',argv=['{python}','scripts/report.py','{report}']); self.save()
            result,_=runner.run_project(self.root); self.assertEqual(result['result'],'fail')
    def test_log_cap_and_environment_redaction(self):
        self.config['suites'][0].update(kind='check',result='exit-code',argv=['{python}','-c','import os; print(os.getenv("TEST_SECRET", "absent")); print("x"*2000000)']); self.save()
        from unittest.mock import patch
        with patch.dict(os.environ,{'TEST_SECRET':'sensitive'}): result,path=runner.run_project(self.root)
        self.assertEqual(result['result'],'pass'); self.assertTrue(result['suites'][0]['truncated']['stdout'])
        self.assertLessEqual((path/'unit/stdout.txt').stat().st_size,1024*1024)
        self.assertNotIn('sensitive',(path/'unit/stdout.txt').read_text())
    def test_failed_suite_does_not_skip_independent_required_suite(self):
        self.config['suites']=[{'id':name,'kind':'check','argv':['{python}','-c',code], 'cwd':'.','timeout_seconds':5,'result':'exit-code'} for name,code in [('unit','raise SystemExit(1)'),('other','print("observed")')]]
        self.config['required_suites']=['unit','other']; self.save()
        result,_=runner.run_project(self.root)
        self.assertEqual([s['result'] for s in result['suites']],['fail','pass'])
    def test_inspect_does_not_execute(self):
        self.config['suites'][0].update(kind='check',result='exit-code',argv=['{python}','-c','raise RuntimeError("must not execute")']); self.save()
        runner.inspect(self.root,contract.load_config(self.root),self.config['inputs'])
        self.assertFalse((self.root/'.versat/validation-runs').exists())
    def test_interrupt_stops_descendants_and_keeps_attempt(self):
        self.config['suites'][0].update(kind='check',result='exit-code',argv=['{python}','-c','import time; print("started",flush=True); time.sleep(30)']); self.save()
        p=subprocess.Popen([sys.executable,str(PACKAGE/'scripts/testing/run.py'),'run','--root',str(self.root)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.addCleanup(lambda: p.poll() is None and p.kill())
        deadline=time.monotonic()+10
        while time.monotonic()<deadline:
            logs=list(self.root.glob('.versat/validation-runs/*/unit/stdout.txt'))
            if logs: break
            time.sleep(.05)
        p.send_signal(signal.SIGINT)
        stdout,stderr=p.communicate(timeout=10)
        self.assertEqual(p.returncode,1,(stdout,stderr))
        reports=list(self.root.glob('.versat/validation-runs/*/result.json'))
        self.assertEqual(json.loads(reports[0].read_text())['suites'][0]['reason'],'interrupted')

    def test_executable_symlink_preserves_virtual_environment(self):
        import venv
        from common import execute
        virtual = self.root/'runtime'
        venv.EnvBuilder(with_pip=False).create(virtual)
        interpreter = virtual/'bin/python'
        site = next((virtual/'lib').glob('python*/site-packages'))
        (site/'only_in_this_environment.py').write_text('VALUE = "venv-preserved"\n')
        output = self.root/'probe'; output.mkdir()
        result = execute([str(interpreter), '-c', 'from only_in_this_environment import VALUE; print(VALUE)'], self.root, output, 10)
        self.assertEqual(result['result'], 'pass', (output/'stderr.txt').read_text())
        self.assertIn('venv-preserved', (output/'stdout.txt').read_text())
