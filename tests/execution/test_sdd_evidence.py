import copy
import json
from pathlib import Path
import shutil
import sys
import unittest
from support import PACKAGE, runner, sdd, write_config, simple_test
sys.path.insert(0,str(PACKAGE/'tests/validators'))
import test_sdd_v3


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.fixture=test_sdd_v3.V3Tests('test_partial_v3_planning_and_all_gate_states')
        self.fixture.setUp(); self.addCleanup(self.fixture.doCleanups)
        self.root=self.fixture.root
        self.config=write_config(self.root); simple_test(self.root)
        self.fixture.data['design']['validation'][0]['inputs']=self.config['inputs']
        self.fixture.data['design']['validation'][0]['method']['procedure']='Run full configured unit suite; observe greeting and retained behavior.'
        self.fixture.approved_plan()
    def run_check(self,**kwargs):
        return runner.run_project(self.root,change=self.fixture.change_id,check_id='CHECK-001',**kwargs)
    def test_actual_result_exports_without_editing_dossier(self):
        before={p.name:p.read_bytes() for p in self.fixture.change.iterdir()}
        result,path=self.run_check()
        self.assertEqual(result['result'],'pass')
        fragment=json.loads((path/'sdd-result.json').read_text())
        self.assertEqual(fragment['plan_digest'],sdd.stage_digest(self.fixture.change,'tasks'))
        self.assertTrue(fragment['result']['context']['observed'])
        self.assertEqual(before,{p.name:p.read_bytes() for p in self.fixture.change.iterdir()})
    def test_failed_assertion_is_exported_as_failed(self):
        simple_test(self.root,'self.fail("real defect")')
        result,path=self.run_check()
        self.assertEqual(result['result'],'fail')
        self.assertEqual(json.loads((path/'sdd-result.json').read_text())['result']['result'],'fail')
    def test_stale_approval_or_manual_method_cannot_launch(self):
        self.fixture.body['design']+='\nUnapproved design edit.\n'; self.fixture.write('design')
        with self.assertRaises(ValueError): self.run_check()
        self.fixture.body['design']=self.fixture.body['design'].replace('\nUnapproved design edit.\n','')
        self.fixture.data['design']['validation'][0]['method']={'kind':'manual','procedure':'Observe manually.','reason':'manual fixture'}
        self.fixture.approved_plan()
        with self.assertRaises(ValueError): self.run_check()
    def test_targeted_or_wrong_context_export_is_rejected(self):
        with self.assertRaises(ValueError): self.run_check(selected=['unit'])
        with self.assertRaises(ValueError): self.run_check(context='ci')
    def test_mutating_input_withholds_passing_fragment(self):
        simple_test(self.root,'__import__("pathlib").Path("src/changed.txt").write_text("changed")')
        result,path=self.run_check()
        self.assertEqual(result['result'],'fail'); self.assertFalse((path/'sdd-result.json').exists())
    def test_mutating_task_plan_withholds_fragment(self):
        simple_test(self.root,f'__import__("pathlib").Path("specs/changes/{self.fixture.change_id}/tasks.md").open("a").write("\\nChanged task scope.\\n")')
        result,path=self.run_check()
        self.assertEqual(result['result'],'fail'); self.assertFalse((path/'sdd-result.json').exists())
    def test_configuration_must_be_in_approved_scope(self):
        self.fixture.data['design']['validation'][0]['inputs']['include'].remove('.versat/validation.yaml')
        self.fixture.approved_plan()
        with self.assertRaises(ValueError): self.run_check()
    def test_archive_move_keeps_evidence_and_check_digest(self):
        result,path=self.run_check()
        before=sdd.input_digest(self.root,self.fixture.change,self.fixture.data['design']['validation'][0])
        archived=self.root/'specs/archive'/self.fixture.change_id; archived.parent.mkdir(parents=True)
        shutil.move(self.fixture.change,archived)
        after=sdd.input_digest(self.root,archived,self.fixture.data['design']['validation'][0])
        self.assertEqual(before,after)
        self.assertTrue((path/'sdd-result.json').is_file())
    def test_old_results_are_not_relabelled_on_rerun(self):
        first,path=self.run_check()
        original=(path/'sdd-result.json').read_bytes()
        (self.root/'src/greeting.py').write_text('def greet(): return "updated"\n')
        second,new=self.run_check()
        self.assertNotEqual(first['input_digest_before'],second['input_digest_before'])
        self.assertEqual(original,(path/'sdd-result.json').read_bytes())
        self.assertNotEqual(path,new)
