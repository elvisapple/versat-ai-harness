---
change: align-language-standard
status: implemented
owner: versat
summary: Align repository artifacts with the canonical language standard
risk: medium
---

# Proposal

## Context and problem

The repository was bootstrapped with technical documentation in Portuguese and SDD templates in Spanish. These artifacts conflict with `standards/core/language.md`, which requires English for technical and structural content.

## Expected outcome

All existing repository artifacts use the language required for their artifact class, while explicitly allowed Spanish corporate content remains unchanged.

## Scope

- audit every tracked file for language-policy compliance;
- translate legacy technical and structural content to English;
- preserve the internal Pull Request template in Spanish;
- reconcile the historical language ADR with the canonical standard;
- validate repository and Plugin contracts.

## Out of scope

- changing technical behavior or repository architecture;
- updating consumer repositories;
- publishing a release or opening a remote Pull Request;
- introducing automated natural-language detection.

## Impact and risks

The change is mechanically broad but behaviorally low risk. The main risks are translation drift, broken references and accidental changes to contracts embedded in documentation.

## Proposal acceptance criterion

The repository contains no known language-policy violations, permitted Spanish content is preserved and all applicable validation passes.
