---
sdd_version: 3
change: test-payment-validation
requirements:
- id: REQ-001
  statement: Tests must verify that an empty payment key is rejected without recording
    a charge.
  acceptance:
  - Given an empty recorded-key set, an empty string key and amount 1, charge raises
    ValueError and the set remains empty.
  - Given an existing unrelated recorded key, an empty string key and amount 1, charge
    raises ValueError and the existing set remains unchanged.
- id: REQ-002
  statement: Tests must verify that nonpositive payment amounts are rejected without
    recording a charge.
  acceptance:
  - Given an unused nonempty key and amount 0, charge raises ValueError and the recorded-key
    set remains unchanged.
  - Given an unused nonempty key and amount -1, charge raises ValueError and the recorded-key
    set remains unchanged.
- id: REQ-003
  statement: Tests must preserve successful charging of a new key with a positive
    amount.
  acceptance:
  - Given an empty recorded-key set, unused key a and amount 1, charge returns True
    and the set contains exactly a.
  - Given a set containing a, unused key b and amount 1, charge returns True and the
    set contains a and b.
- id: REQ-004
  statement: Tests must preserve duplicate prevention based on the payment key.
  acceptance:
  - After a successful charge of key a with amount 1, submitting a again with amount
    1 returns False and the recorded-key set is unchanged.
  - After a successful charge of key a with amount 1, submitting a again with amount
    2 returns False and the recorded-key set is unchanged.
---

# Requirements

## Actors and context

Callers submit a key and amount to `src/payment.py:charge` with a caller-owned set of already charged keys. Maintainers need reliable regression observations for the existing product contract in `specs/product/payment.md`.

## Functional requirements

REQ-001 covers empty keys; REQ-002 covers zero and negative amounts; REQ-003 retains valid new-charge success; REQ-004 retains key-based duplicate prevention. The ordered acceptance arrays above are the authoritative scenario positions for later Design coverage.

## Non-functional requirements

Checks must be deterministic, run with synthetic in-memory data and inspect outcomes and meaningful state invariants. Reuse adequate existing tests and preserve the consumer's required unit suite. Tests must remain independent and require no external service or credentials.

## Acceptance scenarios

Exercise each invalid input independently with its other arguments valid. Observe both the exception/Boolean outcome and the set contents. Retain successful payment checks alongside rejection checks. A duplicate is identified by the same key even if the positive amount differs.

## Constraints and assumptions

This is a test-coverage change preserving existing behavior, not authorization to change runtime code. Empty string is the concrete empty-key case; numeric zero and -1 are representative nonpositive amounts. Whitespace policy, new input types, real charging, persistence and concurrency are outside scope. Error-message wording is not an acceptance requirement. Test execution and detailed check selection belong to subsequent approved stages.
