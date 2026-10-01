# ADR-0012 — Separate consumer agent artifacts from Plugin packaging

- Status: Proposed
- Date: 2026-09-16
- Related: [ADR-0007](0007-composable-project-templates.md), [ADR-0009](0009-execution-adapters.md), [ADR-0011](0011-root-portable-plugin-package.md)

## Context

The agent profile creates root `skills/`, `agents/` and `workflows/` directories without discovery or execution contracts. The Harness itself uses root directories because it is a Plugin package. Applying that package layout to consumers confuses reusable capability authoring, Codex agent registration and operational workflow composition.

Codex discovers project Skills under `.agents/skills/` with uppercase `SKILL.md`. Its documented custom-agent format uses standalone TOML under `.codex/agents/`. Versat also needs explicit business workflows that call several Skills, such as invoice intake, ERP registration and attachment archival.

## Decision

Adopt the consumer paths and responsibilities in the canonical [Agent Artifact Standard](../../standards/core/agent-artifacts.md). Add the standard to the core resolver so any profile using these artifacts receives the same contract. Profiles without these artifacts need not create unused directories.

Keep the common authoring model independent of execution: Skills supply capabilities, agents define roles and workflows sequence capability calls. The `.codex/agents/` mapping is explicitly a Codex adapter; other runtimes document their adapter boundaries. Business operations may run through Codex, while separately deployed application agents retain their runtime architecture.

Use `workflows/<workflow-name>/workflow.md` as a Versat operational workflow convention. An executor or caller must explicitly load it. This change adds no workflow engine, scheduler or integration implementation.

Preserve `base + agent` and `base + software + agent` composition. Keep illustrative artifacts outside composed modules so bootstrap does not install placeholder capabilities or finance workflows automatically.

Retain the Harness root Plugin layout from ADR-0011. Its `agents/*.md` files are reusable role guidance, not automatically registered Codex custom agents. Retain `sdd/workflows/` as internal development lifecycle procedures. No previous ADR is superseded: this decision adds the consumer contract missing from those boundaries.

## Consequences

- Consumer layout has explicit discovery, authorship and execution responsibilities.
- `SKILL.md` casing is preserved for Codex compatibility; technical names and workflow definitions use the existing language policy.
- Workflow readiness requires real capability bindings, access and execution evidence rather than merely a Markdown file.
- Templates and current documentation must distinguish consumer conventions from Plugin packaging and SDD procedures.
- Existing consumers need a reviewed migration, including role conversion and reference updates, using an exact target release; no automatic move to `latest` occurs.
- Required policy review and merge remain pending; the local implementation records the requested direction without claiming review approval.

## References

- [Codex Skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
- [SDD change](../../specs/archive/agent-project-layout/proposal.md)
