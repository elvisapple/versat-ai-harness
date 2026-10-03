---
sdd_version: 3
change: automated-test-execution
tasks:
- id: TASK-001
  description: Define versioned validation configuration and result contracts with pure deterministic enforcement.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-008
  status: completed
- id: TASK-002
  description: Implement bounded full and targeted suite execution with truthful attempt reporting.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-008
  status: completed
- id: TASK-003
  description: Add structured unittest and generic test reports with meaningful regression fixtures.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-008
  status: completed
- id: TASK-004
  description: Export current SDD execution evidence without mutating approvals or semantic assessments.
  requirements:
  - REQ-004
  - REQ-008
  status: completed
- id: TASK-005
  description: Compose consumer validation artifacts and integrate bootstrap and maintenance adoption.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-005
  - REQ-007
  status: in-progress
- id: TASK-006
  description: Implement real Codex skill evaluations with isolated scenarios and bounded observations.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  - REQ-008
  status: completed
- id: TASK-007
  description: Integrate complete deterministic CI and protected agent evaluation workflows including draft opt-in.
  requirements:
  - REQ-003
  - REQ-005
  - REQ-006
  - REQ-008
  status: completed
- id: TASK-008
  description: Update canonical testing policy, SDD usage and living guides to match implemented behavior.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: in-progress
- id: TASK-009
  description: Verify the reference consumer, complete local regressions and real agent behavior with current evidence.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  - REQ-007
  - REQ-008
  status: blocked
- id: TASK-010
  description: Observe authorized draft CI and complete pre-closure acceptance and retained-regression assessments.
  requirements:
  - REQ-004
  - REQ-005
  - REQ-008
  status: blocked
review:
  revision: 1
  state: superseded
  blockers: []
  upstream:
    proposal: 87e3e8d41aeea6ee4bdbc7a036cce8a9b9aa636c059d9c50fcd4b503147f9afb
    design: b5c643f91e45375fd15391db1556f64d4e6a3d1cf10dff6482b3eed375869691
  approval: null
validation:
  plan_digest: e092fe22186c0bdbd9ffc49bad5d8e9cc2771ab4d1332d888cd5e328134c84eb
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/automated-test-execution/local-e9f35bafe37c4e50996de2d3f303406e/CHECK-001.txt
    revision: input:bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a; attempt:local-e9f35bafe37c4e50996de2d3f303406e
    input_digest_before: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    input_digest_after: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/automated-test-execution/local-e9f35bafe37c4e50996de2d3f303406e/CHECK-002.txt
    revision: input:bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a; attempt:local-e9f35bafe37c4e50996de2d3f303406e
    input_digest_before: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    input_digest_after: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/automated-test-execution/local-e9f35bafe37c4e50996de2d3f303406e/CHECK-003.txt
    revision: input:bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a; attempt:local-e9f35bafe37c4e50996de2d3f303406e
    input_digest_before: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    input_digest_after: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-004
    result: unverified
    evidence: docs/validation/automated-test-execution/live/4e962b33a5534309805e4b513e9d5b4b/summary.json
    revision: input:bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a; preflight-only; runtime:81d17102a2798a1e254db6bc4838cba63143c5a0f111bdac6803b40ad47ff819
    input_digest_before: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    input_digest_after: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; no isolated runtime attestation or transport credential
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/automated-test-execution/local-e9f35bafe37c4e50996de2d3f303406e/CHECK-005.txt
    revision: input:bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a; attempt:local-e9f35bafe37c4e50996de2d3f303406e
    input_digest_before: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    input_digest_after: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-006
    result: unverified
    evidence: docs/validation/automated-test-execution/review.md
    revision: input:bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a; manual-review-continuation:2026-10-02
    input_digest_before: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    input_digest_after: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; CLI sandbox probe passed, live first-use unavailable
      observed: true
  - check: CHECK-007
    result: pass
    evidence: docs/validation/automated-test-execution/local-e9f35bafe37c4e50996de2d3f303406e/CHECK-007.txt
    revision: input:bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a; attempt:local-e9f35bafe37c4e50996de2d3f303406e
    input_digest_before: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    input_digest_after: bf4d1e7951da1bcc030bf23647151fcf77d4b137618440c965c5b641968f0e4a
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  assessments: []
  findings: []
