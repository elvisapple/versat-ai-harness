---
sdd_version: 3
change: payment-validation-coverage
status: proposed
owner: Synthetic evaluator
summary: Strengthen regression coverage of the existing payment validation contract.
risk: medium
impact:
  state: assessed
  summary: Preserve the living payment contract and extend maintained test coverage;
    no product behavior change or historical origin is claimed.
  items:
  - current_contract:
      path: specs/product/payment.md
      locator: Payment requires a nonempty key and positive amount. A key may be charged
        only once; duplicates return False. New charges return True.
      digest: 46a4d95d4458d55ce93d10aae8bdadcb9c60263aecf16f1bb3dd8163df955aaf
    effect: preserve
    targets:
    - REQ-001
    - REQ-002
    - REQ-003
    reason: Keep existing validation and duplicate prevention while filling meaningful
      test gaps.
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream: {}
  approval: null
---

# Proposal

## Context and problem

The synthetic payment-fixture project uses Harness 0.4.0, the software profile, finance domain and Python. Its exact resolved Standards match the installed provider and lockfile hashes. The living specification is `specs/product/payment.md`.

`src/payment.py` validates the key and amount before changing the supplied set, raises `ValueError` for an empty key or nonpositive amount, returns `False` for a previously seen key, and adds a new key before returning `True`. Source inspection is not execution evidence.

`tests/test_payment.py` already covers a new charge, one duplicate, zero amount and an empty string key. It lacks explicit negative-amount coverage and assertions that invalid or duplicate attempts preserve the set. No active or archived change dossiers exist, so no historical requirement origin is available.

## Expected outcome

Maintained regression tests protect the documented acceptance rules and observed rejection behavior. Callers can distinguish a new charge from a duplicate, and invalid attempts do not consume a key. Existing adequate cases remain usable.

## Scope

Plan a test-focused change for empty string keys, zero and negative amounts, valid new charges and repeated keys. Verify observable return values, exceptions and set contents. Preserve the required unit suite declared in `.versat/validation.yaml`.

## Out of scope

Product implementation changes, payment providers, money movement, persistence, concurrency guarantees, input normalization, new numeric types, credentials, external services and publication are outside this change. No Design, Tasks or implementation is authorized at this gate.

## Work tracking

No Story or issue is associated with this synthetic scenario. No identifier is invented. The synthetic directory has no local Git metadata; branch, PR and remote control state are unavailable. Planning remains local and uses `payment-validation-coverage` as the stable ID.

## Impact and risks

The current contract is preserved. Coverage must distinguish zero from a negative amount and prove that rejection does not mutate existing state. The fixture's medium criticality is retained because it models payment acceptance, although no real transactions occur. Public interface behavior and documented usage remain unchanged; no new usage guide or architectural boundary is proposed.

## Current contract baseline

The living specification requires a nonempty key and positive amount, permits charging a key only once, returns `False` on duplicate keys and `True` on new charges. Code inspection additionally establishes `ValueError` on invalid inputs and validation before set mutation. These observed details are proposed for regression coverage without claiming they appear verbatim in the living specification.

## Proposal acceptance criterion

The combined Proposal and Requirements define reviewable, observable success, error and boundary scenarios for the existing contract, retain required regression coverage, and explicitly await human approval before Design.

## Planning review

Gate 1, Proposal/Requirements revision 1, is awaiting approval. No human approval has been observed. There are no material planning blockers. Approval of this revision unlocks Design only. This is a synthetic bounded evaluation, not production acceptance.
