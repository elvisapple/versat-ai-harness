---
change: consolidate-sdd-workflow
tasks:
  - id: TASK-001
    description: Consolidate the public SDD entry point and lifecycle documentation
    requirements: [REQ-001, REQ-002, REQ-003]
    status: completed
  - id: TASK-002
    description: Add versioned schemas, templates and deterministic SDD validation
    requirements: [REQ-002, REQ-004, REQ-005]
    status: completed
  - id: TASK-003
    description: Record the architecture decision, legacy compatibility and developer guidance
    requirements: [REQ-001, REQ-003, REQ-005, REQ-006]
    status: completed
  - id: TASK-004
    description: Add behavioral tests and integrate the checks into repository validation and CI
    requirements: [REQ-004, REQ-006]
    status: completed
---

# Tasks

- [x] TASK-001 — Consolidate the public SDD entry point and lifecycle documentation
- [x] TASK-002 — Add versioned schemas, templates and deterministic SDD validation
- [x] TASK-003 — Record the architecture decision, legacy compatibility and developer guidance
- [x] TASK-004 — Add behavioral tests and integrate the checks into repository validation and CI

## Dependencies

- The developer's review and authorization to implement the consolidated proposal.
- Existing Standards, SDD history and portable Plugin validation contract.

## Progress

The consolidation was implemented in the same local branch. This legacy transition dossier intentionally has no retrospective v2 approvals; its immutable allowlist entry records that constraint.

## Validation evidence

- Repository package validation and the SDD behavioral tests are run by `scripts/validate/run.sh` with `requirements-validation.txt` installed.
- Surviving skills are structurally checked with `skill-creator`'s validator.
- The final working-tree diff receives a whitespace check before handoff.

## Delivery

This dossier documents local implementation preparation only. It does not claim that a pull request was opened, reviewed, merged or deployed.
