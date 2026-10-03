---
sdd_version: 3
change: automated-test-execution
status: proposed
owner: Versat
summary: Integrate project test execution and supervised native-subagent skill evaluations with the existing SDD coverage and evidence lifecycle.
risk: medium
impact:
  state: assessed
  summary: Preserve executable consumer integration, coverage, regressions and full required automated CI suites; replace this delivery's autonomous credentialed skill evaluation requirement with separately reviewed supervised behavioral evidence through a governed Testing Standard revision.
  items:
    - source:
        change: sdd-acceptance-regression
        requirement: REQ-001
        scenarios: [1, 2, 3]
        requirements_digest: 9da4509621ec9914ecd5f78b6334b6512bf85822fdde33e829ccddc7e3dd9cbe
      current_contract:
        path: standards/core/testing.md
        locator: '# Testing Standard'
        digest: 121ad9483f659b280a1c5d647af010c48df87382feb32f508639806cac49155c
      effect: extend
      targets: [REQ-002]
      reason: Make the agent create missing behavioral coverage within authorized implementation while reusing adequate checks and reviewed exclusions.
    - source:
        change: sdd-acceptance-regression
        requirement: REQ-005
        scenarios: [1, 2, 3, 4, 5]
        requirements_digest: 9da4509621ec9914ecd5f78b6334b6512bf85822fdde33e829ccddc7e3dd9cbe
      current_contract:
        path: standards/core/testing.md
        locator: '# Testing Standard'
        digest: 121ad9483f659b280a1c5d647af010c48df87382feb32f508639806cac49155c
      effect: extend
      targets: [REQ-002, REQ-003, REQ-005]
      reason: Execute maintained regression suites through the consumer entry point without dropping required checks or weakening retirement rules.
    - source:
        change: sdd-acceptance-regression
        requirement: REQ-006
        scenarios: [1, 2, 3, 4]
        requirements_digest: 9da4509621ec9914ecd5f78b6334b6512bf85822fdde33e829ccddc7e3dd9cbe
      current_contract:
        path: sdd/metadata.md
        locator: '## Input snapshots'
        digest: 788c3a0ae8ac265a66546d3dddbf35e2c0c81bfa932940f3e5eae34990a0a064
      effect: extend
      targets: [REQ-004]
      reason: Capture execution results and input freshness mechanically while retaining semantic assessment and the limits of local evidence.
    - source:
        change: sdd-acceptance-regression
        requirement: REQ-007
        scenarios: [1, 2, 3, 4]
        requirements_digest: 9da4509621ec9914ecd5f78b6334b6512bf85822fdde33e829ccddc7e3dd9cbe
      current_contract:
        path: sdd/metadata.md
        locator: '## Checks and traceability'
        digest: 788c3a0ae8ac265a66546d3dddbf35e2c0c81bfa932940f3e5eae34990a0a064
      effect: preserve
      targets: [REQ-003, REQ-004, REQ-008]
      reason: Keep structural validation read-only and distinguish running configured commands from checking declared evidence.
    - source:
        change: sdd-acceptance-regression
        requirement: REQ-008
        scenarios: [1, 2, 3, 4, 5]
        requirements_digest: 9da4509621ec9914ecd5f78b6334b6512bf85822fdde33e829ccddc7e3dd9cbe
      current_contract:
        path: sdd/process.md
        locator: '## Human gates'
        digest: 488b63b3ad26e4779db69d4b6ea9bd28b629936f58ccb42493cdaa99c940ccdb
      effect: preserve
      targets: [REQ-001, REQ-007, REQ-008]
      reason: Add automation through the existing governed lifecycle without migrating history or granting new authority.
    - current_contract:
        path: tests/skills/scenarios.md
        locator: '# SDD skill evaluation scenarios'
        digest: 6ec16454af5e84713d0eeaf98e5f90c5c690b55c6cf33b2127ebbb669035a824
      effect: extend
      targets: [REQ-006]
      reason: Exercise the skill through supervised native subagents with versioned synthetic inputs and independently verified artifacts and test execution; code review and scripted walkthroughs alone remain insufficient.
    - current_contract:
        path: project-templates/README.md
        locator: '## Composition'
        digest: 647350de506e4d8ed2d30e26e8572da0879ab1126701062bebbd83df361e39f9
      effect: extend
      targets: [REQ-001, REQ-007]
      reason: Supply composable validation integration and reviewed adoption without replacing project-specific commands or claiming that directory scaffolds execute tests.
    - current_contract:
        path: standards/core/testing.md
        locator: '## Explicit execution and coverage'
        digest: 121ad9483f659b280a1c5d647af010c48df87382feb32f508639806cac49155c
      effect: supersede
      targets: [REQ-005, REQ-006, REQ-008]
      reason: Replace this delivery's unreleased mandatory isolated credentialed Skill evaluation and automatic live CI outcome with required supervised behavioral evaluation and independent verification. Explicitly distinguish supervised Skill checks from required automated CI suites in the canonical Testing Standard; preserve all other required automated suites and separately assess supervised evidence before delivery.
