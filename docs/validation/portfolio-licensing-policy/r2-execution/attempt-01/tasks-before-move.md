---
sdd_version: 3
change: portfolio-licensing-policy
tasks:
- id: TASK-001
  description: Reconcile the current baseline, approved R2 scope and retained rights evidence.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-002
  description: Reconcile the canonical policy and exact approved snapshot exclusions.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  status: completed
- id: TASK-003
  description: Reverify the existing approved terms, provenance and notices without changing the grant.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  status: completed
- id: TASK-004
  description: Reverify localized licensing guidance, navigation and H02 dependencies.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-005
  description: Execute R2 checks and record all 24 current acceptance and regression assessments.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-006
  description: Prepare the H01 acceptance package and reconcile the coordinated handoff.
  requirements:
  - REQ-004
  - REQ-006
  status: completed
review:
  revision: 2
  state: approved
  blockers: []
  upstream:
    proposal: 5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7
    design: 5c77e32078568a63d9bde6361e72edd485c47dd10ca7ef7f1c490181720f920e
  approval:
    source: Actual user reply in this chat to the combined question approving both Tasks R2 revisions and authorizing
      execution through ready-for-review with passing checks, excluding merge and license application.
    quote: sim
    revision: 2
    digest: 5abf78d6ee0592d4261190de0e203e0765a10e2047681df51efab5999393b568
