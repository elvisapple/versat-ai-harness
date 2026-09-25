# Agent project architecture

Complete this document during bootstrap. Resolve the Agent Artifact Standard through `standards/index.yaml` in the exact Harness version recorded by `.versat/standards.lock`.

## Artifact map

```text
AGENTS.md
.agents/skills/<skill-name>/SKILL.md
.codex/agents/<agent-name>.toml
workflows/<workflow-name>/workflow.md
evals/
tests/
```

Skills supply reusable capabilities. Codex agent TOML defines execution roles. Workflows sequence Skill calls and hand their outputs to subsequent steps. `AGENTS.md` supplies shared repository guidance. These artifacts can serve business operations or development assistance; record their purpose below.

The Harness Plugin's root directories are packaging details, not this project's directory convention. Application source, if present, follows its own module architecture.

## Capability and workflow inventory

For each artifact, record its purpose, owner, path and consumers. For each workflow, identify its executor, local or installed Plugin Skill dependencies, connector setup and exact external version references. Use the authoring artifacts and examples from the pinned Harness package as starting points; do not activate unresolved placeholders.

## Execution

Document the supported Codex release and agent loading verification. For an operational workflow, explicitly instruct the executor to read `workflows/<workflow-name>/workflow.md` and resolve its prerequisites before running the steps. Codex does not automatically execute that file by directory discovery.

Identify any scheduling, state storage, concurrency or retry mechanism actually implemented. If execution is supervised and manual, state that explicitly.

## Data and authorization

Document connector scopes, data ownership, classification, memory and retention boundaries, approval responsibilities and the evidence retained for each execution. Reference resolved Standards and keep secrets outside the repository.

## Validation and recovery

Document the project's validation entry point, critical evals, integration checks, duplicate prevention, partial-failure recovery and escalation owner. Distinguish tested behavior from planned capabilities.
