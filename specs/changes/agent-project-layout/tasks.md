---
change: agent-project-layout
tasks:
  - id: TASK-001
    description: Define the canonical artifact contract and record the ADR
    requirements: [REQ-002, REQ-004]
    status: completed
  - id: TASK-002
    description: Update the agent module and provide authoring artifacts and workflow example
    requirements: [REQ-001, REQ-003]
    status: completed
  - id: TASK-003
    description: Reconcile current documentation and migration guidance
    requirements: [REQ-002, REQ-004]
    status: completed
  - id: TASK-004
    description: Validate composition, syntax, links and acceptance scenarios
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
    status: completed
---

# Tasks

- [x] TASK-001 — Define canonical contracts and ADR.
- [x] TASK-002 — Reformulate templates and examples.
- [x] TASK-003 — Review all documentation and update current guidance.
- [x] TASK-004 — Validate and record evidence.

## Validation evidence

- `./scripts/validate/run.sh`: portable Plugin package and Harness structural validation passed.
- `git diff --check`: passed.
- Python 3.11 with the available PyYAML and standard-library TOML parser: repository YAML/TOML syntax, Skill and agent required metadata, Standards index references and SDD task traceability passed.
- Temporary-directory composition smoke checks followed the documented overlay contract for both agent and hybrid profiles: expected hidden directories exist, root consumer `skills/` and `agents/` are absent, base files retain their contents, architecture guidance is copied, hybrid preserves `src/` and `infra/`, and no authoring placeholders or examples become active artifacts. These checks do not constitute an implemented bootstrap product.
- Local Markdown links across repository documentation resolve. Existing Plugin manifests, version pins and canonical package paths are preserved.
- Manual acceptance review and documentation coverage are recorded in [documentation-review.md](documentation-review.md).
- No live service calls or deployed agent behavior changed. Consumer discovery and integration checks remain separate from these local checks.

## Delivery gates

Mandatory human policy review, remote required checks and merge are separate gates. Keep this change active until those gates and archival requirements are satisfied.
