---
sdd_version: 2
change: quickstart-scenario-coverage
requirements:
  - id: REQ-001
    statement: Projects MUST provide a concise living first-use guide when usable product behavior needs explanation, reusing an equivalent existing guide or defaulting to docs/quickstart.md.
    acceptance:
      - Given a project with usable behavior and no equivalent guide, when first-use documentation is delivered, then docs/quickstart.md explains the prerequisites, preparation, a representative action and its observable expected result.
      - Given an existing suitable first-use guide, when this guidance is adopted, then the guide is updated in place without creating a duplicate solely to match the default path.
      - Given an empty scaffold with no meaningful usable behavior, when the project is bootstrapped, then no empty quickstart or instructions claiming unimplemented behavior are created.
  - id: REQ-002
    statement: The root README MUST link to the actual first-use guide, whose stable location and focused supporting guides remain independent of SDD dossier archival.
    acceptance:
      - Given a delivered first-use guide, when a reader opens the root README, then a descriptive working link leads to that guide.
      - Given a concise first-use workflow, when documentation is organized, then one guide is sufficient and no per-feature files or empty guide directories are required.
      - Given a distinct workflow needing more explanation, when a supporting guide is added, then the default location is docs/guides/ unless an existing documentation convention applies, and the quickstart links to it without copying shared setup instructions.
      - Given a change dossier that references the living guide, when the dossier is archived, then the README link and guide location remain valid.
  - id: REQ-003
    statement: SDD planning and implementation MUST account for affected usage documentation through existing tasks and update that documentation alongside delivered behavior.
    acceptance:
      - Given a change to setup, commands or a user workflow, when it is planned, then existing Tasks include the required documentation work and implementation updates the affected guide or examples before delivery.
      - Given an internal change with no effect on documented usage, when its tasks are prepared, then no documentation artifact or task is added solely for ceremony.
      - Given an already documented workflow, when a later change alters its behavior, then the living guide is updated rather than creating a competing guide for the new change ID.
  - id: REQ-004
    statement: Validation MUST check affected documented steps and examples against implemented behavior and record actual outcomes through the existing evidence contract.
    acceptance:
      - Given changed runnable instructions, when validation runs, then the affected setup or usage steps are exercised and observed results are compared with the documented outcomes.
      - Given a documented UI workflow, when validation runs, then its affected steps and observable result are verified through an appropriate manual or automated check.
      - Given unavailable access or environment dependencies, when an affected guide cannot be verified, then the existing Tasks evidence records the check as unverified with the reason rather than claiming success.
      - Given a documentation check that shares a method with a functional check, when evidence is recorded, then the existing check and result can be reused without a separate documentation report.
  - id: REQ-005
    statement: Test planning and validation MUST assess relevant acceptance scenarios, including meaningful error and boundary behavior in proportion to change risk.
    acceptance:
      - Given a requirement with relevant success, error and boundary scenarios, when its validation is planned and reviewed, then those scenarios are covered by appropriate tests or explicit checks rather than treating one linked happy-path check as sufficient.
      - Given existing tests that already cover the affected scenarios, when the change is planned, then they can be reused without duplicating test cases or introducing new scenario identifiers.
      - Given a relevant scenario without coverage or observed evidence, when validation is reported, then the gap is explicit and is not hidden by a passing metadata validator or an unrelated passing test.
      - Given a low-risk change, when checks are selected, then they address its observable behavior without a fixed case count, exhaustive input enumeration or mandatory test-first development.
  - id: REQ-006
    statement: The change MUST preserve the existing SDD lifecycle, policy ownership, template composition and proportional adoption without adding mandatory artifacts or enforcement mechanisms.
    acceptance:
      - Given the revised Harness, when a change follows SDD, then it uses the existing four primary dossier files, three planning gates and current requirement/check/task identifiers and evidence fields.
      - Given bootstrap guidance for multiple profiles, when projects are composed, then shared documentation guidance is supplied through base composition without copied profile policies, empty guides or broken README links.
      - Given an existing consumer, when the Harness source is changed or released, then its documentation and pinned reference remain unchanged until an explicitly governed adoption.
      - Given documentation for different audiences, when it is authored, then the existing Language and Security Standards determine language, translations and permissible data without a new quickstart-specific policy.
---

# Requirements

## Actors and context

Product users need a short route to a first useful result. Developers and coding agents maintain the guide and scenario coverage as behavior changes. Reviewers assess actual validation evidence. Bootstrap authors provide shared guidance without manufacturing runnable product instructions for an empty project.

These requirements govern Harness instructions and templates for consumer projects. They do not execute a migration or implement features in a consumer repository.

## Functional requirements

REQ-001 and REQ-002 define guide content, discoverability and organization. REQ-003 and REQ-004 integrate maintenance and verification into the existing lifecycle. REQ-005 strengthens behavioral scenario coverage. REQ-006 constrains the delivery to the existing governance and composition model.

## Non-functional requirements

Keep the first-use guide focused on one useful outcome and link to supporting detail as needed. State the intended audience and use commands or UI steps appropriate to that audience. Reference existing setup, contracts and requirements instead of copying them into multiple sources. Living guides describe implemented behavior; planning may identify future documentation work without presenting it as delivered.

Canonical policy belongs under `standards/` and is resolved through its index. SDD procedures apply that policy; Skills route to it. No new validator, schema field, test-case catalog, coverage percentage, fixed guide count or universal TDD rule is introduced.

## Acceptance scenarios

The scenarios attached to each requirement in the frontmatter are the canonical acceptance scenarios for this change. Design will map them to reproducible checks after approval; no separate scenario catalog or test-plan artifact is required.

## Constraints and assumptions

- Default consumer paths are `docs/quickstart.md` and, only when needed, `docs/guides/`. Existing suitable documentation conventions are preserved.
- A quickstart may support end users, API/library consumers, operators or developers according to the product; a runnable command is not required for a purely graphical workflow.
- Guide creation is conditional on useful content. README links are added only when their target exists. Detailed manuals and automatic publication remain outside scope.
- Existing local validators establish structural consistency, not semantic scenario coverage or successful execution of a usage guide. Review and observed checks remain necessary.
- Existing language, security, PR review and exact-release adoption rules remain authoritative. No consumer upgrades or historical dossier edits are authorized by this proposal.
- No material unresolved decision blocks review of Proposal/Requirements R1. Design and Tasks remain pending their existing gates.
