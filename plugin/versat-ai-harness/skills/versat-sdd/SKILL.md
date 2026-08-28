---
name: versat-sdd
description: Specify and deliver a Versat project change through proposal, requirements, design, tasks, implementation, validation and archival. Use for material product, agent, infrastructure or policy changes.
---

# Versat SDD

Use `sdd/process.md` as the canonical lifecycle and the matching artifacts in `sdd/templates/`.

## Outcome

Produce a change directory whose documents stay consistent with one another and with the implementation. Scale detail to risk, but never omit intent, acceptance criteria or validation.

## Rules

- Start from observable need and scope, not a preferred implementation.
- Resolve applicable Standards before design.
- Record alternatives and significant tradeoffs in design; create an ADR for durable structural decisions.
- Keep tasks independently verifiable and update their status truthfully.
- Run tests, evals and validators required by the project profile.
- Archive only after implementation, validation and living specifications agree.
- Do not mutate remote branches or Pull Requests unless the user authorized that workflow.
