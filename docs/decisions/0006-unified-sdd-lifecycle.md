# ADR-0006 — Adopt one SDD lifecycle for all profiles

- Status: Accepted
- Date: 2026-08-28

## Context

Separate processes for software, agents and infrastructure would duplicate governance and create inconsistent experiences.

## Decision

Adopt a single Versat SDD lifecycle. The project profile selects additional modules, documents and criteria but does not change the primary corporate workflow.

## Consequences

- every change has intent, specification, implementation, validation and review;
- agents are treated as versioned software with tests and evals;
- SDD must allow proportionality for small changes without removing essential controls.
