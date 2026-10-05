# ADR-0015 — Separate explicit test execution from validation and evaluate real skill behavior

- Status: Accepted
- Date: 2026-10-02
- Related: ADR-0003, ADR-0004, ADR-0007, ADR-0009, ADR-0011, ADR-0013, ADR-0014
- Change: `automated-test-execution`, Design R1
- Decision evidence: The developer approved the presented Design R1 and ADR-0015 in the development conversation on 2026-10-02 with “Sim, aprovado. Avance para as tasks.” This accepts the architectural decision and authorizes Tasks planning, not implementation or remote actions.

## Context

The Harness already defines acceptance coverage, retained regression obligations and current evidence. Its package script runs deterministic tests, but consumer integration relies on project-defined commands and an agent translating guidance into execution. SDD validators inspect declared records and snapshots; they intentionally never execute check prose. The maintained skill scenarios and synthetic walkthrough do not establish actual agent behavior.

Making validation execute arbitrary narrative would mix trust boundaries and convert a read-only check into an action. Requiring new tests for every change would duplicate adequate coverage. Treating mocked agent events or a model's final answer as evidence would leave the observed gap unresolved.

## Decision

Add an explicit execution adapter under `scripts/testing/`, with versioned consumer configuration in `.versat/validation.yaml`. Keep pure schema/result enforcement in `validators/testing/`; preserve the existing SDD validator's read-only behavior. Configuration names required suites and executable argument arrays. Full validation runs every required suite; targeted development runs cannot claim full readiness. Test suites must provide actual structured collection/execution counts, with a Python unittest reference and a generic JSON report adapter. Zero executed tests, missing results, failures and unavailable prerequisites cannot produce full success.

The runner records separate attempts, command identity, outcomes, safe outputs and current snapshots. Its optional SDD binding exports a result fragment using the approved v3 check and current plan; it does not edit approvals, task completion, semantic assessments or findings. The agent/reviewer incorporates observed evidence through the existing lifecycle and remains responsible for coverage adequacy. No v3 schema change or fifth dossier file is required.

Add a separate Codex CLI evaluation adapter under `scripts/eval/`. It executes the actual skill instructions from an exact package snapshot in disposable synthetic consumer projects. Versioned cases grade observed actions, artifacts, independent behavior checks and governance boundaries. CLI events are evidence inputs, not proof of correctness. Mocked event tests remain distinct from live evaluations. The initial CLI target is the locally inspected 0.159.2 interface; model and reasoning settings are explicit reviewed runtime inputs, without silent defaults or substitution.

Keep the local package command deterministic and offline after prerequisite setup. Require real evaluations separately for delivery through an exact-revision, protected CI workflow and corresponding platform-required check. Eligible same-repository PRs queue evaluations behind maintainer approval of the exact source and workflow in a protected environment; untrusted PR jobs receive no evaluation credentials and cannot report readiness. A credential-free aggregate check rejects skipped required evaluation. Exact-ref dispatch supports reruns once the workflow is available on the default branch. Missing required model/runtime access remains unverified and cannot be replaced with deterministic success. This change supplies workflow and configuration guidance; actual remote protection and observed CI remain separate facts.

Extend Standards, SDD workflows and bootstrap/maintenance integration in their existing responsibilities. The agent creates missing meaningful coverage within authorized implementation and reuses adequate maintained tests. A Python reference consumer demonstrates the contract; a generic command interface preserves framework choices. Templates compose over base, and consumers adopt exact versions through review.

## Alternatives

- Retain prose-only execution: low implementation effort but no consistent command/result boundary or real agent evidence.
- Execute SDD check prose: rejected for implicit command execution and conflation of validation with effects.
- Infer every framework and generate tests universally: rejected as unnecessary scope and an unreliable proxy for behavioral coverage.
- Write semantic acceptance from process exit codes: rejected because successful execution alone cannot establish requirement satisfaction.
- Run live model evaluations in every local check: rejected for cost and offline usability; use an independently required delivery check.
- Introduce a general workflow engine: rejected in favor of bounded sequential process execution and an executor adapter.

## Consequences

- Developers get one documented project command, explicit required suites and actual execution reports; agents still author tests and assess coverage.
- Maintained regressions survive archival and remain required. Existing SDD gates, evidence limits and immutable compatibility records are preserved.
- Configuration and result schemas add a versioned contract with migration and rollback obligations. Existing project commands are preserved through reviewed integration.
- A runner is not a sandbox. Executed code, input scopes, credentials, environment isolation and privileged CI configuration require review.
- Agent evaluations add runtime availability, nondeterminism and cost. Bounded attempts and retained failures expose these rather than retrying until success.
- A local digest cannot authenticate remote runs or capture every external dependency. Observed CI, explicit environment records and semantic review remain necessary.
- Publishing a release, updating consumer pins, configuring remote protection and provisioning credentials remain separately scoped actions.

## Review boundary

This ADR was accepted together with Design R1. Implementation still requires current planning approvals and explicit execution authorization. Living architecture documentation is updated with delivered implementation, not by treating an accepted decision as implemented behavior. A later Design revision may refine the CI delivery sequence without changing this decision's execution, trust or governance boundaries.
