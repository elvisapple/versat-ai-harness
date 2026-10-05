"""Factual supervised-fixture observations and bounded replay; never semantic acceptance."""
from __future__ import annotations
import json
from pathlib import Path
import shutil
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts/testing'))
from common import PACKAGE, atomic_json, contract, digest_file, execute, sdd


def snapshot(project):
    project = Path(project)
    result = {}
    for path in sorted(project.rglob('*')):
        if '.git' in path.parts or '__pycache__' in path.parts:
            continue
        if path.is_symlink():
            raise ValueError('Fixture contains a symlink: ' + str(path))
        if path.is_file():
            result[path.relative_to(project).as_posix()] = digest_file(path)
        elif not path.is_dir():
            raise ValueError('Fixture contains a special file: ' + str(path))
    return result


def source_digest(package=PACKAGE):
    scope = {'inputs': {'include': ['AGENTS.md', 'README.md', 'VERSION', 'plugin.json',
              '.codex-plugin', '.agents/plugins', 'requirements-validation.txt', 'skills',
              'standards', 'sdd', 'schemas', 'scripts', 'validators', 'tests',
              'project-templates', '.github', 'docs'],
              'exclude': ['docs/validation/automated-test-execution']},
             'outputs': ['docs/validation/automated-test-execution']}
    return sdd.input_digest(package, package/'specs/changes/automated-test-execution', scope)


def plan_identity(project):
    directory = Path(project)/'specs/changes/payment-validation'
    return {stage: {'digest': sdd.stage_digest(directory, stage),
                    'review': sdd._read_artifact(directory/(stage+'.md'))['metadata']['review']}
            for stage in ('proposal', 'design', 'tasks')}


def changes(project, before, approved_plan=None):
    after = snapshot(project)
    delta = {p: {'before': before.get(p), 'after': after.get(p)}
             for p in sorted(set(before) | set(after)) if before.get(p) != after.get(p)}
    controls = ('AGENTS.md', '.versat/validation.yaml', '.versat/project.yaml', '.versat/standards.lock')
    return {'diff': delta,
            'controls_unchanged': all(p not in controls and not p.startswith(('.codex/', '.agents/')) for p in delta),
            'source_tests_unchanged': all(not p.startswith(('src/', 'tests/')) for p in delta),
            'plan_unchanged': None if approved_plan is None else plan_identity(project) == approved_plan}


def validate_report(data):
    if not isinstance(data, dict) or data.get('scope') != 'full' or data.get('result') not in ('pass', 'fail', 'unverified'):
        raise ValueError('Expected a completed full runner report')
    if not data.get('attempt') or not data.get('suites') or not data.get('started_at') or not data.get('ended_at'):
        raise ValueError('Missing original execution observations')
    for suite in data['suites']:
        if 'counts' in suite:
            contract.validate_counts(suite['counts'])
    return data


def reports(project):
    """Return validated original runner reports; these are not authenticated attestations."""
    found = []
    for path in sorted((Path(project)/'docs/evidence').glob('*/result.json')):
        safe = contract.safe_path(Path(project), path.relative_to(project).as_posix())
        data = json.loads(safe.read_text())
        validate_report(data)
        found.append({'path': str(path), 'report': data})
    return found


def replay(project, output, timeout=30):
    """Execute reviewed fixture commands in a subprocess with the retained runner's bounds."""
    if Path(project).is_symlink() or Path(output).is_symlink():
        raise ValueError('Symlink fixture/output root forbidden')
    project, output = Path(project).resolve(), Path(output).resolve()
    if output.is_relative_to(project) or project.is_relative_to(output):
        raise ValueError('Replay output must be outside the scenario project')
    snapshot(project)  # Reject symlinks/special files before running generated code.
    contract.load_config(project)
    output.mkdir(parents=True, exist_ok=False)
    process = execute([sys.executable, str(PACKAGE/'scripts/testing/run.py'), 'run',
                       '--root', str(project)], project, output, timeout)
    result = {'process': process, 'report': None}
    if process.get('reason') == 'exit' and not any(process.get('truncated', {}).values()):
        try:
            summary = json.loads((output/'stdout.txt').read_text().splitlines()[-1])
            report_path = contract.safe_path(project, Path(summary['report']).relative_to(project).as_posix())
            report = json.loads(report_path.read_text())
            validate_report(report)
            result['report'] = report
        except (ValueError, OSError, KeyError, IndexError) as exc:
            result['observation_error'] = str(exc)
    atomic_json(output/'replay.json', result)
    return result


def mutation_replays(project, output):
    """Keep the original untouched and run each controlled defect in a separate copy."""
    from fixtures import GOOD
    if Path(project).is_symlink() or Path(output).is_symlink():
        raise ValueError('Symlink fixture/output root forbidden')
    project, output = Path(project).resolve(), Path(output).resolve()
    if output.is_relative_to(project) or project.is_relative_to(output):
        raise ValueError('Mutation output must be outside the scenario project')
    snapshot(project)
    output.mkdir(parents=True, exist_ok=False)
    mutants = {'duplicate': GOOD.replace('if key in seen:', 'if False:'),
               'boundary': GOOD.replace('amount <= 0', 'amount < 0'),
               'empty-key': GOOD.replace('not key or ', '')}
    results = {}
    for name, source in mutants.items():
        clone = output/name/'project'
        shutil.copytree(project, clone, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        (clone/'src/payment.py').write_text(source)
        results[name] = replay(clone, output/name/'replay')
    atomic_json(output/'mutations.json', results)
    return results
