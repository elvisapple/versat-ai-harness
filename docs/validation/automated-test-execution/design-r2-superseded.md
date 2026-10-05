---
sdd_version: 3
change: automated-test-execution
requirements:
- REQ-001
- REQ-002
- REQ-003
- REQ-004
- REQ-005
- REQ-006
- REQ-007
- REQ-008
adrs:
- ADR-0015
validation:
- id: CHECK-001
  description: Configuration and actual subprocess execution
  requirements:
  - REQ-001
  - REQ-003
  - REQ-008
  required: true
  method:
    kind: automated
    procedure: 'Proposed: python -m unittest discover -s tests/execution -p test_runner.py. Execute harmless fixture
      commands and assert configuration errors, required-suite union, targeted labeling, nonzero exits, missing
      tools, zero collected or all-skipped tests, timeouts, SIGINT termination and preserved attempt reports. Verify
      invalid or escaping paths fail and SDD prose is never executed.'
  inputs:
    include: &id001
    - AGENTS.md
    - README.md
    - VERSION
    - plugin.json
    - .codex-plugin
    - .agents/plugins
    - requirements-validation.txt
    - standards
    - schemas
    - skills
    - sdd
    - validators
    - scripts
    - tests
    - project-templates
    - .github
    - docs
    exclude:
    - docs/validation/automated-test-execution
  outputs:
  - docs/validation/automated-test-execution
  execution: local
- id: CHECK-002
  description: SDD execution evidence integration and freshness
  requirements:
  - REQ-004
  - REQ-008
  required: true
  method:
    kind: automated
    procedure: 'Proposed: python -m unittest discover -s tests/execution -p test_sdd_evidence.py. Use approved synthetic
      v3 plans, execute real commands, validate generated result fragments and assert plan/config/input changes,
      during-run mutation, output relocation, manual methods, unavailable execution and archive-move handling. Assert
      no approvals, assessments, task states or findings are modified by the runner.'
  inputs:
    include: *id001
    exclude:
    - docs/validation/automated-test-execution
  outputs:
  - docs/validation/automated-test-execution
  execution: local
- id: CHECK-003
  description: Reference consumer, coverage adequacy and migration behavior
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-005
  - REQ-007
  - REQ-008
  required: true
  method:
    kind: automated
    procedure: 'Proposed: python -m unittest discover -s tests/execution -p test_consumer.py. Materialize base plus
      Python reference configuration in temporary repositories, preserve custom commands, execute new and retained
      payment tests, seed duplicate-payment and boundary defects, and verify failures. Exercise reviewed reuse,
      missing old coverage, explicit supersession/manual dispositions, clean setup and rollback. This tests integration
      and fixtures; CHECK-004 separately tests agent behavior.'
  inputs:
    include: *id001
    exclude:
    - docs/validation/automated-test-execution
  outputs:
  - docs/validation/automated-test-execution
  execution: local
- id: CHECK-004
  description: Real Codex skill evaluation with observed behavior
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  - REQ-008
  required: true
  method:
    kind: automated
    procedure: 'Proposed: python scripts/eval/run.py --root . --suite sdd-critical --runtime-config <reviewed-runtime-json>
      --output docs/validation/automated-test-execution/live. Execute the six scenarios and two repetitions per
      scenario specified below using real Codex CLI, a fixed configured model and disposable projects. Require all
      artifact/action assertions and seeded behavior checks to pass; retain every attempt. Missing runtime, authentication,
      observations or exceeded limits is non-passing. Record actual runtime configuration, model and source digest;
      never substitute mocked events.'
  inputs:
    include: *id001
    exclude:
    - docs/validation/automated-test-execution
  outputs:
  - docs/validation/automated-test-execution
  execution: local
- id: CHECK-005
  description: CI dispatch, required-suite and trust-boundary contracts
  requirements:
  - REQ-003
  - REQ-005
  - REQ-008
  required: true
  method:
    kind: automated
    procedure: 'Proposed: python -m unittest discover -s tests/execution -p test_ci.py. Execute workflow command
      branches against harmless fixtures for planning drafts, explicitly opted-in implementation drafts, ready,
      push, protected PR evaluations and manually dispatched exact-ref reruns. Assert
      full required suites, nonzero prerequisite outcomes, baseline/archive forwarding, exact SHA rejection, aggregate-eval
      gating, opt-in removal and absence of credentialed untrusted PR or pull_request_target execution. Mock only CI platform metadata; do
      not report remote CI as observed.'
  inputs:
    include: *id001
    exclude:
    - docs/validation/automated-test-execution
  outputs:
  - docs/validation/automated-test-execution
  execution: local
