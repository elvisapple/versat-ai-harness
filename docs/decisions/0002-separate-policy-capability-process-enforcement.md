# ADR-0002 — Separate policy, capability, process and enforcement

- Status: Superseded by ADR-0011
- Date: 2026-08-28

## Context

Corporate rules hidden in Skills might not be loaded. Agent instructions are also not a sufficient guarantee for mandatory controls.

## Decision

Separate responsibilities:

- `standards/`: canonical policies;
- `plugin/versat-ai-harness/skills/`: capabilities and procedures;
- `sdd/`: change process;
- `validators/` and CI: deterministic enforcement.

Skills reference Standards but do not duplicate them.

## Consequences

- policies remain auditable even without a specific executor;
- Skills remain small and are loaded on demand;
- critical rules require validators or platform controls;
- changes may require coordination between guidance and enforcement.
