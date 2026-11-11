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
  status: pending
- id: TASK-002
  description: Reconcile the canonical policy and exact approved snapshot exclusions.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  status: pending
- id: TASK-003
  description: Reverify the existing approved terms, provenance and notices without changing the grant.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  status: pending
- id: TASK-004
  description: Reverify localized licensing guidance, navigation and H02 dependencies.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: pending
- id: TASK-005
  description: Execute R2 checks and record all 24 current acceptance and regression assessments.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: pending
- id: TASK-006
  description: Prepare the H01 acceptance package and reconcile the coordinated handoff.
  requirements:
  - REQ-004
  - REQ-006
  status: pending
review:
  revision: 2
  state: awaiting-approval
  blockers: []
  upstream:
    proposal: 5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7
    design: 5c77e32078568a63d9bde6361e72edd485c47dd10ca7ef7f1c490181720f920e
  approval: null
validation:
  plan_digest: null
  results: []
  assessments: []
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

- [ ] TASK-001 — Reconcile the current baseline, approved R2 scope and retained rights evidence.

  **Depends on:** Current Tasks R2 approval and applicable execution authorization for both coordinated changes.

  **Work:** Refresh private PR #37/main and public PR #4 read-only; compare with reviewed private head 1198c2cd2d39f69a12e4f5abae727725b577593a, main 0ed31390cc415c3c50c83c9e87bf347ad50fb608 and public head 97d7f4c1ceb76ea42cc37250fc47bdecec7a677b. Preserve unrelated work and the selected Harness 0.3.0 contract. Verify actual Proposal/Design/Tasks approvals for both changes and retain R1 source/provenance observations with their original dates and scope. Identify concrete drift; do not ask again for already recorded owner decisions.

  **Complete when:** Current sources and access limits are recorded, R2 planning bindings are current, and no unreviewed material drift is absorbed. Inventory is not export clearance.

  **Evidence/checks:** CHECK-001/002/006.

- [ ] TASK-002 — Reconcile the canonical policy and exact approved snapshot exclusions.

  **Depends on:** TASK-001; coordinate shared sources with H02 TASK-002.

  **Work:** Verify the existing licensing/publication Standard, its single index entry and the policy ledger against the approved requirements. Confirm CHECK-005 and CHECK-006 exclude only specs/archive/contribution-security-guidance/tasks.md in addition to the preexisting output directories. Keep peer Proposal/Requirements/Design, other historical Tasks, real sources and required suites included. Do not change validators, schemas, workflow code, releases or consumer refs. Preserve publish/defer/retain-private decision examples and per-product boundaries.

  **Complete when:** Canonical policy and the exact R2 scope match the approved Design; no broader exclusion, new waiver or effective license is introduced.

  **Evidence/checks:** CHECK-001/003/005/006.

- [ ] TASK-003 — Reverify the existing approved terms, provenance and notices without changing the grant.

  **Depends on:** TASK-001/002 and accessible existing approval/source records.

  **Work:** Inspect actual owner text approval and first-party attestation, notices and exact dependency-license records. Verify reviewed draft SHA-256 ba84ea407a9402c2e653bb4450ca79e0e9032582bf5c0283e16b3b45a3ddbb2c and status-only current SHA-256 e0909a27b460e4cb2a54d5f33e8b02a8f9dfcbab047a7a691c671e4f785e01c9. Retain component/third-party limits and the separation of tool/project terms. Do not rewrite legal clauses, apply LICENSE or request approval again for identical text. Actual changed rights/terms block the affected work and require the concrete appropriate review.

  **Complete when:** Exact terms/approval and required rights/notices evidence remain attributable and consistent with the current candidate. Approval remains distinct from application and H03 distribution.

  **Evidence/checks:** CHECK-002.

- [ ] TASK-004 — Reverify localized licensing guidance, navigation and H02 dependencies.

  **Depends on:** TASK-002/003.

  **Work:** Walk the existing EN/PT/ES licensing journeys and missing-evidence recovery. Resolve current local links and intended-access references; preserve optional private resources and independent public participation. Confirm H02 consumes the actual approved terms without importing them into project licensing. Only correct in-scope documentary defects if found; substantive changes reopen the affected gate.

  **Complete when:** Locales, permissions, links and source boundaries are aligned and current; no unsupported public availability or product adoption claim is added.

  **Evidence/checks:** CHECK-002/003/004.

- [ ] TASK-005 — Execute R2 checks and record all 24 current acceptance and regression assessments.

  **Depends on:** TASK-001–004; both approved task plans, stable relevant sources and coordinated H02 validation.

  **Work:** Execute all six approved methods with actual before/after snapshots, environment and evidence. For CHECK-006, reproduce the R1 cycle and R2 evidence-only stability in disposable copies, retain real-source/peer-plan/unrelated-history sensitivity and independent approval/failure rejection. Run selected planning/implementation as specified for both changes and the full maintained package suite for CHECK-005. Use a truthful pending ledger after preserving previous attempts; do not prefill passing placeholders. Record 18 local and six retained assessments, findings and actual results. Distinguish current source review from retained historical operational facts. Final closure auditing is not a prerequisite of CHECK-006.

  **Complete when:** Six actual current checks pass, all 24 obligations pass with valid mappings, snapshots match, stage/task binding is current and no open finding remains. A diagnosis or historical CI does not replace these results.

  **Evidence/checks:** CHECK-001–006.

- [ ] TASK-006 — Prepare the H01 acceptance package and reconcile the coordinated handoff.

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
