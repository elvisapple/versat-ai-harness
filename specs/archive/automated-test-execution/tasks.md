---
sdd_version: 3
change: automated-test-execution
tasks:
- id: TASK-001
  description: Revalidate the existing configuration and report contracts against the retained execution requirements.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-008
  status: completed
- id: TASK-002
  description: Revalidate full and targeted execution, bounded processes and truthful attempt reporting.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-008
  status: completed
- id: TASK-003
  description: Verify structured test reports and meaningful new and retained regression coverage.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-008
  status: completed
- id: TASK-004
  description: Verify current SDD result export and preserve historical evidence across replanning.
  requirements:
  - REQ-004
  - REQ-008
  status: completed
- id: TASK-005
  description: Finish consumer validation adoption and first-use integration without evaluation infrastructure
    prerequisites.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-005
  - REQ-007
  status: completed
- id: TASK-006
  description: Replace the unshipped autonomous evaluator with supervised fixtures and independent verification
    helpers.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-007
  description: Remove protected live-model CI and preserve complete deterministic CI and delivery enforcement.
  requirements:
  - REQ-003
  - REQ-005
  - REQ-006
  - REQ-008
  status: completed
- id: TASK-008
  description: Align canonical policy, workflows and living documentation with the supervised evaluation design.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-009
  description: Execute current deterministic checks, the six supervised scenarios and first-use verification.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-010
  description: Review local CI integration and complete all acceptance and retained-regression assessments.
  requirements:
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-008
  status: completed
review:
  revision: 2
  state: approved
  blockers: []
  upstream:
    proposal: 3278e689b32cbd1d5f51e8357f445a5d59ed782662cfec3de05985aada41da3e
    design: 244b88d4d9d59056d6956304d15bdea5c02f975a62877073a330151d488c7488
  approval:
    source: Developer response in this Codex conversation on 2026-10-03 after presentation of Tasks R2 and
      request to resume implementation.
    quote: aprovado
    revision: 2
    digest: 619ef3158d34627629a85e91c80bab1ff3898152a86e43a4bcea50309f350458