review:
  revision: 2
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Developer response in this Codex conversation after presentation of Proposal/Requirements R2.
    quote: aprovado
    revision: 2
    digest: 3278e689b32cbd1d5f51e8357f445a5d59ed782662cfec3de05985aada41da3e
---

# Proposal

## Context and problem

The developer requested planning after reviewing automated testing in this repository. The developer reports updating the Marketplace/plugin to the same content as this checkout; that distribution discrepancy is treated as resolved for this change, without asserting independent verification of installed bytes.

The source already requires relevant acceptance coverage, maintained regression checks, full required CI suites and current evidence. `scripts/validate/run.sh` executes the Harness validator suite; `.github/workflows/validate.yml` invokes it for PRs and pushes to main. The repository has 131 test methods across `test_sdd.py` and `test_sdd_v3.py`. The unit suite includes a synthetic behavioral walkthrough, but `tests/skills/scenarios.md` explicitly distinguishes these checks from executing an autonomous agent using the skill.

Consumer templates document validation but do not provide a complete executable integration. SDD validation checks declared records and freshness; it deliberately does not execute prose check procedures. Consequently, generating missing tests and running consumer suites depends on the agent correctly translating guidance into project commands. The initial audit also encountered an interpreter without validation dependencies; a reusable local environment was subsequently found. Environment readiness must be reported accurately instead of being confused with passing tests.

## Expected outcome

An authorized implementation uses the approved acceptance and impact assessment to reuse or add meaningful tests. A documented project entry point executes new coverage and maintained regressions, records actual outcomes and supports required CI execution. For relevant Skill behavior changes, supervised native subagents exercise versioned scenarios in fresh synthetic project directories. The coordinator independently inspects artifacts and actions, re-executes tests and checks controlled defects, including approval boundaries and regression handling. Required supervised evidence is assessed separately from automated CI results.

## Scope

- A reviewable project validation configuration and execution entry point with explicit required suites, prerequisites and observable results.
- Integration with SDD implementation/validation, bootstrap and maintenance; Standards remain the policy source resolved through `standards/index.yaml`.
- A working Python reference consumer and technology-neutral support for explicitly configured project commands. Native test generators or automatic environment provisioning for every listed technology are not required.
- Behavioral test creation or reuse by the implementing agent, coupled with execution of retained regressions and full required CI suites.
- Execution evidence compatible with SDD's current snapshot, assessment and findings semantics.
- A supervised behavioral evaluation procedure using native subagents, fresh synthetic fixtures, available runtime/context records, reviewed time/attempt limits and retained observations. Scenario agents receive scenario context without the grading answer key or the implementation conversation.
- A governed revision of the canonical Testing Standard distinguishing required automated CI suites from required supervised Skill evaluations. The latter need independently verified evidence before delivery and cannot be labeled as automated CI passes.
- Removal or deferral of the unshipped credentialed CLI evaluation adapter and protected live-model workflow from this delivery's active implementation, with affected tests and guidance reconciled under the revised Design and Tasks.
- Documentation, migration guidance, deterministic regression tests and CI integration for the new capabilities.

## Out of scope

- Repeating the Marketplace update reported complete, publishing a release, or silently upgrading consumer pins.
- A universal test generator, automatic proof of assertion adequacy, a coverage-percentage mandate, or one new test per change regardless of need.
- Replacing test frameworks, automatically inferring every affected dependency, or building native adapters for every technology in the Standards index.
- A general workflow engine, remote merge/deployment automation, real business integrations, or granting commands additional permissions.
- Rewriting archived dossiers, adding planning gates, or treating a scripted walkthrough as a live agent evaluation.
- Provisioning a dedicated API key, isolated evaluation service or protected live-model GitHub environment; unattended model evaluation in CI is deferred to a separately justified change.
- Claiming that temporary directories isolate permissions, that a native subagent review alone is a behavioral evaluation, or that the session exposes complete transcripts or exact usage accounting when those observations are unavailable.

## Work tracking

No Shortcut Story or issue was supplied; no identifier is invented. The stable change ID is `automated-test-execution`, on local branch `codex/automated-test-execution`. No remote issue or PR has been created by this planning step.

