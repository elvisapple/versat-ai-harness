---
change: align-language-standard
requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
adrs: [ADR-0008, ADR-0010]
validation:
  - Repository structural validator
  - Codex Plugin validator
  - JSON, YAML and shell syntax checks
  - Git whitespace check
  - Repository-wide language scan
---

# Design

## Current state

Most schemas, Standards, Skills, project templates and validator documentation already use English. Root documentation, architecture documentation, accepted ADRs and several supporting READMEs use Portuguese. SDD templates use Spanish, and the internal Pull Request template correctly uses Spanish.

## Proposed design

Classify each tracked file by the artifact table in `standards/core/language.md`. Translate technical and structural artifacts to English, preserve Spanish content where the table explicitly requires it and leave language-neutral code and identifiers unchanged.

## Boundaries and contracts

- Do not rename files, paths, schema keys or identifiers.
- Do not change executable behavior.
- Keep `standards/core/language.md` as the only canonical policy.
- Keep the Plugin manifest within the supported schema.

## Data, security and permissions

The change does not process production data, credentials or customer information. It only updates repository text artifacts.

## Operations and observability

Validation output is the operational evidence for this documentation-only change.

## Migration, rollout and rollback

The branch contains a reviewable translation diff. Rollback consists of reverting the change before release; consumers remain unchanged until a versioned release is explicitly adopted.

## Alternatives considered

- Retain Portuguese through an exception: rejected because the canonical standard already defines English for these artifacts.
- Rewrite ADR-0008 in place: rejected because accepted decisions must preserve their history.
- Add locale-specific fields to `plugin.json`: rejected because unsupported manifest fields fail Plugin validation.

## Validation plan

Run the repository validator, the Codex Plugin validator, syntax checks for structured files and shell, `git diff --check`, link inspection and a repository-wide lexical scan.