validation:
  plan_digest: 619ef3158d34627629a85e91c80bab1ff3898152a86e43a4bcea50309f350458
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/automated-test-execution/local-e7e8e56fa453409382e7ae0dad5c3aaf/CHECK-001.txt
    revision: input:dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955; attempt:local-e7e8e56fa453409382e7ae0dad5c3aaf
    input_digest_before: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    input_digest_after: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/automated-test-execution/local-e7e8e56fa453409382e7ae0dad5c3aaf/CHECK-002.txt
    revision: input:dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955; attempt:local-e7e8e56fa453409382e7ae0dad5c3aaf
    input_digest_before: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    input_digest_after: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/automated-test-execution/local-e7e8e56fa453409382e7ae0dad5c3aaf/CHECK-003.txt
    revision: input:dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955; attempt:local-e7e8e56fa453409382e7ae0dad5c3aaf
    input_digest_before: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    input_digest_after: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/automated-test-execution/review-r2.md
    revision: input:dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955; supervised:fc499f64e2d948a2a8b9b3427e924bd7;
      reviewed:2026-10-03T14:09:33.476474+00:00
    input_digest_before: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    input_digest_after: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; native session model/reasoning identity and
        usage not exposed
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/automated-test-execution/local-e7e8e56fa453409382e7ae0dad5c3aaf/CHECK-005.txt
    revision: input:dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955; attempt:local-e7e8e56fa453409382e7ae0dad5c3aaf
    input_digest_before: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    input_digest_after: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-006
    result: pass
    evidence: docs/validation/automated-test-execution/review-r2.md
    revision: input:dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955; supervised:fc499f64e2d948a2a8b9b3427e924bd7;
      reviewed:2026-10-03T14:09:33.476474+00:00
    input_digest_before: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    input_digest_after: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; native session model/reasoning identity and
        usage not exposed
      observed: true
  - check: CHECK-007
    result: pass
    evidence: docs/validation/automated-test-execution/local-e7e8e56fa453409382e7ae0dad5c3aaf/CHECK-007.txt
    revision: input:dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955; attempt:local-e7e8e56fa453409382e7ae0dad5c3aaf
    input_digest_before: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    input_digest_after: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4
      observed: true
  - check: CHECK-008
    result: pass
    evidence: docs/validation/automated-test-execution/review-r2.md
    revision: input:dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955; supervised:fc499f64e2d948a2a8b9b3427e924bd7;
      reviewed:2026-10-03T14:09:33.476474+00:00
    input_digest_before: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    input_digest_after: dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; native session model/reasoning identity and
        usage not exposed
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Clean first-use exact-commit provider and base-composed Python consumer executed the documented
      wrapper with four observed passing tests; runner tests independently verify full required selection.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Custom-command first-use execution preserved configuration bytes and passed; rollback restored
      the original passing command. Consumer tests reject unresolved provider pins rather than guessing integration.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Invalid configuration and empty/all-skipped selection are rejected by real runner tests; the
      first-use missing interpreter reports exit 2 without installation or overall success.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: The missing-coverage native agent added meaningful state, error and boundary assertions. Seven
      tests passed; independent duplicate, zero-boundary and empty-key mutants each failed their intended assertions.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: The adequate-reuse native agent preserved all four original tests and source bytes, mapped
      them and executed them. Independent replay passed and three seeded defects failed without redundant tests.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Consumer tests show a duplicate defect escapes an insufficient historical happy path but fails
      after retained coverage is added. Canonical tests reject unapproved exclusions and require reasons/outcomes
      for manual and replacement dispositions.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Native retained-failure validation and independent replay execute four tests including the
      failing retained duplicate assertion. The local reference CI command also executes new passing and separate
      retained failing suites and returns failure.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-005
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Runner and SDD export tests label targeted scope and reject its use as full readiness evidence.
      Reviewed workflow commands always select the complete required suite set.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Real bounded subprocess tests retain reports for timeout, interruption with descendant termination,
      nonzero exit, zero/all-skipped tests and unavailable execution; attempt directories are exclusive, preserving
      earlier outcomes.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Configuration inspection and SDD validators do not execute procedure prose. The native new-intent
      case stopped at Proposal/Requirements approval, and validation-only cases preserved source, tests and
      plan identity.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Actual runner reports and fragments contain command arguments, environment, counts, output
      and stable before/after digests. Current R2 results bind the approved Tasks digest; the runner leaves
      dossier bookkeeping to the coordinator.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: SDD execution tests withhold fresh fragments after source or plan mutation and retain old
      attempts. Native stale-evidence validation reran the current inputs while preserving the earlier stale
      report; independent replay verified current behavior.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Manual/export rejection tests preserve method boundaries; missing prerequisite first-use execution
      remains unavailable. Synthetic missing/unverified supervised delivery records stay non-passing despite
      a declared automated pass.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 4
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: The archive relocation regression preserves evidence resolution and input identity. Export
      tests confirm no approval, assessment, finding or task status changes; local reports make no merge/deployment
      claim.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    - CHECK-008
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: The actual reference CI step, executed locally with controlled consumer fixtures, runs both
      new and retained suites and exposes the failing retained suite with exit 1. This verifies command integration,
      not a remote GitHub run.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: pass
    checks:
    - CHECK-005
    - CHECK-007
    - CHECK-008
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Actual workflow shell branches preserve baseline arguments and add the archive guard for ready/push
      behavior; missing baseline and nonzero validation stop the job. All 131 existing validator regressions
      pass in the full package suite.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 3
    result: pass
    checks:
    - CHECK-005
    - CHECK-008
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Synthetic delivery checks show missing and unverified required supervised evidence remain
      gaps alongside a declared passing automated result. Canonical policy requires both evidence types; the
      privileged model workflow was removed.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Six fresh native agents received only their saved scenario prompt and fixture with the versioned
      Skill, using fork_turns=none. Inputs, artifacts, available messages and unknown model/usage fields are
      retained; shared permissions are explicit.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Coordinator inspections verify the first approval gate, meaningful missing coverage, adequate
      reuse and truthful retained failure. Independent replays and three separate mutation copies per coverage
      case substantiate the verdicts beyond native narratives.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Native stale-evidence and validation-only artifacts are compared to pre-dispatch source/tests,
      controls and approved plan snapshots. Current replay and original command reports verify rerunning and
      failure reporting without unauthorized code fixes.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 4
    result: pass
    checks:
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: One invocation per case was retained under monitored 600-second case and 3600-second suite
      bounds, without retries. The guide requires unavailable/over-budget results to stay unverified; helper
      tests exercise actual bounded replay and missing observations. Runtime outage was not forced; model/usage
      telemetry remains unknown.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Clean first-use applied the optional Python validation artifact on base, resolved canonical
      Standards and an exact synthetic provider commit, then ran the usable wrapper. Template placeholders
      are authoring inputs, not claimed execution.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Provider tests reject unresolved or changed identities; maintenance guidance requires reviewed
      conflict handling and exact pins. Actual custom-command preservation and rollback succeeded without rewriting
      historical dossiers.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    - CHECK-004
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: First-use observed wrapper success, retained regression failure, unavailable prerequisite
      and rollback. The six native scenarios use session collaboration without a dedicated API key; their evidence
      remains separate from deterministic CI.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-005
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Complete current validation passes 131 existing governance/SDD regressions and 48 execution/consumer/CI/helper
      tests, including real success, failure, interruption, unsafe inputs and the venv interpreter regression.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Runner/SDD tests reject escaping paths, overlapping unsafe outputs and narrative execution.
      Subprocess argument data is not shell-expanded, and execution preserves caller permissions without claiming
      isolation.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 3
    result: pass
    checks:
    - CHECK-006
    - CHECK-007
    - CHECK-008
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: The approved R2/R3/R2 chain governs the canonical Testing Standard revision. Existing gate,
      compatibility and freshness tests pass; exact adoption and preserved history remain explicit. Supervised
      local review does not waive automated application evaluations.
  - obligation:
      regression:
        impact: 1
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Canonical coverage tests require each success/error/boundary scenario to be mapped; native
      missing-coverage adds actual missing assertions and independent mutants expose defects.
  - obligation:
      regression:
        impact: 1
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Canonical reuse tests and the native adequate-reuse case retain the same four maintained tests
      while mapping multiple obligations, with no duplicate catalog or test quota.
  - obligation:
      regression:
        impact: 1
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Canonical and consumer integration tests reject unapproved exclusions and require a scope
      reason for inapplicability; required current obligations remain assessed.
  - obligation:
      regression:
        impact: 2
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Consumer tests and the actual local reference CI step execute a passing new test together
      with failed retained duplicate/regression checks; overall failure is preserved.
  - obligation:
      regression:
        impact: 2
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Adequate existing tests remain in the consumer tests directory and are reused unchanged in
      the native case; independent replay and mutation verification confirm retained behavior.
  - obligation:
      regression:
        impact: 2
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Approved regression mapping and explicit required_suites preserve selection rationale; CI
      command tests run the full set even after another required suite fails.
  - obligation:
      regression:
        impact: 2
        scenario: 4
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Canonical manual-check tests require a reason and observed outcome, while unverified supervised
      delivery fixtures remain non-passing. Review methods are not exported as automated executions.
  - obligation:
      regression:
        impact: 2
        scenario: 5
    result: pass
    checks:
    - CHECK-003
    - CHECK-005
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Canonical supersession tests require local replacement and approval. The explicit retirement
      map defers only unshipped CLI/protected-CI responsibilities and retains failing-regression assertions.
  - obligation:
      regression:
        impact: 3
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: SDD evidence tests and current native stale-evidence artifacts show source changes invalidate
      prior results with unchanged Tasks planning; only actual current execution supplies new evidence.
  - obligation:
      regression:
        impact: 3
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Gate and evidence regressions reject modified requirements/mappings and stale plan digests.
      Historical R1 results remain in their original snapshots rather than being rebound to R2.
  - obligation:
      regression:
        impact: 3
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Actual reports identify command, environment and input snapshots. Validator warnings distinguish
      declared references from authenticated execution; supervised observations are locally reviewed, not remote
      attestations.
  - obligation:
      regression:
        impact: 3
        scenario: 4
    result: pass
    checks:
    - CHECK-002
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Archive relocation tests keep report references and freshness intact while unchanged history
      remains inventory-only; local delivery does not establish merge or deployment.
  - obligation:
      regression:
        impact: 4
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: The maintained validator suite rejects duplicate, dangling, malformed and ambiguous references
      with source-specific findings; the execution integration preserves those validators.
  - obligation:
      regression:
        impact: 4
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Full deterministic regressions plus retained-failure native evidence demonstrate failed, missing,
      unverified and stale records block delivery rather than passing structural readiness.
  - obligation:
      regression:
        impact: 4
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Partial planning regressions and the actual new-intent agent allow Proposal/Requirements without
      premature Design, Tasks or execution results, and stop for the first human gate.
  - obligation:
      regression:
        impact: 4
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Structural output preserves its semantic/authenticity limitation; inadequate test coverage
      can pass execution in the consumer fixture until meaningful assertions are added. Coordinator mutation
      review supplies the separate assessment.
  - obligation:
      regression:
        impact: 5
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Legacy and historical archive compatibility regressions pass with preserved bytes; the R1
      task/evidence snapshot remains readable and unchanged under the revised approved plan.
  - obligation:
      regression:
        impact: 5
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Missing historical coverage is exposed by the consumer duplicate mutant and addressed in current
      native implementation. Synthetic fixture approvals are labeled and never portrayed as real retrospective
      approvals.
  - obligation:
      regression:
        impact: 5
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: All 131 maintained validator tests pass, retaining positive and negative coverage for references,
      regression evidence, freshness, gate sequencing and archives alongside new execution tests.
  - obligation:
      regression:
        impact: 5
        scenario: 4
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Reviewed guides retain one public versat-sdd Skill and four dossier files. Actual native scenarios
      follow planning, implementation and validation routes, preserve failures and report the required next
      authorization.
  - obligation:
      regression:
        impact: 5
        scenario: 5
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    - CHECK-007
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Clean consumer setup resolves base composition and an exact synthetic provider commit. Guides
      require a reviewed real release pin for adoption; no consumer or Marketplace release is updated automatically.
  - obligation:
      regression:
        impact: 6
        scenario: 0
    result: pass
    checks:
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: All six versioned critical scenario intents were exercised through fresh native agents with
      original artifacts and coordinator replay. Narrative-only and old scripted walkthrough evidence were
      not used as substitutes.
  - obligation:
      regression:
        impact: 7
        scenario: 0
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/automated-test-execution/review-r2.md
    explanation: Optional validation artifacts extend base; clean first-use exercised usable configuration,
      custom commands and rollback with an exact provider pin. Scaffolding and adoption remain separate from
      observed execution.
  findings:
  - id: FIND-001
    source:
      local:
        requirement: REQ-001
        scenario: 1
    category: contradicts
    state: resolved
    evidence: docs/validation/automated-test-execution/development-failure-r2.md
    description: Independent replay exposed a venv interpreter symlink being resolved before launch, bypassing
      prepared dependencies; helper output overlap also failed for macOS temporary path aliases.
    tasks:
    - TASK-002
    - TASK-006
    checks:
    - CHECK-001
    - CHECK-007
    resolution: Preserve the interpreter invocation path while recording the resolved binary; canonicalize
      both replay paths before overlap comparison. Real-venv and overlap regressions plus the full 179-test
      suite pass; historical failure observations remain retained.
