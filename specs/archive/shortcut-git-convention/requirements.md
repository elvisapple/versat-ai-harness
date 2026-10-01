---
change: shortcut-git-convention
requirements:
  - id: REQ-001
    statement: Define Shortcut-linked branch and commit naming in the canonical Git Standard
    acceptance:
      - Story branches use the Story ID, Shortcut type and underscore-separated description
      - Story commits retain the ch marker and use feat, fix or chore
      - Work without a Story never receives an invented ID
  - id: REQ-002
    statement: Preserve language policy and simple adoption
    acceptance:
      - Technical descriptions remain English and internal Pull Requests remain Spanish
      - Scope and body are optional and Tasks have no one-to-one commit requirement
      - Existing history and merge strategy remain unchanged
  - id: REQ-003
    statement: Carry traceability through SDD and Pull Request review
    acceptance:
      - Proposal and Pull Request templates capture Story context when applicable
      - SDD workflows apply resolved Standards without copying naming rules into Skills
      - Squash commit guidance preserves the required commit format
  - id: REQ-004
    statement: Describe integration and enforcement limits truthfully
    acceptance:
      - Documentation distinguishes the Shortcut prefix extension from strict Conventional Commits
      - Future parsers must support the prefix and actual workspace linkage requires verification
      - Repository validation passes without implying Git naming enforcement
---

# Requirements

## Actors and context

Contributors, agents and reviewers use the same resolved core Standards. Shortcut Story metadata supplies the ID and branch type when a Story exists.

## Constraints and assumptions

The supplied convention changes naming and traceability, not the existing delivery process. The current language policy remains authoritative. No Story has been supplied for this change. Historical commits and branches are not migration targets.

## Acceptance scenarios

- A Bug Story numbered 305319 uses an English branch description and a fix subject with its Story marker.
- Feature and Chore Stories use their respective branch types and initial commit mappings.
- A contributor can omit the scope and body and can create several logical commits for one Story.
- A reviewer can follow the Story from the SDD proposal to the PR and commits, or see an explicit statement that no Story applies.
- A Spanish PR title is not used unchanged as an English squash commit subject.
- Structural validation passes while Git naming and external Story association remain separately identified review checks.
