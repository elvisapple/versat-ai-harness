# Archive change

Use to prepare documentary closure in the implementation branch/PR, or to confirm delivery read-only after merge. Read the [process](../process.md) and [metadata](../metadata.md). Archive storage is a documentary state; it is not proof of merge or deployment.

## Prepare documentary closure before merge

Prerequisites: authorized preparation, current planning approvals, no material blockers, completed tasks, consistent living specifications and actual passing required checks. Run `--change <change-id> --phase delivery` using the [SDD validator](../../validators/sdd/README.md). Failure or inability to verify blocks a readiness claim and the archival move. An exact legacy exemption is not enough; migrate with real records before closure.

1. Review the implementation and living specifications against the approved scope and recorded evidence. Preserve history, actual approval records, stable IDs and ADR links. Resolve unfinished required work; do not relabel it as future work merely to pass closure.
2. Move the unique dossier from `specs/changes/<change-id>/` to `specs/archive/<change-id>/` in the same working branch. Set Tasks `closure: prepared`. Keep evidence at stable locations and update affected repository links. Do not create a second copy or fabricate a merge record.
3. Recheck all affected references and rerun the applicable checks, including SDD delivery validation, on the resulting branch content. A changed plan/link that participates in a digest follows the normal reapproval rules; prefer stable references to avoid needless invalidation. Report readiness only after the final checks pass.
4. Prepare the delivery summary. If a draft PR already exists and publication is authorized, use that same PR. Otherwise publish only when authorized. Keep PR review and final required CI checks as separate delivery requirements.

An unmerged archived dossier remains revisable in the same change and branch. Review fixes rerun the affected checks; material planning changes reopen the relevant gates and can move the dossier back to active storage with `closure: active`. Archive location/prepared closure enforces delivery eligibility, so a dossier with newly stale approvals or evidence fails until corrected. Do not treat the prior archival move as permission to bypass review.

## Confirm delivery after merge

When asked to check delivery, inspect actual Git/PR merge evidence and final check status read-only. Confirm the relevant branch/PR and distinguish merged, unmerged, failed and unverified. If evidence is unavailable, report that limitation; do not infer merge from `specs/archive/`, completed tasks, a proposal status or local validator success. Deployment remains a separate fact.

Merge brings code, living specifications and the dossier to the default branch together. No mandatory second branch, commit or PR is needed to write that the first PR merged. Do not require a self-referential final commit SHA in the dossier. Preserve recorded tested revisions/runs; the platform records the actual merge result.

Administrative migration/closure of existing changes can use a reviewed maintenance PR without recursively creating another functional SDD change. New behavior or an out-of-scope defect after delivery starts a new change ID. Preserve the delivered dossier's history.

## Handoff

Report dossier location, documentary closure, local validation results, PR/review status when observed, and the next authorized delivery step. Say “prepared for review/merge” before merge; say “merged” only with actual evidence. Do not silently perform merge or deployment.
