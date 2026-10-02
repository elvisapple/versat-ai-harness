#!/usr/bin/env python3
"""Execute disposable behavior for a recorded reviewer walkthrough, not an agent eval.

Synthetic approvals exercise record boundaries; they never represent human approval.
Run explicitly with --output /path/to/report.json. No network or production data.
"""
from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

from test_sdd_v3 import V3Tests
from test_sdd import VALIDATOR, VALIDATOR_PATH

BROKEN = '''balances = {}
AUDIT_DISABLED = True

def pay(request_id, amount):
    balances[request_id] = balances.get(request_id, 0) + amount
    return balances[request_id]

def export_all_customers():
    return ["synthetic-customer"]
'''
FIXED = '''balances = {}

def pay(request_id, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if request_id not in balances:
        balances[request_id] = amount
    return balances[request_id]
'''
TESTS = '''import unittest
from src import payments

class Payments(unittest.TestCase):
    def setUp(self):
        payments.balances.clear()

    def test_success(self):
        self.assertEqual(10, payments.pay("synthetic-1", 10))

    def test_error_boundary(self):
        for amount in (-1, 0):
            with self.assertRaises(ValueError):
                payments.pay("synthetic-1", amount)
        self.assertEqual({}, payments.balances)

    def test_duplicate(self):
        payments.pay("synthetic-1", 10)
        self.assertEqual(10, payments.pay("synthetic-1", 10))
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_walkthrough():
    fixture = V3Tests()
    fixture.setUp()
    report = {'kind': 'Executed local reviewer walkthrough; not an autonomous-agent evaluation',
              'environment': {'python': platform.python_version(), 'platform': platform.platform()},
              'synthetic_approval_notice': 'All disposable approval records are synthetic test data.', 'steps': []}
    try:
        source = fixture.root / 'src/payments.py'
        source.write_text(BROKEN)
        (fixture.root / 'tests/test_payments.py').write_text(TESTS)
        requirements = fixture.data['requirements']['requirements'][0]
        requirements.update(statement='Process positive payments, reject invalid amounts and retain duplicate prevention.',
                            acceptance=['A positive payment succeeds.', 'Negative and zero amounts raise without modifying balances.'])
        fixture.body['proposal'] = '# Proposal\n\n## Baseline\nDuplicate requests charge once. Audit must remain enabled; customer export is out of scope.\n'
        fixture.add_origin('prevent-duplicates')
        origin = fixture.root / 'specs/archive/prevent-duplicates/requirements.md'
        historic = VALIDATOR._read_artifact(origin)
        historic['metadata']['requirements'][0].update(statement='Prevent duplicate payments.', acceptance=['Submitting the same request twice charges once.'])
        import yaml
        origin.write_text('---\n' + yaml.safe_dump(historic['metadata'], sort_keys=False) + '---\n# Synthetic historical origin\n')
        fixture.data['proposal']['impact']['items'][0]['source']['requirements_digest'] = VALIDATOR.sdd_assurance.requirements_digest(VALIDATOR, VALIDATOR._read_artifact(origin))
        check = fixture.data['design']['validation'][0]
        check.update(description='Observe positive synthetic payment.', method={'kind': 'automated', 'procedure': 'python -m unittest discover -s tests -p test_payments.py -k success; expect one accepted payment.'})
        for identifier, description, selector in [('CHECK-002', 'Reject negative and zero amounts.', 'error_boundary'),
                                                   ('CHECK-003', 'Reuse maintained duplicate prevention.', 'duplicate')]:
            item = copy.deepcopy(check)
            item.update(id=identifier, description=description,
                        method={'kind': 'automated', 'procedure': f'python -m unittest discover -s tests -p test_payments.py -k {selector}; expect contract assertions to pass.'})
            fixture.data['design']['validation'].append(item)
        fixture.data['design']['coverage'].append({'scenario': {'requirement': 'REQ-001', 'scenario': 2}, 'applicability': 'required', 'checks': ['CHECK-002']})
        fixture.data['design']['regression'][0]['checks'] = ['CHECK-003']
        fixture.approved_plan()
        fixture.complete()
        evidence = fixture.root / 'docs/evidence/payment.txt'
        evidence.parent.mkdir(parents=True)
        evidence.write_text('Local synthetic payment walkthrough.\n')
        val = fixture.data['tasks']['validation']
        val['plan_digest'] = fixture.digest('tasks')
        report['approved_plan_digests'] = {stage: fixture.digest(stage) for stage in VALIDATOR.STAGES}
        report['original_implementation'] = BROKEN
        report['maintained_test'] = TESTS
        report['origin_requirements'] = origin.read_text()
        test_hash = digest(fixture.root / 'tests/test_payments.py')

        def command(args):
            result = subprocess.run(args, cwd=fixture.root, capture_output=True, text=True,
                                    env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
            return {'command': [str(a).replace(str(fixture.root), '<fixture>') for a in args],
                    'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}

        def snapshot(identifier):
            result = command([sys.executable, str(VALIDATOR_PATH), '--root', str(fixture.root), '--change', fixture.change_id, '--input-digest', identifier])
            assert result['exit'] == 0, result
            return result['stdout'].strip()

        def observe(label):
            results, observations, assessments = [], [], []
            for item, selector, obligation in zip(fixture.data['design']['validation'], ['success', 'error_boundary', 'duplicate'],
                    [{'local': {'requirement': 'REQ-001', 'scenario': 1}}, {'local': {'requirement': 'REQ-001', 'scenario': 2}}, {'regression': {'impact': 1, 'scenario': 1}}]):
                before = snapshot(item['id'])
                observed = command([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_payments.py', '-k', selector])
                after = snapshot(item['id'])
                assert before == after
                outcome = 'pass' if observed['exit'] == 0 else 'fail'
                observations.append({'check': item['id'], 'outcome': outcome, 'before': before, 'after': after, **observed})
                results.append({'check': item['id'], 'result': outcome, 'evidence': 'docs/evidence/payment.txt',
                                'revision': label + ':' + digest(source), 'input_digest_before': before, 'input_digest_after': after,
                                'context': {'execution': 'local', 'environment': str(report['environment']), 'observed': True}})
                assessments.append({'obligation': obligation, 'result': outcome, 'checks': [item['id']], 'evidence': 'docs/evidence/payment.txt',
                                    'explanation': 'Observed assertion outcome in the maintained synthetic test: ' + selector})
            val.update(results=results, assessments=assessments)
            evidence.write_text(json.dumps(observations, indent=2))
            fixture.write('tasks')
            return observations

        initial = observe('before-correction')
        assert [r['outcome'] for r in initial] == ['pass', 'fail', 'fail']
        for number, category, obligation, description, check_id in [
            (1, 'partial', {'local': {'requirement': 'REQ-001', 'scenario': 2}}, 'Zero and negative amounts are accepted; error handling is absent.', 'CHECK-002'),
            (2, 'contradicts', {'regression': {'impact': 1, 'scenario': 1}}, 'A repeated request charges twice despite the retained contract.', 'CHECK-003'),
            (3, 'unrequested', {'plan': 'Proposal baseline excludes export and requires auditing.'}, 'AUDIT_DISABLED and export_all_customers contradict/exceed the approved scope.', 'CHECK-001')]:
            val['findings'].append({'id': f'FIND-{number:03}', 'source': obligation, 'category': category, 'state': 'open',
                                    'evidence': 'docs/evidence/payment.txt', 'description': description, 'tasks': ['TASK-001'], 'checks': [check_id]})
        fixture.write('tasks')
        before_readonly = digest(source)
        initial_validation = fixture.result('delivery')
        assert initial_validation['status'] == 'fail'
        repeated = fixture.result('delivery')
        assert digest(source) == before_readonly and len(val['findings']) == 3 and repeated['status'] == 'fail'
        report['steps'].append({'action': 'Validation-only: execute checks, inspect code, record and reuse findings; no product edits.',
                                'checks': initial, 'findings': copy.deepcopy(val['findings']),
                                'validator': initial_validation, 'source_unchanged': True, 'finding_count_after_repeat': 3})

        source.write_text(FIXED)
        stale = fixture.result('delivery')
        assert 'INPUT_STALE' in fixture.codes(stale)
        corrected = observe('authorized-in-scope-correction')
        assert all(r['outcome'] == 'pass' for r in corrected)
        assert 'AUDIT_DISABLED' not in source.read_text() and 'export_all_customers' not in source.read_text()
        for finding in val['findings']:
            finding.update(state='resolved', resolution='Reviewer inspected the correction/removal under the existing task and observed current passing tests.')
        fixture.write('tasks')
        fixed_validation = fixture.result('delivery')
        assert fixed_validation['status'] == 'pass', fixed_validation
        assert test_hash == digest(fixture.root / 'tests/test_payments.py')
        assert report['approved_plan_digests']['tasks'] == fixture.digest('tasks')
        report['steps'].append({'action': 'Authorized correction within the existing task; remove unrequested behavior, retain tests and rerun.',
                                'diff': ''.join(difflib.unified_diff(BROKEN.splitlines(True), FIXED.splitlines(True), fromfile='before.py', tofile='after.py')),
                                'stale_before_rerun': stale, 'checks': corrected, 'validator': fixed_validation,
                                'maintained_test_unchanged': True, 'approved_task_digest_unchanged': True})
        (fixture.root / 'config.txt').write_text('changed-execution-config\n')
        resumed = fixture.result('delivery')
        assert resumed['status'] == 'unable-to-verify'
        (fixture.root / 'config.txt').write_text('locale=en\n')
        old_description = fixture.data['tasks']['tasks'][0]['description']
        fixture.data['tasks']['tasks'][0]['description'] = 'Add a new unapproved export capability.'
        fixture.write('tasks')
        replanning = fixture.result('implementation')
        assert 'APPROVAL_STALE' in fixture.codes(replanning)
        fixture.data['tasks']['tasks'][0]['description'] = old_description
        fixture.write('tasks')
        report['steps'].append({'action': 'Resume after configuration edit, then propose a task-plan scope edit.',
                                'resumed_validation': resumed, 'changed_plan_validation': replanning,
                                'dependent_implementation_stopped': True})
        report['final_fixture_artifacts'] = {name: (fixture.change / (name + '.md')).read_text() for name in VALIDATOR.ARTIFACTS}

        # Separate small reviewer cases, with actual observations rather than an
        # implication that generated result records prove execution.
        isolated = V3Tests()
        isolated.setUp()
        try:
            isolated.begin()
            no_impact = isolated.result()
            assert no_impact['status'] == 'pass'
            report['steps'].append({'action': 'Review isolated new greeting scope: no related contract declared in this synthetic empty project.',
                                    'observation': (isolated.root / 'src/greeting.py').read_text(), 'validator': no_impact,
                                    'limit': 'The reviewer grounds no-impact; the validator does not discover dependencies.'})
            isolated.data['requirements']['requirements'][0].update(statement='The documented example defines a local greeting literal.', acceptance=['The example source contains Hello world and no HTTP calls.'])
            isolated.write('requirements')
            manual = isolated.data['design']['validation'][0]
            manual['method'] = {'kind': 'review', 'procedure': 'Read greeting source and scenario; confirm literal Hello world and absence of external calls.',
                                'reason': 'This bounded documentary walkthrough inspects the stated example, not user-interface behavior.'}
            isolated.approved_plan()
            isolated.complete()
            before = VALIDATOR.input_digest(isolated.root, isolated.change, manual)
            observed = (isolated.root / 'src/greeting.py').read_text()
            assert 'Hello world' in observed and 'http' not in observed
            after = VALIDATOR.input_digest(isolated.root, isolated.change, manual)
            assert before == after
            isolated.passing_evidence()
            isolated.data['tasks']['validation']['results'][0].update(input_digest_before=before, input_digest_after=after, revision='observed-source-review:' + before)
            isolated.write('tasks')
            (isolated.root / 'docs/evidence/greeting.txt').write_text('Actual reviewer source observation: ' + observed)
            report['steps'].append({'action': 'Actual manual source review with justified method.', 'observation': observed,
                                    'before': before, 'after': after, 'validator': isolated.result('delivery')})
            manual['method'] = {'kind': 'automated', 'procedure': 'Run the configured synthetic runtime to verify greeting behavior.'}
            isolated.approve('design')
            isolated.approve('tasks')
            isolated.data['tasks']['validation']['plan_digest'] = isolated.digest('tasks')
            try:
                subprocess.run([str(isolated.root / 'unavailable-runtime')], check=True, capture_output=True)
                raise AssertionError('Synthetic unavailable prerequisite unexpectedly existed')
            except FileNotFoundError:
                unavailable = 'The configured synthetic runtime does not exist; execution was not observed.'
            isolated.data['tasks']['validation']['results'][0].update(result='unverified')
            isolated.data['tasks']['validation']['results'][0]['context']['observed'] = False
            (isolated.root / 'docs/evidence/greeting.txt').write_text(unavailable)
            isolated.data['tasks']['validation']['assessments'][0].update(result='unverified', explanation=unavailable)
            isolated.write('tasks')
            missing = isolated.result('delivery')
            assert missing['status'] == 'unable-to-verify'
            report['steps'].append({'action': 'Attempt execution with an unavailable synthetic prerequisite.', 'observation': unavailable, 'validator': missing})
        finally:
            isolated.doCleanups()

        replacement = V3Tests()
        replacement.setUp()
        try:
            origin = replacement.add_origin(effect='supersede')
            historical_hash = digest(origin)
            replacement.data['requirements']['requirements'][0].update(statement='Display Welcome instead of Hello world.', acceptance=['Activation displays Welcome.'])
            replacement.data['proposal']['impact']['items'][0]['reason'] = 'Synthetic reviewed replacement of greeting wording; retired Hello world assertion is obsolete.'
            replacement.data['design']['validation'][0]['method']['procedure'] = 'Call greet() and assert Welcome.'
            living = replacement.root / 'docs/greeting.md'
            living.parent.mkdir()
            living.write_text('# Greeting\nActivation displays Hello world.\n')
            replacement.data['design']['validation'][0]['inputs']['include'].append('docs/greeting.md')
            replacement.approved_plan()
            (replacement.root / 'src/greeting.py').write_text('def greet(): return "Welcome"\n')
            living.write_text('# Greeting\nActivation displays Welcome.\n')
            assert 'Welcome' in living.read_text()
            check = replacement.data['design']['validation'][0]
            before = VALIDATOR.input_digest(replacement.root, replacement.change, check)
            run = subprocess.run([sys.executable, '-B', '-c', 'from src.greeting import greet; assert greet() == "Welcome"; print(greet())'], cwd=replacement.root, capture_output=True, text=True)
            after = VALIDATOR.input_digest(replacement.root, replacement.change, check)
            assert before == after
            assert run.returncode == 0 and digest(origin) == historical_hash
            replacement.complete()
            replacement.passing_evidence()
            replacement.data['tasks']['validation']['results'][0].update(input_digest_before=before, input_digest_after=after, revision='observed-replacement:' + before)
            replacement.write('tasks')
            (replacement.root / 'docs/evidence/greeting.txt').write_text('Actual executed replacement assertion: ' + run.stdout)
            outcome = replacement.result('delivery')
            assert outcome['status'] == 'pass'
            report['steps'].append({'action': 'Reviewed synthetic supersession: replace the contract and execute its replacement assertion.',
                                    'stdout': run.stdout, 'exit': run.returncode, 'before': before, 'after': after, 'historical_bytes_unchanged': True, 'living_contract': living.read_text(),
                                    'validator': outcome, 'scope': 'Synthetic planning approvals only; no human approval claim.'})
        finally:
            replacement.doCleanups()
        return report
    finally:
        fixture.doCleanups()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    report = run_walkthrough()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Preserve actual observations; paths identify disposable fixture runs.
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(f'Reviewer walkthrough passed: {len(report["steps"])} observed steps; {args.output}')


if __name__ == '__main__':
    main()
