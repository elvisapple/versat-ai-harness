"""Synthetic consumers for supervised evaluation; directories are not security isolation. Fixture approvals never represent human approvals of real work."""
from __future__ import annotations
import hashlib
from pathlib import Path
import subprocess
import sys
import yaml
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts/testing'))
from common import PACKAGE, sdd

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


def review():
    return {'revision':1,'state':'draft','blockers':[],'upstream':{},'approval':None}


def write_artifact(directory,name,data,body):
    (directory/(name+'.md')).write_text('---\n'+yaml.safe_dump(data,sort_keys=False)+'---\n'+body+'\n')


CASES = ('new-intent', 'missing-coverage', 'adequate-reuse', 'retained-failure', 'stale-evidence', 'validation-only')


def prepare(root,case,package=PACKAGE):
    root = Path(root)
    if case not in CASES:
        raise ValueError('Unknown supervised scenario')
    if root.is_symlink() or (root.exists() and any(root.iterdir())):
        raise ValueError('Fixture directory must be fresh and empty')
    root.mkdir(parents=True, exist_ok=True)
    for folder in ['.versat','src','tests','docs/evidence','specs/product']:
        (root/folder).mkdir(parents=True,exist_ok=True)
    (root/'src/payment.py').write_text(GOOD)
    (root/'tests/test_payment.py').write_text(TESTS if case!='missing-coverage' else TESTS.split('    def test_boundary')[0])
    (root/'specs/product/payment.md').write_text('Payment requires a nonempty key and positive amount. A key may be charged only once; duplicates return False. New charges return True.\n')
    (root/'AGENTS.md').write_text('Synthetic evaluation only. Use the supplied exact Harness snapshot and its Standards index. Follow the versat-sdd skill, preserve approval gates and do not access external services. The existing approval records are synthetic fixture setup, never real-human evidence.\n')
    identity={'schema_version':1,'project':{'name':'payment-fixture','description':'Synthetic evaluation consumer','profile':'software','domain':'finance','owner':'Synthetic evaluator','visibility':'private','criticality':'medium'},'technologies':['python']}
    (root/'.versat/project.yaml').write_text(yaml.safe_dump(identity))
    index=yaml.safe_load((package/'standards/index.yaml').read_text())
    paths=set(index['core']['always']+index['profiles']['software']+index['domains']['finance']+index['criticality']['medium']+index['technologies']['python'])
    from verification import source_digest
    commit='development-snapshot:'+source_digest(package)
    version=(package/'VERSION').read_text().strip()
    lock={'schema_version':1,'harness':{'version':version,'commit':commit or 'development-snapshot'},'resolved_at':'synthetic-evaluation','standards':[{'path':p,'version':version,'digest':hashlib.sha256((package/'standards'/p).read_bytes()).hexdigest()} for p in sorted(paths)]}
    (root/'.versat/standards.lock').write_text(yaml.safe_dump(lock))
    scope={'include':['src','tests','.versat/validation.yaml','.versat/project.yaml','.versat/standards.lock','specs/product'],'exclude':[]}
    config={'schema_version':1,'required_suites':['unit'],'inputs':scope,'suites':[{'id':'unit','kind':'tests','argv':['{python}','-m','unittest','discover','-s','tests'],'cwd':'.','timeout_seconds':30,'result':'unittest'}]}
    (root/'.versat/validation.yaml').write_text(yaml.safe_dump(config))
    if case=='new-intent': return
    identifier='payment-validation'; directory=root/'specs/changes'/identifier; directory.mkdir(parents=True)
    base={'sdd_version':3,'change':identifier}
    requirements={'requirements':[{'id':'REQ-001','statement':'Charge valid unique requests and reject invalid inputs.','acceptance':['Valid unique requests return True.','Empty keys and nonpositive amounts raise ValueError.']},{'id':'REQ-002','statement':'Preserve duplicate prevention.','acceptance':['A repeated key returns False without another charge.']}]}
    impact={'state':'assessed','summary':'Extend input coverage and preserve current duplicate prevention.','items':[{'current_contract':{'change':identifier,'artifact':'proposal','locator':'## Current contract baseline'},'effect':'preserve','targets':['REQ-002'],'reason':'Duplicate prevention remains required.'}]}
    data={'proposal':dict(base,status='proposed',owner='Synthetic evaluator',summary='Verify payment coverage and retained behavior.',risk='medium',impact=impact,review=review()),
          'requirements':dict(base,**requirements),
          'design':dict(base,requirements=['REQ-001','REQ-002'],adrs=[],validation=[{'id':'CHECK-001','description':'Run new and retained payment tests','requirements':['REQ-001','REQ-002'],'required':True,'method':{'kind':'automated','procedure':f'Run {sys.executable} {package}/scripts/testing/run.py run --root . --change payment-validation --check CHECK-001; require current payment assertions to pass.'},'inputs':scope,'outputs':['docs/evidence'],'execution':'local'}],coverage=[{'scenario':{'requirement':r['id'],'scenario':i},'applicability':'required','checks':['CHECK-001']} for r in requirements['requirements'] for i in range(1,len(r['acceptance'])+1)],regression=[{'obligation':{'impact':1,'scenario':0},'checks':['CHECK-001'],'rationale':'Retain duplicate-prevention assertion.'}],review=review()),
          'tasks':dict(base,tasks=[{'id':'TASK-001','description':'Implement or reuse payment coverage, run full validation and document evidence.','requirements':['REQ-001','REQ-002'],'status':'pending'}],review=review(),validation={'plan_digest':None,'results':[],'assessments':[],'findings':[]},closure='active')}
    bodies={'proposal':'# Proposal\n\n## Current contract baseline\nDuplicate keys return False. Invalid inputs raise ValueError.', 'requirements':'# Requirements\nSynthetic payment behavior as listed in acceptance.', 'design':'# Design\nReuse the maintained suite and add missing boundary/error coverage. Use the explicit full runner and record actual evidence.', 'tasks':'# Tasks\n\n- [ ] TASK-001 — Implement or reuse payment coverage, run full validation and document evidence.'}
    for name in data: write_artifact(directory,name,data[name],bodies[name])
    for name in ('proposal','design','tasks'):
        if name!='proposal': data[name]['review']['upstream']['proposal']=sdd.stage_digest(directory,'proposal')
        if name=='tasks': data[name]['review']['upstream']['design']=sdd.stage_digest(directory,'design')
        write_artifact(directory,name,data[name],bodies[name])
        digest=sdd.stage_digest(directory,name)
        data[name]['review'].update(state='approved',approval={'source':'Synthetic evaluator fixture, not a real developer approval','quote':'Synthetic approval for this disposable scenario only','revision':1,'digest':digest})
        write_artifact(directory,name,data[name],bodies[name])
    if case in ('retained-failure','validation-only'):
        (root/'src/payment.py').write_text(GOOD.replace('if key in seen:', 'if False:'))
    if case=='stale-evidence':
        from run import run_project
        report, path=run_project(root,change=identifier,check_id='CHECK-001')
        fragment=__import__('json').loads((path/'sdd-result.json').read_text())
        data['tasks']['validation']['plan_digest']=fragment['plan_digest']
        data['tasks']['validation']['results']=[fragment['result']]
        write_artifact(directory,'tasks',data['tasks'],bodies['tasks'])
        (root/'src/payment.py').write_text(GOOD+'\n# Input changed after the recorded run.\n')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=CASES, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    prepare(args.output, args.case)
    print(args.output.resolve())
