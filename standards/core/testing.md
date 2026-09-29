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