- id: CHECK-006
  description: First-use, architecture and semantic review
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  required: true
  method:
    kind: review
    procedure: Follow the proposed docs/guides/project-validation.md and docs/guides/skill-evaluations.md in a clean
      disposable supported environment. Review actual test assertions and generated evidence against acceptance
      and retained obligations; verify Standards resolution, base composition, migration conflicts, rollback, configured
      suite-to-SDD mappings, source/runtime digests and CI gating documentation. Confirm missing dependencies and
      manual checks are described honestly. Compare observed commands and outcomes; record gaps in a dated report
      under docs/validation/automated-test-execution/review.md.
    reason: Semantic adequacy and observed platform configuration cannot be proved by local schema checks or mocked
      CI metadata.
  inputs:
    include: *id001
    exclude:
    - docs/validation/automated-test-execution
  outputs:
  - docs/validation/automated-test-execution
  execution: local
- id: CHECK-007
  description: Complete maintained Harness deterministic regression suite
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  required: true
  method:
    kind: automated
    procedure: 'Existing entry point, extended suite: PYTHON=<prepared-python-3.11-interpreter> ./scripts/validate/run.sh.
      Require package and SDD inventory checks, all existing validator tests and all new execution/evaluation adapter
      tests to pass. Also run selected SDD delivery and the existing archive guard at their appropriate lifecycle
      points; preserve historical records and baseline rules. This check does not invoke a model or stand in for
      CHECK-004 or CHECK-008.'
  inputs:
    include: *id001
    exclude:
    - docs/validation/automated-test-execution
  outputs:
  - docs/validation/automated-test-execution
  execution: local
- id: CHECK-008
  description: Observed required CI runs on the submitted revision
  requirements:
  - REQ-005
  - REQ-008
  required: true
  method:
    kind: review
    procedure: Observe the actual deterministic validation workflow and protected skill-evaluations workflow for
      the explicitly authorized implementation draft's exact revision before closure. This check completes with
      observed passing draft runs and their evidence; final required CI after archive preparation and ready-for-review
      remains a separate delivery control, not a precondition for this check. Confirm required full suites,
      draft baseline behavior, tested archive-guard regressions and observed agent-evaluation
      results. Use a trusted synthetic failing-regression revision or dispatch exercise to confirm non-passing status,
      and verify missing required live runtime cannot become readiness. Record observed run URLs and commit identities;
      absent access or unavailable protected environment is unverified, not a fabricated pass.
    reason: Semantic adequacy and observed platform configuration cannot be proved by local schema checks or mocked
      CI metadata.
  inputs:
    include: *id001
    exclude:
    - docs/validation/automated-test-execution
  outputs:
  - docs/validation/automated-test-execution
  execution: ci
coverage:
- scenario:
    requirement: REQ-001
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
  - CHECK-003
- scenario:
    requirement: REQ-001
    scenario: 2
  applicability: required
  checks:
  - CHECK-003
  - CHECK-006
- scenario:
    requirement: REQ-001
    scenario: 3
  applicability: required
  checks:
  - CHECK-001
  - CHECK-003
- scenario:
    requirement: REQ-002
    scenario: 1
  applicability: required
  checks:
  - CHECK-003
  - CHECK-004
  - CHECK-006
- scenario:
    requirement: REQ-002
    scenario: 2
  applicability: required
  checks:
  - CHECK-003
  - CHECK-004
- scenario:
    requirement: REQ-002
    scenario: 3
  applicability: required
  checks:
  - CHECK-003
  - CHECK-006
- scenario:
    requirement: REQ-003
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
  - CHECK-003
  - CHECK-004
- scenario:
    requirement: REQ-003
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-005
- scenario:
    requirement: REQ-003
    scenario: 3
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-003
    scenario: 4
  applicability: required
  checks:
  - CHECK-001
  - CHECK-004
- scenario:
    requirement: REQ-004
    scenario: 1
  applicability: required
  checks:
  - CHECK-002
  - CHECK-006
- scenario:
    requirement: REQ-004
    scenario: 2
  applicability: required
  checks:
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-004
    scenario: 3
  applicability: required
  checks:
  - CHECK-002
  - CHECK-006
- scenario:
    requirement: REQ-004
    scenario: 4
  applicability: required
  checks:
  - CHECK-002
- scenario:
    requirement: REQ-005
    scenario: 1
  applicability: required
  checks:
  - CHECK-003
  - CHECK-005
  - CHECK-008
- scenario:
    requirement: REQ-005
    scenario: 2
  applicability: required
  checks:
  - CHECK-005
  - CHECK-007
  - CHECK-008
- scenario:
    requirement: REQ-005
    scenario: 3
  applicability: required
  checks:
  - CHECK-005
  - CHECK-008
- scenario:
    requirement: REQ-006
    scenario: 1
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-006
    scenario: 2
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-006
    scenario: 3
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-006
    scenario: 4
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-007
    scenario: 1
  applicability: required
  checks:
  - CHECK-003
  - CHECK-006
- scenario:
    requirement: REQ-007
    scenario: 2
  applicability: required
  checks:
  - CHECK-003
  - CHECK-006
