import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import yaml
from support import PACKAGE, runner, write_config
import provider

GOOD='''def charge(seen, key, amount):
    if not key or amount <= 0:
        raise ValueError("key and positive amount required")
    if key in seen:
        return False
    seen.add(key)
    return True
'''
TESTS='''import unittest
from src.payment import charge
class Payment(unittest.TestCase):
    def test_new(self): self.assertTrue(charge(set(), 'a', 1))
    def test_duplicate(self):
        seen=set(); charge(seen,'a',1)
        self.assertFalse(charge(seen,'a',1))
    def test_boundary(self):
        with self.assertRaises(ValueError): charge(set(),'a',0)
    def test_error(self):
        with self.assertRaises(ValueError): charge(set(),'',1)
'''


class ConsumerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        shutil.copytree(PACKAGE/'project-templates/base',self.root,dirs_exist_ok=True)
        shutil.copytree(PACKAGE/'project-templates/artifacts/validation/python',self.root,dirs_exist_ok=True)
        (self.root/'src').mkdir(); (self.root/'tests').mkdir()
        (self.root/'src/payment.py').write_text(GOOD)
        (self.root/'tests/test_payment.py').write_text(TESTS)
    def test_reference_and_seeded_regressions(self):
        baseline,_=runner.run_project(self.root); self.assertEqual(baseline['result'],'pass')
        for mutant in [GOOD.replace('if key in seen:','if False:'),GOOD.replace('amount <= 0','amount < 0'),GOOD.replace('not key or ','')]:
            (self.root/'src/payment.py').write_text(mutant)
            result,_=runner.run_project(self.root); self.assertEqual(result['result'],'fail')
        (self.root/'src/payment.py').write_text(GOOD)
        result,_=runner.run_project(self.root); self.assertEqual(result['result'],'pass')
    def test_adequate_coverage_reuse_and_missing_history(self):
        tests=self.root/'tests/test_payment.py'; original=tests.read_bytes()
        runner.run_project(self.root); runner.run_project(self.root)
        self.assertEqual(tests.read_bytes(),original)
        tests.write_text(TESTS.split('    def test_duplicate')[0])
        (self.root/'src/payment.py').write_text(GOOD.replace('if key in seen:','if False:'))
        insufficient,_=runner.run_project(self.root); self.assertEqual(insufficient['result'],'pass')
        # Full command success cannot establish semantic coverage. Add the missing retained check.
        tests.write_text(TESTS)
        covered,_=runner.run_project(self.root); self.assertEqual(covered['result'],'fail')
    def test_custom_command_preserved_and_rollback(self):
        config_path=self.root/'.versat/validation.yaml'; original=config_path.read_bytes()
        config=yaml.safe_load(original)
        config['suites'][0]['argv']+=['-p','test_payment.py']; config_path.write_text(yaml.safe_dump(config))
        expected=config_path.read_bytes()
        result,_=runner.run_project(self.root)
        self.assertEqual(result['result'],'pass'); self.assertEqual(config_path.read_bytes(),expected)
        config_path.write_bytes(original)
        self.assertEqual(runner.run_project(self.root)[0]['result'],'pass')
    def test_provider_rejects_unresolved_pin(self):
        with self.assertRaises(ValueError): provider.verify(self.root)
    def test_manual_and_replacement_dispositions_require_review(self):
        # Reuse the canonical SDD fixture so this integration does not invent a second policy.
        sys.path.insert(0,str(PACKAGE/'tests/validators'))
        import test_sdd_v3
        for method in ('test_manual_check_needs_reason_and_observed_result','test_supersession_uses_local_replacement','test_unapproved_exclusion_is_rejected'):
            case=test_sdd_v3.V3Tests(method)
            result=unittest.TestResult(); case.run(result)
            self.assertTrue(result.wasSuccessful(),(method,result.errors,result.failures))
    def test_clean_provider_resolves_canonical_index(self):
        with tempfile.TemporaryDirectory() as directory:
            package=Path(directory)
            for name in ['standards','schemas','scripts/testing','validators','sdd']:
                shutil.copytree(PACKAGE/name,package/name)
            shutil.copy(PACKAGE/'VERSION',package/'VERSION')
            def git(*args): return subprocess.check_output(['git','-C',str(package),*args],text=True).strip()
            git('init','-q'); git('add','.')
            git('-c','user.name=Synthetic','-c','user.email=fixture@example.invalid','-c','commit.gpgsign=false','commit','-qm','Synthetic provider')
            identity={'schema_version':1,'project':{'name':'fixture','description':'Synthetic consumer','profile':'software','domain':'finance','owner':'Synthetic','visibility':'private','criticality':'medium'},'technologies':['python']}
            index=yaml.safe_load((package/'standards/index.yaml').read_text()); paths=set(index['core']['always']+index['profiles']['software']+index['domains']['finance']+index['criticality']['medium']+index['technologies']['python'])
            version=(package/'VERSION').read_text().strip()
            lock={'schema_version':1,'harness':{'version':version,'commit':git('rev-parse','HEAD')},'resolved_at':'synthetic-fixture','standards':[{'path':p,'version':version,'digest':hashlib.sha256((package/'standards'/p).read_bytes()).hexdigest()} for p in sorted(paths)]}
            (self.root/'.versat/project.yaml').write_text(yaml.safe_dump(identity)); (self.root/'.versat/standards.lock').write_text(yaml.safe_dump(lock))
            self.assertEqual(provider.verify(self.root,package)['result'],'pass')
            result=subprocess.run(['bash',str(self.root/'scripts/validate/run.sh')],
                                  env={**os.environ,'VERSAT_HARNESS_ROOT':str(package),'PYTHON':sys.executable},
                                  capture_output=True,text=True)
            self.assertEqual(result.returncode,0,(result.stdout,result.stderr))
            self.assertEqual(json.loads(result.stdout.splitlines()[-1])['scope'],'full')
            (package/'standards/core/testing.md').write_text('changed')
            with self.assertRaises(ValueError): provider.verify(self.root,package)
