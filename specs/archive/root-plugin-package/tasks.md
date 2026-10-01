---
change: root-plugin-package
tasks:
  - id: TASK-001
    description: Record the root Plugin package architecture and migration
    requirements: [REQ-004]
    status: completed
  - id: TASK-002
    description: Move Plugin manifests, Skills and agent references to the repository root
    requirements: [REQ-001, REQ-002]
    status: completed
  - id: TASK-003
    description: Add the exact-version workspace marketplace catalog and installation guidance
    requirements: [REQ-003]
    status: completed
  - id: TASK-004
    description: Update deterministic validation for the root package contract
    requirements: [REQ-001, REQ-003, REQ-004]
    status: completed
  - id: TASK-005
    description: Run all required validation and record evidence
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
    status: completed
---

# Tasks

- [x] TASK-001 — Record the root Plugin package architecture and migration
- [x] TASK-002 — Move Plugin manifests, Skills and agent references to the repository root
- [x] TASK-003 — Add the exact-version workspace marketplace catalog and installation guidance
- [x] TASK-004 — Update deterministic validation for the root package contract
- [x] TASK-005 — Run all required validation and record evidence

## Dependencies

- Accepted package-boundary direction from the repository owner.
- Canonical architecture and language Standards.
- Agent Plugins portable manifest and ChatGPT workspace marketplace contracts.

## Validation evidence

- `./scripts/validate/run.sh`
- `python3 /Users/elviszoz/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .`
- `python3 /Users/elviszoz/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<skill>` for every Skill
- JSON parsing for `plugin.json`, `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`
- `bash -n scripts/validate/run.sh`
- `git diff --check`