closure: active
---

# Tasks

This plan implements approved Proposal/Requirements R1 and Design R2, including accepted ADR-0015. All tasks are pending; neither writing this plan nor approving an upstream stage completes implementation work. Use the exact Design CHECK definitions and mappings; do not substitute targeted tests for required suites or canned events for real agent evaluations.

## Ordered work

- [x] TASK-001 — Define versioned validation configuration and result contracts with pure deterministic enforcement.

  Create `schemas/validation.schema.yaml`, `schemas/validation-result.schema.yaml` and `validators/testing/validate.py`. Enforce nonempty unique required suites, command arrays, allowed substitutions, reviewed scopes, safe paths, supported result adapters, bounded execution settings and consistent report counts. Keep configuration inspection and validation free of project subprocess execution. Add configuration cases in `tests/execution/test_runner.py`.

  Completion: CHECK-001 and relevant CHECK-007 coverage pass for valid configurations and actionable rejection of duplicate/missing suites, malformed commands/reports, unsafe paths and unsupported adapter combinations. Test-like suites cannot claim success through the check-only exit-code adapter. Existing SDD validators still treat procedure text solely as data.

- [x] TASK-002 — Implement bounded full and targeted suite execution with truthful attempt reporting.

  Implement `scripts/testing/run.py` and focused helpers for `inspect` and `run`, required-suite selection, explicit targeted scope, restricted environment inheritance, no implicit shell evaluation and safe argument substitutions. Add exclusive attempt directories, snapshots, bounded logs, atomic result finalization, POSIX process-group cancellation, timeouts and aggregate exit/status semantics. Preserve every explicit rerun as a new attempt; do not add automatic retries or dependency installation.

  Completion: CHECK-001 launches harmless real subprocess fixtures and verifies full-suite union, targeted labeling, continued independent suites after assertion failure, missing executables, nonzero exits, timeout/interruption termination, incomplete attempts and safe output handling. Verify Python 3.11 on Linux and macOS; report unavailable platform verification instead of claiming support. Required source/config changes during execution prevent fresh success.

- [x] TASK-003 — Add structured unittest and generic test reports with meaningful regression fixtures.

  Implement `scripts/testing/unittest_report.py` and JSON-v1 report consumption. Require actual executed/skipped/failure/error counts, detect empty discovery and all-skipped tests, and reject stale or contradictory reports. Build synthetic reference consumer fixtures with new behavior plus maintained duplicate-payment, error and boundary assertions. Include custom framework-wrapper preservation, adequate test reuse, missing historical coverage, justified manual checks and reviewed test retirement cases in `tests/execution/test_consumer.py`.

  Completion: CHECK-001 and CHECK-003 demonstrate that a new happy path cannot hide a failing retained regression; seeded duplicate-payment and boundary defects fail meaningful assertions. Empty/all-skipped discovery never passes required tests. Restoring the intended behavior makes the maintained suite pass without deleting or weakening assertions. Mocked fixtures are not described as agent behavior.

- [x] TASK-004 — Export current SDD execution evidence without mutating approvals or semantic assessments.

  Add optional full-run `--change`/`--check` integration using the current SDD approval and snapshot interfaces. Verify approved automated checks, local/CI context, configuration/source scope and stable safe outputs; reject targeted export. Record before/after plan and input identity plus provider/runtime identity. Export one observed result fragment for review without writing the dossier, task statuses, findings or assessments. Add `tests/execution/test_sdd_evidence.py`.

  Completion: CHECK-002 verifies real execution, failed/unavailable outcomes, stale plans and inputs, during-run mutations, manual-method rejection, provider identity recording and archive-safe evidence paths. Fixture dossier bytes remain unchanged by the executor. Both existing v3 freshness tests and historical compatibility tests remain passing under CHECK-007.