validation:
  plan_digest: 5abf78d6ee0592d4261190de0e203e0765a10e2047681df51efab5999393b568
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/check-001.md
    revision: R2 active-dossier execution; approved Tasks R2; baseline 0ed31390cc415c3c50c83c9e87bf347ad50fb608
    input_digest_before: b9acafb81b563e3e4578f76c1642798662ec39c46f048a40778fbc39d43f9e57
    input_digest_after: b9acafb81b563e3e4578f76c1642798662ec39c46f048a40778fbc39d43f9e57
    context:
      execution: local
      environment: macOS Python 3.11.4; actual local methods and current read-only remote observations; original
        operational event timestamps retained
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/check-002.md
    revision: R2 active-dossier execution; approved Tasks R2; baseline 0ed31390cc415c3c50c83c9e87bf347ad50fb608
    input_digest_before: b9acafb81b563e3e4578f76c1642798662ec39c46f048a40778fbc39d43f9e57
    input_digest_after: b9acafb81b563e3e4578f76c1642798662ec39c46f048a40778fbc39d43f9e57
    context:
      execution: local
      environment: macOS Python 3.11.4; actual local methods and current read-only remote observations; original
        operational event timestamps retained
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/check-003.md
    revision: R2 active-dossier execution; approved Tasks R2; baseline 0ed31390cc415c3c50c83c9e87bf347ad50fb608
    input_digest_before: ea585b7f21de8358c14702dc62c28100f71ebcb65f2d2b60b0b09d949d5aa6e6
    input_digest_after: ea585b7f21de8358c14702dc62c28100f71ebcb65f2d2b60b0b09d949d5aa6e6
    context:
      execution: local
      environment: macOS Python 3.11.4; actual local methods and current read-only remote observations; original
        operational event timestamps retained
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/check-004.md
    revision: R2 active-dossier execution; approved Tasks R2; baseline 0ed31390cc415c3c50c83c9e87bf347ad50fb608
    input_digest_before: b9acafb81b563e3e4578f76c1642798662ec39c46f048a40778fbc39d43f9e57
    input_digest_after: b9acafb81b563e3e4578f76c1642798662ec39c46f048a40778fbc39d43f9e57
    context:
      execution: local
      environment: macOS Python 3.11.4; actual local methods and current read-only remote observations; original
        operational event timestamps retained
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/check-005.md
    revision: R2 active-dossier execution; approved Tasks R2; baseline 0ed31390cc415c3c50c83c9e87bf347ad50fb608
    input_digest_before: e90c00ee386813500eb08728b219e1b8c7a416a30f11415932ad3c4814241059
    input_digest_after: e90c00ee386813500eb08728b219e1b8c7a416a30f11415932ad3c4814241059
    context:
      execution: local
      environment: macOS Python 3.11.4; actual local methods and current read-only remote observations; original
        operational event timestamps retained
      observed: true
  - check: CHECK-006
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/check-006.md
    revision: R2 active-dossier execution; approved Tasks R2; baseline 0ed31390cc415c3c50c83c9e87bf347ad50fb608
    input_digest_before: 2cb0ea990c30a1368747343331f586e4eb20808ca01cb3ad57bf5eebc7c4cd49
    input_digest_after: 2cb0ea990c30a1368747343331f586e4eb20808ca01cb3ad57bf5eebc7c4cd49
    context:
      execution: local
      environment: macOS Python 3.11.4; actual local methods and current read-only remote observations; original
        operational event timestamps retained
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Ledger retains
      Apache-2.0 intent separately for Platform and Workspace with individual adoption/export evidence.'
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Ledger and terms
      preserve proprietary/private Harness, Discover and CRM; public plugin installation is distinct from source
      licensing.'
  - obligation:
      local:
        requirement: REQ-001
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Policy/guide separate
      recommended disposition from license application, public export, SDK and other handoffs; no operation occurred.'
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Baseline CSV identifies
      all 1,040 source files; owner attestation identifies first-party provenance; seven installed validation packages
      have exact versions/license texts, external to source.'
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Synthetic missing-grant,
      incompatible-dependency, secret-history, missing-reviewer and unknown-control cases all defer; private scope
      remains restricted.'
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Policy explicitly
      requires tree/history/tags/releases/LFS/fixtures/CI/attachments scope; technical source inventory does not
      claim H03 export clearance.'
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Approved draft-0.2
      and status-only current version retain exact installation/use/modification/redistribution clauses; reviewed
      notices identify source and external dependency boundaries.'
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Actual user approval
      follows presentation of exact draft; original SHA-256 and current administrative hash verify. CODEOWNERS/planning
      were not used as text approval.'
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Terms and guides
      preserve destination-project terms, including Apache projects, independently of proprietary tool permissions.'
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Ledger identifies
      owner/executor/company approver, technical CODEOWNERS, source evidence and limits; technical review is by
      this agent and owner approval is attributable.'
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Policy keeps P01/P03
      evidence separate and H03 distribution separate; no unrelated product delivery is claimed.'
  - obligation:
      local:
        requirement: REQ-004
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Unknown controls/authority
      remain explicit in policy; current owner attestation resolves documentary provenance only, not future operational
      controls.'
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Both new core policies
      occur exactly once in core.always; no Skills copied or altered.'
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Root package/schema/SDD/template/validator
      paths and manifests are unchanged; technical suites exercise them.'
  - obligation:
      local:
        requirement: REQ-005
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): VERSION/marketplace
      v0.3.0 and consumer locks are unchanged; no release or implicit consumer update occurred.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Planning itself
      performed no operation; subsequent explicit authorization permitted private implementation, two draft PRs
      and bounded H02 route tests. No license application, release, merge, product distribution or broader access
      grant occurred.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Owner text approval
      and technical source review are explicit; effective adoption/distribution remain separately scoped, and unavailable
      operational evidence stays unverified.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): All 18 local scenarios
      and six retained obligations were reviewed against current source; package and selected planning/implementation
      checks actually passed. This is documentary acceptance, not merge, effective terms or distribution.'
  - obligation:
      regression:
        impact: 1
        scenario: 0
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Reviewed retained
      behavior against current source and rerun mapped checks: Add the absent portfolio policy and concrete-terms
      approval path without treating strategic selection as operative licensing. Compare the specific historical
      acceptance position or captured baseline with current observable behavior; do not reuse historical results
      as fresh evidence. Actual source/diff/navigation, approved terms, authorized route and package evidence are
      recorded in the mapped reports; historical delivery is not reused as a new test result.'
  - obligation:
      regression:
        impact: 2
        scenario: 0
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Reviewed retained
      behavior against current source and rerun mapped checks: Preserve least privilege, secret handling, provenance
      and explicit high-impact authorization while specifying evidence for publication decisions. Compare the specific
      historical acceptance position or captured baseline with current observable behavior; do not reuse historical
      results as fresh evidence. Actual source/diff/navigation, approved terms, authorized route and package evidence
      are recorded in the mapped reports; historical delivery is not reused as a new test result.'
  - obligation:
      regression:
        impact: 3
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Reviewed retained
      behavior against current source and rerun mapped checks: New policy must retain canonical root resources and
      avoid copied Standards. Compare the specific historical acceptance position or captured baseline with current
      observable behavior; do not reuse historical results as fresh evidence. Actual source/diff/navigation, approved
      terms, authorized route and package evidence are recorded in the mapped reports; historical delivery is not
      reused as a new test result.'
  - obligation:
      regression:
        impact: 3
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Reviewed retained
      behavior against current source and rerun mapped checks: New policy must retain canonical root resources and
      avoid copied Standards. Compare the specific historical acceptance position or captured baseline with current
      observable behavior; do not reuse historical results as fresh evidence. Actual source/diff/navigation, approved
      terms, authorized route and package evidence are recorded in the mapped reports; historical delivery is not
      reused as a new test result.'
  - obligation:
      regression:
        impact: 3
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Reviewed retained
      behavior against current source and rerun mapped checks: New policy must retain canonical root resources and
      avoid copied Standards. Compare the specific historical acceptance position or captured baseline with current
      observable behavior; do not reuse historical results as fresh evidence. Actual source/diff/navigation, approved
      terms, authorized route and package evidence are recorded in the mapped reports; historical delivery is not
      reused as a new test result.'
  - obligation:
      regression:
        impact: 4
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/r2-execution/review.md
    explanation: 'R2 current source/mapped-method review (no source content drift from 1198c2c): Reviewed retained
      behavior against current source and rerun mapped checks: Retain the exact semantic release selection contract;
      this proposal neither releases nor enables public distribution. Compare the specific historical acceptance
      position or captured baseline with current observable behavior; do not reuse historical results as fresh evidence.
      Actual source/diff/navigation, approved terms, authorized route and package evidence are recorded in the mapped
      reports; historical delivery is not reused as a new test result.'
  findings: []
