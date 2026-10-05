# Evaluation approach review — 2026-10-02

Status: recommendation selected by the developer with "Adote a recomendação". Proposal/Requirements R2 incorporated it and was approved; Design R3 and revised ADR-0015 were approved; Tasks R2 now presents the execution plan for Gate 3 review; this report is not approval of unseen revised artifacts or a replacement execution result.

The developer requested a review of a simpler alternative, including native subagents. A native subagent reviewed the approved requirements, design, ADR and implementation; the primary agent checked the conclusions against those contracts and the available collaboration interface. No model behavior scenario was executed as part of this review.

## Recommendation

Keep explicit project test execution, meaningful test creation/reuse guidance, current SDD evidence and the complete deterministic CI suite. Use supervised native subagents for targeted behavioral evaluation of the Skill, with synthetic disposable project directories and independent verification of produced artifacts/tests. Defer autonomous credentialed model evaluation in GitHub Actions to a separately justified requirement.

The dedicated API key is a prerequisite imposed by the chosen CLI adapter. Native subagents are already available through this session and do not require a newly provisioned API key. They still consume the account's model usage. The original goal—create or reuse adequate tests for authorized changes and run retained regressions—does not inherently require an autonomous live-model CI service.

## Proposed workflow

1. The implementation agent reads approved acceptance/impact, reuses adequate checks and creates missing behavioral assertions.
2. The explicit runner executes all required suites and produces actual current results. CI repeats all required deterministic suites.
3. When Skill behavior changes, a native subagent receives a fresh synthetic fixture and a specific scenario. Give the scenario agent only the scenario context, not an answer key or the implementation conversation.
4. The coordinator verifies files, diffs, approval boundaries and real command results. Re-execute the resulting tests and introduce controlled defects to check assertion adequacy. Preserve failed and unavailable attempts.
5. Record a supervised evaluation with available runtime/context information and stable evidence. Do not treat the subagent's narrative as proof or label this as an autonomous CI execution.

Use the existing six scenario definitions where relevant: first planning gate, missing coverage, adequate reuse, retained failure, stale evidence and validation-only. Choose repetitions in the reviewed evaluation plan; do not introduce automatic retries or a fixed new-test count for every change.

## Boundaries

- A temporary project directory organizes synthetic inputs; it is not a separate security boundary. Native subagents share the session filesystem and inherit its sandbox/permissions.
- The available collaboration interface exposes delegated work, messages and results; it does not offer the CLI adapter's automatic JSONL transcript export and usage accounting. Retain only observations that can actually be inspected and independently checked.
- A supervised evaluation can exercise real agent behavior. A review of code or instructions alone is not that evaluation.
- This approach does not establish an autonomous, unattended CI job for agent behavior. Keep that limitation explicit in requirements, checks and delivery claims.

Official capability reference: [OpenAI documentation on subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), including inherited permissions and model usage. The actual session also successfully started the requested review subagent.

## Required planning revision

For the recommended simplification, reopen Proposal/Requirements first:

- REQ-006 currently mandates automated behavioral evaluation with captured actions/conversation. Revise it to require versioned, supervised behavioral evaluation with actual artifacts, observed actions where available and independent test verification.
- REQ-005 scenario 3 currently makes unavailable required agent evaluations non-passing in CI. Specify which automated suites are required in CI and which supervised behavioral checks require separately reviewed local evidence.
- Preserve REQ-001 through REQ-004's execution, regression and freshness guarantees; reconcile mappings in REQ-007/008 and the impact assessment with the revised evaluation contract.
- Reconcile the Testing Standard explicitly. Required automated suites continue to run in CI. Supervised reviews must not be mislabeled as passing CI suites or silently waive an already-required evaluation.

Then revise Design, ADR-0015 and Tasks to remove the mandatory dedicated-key/protected-evaluation-workflow dependency for this delivery, define the supervised evidence contract, and update CHECK-004/CHECK-006/CHECK-008 and their scenario mappings. Defer or remove the CLI/evaluation-CI assets from this delivery's active scope rather than presenting them as validated optional functionality.

If the developer instead requires exactly the current automated/observable/CI outcomes and changes only the agent transport, the earliest affected gate is Design. A native-subagent replacement would first need proof of the same orchestration, transcript, limits and CI capabilities; this review did not establish those capabilities.

## Existing evidence

The 183 deterministic tests and the successful real CLI sandbox probe remain valid observations for their recorded source revision. They do not prove the proposed supervised evaluation or satisfy the current required live checks. The review itself did not modify approved artifacts or evidence. The subsequent adoption request reopened Proposal/Requirements as R2 and marked Design R2 and Tasks R1 superseded, preserving historical approvals and execution observations.
