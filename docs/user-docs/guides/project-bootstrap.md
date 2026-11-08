# Bootstrap a project

[English](project-bootstrap.md) | [Português](project-bootstrap.pt.md) | [Español](project-bootstrap.es.md)

Use bootstrap for a new or empty project. Supply its purpose, owner, profile, domain, criticality, technologies and exact Harness provider. Existing repositories with content use maintenance instead.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $project-bootstrap for this empty repository. Reuse the supplied product brief, ask about missing identity, and present a reviewable skeleton and product context. Do not create remote repositories or PRs.
```

## Expected result

Expect a composed base/profile skeleton, specs/product/overview.md with evidence gaps, .versat/project.yaml, an exact .versat/standards.lock and a project-bootstrap SDD change. The provider index resolves Standards; users do not choose a subset of mandatory policy. Review product assumptions before treating them as requirements.

## Recovery and limits

An empty scaffold does not prove a usable application. Record unavailable runtime checks and avoid empty guides or fictional runnable steps. Conflicting existing content means stop and classify the repository before composing templates.

## References

- [Skill (English)](../../../skills/project-bootstrap/SKILL.md)
- [Templates (English)](../../../project-templates/README.md)
- [Project schema (English)](../../../schemas/project.schema.yaml)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
