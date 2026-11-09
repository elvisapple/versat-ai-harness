# Review architecture

[English](architecture-review.md) | [Português](architecture-review.pt.md) | [Español](architecture-review.es.md)

Use this review when system boundaries, architectural risks or an ADR are in scope. Supply Proposal/Requirements, Design, current architecture, related ADRs and applicable project context.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $architecture-review to review this proposed design against the current architecture and resolved Standards. Lead with material risks, evidence and necessary ADR decisions. Do not implement changes.
```

## Expected result

Expect evidence-backed findings on ownership, trust/data boundaries, failure and recovery, operations, compatibility and migration. Separate required corrections from optional improvements. Significant tradeoffs belong in reviewable ADRs; a file’s existence does not prove the decision is sound.

## Recovery and limits

Missing architecture or conflicting specifications must be reported before relying on the design. Keep policy, capabilities, lifecycle and enforcement responsibilities distinct. Review does not grant implementation or publication authority.

## References

- [Skill (English)](../../../skills/architecture-review/SKILL.md)
- [Architecture (English)](../../architecture/overview.md)
- [ADRs (English)](../../decisions/README.md)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
