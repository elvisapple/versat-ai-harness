---
change: agent-project-layout
status: implemented
owner: versat
summary: Separate project Skills, Codex agents and Versat workflows from Plugin packaging
risk: medium
---

# Proposal

## Context and problem

The agent template creates root `skills/`, `agents/` and `workflows/` directories without defining their discovery or execution contracts. This resembles the Harness Plugin package and obscures how consumer projects should author capabilities, agents and business workflows.

## Expected outcome

Consumer projects use `.agents/skills/<skill-name>/SKILL.md`, `.codex/agents/<agent-name>.toml` and `workflows/<workflow-name>/workflow.md`. The Harness retains its Plugin layout. Workflow documents compose Skills through an explicitly identified executor; they do not create an execution engine.

## Scope

- Define the canonical artifact contract and resolve it through the Standards index.
- Reformulate the agent module while preserving base and hybrid composition.
- Provide authoring templates and an illustrative supplier-payment workflow.
- Review all Harness documentation and adapt current guidance, migration instructions and validation claims.
- Align CODEOWNERS review routing with current Skills, role guidance and template paths.
- Record an ADR, local validation evidence and pending delivery gates.

## Out of scope

Implementing Gmail, Versat ERP or Google Drive integrations; executing payments; building a workflow engine; migrating consumer repositories; releasing or changing exact version pins. Root Plugin role documents are not converted into native Codex agents by this change.

## Work tracking

No Shortcut Story was supplied. Use `codex/agent-project-layout` without inventing a Story identifier.

## Impact and risks

The user accepted the structural direction. `SKILL.md` remains uppercase for Codex discovery despite the lowercase spelling in the request. Technical names remain English under the existing language policy. New templates change consumer paths, so existing projects need a reviewed migration with an exact target release. Human policy review, required checks and merge remain delivery gates.

## Proposal acceptance criterion

A contributor can distinguish a Plugin resource from a project Skill, a native Codex agent and a Versat workflow, and can author each at the intended path without assuming automatic workflow execution.
