---
sdd_version: 3
change: payment-validation-tests
requirements:
  - id: REQ-001
    statement: Maintained tests demonstrate that an empty key is rejected without changing the caller's seen keys.
    acceptance:
      - Given seen contains an existing synthetic key, calling charge with an empty string key and amount 1 raises ValueError and leaves seen unchanged.
  - id: REQ-002
    statement: Maintained tests demonstrate rejection of zero and negative amounts without consuming a valid key.
    acceptance:
      - Given a fresh seen set and an unused nonempty key, amount 0 raises ValueError and leaves seen empty; a subsequent call for that key with amount 1 returns True.
      - Given a fresh seen set and an unused nonempty key, amount -1 raises ValueError and leaves seen empty; a subsequent call for that key with amount 1 returns True.
  - id: REQ-003
    statement: Maintained tests demonstrate that a previously charged key cannot be charged again within the same caller-owned seen set.
    acceptance:
      - Given a successful charge for a key at amount 1, repeating that key at amount 1 returns False and leaves seen unchanged.
      - Given a successful charge for a key at amount 1, repeating that key at a different positive amount of 2 returns False and leaves seen unchanged.
  - id: REQ-004
    statement: Maintained tests preserve successful charging of distinct valid keys and existing regression coverage.
    acceptance:
      - Given an empty seen set, a nonempty key and amount 1, charge returns True and seen contains exactly that key.
      - Given one successfully charged key, charging a different nonempty key at amount 1 returns True and seen contains both keys.
      - The required unit suite retains the existing success, duplicate, zero-amount and empty-key coverage and includes the new meaningful cases without skipped or empty coverage replacing those assertions.
---

# Requirements

## Actors and context

The caller owns the in-memory seen set. A maintainer uses automated tests to
check the existing payment contract. All inputs are synthetic and no external
service participates.

## Functional requirements

REQ-001 and REQ-002 cover invalid input. REQ-003 covers duplicate prevention.
REQ-004 retains successful behavior and the existing maintained regressions.
Acceptance-array positions in the metadata are the canonical scenarios; no
additional case catalog is introduced.

## Non-functional requirements

Tests must be deterministic, independent of execution order and based on
observable exceptions, return values and caller-visible state. They must reuse
adequate tests and run within the project's required unit-suite contract.
Future execution evidence must distinguish actual scenario observations from
structural validation. No product runtime or security-isolation guarantee is
introduced.

## Acceptance scenarios

The frontmatter defines eight scenarios covering empty input, the zero boundary,
a negative amount, same-key repetition, changed-amount repetition, first success,
distinct-key success and preservation of the required suite. They describe
required observations, not completed checks.

## Constraints and assumptions

Harness 0.4.0 remains pinned. The living specification is the authority for
product behavior. The existing implementation grounds the assumed ValueError
and unchanged-state semantics proposed for preservation. Inputs here are
string keys and integer amounts; the specification does not define a broader
type or whitespace contract. No historical origin dossiers are available.
Existing tests are inspected but have not been run in this planning stage.
No approval, implementation authority, CI result, merge or delivery is inferred.
