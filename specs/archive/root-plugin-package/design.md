---
change: root-plugin-package
requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
adrs: [ADR-0001, ADR-0002, ADR-0004, ADR-0009, ADR-0011]
validation:
  - Repository structural validator
  - Codex compatibility Plugin validator
  - Portable manifest and marketplace JSON validation
  - Semantic version consistency check
  - Git whitespace check
---

# Design

## Current state

`plugin/versat-ai-harness/` contains the compatibility manifest and Skills. The Skills depend on canonical artifacts located at the repository root, but installation copies only the nested package. The installed result is therefore structurally valid but functionally incomplete outside the source checkout.

## Proposed design

Treat the repository root as the portable Plugin root:

```text
versat-ai-harness/
├── plugin.json
├── .codex-plugin/plugin.json
├── skills/
├── agents/
├── standards/
├── sdd/
├── project-templates/
├── schemas/
├── validators/
└── .agents/plugins/marketplace.json
```

The portable manifest is the canonical package identity. The compatibility manifest mirrors its version and OpenAI presentation metadata. Portable component discovery loads `skills/` from the package root.

The marketplace catalog references the repository root through a Git URL pinned to `v0.2.0`. The catalog itself is imported by a workspace administrator, who configures installation policy for eligible roles in workspace administration.

## Boundaries and contracts

- `standards/` remains the only policy authority.
- `skills/` contains capabilities and procedures that locate canonical artifacts; it does not restate policies.
- `sdd/` remains the lifecycle authority.
- `validators/` remains deterministic enforcement.
- `agents/` contains reusable role guidance and is not a policy authority.
- `plugin.json`, `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` are distribution adapters over those boundaries.

## Data, security and permissions

The package contains internal governance content already present in the private repository. Workspace import must use an approved GitHub account with read access. The Plugin declares no MCP server or external app, so it adds no service credentials or connector permissions.

## Operations and observability

Validation checks required paths, JSON syntax, semantic versions, manifest agreement, marketplace pinning, supported Skill frontmatter and absence of tracked legacy package files. CI runs the same entry point on Pull Requests and `main`.

## Migration, rollout and rollback

1. Merge the governed change.
2. Create the exact `v0.2.0` tag.
3. Import the repository marketplace in workspace administration.
4. Configure `Installed` for the intended roles.
5. Ask users to start new conversations after installation.

Rollback consists of selecting the previous workspace Plugin version or reverting the marketplace import. Consumer repositories remain protected by their existing lockfiles.

## Alternatives considered

- Move canonical directories under `plugin/versat-ai-harness/`: rejected because executor-independent content would become subordinate to a Codex adapter directory.
- Generate copied snapshots inside the nested package: rejected for the current scale because it introduces avoidable packaging and drift controls.
- Keep the incomplete nested package: rejected because installed Skills cannot reliably resolve their required canonical artifacts.

## Validation plan

Run the repository validator, the compatibility Plugin validator, JSON and YAML syntax checks, shell syntax validation and `git diff --check`. Inspect the resulting tracked tree to confirm that the former nested package no longer contains files.
