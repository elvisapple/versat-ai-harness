---
change: consolidate-sdd-workflow
requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]
adrs: [ADR-0013]
validation:
  - Repository package and SDD validator execution
  - SDD validator behavioral test suite
  - Skill structural validation
  - Git whitespace check
---

# Design

## Current state

The repository stored useful SDD material in parallel entry points, Markdown workflow documents and unenforced metadata. The old schemas support existing completed dossiers but cannot express human-gate provenance or evidence readiness.

## Proposed design

`skills/versat-sdd/SKILL.md` is a concise router to `sdd/process.md`. The process owns lifecycle semantics; `sdd/workflows/` owns the four step procedures; `sdd/README.md` and `sdd/metadata.md` explain developer prompts and artifact data. Planning applies three sequential approval gates, after which execution requires explicit user authority.

The v2 schemas and `validators/sdd/validate.py` locally evaluate document shape, stable content digests, approvals, traceability, task checkboxes and recorded evidence. The validator is deliberately non-networked and reports unavailable verification separately from an observed failed result.

Legacy schemas remain under `sdd/schemas/legacy/`. `sdd/legacy-changes.json` allows only the exact old dossiers plus this transitional one by raw file hash. It is a compatibility record, not a statement that historical gates happened.

## Boundaries and contracts

- `sdd/process.md` is lifecycle authority; skills route to it.
- `sdd/workflows/` is procedural guidance, not an executable engine.
- `sdd/schemas/` and `validators/sdd/` form the local data contract.
- `docs/decisions/0013-consolidated-sdd-workflow.md` records the architectural decision.
- Archive preparation is documentary branch work; remote merge confirmation remains outside the validator.

## Data, security and permissions

Approval records retain only a user-visible source and quote. They bind content via digest but do not authenticate a person. Evidence paths cannot escape the repository or use symlinks; HTTPS evidence is recorded but never fetched. No credentials, connector or Git mutation is introduced.

## Operations and observability

`requirements-validation.txt` pins the local validator dependencies. `scripts/validate/run.sh` and CI run the structural validation, SDD validator and behavioral tests. The CLI provides structured output and nonzero statuses for fail or unable-to-verify states.

## Migration, rollout and rollback

New dossiers use v2 templates immediately. Existing history remains byte-identical under the allowlist. A historical dossier that needs further execution or delivery must be deliberately migrated through current gates. Rolling back the consolidation restores the prior documentation and removes the new validation dependency; it does not rewrite historical records.

## Alternatives considered

- Keep both skills: rejected because developers must choose between overlapping entry points.
- Turn every workflow document into a separate public skill: rejected because four public commands obscure the lifecycle state rather than clarify it.
- Archive only after merge in a second branch and pull request: rejected because it separates implementation from its documentary record without proving more.
- Add fictional v2 approval records to old dossiers: rejected because that would misrepresent history.

## Validation plan

Run package validation, the SDD validator and its synthetic behavioral suite with the pinned dependencies; structurally validate each surviving skill; and run `git diff --check`. Verify that the central guide, process and ADR agree on routing, planning gates and archive semantics.
