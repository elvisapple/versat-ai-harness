# Testing Standard

- Every change MUST define observable acceptance criteria.
- Tests MUST cover behavior and meaningful invariants, not implementation wording.
- Tests or explicit checks MUST cover relevant acceptance scenarios, including meaningful error and boundary behavior, in proportion to change risk. One passing check linked to a requirement is not sufficient if relevant scenarios remain uncovered.
- Reuse adequate existing tests and checks. Coverage does not require a separate case catalog, new scenario identifiers, fixed case counts, exhaustive input enumeration or mandatory test-first development.
- Validation MUST report relevant scenarios without coverage or observed evidence; a structural validator pass or unrelated passing test MUST NOT conceal those gaps.
- Bug fixes SHOULD include a regression test when feasible.
- Agent projects MUST include evals for critical behavior and approval boundaries.
- Test fixtures MUST NOT contain production secrets or personal data.
- Required automated test and eval suites MUST run in CI before merge. Supervised Skill behavioral checks MAY use separately reviewed local execution when the approved plan identifies reproducible scenarios, independent artifact/test verification, available observations, bounded attempts and required delivery evidence. Missing or unverified required supervised evidence MUST prevent delivery readiness. This distinction MUST NOT waive required automated application evals or relabel supervised work as an automated CI pass.

- Impact assessment MUST distinguish historical requirement origins from the effective current contract. Preserved or extended behavior MUST retain regression coverage in maintained project suites, independent of whether its originating dossier is active or archived. A missing historical test is work to address, not evidence of no impact.
- Intentional supersession or retirement of behavior/tests MUST have a reviewed rationale, affected requirement references and replacement checks where applicable. A failing regression alone is not grounds to delete or exclude it.
- Manual/review checks MUST specify reproducible steps, expected observations and a reason when substituting for useful automation. Not-applicable scenarios require an approved justification; unavailable execution is unverified, never not-applicable or passed.
- Validation MUST assess each applicable acceptance scenario and retained regression obligation against current implementation and observed evidence. Complete task checkboxes alone do not establish acceptance. Missing, partial, contradictory or unrequested behavior MUST remain visible until resolved or reviewed through the planning gates.
- Execution evidence MUST identify the tested inputs and relevant environment. Rerun affected checks after implementation, test, fixture, configuration or known external dependency changes. Historical runs, editable revision labels and structural success do not prove current behavior. Declared scopes and hashes do not authenticate execution or discover undeclared dependencies.
- Targeted checks complement required profile suites and final CI; they MUST NOT silently replace them.

## Explicit execution and coverage

- During implementation, create or update meaningful tests for new/changed behavior and missing retained coverage, or document why existing checks are adequate. A new file/test is not mandatory for every change; adequate reuse and justified manual checks remain valid.
- Projects adopting the Harness executor MUST declare their required suites, command arguments, result adapters, bounded execution and reviewed input/output scope in `.versat/validation.yaml`. Required suites include retained regression coverage; targeted runs cannot claim full readiness. Preserve custom framework integrations through reviewed adapters.
- Test execution MUST report actual counts; empty or all-skipped suites, malformed results, nonzero exits and required assertion failures cannot pass. Non-test checks may use exit status. Configuration inspection and SDD validation MUST NOT execute arbitrary procedure text.
- Keep each real attempt and its outcome. Missing execution prerequisites are unverified; incomplete evidence, unavailable observations or a planned command cannot establish success. Source/provider changes require current execution evidence. Execution fragments do not authorize plans or replace semantic assessment.
- Critical Skill evaluations MUST exercise real behavior with versioned synthetic inputs, available runtime/action observations, independent artifact/test verification and retained attempts. Code reviews, canned events and final narratives alone do not establish behavioral execution. Record unknown telemetry, shared-permission limits and unavailable required observations explicitly; temporary fixture directories MUST NOT be described as security isolation. Follow the reviewed time/attempt limits and retain failures without automatic retries or selecting only successful outcomes.