closure: prepared
---

# Tasks

This revision implements approved Proposal/Requirements R2, Design R3 and the accepted revision of ADR-0015. Reuse the existing explicit runner and consumer integration; reconcile the unshipped evaluator and its CI assets with the supervised approach. The ten task IDs retain their logical responsibility, with revised deliverables and completion checks. All R2 tasks start pending because their current verification or reconciliation remains to be performed. This does not erase completed R1 work or require rebuilding adequate code.

## Existing implementation and evidence

The [superseded Tasks R1 snapshot](../../../docs/validation/automated-test-execution/tasks-r1-superseded.md) preserves exact prior metadata, seven results, progress and approval history. TASK-001 through TASK-004 were locally implemented and tested; TASK-006/007 implemented the now-deferred CLI/CI approach. TASK-005/008 had partial integration and documentation. TASK-009/010 lacked live evaluation and protected CI evidence. Their old credential/protected-environment dependencies are replaced by the current Design, not counted as satisfied.

Existing test files, logs, CLI probe and all prior attempts remain historical evidence. They are not active R2 results, and their input hashes or outcomes must not be rewritten. The new `validation` record is empty until checks actually run against the revised plan. Current implementation readiness requires R2 approval; a planning pass is not execution or delivery readiness.

## Ordered work

- [x] TASK-001 — Revalidate the existing configuration and report contracts against the retained execution requirements.

  Reuse `schemas/validation.schema.yaml`, `schemas/validation-result.schema.yaml` and `validators/testing/validate.py`. Inspect their current implementation against nonempty unique required suites, argv-only commands, supported adapters, safe paths/scopes and consistent counts. Correct only actual gaps within the approved contract; do not redesign the retained configuration interface.

  Completion: CHECK-001 configuration cases pass for valid inputs and actionable rejection of malformed/unsafe data. Test suites cannot pass through the check-only exit-code adapter. Configuration inspection and SDD validation do not launch project commands. Record current focused results and include the coverage in final CHECK-007.

