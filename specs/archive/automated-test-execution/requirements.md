---
sdd_version: 3
change: automated-test-execution
requirements:
  - id: REQ-001
    statement: Consumer projects MUST have an explicit, reviewable validation entry point that resolves their configured required suites and prerequisites.
    acceptance:
      - Given a configured Python reference consumer, when its documented validation command runs from a fresh prepared environment, then it resolves the project's required suites and executes the intended tests with observable results.
      - Given an existing project with custom test commands, when validation integration is adopted, then its commands and content are preserved or changed through an explicit reviewed mapping rather than overwritten or guessed.
      - Given an invalid configuration, missing required suite, unavailable runtime or missing dependency, when validation is requested, then it reports the specific failure or unavailable prerequisite and does not return an overall success or silently install dependencies.
  - id: REQ-002
    statement: Each authorized change implementation MUST reuse adequate behavioral coverage and create or update missing tests for its approved acceptance and retained regression obligations.
    acceptance:
      - Given an approved change with uncovered success, error or boundary behavior, when authorized implementation completes, then maintained automated tests cover the relevant behavior where useful, and a seeded defect in that behavior causes the relevant check to fail.
      - Given adequate existing tests covering the approved scenarios, when implementing the change, then those tests are reused and mapped without requiring redundant new test files or fixed case counts.
      - Given relevant retained behavior with no historical test, when implementing the current approved plan, then missing regression coverage becomes current work; obsolete tests are retired only for reviewed supersession, and manual or inapplicable dispositions retain their approved reasons and evidence rules.
  - id: REQ-003
    statement: Explicit validation execution MUST run the selected new checks and maintained regressions without silently omitting required suites or changing the approved scope.
    acceptance:
      - Given a new passing feature and a seeded failure in an existing required regression, when full project validation runs, then it executes both and returns a failing overall outcome even if the regression originated in an archived change.
      - Given a targeted development run, when it completes, then its result clearly identifies its limited scope and does not claim full validation or remove required suites from final CI.
      - Given a timeout, interrupted process, nonzero exit or required test selection that discovers no tests, when execution concludes, then the outcome is non-passing with an actionable cause; retries retain the failed attempt rather than conceal it.
      - Given a planning or structural-validator invocation, when check procedures contain executable-looking prose, then no project command is launched; actual execution requires the explicit execution path and stays within caller permissions without modifying approvals, scope or tests to obtain a pass.
  - id: REQ-004
    statement: Automated execution MUST produce current, attributable evidence usable by the existing SDD validation contract without substituting for semantic assessment.
    acceptance:
      - Given an approved v3 check mapping, when its configured command executes, then the result records the actual command identity, outcome, relevant environment, durable output and before/after input snapshots and can be associated with the current planned check without inventing observations.
      - Given relevant implementation, test, fixture, configuration or plan changes after a run, when readiness is checked, then stale evidence cannot pass until the affected checks actually rerun; changes during a run also prevent a fresh passing result.
      - Given a manual check, unavailable environment or recorded external report that was not verified, when results are assembled, then they retain their distinct method and verification status rather than becoming automated passes.
      - Given documentary archival with unchanged assessed inputs, when the dossier moves, then evidence remains resolvable; execution results do not automatically approve semantic assessments, close findings or claim merge or deployment.
  - id: REQ-005
    statement: CI integration MUST execute the complete configured required deterministic suites and preserve the existing SDD delivery controls.
    acceptance:
      - Given a configured consumer PR containing a regression that passes its new targeted test but fails a maintained required suite, when CI runs, then the job fails and exposes the failing suite and its evidence.
      - Given draft and ready-for-review transitions in the Harness repository, when the revised integration runs, then all current validator regressions still execute and the existing baseline selection and archive guard retain their phase behavior.
      - Given passing deterministic CI and a missing or unverified required supervised Skill evaluation, when delivery readiness is assessed, then readiness remains non-passing and identifies the missing local evidence separately from the CI result; all required automated suites still execute in CI, and this delivery neither requires dedicated live-model credentials nor labels supervised work as an automated CI pass.
  - id: REQ-006
    statement: The Harness MUST provide versioned supervised behavioral evaluations that execute the SDD skill through native subagents and independently verify observable actions, artifacts and test behavior.
    acceptance:
      - Given a fresh synthetic consumer fixture and an available native subagent runtime, when a supervised evaluation runs, then the scenario agent receives the actual versioned Skill and scenario context without the grading answer key or implementation conversation, and the record identifies inputs, available runtime/context, inspectable observations and resulting artifacts; shared session permissions, missing telemetry, mocked events and review-only work are stated explicitly rather than portrayed as isolated or fully captured execution.
      - Given scenarios for a new change, missing behavioral coverage, adequate existing coverage and a retained regression failure, when the subagent is evaluated, then the coordinator independently verifies gate stopping, meaningful creation or adequate reuse of tests, actual execution of new and retained checks and truthful failure reporting by inspecting artifacts and command results, re-executing tests and using controlled defects; the subagent's narrative alone cannot establish success.
      - Given stale evidence or a validation-only request with a defect, when the subagent is evaluated, then independently checked actions, artifacts and command results establish that applicable checks rerun or their unavailability is reported and that product code is not fixed without authorization or passing evidence invented; insufficient observations remain unverified.
      - Given an unavailable runtime, an exceeded reviewed time or attempt limit, or inconsistent results across planned repetitions, when an evaluation ends, then every actual attempt and reason is retained, observable usage is recorded without fabricated accounting and required unmet criteria remain non-passing without unlimited retries or selecting only a successful attempt.
  - id: REQ-007
    statement: Bootstrap, maintenance and documentation MUST make validation setup and adoption reproducible while preserving template composition and exact-version consumer governance.
    acceptance:
      - Given a new supported consumer, when bootstrap applies the reviewed validation integration, then it extends the base composition, supplies usable configuration and documents prerequisites, one validation command and expected outcomes without claiming execution from scaffolding alone.
      - Given an existing consumer, when maintenance proposes adoption, then it presents configuration and CI changes with conflict handling and rollback guidance, preserves project-specific tests and requires a reviewed exact Harness reference without rewriting historical dossiers.
      - Given a developer following the quickstart in a clean supported environment, when dependencies are prepared and validation is executed, then the documented pass, failing-regression and unavailable-prerequisite examples match observed behavior, and separate supervised Skill evaluation instructions use session-native subagents without a dedicated API key or live-model CI provisioning requirement.
  - id: REQ-008
    statement: The implementation MUST preserve governance and verify execution boundaries with maintained deterministic tests and separately assessed supervised behavioral evidence under an explicit canonical Testing Standard revision.
    acceptance:
      - Given the new execution integration, when the package checks run, then existing SDD gate, compatibility, reference, freshness and archive tests remain passing and new runner tests exercise real harmless commands for success, failure, interruption and configuration errors.
      - Given malformed paths, unsafe output destinations or command text supplied through SDD narrative, when the relevant contract is checked, then actionable validation rejects invalid data and does not implicitly execute prose or grant permissions beyond the invoking environment.
      - Given a source update or a proposed repair requiring revised scope, when the workflow continues, then Standards remain canonical, the earliest affected planning gate is reopened, exact-release adoption stays explicit and no approvals or historical evidence are fabricated; the Testing Standard explicitly distinguishes required automated CI suites from supervised Skill checks with required independent evidence, without silently waiving other required evaluations.
