"""Reproduce local Design checks; this collector does not invoke models or remote CI."""
import datetime
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import uuid

ROOT=Path(__file__).resolve().parents[3]
OUTPUT=Path(__file__).resolve().parent/('local-'+uuid.uuid4().hex)
OUTPUT.mkdir()
ENV={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHON':sys.executable}
BASE=[sys.executable,str(ROOT/'validators/sdd/validate.py'),'--root',str(ROOT),'--change','automated-test-execution','--phase','implementation']

def read(*args):
    return subprocess.check_output([*BASE,*args],cwd=ROOT,env=ENV,text=True).strip()

plan=read('--digest','tasks')
rows=[]
for check,test in [('CHECK-001','test_runner.py'),('CHECK-002','test_sdd_evidence.py'),('CHECK-003','test_consumer.py'),('CHECK-005','test_ci.py'),('CHECK-007',None)]:
    argv=[sys.executable,'-m','unittest','discover','-s','tests/execution','-p',test] if test else ['./scripts/validate/run.sh']
    before=read('--input-digest',check)
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,text=True,timeout=180)
    ended=datetime.datetime.now(datetime.timezone.utc).isoformat()
    after=read('--input-digest',check)
    log=OUTPUT/(check+'.txt'); log.write_text(result.stdout+result.stderr)
    row={'check':check,'result':'pass' if result.returncode==0 and before==after else 'fail',
         'evidence':log.relative_to(ROOT).as_posix(),'revision':'input:'+before+'; attempt:'+OUTPUT.name,
         'input_digest_before':before,'input_digest_after':after,
         'context':{'execution':'local','environment':platform.platform()+'; Python '+platform.python_version(),'observed':True}}
    rows.append(row)
    (OUTPUT/(check+'.json')).write_text(json.dumps({'command':argv,'started':started,'ended':ended,'exit_code':result.returncode,'result':row},indent=2)+'\n')
    print(check,row['result'],flush=True)
(OUTPUT/'results.json').write_text(json.dumps({'plan_digest':plan,'results':rows},indent=2)+'\n')
print(OUTPUT.relative_to(ROOT))
raise SystemExit(any(r['result']!='pass' for r in rows))