- scenario:
    requirement: REQ-007
    scenario: 3
  applicability: required
  checks:
  - CHECK-003
  - CHECK-006
- scenario:
    requirement: REQ-008
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
  - CHECK-002
  - CHECK-005
  - CHECK-007
- scenario:
    requirement: REQ-008
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-002
- scenario:
    requirement: REQ-008
    scenario: 3
  applicability: required
  checks:
  - CHECK-006
  - CHECK-007
regression:
- obligation:
    impact: 1
    scenario: 1
  checks:
  - CHECK-003
  - CHECK-004
  - CHECK-006
  rationale: Make the agent create missing behavioral coverage within authorized implementation while reusing adequate
    checks and reviewed exclusions. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 1
    scenario: 2
  checks:
  - CHECK-003
  - CHECK-004
  - CHECK-006
  rationale: Make the agent create missing behavioral coverage within authorized implementation while reusing adequate
    checks and reviewed exclusions. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 1
    scenario: 3
  checks:
  - CHECK-003
  - CHECK-004
  - CHECK-006
  rationale: Make the agent create missing behavioral coverage within authorized implementation while reusing adequate
    checks and reviewed exclusions. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 2
    scenario: 1
  checks:
  - CHECK-003
  - CHECK-005
  - CHECK-007
  rationale: Execute maintained regression suites through the consumer entry point without dropping required checks
    or weakening retirement rules. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 2
    scenario: 2
  checks:
  - CHECK-003
  - CHECK-005
  - CHECK-007
  rationale: Execute maintained regression suites through the consumer entry point without dropping required checks
    or weakening retirement rules. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 2
    scenario: 3
  checks:
  - CHECK-003
  - CHECK-005
  - CHECK-007
  rationale: Execute maintained regression suites through the consumer entry point without dropping required checks
    or weakening retirement rules. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 2
    scenario: 4
  checks:
  - CHECK-003
  - CHECK-005
  - CHECK-007
  rationale: Execute maintained regression suites through the consumer entry point without dropping required checks
    or weakening retirement rules. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 2
    scenario: 5
  checks:
  - CHECK-003
  - CHECK-005
  - CHECK-007
  rationale: Execute maintained regression suites through the consumer entry point without dropping required checks
    or weakening retirement rules. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 3
    scenario: 1
  checks:
  - CHECK-002
  - CHECK-007
  rationale: Capture execution results and input freshness mechanically while retaining semantic assessment and
    the limits of local evidence. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 3
    scenario: 2
  checks:
  - CHECK-002
  - CHECK-007
  rationale: Capture execution results and input freshness mechanically while retaining semantic assessment and
    the limits of local evidence. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 3
    scenario: 3
  checks:
  - CHECK-002
  - CHECK-007
  rationale: Capture execution results and input freshness mechanically while retaining semantic assessment and
    the limits of local evidence. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 3
    scenario: 4
  checks:
  - CHECK-002
  - CHECK-007
  rationale: Capture execution results and input freshness mechanically while retaining semantic assessment and
    the limits of local evidence. Retain the existing tests; verify current execution separately from historical
    evidence.
- obligation:
    impact: 4
    scenario: 1
  checks:
  - CHECK-001
  - CHECK-002
  - CHECK-007
  rationale: Keep structural validation read-only and distinguish running configured commands from checking declared
    evidence. Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 4
    scenario: 2
  checks:
  - CHECK-001
  - CHECK-002
  - CHECK-007
  rationale: Keep structural validation read-only and distinguish running configured commands from checking declared
    evidence. Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 4
    scenario: 3
  checks:
  - CHECK-001
  - CHECK-002
  - CHECK-007
  rationale: Keep structural validation read-only and distinguish running configured commands from checking declared
    evidence. Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 4
    scenario: 4
  checks:
  - CHECK-001
  - CHECK-002
  - CHECK-007
  rationale: Keep structural validation read-only and distinguish running configured commands from checking declared
    evidence. Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 5
    scenario: 1
  checks:
  - CHECK-003
  - CHECK-006
  - CHECK-007
  rationale: Add automation through the existing governed lifecycle without migrating history or granting new authority.
    Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 5
    scenario: 2
  checks:
  - CHECK-003
  - CHECK-006
  - CHECK-007
  rationale: Add automation through the existing governed lifecycle without migrating history or granting new authority.
    Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 5
    scenario: 3
  checks:
  - CHECK-003
  - CHECK-006
  - CHECK-007
  rationale: Add automation through the existing governed lifecycle without migrating history or granting new authority.
    Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 5
    scenario: 4
  checks:
  - CHECK-003
  - CHECK-006
  - CHECK-007
  rationale: Add automation through the existing governed lifecycle without migrating history or granting new authority.
    Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 5
    scenario: 5
  checks:
  - CHECK-003
  - CHECK-006
  - CHECK-007
  rationale: Add automation through the existing governed lifecycle without migrating history or granting new authority.
    Retain the existing tests; verify current execution separately from historical evidence.
