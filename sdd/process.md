# Versat Spec Driven Development

This is the canonical lifecycle for all profiles and execution adapters. The [developer guide](README.md) explains how to conduct it. The public [`versat-sdd` skill](../skills/versat-sdd/SKILL.md) routes to the phase procedures; it does not define a second process.

## Lifecycle and procedures

```text
Intent -> Proposal + Requirements -> approval -> Design -> approval -> Tasks -> approval
       -> explicit implementation request
       -> Implementation + living specifications -> Validation
       -> Documentary archive preparation in the same branch/PR
       -> PR review + final required checks -> Merge -> read-only delivery confirmation
```

| Phase | Canonical procedure | Exit condition |
|---|---|---|
| Planning | [New change](workflows/new-change.md) | Three current human approvals; no material unresolved decision. |
| Implementation | [Implement change](workflows/implement-change.md) | Approved tasks implemented, task progress truthful and living specifications consistent. |
| Validation | [Validate change](workflows/validate-change.md) | Requirement coverage and actual required check results recorded; failures and unknowns reported. |
| Documentary closure | [Archive change](workflows/archive-change.md) | Delivery checks pass and dossier prepared in the same branch; merge remains a separate external fact. |

Read and follow a procedure when entering its phase. These Markdown files are instructions, not commands that execute automatically. The same change can be resumed in another session; status-only requests do not authorize the next phase. Appropriate development checks are part of implementation. An explicitly requested implementation-and-validation workflow can continue between those phases without inventing a fourth planning gate.

## Context and artifacts

Use the project's selected Harness release, resolved Standards and applicable repository instructions. Resolve Standards through `standards/index.yaml`; do not reproduce Git, language, security or other policies here. Follow the resolved Git Standard for branches, commits, work tracking and PRs. Keep a real issue or Story reference when available; never invent one. Missing project/Standards context can be recorded while drafting intent, but must be resolved before accepting Design.

## Workflow terminology

The procedures in `sdd/workflows/` implement this development lifecycle. Consumer operational workflows compose Skills under the [Agent Artifact Standard](../standards/core/agent-artifacts.md); their definitions and changes pass through SDD but do not replace it. A workflow document describes execution and dependencies, not an automatically installed runtime.

## Directory convention

Every change has one stable lowercase hyphen-case ID and one dossier in either `specs/changes/<change-id>/` or `specs/archive/<change-id>/`. Never retain duplicate active and archive copies. The four primary files are:

- `proposal.md`: need, expected outcome, scope, exclusions, impact and the combined Proposal/Requirements review.
- `requirements.md`: stable requirement IDs and observable acceptance scenarios.
- `design.md`: requirement coverage, approach, relevant alternatives/risks, ADR references, planned checks and Design review.
- `tasks.md`: requirement-linked tasks, dependencies, completion conditions, Tasks review, actual validation evidence and documentary closure state.

Create only the current stage's files. A new change starts with Proposal and Requirements; Design and Tasks are absent until their upstream gate is approved. Templates and schemas in this release use the [v2 metadata contract](metadata.md). Drafts of necessary ADRs accompany Design. Current product/architecture documentation is updated with implementation, not to portray a proposed feature as delivered.

Small changes may use concise documents and explain why a concern is not applicable. Higher risk requires deeper alternatives, rollout, rollback and observability analysis. Proportionality changes depth, not the gates or traceability.

## Human gates

1. **Gate 1 — Proposal/Requirements:** present both files and their shared revision; approval unlocks Design.
2. **Gate 2 — Design:** present the approach, planned checks and related ADRs for the current upstream revision; approval unlocks Tasks.
3. **Gate 3 — Tasks:** present task coverage, dependencies and completion checks; approval completes planning.

At each gate, present links to the actual files, stage/revision, concise decisions and assumptions, blockers or “none,” and one approval request. End the turn and wait for the human response before creating or advancing later-stage content. A valid approval refers to the presented revision; a short “approved” works when the stage is unambiguous. Conditional approval remains pending until the revised result is presented and accepted. Initial blanket permission, silence, checkboxes, passing validators, an agent opinion and unsupported status labels are not approvals of unseen artifacts.

