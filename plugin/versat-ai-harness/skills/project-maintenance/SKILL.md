---
name: project-maintenance
description: Bring an existing Versat repository forward by updating Harness artifacts, resolved Standards, templates or metadata through a reviewable migration. Use for upgrades and drift remediation, not new-project creation.
---

# Project Maintenance

## Workflow

1. Establish the current Harness version, project identity, lockfile and local deviations.
2. Identify the explicit target release; never migrate to an unspecified `latest`.
3. Read the target changelog and migration-relevant ADRs.
4. Compute a reviewable diff for Standards snapshots, Skills, templates and metadata.
5. Preserve valid project-specific content and surface conflicts instead of overwriting them.
6. Run profile-specific validation and summarize behavior changes.

Remote updates and Pull Requests require authorization. A successful migration records the exact target version and leaves no hidden local rewrite.
