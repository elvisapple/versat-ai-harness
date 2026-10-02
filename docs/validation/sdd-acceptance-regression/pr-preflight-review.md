# Pre-PR archival enforcement review

The developer requested review and correction of the missing enforcement before completing the authorized archival. This is a correction of the existing lifecycle precondition, within the existing validator/workflow/CI boundaries.

## Gap and correction

The process already required documentary archival before submitting completed implementation for PR review. Plain delivery validation intentionally also worked while the dossier remained active, because it supplies the pre-move eligibility check. CI selected changed archive paths only, so a completed active dossier could pass all checks without ever reaching that selection. The PR template merely said archival was required when applicable.

The `--require-archive` preflight now requires selected dossiers in archive storage, Tasks `closure: prepared` and live delivery readiness. It works with an explicit change without Git; baseline selection covers affected active and archived dossiers, including removed paths. Combining selectors checks their union. Empty selection, missing dossiers and missing baseline fail. Unchanged history is still inventory.

Archive/validation workflows require the preflight before publication or marking a draft ready. The PR template records the archive path, closure and result. CI supplies the guard for non-draft PRs, ready-for-review transitions and pushes to main; planning/incomplete draft PRs keep inventory behavior. Required platform checks remain necessary to block merge. CI detects a noncompliant PR after creation; it cannot prevent every client from creating one.

## Observed checks

- The actual completed active dossier was rejected with `ARCHIVE_REQUIRED` and `CLOSURE_REQUIRED`: [before-move result](prearchive-guard.json).
- Eleven new regression cases cover completed-active rejection, both storage/closure prerequisites, live stale evidence, unfinished tasks/missing results, baseline selection of active dossiers, draft planning, missing/empty selection, deletion, unchanged unrelated plans, CLI digest misuse and draft/ready CI command dispatch.
- All 125 tests passed before archival: [package check](package-check-before-archive.txt). The seven-step behavioral walkthrough also ran again against the revised validator.
- The one-line relocation-safe Proposal link correction was explicitly authorized by the developer after its diff was presented. Proposal review retains the original digest and the actual authorization quote; its current binding is updated. Design/Tasks substantive digests are unchanged, their upstream reference is rebound, and the reviewed in-flight compatibility entry records the administrative exception. Requirements and historical dossiers remain unchanged.
- The final [delivery preflight](delivery.json), [baseline archive selection](archive-selection.json), [package check](package-check.txt) and [document audit](document-audit.json) record the actual post-move result. No PR, remote CI, merge or release is claimed.

This correction introduces no automatic approval of future editorial changes. The one-line exception applies only to the amendment presented and authorized in this conversation.