- obligation:
    impact: 6
    scenario: 0
  checks:
  - CHECK-004
  - CHECK-006
  rationale: Exercise the skill through an actual agent executor and grade observed actions in addition to existing
    deterministic fixtures and reviewer walkthroughs. Retain the existing tests; verify current execution separately
    from historical evidence.
- obligation:
    impact: 7
    scenario: 0
  checks:
  - CHECK-003
  - CHECK-006
  rationale: Supply composable validation integration and reviewed adoption without replacing project-specific commands
    or claiming that directory scaffolds execute tests. Retain the existing tests; verify current execution separately
    from historical evidence.
review:
  revision: 2
  state: superseded
  blockers: []
  upstream:
    proposal: 87e3e8d41aeea6ee4bdbc7a036cce8a9b9aa636c059d9c50fcd4b503147f9afb
  approval: null
---

# Design

## Current state

Proposal/Requirements R1 was approved on 2026-10-02 with “Sim, aprovado. Avance para o design.” Its combined digest is recorded in `review.upstream`. This Design proposes implementation; none of the proposed commands or files below are delivered by this planning artifact.

The current package has 131 deterministic tests, a package validation script and a GitHub Actions workflow. The existing suite passed during Gate 1 planning. Consumer validation remains project-defined. `validators/sdd/sdd_inputs.py` hashes declared scopes; `sdd_assurance.py` checks declared scenario/evidence consistency. Neither executes check prose. Existing skill scenarios and the synthetic reviewer walkthrough do not run a model.

The source package is the provider, not a consumer with fabricated identity metadata. Consumer fixtures use real schema-valid synthetic identity and exact source references. Applicable policy is resolved from `standards/index.yaml` at this checkout: core policies apply, with Python for implementation and agent/AI policy for evaluation. This root has no consumer lockfile. Tests must exercise consumer resolution from the selected index, not copy a second list of policies into Skills.

## Proposed design

### Components and ownership

| Location (proposed unless marked existing) | Responsibility |
| --- | --- |
| `schemas/validation.schema.yaml`, `schemas/validation-result.schema.yaml` | Version 1 project execution and attempt-report contracts |
| `validators/testing/validate.py` | Pure configuration/result checks; no subprocess execution |
| `scripts/testing/run.py` and adjacent helpers | Explicit local/CI subprocess execution, suite collection checks and SDD result-fragment export |
| `scripts/testing/unittest_report.py` | Python unittest adapter producing structured counts and outcomes |
| `scripts/eval/run.py`, `scripts/eval/codex.py` | Evaluation orchestration and isolated Codex CLI adapter |
| `tests/skills/cases/`, `tests/skills/runtime.schema.json` | Versioned scenario inputs, artifact/action assertions and explicit runtime configuration |
| `tests/execution/` | Offline runner, evidence, consumer, CI and Codex-event parser tests |
| `project-templates/artifacts/validation/` | Opt-in reference configuration, wrapper and workflow assets, composed once over base |
| `standards/core/testing.md`, `sdd/workflows/` (existing) | Policy clarifications and lifecycle integration |
| `docs/guides/project-validation.md`, `docs/guides/skill-evaluations.md` | Setup, usage, evidence, failures, migration and rollback |

The core runner uses Python 3.11 and the existing pinned YAML/JSON Schema dependencies. First verified environments are Python 3.11 on Linux CI and macOS local execution. Other Python versions/operating systems are not advertised as verified. POSIX process-group termination is tested on these systems; unsupported platforms return an explicit prerequisite error rather than silently lose cancellation guarantees.

No new public Skill or fifth SDD file is introduced. `versat-sdd` remains the entry point. Bootstrap and maintenance select the validation artifact only when they can configure real suites. The Python example extends base and the relevant profile; it does not clone base or install sample business logic in consumers.

### Project configuration

Consumers store `.versat/validation.yaml` with `schema_version: 1`. The provider runner is loaded from an explicit `--harness-root`/`VERSAT_HARNESS_ROOT` path selected by the consumer wrapper. It never downloads a release or searches for `latest`. Bootstrap/maintenance verify the selected package against the exact version/commit in `standards.lock` and record any development-source snapshot explicitly. Package tests invoke provider commands directly, without inventing a consumer manifest.

Configuration contains:

