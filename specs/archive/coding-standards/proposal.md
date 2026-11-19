---
sdd_version: 3
change: coding-standards
status: accepted
owner: evertonspohrversat
summary: Establish coding and changelog standards with reproducible GitHub checks and explicit review criteria.
risk: medium
impact:
  state: assessed
  summary: Extend project validation and changelog maintenance while preserving required suites, exact provider adoption, and SDD delivery controls.
  items:
    - source:
        change: automated-test-execution
        requirement: REQ-005
        scenarios: [1, 2, 3]
        requirements_digest: 63fc678f2c350f828a5ce5e2e3e077f60e3d51d1cbd4d57c04fe5ad4665755a5
      current_contract:
        path: docs/guides/project-validation.md
        locator: '## CI and rollback'
        digest: f3ef63238b100a92cb42ca4753130f54018a5a76ec44e7a5cf809761c6b77b37
      effect: extend
      targets: [REQ-003, REQ-004]
      reason: Add deterministic checks to the existing validation path while retaining suite and readiness behavior.
    - source:
        change: automated-test-execution
        requirement: REQ-007
        scenarios: [1, 2, 3]
        requirements_digest: 63fc678f2c350f828a5ce5e2e3e077f60e3d51d1cbd4d57c04fe5ad4665755a5
      current_contract:
        path: docs/guides/project-validation.md
        locator: '## Prerequisites and adoption'
        digest: f3ef63238b100a92cb42ca4753130f54018a5a76ec44e7a5cf809761c6b77b37
      effect: preserve
      targets: [REQ-004]
      reason: Keep reference setup reproducible and preserve reviewed adoption of an exact provider reference.
    - current_contract:
        path: CHANGELOG.md
        locator: '## [Unreleased]'
        digest: 4d69754f2a696fd1e684ca9b712856478b44eaf8d47b399cb532bb5ea5ad1c14
      effect: extend
      targets: [REQ-002]
      reason: Make the existing practice of recording notable changes measurable in validation while retaining release history.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Developer reply in the Codex chat for issue #27 after presentation of Proposal and Requirements R1 in Portuguese.
    quote: Aprovo a Proposal e os Requirements R1 da issue #27. Pode avançar para o Design e trazer a versão em pt-BR aqui no chat para eu revisar.
    revision: 1
    digest: 125767fca0766318d669f4e5a51e20689bb8687fa443a4077638b85524d38ab1
---

# Proposal

## Context and problem

Versat SDD developers and reviewers need common criteria when changing software. Existing technology Standards cover some formatting and analysis, and the Harness keeps a changelog and runs GitHub validation. There is no shared Clean Code and SOLID review contract or routine CI check for a missing changelog entry on a notable change.

## Expected outcome

Developers can resolve the applicable coding conventions, run the same objective checks locally and in CI, and tell what still requires human review. A pull request records notable changes for users and maintainers before delivery.

## Scope

- Define canonical coding guidance under `standards/`, resolved through the existing index and applied alongside technology Standards. Make Clean Code and SOLID criteria actionable for code authors and reviewers.
- Define when a change requires an unreleased changelog entry and how to document an allowed exemption. Check objective evidence in CI and review the accuracy of the entry in the PR.
- Run the applicable checks locally, on pushes and as part of PR validation. Prove the integration in the Harness repository and the existing Python reference consumer. Keep other technology conventions resolvable through the index.

## Out of scope

- Automated judgment of every Clean Code or SOLID principle, new analyzers for every technology, repository-wide reformatting, Git history rewriting, release automation, and rollout to existing consumers.

## Work tracking

[GitHub issue #27](https://github.com/versat-labs/versat-ai-harness/issues/27). No Shortcut Story is associated. The local branch is `codex/27-coding-standards`.

## Impact and risks

The baseline is provider source `c13b2f9` (`VERSION` 0.4.0, private candidate). Harness validation covers PR events and main pushes. The Python consumer reference already has push and PR triggers and invokes configured suites. The Harness changelog has an Unreleased section above candidate and historical entries. Relevant maintained coverage includes `tests/validators/`, `tests/execution/`, and the consumer validation integration documented in `docs/guides/project-validation.md`.

Overbroad rules could force unrelated legacy cleanup or demand release notes for internal edits. Weak checks could accept placeholder notes or imply automatic conformance to design principles. Define mechanically detectable cases and a documented path for changes requiring reviewer judgment. A push check evaluates the resulting revision, including the head of a multi-commit push. The PR checks the net change against its base. The initial Python scope limits CI adoption work to an existing supported reference.

## Proposal acceptance criterion

The approved scope identifies reviewable coding criteria, actionable failures for objective violations and missing changelog evidence, and compatible local and CI adoption. Tool selection, exact rule coverage, release-note classification mechanics and Git baseline handling belong in Design.