- [ ] TASK-005 — Compose consumer validation artifacts and integrate bootstrap and maintenance adoption.

  Add opt-in reference assets under `project-templates/artifacts/validation/`: configuration, thin project wrapper, Python reference and CI example. Compose over base and the selected profile. Integrate selection and verification into bootstrap/maintenance through the canonical template guide; preserve existing project commands and surface conflicts. Verify exact selected Harness version/commit and declared consumer identity without fabricating a package-root consumer or fetching `latest`.

  Completion: CHECK-003 creates a usable disposable consumer, executes its documented full wrapper, preserves a custom command during adoption and exercises rollback. The example CI runs all required suites. CHECK-006 verifies exact-reference guidance, conflict handling and that no empty bootstrap scaffold claims tests ran. Required instructions are supplied alongside the usable artifacts.

- [x] TASK-006 — Implement real Codex skill evaluations with isolated scenarios and bounded observations.

  Add `scripts/eval/run.py`, `scripts/eval/codex.py`, versioned `tests/skills/cases/` and `tests/skills/runtime.schema.json`. Implement preflight for CLI 0.159.2, explicit model/reasoning configuration, sandbox availability and declared environment isolation. Run the six approved `sdd-critical` scenarios through actual skill instructions from the exact provider snapshot, with two fresh repetitions, sequential invocation, 600-second case and 7200-second suite bounds and a 12-invocation maximum. Capture tool events, artifact changes, usage where available, independent test replay and per-assertion outcomes.

  Completion: offline adapter tests in CHECK-007 cover malformed/missing events, unavailable runtime, exceeded bounds, retained failed attempts and grading that cannot pass on a final answer alone. All six scenarios have executable artifact/action assertions, synthetic approval provenance and seeded behavioral checks where applicable. No model-as-judge, automatic retry, unbounded invocation or approval bypass is introduced. Actual live acceptance is completed by TASK-009, not inferred from these adapter tests.

- [x] TASK-007 — Integrate complete deterministic CI and protected agent evaluation workflows including draft opt-in.

  Extend `scripts/validate/run.sh` to run the existing validator suite and all new offline execution/adapter tests. Preserve `.github/workflows/validate.yml` baseline/archive behavior. Add `.github/workflows/skill-evaluations.yml` with credential-free eligibility, protected evaluation and a credential-free aggregate check. Implement R2's `harness-run-evals` draft opt-in, relevant PR events, current-revision binding, cancellation when eligibility changes and exact-ref reruns once dispatch is available. Pin CLI/actions as approved by Design; secrets remain inaccessible to untrusted sources.

  Completion: CHECK-005 executes workflow command branches against harmless fixtures and confirms no successful skip for required live evaluation, no privileged fork fallback, no `pull_request_target`, correct draft/ready behavior and rejection of stale revision/label state. CHECK-007 runs the expanded suite in full. Documentation identifies required platform protections and unavailable protection as a prerequisite failure; workflow-file existence does not claim remote configuration or observed execution.

- [ ] TASK-008 — Update canonical testing policy, SDD usage and living guides to match implemented behavior.

  Refine `standards/core/testing.md` only for the approved execution/coverage contract, keeping Standards canonical and resolved through the index. Update implementation/validation workflow instructions for test creation or reuse, full versus targeted runs, evidence fragments and truthful gaps. Update template composition/migration guidance, `docs/architecture/overview.md`, affected README/quickstart links, and the new `docs/guides/project-validation.md` and `docs/guides/skill-evaluations.md`. Cover clean setup, supported environments, failure outputs, runtime configuration, credential boundaries, draft evidence collection, archival and rollback. Record the source change in the existing changelog convention without claiming a published release.

  Completion: CHECK-006 follows the documented first-use path in a disposable environment, checks actual output against examples and reviews assertions and evidence adequacy. All links resolve; Skills route through canonical contracts without copying policy. The guides distinguish local success, live evaluation, draft CI, final required CI and merge. No existing history is rewritten and no release/cache update is implied.

