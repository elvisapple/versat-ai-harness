# ADR-0009 — Keep the Harness executor-independent

- Status: Accepted
- Date: 2026-08-28

## Context

Standards and SDD have a longer lifespan than any specific agent, IDE or vendor.

## Decision

Treat the Codex Plugin, CI/CD, CLI and future integrations as execution adapters over the same versioned core. The Marketplace distributes capabilities but is not the source of authority.

## Consequences

- new executors can reuse Standards, SDD and validators;
- specific integrations cannot contaminate canonical contracts;
- the first adapter will be the Codex Plugin, without preventing others.
