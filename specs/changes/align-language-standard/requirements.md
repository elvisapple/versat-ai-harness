---
change: align-language-standard
requirements:
  - id: REQ-001
    statement: Technical and structural artifacts use English
    acceptance:
      - Legacy Portuguese technical documentation is translated to English
      - Spanish SDD templates are translated to English
  - id: REQ-002
    statement: Artifact-specific Spanish content is preserved
    acceptance:
      - The internal Pull Request template remains in Spanish
  - id: REQ-003
    statement: The historical language decision agrees with the canonical policy lineage
    acceptance:
      - ADR-0008 is marked as superseded
      - A new ADR records the refined language policy
  - id: REQ-004
    statement: Updated repository and Plugin contracts remain valid
    acceptance:
      - Repository structural validation passes
      - Plugin validation passes
      - JSON, YAML and shell syntax checks pass
---

# Requirements

## Functional requirements

- REQ-001: Every existing technical or structural text artifact MUST use English.
- REQ-002: Content assigned to Spanish by the language standard MUST NOT be translated to English.
- REQ-003: Accepted ADR history MUST be preserved when reconciling the language policy.
- REQ-004: Translation changes MUST preserve valid repository and Plugin contracts.

## Non-functional requirements

- Translations MUST preserve the intent and normative strength of the source content.
- File paths, identifiers, schema keys and executable behavior MUST remain stable unless required by the language policy.

## Acceptance scenarios

- A repository-wide lexical scan finds non-English technical content only where explicitly permitted.
- Every updated reference resolves to an existing file.
- All documented validation commands complete successfully.

## Constraints and assumptions

- `standards/core/language.md` is the canonical policy.
- The Codex Plugin manifest schema accepts canonical English interface metadata and no locale-specific manifest fields.
