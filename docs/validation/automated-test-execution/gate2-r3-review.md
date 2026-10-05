# Design R3 and ADR-0015 revision review

Proposal/Requirements R2 was approved by the developer with "aprovado" after presentation. Its digest remains `3278e689b32cbd1d5f51e8357f445a5d59ed782662cfec3de05985aada41da3e`. Design R3 is awaiting Gate 2 approval at digest `244b88d4d9d59056d6956304d15bdea5c02f975a62877073a330151d488c7488`; ADR-0015 is a proposed revision presented with it. Tasks R1 remains superseded and its substantive digest unchanged.

## Architectural assessment

The material limitations are native agents' shared filesystem/permissions, incomplete observation export and dependence on a supervising coordinator. The design documents these directly. Fresh synthetic fixtures, actual structured runner results, artifact inspection and independent test/mutation replay provide reviewable evidence; unavailable critical observations remain unverified. Neither a fresh context nor a temporary directory is described as security isolation. Usage is recorded only where available, and monitored time limits are not a hard billing cap.

The explicit command runner, full required deterministic suites, consumer composition, source freshness and retained regressions remain. The revised policy distinction belongs in the canonical Testing Standard, with Skills/workflows referring to it. Native delegation is an execution procedure; pure validators never invoke models or parse narrative commands. Supervised evidence uses the existing local review method, preserving the four-file lifecycle and current approval rules.

CHECK-004 specifies six fresh-context scenarios with independent verification, one planned invocation each and monitored limits. CHECK-006 reuses the resulting attempts for first-use/semantic review. CHECK-008 becomes an explicitly local review of deterministic CI integration and evidence readiness. This removes the prior protected-model CI prerequisite to local closure while preserving actual final required CI and PR review before merge. No local result is labeled as remote CI success.

The unshipped CLI/runtime/protected-workflow artifacts are removed under an explicit migration mapping. Useful fixture, integrity and replay coverage is retained in supervised helpers; transport-exclusive tests may be retired with reviewed reasons. No optional unvalidated credentialed path remains in the proposed delivery. Historical evidence and previous decisions stay available.

No unresolved architectural decision blocks presenting Gate 2. Actual supervised scenarios, revised implementation, Linux CI and final remote outcomes remain future verification work, not observed successes.

## Actual checks

- Selected planning validation: `fail`, with only two `APPROVAL_REQUIRED` findings for Design/Tasks and seven `INPUT_STALE` findings for historical results. No schema, impact, reference or coverage errors remain. The initial mapping error and its corrected output are retained separately.
- `PYTHON=/private/tmp/versat-sdd-acceptance-venv/bin/python ./scripts/validate/run.sh`: exit 1 because SDD remains non-passing during replanning. All 131 validator tests and all 52 execution/adapter tests passed. These exercise current code, including the not-yet-removed CLI adapter, and do not prove the proposed native scenario procedure.
- `git diff --check`: pass. Proposal digest still matches the developer-approved revision; Tasks content has not been silently revised.

Evidence: [final planning output](gate2-r3-planning.json), [initial planning output](gate2-r3-planning-initial.json), [package output](gate2-r3-package.txt), [stage digests](gate2-r3-digests.json), [previous Design](design-r2-superseded.md), [previous accepted ADR](adr-0015-r1-accepted.md).

Preserved executed task statuses cause the validator to require current approvals even in planning mode. The old results also remain stale. Neither statuses nor hashes were rewritten to force a pass. A small final wording clarification distinguishes consistent structured runner evidence from authenticated action telemetry; selected planning validation was rerun after that clarification.

## Handoff

Present Design R3 and the proposed ADR-0015 revision for Gate 2 approval. Acceptance unlocks revised Tasks, including reconciliation of historical progress and evidence with the new check methods. No product implementation, native scenario execution, remote publication or platform change was performed in this design phase.
