# H01/H02 Design R2 review package

Prepared 2026-11-11 from private PR #37 head `1198c2cd2d39f69a12e4f5abae727725b577593a`. Local branch `codex/h01-h02-design-r2`; no remote push, PR transition, merge, effective license, live report or public documentation edit.

## Decision requested

Approve Design R2 for both existing changes. Only CHECK-005/006 snapshot scopes and CHECK-006 lineage/diagnostic method change. Each excludes the exact archived sibling `tasks.md` from raw input hashing, while keeping its plans, all other dossiers and all actual source/test/configuration inputs. Independent canonical task approvals, schema, results, coverage and final delivery guards still enforce both changes. Final closure auditing stays separate from CHECK-006's execution; there is no self-result prerequisite.

| Change | Added exclusion in CHECK-005 and CHECK-006 | Coverage |
|---|---|---|
| H01 | specs/archive/contribution-security-guidance/tasks.md | 18 local + 6 retained obligations |
| H02 | specs/archive/portfolio-licensing-policy/tasks.md | 21 local + 14 retained obligations |

No scenario becomes optional or not-applicable. Terms and prior text approval are unchanged. No generic validator, schema, workflow, suite or new ADR is proposed. Proposal/Requirements remain approved. Tasks R1 plans are preserved with their original substantive digests; downstream reviews are superseded, approval fields cleared and current progress/evidence pending. Completed R1 records remain intact in r1-tasks.md. H02 is reopened to active storage only in this local candidate, preserving one dossier per ID.

## What was checked

- Both selected planning validators pass, with no findings/warnings on the final candidate.
- Disposable diagnosis: 16 observations reproduce both R1 cycles, show proposed evidence-only stability, retain source/sibling-design/sibling-requirement/unrelated-history sensitivity, detect substantive Tasks edits through canonical approval binding, and reject failed result records through the unchanged validator.
- These observations use the low-level input function to compare proposed scope behavior. They are Design diagnostics, not approved R2 CHECK execution or operational acceptance.
- All 59 scenario/regression mappings, twelve check identities/required flags, original Proposal and substantive Tasks digests are preserved.
- Full maintained package suite passed: 131 validator tests + 48 execution tests. That log precedes a final wording clarification separating CHECK-006 from the final closure audit; selected planning validators were rerun on the exact final documents afterward. No later full-suite execution is invented.
- Initial planning check retained as attempt-01-planning.json: historical completed progress triggered execution-approval requirements. Reopening progress to pending, preserving original completion in the historical ledger, corrected that bookkeeping. No required validation was removed.

## Current stage identities

### portfolio-licensing-policy

- proposal: `5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7`
- design: `5c77e32078568a63d9bde6361e72edd485c47dd10ca7ef7f1c490181720f920e`
- tasks: `ac2e801e4908448c2e534f8865970d979dbb751097b11b89532ee7a26299c138`

### contribution-security-guidance

- proposal: `6bed2e92d705d83385b31d27364cfcda2b05549678818801c6082132d6dbc8d2`
- design: `fa67e58e5e75d6d2e42757919b126690368d2654b25f48352eaf0a3b5f7ee844`
- tasks: `d969a531b3de153e562ff06d72c4ad0568b3a88caabbb52ca7b465bd05c2d284`

## Boundaries and next step

Remote Harness PR #37 and public .github PR #4 remain draft and unmerged, at their original reviewed heads. Their existing green/draft verification is not presented as joint R2 archive readiness. The public seven-file payload is unchanged; private evidence remains private.

Gate 2 approval unlocks preparation of Tasks R2. Only after applicable Tasks approval and execution authority can the affected actual checks be rerun, both dossiers archived, final guards/CI verified and existing PRs prepared for review. No merge or license application is included. The previous PVR/email facts are retained with their original limits; no new messages or synthetic submissions are needed solely to review this Design.

To reproduce the design diagnosis with Python validation dependencies installed: run diagnostic.py with three positional arguments: the clean R1 checkout at commit 1198c2c, this R2 candidate checkout, and an output JSON path. It copies R1 to a disposable directory, restores each probe and removes the temporary copy; it never edits the source checkouts.
