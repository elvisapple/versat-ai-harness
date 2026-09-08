# ADR-0011 — Make the repository root the portable Plugin package

- Status: Accepted
- Date: 2026-09-08
- Supersedes: ADR-0001, ADR-0002

## Context

ADR-0001 placed the installable Plugin under `plugin/versat-ai-harness/`, while ADR-0002 kept Standards, SDD and validators in canonical top-level directories. That separation left installed Skills outside the package boundary of the artifacts they must resolve and apply.

Copying those artifacts into the nested package would require synchronization machinery and create a second representation of governed content. Moving executor-independent content under a Codex-specific adapter directory would also weaken the boundary established by ADR-0009.

The portable Agent Plugins format supports a root `plugin.json`, root `skills/` discovery and additional package resources.

## Decision

Make the repository root both the source-of-truth boundary and the portable Plugin package root.

Keep responsibilities separated by top-level directory:

- `standards/`: canonical policies;
- `skills/`: capabilities and procedures;
- `sdd/`: change process;
- `validators/` and CI: deterministic enforcement;
- `project-templates/` and `schemas/`: composable project and metadata contracts;
- `agents/`: reusable execution roles.

Use root `plugin.json` as the portable package manifest and root `.codex-plugin/plugin.json` as a compatibility overlay. Distribute the package through a repository marketplace whose Plugin source selects an exact semantic release reference.

## Consequences

- installed Skills can resolve all version-matched canonical artifacts within one package root;
- policies remain canonical and are not copied into Skills or a generated distribution tree;
- the installable package includes the complete repository, increasing package size;
- package metadata and repository version must remain synchronized;
- the former `plugin/versat-ai-harness/` path is removed and existing local installations must reinstall;
- workspace distribution remains an adapter and does not replace Standards, SDD or deterministic enforcement;
- consumer repositories continue to adopt new Standards through exact lockfile updates and reviewable changes.