- [x] TASK-002 — Revalidate full and targeted execution, bounded processes and truthful attempt reporting.

  Reuse `scripts/testing/run.py` and its helpers. Verify all-required versus targeted selection, restricted environment, explicit substitutions, exclusive output directories, retained attempts, bounded logs and timeout/interruption behavior. Preserve full-suite failure aggregation and no automatic retries or dependency installation.

  Completion: CHECK-001 executes real harmless commands and detects required-suite failure, zero tests, missing tools, source/configuration mutation, unsafe outputs and interruption. Targeted success retains limited scope and no readiness claim. Record observed macOS/Python 3.11 behavior; Linux CI is a target, not an unobserved local completion claim.

- [x] TASK-003 — Verify structured test reports and meaningful new and retained regression coverage.

  Reuse unittest/JSON-v1 adapters and consumer fixtures. Verify actual executed/skipped/failure/error counts, empty/all-skipped rejection and new behavior plus retained duplicate-payment/error/boundary coverage. Preserve meaningful assertions, adequate reuse, missing historical coverage and reviewed supersession cases; add tests only for actual gaps.

  Completion: CHECK-001/CHECK-003 pass. Independent seeded duplicate-payment and boundary defects fail the intended assertions while the good fixture passes. A new passing happy path cannot hide an old failing regression. Custom project commands and required suites survive adoption. Fixture tests are labeled deterministic integration evidence, not native agent execution.

