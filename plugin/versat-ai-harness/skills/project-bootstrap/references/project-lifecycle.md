# Project lifecycle

```text
Request
  -> classify
  -> validate identity and conflicts
  -> create local repository skeleton
  -> resolve Standards
  -> initialize SDD
  -> document architecture and operation
  -> generate profile-specific modules
  -> run readiness checks
  -> prepare bootstrap PR
  -> human review
  -> activate project
```

Minimum identity fields are name, description, owner, profile, domain, criticality and visibility. Infrastructure, data classification and integrations become required when the proposal makes them relevant.

Do not treat remote setup as implicit permission. Local materialization and read-only discovery may proceed; GitHub organization mutations require the relevant authorization.
