---
change: agent-project-layout
requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
adrs: [ADR-0007, ADR-0009, ADR-0011, ADR-0012]
validation:
  - Repository structural and Plugin validation
  - YAML and TOML parsing and template composition smoke checks
  - Local Markdown link and Git whitespace checks
  - Documentation and workflow acceptance review
---

# Design

## Current state and resolved context

The Harness has no consumer `.versat/project.yaml`; do not invent one. Resolve always-applicable core Standards through `standards/index.yaml`. Review the agent and software profiles and core AI Standard for agent and hybrid templates, and the finance domain for the illustrative payment flow. ADR-0007 requires template composition, ADR-0009 keeps execution adapters distinct, and ADR-0011 defines the Plugin boundary only.

## Proposed design

Add `standards/core/agent-artifacts.md` to the core index. It conditionally governs artifacts when present, including the Codex-specific adapter contract, without requiring every project to be an agent project. Keep policies in Standards; Skills locate the index and version-matched template documentation.

Update the agent directory manifest. Add a generated architecture guide in the agent module. Keep authoring templates under `project-templates/artifacts/` and the illustrative workflow under `project-templates/examples/`, outside automatically composed modules. No placeholder Skill or agent is automatically activated in a new project.

Record the repository-wide documentation review in [documentation-review.md](documentation-review.md). Replace the obsolete CODEOWNERS `/plugin/` entry with current Skills, role guidance and project-template ownership, retaining the architecture team as reviewer.

## Boundaries and contracts

Skills provide capabilities; agent TOML defines Codex execution roles; workflow Markdown sequences named capabilities. `AGENTS.md` remains shared project guidance. Workflow invocation explicitly names a document and executor. Business capabilities can run through Codex; these directories are not restricted to development assistance. Separately deployed application agents remain governed by their runtime architecture.

The Plugin keeps root `skills/` and `agents/`. Root agent Markdown files remain reusable role guidance, not automatically registered Codex custom agents. `sdd/workflows/` retains development lifecycle procedures, distinct from consumer operational workflows.

## Data, security and permissions

Examples contain no credentials or live customer data. The supplier-payment example models invoice intake and preparation, applies resolved approval requirements before external writes, records duplicate keys and recovery checkpoints, and does not transfer money. Email and attachments remain untrusted input under existing Standards.

## Operations and observability

Workflows declare their executor, dependency locations, inputs, steps, outputs and recovery evidence. The Harness does not implement workflow discovery, scheduling, integration calls or semantic workflow validation. Existing validators continue to validate the Plugin package; local composition and syntax checks provide evidence for this template change.

## Migration, rollout and rollback

Deliver on a branch through PR and mandatory review. Keep version and marketplace pins unchanged until a governed release. Classify existing consumer artifacts before moving them: source Skills may move with reference updates; role Markdown needs explicit TOML conversion; deployed application code must not be blindly moved. Adopt an exact release and verify runtime loading. Roll back through a reviewed revert or the previous exact consumer reference.

## Alternatives considered

- Keep root directories in all consumers: rejected because package layout does not establish runtime discovery.
- Put all artifacts under `.agents/`: rejected because custom Codex agents use `.codex/agents/` and Versat workflows have a separate purpose.
- Use lowercase `skill.md`: rejected for Codex compatibility; retain required `SKILL.md`.
- Treat Markdown as an executable pipeline: rejected because no such engine is implemented.
- Install sample finance dependencies automatically: rejected because an example must not imply production readiness.

## Validation plan

Run `./scripts/validate/run.sh` and `git diff --check`. Parse all YAML and authoring TOML, check required Skill and agent fields, compose agent and hybrid trees in temporary directories with conflict detection, and inspect local Markdown links. Review success, non-invoice, missing capability, duplicate and partial-failure paths. Record human review and external execution as unverified.