closure: active
---

# Tasks — H01 R2

Change `portfolio-licensing-policy` · [Harness #34](https://github.com/versat-labs/versat-ai-harness/issues/34) · Tasks revision 2, awaiting Gate 3 approval.

Executor/accountable contact: Elvis Luis Zoz (`@elviszoz`); technical review follows actual CODEOWNERS. This revision revalidates existing documentary work under the approved Design R2. It does not repeat already accepted licensing decisions or claim that previous completed work never occurred.

## Stage and execution boundary

Proposal/Requirements R1 remains approved. The user approved both exact Design R2 revisions with “aprovado.” after their presentation. This authorizes preparing these Tasks, not execution of previously unseen Tasks R2. All tasks below are pending for the current revision, with no prefilled check results or assessments. Historical approvals, completed work, green draft CI and route evidence remain attributable in the R1 records.

The proposed execution scope is bounded revalidation, joint documentary closure and preparation of the two existing PRs for review under the authority actually given after this plan is reviewed. No merge, license application, new legal grant, new live report/email, channel activation, role change, release or product-wide adoption is included. Public custom-form deployment/inheritance remains a later consequence/check of an authorized merge, not a fabricated pre-merge observation.

## Ordered work

- [x] TASK-001 — Reconcile the current baseline, approved R2 scope and retained rights evidence.

  **Depends on:** Current Tasks R2 approval and applicable execution authorization for both coordinated changes.

  **Work:** Refresh private PR #37/main and public PR #4 read-only; compare with reviewed private head 1198c2cd2d39f69a12e4f5abae727725b577593a, main 0ed31390cc415c3c50c83c9e87bf347ad50fb608 and public head 97d7f4c1ceb76ea42cc37250fc47bdecec7a677b. Preserve unrelated work and the selected Harness 0.3.0 contract. Verify actual Proposal/Design/Tasks approvals for both changes and retain R1 source/provenance observations with their original dates and scope. Identify concrete drift; do not ask again for already recorded owner decisions.

  **Complete when:** Current sources and access limits are recorded, R2 planning bindings are current, and no unreviewed material drift is absorbed. Inventory is not export clearance.

  **Evidence/checks:** CHECK-001/002/006.

- [x] TASK-002 — Reconcile the canonical policy and exact approved snapshot exclusions.

  **Depends on:** TASK-001; coordinate shared sources with H02 TASK-002.

  **Work:** Verify the existing licensing/publication Standard, its single index entry and the policy ledger against the approved requirements. Confirm CHECK-005 and CHECK-006 exclude only specs/archive/contribution-security-guidance/tasks.md in addition to the preexisting output directories. Keep peer Proposal/Requirements/Design, other historical Tasks, real sources and required suites included. Do not change validators, schemas, workflow code, releases or consumer refs. Preserve publish/defer/retain-private decision examples and per-product boundaries.

  **Complete when:** Canonical policy and the exact R2 scope match the approved Design; no broader exclusion, new waiver or effective license is introduced.

  **Evidence/checks:** CHECK-001/003/005/006.

- [x] TASK-003 — Reverify the existing approved terms, provenance and notices without changing the grant.

  **Depends on:** TASK-001/002 and accessible existing approval/source records.

  **Work:** Inspect actual owner text approval and first-party attestation, notices and exact dependency-license records. Verify reviewed draft SHA-256 ba84ea407a9402c2e653bb4450ca79e0e9032582bf5c0283e16b3b45a3ddbb2c and status-only current SHA-256 e0909a27b460e4cb2a54d5f33e8b02a8f9dfcbab047a7a691c671e4f785e01c9. Retain component/third-party limits and the separation of tool/project terms. Do not rewrite legal clauses, apply LICENSE or request approval again for identical text. Actual changed rights/terms block the affected work and require the concrete appropriate review.

  **Complete when:** Exact terms/approval and required rights/notices evidence remain attributable and consistent with the current candidate. Approval remains distinct from application and H03 distribution.

  **Evidence/checks:** CHECK-002.

- [x] TASK-004 — Reverify localized licensing guidance, navigation and H02 dependencies.

  **Depends on:** TASK-002/003.

  **Work:** Walk the existing EN/PT/ES licensing journeys and missing-evidence recovery. Resolve current local links and intended-access references; preserve optional private resources and independent public participation. Confirm H02 consumes the actual approved terms without importing them into project licensing. Only correct in-scope documentary defects if found; substantive changes reopen the affected gate.

  **Complete when:** Locales, permissions, links and source boundaries are aligned and current; no unsupported public availability or product adoption claim is added.

  **Evidence/checks:** CHECK-002/003/004.

- [x] TASK-005 — Execute R2 checks and record all 24 current acceptance and regression assessments.

  **Depends on:** TASK-001–004; both approved task plans, stable relevant sources and coordinated H02 validation.

  **Work:** Execute all six approved methods with actual before/after snapshots, environment and evidence. For CHECK-006, reproduce the R1 cycle and R2 evidence-only stability in disposable copies, retain real-source/peer-plan/unrelated-history sensitivity and independent approval/failure rejection. Run selected planning/implementation as specified for both changes and the full maintained package suite for CHECK-005. Use a truthful pending ledger after preserving previous attempts; do not prefill passing placeholders. Record 18 local and six retained assessments, findings and actual results. Distinguish current source review from retained historical operational facts. Final closure auditing is not a prerequisite of CHECK-006.

  **Complete when:** Six actual current checks pass, all 24 obligations pass with valid mappings, snapshots match, stage/task binding is current and no open finding remains. A diagnosis or historical CI does not replace these results.

  **Evidence/checks:** CHECK-001–006.

- [x] TASK-006 — Prepare the H01 acceptance package and reconcile the coordinated handoff.

  **Depends on:** TASK-005.

  **Work:** Verify the actual task outcomes, six results, 24 assessments, source/approval bindings and evidence access. Prepare the existing private PR/issue summary with truthful H01 candidate status, retained H02 operational limits, per-product adoption and H03 boundaries. Keep closure auditing, both archive moves, remote review and CI separately observed under the joint closure procedure below. Do not close unrelated issues or assert integration.

  **Complete when:** The current acceptance package is reviewable and accurate. This task completes before its own final delivery/archive guard and does not require a merge.

  **Evidence/checks:** Current CHECK-001–006 evidence.

## Joint validation and closure sequence

This procedure coordinates the two existing changes without creating a task that requires its own completion result. Both have approved Designs R2; execution waits for current Tasks approval and its applicable authority.

1. Preserve the complete R1 ledger and all real attempts. Reconcile baselines and finish actual source work; freeze relevant plans, terms, guidance and shared sources before snapshots. Reuse existing work and actual operational observations with their original scope, not blanket historical passes.
2. Execute all approved methods on current inputs, record truthful results and individual assessments, resolve actual findings, and finish each acceptance-package task. Selected planning/implementation checks and full maintained suites remain required. No passing placeholder, test exclusion or validator modification may resolve a ledger/closure failure.
3. Run selected pre-move `--phase delivery` for each eligible change. Move only an eligible unique dossier to archive and set `closure: prepared`. Recheck references and rerun any affected source-dependent check after a sibling move; do not silently give a previous run a new digest. If a guard fails, reopen affected work honestly under the canonical workflow before claiming readiness. A dossier move may change peer plan paths once; evidence-only updates must not retain the R1 hash cycle.
4. On the final combined layout, verify every actual before/after snapshot remains current after recording both result sets. Verify both stage/Tasks approvals and run selected `--phase delivery --require-archive` for both IDs plus the maintained full suite with the trusted PR baseline and `--require-archive`. These are final lifecycle audits, independent of CHECK-006's completed execution. Stop and report a concrete failure rather than weakening a gate or inventing a run.
5. Reuse private PR #37 for the resulting authorized implementation; preserve public PR #4's seven-file payload. Reconcile private metadata/evidence and only documentary public summaries. When transition to review is authorized and both final local guards pass, mark the existing PRs ready for review and observe all resulting required CI. Human/platform reviews remain separate; their absence cannot be filled by an agent-authored approval. Do not merge.

Common work can be observed once when its method, inputs and context genuinely satisfy both mappings; each change still needs its own accurate results and individual assessments. H01 exact terms approval, H02 reporting verification, other-product adoption and H03 distribution remain distinct. No automatic consumer upgrade or effective license follows from archival or PR readiness.

## Stop conditions and rollback

No technical blocker prevents review of this Tasks revision. Actual material source drift, missing approvals, changed legal wording, unavailable external evidence, failing/stale checks or unmet repository controls block the affected execution step. Preserve evidence and name the concrete gap. Existing valid permissions and unchanged text approvals are not requested again. New operational actions require their actual scope; merge and license application remain excluded.

Before execution, this local plan may be revised or discarded without changing remote PRs. During execution, restore a truthful active/pending state when required and preserve prior successful/failed records; never treat a revert as license or access revocation. Do not delete the closed private test reports or reopen unrelated completed issues.

## Planning review

Tasks R2 is presented after actual Design R2 approval. No R2 Tasks approval is recorded before the user reviews this revision. Original Tasks R1 approval, substantive plan and completed ledger remain in `docs/validation/portfolio-licensing-policy/design-r2/r1-tasks.md`; the superseded pre-R2 state is preserved in `docs/validation/portfolio-licensing-policy/tasks-r2/pre-r2-tasks.md`. Their old passes are not current R2 results.

## Progress

Planning only: all current tasks pending. Design R2 approval recorded with the exact presented digest; Tasks R2 awaits approval. No implementation, archive move, remote publication or PR-state change performed by this preparation.

## Validation evidence

Current results, assessments and findings remain empty. Planning validation is recorded outside this ledger; it cannot prove implementation or operational readiness.

## Delivery

Both local dossiers remain active. Remote PRs remain draft and unmerged; their existing CI does not establish R2 combined archival readiness. No effective license application.


### Tasks R2 approval and execution authority

The user replied "sim" to the explicit combined approval/execution question for both presented Tasks R2 revisions, including making both existing PRs ready for review after applicable checks pass. This supersedes earlier pending-status wording. No merge or license application is authorized. Actual outcomes are recorded separately; no result is prefilled by this approval.


### R2 pre-archive execution

All source work, six methods and individual assessments completed before joint archival; fresh results above reflect actual execution. The final combined archive guard is not yet observed. Retained R1 findings and outcomes remain in the historical ledger. No merge, effective license, new report or message.
