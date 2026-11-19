---
sdd_version: 3
change: coding-standards
requirements:
  - id: REQ-001
    statement: Developers and reviewers MUST have index-resolved coding conventions with actionable Clean Code and SOLID criteria and a documented verification method for each rule.
    acceptance:
      - Given a supported project context, when its Standards are resolved, then the result points to canonical guidance for readable names, cohesive responsibilities, interfaces, dependencies and the applicable technology rules.
      - Given a proposed change affecting module responsibilities or interfaces, when it is reviewed, then the reviewer has concrete criteria for separation of responsibilities, extension, substitutability, interface size and dependency direction, with guidance on when those principles apply.
      - Given a passing automated result, when a reviewer assesses the PR, then the guidance identifies the rules checked mechanically and the decisions requiring human review.
  - id: REQ-002
    statement: Notable changes MUST include an unreleased changelog entry and the validation path MUST identify missing changelog evidence.
    acceptance:
      - Given a change adding a feature, fixing observable behavior or modifying an applicable policy or compatibility contract, when required changelog evidence is absent or only historical release entries were touched, then the applicable check fails with instructions to add an unreleased entry.
      - Given an applicable change with a meaningful new entry in the project's unreleased changelog, when validated and reviewed, then the check recognizes the entry and the reviewer can confirm that it describes the impact.
      - Given an exempt change such as planning-only SDD edits, when validation and review apply the documented classification, then the reason can be inspected and a release entry is unnecessary.
  - id: REQ-003
    statement: GitHub Actions MUST run applicable deterministic checks on pushed revisions and PR updates while preserving required suite and delivery behavior.
    acceptance:
      - Given a Python source change violating an enabled lint or formatting rule, when a developer runs the documented local check or GitHub Actions validates the pushed revision or PR, then the corresponding check fails with an actionable diagnostic.
      - Given a compliant change, when the checks run, then they pass and retained test suites still execute, including cases where a retained suite fails independently of coding checks.
      - Given missing validation prerequisites or an unavailable required comparison base, when the check runs, then it reports the cause and returns a non-passing outcome.
      - Given draft and ready-for-review events and a main push, when Harness CI runs, then SDD inventory, baseline selection and the archive guard retain their current phase behavior. Any required supervised evidence continues to be assessed separately.
  - id: REQ-004
    statement: The Harness MUST provide a reproducible Python reference adoption path that preserves project-specific validation and exact provider references.
    acceptance:
      - Given a new or existing Python project adopting the reference integration, when the developer follows the guide from a prepared environment, then the exact provider and prerequisites are identifiable and the documented validation command produces observable success and failure results.
      - Given an existing consumer with custom commands, when adoption is proposed, then the reviewed change preserves or explicitly maps those commands, retains the composed template structure and gives a rollback path.
      - Given a targeted local run or consumer project that has yet to adopt the integration, when validation readiness is reported, then the limited scope or missing integration is visible and full required CI still applies to adopted projects.
---

# Requirements

## Actors and context

Versat SDD developers and coding agents apply the resolved Standards. Maintainers define technology rules and scope exceptions. Reviewers assess design choices and changelog accuracy. GitHub Actions executes deterministic checks and reports failures for the tested revision.

## Constraints and assumptions

Use the existing Standards index and keep policy, deterministic checks and SDD evidence in their respective layers. Reuse the configured validation path and retain existing tests and SDD controls. CI checks every delivered push head and PR update. The reference integration targets Python, and existing consumers adopt it through a reviewed exact version. The Design review will specify tool versions, enforceable rules, comparison baseline selection and how exemptions are recorded and reviewed.
