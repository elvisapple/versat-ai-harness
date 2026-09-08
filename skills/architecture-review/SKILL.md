---
name: architecture-review
description: Review a proposed or implemented Versat architecture for boundary clarity, Standards compliance, operability, risk and decision traceability. Use when architectural judgment or an ADR is in scope.
---

# Architecture Review

Locate the installed Plugin root two directories above this file. Review the relevant SDD proposal, requirements and design against the Plugin root [SDD process](../../sdd/process.md) and [Standards index](../../standards/index.yaml) before the implementation details.

Check:

- ownership and system boundaries;
- data, trust and authorization boundaries;
- failure modes, recovery and observability;
- deterministic versus model-driven responsibilities;
- compatibility and migration strategy;
- alignment with resolved Standards;
- whether durable tradeoffs are represented by ADRs.

Lead with material risks and evidence. Separate required corrections from optional improvements. Do not approve a design merely because documents exist; confirm they agree with observable behavior.
