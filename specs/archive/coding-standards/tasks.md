---
sdd_version: 3
change: coding-standards
tasks:
- id: TASK-001
  description: Define the index-resolved coding and changelog policy and PR review guidance.
  requirements:
  - REQ-001
  - REQ-002
  status: completed
- id: TASK-002
  description: Implement deterministic Git comparison and Unreleased changelog validation.
  requirements:
  - REQ-002
  - REQ-003
  status: completed
- id: TASK-003
  description: Integrate pinned Ruff and Git comparison into the Harness local command and CI.
  requirements:
  - REQ-003
  status: completed
- id: TASK-004
  description: Integrate full quality validation in the exact-provider Python consumer reference and
    document adoption and rollback.
  requirements:
  - REQ-003
  - REQ-004
  status: completed
- id: TASK-005
  description: Execute the approved checks and record current acceptance and regression evidence.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  status: completed
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 125767fca0766318d669f4e5a51e20689bb8687fa443a4077638b85524d38ab1
    design: c2d456db6f44c604141519558f7be127564ffac2c20a16a45c94721cc4045bcc
  approval:
    source: Developer reply in the Codex chat for issue
    quote: Ok, aprovado
    revision: 1
    digest: 52599c51ba2a433baa57b08bdc5a1c027683eff74f560ebdfeb360cfb8a364f6
