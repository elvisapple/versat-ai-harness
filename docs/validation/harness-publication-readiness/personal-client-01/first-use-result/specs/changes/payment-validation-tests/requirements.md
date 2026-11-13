---
sdd_version: 3
change: payment-validation-tests
requirements:
  - id: REQ-001
    statement: Regression tests demonstrate that an empty key is rejected without recording a charge.
    acceptance:
      - Given an empty recorded-key set and an empty-string key with amount 1, charging raises ValueError and the set remains empty.
      - Given a set containing an unrelated valid key and an empty-string key with amount 1, charging raises ValueError and the existing set is unchanged.
  - id: REQ-002
    statement: Regression tests demonstrate rejection of zero and negative amounts without consuming a valid key.
    acceptance:
      - Given an unseen nonempty key and amount 0, charging raises ValueError and the recorded-key set is unchanged.
      - Given an unseen nonempty key and amount -1, charging raises ValueError and the recorded-key set is unchanged.
      - Given a rejected zero or negative attempt for a key, a later attempt with the same key and amount 1 returns True and records that key exactly once.
  - id: REQ-003
    statement: Regression tests preserve duplicate prevention for already recorded keys.
    acceptance:
      - Given a successful charge for a key at amount 1, a second valid request with the same key returns False and leaves the recorded-key set unchanged.
      - Given a recorded key, another valid request for that key with a different positive amount returns False and leaves the recorded-key set unchanged.
  - id: REQ-004
    statement: Regression tests preserve successful charging of new valid keys.
    acceptance:
      - Given an empty recorded-key set, a nonempty key and amount 1, charging returns True and the set contains exactly that key.
      - Given one recorded key, charging a distinct nonempty key with amount 1 returns True and the set contains both keys.
---

# Requirements

## Actors and context

The actor is a maintainer validating the synthetic `charge` function against
`specs/product/payment.md`. No real customer, account or transaction is involved.

## Functional requirements

REQ-001 and REQ-002 cover validation errors and numeric boundaries. REQ-003
covers duplicate prevention, and REQ-004 retains the successful path. Together
they preserve all clauses of the existing living specification.

## Non-functional requirements

Assertions must observe exceptions, exact Boolean outcomes and recorded-key
state with deterministic synthetic inputs. Reuse adequate maintained tests and
retain the complete required unit suite. New tests must not require a network,
credentials, external accounts or production data.

## Acceptance scenarios

The frontmatter acceptance arrays are the authoritative scenario positions for
later Design coverage. These are proposed expectations, not executed results.
There are nine scenarios across four requirements.

## Constraints and assumptions

The bounded input domain is string keys, integer amounts and the existing
caller-supplied set. Empty means the empty string; whitespace normalization,
None, nonnumeric amounts, NaN/infinity, precision policy and concurrent calls
are not being newly specified. `ValueError` and unchanged state on rejected
requests preserve inspected behavior rather than introduce a new API.
No detailed method, task order or execution evidence is established at Gate 1.
There are no material unresolved decisions within this test-only scope.