- [x] TASK-004 — Verify current SDD result export and preserve historical evidence across replanning.

  Verify `--change`/`--check` export against current approvals, automated method, full scope, local/CI context and provider identity. Keep before/after plan/input snapshots, separate attempts and archive-safe outputs. Ensure the runner does not write approvals, task completion, findings or assessments. Retain previous results only in historical evidence and populate R2 results from actual current execution.

  Completion: CHECK-002 passes for real success/failure/unavailable outcomes, stale and changing inputs, targeted/manual export rejection and archive relocation. No fixture dossier bytes change as a side effect of export. Current fragments bind R2 when incorporated by the coordinator; old results remain resolvable and unchanged.

- [x] TASK-005 — Finish consumer validation adoption and first-use integration without evaluation infrastructure prerequisites.

  Complete `project-templates/artifacts/validation/`, bootstrap/maintenance integration and the project validation guide using the existing assets. Preserve base/profile composition, custom commands and reviewed exact Harness identity. Clearly separate the consumer test command from supervised Harness Skill evaluation; remove any suggestion that test authoring or regression execution requires an API key or model CI service.

  Completion: CHECK-003 creates a fresh supported consumer, runs its full documented wrapper, preserves custom commands and verifies rollback. Configuration identifies actual required suites rather than treating scaffolding as execution. CHECK-006 later confirms the first-use instructions against observed outputs and exact-version/conflict handling.