- [ ] TASK-009 — Verify the reference consumer, complete local regressions and real agent behavior with current evidence.

  Run CHECK-001 through CHECK-007 against the implemented branch, including CHECK-004 with the reviewed runtime configuration in an authorized isolated environment. Record real local results and semantic review under `docs/validation/automated-test-execution/`, using current Tasks/Design bindings and before/after snapshots. Verify all six cases twice, retain failures, and correct only within approved task scope before rerunning affected checks. Assess local scenarios and retained obligations that these checks cover.

  Completion: the full deterministic suite, reference consumer, documentation review and all required live assertions have current passing evidence. Assertions catch the seeded regressions; the recorded agent really used the skill and executed relevant checks. Missing model access, authentication, sandbox or an unavailable verified platform remains unverified and leaves this task incomplete. Execution reports never replace semantic assessment.

- [ ] TASK-010 — Observe authorized draft CI and complete pre-closure acceptance and retained-regression assessments.

  After local implementation and validation, use R2's explicitly authorized incomplete implementation draft route to obtain CHECK-008 evidence. Verify actual protected-environment prerequisites before credentialed execution, observe both full deterministic and protected evaluation runs for the tested revision, and record durable run references plus provider/model/runtime identities. Preserve failed/unavailable results and report gaps. Complete the 27 local and 23 retained-regression assessments and resolve findings only with current supporting evidence.

  Completion: CHECK-008's pre-closure draft runs are observed passing; all eight required Design checks and all mapped obligations have adequate current evidence, with no unresolved acceptance findings. Confirm the resulting task/evidence records are consistent before marking this task complete. Remote publication, labeling and environment/settings mutations require their actual scoped authority; without it or the required platform support, record the specific dependency and leave execution incomplete. Final post-archive CI and merge are delivery controls, not hidden completion conditions for this task.

## Dependencies

| Task | Prerequisites | Main verification |
| --- | --- | --- |
| TASK-001 | Current Tasks approval and existing implementation authorization | CHECK-001, CHECK-007 |
| TASK-002 | TASK-001 | CHECK-001 |
| TASK-003 | TASK-001, TASK-002 | CHECK-001, CHECK-003 |
| TASK-004 | TASK-001, TASK-002 | CHECK-002, CHECK-007 |
| TASK-005 | TASK-003, TASK-004 | CHECK-003, CHECK-006 |
| TASK-006 | TASK-003, TASK-004 | CHECK-007; live execution in TASK-009 |
| TASK-007 | TASK-005, TASK-006 | CHECK-005, CHECK-007 |
| TASK-008 | TASK-005, TASK-006, TASK-007 | CHECK-006 |
| TASK-009 | TASK-001 through TASK-008; usable isolated evaluation runtime | CHECK-001 through CHECK-007 |
| TASK-010 | TASK-009; authorized draft CI and supported platform protections | CHECK-008 and complete acceptance assessment |

Tasks are logical deliverables, not mandatory individual commits. Each implementation task includes its focused tests; TASK-009 consolidates current evidence rather than postponing all testing until the end. TASK-004 and TASK-003 are independent after TASK-002, and TASK-005 and TASK-006 can progress independently once their prerequisites are met. This plan does not request additional agents or parallel execution.

The complete existing validator suite remains mandatory; future additions increase it rather than freezing a test-count threshold. CHECK-008's first observed CI evidence is collected while the PR is explicitly incomplete, before archival. Final ready-for-review checks run afterward under the normal delivery lifecycle. This ordering preserves R2's resolution of the archive/CI dependency cycle.

## Prerequisites and risk handling

- No unresolved scope or architectural decision blocks review of Tasks R1. Proposal R1 and Design R2 are approved; ADR-0015 is accepted.
- Model ID/reasoning settings, actual runtime access and protected CI configuration are execution prerequisites. Inspect them before dependent execution; never fabricate credentials, substitute a model silently or enable an unprotected credentialed job. An unavailable prerequisite blocks the affected task, not unrelated authorized implementation.
- Existing implementation authority covers local work after Tasks review. It does not itself authorize publishing a draft, changing remote protection or approving a protected environment. Prepare reviewable local artifacts before requesting any still-missing remote authority.
- Preserve approved bounds and all attempted outcomes. Failures in required regression or live evaluations cannot be waived by skipping, weakening assertions or calling them inapplicable. A material change to the agreed runtime or trust design reopens the corresponding review.
- Preserve exact-version consumer governance, archived bytes and existing tests. This plan adds no release publication, consumer rollout, automatic recurring run or post-merge task.

