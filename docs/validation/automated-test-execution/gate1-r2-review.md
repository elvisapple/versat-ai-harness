# Proposal/Requirements R2 review

The developer selected the supervised native-subagent recommendation with "Adote a recomendação" in the current conversation. The revised direction is now incorporated in Proposal/Requirements R2. Its shared stage digest is `3278e689b32cbd1d5f51e8357f445a5d59ed782662cfec3de05985aada41da3e`.

## Scope and state

- REQ-001 through REQ-004 and their scenarios remain unchanged: explicit execution, meaningful test creation/reuse, retained regressions and current evidence.
- REQ-005/006 separate automated CI from required supervised behavioral evidence, with native scenario subagents and independent verification.
- REQ-007/008 reconcile adoption guidance and the canonical Testing Standard. The proposal records a governed supersession of the unreleased credentialed evaluation obligation, not a silent waiver of existing automated suites.
- Dedicated evaluation credentials, autonomous CLI evaluation and protected live-model CI are deferred from this delivery. Design/Tasks must reconcile the existing unshipped implementation and its tests.
- There are still 27 local scenarios and 23 retained regression obligations. The additional impact item explicitly records policy supersession and replacement targets.
- Proposal R2 awaits Gate 1 approval. Design R2 and Tasks R1 are superseded. Their substantive digests remain unchanged, and historical approval quotes, task progress and actual results are preserved. No revised Design, ADR decision, Tasks plan or product implementation is claimed by this planning step.

## Actual verification

Commands used `/private/tmp/versat-sdd-acceptance-venv/bin/python` in this checkout.

- Selected planning validation returned `fail`: three `APPROVAL_REQUIRED` findings and seven `INPUT_STALE` findings. It reported no schema, reference, impact or coverage errors. See [structured output](gate1-r2-planning.json).
- `PYTHON=/private/tmp/versat-sdd-acceptance-venv/bin/python ./scripts/validate/run.sh` returned exit 1 because the SDD check remains non-passing. Both deterministic suites passed: 131 validator tests and 52 execution/adapter tests. See [complete output](gate1-r2-package.txt).
- `git diff --check` passed.
- [Stage digests](gate1-r2-digests.json) confirm that the old Design and Tasks content was not silently rewritten.

The current validator requires current approvals when retained task statuses show prior execution, even in planning mode. Keeping truthful historical progress therefore leaves the package check non-passing during replanning. Old execution records also remain stale; their hashes/results were not rewritten to manufacture readiness. These results are planning observations, not replacement CHECK results or evidence of supervised scenario execution.

## Next permitted action

Present Proposal/Requirements R2 for Gate 1 approval. Once accepted, revise Design and ADR-0015, then Tasks through their current gates, and reconcile implementation and rerun affected checks. Approval of the recommended direction is recorded separately from approval of newly presented artifact contents. No remote publication or platform mutation occurred.
