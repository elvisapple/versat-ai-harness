---
sdd_version: 3
change: coding-standards
requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
adrs: [ADR-0017]
validation:
  - id: CHECK-001
    description: Review the resolved coding policy and PR guidance
    requirements: [REQ-001]
    required: true
    method:
      kind: review
      procedure: >-
        Resolve software, hybrid, library and Python project examples using the existing standards resolver. Review a fixture that mixes persistence and business policy and a fixture with a subtype that changes a caller guarantee. Expect canonical criteria and a corresponding PR review decision. Verify the guide distinguishes semantic decisions from automated Ruff rules.
      reason: Semantic correctness and appropriateness of SOLID are reviewer judgments.
    inputs:
      include: [standards, project-templates, scripts, docs/guides, .github]
      exclude: []
    outputs: [docs/validation/coding-standards/check-001.md]
    execution: local
  - id: CHECK-002
    description: Verify the Unreleased changelog contract
    requirements: [REQ-002]
    required: true
    method:
      kind: automated
      procedure: >-
        Run the maintained quality validator integration tests through scripts/validate/run.sh with temporary Git histories. Expect a fail for missing, repeated, moved or historical-only notes and a pass for a new note, first changelog and planning-only exemption. Exercise mixed paths, deletions, no-change comparisons and unavailable bases.
    inputs:
      include: [standards, validators, scripts, tests, project-templates, .github, CHANGELOG.md]
      exclude: []
    outputs: [docs/validation/coding-standards/check-002.md]
    execution: local
  - id: CHECK-003
    description: Review changelog accuracy and classification
    requirements: [REQ-002]
    required: true
    method:
      kind: review
      procedure: >-
        Apply the documented classification and PR guidance to an API behavior change with a candidate note and to a planning-only fixture. Expect the reviewer to identify scope and impact in the note and the documented reason for the exemption.
      reason: Git can detect an entry but cannot assess whether it accurately describes impact.
    inputs:
      include: [standards, validators, scripts, tests, project-templates, .github, CHANGELOG.md, docs/guides]
      exclude: []
    outputs: [docs/validation/coding-standards/check-003.md]
    execution: local
  - id: CHECK-004
    description: Exercise local and CI quality and retain delivery controls
    requirements: [REQ-003, REQ-004]
    required: true
    method:
      kind: automated
      procedure: >-
        Run scripts/validate/run.sh and the maintained CI and consumer integration tests in tests/execution. Extend those tests and add validator fixtures to exercise actual Ruff lint, format and clean outcomes plus missing tools and Git history, branch creation, PR update and push base selection. Expect identical quality behavior for the same baseline and checkout, independent failure reporting for retained suites, and unchanged SDD archive and supervised evidence outcomes.
    inputs:
      include: [.github, standards, schemas, project-templates, requirements-validation.txt, scripts, tests, validators, sdd, VERSION, plugin.json, CHANGELOG.md]
      exclude: []
    outputs: [docs/validation/coding-standards/check-004.md]
    execution: local
  - id: CHECK-005
    description: Walk through Python adoption and rollback
    requirements: [REQ-004]
    required: true
    method:
      kind: review
      procedure: >-
        Follow the updated project validation guide on a clean Python reference consumer with an exact provider checkout and on the existing custom-suite fixture. Run the documented success, failure and targeted invocations. Inspect template composition, provider enforcement, unadopted status and rollback. Expect a working full invocation, exact provider binding, preserved custom suites, visible limited readiness and restoration of the previous validation setup.
      reason: A walkthrough checks whether the published instructions are usable and the migration diff preserves consumer intent.
    inputs:
      include: [.github, standards, schemas, project-templates, requirements-validation.txt, docs/guides, scripts, tests, validators, VERSION, CHANGELOG.md]
      exclude: []
    outputs: [docs/validation/coding-standards/check-005.md]
    execution: local
