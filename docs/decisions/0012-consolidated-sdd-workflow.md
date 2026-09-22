# ADR-0012 — Consolidate SDD routing and prepare documentary closure before merge

- Status: Accepted
- Date: 2026-09-22
- Related: ADR-0006, ADR-0009, ADR-0011
- Decision evidence: the repository owner reviewed the consolidation proposal in the development conversation and requested, “Ok implemente as mudanças propostas.” This approves the design direction and implementation, not a PR review, merge or release.

## Context

The full-cycle `versat-sdd` Skill and the added `new-change` Skill both offered planning, but only the latter specified three human gates. The canonical process and public Skill did not explicitly route to the four workflow documents. Gate behavior consequently depended on the entry point selected.

The previous archival procedure required an already merged implementation and then changed versioned files, including living specifications. Persisting those edits required another delivery cycle and delayed documentation consistency. Package validation did not validate the SDD schemas, approval records, traceability or closure readiness.

## Decision

Expose a single public `versat-sdd` Skill. It resolves context, intent and the target change, then reads the matching canonical workflow. Keep four workflow documents for planning, implementation, validation and documentary archive preparation. Move the useful `new-change` gates and resumption behavior into `sdd/` and remove the duplicate Skill. The developer guide lives at `sdd/README.md`.

Require three current human planning approvals: Proposal/Requirements, Design and Tasks. Store schema-defined review records bound to artifact content. Approval of Tasks alone does not authorize implementation; a developer may explicitly approve a presented plan and request implementation in one message. Neither planning approval nor local validation substitutes for PR review or authorizes remote mutations.

Update living specifications alongside implementation. Prepare the documentary archive in that same branch/PR after validation; check paths and evidence after the move. The dossier on an unmerged branch remains revisable. Its directory and documentary status never prove a merge or deployment. Confirm delivery from actual platform/Git evidence without requiring another repository edit. Administrative archival references the original change instead of creating a recursive functional change.

Introduce versioned SDD metadata and stage-aware local validation. Keep the four primary specification files; task evidence stays with Tasks. A schema check can establish recorded consistency, not whether a claimed human approval or remote run is authentic. Report external uncertainty explicitly.

Preserve old dossiers through a reviewed allowlist of exact content hashes and the original schemas. An exception is not approval evidence and cannot establish new implementation/delivery readiness. The transitional consolidation dossier records the already reviewed proposal and present authorization without fabricating three retrospective artifact approvals. Subsequent changes use the new contract.

## Alternatives

- Four public skills delegating to the same core: valid, but adds selection overhead without providing additional phase semantics.
- Keep independent full planning instructions in both skills: rejected because approvals and revisions can drift.
- Strict post-merge archive: valid if the organization accepts a later maintenance PR, optionally batched. It is not the chosen default.
- Derive closure solely from a stable folder and a GitHub integration: avoids moves, but needs a broader state/query integration than this change.
- Enforce new gates retroactively on all history: rejected because unknown historical approvals must not be manufactured.

## Consequences

- One discoverable entry point and one canonical process; workflows remain reusable by other executors.
- Code, living specifications and the documentary archive can enter the default branch atomically through one delivery PR.
- Checks cover structured records and traceability, while operational trust remains with review and platform controls.
- Local/CI validation requires the declared Python dependencies; failures and unavailable verification are distinguished.
- Existing released version pins remain unchanged. Publishing this behavior requires a separately reviewed versioned release; no cache mutation or silent consumer upgrade is part of this decision.

This decision refines lifecycle execution without replacing the single-cycle, executor-independent and package-boundary decisions in the related ADRs.