validation:
  plan_digest: 52599c51ba2a433baa57b08bdc5a1c027683eff74f560ebdfeb360cfb8a364f6
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/coding-standards/check-001.md
    revision: Working tree over c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa, declared input snapshot
      e5205b9b653a2678e54a66d6d40afd87387e7b32dfde318b91febff14058829c
    input_digest_before: e5205b9b653a2678e54a66d6d40afd87387e7b32dfde318b91febff14058829c
    input_digest_after: e5205b9b653a2678e54a66d6d40afd87387e7b32dfde318b91febff14058829c
    context:
      execution: local
      environment: macOS 27.2.1 arm64, CPython 3.11.14, Git 2.54.0, Ruff 0.14.14
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/coding-standards/check-002.md
    revision: Working tree over c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa, declared input snapshot
      50c5574d71030cf6e88e098e9ce6df7d3ec23e697802442a9079edd3c3126a0e
    input_digest_before: 50c5574d71030cf6e88e098e9ce6df7d3ec23e697802442a9079edd3c3126a0e
    input_digest_after: 50c5574d71030cf6e88e098e9ce6df7d3ec23e697802442a9079edd3c3126a0e
    context:
      execution: local
      environment: macOS 27.2.1 arm64, CPython 3.11.14, Git 2.54.0, Ruff 0.14.14
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/coding-standards/check-003.md
    revision: Working tree over c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa, declared input snapshot
      5d8438b5eb73251dc4a519467cb71207fa6881039fe8928b493fa6e87a5c1146
    input_digest_before: 5d8438b5eb73251dc4a519467cb71207fa6881039fe8928b493fa6e87a5c1146
    input_digest_after: 5d8438b5eb73251dc4a519467cb71207fa6881039fe8928b493fa6e87a5c1146
    context:
      execution: local
      environment: macOS 27.2.1 arm64, CPython 3.11.14, Git 2.54.0, Ruff 0.14.14
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/coding-standards/check-004.md
    revision: Working tree over c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa, declared input snapshot
      5816e11b253908b8528e5f2a243ee32c1cb6f21725d473166ab5f2de24d6dcfe
    input_digest_before: 5816e11b253908b8528e5f2a243ee32c1cb6f21725d473166ab5f2de24d6dcfe
    input_digest_after: 5816e11b253908b8528e5f2a243ee32c1cb6f21725d473166ab5f2de24d6dcfe
    context:
      execution: local
      environment: macOS 27.2.1 arm64, CPython 3.11.14, Git 2.54.0, Ruff 0.14.14
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/coding-standards/check-005.md
    revision: Working tree over c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa, declared input snapshot
      3a308196fd4e8c6930149a1b2ba82cd5a208dbabf910b1a6984c8c217c8c17dd
    input_digest_before: 3a308196fd4e8c6930149a1b2ba82cd5a208dbabf910b1a6984c8c217c8c17dd
    input_digest_after: 3a308196fd4e8c6930149a1b2ba82cd5a208dbabf910b1a6984c8c217c8c17dd
    context:
      execution: local
      environment: macOS 27.2.1 arm64, CPython 3.11.14, Git 2.54.0, Ruff 0.14.14
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/coding-standards/check-001.md
    explanation: Exact provider verification resolved the canonical coding guidance for software,
      hybrid and library contexts and selected Python rules only for the Python examples.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/coding-standards/check-001.md
    explanation: Reviewed a mixed persistence and business policy case and a substitution that violates
      the error contract. The Standard supplies criteria for both and for extension, interface size
      and dependency direction.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/coding-standards/check-001.md
    explanation: The resolved guidance and PR prompts distinguish configured Ruff checks from semantic
      judgments and the accuracy of release notes.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/coding-standards/check-002.md
    explanation: Git fixtures failed for missing, duplicate, moved and historical-only notes and for
      a mixed change with an in-scope workflow path.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-003
    evidence: docs/validation/coding-standards/check-002.md
    explanation: A valid new entry passed in a real comparison. The note for this change describes
      the impact and identifies both the Harness and reference consumer.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-003
    evidence: docs/validation/coding-standards/check-002.md
    explanation: The planning-only comparison reported its exemption. The Standard and guide identify
      the rationale and PR review asks for the applicable reason.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/coding-standards/check-004.md
    explanation: Actual Ruff reported F401 and formatting violations without writing files. The local
      command and the event path use the same pinned checker.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/coding-standards/check-004.md
    explanation: The full Harness run passed and the consumer still executed suites after a changelog
      failure. A seeded retained failure made consumer CI validation fail independently of passing
      quality.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/coding-standards/check-004.md
    explanation: Git fixtures rejected missing history with a fetch suggestion, and a clean interpreter
      without Ruff reported the pinned install prerequisite.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 4
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/coding-standards/check-004.md
    explanation: The structural workflow retained its selection and archive logic. CI step and SDD
      tests exercised draft/ready/main behavior and missing supervised evidence locally.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    - CHECK-005
    evidence: docs/validation/coding-standards/check-004.md
    explanation: The documented exact-provider Python wrapper produced a full passing run and a failure
      with an actionable missing-note message in a fresh disposable project.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-005
    evidence: docs/validation/coding-standards/check-005.md
    explanation: The optional assets composed over base, the custom suite remained byte-identical
      and restoring the previous wrapper ran the original suite. The guide covers rollback of the
      complete integration.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    - CHECK-005
    evidence: docs/validation/coding-standards/check-004.md
    explanation: The targeted path reported limited scope. An unresolved provider did not pass verification
      and the adopted wrapper ran full validation for the simulated CI push.
  - obligation:
      regression:
        impact: 1
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/coding-standards/check-004.md
    explanation: Maintained consumer CI coverage ran a new suite and a seeded retained regression,
      propagated failure and exposed both outcomes.
  - obligation:
      regression:
        impact: 1
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/coding-standards/check-004.md
    explanation: Structural workflow tests ran both archive and inventory branches, preserved failure
      propagation and rejected a missing baseline.
  - obligation:
      regression:
        impact: 1
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/coding-standards/check-004.md
    explanation: The delivery validator still blocked missing or unverified supervised evidence. Deterministic
      quality did not change its disposition.
  - obligation:
      regression:
        impact: 2
        scenario: 1
    result: pass
    checks:
    - CHECK-005
    evidence: docs/validation/coding-standards/check-005.md
    explanation: Adoption walkthrough used composed Python assets and the documented wrapper with
      configured prerequisites and observable changes in result.
  - obligation:
      regression:
        impact: 2
        scenario: 2
    result: pass
    checks:
    - CHECK-005
    evidence: docs/validation/coding-standards/check-005.md
    explanation: The exact clean provider and selected Standard digests were verified. The custom
      suite and reviewed rollback procedure remained available.
  - obligation:
      regression:
        impact: 2
        scenario: 3
    result: pass
    checks:
    - CHECK-005
    evidence: docs/validation/coding-standards/check-005.md
    explanation: The reference exercised passing, invalid adoption and seeded regression paths. The
      guide continues to separate supervised evaluations from deterministic CI.
  - obligation:
      regression:
        impact: 3
        scenario: 0
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/coding-standards/check-002.md
    explanation: Compared changelog against the base. The new note is under the existing Unreleased
      heading and the candidate and historical sections remained byte-identical.
  findings: []
