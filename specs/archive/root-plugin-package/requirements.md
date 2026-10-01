---
change: root-plugin-package
requirements:
  - id: REQ-001
    statement: The repository root is an installable portable Plugin package
    acceptance:
      - Root plugin.json declares the Agent Plugins schema and version 0.2.0
      - Root skills directory contains every supported Harness Skill
      - Root compatibility manifest remains valid for Codex
  - id: REQ-002
    statement: Canonical Harness artifacts are available to installed Skills without duplication
    acceptance:
      - Standards, SDD, templates, schemas and validators remain canonical root directories
      - Skills resolve canonical paths from the installed Plugin root
      - No copied Standards tree exists inside a Skill
  - id: REQ-003
    statement: The Plugin is distributable to the Versat workspace from GitHub
    acceptance:
      - A repository marketplace catalog contains the Plugin
      - The Git source selects an exact semantic release reference
      - Workspace installation steps are documented
  - id: REQ-004
    statement: The package-boundary migration is governed and mechanically validated
    acceptance:
      - Superseded architecture decisions retain their history
      - A new ADR records the root-package decision
      - Validation rejects stale nested Plugin paths and version drift
---

# Requirements

## Functional requirements

- REQ-001: The repository root MUST be a portable Plugin package and MUST retain the supported Codex compatibility manifest.
- REQ-002: Installed Skills MUST be able to access the same canonical artifacts versioned with the Plugin without maintaining parallel policy copies.
- REQ-003: A workspace administrator MUST be able to import the Plugin from the private GitHub repository through a marketplace catalog pinned to an exact release.
- REQ-004: The migration MUST preserve ADR history, semantic version consistency and deterministic structural validation.

## Non-functional requirements

- The Plugin package MUST remain executor-independent at its canonical core boundaries.
- Plugin identity and version MUST agree across `VERSION`, the portable manifest and the compatibility manifest.
- Marketplace updates MUST NOT implicitly select `latest` or a moving branch for the Plugin source.
- Existing project lockfiles MUST continue to control consumer artifact versions.

## Acceptance scenarios

- Given a checkout of release `v0.2.0`, a Plugin host discovers root `plugin.json` and every root Skill.
- Given an installed Plugin cache, a Skill can resolve `standards/`, `sdd/`, `project-templates/`, `schemas/` and `validators/` within the same package root.
- Given the workspace marketplace import, the catalog resolves `versat-ai-harness` from the exact `v0.2.0` Git reference.
- Given any stale tracked file under `plugin/versat-ai-harness/`, repository validation fails.

## Constraints and assumptions

- ChatGPT workspace import and policy configuration are administrator actions outside this repository change.
- The private GitHub repository remains readable by the account used to configure marketplace synchronization.
- Version `0.2.0` is not considered released until the governed Pull Request is merged and the exact tag is created.
