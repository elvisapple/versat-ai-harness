---
sdd_version: 3
change: welcome-message
requirements:
  - id: REQ-001
    statement: The existing English home page MUST show a short accessible welcome message on initial load while retaining existing content.
    acceptance:
      - Given the home page, when it loads, then the visible main content includes Welcome to the demo and the existing Home heading.
      - Given a visitor using a screen reader, when reading the main content, then the welcome is ordinary text in document order without requiring interaction or opening a dialog.
      - Given a page reload, when the content is shown again, then one welcome message is present without duplicate inserted copies.
---

# Requirements

## Actors and context

Visitors of the synthetic English static home page.

## Functional requirements

REQ-001 defines text, placement and initial-load behavior.

## Non-functional requirements

Preserve the page language and existing content. No implementation is part of this planning exercise.

## Acceptance scenarios

The frontmatter contains the observable scenarios for later Design mapping.

## Constraints and assumptions

index.html exists and was read before planning. This exercise uses the actual current Codex session, with no independent fresh-session or end-to-end UI claim.
