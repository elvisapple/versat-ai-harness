# Testing Standard

- Every change MUST define observable acceptance criteria.
- Tests MUST cover behavior and meaningful invariants, not implementation wording.
- Tests or explicit checks MUST cover relevant acceptance scenarios, including meaningful error and boundary behavior, in proportion to change risk. One passing check linked to a requirement is not sufficient if relevant scenarios remain uncovered.
- Reuse adequate existing tests and checks. Coverage does not require a separate case catalog, new scenario identifiers, fixed case counts, exhaustive input enumeration or mandatory test-first development.
- Validation MUST report relevant scenarios without coverage or observed evidence; a structural validator pass or unrelated passing test MUST NOT conceal those gaps.
- Bug fixes SHOULD include a regression test when feasible.
- Agent projects MUST include evals for critical behavior and approval boundaries.
- Test fixtures MUST NOT contain production secrets or personal data.
- Required test and eval suites MUST run in CI before merge.

- Impact assessment MUST distinguish historical requirement origins from the effective current contract. Preserved or extended behavior MUST retain regression coverage in maintained project suites, independent of whether its originating dossier is active or archived. A missing historical test is work to address, not evidence of no impact.
- Intentional supersession or retirement of behavior/tests MUST have a reviewed rationale, affected requirement references and replacement checks where applicable. A failing regression alone is not grounds to delete or exclude it.
- Manual/review checks MUST specify reproducible steps, expected observations and a reason when substituting for useful automation. Not-applicable scenarios require an approved justification; unavailable execution is unverified, never not-applicable or passed.
- Validation MUST assess each applicable acceptance scenario and retained regression obligation against current implementation and observed evidence. Complete task checkboxes alone do not establish acceptance. Missing, partial, contradictory or unrequested behavior MUST remain visible until resolved or reviewed through the planning gates.
- Execution evidence MUST identify the tested inputs and relevant environment. Rerun affected checks after implementation, test, fixture, configuration or known external dependency changes. Historical runs, editable revision labels and structural success do not prove current behavior. Declared scopes and hashes do not authenticate execution or discover undeclared dependencies.
- Targeted checks complement required profile suites and final CI; they MUST NOT silently replace them.