- `required_suites`: a nonempty unique list of suite IDs for full validation. Requiredness lives here, not in separate contradictory flags.
- `suites`: unique IDs with `kind: tests | check`, nonempty `argv`, project-relative `cwd`, bounded `timeout_seconds`, optional declared environment variable names and a `result` adapter.
- `result`: `unittest`, `json-v1`, or `exit-code`. Test suites require structured counts through the first two; `exit-code` is allowed only for checks such as lint/schema validation. A producer must report executed, skipped, failed and error counts; executed excludes skipped. Required tests with zero executed cases, all-skipped results, absent reports or inconsistent totals cannot pass. No regex scraping of framework console output.
- `inputs`: reviewed include/exclude roots used for standalone run snapshots; SDD-bound execution additionally uses the approved check scopes. Runner configuration and project wrappers must be included. Output roots cannot overlap explicit inputs.

Arguments are arrays passed without an implicit shell. Shell scripts remain usable as explicit executables/arguments (for example `bash scripts/check.sh`) and carry the same trust as other repository code. Only complete argument tokens `{python}`, `{harness_root}` and `{report}` are substituted; they are runner-owned values, never shell expansion. Unknown tokens are configuration errors. Arbitrary string interpolation, `eval`, and parsing SDD narrative as commands are prohibited.

The Python reference uses the runner's interpreter, unittest discovery in the consumer test directory, and a structured output file under the fresh attempt directory. The generic JSON adapter lets existing frameworks use a small project-owned wrapper rather than adding a framework adapter to the Harness. Wrappers must translate their actual framework report, not fabricate case counts. Unit tests seed empty discovery and malformed reports. Framework assertions still require semantic review.

### Execution interface and outcomes

The consumer documents a thin `scripts/validate/run.sh` wrapper invoking the selected package's `scripts/testing/run.py`. Existing wrappers are extended through review, never blindly replaced. The provider CLI is:

```text
python scripts/testing/run.py inspect --root PROJECT
python scripts/testing/run.py run --root PROJECT
python scripts/testing/run.py run --root PROJECT --suite UNIT
python scripts/testing/run.py run --root PROJECT --change CHANGE --check CHECK-ID
```

`inspect` reads configuration and checks prerequisites without executing project commands. `run` without suite selection executes every `required_suites` entry in declared order. `--suite` selects development checks, always labels the result `targeted`, and cannot be combined with SDD evidence export. Full execution continues independent suites after an ordinary failed suite to collect failures; interruption, unsafe configuration or missing execution infrastructure stops affected work with explicit statuses. No dependency graph, scheduler or automatic retries is added.

A full invocation has `pass`, `fail`, or `unverified` with exit codes 0, 1, or 2 respectively. Configuration violations, assertion failures, timeouts, zero tests, malformed reports and interrupted execution are non-passing. Missing tools/services/authentication are unverified. Failure takes precedence over unverified in aggregation. Successful targeted runs may exit 0 but carry `scope: targeted` and `readiness: false`. Full success means configured required suites passed, not SDD delivery readiness or exhaustive coverage.

Each invocation gets a unique exclusive output directory, an initial running record and final atomic JSON report. Suites run once per invocation. Explicit reruns create new attempts and retain previous failures. Record suite IDs, resolved executable identity, argv without secrets, input/config digests, start/end/duration, exit/signal, count/report status and bounded stdout/stderr. Timeout or SIGINT terminates the process group, escalates termination after a bounded grace period, and finalizes the report where possible. A hard kill can leave `running`; that incomplete attempt is never a pass. Reports and logs have size caps, and truncation is explicit; losing a required structured report is non-passing.

### SDD evidence integration

No SDD schema-version change is required. The optional `--change` and `--check` pair selects one reviewed automated check. Before launch, the runner uses the existing validation API/CLI to require current planning approvals, no implementation blockers, `method.kind: automated`, matching local/CI execution context, safe outputs and a scope including validation configuration and project command sources. The check procedure must identify this full validation invocation and its intended suite coverage for reviewer inspection; the runner does not infer that arbitrary suites prove a requirement.

Capture the existing Tasks plan digest and check input digest immediately before and after the run. If approvals, plan, mapping, execution configuration or inputs changed, preserve the attempted result but withhold a passing SDD fragment. Require the effective provider execution-code digest to remain stable during execution and record it along with the selected Harness reference. Later known runtime/provider changes require reruns; v3 local snapshots alone do not authenticate external installations.

For an eligible attempt, write an SDD-compatible result fragment containing the check ID, observed outcome/context, stable evidence path, actual revision/run identity and both input digests. The agent reviews and incorporates the fragment into Tasks using the existing lifecycle. The runner never edits the dossier, supplies semantic assessments, resolves findings, checks off tasks or grants approvals. Agent/reviewer verification of suite-to-scenario adequacy remains required. Failed or unavailable runs can be recorded truthfully; a fragment is not a delivery assertion.

Standalone runs may write to `.versat/validation-runs/`; SDD-bound runs write directly under the selected check's approved stable output directory outside its dossier. Refuse output traversal, symlinks and overwrite of old attempts. Broad input scopes need an approved exclusion of the complete output subtree. Shared SDD snapshot helpers remain pure: the executor depends on validation, not the reverse. Manual/review checks use the existing evidence workflow and cannot be automatically relabeled automated.

