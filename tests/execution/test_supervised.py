"""Test deterministic scenario helpers; these tests never stand in for agent behavior."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
import yaml
from support import PACKAGE, runner, sdd
sys.path.insert(0, str(PACKAGE/'tests/skills'))
import fixtures
import verification


class SupervisedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def fixture(self, case='adequate-reuse'):
        project = self.root/case
        fixtures.prepare(project, case)
        return project

    def test_all_fixtures_preserve_valid_plans_or_actual_stale_evidence(self):
        for case in fixtures.CASES:
            with self.subTest(case=case):
                project = self.fixture(case)
                result = sdd.validate_repository(project, 'planning' if case == 'new-intent' else 'implementation')
                if case == 'stale-evidence':
                    self.assertEqual({f['code'] for f in result['findings']}, {'INPUT_STALE'})
                    self.assertTrue(verification.reports(project))
                else:
                    self.assertEqual(result['status'], 'pass', result)
                lock = yaml.safe_load((project/'.versat/standards.lock').read_text())
                self.assertTrue(lock['harness']['commit'].startswith('development-snapshot:'))

    def test_fixture_does_not_overwrite_existing_work_or_accept_unknown_case(self):
        project = self.fixture()
        before = verification.snapshot(project)
        with self.assertRaises(ValueError): fixtures.prepare(project, 'adequate-reuse')
        self.assertEqual(before, verification.snapshot(project))
        with self.assertRaises(ValueError): fixtures.prepare(self.root/'bad', 'unknown')

    def test_plan_rewrite_is_detected_even_after_rehashing_approval(self):
        project = self.fixture()
        before = verification.snapshot(project)
        plan = verification.plan_identity(project)
        path = project/'specs/changes/payment-validation/tasks.md'
        path.write_text(path.read_text().replace('TASK-001', 'TASK-002'))
        artifact = sdd._read_artifact(path)
        artifact['metadata']['review']['approval']['digest'] = sdd.stage_digest(path.parent, 'tasks')
        fixtures.write_artifact(path.parent, 'tasks', artifact['metadata'], artifact['body'])
        self.assertFalse(verification.changes(project, before, plan)['plan_unchanged'])

    def test_source_and_execution_control_changes_are_visible(self):
        project = self.fixture()
        before = verification.snapshot(project)
        (project/'src/payment.py').write_text('changed')
        (project/'.versat/validation.yaml').write_text('changed')
        observed = verification.changes(project, before)
        self.assertFalse(observed['source_tests_unchanged'])
        self.assertFalse(observed['controls_unchanged'])

    def test_final_narrative_cannot_replace_runner_observations(self):
        with self.assertRaises(ValueError): verification.validate_report({'result':'pass', 'message':'Everything passed'})
        project = self.fixture()
        self.assertEqual(verification.reports(project), [])
        runner.run_project(project, change='payment-validation', check_id='CHECK-001')
        self.assertEqual(len(verification.reports(project)), 1)

    def test_independent_replay_and_mutations_preserve_original_and_detect_defects(self):
        project = self.fixture()
        baseline = verification.snapshot(project)
        result = verification.replay(project, self.root/'baseline')
        self.assertEqual(result['report']['result'], 'pass', result)
        # Replay creates its own output; compare the source/tests and original dossier.
        after_replay = verification.snapshot(project)
        mutants = verification.mutation_replays(project, self.root/'mutants')
        self.assertTrue(all(r['report']['result'] == 'fail' for r in mutants.values()), mutants)
        self.assertEqual(after_replay, verification.snapshot(project))
        self.assertTrue(verification.changes(project, baseline)['source_tests_unchanged'])

    def test_insufficient_coverage_does_not_detect_all_defects(self):
        project = self.fixture('missing-coverage')
        mutants = verification.mutation_replays(project, self.root/'mutants')
        self.assertEqual(mutants['duplicate']['report']['result'], 'fail')
        self.assertEqual(mutants['boundary']['report']['result'], 'pass')
        self.assertEqual(mutants['empty-key']['report']['result'], 'pass')

    def test_failed_replay_is_retained_as_failure(self):
        project = self.fixture('validation-only')
        result = verification.replay(project, self.root/'failure')
        self.assertEqual(result['report']['result'], 'fail')
        self.assertEqual(json.loads((self.root/'failure/replay.json').read_text())['process']['exit_code'], 1)
        self.assertTrue((self.root/'failure/stderr.txt').exists())

    def test_replay_deadline_and_missing_observations_stay_nonpassing(self):
        project = self.fixture()
        (project/'tests/test_payment.py').write_text('import time\ntime.sleep(30)\n')
        result = verification.replay(project, self.root/'timeout', timeout=.2)
        self.assertEqual(result['process']['reason'], 'timeout')
        self.assertIsNone(result['report'])
        self.assertLess(result['process']['duration_seconds'], 4)

    def test_replay_rejects_links_and_output_overlap(self):
        project = self.fixture()
        with self.assertRaises(ValueError): verification.replay(project, project/'output')
        (project/'src/link.py').symlink_to(project/'src/payment.py')
        with self.assertRaises(ValueError): verification.replay(project, self.root/'replay')
