---
change: agent-project-layout
requirements:
  - id: REQ-001
    statement: Agent and hybrid templates use the consumer artifact layout
    acceptance:
      - Agent composition creates .agents/skills, .codex/agents and workflows without root skills or agents
      - Hybrid composition preserves software directories and shared base files without conflicts
  - id: REQ-002
    statement: Canonical contracts distinguish capability, agent configuration and workflow composition
    acceptance:
      - The Standards index resolves the artifact contract for all profiles
      - Skill filename casing and required Codex agent fields are explicit
      - Workflows identify dependencies, executor, steps, outputs and recovery behavior
  - id: REQ-003
    statement: A supplier-payment example demonstrates explicit multi-Skill orchestration
    acceptance:
      - The example checks Gmail, branches on invoice classification, registers an ERP record and archives the attachment in Drive
      - Missing dependencies, duplicate invoices and partial failure prevent false completion
      - The example makes no live integration or payment-execution claim
  - id: REQ-004
    statement: Documentation, packaging and migration guidance agree
    acceptance:
      - Current guidance distinguishes Plugin roles, SDD procedures and consumer workflows
      - Historical ADRs and change artifacts retain their original context
      - Existing consumers require an explicit reviewed migration and unchanged release pins
      - Repository validation and template composition checks pass with limitations recorded
---

# Requirements

## Actors and context

Project authors, bootstrap and maintenance Skills, reviewers and workflow executors share the same canonical contract. Profiles without agent artifacts are not required to create unused directories.

## Constraints and assumptions

The workflow format is a Versat Markdown authoring convention, not a Codex discovery format or a deterministic engine. External services and capabilities in examples must be configured and verified before use. Business approval rules are resolved from existing core and domain Standards.
