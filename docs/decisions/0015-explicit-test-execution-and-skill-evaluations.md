# ADR-0015 — Separate explicit test execution from validation and evaluate real skill behavior

- Status: Accepted (revised with Design R3)
- Date: 2026-10-02
- Related: ADR-0003, ADR-0004, ADR-0007, ADR-0009, ADR-0011, ADR-0013, ADR-0014
- Change: `automated-test-execution`, Design R3, approved Proposal/Requirements R2
- Decision evidence: The developer approved the original ADR with Design R1 using “Sim, aprovado. Avance para as tasks.” The developer subsequently selected the supervised alternative and approved Proposal/Requirements R2 with “aprovado”. After presentation of Design R3 and this revised ADR, the developer replied “sim”, accepting the revision. The Design R3 digest is `244b88d4d9d59056d6956304d15bdea5c02f975a62877073a330151d488c7488`; prior acceptance remains historical evidence.

## Context

The Harness already defines acceptance coverage, retained regression obligations and current evidence. Its package script runs deterministic tests, but consumer integration relies on project-defined commands and an agent translating guidance into execution. SDD validators inspect declared records and snapshots; they intentionally never execute check prose. The maintained skill scenarios and synthetic walkthrough do not establish actual agent behavior.

Making validation execute arbitrary narrative would mix trust boundaries and convert a read-only check into an action. Requiring new tests for every change would duplicate adequate coverage. Treating mocked agent events or a model's final answer as evidence would leave the observed gap unresolved.

The first design added a credentialed Codex CLI evaluator and protected live-model CI. Local deterministic tests and a sandbox probe were observed, but actual model scenarios and protected CI were not. The developer selected a smaller supervised approach using session-native subagents. The original need for test authoring/reuse and regression execution does not require an autonomous model CI service. The [previous accepted ADR](../validation/automated-test-execution/adr-0015-r1-accepted.md) preserves that historical decision.

## Decision

Add an explicit execution adapter under `scripts/testing/`, with versioned consumer configuration in `.versat/validation.yaml`. Keep pure schema/result enforcement in `validators/testing/`; preserve the existing SDD validator's read-only behavior. Configuration names required suites and executable argument arrays. Full validation runs every required suite; targeted development runs cannot claim full readiness. Test suites must provide actual structured collection/execution counts, with a Python unittest reference and a generic JSON report adapter. Zero executed tests, missing results, failures and unavailable prerequisites cannot produce full success.

The runner records separate attempts, command identity, outcomes, safe outputs and current snapshots. Its optional SDD binding exports a result fragment using the approved v3 check and current plan; it does not edit approvals, task completion, semantic assessments or findings. The agent/reviewer incorporates observed evidence through the existing lifecycle and remains responsible for coverage adequacy. No v3 schema change or fifth dossier file is required.

Use a supervised native-subagent evaluation procedure for relevant Skill behavior. A coordinator provides a fresh synthetic consumer and exact Skill snapshot to each scenario agent without inherited implementation conversation or a grading answer key. The coordinator inspects available actions and artifacts, re-executes resulting tests and uses controlled defects to verify assertions. Versioned fixtures and independent verification helpers live under `tests/skills/`; deterministic helper tests remain in the ordinary package suite. No model transport, generic orchestrator or new public Skill is added.

Keep the local package command deterministic and offline after prerequisite setup. All required automated test/eval suites continue running in CI. Revise the canonical Testing Standard explicitly to permit separately reviewed local supervised Skill evaluations with reproducible scenarios, independent verification, available observations, bounded attempts and required delivery evidence. Missing required supervised evidence prevents delivery readiness even when deterministic CI passes. This scoped distinction does not waive required automated application evals or label supervised work as an automated CI pass.

Record supervised results through the existing v3 local `review` method, including stable evidence references and before/after provider input snapshots. Preserve actual prompts, fixture manifests/diffs, available observations, runtime unknowns, real command/mutation outputs, per-assertion verdicts and all attempts. The coordinator supplies semantic assessment; a helper or subagent narrative cannot create acceptance. Missing critical observations remain unverified. Native agents share the session filesystem/permissions: disposable directories organize tests but do not enforce isolation, and complete transcript export or exact usage accounting is not assumed. The Design specifies six cases, one fresh invocation per case and monitored time/attempt limits for this delivery; no automatic retries or reliability-rate claim is made.

Remove the unshipped CLI adapter, dedicated runtime schema, credentialed workflow and their exclusive tests/setup instructions from this delivery, retaining reusable fixtures, runner/regression coverage and historical evidence under the reviewed migration mapping. Do not keep an unvalidated optional credentialed path. Dedicated keys and protected evaluation infrastructure are deferred to a separately justified change.

Required local evidence and semantic review precede documentary archival in the implementation branch. Authorized submission is followed by final required deterministic CI and PR review before merge. The local CI integration review does not claim an observed remote run. Neither archive preparation nor native evaluation requires publication of an intermediate evaluation draft. Actual platform protection remains external and must be reconciled if it conflicts with the revised required checks; this decision grants no remote settings authority.

Extend Standards, SDD workflows and bootstrap/maintenance integration in their existing responsibilities. The agent creates missing meaningful coverage within authorized implementation and reuses adequate maintained tests. A Python reference consumer demonstrates the contract; a generic command interface preserves framework choices. Templates compose over base, and consumers adopt exact versions through review.

## Alternatives

- Retain prose-only execution: low implementation effort but no consistent command/result boundary or real agent evidence.
- Execute SDD check prose: rejected for implicit command execution and conflation of validation with effects.
- Infer every framework and generate tests universally: rejected as unnecessary scope and an unreliable proxy for behavioral coverage.
- Write semantic acceptance from process exit codes: rejected because successful execution alone cannot establish requirement satisfaction.
- Keep autonomous live-model CI for this delivery: deferred because the approved supervised outcome does not justify its provisioning and credential dependencies.
- Use a code-review-only subagent: insufficient to exercise Skill behavior or establish actual test execution.
- Run live model evaluations in every local check: rejected for cost and offline usability; use a separately assessed supervised delivery check.
- Introduce a general workflow engine: rejected in favor of the existing explicit process runner and supervised native delegation.

## Consequences

- Developers get one documented project command, explicit required suites and actual execution reports; agents still author tests and assess coverage.
- Maintained regressions survive archival and remain required. Existing SDD gates, evidence limits and immutable compatibility records are preserved.
- Configuration and result schemas add a versioned contract with migration and rollback obligations. Existing project commands are preserved through reviewed integration.
- A runner and temporary fixture directory are not sandboxes. Shared permissions and generated commands require review; fresh conversational context does not enforce filesystem containment.
- Agent evaluations consume session model usage and add runtime availability and nondeterminism. Monitored limits and retained failures expose these rather than retrying until success; native interruption is not a hard monetary ceiling.
- Supervised evidence needs an available coordinator and adequate observations. It is reproducible in its scenario inputs and verification steps, not guaranteed deterministic in agent outcomes or available as unattended CI.
- A local digest cannot authenticate remote runs or capture every external dependency. Observed CI, explicit environment records and semantic review remain necessary.
- Publishing a release, updating consumer pins, configuring remote protection and provisioning credentials remain separately scoped actions.

## Review boundary

The original ADR was accepted with Design R1. This revision changes the evaluation responsibility and delivery prerequisites under approved Proposal/Requirements R2 and was accepted together with Design R3 by the developer response “sim”. The explicit runner/validator boundary remains. Implementation requires current planning approvals and execution authority; living architecture documentation is reconciled with actual implementation in that phase. No supervised scenario result, remote CI pass, publication or release is claimed by this ADR.
