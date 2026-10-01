---
change: consolidate-sdd-workflow
status: implemented
owner: versat
summary: Consolidate the Versat SDD entry point, workflows, documentation and local validation contract
risk: high
---

# Proposal

## Context and problem

The Harness had overlapping `new-change` and `versat-sdd` skills, four workflow documents with no visible routing contract, a post-merge archive interpretation, and no validator for the SDD review and evidence model. Developers could not reliably tell which procedure to invoke or what a recorded archive asserted.

## Expected outcome

One public `versat-sdd` skill routes developers through the four canonical workflow documents. It makes planning gates, implementation authority, documentary archival and local validation limits explicit. The repository checks the new v2 metadata contract while preserving exact immutable historical dossiers without claiming retrospective approval.

## Scope

- document one SDD entry point, four workflow contracts and the developer-facing lifecycle guide;
- remove the standalone `new-change` skill after incorporating its planning-gate behavior;
- add versioned templates, schemas and deterministic local validation for new dossiers;
- use same-branch documentary archival and retain a separate read-only merge confirmation;
- preserve pre-v2 history through a byte-exact, explicit legacy allowlist;
- add tests, CI dependency setup and a decision record for the governing architecture.

## Out of scope

- creating a workflow engine or automatically invoking documents as commands;
- authenticating a reviewer, fetching remote CI, checking pull-request state, or asserting a merge/deployment;
- changing release version, marketplace pins, branches, tags or remote pull requests.

## Impact and risks

The new contract intentionally requires validation dependencies and changes how new SDD dossiers are recorded. The archived directory remains a documentary state, so users must not treat it as remote delivery proof. Historical dossiers cannot receive fictitious approvals; an exact allowlist makes that limitation visible.

## Proposal acceptance criterion

The repository offers one unambiguous SDD entry point, describes all lifecycle handoffs, validates new dossier consistency and evidence readiness locally, and keeps only explicitly identified historical exemptions.
