# Maintain an existing project

[English](project-maintenance.md) | [Português](project-maintenance.pt.md) | [Español](project-maintenance.es.md)

Use maintenance for upgrades or drift in an existing repository. Supply the current identity/lockfile, explicit target release, local deviations and maintained validation commands.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $project-maintenance to compare this repository with the exact target Harness release I supplied. Preserve local changes, present migration conflicts and a rollback plan, and do not publish remote changes.
```

## Expected result

Expect a reviewable difference covering Standards snapshots, templates, capability references and metadata. Classify consumer artifacts before relocating them. Preserve custom wrappers and tests. Validate against the target provider; record the exact adopted version and integration results.

## Recovery and limits

If no target is supplied, resolve it before modifying pins; never use latest. Surface conflicts instead of overwriting them. Roll back configuration and provider references together, then run the restored original suite.

## References

- [Skill (English)](../../../skills/project-maintenance/SKILL.md)
- [Changelog (English)](../../../CHANGELOG.md)
- [Migration (English)](../../../project-templates/README.md)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
