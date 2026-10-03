---
name: project-maintenance
description: Bring an existing Versat repository forward by updating Harness artifacts, resolved Standards, templates or metadata through a reviewable migration. Use for upgrades and drift remediation, not new-project creation.
---

# Project Maintenance

## Workflow

1. Locate the installed Plugin root two directories above this file and establish its exact Harness version from [VERSION](../../VERSION).
2. Establish the target project's current Harness version, identity, lockfile and local deviations.
3. Identify the explicit target release; never migrate to an unspecified `latest`.
4. Read the target [changelog](../../CHANGELOG.md) and migration-relevant ADRs from the matching Plugin package.
5. Compute a reviewable diff for Standards snapshots, Skills, templates and metadata using the matching [template migration guidance](../../project-templates/README.md). Classify existing artifacts before relocating them; distinguish consumer content from Plugin exports and application source.
6. Preserve valid project-specific content and surface conflicts instead of overwriting them. For validation adoption, follow the optional validation section of the same template guide, retaining custom test wrappers and a reviewed rollback.
7. Run profile-specific validation and summarize behavior changes, including affected capability references and executor loading. Record integration checks that could not be performed instead of treating package validation as consumer readiness.

Remote updates and Pull Requests require authorization. A successful migration records the exact target version and leaves no hidden local rewrite.
