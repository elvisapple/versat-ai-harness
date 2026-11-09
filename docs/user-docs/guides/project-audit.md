# Audit a project

[English](project-audit.md) | [Português](project-audit.pt.md) | [Español](project-audit.es.md)

Use an audit to assess compliance, readiness or drift. Prepare repository instructions, .versat/project.yaml, .versat/standards.lock, active specifications and the selected provider. This is broader than an ordinary code review.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $project-audit to assess this repository against its declared profile and resolved Standards. Report evidence, severity and remediation options. Do not modify files.
```

## Expected result

Expect findings that distinguish verified compliance, non-compliance and unavailable verification, with affected contracts and concrete next steps. Deterministic validation supplies bounded evidence; qualitative review also considers security, tests/evals, documentation, operations and profile/criticality.

## Recovery and limits

Missing identity or provider context is a visible gap, not evidence of compliance. An audit request does not authorize remediation. Use maintenance or an SDD change to address approved findings.

## References

- [Skill (English)](../../../skills/project-audit/SKILL.md)
- [Standards index (English)](../../../standards/index.yaml)
- [Validators (English)](../../../validators/README.md)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
