---
sdd_version: 2
change: quickstart-scenario-coverage
tasks:
- id: TASK-001
  description: Define concise living first-use documentation policy and review guide selection and content scenarios.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  status: completed
- id: TASK-002
  description: Clarify proportional acceptance-scenario coverage in the Testing Standard and review coverage gaps and test
    reuse.
  requirements:
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-003
  description: Apply documentation and scenario-coverage policy in existing SDD procedures and the developer guide, then verify
    representative change paths.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-004
  description: Align shared README and bootstrap guidance and verify conditional first-use links across base/profile composition.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-006
  status: completed
- id: TASK-005
  description: Complete integrated scope and link review, run required repository checks and record actual evidence without
    concealing baseline failures.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 5a1170e5847ce0e113aa1ea89032a5e27b63ec9619db62c5e292636a5a317f7f
    design: 7cc446787e408799dda5f5148d078c7cd891542096ca55af9b0c638ef2e33b6c
  approval:
    source: Developer message in this conversation approving the presented Tasks R1 and explicitly authorizing implementation
    quote: Aprovo as tasks e autorizo a implementação
    revision: 1
    digest: aa7006716772e96fa2f356a714418c03af7f3d9adcca09998bbf3eee6f14ce67
validation:
  plan_digest: aa7006716772e96fa2f356a714418c03af7f3d9adcca09998bbf3eee6f14ce67
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/quickstart-scenario-coverage/review.md
    revision: working-tree source snapshot 671e90e76e44aced6859b8f5a8abd20b244b6ae016ea3aedcb4fa07ab3cfa406; base 0b0471f7b0fcaa0e4784892197439f8c61ffba48
  - check: CHECK-002
    result: pass
    evidence: docs/validation/quickstart-scenario-coverage/review.md
    revision: working-tree source snapshot 671e90e76e44aced6859b8f5a8abd20b244b6ae016ea3aedcb4fa07ab3cfa406; base 0b0471f7b0fcaa0e4784892197439f8c61ffba48
  - check: CHECK-003
    result: pass
    evidence: docs/validation/quickstart-scenario-coverage/review.md
    revision: working-tree source snapshot 671e90e76e44aced6859b8f5a8abd20b244b6ae016ea3aedcb4fa07ab3cfa406; base 0b0471f7b0fcaa0e4784892197439f8c61ffba48
  - check: CHECK-004
    result: pass
    evidence: docs/validation/quickstart-scenario-coverage/review.md
    revision: source snapshot 671e90e76e44aced6859b8f5a8abd20b244b6ae016ea3aedcb4fa07ab3cfa406; compatibility manifest SHA-256 65f3ba86bffe56116c65ba07123d2281eeb2e0ce649bb7881a82dede934ae097
  - check: CHECK-005
    result: pass
    evidence: docs/validation/quickstart-scenario-coverage/review.md
    revision: source snapshot 671e90e76e44aced6859b8f5a8abd20b244b6ae016ea3aedcb4fa07ab3cfa406; compatibility manifest SHA-256 65f3ba86bffe56116c65ba07123d2281eeb2e0ce649bb7881a82dede934ae097
closure: active
---

# Tasks

- [x] TASK-001 — Define concise living first-use documentation policy and review guide selection and content scenarios.
- [x] TASK-002 — Clarify proportional acceptance-scenario coverage in the Testing Standard and review coverage gaps and test reuse.
- [x] TASK-003 — Apply documentation and scenario-coverage policy in existing SDD procedures and the developer guide, then verify representative change paths.
- [x] TASK-004 — Align shared README and bootstrap guidance and verify conditional first-use links across base/profile composition.
- [x] TASK-005 — Complete integrated scope and link review, run required repository checks and record actual evidence without concealing baseline failures.

## Dependencies

All work requires approval of this Tasks revision and an explicit implementation request. TASK-001 and TASK-002 have no implementation dependencies on each other. TASK-003 depends on both. TASK-004 depends on TASK-001. TASK-005 integrates TASK-001 through TASK-004 and can complete only when required checks pass. Tests and documentation reviews accompany each implementation task; TASK-005 consolidates evidence and checks cross-file consistency.

The known `bootstrap-product-context` metadata/schema failure blocks completion of TASK-005, not review of this plan or the independent implementation tasks. Its repair is outside this approved scope. Once implementation is authorized, run unaffected checks and report the observed baseline outcome; do not edit the historical dossier, its exemption manifest or validation rules to make this task pass. If the failure persists, mark the task blocked and do not claim delivery readiness. All task statuses remain pending during planning because the current validator treats any other status as execution having started.

## Task details and completion conditions

### TASK-001 — First-use documentation policy

Update `standards/core/documentation.md` with the approved guide content, default location, reuse of equivalent documentation, README discovery, optional supporting guides and updates with implemented behavior. Keep language/security rules referenced through existing Standards rather than redefined. Do not introduce a standalone quickstart template or generate a guide for a hypothetical consumer.

**Completion:** review the policy against usable CLI, graphical workflow, existing guide/README section and empty-scaffold cases from CHECK-001. It must yield meaningful first-use instructions when needed, stable links outside the dossier and no empty artifacts or duplicate setup content. Confirm documented examples are subject to actual verification and unavailable access is not treated as success. Retain observations for CHECK-001, CHECK-002 and CHECK-004 evidence.

