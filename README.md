# Versat AI Harness

Versat's source of truth for AI-assisted development. This repository brings together corporate standards, the Spec Driven Development (SDD) process, capabilities distributed as a Plugin, project templates and deterministic validation.

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
| `plugin/versat-ai-harness/` | Installable package containing Harness capabilities |
| `standards/` | Corporate rules that must be followed |
| `sdd/` | How changes are specified, implemented and archived |
| `project-templates/` | Composable structures used to create projects |
| `validators/` | Deterministic validation contracts |
| `scripts/` | Operational entry points for bootstrap, validation and release |
| `schemas/` | Harness metadata contracts |
| `resources/` | Verified, non-normative institutional knowledge |
| `docs/architecture/` | Current architecture overview |
| `docs/decisions/` | Architecture Decision Records (ADRs) |

## Initial state

This version materializes the initial architecture and contracts. Skills, standards, schemas, templates and the minimum validation pipeline are already versioned; external integrations and technology-specific validators will be implemented incrementally through SDD.

## Local validation

```bash
./scripts/validate/run.sh
```

## Evolution

Every material change starts with an SDD proposal and, when it changes a structural decision, an ADR. Read `AGENTS.md`, `sdd/process.md` and `docs/decisions/README.md` before modifying the Harness.