coverage:
  - scenario: {requirement: REQ-001, scenario: 1}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-001, scenario: 2}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-001, scenario: 3}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-002, scenario: 1}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-002, scenario: 2}
    applicability: required
    checks: [CHECK-002, CHECK-003]
  - scenario: {requirement: REQ-002, scenario: 3}
    applicability: required
    checks: [CHECK-002, CHECK-003]
  - scenario: {requirement: REQ-003, scenario: 1}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-003, scenario: 2}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-003, scenario: 3}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-003, scenario: 4}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-004, scenario: 1}
    applicability: required
    checks: [CHECK-004, CHECK-005]
  - scenario: {requirement: REQ-004, scenario: 2}
    applicability: required
    checks: [CHECK-005]
  - scenario: {requirement: REQ-004, scenario: 3}
    applicability: required
    checks: [CHECK-004, CHECK-005]
regression:
  - obligation: {impact: 1, scenario: 1}
    checks: [CHECK-004]
    rationale: A retained suite failure still fails complete consumer CI.
  - obligation: {impact: 1, scenario: 2}
    checks: [CHECK-004]
    rationale: Preserve draft, ready and main push SDD enforcement and baseline tests.
  - obligation: {impact: 1, scenario: 3}
    checks: [CHECK-004]
    rationale: Keep supervised evidence findings independent of CI success.
  - obligation: {impact: 2, scenario: 1}
    checks: [CHECK-005]
    rationale: Preserve the composed Python setup and a documented entry point.
  - obligation: {impact: 2, scenario: 2}
    checks: [CHECK-005]
    rationale: Keep custom validation, exact pins and rollback reviewable.
  - obligation: {impact: 2, scenario: 3}
    checks: [CHECK-005]
    rationale: Exercise the documented first-use and retained-regression workflow and preserve supervised guidance.
  - obligation: {impact: 3, scenario: 0}
    checks: [CHECK-002]
    rationale: Keep the Unreleased section above intact historical entries.
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 125767fca0766318d669f4e5a51e20689bb8687fa443a4077638b85524d38ab1
  approval:
    source: Developer reply in the Codex chat for issue #27 after presentation of Design R1 in Portuguese and draft ADR-0017.
    quote: Aprovo o Design R1 e o ADR-0017 da issue #27. Pode preparar o plano de tarefas e trazer a versão em pt-BR aqui no chat para eu revisar.
    revision: 1
    digest: c2d456db6f44c604141519558f7be127564ffac2c20a16a45c94721cc4045bcc
---

# Design

## Current state

The provider source is `c13b2f9` (private 0.4.0 candidate). The Harness workflow validates PR activity and main pushes. Its structural job selects the SDD archive baseline. The Python reference already runs configured suites through the consumer wrapper and provider verifier on push and PR. The repository changelog separates Unreleased from named releases. An exploratory Ruff run on selected Harness directories found 20 files requiring formatting, so enforcing format across the whole repository would add unrelated churn.

## Proposed design

- Add shared coding policy to the index-resolved core Standards. Explain readable names, cohesive responsibilities and SOLID using concrete review examples. Reviewers examine responsibility boundaries, safe extension and substitution, narrow interfaces and dependency direction where relevant. Add review prompts to existing PR guidance without copying policy into Skills. Extend the Python Standard with the mechanical rules and documented invocation. Apply the resolved language, documentation, Git, security, contribution and testing Standards alongside it.
- Pin Ruff to `0.14.14` for the initial Python integration and set the reference target to Python 3.11. Use `E4,E7,E9,F` lint families and Ruff's formatter, in read-only modes `ruff check --no-fix` and `ruff format --check`. Use versioned project configuration with the same settings locally and in CI. Validate complete tracked Python source files added or modified by the change, including rename destinations. Leave deleted files out of Ruff selection. Exclude vendored or generated content only with a documented, reviewed rule. Report the number checked or an explicit empty selection. A file already touched by a change may need formatting beyond edited lines.
- Add `validators/quality/validate.py` as a deterministic check of the chosen base and the checkout. It identifies changed paths and verifies changelog evidence. A small `scripts/validate/quality.sh` entry point coordinates the validator and Ruff, with explicit dependencies and a required base. Full local validation runs quality and existing suites and aggregates failure. The consumer wrapper verifies its exact provider and invokes the same quality entry point with the consumer root. Explicit targeted suite runs report partial scope. Keep the existing SDD schemas, test runner and evidence formats.
- Require a new, nonblank list item under the unique `## [Unreleased]` heading for a change in scope. Classify conservatively by path with a narrow documented exemption list. A diff limited to SDD dossiers, tests or internal documentation is exempt. Runtime, public guidance, policies, CI, templates and compatibility changes require a note. Treat unclassified paths as in scope. A mixed change is in scope if any affected path requires a note. A rename considers both paths for classification. Exemptions are versioned with their rationale and reviewed through the existing governance. The check emits the classification, then compares normalized Unreleased entries against the base, ignoring duplicates and entries already present anywhere in the base changelog. Reject missing or ambiguous required structure. An initial changelog may supply a note when no file existed at the base. Editing historical entries alone does not satisfy the check. PR review confirms accuracy and can require a note when a path-based exemption misses a material effect.