### TASK-002 — Relevant scenario coverage

Update `standards/core/testing.md` to address relevant success, error and boundary scenarios in proportion to risk, reuse adequate existing tests and surface coverage gaps. Preserve behavior-focused testing, regression guidance and existing CI obligations.

**Completion:** perform CHECK-003's comparison of happy-path-only evidence, incomplete error/boundary coverage and sufficient preexisting tests. The policy must expose missing relevant coverage while permitting test reuse and concise low-risk checks. Confirm it introduces no scenario IDs, fixed case count, coverage quota or mandatory TDD. Retain the review for CHECK-003 and CHECK-004 evidence.

### TASK-003 — SDD integration and developer guidance

Update `sdd/workflows/new-change.md`, `sdd/workflows/implement-change.md`, `sdd/workflows/validate-change.md` and `sdd/README.md` as specified by the approved Design. Apply policy through existing acceptance scenarios, check methods, documentation tasks and result records. Keep path/content conventions in the Documentation Standard and use references from procedural guidance.

**Completion:** perform CHECK-002 for a changed setup command, changed UI action, internal-only refactor and later revision of an existing workflow. Documentation work must follow affected behavior; unrelated changes must not acquire unnecessary documentation tasks. Validation must compare observed and expected usage outcomes, permit shared functional/documentation evidence and report unavailable checks as unverified. Reapply CHECK-003 to confirm one linked passing check cannot conceal uncovered relevant scenarios. Verify the developer guide describes these changes without a new phase, artifact or gate.

### TASK-004 — Conditional README and bootstrap guidance

Update `project-templates/base/README.md`, `project-templates/README.md` and `skills/project-bootstrap/references/project-lifecycle.md`. The shared README prompt must resolve to the actual guide/section only when present, and be omitted when there is no meaningful first-use content. Bootstrap applies the resolved policy instead of restating it. Keep profile modules and directory manifests unchanged.

**Completion:** use temporary illustrative layouts for CHECK-001 and inspect base/profile composition for CHECK-004. Verify an actual guide link, an existing README-section anchor, a supporting guide and an empty scaffold. Simulate dossier archival and confirm README/guide links remain valid. Check software, agent, hybrid, library and infrastructure guidance all reuse the base contract without copied policy or mandatory empty files. These walkthroughs do not claim an automated composer or actual consumer adoption.

### TASK-005 — Integrated validation and evidence

Review the combined guidance for consistency with all six requirements and execute CHECK-004 and CHECK-005. Run `git diff --check`, inspect untracked files and changed Markdown targets, then run `./scripts/validate/run.sh` with the declared dependencies. Use the phase-appropriate SDD validation command from Design. Re-run earlier checks only when subsequent edits affect their conclusions.

Consolidate observations from CHECK-001 through CHECK-005 using the existing evidence contract: one result per Design check, the current Tasks plan digest, actual tested revision/run and stable evidence locations. A compact evidence file under `docs/validation/quickstart-scenario-coverage/` may hold local walkthrough observations and command outcomes; it is check evidence, not a new mandatory report type. Keep temporary illustrative layouts out of consumer templates.

**Completion:** required checks pass, meaningful scenario outcomes and link/scope review are recorded, all evidence corresponds to the current work and no external review, CI, merge or release is inferred. The package-wide baseline failure must be genuinely resolved under separate authorization before this task can complete. Until then, record the actual failure, retain completed independent work and report the blocker.

## Planning review

The developer approved the presented Tasks R1 and explicitly authorized implementation with "Aprovo as tasks e autorizo a implementação". The canonical Tasks digest was computed before recording this approval. Proposal/Requirements R1 and Design R1 retain their current approvals. The known repository validation failure remains a completion blocker, not an unresolved planning decision.

## Progress

TASK-001 through TASK-004 are implemented and their focused checks passed. Nine existing source files changed; no new template, validator or consumer file was created. The first integrated run left TASK-005 blocked by the preexisting `bootstrap-product-context` SDD schema failure. The developer subsequently authorized the proposed compatibility correction with "Ok execute." The exact historical dossier hashes were registered in the existing legacy manifest; no historical artifact or validator changed. The full package check then passed, completing TASK-005.

## Validation evidence

CHECK-001 through CHECK-004 passed for the current source snapshot. CHECK-004 was reviewed again after the authorized compatibility correction. CHECK-005 passed on the complete repository check: package structure, SDD contract and all 48 validator tests. The earlier failure remains in the [observations and command results](../../../docs/validation/quickstart-scenario-coverage/review.md), along with the source manifest, illustrative layout checks, manual instruction walkthroughs and limitations. Evidence uses the approved Tasks plan digest, actual working-tree source snapshot and the exact compatibility manifest hash, not an inferred merge revision.

## Delivery

Closure remains active while PR #8 receives its final CI run and required review. Implementation, the historical compatibility correction and PR publication were authorized in this conversation. Local checks do not assert remote CI or human review; merge and release remain separate decisions.
