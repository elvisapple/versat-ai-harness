---
sdd_version: 3
change: change-id
tasks:
  - id: TASK-001
    description: Verifiable deliverable
    requirements: [REQ-001]
    status: pending
review:
  revision: 1
  state: draft
  blockers: []
  upstream:
    proposal: REPLACE_WITH_APPROVED_PROPOSAL_DIGEST
    design: REPLACE_WITH_APPROVED_DESIGN_DIGEST
  approval: null
validation:
  plan_digest: null
  results: []
  assessments: []
  findings: []
closure: active
---

# Tasks

- [ ] TASK-001 — Verifiable deliverable

## Dependencies

Replace upstream placeholders with the current approved digests. All requirements need task coverage. Keep checklist status aligned with metadata; approval alone does not complete a task.

## Planning review

Record the actual human response for this plan revision. Tasks approval ends planning; implementation requires an explicit request.

## Progress

Record execution notes here without changing the approved task scope.

## Validation evidence

Populate metadata results using the Design CHECK identifiers, current Tasks digest, matching input snapshots taken before/after execution and observed context. Assess each local scenario and retained regression obligation against current implementation, even with every task checked. Reuse stable findings until resolved; new task-plan content reopens the appropriate gate. Record real evidence at stable repository-relative paths or HTTPS URLs, with the observed revision. A recorded pass is not proof that remote CI, human review or merge occurred.

## Delivery

Set closure to prepared only when delivery validation passes. Preparing the dossier in this branch does not assert merge or deployment. Record externally observed delivery evidence separately.
