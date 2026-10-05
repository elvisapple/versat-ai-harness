---
sdd_version: 3
change: payment-validation
requirements:
- id: REQ-001
  statement: Charge valid unique requests and reject invalid inputs.
  acceptance:
  - Valid unique requests return True.
  - Empty keys and nonpositive amounts raise ValueError.
- id: REQ-002
  statement: Preserve duplicate prevention.
  acceptance:
  - A repeated key returns False without another charge.
---
# Requirements
Synthetic payment behavior as listed in acceptance.
