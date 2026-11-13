---
sdd_version: 3
change: payment-validation-tests
status: proposed
owner: Synthetic evaluator
summary: Strengthen regression coverage for the existing payment validation contract.
risk: medium
impact:
  state: assessed
  summary: Preserve the living payment contract and existing tests while covering negative amounts and state invariants.
  items:
    - current_contract:
        path: specs/product/payment.md
        locator: Payment requires a nonempty key and positive amount.
        digest: 46a4d95d4458d55ce93d10aae8bdadcb9c60263aecf16f1bb3dd8163df955aaf
      effect: preserve
      targets: [REQ-001, REQ-002, REQ-003, REQ-004]
      reason: Test the current documented rules without changing payment behavior or retiring regressions.
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
Python, the finance domain and medium criticality. Its 12 resolved Standards
match the installed release index and the file digests in the project lockfile.
The living specification is `specs/product/payment.md`.

Inspection of `src/payment.py` shows that `charge(seen, key, amount)` raises
`ValueError` for an empty key or a nonpositive amount, returns `False` for an
already seen key, and otherwise adds the key and returns `True`.
`tests/test_payment.py` currently checks a new charge, a duplicate, zero amount
and an empty key. It has no explicit negative-amount or unchanged-state
assertions. These are source observations, not executed test results.

## Expected outcome

The maintained payment tests demonstrate success, invalid-input rejection and
duplicate prevention, including meaningful boundary and state-preservation
scenarios. Existing behavior and adequate existing tests remain intact.

## Scope

Plan test coverage for the existing payment function using synthetic keys and
integer amounts. Reuse existing cases where adequate and close the identified
coverage gaps. Preserve the required unit suite declared by
`.versat/validation.yaml`.

## Out of scope

Payment-provider integration, real charges, production data, persistence,
concurrent calls, monetary precision, currency conversion, retries across
processes, new input types, whitespace normalization and new product behavior.
This stage does not modify source, tests or living specifications and does not
prepare Design, Tasks, a PR or a release.

## Work tracking

No Story or issue is associated with this synthetic scenario. No Git repository
metadata is present at the target project root; no branch, commit or remote
state is claimed. The stable specification identifier is
`payment-validation-tests`.

## Impact and risks

The baseline contract is preserved. No active or archived change dossiers
existed at inspection, so historical requirement origins are unavailable; none
are invented. The impact item binds the living product specification by its
raw SHA-256 digest. Subsequent Design must retain regression coverage for this
baseline in addition to the local acceptance scenarios.

A weak assertion could accept the right return value while missing a state
mutation. The requirements therefore include set-state observations. Tests use
fresh caller-owned sets to avoid order-dependent results. Financial production
assurance is outside this synthetic function-level evaluation.

## Current contract baseline

The product specification requires nonempty keys, positive amounts, at most one
charge for each key, `False` for duplicates and `True` for new charges.
Existing code supplies the concrete rejection behavior (`ValueError`) and
state handling. Preserving these observed details is an explicit assumption
for Gate 1 review, rather than a claim that the product specification spells
out every implementation detail.

## Proposal acceptance criterion

Proposal and Requirements R1 state the existing contract, focused coverage gaps,
observable scenarios, exclusions and assumptions. The planning validator checks
these artifacts, but passing it does not approve the stage or prove tests pass.

## Planning review

Proposal and Requirements share revision 1. Gate 1 awaits human approval.
Approval evidence is absent. Approval of this stage permits Design only.
