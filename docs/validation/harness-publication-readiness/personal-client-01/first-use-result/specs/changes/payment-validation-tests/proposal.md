---
sdd_version: 3
change: payment-validation-tests
status: proposed
owner: Synthetic evaluator
summary: Strengthen payment validation regression tests while preserving the existing payment contract.
risk: medium
impact:
  state: assessed
  summary: Preserve the existing payment specification and extend test coverage for negative amounts and state invariants; no historical dossiers exist in this fixture.
  items:
    - current_contract:
        path: specs/product/payment.md
        locator: "Payment requires a nonempty key and positive amount."
        digest: 46a4d95d4458d55ce93d10aae8bdadcb9c60263aecf16f1bb3dd8163df955aaf
      effect: preserve
      targets: [REQ-001, REQ-002]
      reason: Retain rejection of empty keys and nonpositive amounts while making negative and state-preservation cases observable.
    - current_contract:
        path: specs/product/payment.md
        locator: "A key may be charged only once; duplicates return False."
        digest: 46a4d95d4458d55ce93d10aae8bdadcb9c60263aecf16f1bb3dd8163df955aaf
      effect: preserve
      targets: [REQ-003]
      reason: Retain duplicate prevention for a previously accepted key without altering the recorded key set.
    - current_contract:
        path: specs/product/payment.md
        locator: "New charges return True."
        digest: 46a4d95d4458d55ce93d10aae8bdadcb9c60263aecf16f1bb3dd8163df955aaf
      effect: preserve
      targets: [REQ-004]
      reason: Keep successful valid charges and independent keys working while strengthening rejection coverage.
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream: {}
  approval: null
---

# Proposal

## Context and problem

The synthetic payment-fixture project uses Harness 0.4.0, the software profile,
finance domain, medium criticality and Python. Its selected Standards resolve
through the installed provider's index and match all twelve lockfile digests.
The authoritative product contract is `specs/product/payment.md`.

Inspection of `src/payment.py` shows that `charge(seen, key, amount)` raises
`ValueError` for empty keys and amounts at or below zero, returns `False` for
previously recorded keys, and otherwise records the key and returns `True`.
Inspection of `tests/test_payment.py` shows existing positive, duplicate,
zero-amount and empty-key cases. Negative amounts and preservation of the
recorded keys on rejected or duplicate requests lack explicit assertions.
These are inspection findings, not observed test-execution results.

## Expected outcome

Maintainers can detect regressions in rejection, duplicate prevention and
successful charging through meaningful synthetic unit-test assertions. The
existing public behavior remains unchanged.

## Scope

Preserve adequate existing tests and extend coverage for empty keys, zero and
negative amounts, duplicate requests and successful distinct keys. Assert the
observable return values or exceptions and resulting recorded-key state.
Use synthetic in-memory values only. Retain the required `unit` suite declared
in `.versat/validation.yaml`; detailed check planning belongs to Design.

## Out of scope

Production payments, external services, credentials, persistence, concurrency,
refunds, currency calculations, retries across processes, new key normalization,
new input-type rules and changes to the payment interface are excluded.
This stage does not modify implementation, tests or the living specification.

## Work tracking

No Story or issue is associated with this synthetic evaluation. No Git metadata
exists inside the supplied fixture, and no branch, commit or remote operation
is requested. The stable SDD identifier is `payment-validation-tests`.

## Impact and risks

All three clauses of the existing contract are retained as baseline obligations
in metadata. No active or archived dossiers existed at entry, so historical
requirement origins are unavailable and are not invented. The meaningful risk
is false confidence from tests that assert only return values; acceptance also
covers state invariants. No architecture boundary or deployment changes are
proposed. Existing production readiness and repository governance are outside
this bounded synthetic exercise.

## Current contract baseline

The living product specification requires a nonempty key and positive amount;
a key can be charged once, duplicates return `False`, and new charges return
`True`. `ValueError` and mutation of the supplied `seen` set are observed current
implementation behavior. The proposed scenarios preserve these details.

## Proposal acceptance criterion

Proposal and Requirements revision 1 are consistent with the existing payment
contract, distinguish source inspection from execution evidence, and define
observable success, rejection, boundary and duplicate cases for later Design.

## Planning review

Gate 1 is pending for the combined Proposal and Requirements, revision 1.
No approval has been received or recorded. Approval of this revision unlocks
Design only. No Design or Tasks artifact exists.