The developer approves in the chat; the agent maintains structured review metadata and records the actual approval source and quote. Never invent an approver, timestamp or source. An approved record must match the current stage digest and upstream approvals. Metadata is an auditable record, not cryptographic proof that a person approved it. Where stronger assurance is required, the platform's trusted review evidence remains authoritative.

Approval of Tasks alone ends planning. After reviewing the current Tasks revision, the developer may explicitly combine its approval and implementation authorization in one reply. An earlier request to implement an unplanned intent does not bypass any gate: after the plan is presented, obtain the current Tasks approval and clear execution instruction. PR publication, merge and deployment require their own scoped authorization and repository controls; planning approval does not replace PR review.

## Revisions and resumption

On resumption, reconcile actual artifacts, available conversation evidence and current digests. Reuse the same ID. Missing or ambiguous evidence means the corresponding gate is pending; re-present it instead of synthesizing history. A current valid approval does not need to be requested again simply because the session changed.

When approved scope or design changes, increment the earliest affected stage's revision, clear its current approval, and reopen its gate. Retain historical review evidence in the review section and mark downstream reviews `superseded`; do not revise downstream content until its prerequisites are approved again. Requirements changes reopen Proposal/Requirements, Design and Tasks. Design changes reopen Design and Tasks. Task-plan changes reopen Tasks. Validation evidence based on a superseded plan cannot establish readiness.

The digest contract conservatively treats content edits as revisions. Only its explicit normalization/bookkeeping exclusions avoid renewed approval; do not silently replace an approval digest after an “editorial” content change. Check results, task progress and completion checkboxes can change without reapproving the plan. Changes to referenced ADR decisions must also be reviewed with Design; the local digest only binds the reference, not the contents of every linked file.

Routine implementation fixes within the approved approach do not require replanning, but applicable checks must be rerun after code changes. Distinguish a planned check, an actual result, local readiness, remote CI, merge and deployment. Unknown evidence remains unknown.

## Documentary archive and delivery

Update living specifications alongside implementation. After validation, prepare the dossier under `specs/archive/<change-id>/` in the implementation branch and the same PR. Documentary closure requires current approvals, no blockers, completed tasks, current evidence and passing required checks. Recheck references and final checks after the move.

`closure: prepared` or archive storage means the dossier is prepared for delivery review. Neither means merged, approved remotely or deployed. A draft PR can already exist. If review requires changes before merge, keep the same ID and branch, reopen affected reviews and rerun checks; move the dossier back to active storage when replanning. An archived/prepared dossier that no longer meets delivery conditions must fail validation until corrected.

The merge brings implementation, living specifications and the dossier onto the default branch together. Confirm merge/check status from actual Git/PR evidence afterward without requiring a repository write. Do not embed a document's own final commit or merge SHA as a mandatory field. The tested revision/run and eventual merge commit are different facts. If remote evidence is unavailable, report delivery as unverified.

Administrative closure of an already governed change references that change and does not recursively require another functional SDD change. An existing legacy change may need a maintenance PR for migration/closure. New functional work after delivery gets a new change ID; preserve delivered history.

## Validation and legacy adoption

Use the [SDD validator](../validators/sdd/README.md) with `planning`, `implementation` or `delivery` phase as appropriate. Planning allows missing later-stage files; implementation requires the complete approved plan; delivery additionally requires completion and actual evidence. `fail` and `unable-to-verify` both prevent a readiness claim. Archive location and prepared closure enforce delivery eligibility even in the default planning check.

Exact legacy dossiers may be grandfathered through the explicitly reviewed manifest described in [metadata](metadata.md#legacy-dossiers). That exemption preserves history and is never proof of current approvals or readiness. Starting or resuming execution on a legacy dossier requires a reviewable v2 migration with real approval/evidence records. Do not fabricate retrospective approvals or silently weaken gates to make CI pass.
