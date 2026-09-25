---
change: bootstrap-product-context
tasks:
  - id: TASK-001
    description: Add guided discovery and bootstrap handoff instructions
    requirements: [REQ-001, REQ-003, REQ-004]
    status: completed
  - id: TASK-002
    description: Add the composed product overview template and navigation
    requirements: [REQ-002, REQ-004]
    status: completed
  - id: TASK-003
    description: Validate the Skill, links, composition and acceptance scenarios
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
    status: completed
---

# Tasks

- [x] TASK-001 — Add discovery guidance and connect product context to bootstrap.
- [x] TASK-002 — Add the shared overview and template documentation links.
- [x] TASK-003 — Run validation and record evidence.

## Dependencies

Skill review and required checks precede merge. No Story identifier was supplied. The user authorized publishing the branch and opening a Pull Request after local validation.

## Validation evidence

- `./scripts/validate/run.sh`: portable Plugin package and Harness structural validation passed.
- Skill Creator `quick_validate.py skills/project-bootstrap`: passed.
- `git diff --check`: passed. New and modified Markdown files also passed a whitespace and YAML frontmatter check.
- All 11 local Markdown links in the changed files resolve.
- All five profile manifests inherit base; none duplicates the product overview.
- Manual REQ-001/REQ-002 review: the Skill reads the discovery guide and shared template, reuses briefs, asks short rounds, permits deferred answers and retains all twelve product topics. Optional files require useful content and links.
- Manual REQ-003 review: market guidance requires units, scope, periods, dated evidence and formulas; distinguishes volume and revenue; and permits reasoned non-applicability for internal products. Unknown data is not synthesized as fact.
- Manual REQ-004 review: the bootstrap proposal links to product context, product ambitions remain distinct from delivery commitments, and structural readiness is reported separately from product review.
- These are structural checks and manual instruction reviews, not an end-to-end agent evaluation or validation of actual market data. No executable behavior changed; no new unit tests were added.

## Delivery gates

Local implementation and validation are complete on codex/bootstrap-product-context. Human review, remote required checks, merge and release remain separate delivery steps. Installed consumers retain their exact current references. Keep this change active until the canonical archival conditions are satisfied.