### Creating and retaining tests

During Design, identify actual entry points and coverage gaps. During authorized implementation, add useful missing tests beside the maintained suite and reuse sufficient coverage. Relevant success, error and boundary assertions must detect a seeded defect in the synthetic reference cases. Existing regression assertions remain required even when their dossier is archived. Missing historical tests are added as approved current work. Reviewed supersession and justified manual checks keep their existing semantics.

The implementation workflow calls full project validation before handoff and reruns affected checks after changes. Targeted runs remain available during development. Validation-only still authorizes diagnostics/evidence, not product fixes. New task-plan content reopens Tasks; broader changes reopen the corresponding earlier gate. There is no test-authoring engine or promise that a file count proves coverage.

### Real skill evaluations

Use a dedicated adapter around Codex CLI `exec`, not Codex desktop chats or a simulated conversation. Local inspection found `codex-cli 0.159.2`; its help exposes `--json`, `--ephemeral`, `--ignore-user-config`, `--sandbox`, `--model`, `--cd` and stdin prompts. Official documentation confirms JSONL events and ephemeral runs: [non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) and [CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli). This confirms the intended interface, not authentication, model access or a successful agent evaluation. No model was invoked during Design.

The first adapter targets CLI 0.159.2. Preflight verifies its exact version and expected flags; support for another version requires reviewed adapter verification. Model ID and reasoning settings are required runtime inputs, recorded in evidence; no mutable default model or silent substitution. The runtime configuration is supplied as a reviewed JSON file, includes no credential values, and is copied into the protected evidence manifest with its digest. Model availability is checked during authorized execution and can produce unverified.

The adapter invokes an argv equivalent to:

```text
codex exec --json --ephemeral --ignore-user-config --sandbox workspace-write
  --model CONFIGURED_MODEL --cd DISPOSABLE_PROJECT -
```

Pass the scenario prompt through stdin. Approved configuration supplies reasoning effort using the CLI configuration argument. No bypass/auto-approval flags are added. The fixture explicitly points to the exact `skills/versat-sdd/SKILL.md` in a preserved package snapshot outside the writable project; its relative links resolve against that package. Assert observed reads and resulting behavior. This evaluates the actual skill instruction workflow with explicit loading; Marketplace installation/discovery is a separate distribution concern and not claimed by this test.

Six versioned cases form `sdd-critical`:

1. New intent: produce Proposal/Requirements and stop before Design, implementation or synthetic approval.
2. Authorized implementation with missing boundary/error tests: add meaningful coverage, run it and retained tests; independent seeded mutations must be caught by the resulting suite.
3. Adequate existing coverage: reuse the suite and its mappings without redundant test proliferation.
4. New happy path passes, retained duplicate-payment behavior fails: execute both and report failure without deleting/weaking the old assertions.
5. Previously passing evidence with mutated input: rerun the affected commands or report unavailable execution; do not rehash an old pass.
6. Validation-only defect: execute diagnostics and record the gap while the product/source diff remains unchanged.

Cases 2-6 use explicitly synthetic approved fixtures bound to their fixture plans, never approval evidence for real work. Each case is an independent invocation, avoiding a conversational test driver that fabricates a real person's approval. Run two fresh repetitions per case; all required assertions must pass in both. No best-of-N selection, automatic retry or model-as-judge is used. Command events, independent test replay, validator outcomes, source/dossier diffs and approval/digest changes drive grading. A well-formed final answer alone cannot prove execution. Missing critical event evidence is unverified; deterministic replay of canned events tests the adapter only.

A run is sequential with a 600-second per-case timeout, 7200-second suite deadline and 12 invocation maximum. Report usage when the CLI supplies it. These are execution limits, not a hard monetary ceiling; credential owners configure provider spend limits separately. Runtime configuration may lower limits; increases change reviewed configuration. An event usage threshold stops subsequent invocations; it cannot retroactively cap a completed provider request. Store prompt, fixture/source/runtime digests, model/CLI version, event stream, final response, diffs, independent replay results and per-assertion verdicts. Preserve failed attempts and aggregate variation across repetitions.

## Data, security and permissions

The runner executes repository code under caller permissions; it is not a sandbox. Validate safe paths and configuration before launch, reject symlink/special-file report destinations, use exclusive run directories, and never infer approval from executable configuration. Environment inheritance is restricted to operational variables needed for execution plus explicitly declared variable names. Do not print environment values or accept secrets embedded in argv/config. Tests do not acquire credentials or install packages.

Live evaluations run only in a dedicated disposable environment with no production data, home-directory mounts, ambient connectors or user hooks. The CLI's ignore-user-config option reduces configuration drift but is not credential isolation. Its tool sandbox and the outer execution environment must limit writable paths and network access; lack of a usable sandbox is a prerequisite failure. The trusted fixture snapshot is validated before exposing authentication. The model transport may access its configured service; project tools have no need for general external network access.

