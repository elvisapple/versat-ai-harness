# Synthetic first-use report

## Scope and outcome

One bounded first-use attempt on `payment-fixture`, 2026-11-13. The supplied
installed `versat-sdd` skill from Harness 0.4.0 routed to the new-change workflow.
The resolved Standards index matches all 12 lockfile paths and their SHA-256
file digests. Only Proposal and Requirements R1 were authored for
`payment-validation-tests`; their review is `awaiting-approval`, with null
approval and no blockers. No Design or Tasks exist. No source, test, product
specification, provider or configuration edits were made.

## Observed checks

The single selected planning-validator execution returned exit 0 and `pass`,
no findings or warnings, eight local scenarios and one retained regression
obligation. `planning-validator.json` preserves the observed JSON result.
`file-manifest.json` records current input and artifact hashes.

Command executed from the supplied installed provider:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/versat-pr36-validation-venv/bin/python validators/sdd/validate.py --root /private/tmp/harness-personal-client-03/first-use --change payment-validation-tests --phase planning --json
```

No validator rerun or behavioral retry occurred. Two exploratory combined
reads returned exit 1: one requested the absent `docs/validation` directory;
one guessed `.json` schema filenames where the package uses `.yaml`. The
actual schema filenames were discovered from directory entries and read.
Those read-only discovery failures did not change artifacts or hide a failed
validation attempt.

## Unavailable or deliberately unperformed observations

- No real human approval was observed or recorded. Synthetic fixture ownership
  is not evidence of a real approver or authority.
- Application tests were inspected, not executed. The planning pass is not
  payment acceptance evidence or implementation/delivery readiness.
- Active/archive origin dossiers were absent before this change. The living
  product specification is the preserved baseline; historical origins remain
  unavailable.
- The synthetic target has no project validation shell script or Git metadata.
  Branch controls, real issue association, CI, PR review, merge and deployment
  were not verified. The provider-wide validation suite was not invoked for
  this consumer-only planning stage.
- No external connectors, network operations, credentials or production data
  were used. Fresh agent context and this temporary directory do not establish
  security isolation. Low-level model/runtime telemetry and independent
  external enforcement observations are not available to this report.

## Gate handoff

Present both actual artifact files as Proposal/Requirements R1. Scope preserves
existing behavior and proposes stronger tests, including negative amounts,
state preservation and duplicates with changed positive amounts. Assumptions
are explicit: existing code supplies ValueError/state semantics and this
scenario uses string keys and integer amounts. Blockers: none.

Request approval of Gate 1 R1 from the coordinator's real reviewer. Do not
manufacture approval evidence. Approval permits Design only; no further stage
has been started. Stop after this handoff.
