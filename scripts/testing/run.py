#!/usr/bin/env python3
"""Execute explicitly configured project suites. Test execution is not SDD delivery readiness."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import uuid

sys.dont_write_bytecode = True
from common import PACKAGE, atomic_json, clean_environment, contract, digest_file, execute, provider_digest, sdd


def now():
    return datetime.now(timezone.utc).isoformat()


def locate(root, change):
    if not sdd.CHANGE_ID.fullmatch(change):
        raise ValueError('Invalid change ID')
    matches = [contract.safe_path(root,f'specs/{store}/{change}') for store in ('changes','archive')]
    matches = [p for p in matches if p.is_dir()]
    if len(matches) != 1:
        raise ValueError('Change must resolve uniquely')
    return matches[0]


def binding(root, change, check_id, context):
    directory = locate(root, change)
    validator = sdd.RepositoryValidator(root, 'implementation', change)
    result = validator.run()
    allowed = {'INPUT_STALE', 'VALIDATION_STALE', 'ACCEPTANCE_UNVERIFIED', 'ACCEPTANCE_GAP',
               'ACCEPTANCE_FAILED', 'VALIDATION_FAILED', 'RESOLUTION_UNVERIFIED', 'EXECUTION_UNVERIFIED',
               'ASSESSMENT_MISSING', 'TASK_INCOMPLETE', 'VALIDATION_MISSING'}
    if any(f['code'] not in allowed for f in result['findings']):
        raise ValueError('SDD plan not executable: '+json.dumps(result['findings']))
    design = sdd._read_artifact(directory/'design.md')['metadata']
    if design['sdd_version'] != 3:
        raise ValueError('Execution fragments require SDD v3')
    checks = [c for c in design['validation'] if c['id'] == check_id]
    if len(checks) != 1:
        raise ValueError('Check must resolve uniquely')
    check = checks[0]
    if check['method']['kind'] != 'automated' or check['execution'] != context:
        raise ValueError('Expected approved automated check with matching execution context')
    return directory, check, sdd.stage_digest(directory,'tasks')


def command(suite, root, report):
    tokens = {'{python}':sys.executable, '{harness_root}':str(PACKAGE), '{report}':str(report)}
    argv = [tokens.get(a,a) for a in suite['argv']]
    if suite['result'] == 'unittest':
        argv = [sys.executable,str(PACKAGE/'scripts/testing/unittest_report.py'),'--report',str(report),'--',*argv[3:]]
    return argv


def inspect(root, config, scope):
    """Inspect prerequisites and command-source scope without launching project commands."""
    for suite in config['suites']:
        cwd = contract.safe_path(root,suite['cwd'])
        if not cwd.is_dir():
            raise FileNotFoundError(f'Working directory unavailable: {suite["cwd"]}')
        argv = command(suite,root,root/'unused-report.json')
        executable = argv[0]
        if '/' in executable:
            executable = str(cwd/executable) if not Path(executable).is_absolute() else executable
        else:
            executable = shutil.which(executable) or ''
        if not executable or not os.access(executable,os.X_OK):
            raise FileNotFoundError(f'Executable unavailable: {suite["argv"][0]}')
        # Known project-local files passed as arguments must be in reviewed inputs.
        # Imported/transitive dependencies still require scope review.
        for arg in argv:
            p = Path(arg)
            candidate = p if p.is_absolute() else cwd/p
            try:
                exists = candidate.exists()
            except OSError:
                exists = False  # An argument can be inline code, not a filename.
            if candidate.is_relative_to(root) and exists:
                relative = candidate.relative_to(root).as_posix()
                candidate = contract.safe_path(root,relative)
                if not contract.covered(root,candidate,scope):
                    raise ValueError(f'Command source outside input scope: {relative}')


def run_project(root, selected=None, change=None, check_id=None, context='local', output=None):
    root = Path(root).resolve()
    if bool(change) != bool(check_id) or selected and change:
        raise ValueError('Use --change and --check together, without targeted selection')
    config = contract.load_config(root)
    suites = {s['id']:s for s in config['suites']}
    chosen = selected or config['required_suites']
    if len(chosen) != len(set(chosen)) or not set(chosen) <= suites.keys():
        raise ValueError('Selected suites must be unique configured IDs')
    directory = root/'.versat/__execution_snapshot__'
    plan = None
    if change:
        directory, check, plan = binding(root,change,check_id,context)
        if not contract.covered(root,root/'.versat/validation.yaml',check['inputs']):
            raise ValueError('SDD check must include execution configuration')
        if not check['outputs']:
            raise ValueError('SDD check must declare a stable evidence output directory')
        output = output or check['outputs'][0]
        outpath = contract.safe_path(root,output)
        if outpath.is_relative_to(directory) or not any(outpath.is_relative_to(contract.safe_path(root,p)) for p in check['outputs']):
            raise ValueError('SDD output must be inside declared outputs and outside dossier')
    else:
        output = output or '.versat/validation-runs'
        check = {'inputs':config['inputs'],'outputs':[output]}
    outpath = contract.safe_path(root,output)
    # Validate both scopes before writing anything. The stable parent is intentionally excluded.
    standalone = {'inputs':config['inputs'],'outputs':[output]}
    sdd.sdd_assurance.input_scope(root,directory,standalone)
    sdd.sdd_assurance.input_scope(root,directory,check)
    execution_config = dict(config, suites=[suites[name] for name in chosen])
    inspect(root,execution_config,config['inputs'])
    if change:
        inspect(root,execution_config,check['inputs'])
    outpath.mkdir(parents=True,exist_ok=True)
    run_dir = contract.safe_path(root,f'{output}/{uuid.uuid4().hex}')
    run_dir.mkdir()
    started = now()
    before = sdd.input_digest(root,directory,check)
    standalone_before = sdd.input_digest(root,directory,standalone)
    config_before = digest_file(root/'.versat/validation.yaml')
    provider_before = provider_digest()
    report = {'schema_version':1,'attempt':run_dir.name,'scope':'targeted' if selected else 'full',
              'readiness':False,'result':'running','started_at':started,'selected_suites':chosen,
              'required_suites':config['required_suites'],'suites':[], 'input_digest_before':before,
              'configuration_digest':config_before,'provider_digest':provider_before,
              'provider_version':(PACKAGE/'VERSION').read_text().strip(),
              'environment':f'{platform.platform()}; Python {platform.python_version()}', 'execution':context}
    atomic_json(run_dir/'result.json',report)
    for name in chosen:
        suite = suites[name]
        suite_dir = run_dir/name
        suite_dir.mkdir()
        counts_path = suite_dir/'counts.json'
        argv = command(suite,root,counts_path)
        suite_started = now()
        record = execute(argv,contract.safe_path(root,suite['cwd']),suite_dir,suite['timeout_seconds'],clean_environment(suite.get('environment',[])))
        record['process_reason'] = record.get('reason')
        interrupted = record.get('reason') == 'interrupted'
        record.update(suite=name,started_at=suite_started,ended_at=now())
        if suite['result'] != 'exit-code' and record['result'] != 'unverified':
            try:
                safe = contract.safe_path(root,counts_path.relative_to(root).as_posix())
                if safe.stat().st_size > 1024*1024:
                    raise ValueError('Structured report exceeds 1 MiB')
                record['counts'] = contract.validate_counts(json.loads(safe.read_text()))
                if record['counts']['failed'] or record['counts']['errors']:
                    record.update(result='fail',reason='Test assertions failed')
            except (ValueError,OSError) as exc:
                record.update(result='fail',reason=f'Invalid test report: {exc}')
        report['suites'].append(record)
        atomic_json(run_dir/'result.json',report)
        if interrupted or record['result']=='unverified':
            break
    states = [r['result'] for r in report['suites']]
    outcome = 'fail' if 'fail' in states else 'unverified' if 'unverified' in states or len(states)!=len(chosen) else 'pass'
    fresh = False
    try:
        if change:
            after_dir, after_check, after_plan = binding(root,change,check_id,context)
            if after_plan != plan or after_check != check:
                raise ValueError('SDD plan or check changed during execution')
            directory = after_dir
        after = sdd.input_digest(root,directory,check)
        report['input_digest_after'] = after
        fresh = (before==after and standalone_before==sdd.input_digest(root,directory,standalone)
                 and config_before==digest_file(root/'.versat/validation.yaml') and provider_before==provider_digest())
        if not fresh:
            raise ValueError('Inputs/configuration/provider changed during execution; rerun')
    except (ValueError,OSError) as exc:
        report['freshness_error']=str(exc)
        outcome = 'fail'
    report.update(result=outcome,ended_at=now(),fresh=fresh)
    report['readiness'] = not selected and outcome=='pass' # Configured suite readiness only.
    if change and fresh:
        fragment = {'check':check_id,'result':outcome,'evidence':(run_dir/'result.json').relative_to(root).as_posix(),
                    'revision':f'input:{before}; attempt:{run_dir.name}; provider:{provider_before}',
                    'input_digest_before':before,'input_digest_after':report['input_digest_after'],
                    'context':{'execution':context,'environment':report['environment'],'observed':True}}
        atomic_json(run_dir/'sdd-result.json',{'plan_digest':plan,'result':fragment})
    atomic_json(run_dir/'result.json',report)
    return report, run_dir


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['inspect','run'])
    parser.add_argument('--root',type=Path,default=Path.cwd())
    parser.add_argument('--suite',action='append')
    parser.add_argument('--change')
    parser.add_argument('--check')
    parser.add_argument('--execution',choices=['local','ci'],default='local')
    parser.add_argument('--output')
    args=parser.parse_args()
    try:
        if args.action=='inspect':
            root=args.root.resolve(); config=contract.load_config(root)
            inspect(root,config,config['inputs'])
            print(json.dumps({'result':'pass','required_suites':config['required_suites'],'executed':False}))
            return 0
        result, output=run_project(args.root,args.suite,args.change,args.check,args.execution,args.output)
        print(json.dumps({'result':result['result'],'scope':result['scope'],'report':str(output/'result.json')}))
        return {'pass':0,'fail':1,'unverified':2}[result['result']]
    except (FileNotFoundError,PermissionError) as exc:
        print(json.dumps({'result':'unverified','reason':str(exc)})); return 2
    except (ValueError,OSError,contract.yaml.YAMLError) as exc:
        print(json.dumps({'result':'fail','reason':str(exc)})); return 1


if __name__=='__main__':
    sys.exit(main())
