---
change: shortcut-git-convention
tasks:
  - id: TASK-001
    description: Assess the supplied convention against resolved Standards and existing enforcement
    requirements: [REQ-001, REQ-002, REQ-004]
    status: completed
  - id: TASK-002
    description: Update canonical Git and language policies
    requirements: [REQ-001, REQ-002]
    status: completed
  - id: TASK-003
    description: Connect SDD and PR review to Story traceability and document automation limits
    requirements: [REQ-003, REQ-004]
    status: completed
  - id: TASK-004
    description: Validate the repository and review acceptance scenarios
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
    status: completed
---

# Tasks

- [x] TASK-001 — Assess policy, language, process and enforcement impacts.
- [x] TASK-002 — Update canonical policies.
- [x] TASK-003 — Update traceability prompts and automation documentation.
- [x] TASK-004 — Run validation and record evidence.

## Dependencies

Mandatory policy review and required checks are merge prerequisites. A real Shortcut Story is needed to verify live Story association; none was supplied.

## Validation evidence

- `./scripts/validate/run.sh`: portable Plugin package and Harness structural validation passed.
- `git diff --check`: passed.
- Local Markdown links in changed documents resolve.
- REQ-001: reviewed Story branch examples and all three mappings; no-Story behavior explicitly prohibits fabricated IDs.
- REQ-002: English branches and commits, Spanish PRs, optional scope/body and multiple logical commits per Story are documented without historical migration or merge strategy changes.
- REQ-003: proposal and PR templates capture Story context; SDD workflows reference the resolved Git Standard; squash guidance preserves the commit format. Skills and profile composition remain unchanged.
- REQ-004: Git and release documentation distinguish the Shortcut extension from strict Conventional Commits; validator documentation explicitly excludes naming and external association checks.
- No executable behavior changed; no additional unit tests or agent evals apply to this documentation-only change.

## Delivery gates

Implementation and local validation are complete. Mandatory human policy review, remote required checks and merge are separate gates; this record does not claim approval. Live Shortcut linkage remains unverified because no Story or workspace integration context was supplied. Keep this change active until review, merge and archival requirements are satisfied.