## CI and comparison bases

Use the same content comparison in the Harness and the adopted Python reference. On `pull_request`, compare GitHub's base SHA with the checked-out merge revision. On an existing branch push, compare the event's before SHA with the pushed tip. On a new branch with no before SHA, resolve the merge base against the remote default branch. A repository's initial single root commit may use an empty-tree baseline. Missing or invalid required history, including an unresolvable branch base, fails with instructions to fetch the necessary refs or provide an explicit base locally. Branch deletion and tag events are outside the code check. A push checks its resulting tip. Local comparison uses an explicit base and evaluates the tracked working tree, including staged additions and tracked unstaged edits. Stage a new file before using this local check.

Add a quality job on all branch pushes and PR events in the Harness and retain its existing `structural-validation` job for PRs and main pushes. On other branch pushes, skip the structural job. Preserve its existing PR-base and main-push baseline, draft and archive conditions. Consumer CI runs the quality and suite checks independently within full validation. Both outcomes remain visible and either failure makes full validation fail. Use read-only permissions, full Git history for comparison and checkout without persisted credentials. Accept only resolved Git objects and repository-relative tracked paths as data. Use argument vectors, reject unsafe path or symlink inputs, and keep comparison and checks free of write operations and automatic fixes. Run PRs in the ordinary `pull_request` context. No new secrets or service access are needed for quality checks. Remote ruleset coverage must be confirmed separately before treating merge enforcement as effective.

## Adoption and rollback

Ship the integration first in Harness source and the existing Python reference template. Update the project validation guide with tool setup, local and CI baseline rules, errors and examples of exempt and notable changes. Preserve base/profile composition and custom suite commands. Existing consumers adopt a reviewed exact provider version and corresponding template changes. Keep the previous provider pin, wrapper, CI setup and configuration together for rollback so required existing suites continue to run. In a newly created consumer, set the real paths and revision before calling it ready. No data migration is needed.

## Alternatives and architectural decision

Full-tree Ruff would expose all existing debt at once. Changed-line checks could miss file-wide lint issues and can disagree with the formatter. Checking entire changed files gives a predictable boundary and limits cleanup to files already in review. Human-only changelog review would miss obvious omissions that a Git-based check can surface. Automatic release-note generation would add tooling and convention changes outside this scope. Record the repository and consumer integration boundary in proposed ADR-0017.

## Validation plan

The quality validator and wrapper are proposed entry points. The package validation script, provider wrapper, and maintained CI and consumer suites already exist. CHECK-001 reviews resolution and semantic coding criteria. CHECK-002 runs Git/changelog cases, and CHECK-003 reviews the accuracy and exception decisions. CHECK-004 exercises Ruff, comparison events, missing prerequisites and retained CI behavior. CHECK-005 walks through the documented consumer setup and rollback. All 13 acceptance scenarios and seven retained obligations are mapped in the frontmatter. Run the planned checks locally, preserve required remote CI before merge, and record observed evidence through the existing SDD workflow.

## Planning review

The developer approved Design R1 and ADR-0017 in the issue #27 Codex chat after reviewing the Portuguese presentation. The approval binds to the Design R1 digest above.
