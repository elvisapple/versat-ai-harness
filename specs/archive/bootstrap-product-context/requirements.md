---
change: bootstrap-product-context
requirements:
  - id: REQ-001
    statement: Guide the developer through missing product context during bootstrap
    acceptance:
      - Existing briefs and answers are reused before asking focused follow-up questions
      - Deferred topics become explicit gaps with next validation steps
      - The developer receives a reviewable draft without implied acceptance
  - id: REQ-002
    statement: Generate a shared overview covering all requested product topics
    acceptance:
      - Every profile inherits the overview from the base template
      - Pitch, value proposition, problem, solution, origin and customers or users are covered
      - Market size, investment timing, competition, innovation, scalability and social and environmental considerations are covered
      - Substantial supporting material is linked from the overview without duplicate maintained content
  - id: REQ-003
    statement: Preserve evidence quality and applicability in product discovery
    acceptance:
      - TAM, SAM, SOM and take rate include their calculation basis or explicit gaps
      - Market estimates distinguish customer counts, transaction volume and revenue
      - Internal projects can record reasoned non-applicability instead of fabricated market data
      - Facts, supplied claims, hypotheses and unresolved questions remain distinguishable
  - id: REQ-004
    statement: Connect product context to SDD while preserving existing governance boundaries
    acceptance:
      - The bootstrap proposal references the overview and relevant supporting content
      - Product ambitions are not automatically promoted to implementation tasks
      - Standards remain resolved through the index and templates remain composable
      - Validation reports distinguish structural checks from product evidence and review
---

# Requirements

## Actors and context

Developers supply or refine the product context. The bootstrap agent generates the repository skeleton and documents. Specifiers, implementers and reviewers consume the shared context.

## Acceptance scenarios

- A developer supplies a complete brief: the agent maps it into the overview and asks only about gaps or contradictions.
- A developer supplies only an idea: the agent asks short rounds of related questions and records deferred market research without blocking skeleton creation.
- A commission-based product includes market estimates: the agent records units, scope, period, sources, assumptions and formulas, and does not apply take rate twice to revenue.
- An internal library has no external market: the overview retains the requested topics, explains non-applicability and captures internal users and value.
- A detailed competitor study warrants research.md: the overview keeps a summary and a working relative link to the maintained detail.
- A product ambition is still a hypothesis: it remains product context rather than a committed bootstrap implementation task.

## Constraints and assumptions

This is an instruction and template change. It introduces no remote repository operations, automated market research service, new metadata schema or deterministic content validator. Generated product specifications follow the resolved language policy.
