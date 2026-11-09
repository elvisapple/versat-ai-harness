---
sdd_version: 3
change: project-bootstrap
requirements:
- id: REQ-001
  statement: The fixture MUST compose base and software assets and expose explicit
    readiness gaps.
  acceptance:
  - Given the empty fixture, when composed, then product context, identity and exact
    Standards lock exist without fabricated application readiness.
---

# Requirements

The documentation reviewer is the sole synthetic user. Application generation and deployment are excluded.