- [x] TASK-006 — Replace the unshipped autonomous evaluator with supervised fixtures and independent verification helpers.

  Move reusable fixture preparation from `scripts/eval/fixtures.py` to `tests/skills/fixtures.py`. Extract applicable diff/integrity/replay behavior into `tests/skills/verification.py`, without model transport, delegation, credential or transcript-parser dependencies. Preserve all six case intents and clearly synthetic approval provenance. Document the attempt-record template and coordinator procedure in `tests/skills/README.md` and the evaluation guide.

  Remove `scripts/eval/run.py`, `scripts/eval/codex.py` and `tests/skills/runtime.schema.json` after reusable behavior is migrated; the old fixture module must have no remaining active imports. Replace `test_eval.py` with `test_supervised.py`, retaining meaningful fixture validity, stale-evidence setup, plan/source integrity and controlled replay assertions. Document each retired CLI/parser/authentication/sandbox-only test and its deferred responsibility before removal. Do not leave an optional unverified CLI path.

  Completion: all six fixtures are reproducible; helpers report factual diffs and bounded command outcomes, never semantic approval or proof from narrative alone. Deterministic tests detect seeded defects and protected plan/source changes, and preserve unavailable/partial outcomes. CHECK-007 covers these helpers without spawning models. Actual Skill behavior remains for TASK-009.

- [x] TASK-007 — Remove protected live-model CI and preserve complete deterministic CI and delivery enforcement.

  Remove the unshipped `.github/workflows/skill-evaluations.yml` and `scripts/eval/ci.py`, together with active setup references for dedicated evaluation secrets, environment reviewers, draft opt-in labels and live aggregate jobs. Keep `.github/workflows/validate.yml`, the consumer workflow and the complete package command. Preserve baseline/archive enforcement and the project's existing required automated suites.

  Reconcile `tests/execution/test_ci.py`: retain baseline/archive branches; cover missing baseline, complete suite selection and failure propagation through real local command fixtures. Verify synthetic delivery stays non-passing when required supervised evidence is missing/unverified despite passing deterministic results. Map retirement only of deferred live eligibility, environment/label, dispatch and aggregate tests; preserve historical evidence references.

  Completion: CHECK-005 passes and CHECK-007 runs the full remaining suite. A failing retained regression propagates through the consumer CI command. No privileged model CI job or silently successful substitute is introduced. CHECK-008 later reviews the integration locally; no remote settings or observed CI pass is inferred.

- [x] TASK-008 — Align canonical policy, workflows and living documentation with the supervised evaluation design.

  Implement the approved canonical Testing Standard distinction: required automated suites run in CI; supervised Skill checks require separately assessed local evidence and cannot waive automated application evals. Replace the unreleased isolated/credentialed evaluation clause. Keep policy in Standards and have SDD workflows/Skills resolve it through the index.

  Align implementation/validation instructions, `docs/guides/project-validation.md`, `docs/guides/skill-evaluations.md`, architecture, template guides, READMEs and CHANGELOG with the actual revised implementation. Document fresh subagent context, shared permissions, observable evidence, independent replay, unavailable outcomes, bounds and the local-evidence/archive/submission/final-CI sequence. Maintain exact pins and existing historical artifacts.

  Completion: CHECK-006 finds coherent reproducible first-use instructions, valid links, accurate limits and canonical policy routing; CHECK-008 finds an accurate CI/delivery description. Active operational guidance has no dedicated-key/protected-evaluation prerequisite. Historical records remain explicitly historical. No release or Marketplace update is claimed.

