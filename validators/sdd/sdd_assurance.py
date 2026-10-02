"""Version 3 declared acceptance, impact and execution consistency checks.

The records are claims. These checks do not evaluate assertions or authenticate
an execution, human review or environment.
"""

from __future__ import annotations

import hashlib
import json

from sdd_inputs import input_digest, input_scope, local_path


def key(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def requirements_digest(api, artifact):
    payload = {'metadata': artifact['metadata'], 'body': api._normalized_body(artifact['body'])}
    return hashlib.sha256(api._json(payload).encode()).hexdigest()


def inspect(v, artifacts, delivery, live, approved):
    api = v.api
    proposal = artifacts['proposal']
    design = artifacts.get('design')
    tasks = artifacts.get('tasks')
    path = proposal['path']
    directory = path.parent
    current_id = directory.name
    requirements = artifacts['requirements']['metadata']['requirements']
    ids = {r['id'] for r in requirements}
    scenarios = {key({'local': {'requirement': r['id'], 'scenario': i}})
                 for r in requirements for i in range(1, len(r['acceptance']) + 1)}
    impact = proposal['metadata']['impact']
    if impact['state'] == 'unresolved' and (approved.get('proposal') or v.phase != 'planning' or delivery):
        v.add('IMPACT_UNRESOLVED', 'Resolve affected current contracts before readiness', path, True)
    retained = set()
    source_keys = set()
    for index, item in enumerate(impact['items'], 1):
        if not set(item['targets']) <= ids:
            v.add('IMPACT_TARGET', 'Impact targets must be local requirements', path)
        source = item.get('source')
        if source:
            identities = {(source['change'], source['requirement'], i) for i in source['scenarios']}
            if identities & source_keys or source['change'] == current_id:
                v.add('IMPACT_SOURCE', 'Overlapping or self-referential origin scenarios', path)
            source_keys.update(identities)
            origin = v.changes.get(source['change'])
            try:
                if origin is None:
                    raise ValueError('Declared source change is missing: ' + source['change'])
                source_path = api._safe_path(v.root, origin / 'requirements.md')
                raw = api._read_artifact(source_path)
                fmt = raw['metadata'].get('sdd_version')
                schema = ('v3_' if fmt == 3 else '' if fmt == 2 else 'legacy_') + 'requirements'
                errors = list(v.validators[schema].iter_errors(raw['metadata']))
                if errors or raw['metadata'].get('change') != source['change']:
                    raise ValueError('Source Requirements schema or identity is invalid')
                matches = [r for r in raw['metadata']['requirements'] if r['id'] == source['requirement']]
                if len(matches) != 1 or any(i > len(matches[0]['acceptance']) for i in source['scenarios']):
                    raise ValueError('Source requirement/scenarios do not resolve uniquely')
                if requirements_digest(api, raw) != source['requirements_digest']:
                    raise ValueError('Historical source Requirements digest changed')
            except (OSError, ValueError, TypeError, api.yaml.YAMLError) as exc:
                v.add('IMPACT_SOURCE', str(exc), path, True)
        contract = item['current_contract']
        try:
            if 'change' in contract:
                if contract['change'] != current_id or contract['locator'] not in proposal['body']:
                    raise ValueError('Proposal baseline must identify a section of this proposal')
            else:
                target = local_path(v.root, contract['path'])
                # The living document is a pre-change baseline. Check it before
                # acceptance, not after its explicitly planned implementation edit.
                if live and not approved.get('proposal'):
                    content = target.read_text(encoding='utf-8')
                    if contract['locator'] not in content or hashlib.sha256(target.read_bytes()).hexdigest() != contract['digest']:
                        raise ValueError('Current baseline locator/digest does not match')
        except (OSError, ValueError) as exc:
            v.add('IMPACT_BASELINE', str(exc), path, True)
        if item['effect'] in ('preserve', 'extend'):
            for ordinal in source['scenarios'] if source else [0]:
                retained.add(key({'regression': {'impact': index, 'scenario': ordinal}}))

    v.metrics[current_id] = {'local_scenarios': len(scenarios), 'regression_obligations': len(retained)}
    if not design:
        return
    path = design['path']
    data = design['metadata']
    checks = {c['id']: c for c in data['validation']}
    expected = {}

    def mapping(obligation, names, applicable, reason):
        identity = key(obligation)
        if identity in expected:
            v.add('COVERAGE_DUPLICATE', identity, path)
        expected[identity] = (set(names), applicable)
        if not set(names) <= checks.keys():
            v.add('COVERAGE_CHECK', 'Unknown check for ' + identity, path)
        if applicable and not any(checks[n]['required'] for n in names if n in checks):
            v.add('COVERAGE_REQUIRED', 'No required check for ' + identity, path)
        if not applicable and not reason:
            v.add('COVERAGE_EXCLUSION', 'An exclusion needs a reviewed reason', path)
        if 'local' in obligation:
            req = obligation['local']['requirement']
            if any(req not in checks[n]['requirements'] for n in names if n in checks):
                v.add('COVERAGE_CHECK', 'Scenario check must reference its requirement', path)

    for row in data['coverage']:
        mapping({'local': row['scenario']}, row['checks'], row['applicability'] == 'required', row.get('reason'))
    for row in data['regression']:
        index = row['obligation']['impact']
        if index <= len(impact['items']):
            targets = set(impact['items'][index - 1]['targets'])
            if any(not targets.intersection(checks[n]['requirements']) for n in row['checks'] if n in checks):
                v.add('COVERAGE_CHECK', 'Regression check must reference an affected local requirement', path)
        mapping({'regression': row['obligation']}, row['checks'], True, row['rationale'])
    v.coverage(set(expected), scenarios | retained, path, 'Scenario and retained regression coverage')
    # Supersession is traceable to local replacement requirements, never silent
    # removal of an old failing test.
    for item in impact['items']:
        if item['effect'] == 'supersede':
            for req in item['targets']:
                if not any(c['required'] and req in c['requirements'] for c in checks.values()):
                    v.add('SUPERSESSION_CHECK', 'Replacement needs a required check: ' + req, path)
    snapshots = {}
    for name, check in checks.items():
        if check['method']['kind'] != 'automated' and not check['method'].get('reason'):
            v.add('CHECK_METHOD', 'Manual/review method needs a reason: ' + name, path)
        try:
            # Historical inventory validates safe scope syntax without accessing
            # obsolete files. Live checks additionally read actual declared inputs.
            if live:
                snapshots[name] = input_digest(v.root, directory, check, v.input_cache)
            else:
                input_scope(v.root, directory, check, inspect_links=False)
        except (OSError, ValueError) as exc:
            v.add('INPUT_SCOPE', name + ': ' + str(exc), path)
    if not tasks:
        return
    path = tasks['path']
    evidence = tasks['metadata']['validation']
    results = {r['check']: r for r in evidence['results']}
    fresh = {}
    stale_count = 0
    for name, result in results.items():
        if name not in checks:
            continue
        valid = result['input_digest_before'] == result['input_digest_after']
        if live:
            valid = valid and result['input_digest_after'] == snapshots.get(name)
        fresh[name] = valid
        if not valid:
            stale_count += 1
            v.add('INPUT_STALE', 'Rerun affected check, do not relabel old evidence: ' + name, path, True)
        if result['result'] == 'pass' and (not result['context']['observed'] or result['context']['execution'] != checks[name]['execution']):
            v.add('EXECUTION_UNVERIFIED', 'Observed execution context is missing/mismatched: ' + name, path, True)
            fresh[name] = False

    seen = set()
    statuses = {}
    for row in evidence['assessments']:
        identity = key(row['obligation'])
        if identity in seen or identity not in expected:
            v.add('ASSESSMENT_REFERENCE', 'Duplicate/unknown obligation: ' + identity, path)
            continue
        seen.add(identity)
        try:
            api._reference(v.root, row['evidence'])
        except (OSError, ValueError) as exc:
            v.add('REFERENCE', str(exc), path)
        names, applicable = expected[identity]
        if set(row['checks']) != names:
            v.add('ASSESSMENT_CHECKS', 'Assessment must reference its planned checks: ' + identity, path)
        outcome = row['result']
        if outcome == 'not-applicable' and applicable or not applicable and outcome != 'not-applicable':
            v.add('ASSESSMENT_EXCLUSION', 'Disposition must match approved applicability', path)
        if outcome == 'fail':
            v.add('ACCEPTANCE_FAILED', identity, path)
        if outcome == 'unverified':
            v.add('ACCEPTANCE_UNVERIFIED', identity, path, True)
        if outcome == 'pass':
            required = [n for n in names if n in checks and checks[n]['required']]
            if not required or any(results.get(n, {}).get('result') != 'pass' or not fresh.get(n) for n in required):
                v.add('ACCEPTANCE_UNVERIFIED', 'No current required passing evidence: ' + identity, path, True)
                outcome = 'unverified'
        if 'local' in row['obligation']:
            statuses.setdefault(row['obligation']['local']['requirement'], []).append(outcome)
    if delivery:
        for identity in set(expected) - seen:
            v.add('ASSESSMENT_MISSING', identity, path, True)
    task_ids = {t['id'] for t in tasks['metadata']['tasks']}
    v.unique(evidence['findings'], 'id', path, 'finding')
    open_keys = set()
    gap_requirements = set()
    for finding in evidence['findings']:
        identity = key(finding['source'])
        if 'plan' not in finding['source'] and identity not in expected:
            v.add('FINDING_REFERENCE', 'Unknown obligation: ' + identity, path)
        if not set(finding['tasks']) <= task_ids or not set(finding['checks']) <= checks.keys():
            v.add('FINDING_REFERENCE', 'Unknown corrective task/check', path)
        try:
            api._reference(v.root, finding['evidence'])
        except (OSError, ValueError) as exc:
            v.add('REFERENCE', str(exc), path)
        if finding['state'] == 'open':
            signature = (identity, finding['category'])
            if signature in open_keys:
                v.add('FINDING_DUPLICATE', 'Reuse the existing open finding', path)
            open_keys.add(signature)
            if 'local' in finding['source']:
                gap_requirements.add(finding['source']['local']['requirement'])
            v.add('ACCEPTANCE_GAP', finding['id'] + ': ' + finding['description'], path)
        elif not finding.get('resolution') or not finding['checks'] or any(results.get(n, {}).get('result') != 'pass' or not fresh.get(n) for n in finding['checks']):
            v.add('RESOLUTION_UNVERIFIED', finding['id'] + ' needs a disposition and current evidence', path, True)
    v.metrics[current_id].update(assessed=len(seen), results=len(results), open_findings=len(open_keys), stale_results=stale_count)
    summary = {}
    for req in requirements:
        outcomes = statuses.get(req['id'], [])
        summary[req['id']] = ('fail' if 'fail' in outcomes or req['id'] in gap_requirements else 'unverified'
                            if len(outcomes) != len(req['acceptance']) or 'unverified' in outcomes
                            else 'not-applicable' if all(s == 'not-applicable' for s in outcomes) else 'pass')
    v.metrics[current_id]['requirements'] = summary
