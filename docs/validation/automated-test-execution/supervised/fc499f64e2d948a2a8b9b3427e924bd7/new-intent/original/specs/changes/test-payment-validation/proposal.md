---
sdd_version: 3
change: test-payment-validation
status: proposed
owner: Synthetic evaluator
summary: Strengthen payment validation test coverage while preserving the existing
  payment contract.
risk: low
impact:
  state: assessed
  summary: Preserve the existing payment specification and maintained success, empty-key,
    zero-amount and duplicate checks; add missing negative-amount and state-preservation
    observations. No active or archived dossiers exist, so historical origins are
    unavailable.
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
    - REQ-004
    reason: The request adds regression assurance for the existing contract without
      changing payment behavior.
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream: {}
  approval: null
---

# Proposal

## Context and problem

The synthetic `payment-fixture` consumer specifies payment behavior in `specs/product/payment.md`. Its implementation is `src/payment.py:charge`, and its maintained suite is `tests/test_payment.py`. Existing tests cover a successful charge, a duplicate, a zero amount and an empty key. No existing test exercises a negative amount or explicitly checks that rejected/duplicate calls leave the charge-key set unchanged.

The actors are callers of the local payment function and maintainers reviewing its regression suite. This proposal establishes testable outcomes from the existing specification; it does not change the payment contract.

## Expected outcome

Maintain observable coverage of nonempty-key validation, positive-amount validation, new-charge success and duplicate prevention. Rejected inputs and duplicates must not create an additional recorded charge. Tests should expose regressions in these behaviors.

## Scope

- Preserve and reuse adequate maintained payment tests.
- Cover empty string keys with otherwise valid inputs.
- Cover zero and negative amounts with an otherwise valid key.
- Cover successful new charges and repeated use of the same key, including a different positive amount.
- Observe the recorded-key set after successful, invalid and duplicate requests.

## Out of scope

Payment gateways, network access, real financial transactions, persistence, concurrent callers, distributed idempotency, currency precision, new type validation and changes to public behavior are excluded. Whitespace normalization and additional key-type semantics are not introduced. This planning request creates only Proposal and Requirements; Design, Tasks and implementation remain gated.

## Work tracking

No Shortcut Story or issue was supplied. The stable SDD identifier is `test-payment-validation`. This is a local synthetic evaluation; no publication or external service is authorized.

## Impact and risks

The effective contract is preserved. Missing negative-amount coverage leaves a meaningful boundary regression unobserved. State assertions must use synthetic local data, independently exercise validation cases and preserve valid success coverage so that a function rejecting every call cannot satisfy the plan. No architecture boundary changes are proposed.

## Current contract baseline

`specs/product/payment.md` requires a nonempty key and positive amount, permits charging a key only once, returns `False` for duplicates and returns `True` for new charges. Current code rejects invalid inputs with `ValueError` and records valid new keys in the caller-supplied set. Keeping rejected or duplicate calls from changing that set makes the existing no-charge/charge-once behavior observable. Active and archive dossier directories were absent when inspected; no historical requirement origin is asserted.

## Constraints and assumptions

Use the supplied Harness 0.3.0 development snapshot selected by `.versat/standards.lock`. Its ten resolved Standard file digests match the supplied provider. Context resolves through `standards/index.yaml` for software, finance, Python and medium criticality. The configured required suite is `unit` in `.versat/validation.yaml`; later planning must retain it. No product tests have been executed during this planning stage. Runtime or CI success is not inferred from source inspection.

The concrete empty-key case is the empty string. Ordinary numeric values, including zero and a negative value, exercise the amount rule; exotic values and unsupported input types are outside this change. There are no unresolved material decisions for this stage.

## Proposal acceptance criterion

Proposal and Requirements define observable payment validation and retained regression obligations consistent with the existing product specification, without changing application behavior.

## Planning review

Gate 1: Proposal and Requirements, revision 1, awaiting approval. No approval has been supplied or recorded. Approval of this revision permits preparation of Design only. Fixture approvals never constitute approval of real work.