- [x] TASK-009 — Execute current deterministic checks, the six supervised scenarios and first-use verification.

  After the revised implementation and guides are stable, execute CHECK-001/002/003/005/007 with current R2 bindings and complete CHECK-004 plus CHECK-006. For CHECK-004, use the native collaboration interface with fresh context and only the scenario prompt/fixture/Skill/allowed work. Run the six approved cases sequentially, one fresh invocation each: six planned invocations, monitored 600-second case and 3600-second suite limits including independent verification. Inherit available session model/reasoning settings and record unknowns; require no new API key.

  The coordinator inspects artifacts, original structured runner reports and available observations, independently re-executes produced tests and seeds defects in separate copies. Keep provider snapshots separate from expected fixture mutations. Preserve all attempts, partial observations and limits under the approved evidence subtree. A final narrative, code review or old CLI probe cannot satisfy behavioral acceptance. No automatic retries or best-of-N selection; authorized fixes trigger separate bounded reruns of affected cases with old outcomes retained.

  Completion: the seven checks have current adequate results, including all six required supervised case verdicts and first-use review. Missing runtime or critical observations leave the affected task/check incomplete and unverified; known assertion failures remain failed. CHECK-006 reuses the actual CHECK-004 attempts rather than launching another set. Any changes to provider inputs require affected reruns before readiness.

- [x] TASK-010 — Review local CI integration and complete all acceptance and retained-regression assessments.

  Execute CHECK-008 as the approved local integration review using current CHECK-005/007 evidence, the actual deterministic workflow commands and synthetic missing-supervised-evidence delivery cases. Assess all 27 local acceptance scenarios and 23 retained obligations using current artifacts, command results and the eight Design checks. Review the additional policy supersession through CHECK-004/006/008. Record stable findings and resolve them only with supporting evidence; reuse authorized correction tasks without weakening scope.

  Completion: all eight required checks have current passing evidence, every mapped obligation has an adequate assessment, and no acceptance finding remains unresolved. Verify test-retirement mappings preserve retained obligations and old evidence remains readable. Mark this task complete only after those conditions hold, then run selected delivery eligibility with all task statuses reconciled. Archive preflight, final remote CI and merge are subsequent lifecycle controls, not circular prerequisites for completing this task.

## Dependencies

| Task | Prerequisites | Main verification |
| --- | --- | --- |
| TASK-001 | Current Tasks R2 approval and implementation authority | CHECK-001, CHECK-007 |
| TASK-002 | TASK-001 | CHECK-001 |
| TASK-003 | TASK-002 | CHECK-001, CHECK-003 |
| TASK-004 | TASK-002 | CHECK-002 |
| TASK-005 | TASK-003, TASK-004 | CHECK-003; first-use review in TASK-009 |
| TASK-006 | TASK-003, TASK-004 | Helper tests in CHECK-007; actual scenarios in TASK-009 |
| TASK-007 | TASK-005, TASK-006 | CHECK-005, CHECK-007 |
| TASK-008 | TASK-005, TASK-006, TASK-007 | Documentation inspection; CHECK-006/008 in TASK-009/010 |
| TASK-009 | TASK-001 through TASK-008; usable native collaboration and prepared local test environment | CHECK-001 through CHECK-007 |
| TASK-010 | TASK-009 | CHECK-008 and all scenario/regression assessments |

Tasks represent logical deliverables, not mandatory separate commits. Focused tests run with each task; TASK-009 consolidates current full evidence after source stabilizes. Consumer/helper/CI/documentation tasks finish their artifacts and focused verification before TASK-009 provides integrated first-use/behavioral review, so those later reviews do not create a dependency cycle. A later review finding reopens the affected task within its approved scope and requires reruns.

Native subagents are used for the explicitly designed scenario work in TASK-009. This plan does not delegate implementation to additional agents or require parallel execution. Six scenarios are this reviewed evaluation plan, not a permanent fixed test quota for all changes.

## Prerequisites and risk handling

