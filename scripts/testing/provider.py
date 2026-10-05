#!/usr/bin/env python3
"""Verify a consumer's selected provider and index-resolved Standards without downloads."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
sys.dont_write_bytecode=True
from common import PACKAGE, contract
from jsonschema import Draft202012Validator


def verify(root, package=PACKAGE):
    identity=contract.read_yaml(contract.safe_path(root,'.versat/project.yaml'))
    lock=contract.read_yaml(contract.safe_path(root,'.versat/standards.lock'))
    for data,name in [(identity,'project'),(lock,'standards')]:
        Draft202012Validator(contract.read_yaml(package/'schemas'/f'{name}.schema.yaml')).validate(data)
    version=(package/'VERSION').read_text().strip()
    commit=lock['harness']['commit']
    if lock['harness']['version']!=version or not re.fullmatch('[0-9a-f]{40}|[0-9a-f]{64}',commit):
        raise ValueError('Expected exact provider version and full commit in standards.lock')
    git=subprocess.run(['git','-C',str(package),'rev-parse','HEAD'],capture_output=True,text=True)
    if git.returncode or git.stdout.strip()!=commit:
        raise ValueError('Provider checkout does not match locked commit')
    status=subprocess.run(['git','-C',str(package),'status','--porcelain','--untracked-files=all'],capture_output=True,text=True)
    if status.returncode or status.stdout.strip():
        raise ValueError('Consumer provider must be clean at its locked commit; use direct commands for explicitly recorded development fixtures')
    index=contract.read_yaml(package/'standards/index.yaml')
    project=identity['project']
    required=list(index['core']['always'])
    for group,key in [('profiles',project['profile']),('domains',project['domain']),('criticality',project['criticality'])]:
        if key not in index[group]: raise ValueError(f'Unknown Standards context: {group}/{key}')
        required+=index[group][key]
    for technology in identity['technologies']:
        if technology not in index['technologies']: raise ValueError(f'Unknown technology: {technology}')
        required+=index['technologies'][technology]
    expected=set(required)
    selected={s['path']:s for s in lock['standards']}
    if len(selected)!=len(lock['standards']) or set(selected)!=expected:
        raise ValueError('Locked Standards do not match the canonical index resolution')
    for name,row in selected.items():
        digest=hashlib.sha256(contract.safe_path(package/'standards',name).read_bytes()).hexdigest()
        if row['version']!=version or row['digest']!=digest:
            raise ValueError(f'Locked Standard version/digest mismatch: {name}')
    return {'result':'pass','version':version,'commit':commit,'standards':sorted(selected)}


def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--root',type=Path,required=True)
    args=parser.parse_args()
    try:
        print(json.dumps(verify(args.root.resolve()))); return 0
    except Exception as exc:
        print(json.dumps({'result':'unverified','reason':str(exc)})); return 2
if __name__=='__main__': sys.exit(main())
