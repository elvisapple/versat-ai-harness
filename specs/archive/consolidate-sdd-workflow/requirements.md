---
change: consolidate-sdd-workflow
requirements:
  - id: REQ-001
    statement: Developers have one public SDD entry point with an explicit router to the four canonical workflows
    acceptance:
      - The versat-sdd skill routes rather than duplicates lifecycle content
      - The lifecycle guide identifies the entry, exit and developer prompt for each workflow
  - id: REQ-002
    statement: Planning uses human gates for Proposal/Requirements, Design and Tasks before implementation
    acceptance:
      - Approval records bind presented content without fabricating reviewer evidence
      - Planning approval alone does not authorize code changes
  - id: REQ-003
    statement: Documentary archive can be prepared in the implementation pull request without claiming merge
    acceptance:
      - Archive preparation has delivery evidence prerequisites
      - Merge confirmation is documented as a separate read-only observation
  - id: REQ-004
    statement: New SDD dossiers have machine-checkable metadata, traceability and validation evidence
    acceptance:
      - Local validation checks schemas, gates, traceability and evidence paths
      - Delivery readiness distinguishes failure from unavailable verification
  - id: REQ-005
    statement: Historical dossiers remain usable without fabricated retrospective approvals
    acceptance:
      - Only exact allowlisted dossier files receive legacy treatment
      - Continued implementation or delivery of an exempt dossier remains explicitly unverified
  - id: REQ-006
    statement: The consolidated SDD contract is governed, tested and checked in continuous integration
    acceptance:
      - An ADR records the durable decision and alternatives
      - The repository validation entry point runs the SDD checks and their tests
---

# Requirements

## Functional requirements

- REQ-001: The Harness MUST expose `versat-sdd` as the single public procedure and MUST route to `new-change`, `implement-change`, `validate-change` and `archive-change` documents by state.
- REQ-002: The Harness MUST require actual human approval of Proposal/Requirements, Design and Tasks before execution, and MUST allow approval plus an explicit implementation instruction in the same developer message after Tasks are presented.
- REQ-003: The Harness MUST prepare living specifications and documentary archive in the same change branch when delivery evidence is ready, without asserting that a remote merge occurred.
- REQ-004: The Harness MUST validate v2 metadata, stage digests, requirement/check/task traceability, local evidence references and readiness states without network access.
- REQ-005: The Harness MUST identify legacy exceptions by immutable filename hashes and MUST not silently treat absent v2 fields as an exemption.
- REQ-006: The Harness MUST document the decision and run deterministic validation and behavioral tests in the repository validation workflow.

## Non-functional requirements

- The contract MUST remain readable by a developer without hidden automatic workflow invocation.
- Local validation MUST state its limits rather than claim remote review, merge or deployment facts.
- New checks MUST run on supported Python with pinned validation dependencies.

## Acceptance scenarios

- Given an intent, a developer invokes `versat-sdd` and receives the planning workflow and its first human gate.
- Given current Tasks approval and an explicit implementation request, the agent may implement but may not create a remote pull request without separate authority.
- Given delivery evidence and completed tasks, the archival workflow can prepare the dossier before the pull request merges.
- Given a changed legacy dossier, validation rejects the old exemption instead of treating it as approved history.

## Constraints and assumptions

- This dossier records a transition approved in conversation before v2 individual gates existed; it does not assert retrospective stage approvals.
- External Git-provider facts remain outside the local validator.
