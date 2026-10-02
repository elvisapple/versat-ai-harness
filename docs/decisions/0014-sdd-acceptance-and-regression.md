# ADR-0014 — Bind SDD acceptance and retained behavior to current validation evidence

- Status: Accepted
- Date: 2026-10-01
- Related: ADR-0004, ADR-0006, ADR-0009, ADR-0011, ADR-0013
- Change: `sdd-acceptance-regression`, Design R1
- Decision evidence: The developer approved the presented Design R1 and ADR-0014 together in the development conversation on 2026-10-01 with “Sim, aprovado.” This accepts the architectural decision and unlocks Tasks planning; it does not authorize implementation, PR publication, merge or release.

## Context

Harness 0.3.0 validates requirement/check/task relationships and recorded evidence. It also requires meaningful acceptance-scenario coverage, but scenario dispositions and related historical behavior are not explicit machine-checkable records. Tasks can appear complete while behavior remains incomplete. A plan digest cannot detect a changed implementation, and historical passing results cannot establish a new change's regression safety.

Archived requirements explain origin rather than automatically defining today's contract. Rechecking every old result against current code would invalidate history after legitimate later changes. Conversely, skipping current delivery checks merely because a dossier moved into the archive would weaken the existing lifecycle.

## Decision

Introduce SDD metadata v3 within the same four primary artifacts and public skill. Proposal owns reviewed impact; Requirements retain their acceptance arrays; Design maps local and retained historical scenarios to checks; Tasks records executions, semantic assessments and findings. Reference scenarios by existing requirement and array position bound to the reviewed revision. Qualify historical references by source change and source Requirements digest.

Preserve a maintained current baseline independently of historical origin. For retained or extended behavior, require current regression evidence from active project tests/evals or justified explicit checks. For intentional supersession, review the replacement contract and associated test changes. Missing historical coverage becomes current work without rewriting delivered dossiers.

Use deterministic input snapshots for local freshness: hash reviewed file/directory scopes before and after checks and compare them again for live readiness. Stage digests cover current dossier intent; exclude evidence outputs and the current dossier from raw input hashing to avoid circular results and archive-move invalidation. Input selection is reviewed, not automatically inferred as complete. External state and execution authenticity remain outside the local proof.

Semantic assessment by an agent or reviewer identifies missing, partial, contradictory and unrequested behavior. Deterministic validators enforce the declared mappings, states, safe references and local freshness. Neither layer substitutes for observed execution, required CI or human review. Corrections follow ADR-0013's current authorization and revision gates rather than automatically changing approved Tasks.

Separate historical archive inventory from live delivery assessment. Inventory preserves record consistency under its original contract without asserting current behavior. Selected delivery always checks current evidence; CI additionally selects new/modified archive dossiers using its trusted base revision and runs live delivery checks. Missing selection context must not become a false readiness pass.

Support older records explicitly: preserve pre-v2 exceptions; inventory immutable v2 history by exact hashes and allow specifically reviewed v2 in-flight plans to finish only under their captured approved stage digests and original controls. New work defaults to v3. Exemptions state their limits and are not automatically generated for failures. Source references may read old requirements without migrating their history. Consumers adopt an exact release through review.

The introducing change itself finishes under the bounded v2 in-flight rule, with real stage digests recorded after Gate 3. This avoids rewriting already approved artifacts while implementing their replacement contract. New guarantees are verified in synthetic v3 dossiers and behavioral walkthroughs; its v2 dossier is not described as mechanically satisfying v3.

## Alternatives

- Prose-only review retains low overhead but cannot enforce declared scenario coverage, origin resolution or local freshness.
- A global scenario/test registry duplicates existing sources and requires a broader product contract than this change needs.
- Commit-only freshness misses working-tree changes and binds unrelated edits; scoped content snapshots cover declared inputs without requiring a self-referential commit field.
- Revalidating every archived dossier against current code confuses historical evidence with preserved current behavior.
- Optional unversioned fields or silent v2 strengthening make enforcement and compatibility ambiguous.
- Automatic corrective-task append bypasses existing task-plan approval semantics.

## Consequences

- Developers get explicit requirement/scenario dispositions and auditable regression selection across changes.
- Check-scoped snapshots detect changes within declared local inputs, including added/deleted files, but cannot detect omitted dependencies or authenticate a remote run.
- CI needs trusted baseline selection in addition to archive inventory. Archive location still proves neither merge nor deployment.
- Authoring and review gain structured records; many-to-many mapping, existing IDs and reusable evidence limit duplication.
- New schema/digest dispatch and bounded compatibility require regression fixtures and clear migration documentation.
- Standards, SDD, Skills and validators retain their separate policy, process, routing and enforcement responsibilities. The repository's existing architecture documentation will describe delivered changes during implementation, not present this proposal as current behavior.
