---
sdd_version: 3
change: payment-validation
requirements:
- REQ-001
- REQ-002
adrs: []
validation:
- id: CHECK-001
  description: Run new and retained payment tests
  requirements:
  - REQ-001
  - REQ-002
  required: true
  method:
    kind: automated
    procedure: Run /private/tmp/versat-sdd-acceptance-venv/bin/python /Users/elviszoz/.codex/worktrees/6f00/versat-ai-harness/scripts/testing/run.py
      run --root . --change payment-validation --check CHECK-001; require current
      payment assertions to pass.
  inputs:
    include:
    - src
    - tests
    - .versat/validation.yaml
    - .versat/project.yaml
    - .versat/standards.lock
    - specs/product
    exclude: []
  outputs:
  - docs/evidence
  execution: local
coverage:
- scenario:
    requirement: REQ-001
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-001
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-002
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
regression:
- obligation:
    impact: 1
    scenario: 0
  checks:
  - CHECK-001
  rationale: Retain duplicate-prevention assertion.
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: f7bf7b19f5b28c7cf238c22001cd53702b54d4d7fe09c536adb03375b56dd741
  approval:
    source: Synthetic evaluator fixture, not a real developer approval
    quote: Synthetic approval for this disposable scenario only
    revision: 1
    digest: 6fe31e98cb168331b3ade5b0f486c63953a28dd7c114968bef84ade54d8dd9b2
---
# Design
Reuse the maintained suite and add missing boundary/error coverage. Use the explicit full runner and record actual evidence.