- No unresolved planning decision blocks Tasks R2. Proposal/Requirements R2, Design R3 and revised ADR-0015 are approved; the current Tasks gate is pending.
- Reuse existing implementation and installed validation dependencies. Native scenario availability, adequate observable evidence and supported local process execution are execution prerequisites; unavailable prerequisites block affected verification rather than turn it into a pass.
- Fresh contexts and temporary directories do not isolate permissions. Use synthetic data, inspect actual effects and generated commands, and record shared-permission/telemetry limits. Do not read credentials, call external connectors or publish remotely as part of a case.
- Preserve monitored budgets and every actual outcome. Material changes to scenarios, grading, runtime selection, scope or limits reopen the appropriate gate; routine in-scope fixes and affected reruns retain their existing authority.
- The required deterministic suite remains complete for retained behavior. A test may be retired only where the accepted Design explicitly defers its unshipped transport/CI responsibility, with a recorded mapping. Test count alone does not establish coverage.
- Previous local implementation authority is retained, but execution waits for current Tasks R2 approval. Remote publication, rulesets, secrets, release and consumer rollout remain separately scoped actions. No intermediate protected-evaluation draft, scheduled run or post-merge task is required.

## Planning review

Current approval: the developer replied "aprovado" on 2026-10-03 after presentation of Tasks R2 and the request to resume implementation. This binds digest `619ef3158d34627629a85e91c80bab1ff3898152a86e43a4bcea50309f350458` and authorizes the current local implementation and validation.

Historical Tasks R1 approval: the developer replied "sim", binding digest `e092fe22186c0bdbd9ffc49bad5d8e9cc2771ab4d1332d888cd5e328134c84eb`, under Proposal R1 and Design R2. Historical implementation followed "Ok pode implementar.". The superseded snapshot preserves that approval, actual progress and results.

The developer selected the supervised alternative, approved Proposal/Requirements R2 with "aprovado", and approved Design R3 plus revised ADR-0015 with "sim". Tasks R2 now binds those approved upstream digests and awaits Gate 3. Writing this plan neither approves it nor completes its tasks. Acceptance of this current revision unlocks execution under the retained explicit implementation request; the developer may also confirm implementation in the same reply.

## Progress

2026-10-03: all ten Tasks R2 deliverables are complete. All eight planned checks have current passing evidence, including 179 deterministic tests, six supervised native scenarios with independent replay, clean first-use and local CI integration review. All 27 local and 23 retained obligations have individual passing assessments; no acceptance finding remains open. Earlier planning-time pending statements describe the initial R2 baseline, not current status. Historical R1 work and unsuccessful development attempts remain preserved.

## Validation evidence

Current evidence and semantic review: [review-r2.md](../../../docs/validation/automated-test-execution/review-r2.md). The eight check results bind the approved R2 Tasks digest and unchanged actual input snapshots. CHECK-004/006/008 are local reviews; no remote CI execution is claimed. Historical results remain in their original snapshots. Selected local delivery eligibility is recorded in [delivery-r2.json](../../../docs/validation/automated-test-execution/delivery-r2.json).

## Delivery

Closure stays `active`. After task completion and current evidence/assessments, run selected `--phase delivery`. Prepare the unique dossier under archive storage in this same branch, reconcile references, set `closure: prepared` and run `--phase delivery --require-archive` before authorized submission or marking a draft ready. Final required automated CI and human PR review follow on the submitted revision before merge. Observe their actual outcomes separately; archive location and local evidence do not establish them.

Inspect actual required-check settings before authorized publication. If an unexpected remote rule still requires the deferred model job, report the mismatch and prepare its separately authorized resolution without bypassing protection. No task depends on a post-merge action or on provisioning evaluation credentials.

2026-10-03 archive preparation: the developer explicitly requested archival, PR publication and remote CI. The unique dossier was moved to `specs/archive/automated-test-execution/` in the same implementation branch and closure is now `prepared`. All earlier approval records, stage digests and evidence remain intact. Archive preflight and final required CI are observed separately; no merge is claimed.
