# Versat AI Harness

Versat's source of truth for AI-assisted development. This repository is also the portable Plugin package that brings together corporate standards, the Spec Driven Development (SDD) process, reusable capabilities, project templates and deterministic validation.

## Principles

- the repository defines the policies;
- Skills provide reusable capabilities;
- SDD defines the change process;
- validators and GitHub enforce rules that require deterministic controls;
- operational memory, Skills and policies have distinct governance levels;
- a single bootstrap supports software, agent, hybrid, library and infrastructure projects.

## Repository map

| Path | Responsibility |
|---|---|
| `plugin.json` | Portable Plugin identity and package entry point |
| `.codex-plugin/plugin.json` | Codex compatibility manifest |
| `skills/` | Installable Harness capabilities and procedures |
| [`agents/`](agents/README.md) | Reusable execution role guidance |
| `standards/` | Corporate rules that must be followed |
| `sdd/` | How changes are specified, implemented and archived |
| `project-templates/` | Composable structures used to create projects |
| `validators/` | Deterministic validation contracts |
| `scripts/` | Operational entry points for bootstrap, validation and release |
| `schemas/` | Harness metadata contracts |
| `resources/` | Verified, non-normative institutional knowledge |
| `docs/architecture/` | Current architecture overview |
| `docs/decisions/` | Architecture Decision Records (ADRs) |

The repository root is the installable Plugin boundary. Consequently, installed Skills and the canonical artifacts they resolve always come from the same version.

## Consumer project artifacts

The Plugin map above is not the layout generated for consumer projects. The agent template uses:

| Consumer path | Responsibility |
|---|---|
| `.agents/skills/<skill-name>/SKILL.md` | Local reusable capability |
| `.codex/agents/<agent-name>.toml` | Native Codex custom agent |
| `workflows/<workflow-name>/workflow.md` | Versat operational flow composing Skills |

These artifacts can serve business operations as well as development. Workflows require an explicit executor; the Markdown convention does not add an execution engine. Root Harness `agents/*.md` files are reusable role guidance, not native Codex registrations. See the [canonical contract](standards/core/agent-artifacts.md), [templates and migration guidance](project-templates/README.md) and [supplier-payment example](project-templates/examples/supplier-payment/workflow.md).

## Current state

Version `0.3.0` adds product discovery, first-use documentation and scenario coverage guidance to the portable Plugin package. It also consolidates SDD routing and local validation. Skills, standards, schemas, templates and validators remain versioned together; external integrations and technology-specific validators will be implemented incrementally through SDD.

## Local validation

Use Python 3.11 or later in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-validation.txt
./scripts/validate/run.sh
```

The entry point checks the Plugin package, SDD metadata/gates/traceability and the validator regression suite. The current source adds v3 scenario/regression assessments and input freshness; CI supplies a trusted baseline for live checks of changed archives. See the [validator guide](validators/sdd/README.md) for historical inventory limits and explicit compatibility. Explicit immutable legacy exceptions are reported separately; passing local checks does not authenticate human approval or prove a remote merge. An existing environment can also be selected with `PYTHON=/absolute/path/to/python ./scripts/validate/run.sh`.

## Developing a change

Use the single `$versat-sdd` Skill to plan, implement, validate or prepare documentary archival. It reads the relevant canonical workflow instead of maintaining a parallel process. See the [SDD developer guide](sdd/README.md) for example requests, phase deliverables, human approvals and PR/merge handling, and [SDD metadata](sdd/metadata.md) for validation commands and migration rules.

The consolidated process prepares living specifications and the documentary archive in the same delivery PR; a directory or local status is never proof of merge. Previously generated `new-change` instructions are superseded by this single entry point. Consumers retain their pinned released version until a separately reviewed release update.

## Workspace installation

The repository contains a private workspace marketplace at `.agents/plugins/marketplace.json`. Its Plugin entry selects an exact semantic release tag rather than a moving branch.

After release `v0.3.0` is tagged, a ChatGPT Business workspace administrator can distribute it as follows:

1. Open **Admin > Plugins** and select **Add > Import marketplace**.
2. Use `https://github.com/versat-private/versat-ai-harness` as the source repository and leave the marketplace path empty.
3. Authorize a GitHub account with read access to the private repository.
4. Review the import result and set the Plugin installation policy to **Installed** for the intended workspace roles.
5. Ask members to start a new conversation after installation.

Workspace installation policy is configured by the administrator and is not inherited from the repository marketplace policy. For a new release, update the marketplace entry to another exact tag through a reviewed change.

## Evolution

Every material change starts with an SDD proposal and, when it changes a structural decision, an ADR. Read `AGENTS.md`, `sdd/process.md` and `docs/decisions/README.md` before modifying the Harness.
