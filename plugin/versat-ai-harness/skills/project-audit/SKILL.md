---
name: project-audit
description: Assess a Versat repository against its declared profile, resolved Standards, SDD state and readiness contracts. Use for compliance, readiness or drift reviews, not ordinary code review.
---

# Project Audit

## Audit method

1. Read `.versat/project.yaml`, `.versat/standards.lock`, repository instructions and active SDD changes.
2. Resolve the expected context with `standards/index.yaml` and compare it with the lockfile.
3. Run deterministic validators before making qualitative judgments.
4. Evaluate required documentation, security, tests, evals, observability and operations according to profile and criticality.
5. Report findings by severity with evidence, affected contract and a concrete remediation path.

Do not change the audited repository unless remediation was explicitly requested. A successful audit distinguishes verified compliance, non-compliance and items that could not be verified.
