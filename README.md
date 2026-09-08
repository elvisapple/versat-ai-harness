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
| `agents/` | Reusable execution role guidance |
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

## Current state

Version `0.2.0` makes this repository a self-contained portable Plugin package. Skills, standards, schemas, templates and the minimum validation pipeline are versioned together; external integrations and technology-specific validators will be implemented incrementally through SDD.

## Local validation

```bash
./scripts/validate/run.sh
```

## Workspace installation

The repository contains a private workspace marketplace at `.agents/plugins/marketplace.json`. Its Plugin entry selects an exact semantic release tag rather than a moving branch.

After release `v0.2.0` is tagged, a ChatGPT Business workspace administrator can distribute it as follows:

1. Open **Admin > Plugins** and select **Add > Import marketplace**.
2. Use `https://github.com/versat-private/versat-ai-harness` as the source repository and leave the marketplace path empty.
3. Authorize a GitHub account with read access to the private repository.
4. Review the import result and set the Plugin installation policy to **Installed** for the intended workspace roles.
5. Ask members to start a new conversation after installation.

Workspace installation policy is configured by the administrator and is not inherited from the repository marketplace policy. For a new release, update the marketplace entry to another exact tag through a reviewed change.

## Evolution

Every material change starts with an SDD proposal and, when it changes a structural decision, an ADR. Read `AGENTS.md`, `sdd/process.md` and `docs/decisions/README.md` before modifying the Harness.
