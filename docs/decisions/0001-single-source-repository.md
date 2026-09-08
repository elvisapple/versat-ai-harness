# ADR-0001 — Use a single repository as the source of truth

- Status: Superseded by ADR-0011
- Date: 2026-08-28

## Context

Plugin, Standards, SDD, templates and validators evolve together and must remain consistent. Separating them prematurely would create coordinated releases, distributed discovery and divergence risk.

## Decision

Keep all Versat AI Harness components in a single versioned repository. The package under `plugin/versat-ai-harness/` is the installable Plugin root within this repository.

## Consequences

- cross-cutting changes can be reviewed atomically;
- the Harness version identifies a consistent set of artifacts;
- internal boundaries must remain explicit to avoid improper coupling;
- future separation into packages remains possible when a demonstrated need arises.
