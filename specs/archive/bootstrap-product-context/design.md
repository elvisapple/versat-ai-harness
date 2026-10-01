---
change: bootstrap-product-context
requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
adrs: []
validation:
  - Harness structural and Plugin validation
  - Skill frontmatter validation
  - Local Markdown link and whitespace checks
  - Manual acceptance scenario review
---

# Design

## Current state and resolved context

The project-bootstrap Skill references version-matched schemas, Standards and templates, but its intake is limited to project identity. Base templates have no product content. All profiles compose base, and SDD already reserves a product overview independently of change documents.

standards/index.yaml selects the core language, documentation, Git, security, testing and observability Standards for all work. This Harness change has no declared project manifest; do not invent a profile or domain. Applicable architecture guidance is docs/architecture/overview.md, ADR-0006, ADR-0007 and ADR-0011.

## Proposed design

Add project-templates/base/specs/product/overview.md as the single topic and output template. Add skills/project-bootstrap/references/product-discovery.md for conversational discovery, evidence handling, market calculation guidance, optional document splitting and handoff review. The Skill entrypoint loads this reference during every new-project bootstrap and links generated product context into the initial SDD proposal. Its lifecycle reference and the base README expose the same path.

The overview retains all twelve requested topics. Unknowns and reasoned non-applicability are valid documented outcomes. Optional research.md, strategy.md and product requirements.md are generated only from useful collected content; their detail is linked instead of copied into multiple maintained documents.

## Boundaries and contracts

The Skill defines the capability, the base template defines the generated artifact, and existing Standards and SDD retain their authority. No architectural boundary changes or new ADR are needed. No questionnaire is copied into each profile or into Standards. Product narrative remains distinct from accepted change requirements and implemented behavior.

## Data, security and permissions

Use the resolved documentation and security Standards for supplied customer context and external research. This change adds no credentials, external service dependency, remote mutation or approval bypass. Generated documents identify sourced evidence separately from developer assertions and hypotheses.

## Operations, rollout and rollback

Review as a Skill/template change and release through the existing versioned process. Keep VERSION, marketplace references and consumer pins unchanged during local preparation. Existing repositories are not rewritten. A reviewed revert restores the previous bootstrap behavior.

## Alternatives considered

- Add a mandatory PRD alongside the existing documents: unnecessary duplication for this request.
- Embed the full questionnaire in the Skill entrypoint: increases loaded instructions and duplicates the generated template.
- Require market research before creating any repository: blocks early discovery and internal projects without improving evidence quality.
- Add a validator matching headings: does not establish meaningful answers, market validity or useful guidance; leave content checks explicit and manual.

## Validation plan

Run ./scripts/validate/run.sh, the skill-creator quick validator and git diff --check. Resolve local Markdown links, review template composition and walk through the acceptance scenarios. Record the distinction between structural verification, manual instruction review and an actual end-to-end agent evaluation.
