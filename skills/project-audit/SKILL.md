---
name: project-audit
description: Assess a Versat repository against its declared profile, resolved Standards, SDD state and readiness contracts. Use for compliance, readiness or drift reviews, not ordinary code review.
---

# Project Audit

## Audit method

1. Locate the installed Plugin root two directories above this file.
2. Read `.versat/project.yaml`, `.versat/standards.lock`, repository instructions and active SDD changes from the target project.
3. Resolve the expected context with the Plugin root [Standards index](../../standards/index.yaml) and compare it with the lockfile.
4. Run applicable deterministic validators from the Plugin root before making qualitative judgments.
5. Evaluate required documentation, security, tests, evals, observability and operations according to profile and criticality. Review project artifacts against the resolved contracts, distinguishing package layout from consumer layout and declared dependencies from verified execution readiness. Record checks without a deterministic validator as manual or unverified.
6. Report findings by severity with evidence, affected contract and a concrete remediation path.

Do not change the audited repository unless remediation was explicitly requested. A successful audit distinguishes verified compliance, non-compliance and items that could not be verified.
