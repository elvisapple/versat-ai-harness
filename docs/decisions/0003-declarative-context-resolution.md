# ADR-0003 — Resolve context through declarative metadata

- Status: Accepted
- Date: 2026-08-28

## Context

Asking each team to choose its Standards manually creates gaps and inconsistent combinations.

## Decision

Each project declares its profile, domain, criticality and technologies in `.versat/project.yaml`. The Harness resolves applicable documents through `standards/index.yaml` in this order:

```text
core + profile + domain + technologies + criticality
```

## Consequences

- the bootstrap experience remains simple;
- standards selection is reproducible and testable;
- the index becomes a critical contract and must be validated;
- exceptions must be explicit, justified and versioned.