Credentialed CI uses an explicitly approved environment and scoped credentials, never a secret-bearing `pull_request_target` job or unreviewed fork code. Credentials are supplied only to the model transport invocation; child test/tool environments exclude credential variables. A fresh runtime has no unrelated authenticated plugins. CLI/OS sandbox restrictions do not by themselves prove every secret inaccessible: trusted code review, isolation and scoped credentials remain required. Reports are private artifacts with a 14-day CI retention default; only scrubbed synthetic evidence enters the repository. Log redaction supplements, but does not replace, avoiding secrets at source.

## Operations and CI

Keep `.github/workflows/validate.yml` and its baseline/archive behavior. Extend `scripts/validate/run.sh` to include all new offline execution and event-parser tests as well as all existing validator tests. This command remains offline after dependency setup. Consumer reference CI installs pinned prerequisites explicitly, checks out the exact selected Harness source and runs its full project wrapper without targeted selection.

Add a separate `.github/workflows/skill-evaluations.yml` for PR events, with a credential-free eligibility job and a protected-environment evaluation job. Live evaluations are required for non-draft PRs. An implementation draft may also request them through the explicit `harness-run-evals` label after authorization to publish an incomplete draft for validation. Subscribe to opened, synchronize, reopened, ready_for_review, converted_to_draft, labeled and unlabeled events; recompute eligibility against the current head, draft state and label. A planning draft without opt-in does not invoke a model or claim evaluated readiness. Removing opt-in cancels pending draft evaluations and prevents a stale eligible result from being reused.

Eligible same-repository PRs queue the protected job for a maintainer's environment approval of the exact head, including workflow code; the label itself grants no credential access or permission. Forks and otherwise untrusted sources produce an explicit non-passing eligibility result without credentials. They require reviewed adoption onto a trusted branch, not a privileged fallback. This draft route allows the first version of the workflow to obtain pre-archive evidence without declaring the implementation ready for delivery. After the workflow is available on the default branch, `workflow_dispatch` supports explicit exact-ref reruns.

Before exposing credentials or executing checked-out project code, verify the selected revision equals the expected full commit SHA and that the protected-environment review covered it. Bind PR runs to the event's current tested revision and record both head and tested revision where the platform uses a merge ref; stale-head runs cannot satisfy readiness. Pin CLI installation to 0.159.2 and action dependencies to reviewed immutable references during implementation. Never use `pull_request_target` or automatically move untrusted PR commands into a privileged context.

The deterministic PR job always runs and retains ready-for-review/archive behavior. A stable aggregate check, `skill-evaluations`, is required for delivery PRs under the documented platform setup. It has no credentials, runs even when prerequisite jobs fail or skip, and succeeds only with passing eligibility and observed protected evaluation results for the tested revision. Draft planning may remain without live evaluation but is explicitly labeled planning-only. A newer PR head requires a new evaluation and environment review. A dispatch for a different SHA cannot satisfy it. Missing auth/runtime, skipped required execution or failed cases produces a non-successful aggregate job. There is no `continue-on-error` or successful skip for required live evaluations. If platform rules or environment protections are not configured, report that gap rather than claim merge is mechanically blocked. Local package success does not imply this second check passed.

Design does not change remote rulesets or provision credentials. Implementation adds workflow files and reproducible configuration instructions; CHECK-008 requires actual observed CI evidence before this change is represented as fully verified. If environment access is unavailable, delivery stays unverified. No scheduled monitor or recurring paid run is created.

The delivery sequence is explicit: obtain local evidence; publish an explicitly authorized incomplete implementation draft; opt that draft into protected evaluations; observe CHECK-008 pre-closure evidence and complete its assessments; prepare documentary archival using the normal local delivery checks; then submit ready-for-review and observe final required CI on the resulting revision. The draft remains incomplete while its validation evidence is pending. Draft creation, labeling and environment approval remain separately authorized remote actions. No task is required to finish after merge, and no complete-delivery PR bypasses the existing archive preflight. Final post-submission CI remains a delivery control rather than a prerequisite for obtaining the earlier draft evidence. Changed assessed inputs require reruns; documentary relocation alone follows the existing snapshot exclusions.

Platform prerequisites must be verified before installing credentials: GitHub's availability of required environment reviewers depends on repository visibility and account plan, and an environment name alone does not enable review protection. If the required protection is unavailable, do not enable privileged PR evaluation; report the unmet prerequisite and revisit the CI integration through Design review if an alternative is needed. The workflow bootstrap and protection decisions follow GitHub's [manual workflow prerequisites](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow) and [environment protection and secret-access contract](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments).

## Migration, rollout and rollback