## Impact and risks

The impact records bind historical requirements to effective current contracts. Existing suites and archived bytes remain regression obligations. This change extends execution support without transferring policy into Skills or turning structural validators into implicit command executors. ADR-0009, ADR-0011, ADR-0013 and ADR-0014 constrain Design; the execution boundary and any new configuration/schema contract need an ADR draft at Gate 2.

Configured test commands execute repository code. The executor must respect its caller's permissions and the CI trust boundary, particularly for PR content. A process runner and a temporary directory are not security sandboxes. Native subagents share the session filesystem and permissions; evaluation must use synthetic data and explicitly scoped work, without claiming filesystem isolation. They use the existing session and consume model usage without requiring a newly provisioned API key. Agent nondeterminism, runtime availability and cost require reviewed limits and honest unverified outcomes. Record only observable runtime, actions and usage information; unavailable telemetry is not invented. Input scopes can miss dependencies; execution records still need review and cannot authenticate arbitrary remote claims.

The root is the Harness package, not a consumer with `.versat/project.yaml` and `standards.lock`. Applicable core Standards are resolved from `standards/index.yaml`; Python and agent-related policies inform execution and evaluation. Consumer fixtures must declare their real profile, technologies and exact selected Harness context. No consumer identity is fabricated for the package root.

## Current contract baseline

Current package validation runs deterministic validator tests and contract checks. Consumer base instructions require the project's documented validation entry point but do not supply a generic command runner or CI setup. SDD check procedures are descriptive data and are never evaluated as shell commands. Existing skill scenarios are a maintained behavioral specification with synthetic/reviewer evidence, not an autonomous-agent execution suite. Required test suites must run before merge, while actual repository protection remains an external platform setting.

## Revision baseline and policy reconciliation

R1 and Design R2 required an autonomous Codex CLI evaluation adapter, scoped API credentials, an isolated environment and a protected live-model CI check. The local implementation includes those unshipped assets, 183 passing deterministic tests at their recorded revision and a successful CLI sandbox probe. The live behavioral evaluation and protected CI execution remain unverified. These historical observations do not establish the proposed supervised evaluation.

The developer requested adoption of the [alternative review](../../../docs/validation/automated-test-execution/alternative-review.md). R2 keeps REQ-001 through REQ-004 unchanged, revises REQ-005/006, and reconciles REQ-007/008. The baseline impact references describe the current checkout before this revision is implemented; the earlier approved baseline remains historical review context.

The Testing Standard currently requires required test/eval suites in CI and, in the unreleased implementation, isolated credentialed Skill evaluation. Adoption requires an explicit policy change: all required automated suites still run in CI; supervised Skill checks have a separately reviewed method, reproducible inputs, independently verified evidence and a required local delivery assessment. This is a narrow governed distinction for supervised Skill behavior, not permission to skip application evals, waive automated checks or substitute a review narrative for execution. Missing required supervised evidence blocks delivery even when deterministic CI passes.

Design must revise ADR-0015 and CHECK-004/CHECK-006/CHECK-008, then Tasks must reconcile already implemented CLI/CI assets and tests with the smaller scope. Those superseded artifacts remain historical context until their gates are revisited; R2 does not claim the replacement is already implemented.

## Proposal acceptance criterion

Approve the observable outcomes and boundaries in Requirements R2. Design must then specify the supervised scenario protocol, independent verification, evidence and repetition limits, canonical policy wording, removal/deferment of unshipped autonomous evaluation assets and required deterministic CI integration. Existing consumer execution and freshness guarantees remain. No unresolved product-scope question blocks Gate 1.

## Planning review

Historical approval: the developer approved Proposal and Requirements R1 in this Codex conversation on 2026-10-02 with "Sim, aprovado. Avance para o design.", binding combined digest `87e3e8d41aeea6ee4bdbc7a036cce8a9b9aa636c059d9c50fcd4b503147f9afb`. That approval is superseded and is not reassigned to R2.

Revision instruction: the developer requested "Adote a recomendação" and linked the alternative review in this conversation. This selects the revised direction and authorizes preparing these artifacts. Proposal/Requirements R2 is presented for Gate 1 review; Design R2 and Tasks R1 are marked superseded, with their actual approvals and execution evidence retained as history. Revised dependent implementation awaits the current planning gates.

The developer approved the presented Proposal/Requirements R2 with "aprovado" in the next conversation turn, binding digest `3278e689b32cbd1d5f51e8357f445a5d59ed782662cfec3de05985aada41da3e`. Gate 1 is current and authorizes preparation of Design R3.
