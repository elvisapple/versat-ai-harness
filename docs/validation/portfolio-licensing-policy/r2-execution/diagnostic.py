"""Disposable design diagnostic; not an approved CHECK execution or acceptance ledger."""
from pathlib import Path
import tempfile,shutil,sys,yaml,json,copy,subprocess,hashlib
sys.dont_write_bytecode=True
base=Path(sys.argv[1]).resolve();candidate=Path(sys.argv[2]).resolve()
sys.path.insert(0,str(base/'validators/sdd'))
from sdd_inputs import input_digest
import validate
root=Path(tempfile.mkdtemp(prefix='h01-h02-r2-probe-',dir='/private/tmp'))
shutil.copytree(base,root,dirs_exist_ok=True,ignore=shutil.ignore_patterns('.git','__pycache__'))
ids=['portfolio-licensing-policy','contribution-security-guidance'];shutil.move(root/'specs/changes'/ids[0],root/'specs/archive'/ids[0])
def meta(p):return yaml.safe_load(p.read_text().split('---',2)[1])
def candidate_design(c):return next(p for p in [candidate/'specs/changes'/c/'design.md',candidate/'specs/archive'/c/'design.md'] if p.exists())
def scope(c,revision):
 p=(base/'specs'/('changes' if c==ids[0] else 'archive')/c/'design.md') if revision==1 else candidate_design(c)
 return {x['id']:x for x in meta(p)['validation'] if x['id'] in ['CHECK-005','CHECK-006']}
def snaps(c,rev):return {k:input_digest(root,root/'specs/archive'/c,v) for k,v in scope(c,rev).items()}
def change_file(p,transform,observe):
 raw=p.read_bytes()
 try:p.write_text(transform(p.read_text()));return observe()
 finally:p.write_bytes(raw)
def add_evidence(text):
 _,fm,body=text.split('---',2);m=yaml.safe_load(fm);m['validation']['results'][0]['revision']+=' [disposable evidence-only probe]'
 return '---\n'+yaml.safe_dump(m,sort_keys=False,allow_unicode=True)+'---'+body
def task_digest(c):
 d=root/'specs/archive'/c
 artifacts={name:validate._read_artifact(d/(name+'.md')) for name in ['proposal','requirements','design','tasks']}
 return validate._digest_artifacts(artifacts,'tasks')
rows=[]
for c in ids:
 peer=next(x for x in ids if x!=c);peer_tasks=root/'specs/archive'/peer/'tasks.md'
 for rev in [1,2]:
  before=snaps(c,rev);after=change_file(peer_tasks,add_evidence,lambda:snaps(c,rev))
  changed={k:before[k]!=after[k] for k in before};assert all(v==(rev==1) for v in changed.values())
  rows.append({'observer':c,'scope_revision':rev,'probe':'sibling evidence-only revision','changed':changed})
 for rel,label in [('docs/licensing/harness-plugin-terms.md','real terms source'),(f'specs/archive/{peer}/design.md','sibling Design source'),(f'specs/archive/{peer}/requirements.md','sibling Requirements source'),('specs/archive/default-codeowner-elviszoz/tasks.md','unrelated historical Tasks')]:
  before=snaps(c,2);after=change_file(root/rel,lambda s:s+'\nDesign diagnostic source change.\n',lambda:snaps(c,2));changed={k:before[k]!=after[k] for k in before};assert all(changed.values());rows.append({'observer':c,'scope_revision':2,'probe':label,'changed':changed})
 before=task_digest(peer)
 def edit_task(text):
  _,fm,body=text.split('---',2);m=yaml.safe_load(fm);m['tasks'][0]['description']+=' [substantive diagnostic change]'
  return '---\n'+yaml.safe_dump(m,sort_keys=False,allow_unicode=True)+'---'+body
 after=change_file(peer_tasks,edit_task,lambda:task_digest(peer));assert before!=after
 approval=meta(peer_tasks)['review']['approval']['digest'];assert approval==before and approval!=after
 rows.append({'observer':c,'probe':'sibling substantive task change','canonical_tasks_digest_changed':True,'original_approval_no_longer_matches':True})
 # Failed peer evidence is still a deterministic failure of its own validator.
 def fail_result(text):
  _,fm,body=text.split('---',2);m=yaml.safe_load(fm);m['validation']['results'][0]['result']='fail'
  return '---\n'+yaml.safe_dump(m,sort_keys=False,allow_unicode=True)+'---'+body
 def validate_peer():
  p=subprocess.run([sys.executable,str(root/'validators/sdd/validate.py'),'--root',str(root),'--change',peer,'--phase','delivery','--json'],text=True,capture_output=True)
  j=json.loads(p.stdout);codes=sorted({f['code'] for f in j['findings']});assert p.returncode!=0 and 'VALIDATION_FAILED' in codes
  return {'status':j['status'],'codes':codes}
 observed=change_file(peer_tasks,fail_result,validate_peer)
 rows.append({'observer':c,'probe':'sibling failed result still rejected by its own guard','observed':observed})
result={'base':'1198c2cd2d39f69a12e4f5abae727725b577593a','r2_design_sha256':{c:hashlib.sha256(candidate_design(c).read_bytes()).hexdigest() for c in ids},'purpose':'Design-only disposable diagnostic. Low-level input function compares proposed scopes without asserting approved CHECK execution. No R2 approval or acceptance results fabricated. No source mutation survives probes.','results':rows}
Path(sys.argv[3]).write_text(json.dumps(result,indent=2)+'\n')
print('Design diagnostic passed:',len(rows),'observations. R1 cycle reproduced both directions; R2 evidence exclusion stable; source/plan/failure controls retained.')
shutil.rmtree(root)
