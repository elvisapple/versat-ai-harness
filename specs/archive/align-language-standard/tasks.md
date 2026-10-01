---
change: align-language-standard
tasks:
  - id: TASK-001
    description: Audit tracked repository artifacts by required language
    requirements: [REQ-001, REQ-002]
    status: completed
  - id: TASK-002
    description: Translate non-compliant technical and structural artifacts
    requirements: [REQ-001, REQ-004]
    status: completed
  - id: TASK-003
    description: Record the refined language decision without rewriting ADR history
    requirements: [REQ-003]
    status: completed
  - id: TASK-004
    description: Run repository, Plugin and syntax validation
    requirements: [REQ-004]
    status: completed
---

# Tasks

- [x] TASK-001 — Audit tracked repository artifacts by required language
- [x] TASK-002 — Translate non-compliant technical and structural artifacts
- [x] TASK-003 — Record the refined language decision without rewriting ADR history
- [x] TASK-004 — Run repository, Plugin and syntax validation

## Dependencies

- Canonical language policy at `standards/core/language.md`.
- Architecture and ADR evolution rules.

## Validation evidence

- `./scripts/validate/run.sh`
- Codex Plugin validator
- JSON, YAML and shell syntax checks
- `git diff --check`
- repository-wide lexical scan
