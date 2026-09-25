---
change: bootstrap-product-context
status: implemented
owner: versat
summary: Guide product discovery during project bootstrap and generate a shared product overview
risk: low
---

# Proposal

## Context and problem

The bootstrap Skill collects repository identity but does not guide product discovery. The SDD directory convention already reserves specs/product/overview.md, yet there is no shared template or procedure to populate the strategic context needed by specifiers and implementers.

## Expected outcome

A developer bootstrapping a new repository receives guided questions and a reviewable product overview covering the twelve requested product topics, with supporting documents only when useful. Unknowns remain visible rather than becoming invented business facts.

## Scope

Update project-bootstrap and its lifecycle reference, add a focused discovery reference, and add a product overview to the composable base template. Connect the generated bootstrap proposal and README to the product context.

## Out of scope

Retrofitting existing projects, changing SDD approval gates, requiring a separate PRD, implementing product features, performing market research for this Harness change, changing validators, publishing a release, or updating installed consumers.

## Work tracking

No Shortcut Story was supplied. Use the local codex/bootstrap-product-context branch without inventing a Story identifier.

## Impact and risks

Product assumptions can appear authoritative when generated as polished prose. The discovery procedure separates supplied claims, evidence, hypotheses and gaps. Internal projects can explain why market or commission concepts do not apply. Skill changes remain subject to review before merge; local preparation does not claim remote approval.

## Proposal acceptance criterion

The Skill guides discovery, produces product-specific context or explicit gaps for all requested topics, and connects that context to bootstrap without duplicating Standards or profile templates.