1. Implement the pure configuration contracts, explicit runner and reference consumer with deterministic tests. Preserve the existing package entry point and all historical artifacts.
2. Integrate authoring/reuse guidance and SDD result export without changing v3 schemas or historical compatibility. Update quickstart links and living architecture only with implemented behavior.
3. Add real evaluation adapter/cases and CI configuration; perform local live verification in an authorized isolated environment and observed exact-revision CI checks. Record actual model/runtime/access limits.
4. Consumers adopt the new artifacts through bootstrap/maintenance, reviewing custom commands, required-suite selection, conflicts and exact provider identity. No automatic deployment to consumer repositories.

Rollback restores reviewed wrapper/config/workflow changes and the prior exact package reference together, retaining tests and execution history. Do not remove regression tests, fabricate passes or roll back past a version able to read active SDD v3 artifacts. If a required new capability is disabled, readiness becomes incomplete until an approved alternative verifies its obligations. Publishing a release remains a separately authorized action.

## Alternatives considered

- More prose only: insufficient to observe execution reliably or evaluate agent behavior.
- Execute `method.procedure` inside the SDD validator: rejected because narrative is not an executable contract and validation must remain read-only.
- Universal framework discovery/generation: rejected for scope, false confidence and project-specific behavior; use explicit commands with a Python reference and structured generic reports.
- Automatically write all SDD assessments from exit codes: rejected because process success does not establish semantic acceptance.
- Require live LLM runs inside every local package check: rejected for offline usability and cost; keep a separately required delivery evaluation check.
- Dedicated workflow engine or remote evaluation service: unnecessary for bounded sequential cases; retain an adapter interface so another executor can be introduced through review.

## Validation plan

The metadata maps all 27 local acceptance scenarios and 23 retained obligations; no exclusions are proposed. CHECK-001 through CHECK-005 refer to proposed implementation entry points. CHECK-006 and CHECK-008 are explicit reviews with observable steps, not fabricated automated results. CHECK-007 preserves the complete existing deterministic suite. CHECK-004 is mandatory live agent evidence, not satisfied by unit-test mocks.

All checks bind the relevant provider code, tests, policies, templates, CI and guides. Generated evidence is excluded under `docs/validation/automated-test-execution`; external model/runtime configuration and provider state are recorded separately and trigger reruns when known to change. Temporary fixtures are generated from bound inputs. Runtime and environment availability must be reported in actual validation; no execution results are created at this stage.

Before delivery, verify assertion adequacy and suite selection through review, rerun after input changes, and follow normal documentary archive preparation with selected `--phase delivery --require-archive`. Preserve required CI results separately from local checks. A package inventory pass cannot establish live evaluation or remote protection.

## Architecture review

The Design follows ADR-0009's executor boundary and ADR-0011's package ownership, preserves ADR-0013 gates and ADR-0014 evidence semantics, and applies accepted ADR-0015 for explicit execution. Material risks are bounded but not hidden: repository commands need trust, model behavior varies, external dependencies are not captured by local snapshots, and remote required-check setup needs observation. Semantic review, isolated environments, exact source/runtime identity and non-passing unavailable outcomes address these within the approved scope.

No unresolved architectural choice blocks Gate 2. Credentials, selected model access and platform setup are execution prerequisites, not assumed completed infrastructure. Failure to obtain them blocks verification/delivery instead of silently weakening requirements.

## Planning review

Current status: superseded by the developer-selected supervised evaluation alternative and Proposal/Requirements R2. The historical approval below is retained for audit only; it does not authorize execution under the revised scope. Substantive design/task content and recorded results remain tied to the previous plan until the renewed upstream gates are approved.

The developer approved Design R1 and ADR-0015 in this Codex conversation on 2026-10-02: "Sim, aprovado. Avance para as tasks." The approved Design R1 digest was `49d00081bf0d8e6bdc6ee2f875821e7400dcbb24d31ee4d480c85ac9f61abe45`; its upstream Proposal/Requirements digest remains `87e3e8d41aeea6ee4bdbc7a036cce8a9b9aa636c059d9c50fcd4b503147f9afb`. This historical approval is preserved and is not reassigned to revised content.

Task dependency analysis found a cycle in R1: CHECK-008 evidence was needed before archive preparation, but the initial live workflow required non-draft status, whose preflight already requires archive preparation. Design R2 reopened Gate 2 only for the explicit implementation-draft evaluation route, its CI checks and the delivery sequence. Proposal/Requirements R1 and the architectural decision in ADR-0015 remain unchanged. No Tasks were created while that Design review was pending.

After presentation of Design R2 and clarification that archival precedes final PR review and merge, the developer replied in this Codex conversation on 2026-10-02: "Ok pode implementar." This approves Design R2 at digest `b5c643f91e45375fd15391db1556f64d4e6a3d1cf10dff6482b3eed375869691` and supplies implementation authorization. Tasks must still be presented and approved before implementation starts. No remote publication or repository settings change is inferred from this authorization.