## Planning review

Current status: superseded by the developer-selected supervised evaluation alternative and Proposal/Requirements R2. The historical approval below is retained for audit only; it does not authorize execution under the revised scope. Substantive design/task content and recorded results remain tied to the previous plan until the renewed upstream gates are approved.

The developer approved the presented Tasks R1 in this Codex conversation on 2026-10-02 with "sim", binding digest `e092fe22186c0bdbd9ffc49bad5d8e9cc2771ab4d1332d888cd5e328134c84eb`. Historical implementation proceeded under the previously supplied "Ok pode implementar." authorization. Remote publication and platform mutations retain their separate scope.

## Progress

Replanning status: implementation progress and dependencies below describe the superseded Tasks R1. Existing completion states are preserved as historical facts, not readiness for Proposal/Requirements R2. The old API-key and protected-evaluation prerequisites are to be replaced through renewed Design and Tasks; dependent implementation is paused at Gate 1.

Implementation update on 2026-10-02: TASK-001 through TASK-004, TASK-006 and TASK-007 have completed their local implementation checks. TASK-002 has actual macOS/Python 3.11 evidence; Linux verification is unavailable locally and remains explicitly unclaimed until CI.

TASK-005 and TASK-008 have implemented artifacts/guides and a working disposable consumer wrapper; they remain in progress until CHECK-006's complete isolated evaluation first-use review. TASK-009 is blocked on DEP-001 (a dedicated isolated environment and scoped `CODEX_API_KEY`); the developer selected `gpt-6-astra` with `high` reasoning. TASK-010 is blocked on DEP-002 (authorized incomplete draft, verified protected environment and observed CI), and final acceptance assessments remain pending. DEP-003 tracks the incomplete live first-use portion of CHECK-006. These are execution prerequisites, not invented failed model/CI observations. See the stable [review report](../../../docs/validation/automated-test-execution/review.md).

The existing provider/marketplace version is unchanged. No live model request, remote publication/settings mutation, archival or release was performed. The approved task descriptions and plan digests remain unchanged; statuses and the evidence below record actual progress.

## Validation evidence

All results below belong to the superseded plan. They do not establish acceptance of supervised behavioral evaluation or readiness under Proposal/Requirements R2. No previous result has been relabeled or rehashed for the new scope.

The [current local execution record](../../../docs/validation/automated-test-execution/local-e9f35bafe37c4e50996de2d3f303406e/results.json) binds passing CHECK-001, CHECK-002, CHECK-003, CHECK-005 and CHECK-007 to current before/after input digests and Tasks R1. CHECK-007 ran 131 maintained validator tests and 52 new execution/adapter tests. The earlier successful and the intervening failed attempts remain retained, with the latter caused by stale recorded digests before bookkeeping was refreshed. The [review](../../../docs/validation/automated-test-execution/review.md) records partial first-use/semantic observations; CHECK-006 is unverified because the isolated live first-use path is unavailable. Its before/after digests match.

CHECK-004 has an observed preflight-only unverified result with zero model attempts. CHECK-008 has no execution result because remote CI has not run. Offline adapter/CI fixtures never substitute for those observations. Final assessments of the 27 local and 23 retained obligations remain pending rather than recording unsupported pass claims. Progress dependencies identify the necessary runtime credential and remote authority. A real Codex 0.159.2 sandbox probe passed on macOS after selecting the built-in `:workspace` permission profile. The CHECK-004 preflight is recorded as unverified with zero model attempts; GitHub has no `skill-evaluations` environment or runtime variable. There are no observed implementation defects being waived or hidden as completed acceptance.

## Delivery

Closure remains `active`. After all tasks and required evidence are complete, run selected delivery validation before preparing archive storage. On authorized submission, archive the unique dossier in the same implementation branch/PR, verify links and run `--phase delivery --require-archive` before marking the PR ready. Observe final required CI, review and merge separately; archive location and local checks never assert these external facts. No task depends on a post-merge action.
