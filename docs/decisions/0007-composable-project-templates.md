# ADR-0007 — Compose templates from a base

- Status: Accepted
- Date: 2026-08-28

## Context

Complete templates for each profile would repeat common files and diverge over time.

## Decision

Define a `base` layer and incremental modules for each profile. An `agent` project is `base + agent`; a `hybrid` project is `base + software + agent`.

## Consequences

- common rules are maintained once;
- composition conflicts must be detected;
- the bootstrap must record which modules and versions were applied.