---

# Requirements

## Actors and context

Developers approve changes and configure project validation. Coding agents create or reuse tests within authorized implementation and invoke reviewed project commands. CI executes all required automated suites. Native scenario subagents exercise relevant Skill behavior in fresh synthetic projects under supervision; a coordinator independently verifies their artifacts and test behavior. Maintainers review policy, execution boundaries and release adoption. Reviewers assess semantic adequacy and required supervised evidence beyond process exit codes and CI results.

The baseline is this Harness source checkout at `8e826cb` with SDD v3 and the immutable compatibility records it already supports. The Marketplace synchronization reported by the developer is considered complete and is not a deliverable of this change.

## Functional requirements

REQ-001 defines consumer configuration. REQ-002 covers test authoring and reuse. REQ-003 and REQ-004 define execution and evidence; these four requirements and their acceptance scenarios are unchanged from R1. REQ-005 separates required automated CI suites from supervised delivery evidence. REQ-006 adds real supervised Skill evaluations with native subagents. REQ-007 provides adoption and first-use guidance. REQ-008 preserves governance and requires explicit canonical policy reconciliation.

## Non-functional requirements

- Keep policies in Standards, lifecycle rules in SDD, routing in Skills, deterministic enforcement in validators and executor-specific behavior in explicit adapters. Resolve policies through `standards/index.yaml`.
- Reuse the four dossier files and three planning gates. Preserve immutable history and exact release selection; any metadata extension needs explicit compatibility in Design.
- Run deterministic package tests offline after dependencies are prepared. Keep supervised model-backed execution separately identifiable with explicit prerequisites, reviewed time/attempt limits and reproducible scenario inputs. Record available model/reasoning/context information and any unknowns; do not require unavailable exact token accounting or an automatic transcript export.
- Use fresh disposable project directories and synthetic data for evaluations. Capture only approved diagnostics; avoid secrets and personal data in logs, fixtures and retained observations. Native subagents share session permissions/filesystem; neither a temporary directory nor instructions establish security isolation. Their model usage remains part of session usage.
- Preserve project framework choices. Deliver a working Python reference and configurable command integration; do not imply tested native support for every technology or platform.
- No fixed coverage percentage, universal TDD mandate or duplicate test for each requirement. Passing exit codes and evidence hashes do not prove assertion adequacy or exhaustive impact discovery.

