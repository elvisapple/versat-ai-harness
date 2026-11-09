---
sdd_version: 3
change: welcome-message
status: proposed
owner: documentation-walkthrough
summary: Add a short accessible English welcome message to the existing home page.
risk: low
impact:
  state: assessed
  summary: Extend the synthetic existing home page while retaining its heading and static loading behavior.
  items:
    - current_contract:
        change: welcome-message
        artifact: proposal
        locator: "## Current contract baseline"
      effect: extend
      targets: [REQ-001]
      reason: Retain the Home heading and show a short welcome on page load.
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream: {}
  approval: null
---

# Proposal

## Context and problem

The existing synthetic English static home page has a Home heading but no welcome message. This is the quickstart example, exercised locally by the current Codex session.

## Expected outcome

A visitor finds a short accessible welcome message in the main page content on load.

## Scope

Plan the visible English text Welcome to the demo. Preserve the existing heading and use normal readable text without a dismissible dialog.

## Out of scope

No product implementation, new language system, publication or retrospective approval.

## Work tracking

Synthetic documentation walkthrough. No real Story or issue is invented. Change ID: welcome-message.

## Current contract baseline

index.html is an English static document with a title Demo and a main element containing the heading Home. It has no dependencies or welcome message. Preserve that content while adding the requested message.

## Impact and risks

This bounded plan uses the current Harness source as its declared development provider. It does not claim a released consumer installation. A later Design should check reading order, visible text and preservation of existing content.

## Proposal acceptance criterion

Proposal and Requirements are ready for a real Gate 1 review. No approval has been supplied in this synthetic exercise.

## Planning review

Stop at Gate 1. Present Proposal and Requirements R1 for review; do not create Design, Tasks or change index.html.
