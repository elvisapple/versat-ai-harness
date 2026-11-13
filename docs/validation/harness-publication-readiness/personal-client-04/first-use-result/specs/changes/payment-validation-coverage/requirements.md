---
sdd_version: 3
change: payment-validation-coverage
requirements:
- id: REQ-001
  statement: Maintained tests shall protect rejection of an empty string payment key
    without changing charge state.
  acceptance:
  - Given an empty string key, a positive amount and a set containing an unrelated
    key, charging raises ValueError and leaves the set unchanged.
- id: REQ-002
  statement: Maintained tests shall protect rejection of zero and negative amounts
    without consuming a valid payment key.
  acceptance:
  - Given an unseen nonempty key and amount zero, charging raises ValueError and leaves
    the set unchanged.
  - Given an unseen nonempty key and a negative amount, charging raises ValueError
    and leaves the set unchanged.
  - Given a key rejected for a nonpositive amount, a subsequent positive charge using
    that same key returns True and adds that key exactly once.
- id: REQ-003
  statement: Maintained tests shall protect successful new charges and key-based duplicate
    prevention.
  acceptance:
  - Given an unseen nonempty key and a positive amount, charging returns True, adds
    the key and preserves any unrelated existing keys.
  - Given a previously charged key and a positive amount, repeated calls return False
    and leave the set unchanged, including when the positive amount differs from the
    original charge.
  - Given an existing charged key, a different unseen key with a positive amount still
    returns True and both keys remain recorded.
---

# Requirements

## Actors and context

The caller invokes the local `charge(seen, key, amount)` function. Maintainers use regression tests to preserve the existing synthetic payment contract. The governing product source is `specs/product/payment.md`; implementation and existing tests supply the observed exception and state behavior.

## Functional requirements

REQ-001 covers empty-key rejection. REQ-002 covers the nonpositive boundary and retry after invalid input. REQ-003 covers positive acceptance, repeated-key rejection and independent keys. The ordered acceptance arrays above are the normative scenario positions for later traceability.

## Non-functional requirements

Tests must be deterministic, local and independent of production data, credentials or external systems. Retain the declared required unit suite and adequate current tests. A later structural validator pass cannot substitute for actual acceptance execution.

## Acceptance scenarios

The metadata lists the observable return values, exceptions and state invariants. This planning stage records no executed acceptance results and makes no implementation or delivery readiness claim.

## Constraints and assumptions

Use exact Harness 0.4.0 and the Standards resolved through its index and the project lockfile. Preserve product behavior. Empty means the empty string for this bounded scope; whitespace normalization and other input types are not new requirements. Representative integer amounts are sufficient for the specified positive/nonpositive boundary. Duplicate prevention is scoped to the supplied in-memory set; no durability, concurrency or provider-side guarantee is implied. Error message wording is not part of the contract. No material unresolved decision prevents Gate 1 review.