## Acceptance scenarios

The frontmatter is the canonical scenario list. Design must map every scenario and retained impact obligation to actual or proposed checks. Full required deterministic suites remain mandatory, preserving retained coverage; tests solely for explicitly deferred unshipped CLI/CI capabilities may be retired only through reviewed mapping and rationale. Supervised behavioral evaluations are required local evidence, separately identified from automated CI, unit fixtures, code reviews, recorded walkthroughs and unexecuted scenario specifications. The six existing scenario intents remain applicable: first planning gate, missing coverage, adequate reuse, retained failure, stale evidence and validation-only. Repetition counts and budgets belong in the reviewed evaluation plan; no unlimited retries or fixed new-test count is introduced.

## Constraints and assumptions

- The developer selected the supervised alternative. This revision presents its concrete Proposal/Requirements R2; Gate 1 approval unlocks revised Design, followed by revised Tasks and implementation under current approval and execution authority.
- Design preserves the explicit command interface, zero-test detection and freshness guarantees and specifies supervised scenario setup, independent verification and durable evidence. Unavailable runtime observations remain explicit; no native collaboration capability is assumed without verification.
- The revised canonical Testing Standard must retain all required automated CI suites and explicitly permit separately assessed supervised Skill evaluations with reproducible procedures and independent evidence. This scoped distinction does not waive required automated application evals. Unavailable required supervised evidence prevents delivery readiness.
- Dedicated API-key provisioning, isolated evaluator infrastructure, the mandatory Codex CLI adapter and protected live-model CI workflow are outside this delivery. Their existing unshipped assets must be removed or deferred through reviewed Design/Tasks, not represented as validated optional features. Existing platform-required checks remain authoritative; remote repository protection changes are not implied.
- Test generation is performed by the agent within the approved change. The execution integration runs configured commands and does not autonomously invent requirements, weaken assertions or revise approved tasks.
- No material unresolved product-scope blocker remains for Proposal/Requirements R2. Implementation details and their alternatives belong in the revised Design; prior approvals and results cannot be reused as proof of the revised evaluation contract.