closure: prepared
---

# Tasks

- [x] TASK-001 — Define the index-resolved coding and changelog policy and PR review guidance.
- [x] TASK-002 — Implement deterministic Git comparison and Unreleased changelog validation.
- [x] TASK-003 — Integrate pinned Ruff and Git comparison into the Harness local command and CI.
- [x] TASK-004 — Integrate full quality validation in the exact-provider Python consumer reference and document adoption and rollback.
- [x] TASK-005 — Execute the approved checks and record current acceptance and regression evidence.

## Dependencies and completion

### Policy and review

TASK-001 has no implementation dependency. Add the canonical coding and changelog policy and its index entry. Update the Python Standard and existing PR guidance with references to the resolved policy, the human review criteria, and the initial lint and formatting scope. Document the exempt path groups and rationale. Completion means resolution works for the approved contexts and a reviewer can apply the Clean Code, SOLID and changelog accuracy criteria to the Design examples. Verification uses CHECK-001 and CHECK-003.

### Git and changelog

TASK-002 depends on TASK-001 for classification rules. Implement read-only Git comparison and diagnostics under `validators/quality/`. Select tracked paths, account for deletions and both paths of a rename, and compare normalized Unreleased entries with the selected base. Add maintained tests using temporary Git repositories. Completion means a qualifying new note and a documented exemption pass, while a missing, duplicated, moved or historical-only note fails for in-scope changes. Mixed paths, initial changelog creation, unavailable history, unsafe path inputs and empty diffs have explicit outcomes. Verification uses CHECK-002 and the Git comparison cases of CHECK-004.

### Harness execution and CI

TASK-003 depends on TASK-001 and TASK-002. Add the pinned Ruff configuration and shared quality entry point. Wire them into full Harness validation and the dedicated GitHub Actions quality job. Document local base selection and actionable setup errors in the project validation guide. Add an Unreleased entry and update the ADR index and living architecture documentation to reflect the integration. Completion means actual Ruff lint and formatting failures and clean cases are observable for changed Python files, push and PR baselines are reproducible, and the structural job retains its existing scope and archive guard. Reuse and extend the relevant CI regression tests. Verification uses CHECK-004.

### Python consumer

TASK-004 depends on TASK-003. Extend the existing Python validation assets and guide. Full local and CI validation must surface quality and suite outcomes independently after resolving the exact provider. Preserve existing custom commands in the adoption walkthrough, mark targeted runs as partial, and document rollback of the provider pin, wrapper, CI and configuration together. Completion means a prepared reference consumer can reproduce success and failure with the documented invocation and the migration walkthrough can restore the old validation configuration. Verification uses CHECK-004 and CHECK-005.

### Acceptance and regression evidence

TASK-005 depends on TASK-001 through TASK-004. Run `./scripts/validate/run.sh` and the five mapped Design checks. Capture before/after input snapshots, aggregate results and the observed environment. Assess all 13 acceptance scenarios and seven retained obligations, and record any failure or unavailable verification. Completion means current local evidence supports each required scenario and obligation, with no unresolved required failures or findings. Final remote CI and actual ruleset coverage are verified separately during authorized PR delivery. The local task does not require post-merge evidence.

## Planning review

The developer approved Tasks R1 in the issue #27 Codex chat after reviewing the Portuguese presentation. Approval binds this revision to the approved Proposal and Design. Implementation begins on explicit developer instruction.

## Progress

All five tasks completed. The initial lint probe found an unused import in the touched consumer fixture. The import was removed before the passing verification.

## Validation evidence

CHECK-001 through CHECK-005 passed locally using CPython 3.11.14 and pinned Ruff. The full run passed 142 validator tests and 48 execution tests. The assessments cover all 13 local scenarios and seven retained obligations. GitHub event behavior was exercised with disposable Git repositories and local workflow commands. No remote GitHub Actions run or ruleset verification was observed.

## Delivery

The developer authorized archival and PR submission after implementation. The dossier is prepared for delivery review under specs/archive/coding-standards. Remote review, checks and merge are tracked by GitHub.
