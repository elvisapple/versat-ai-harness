# Implementation validation

Local implementation and validation completed on 2026-10-01 on `codex/sdd-acceptance-regression`, based on `ac69894d94461f7e891dc817bd9ec81498978d0a`. All nine approved tasks and all six Design checks have observed local evidence. Documentary closure is prepared in `specs/archive/sdd-acceptance-regression/` with `closure: prepared`, after the developer-authorized link correction and pre-PR enforcement repair. Selected live delivery and trusted-baseline archive preflight both passed. No PR, merge, release or consumer update is claimed.

## Tested source and commands

The [input manifest](inputs.json) records 167 repository source files and SHA-256 fingerprint `a80442368084187f5f8f6ab8686824edb2b94830c19c849e41742584de0e4778`. It was verified unchanged across the final checks. Its explicit scope excludes this report/output directory, the current dossier's bookkeeping and Python caches; the dossier is separately bound to its approved Design/Tasks digests and explicitly authorized administrative Proposal link amendment. This is the introducing v2 change's working-tree evidence, not a claim that its dossier passed v3 checks.

Python 3.11+ validation dependencies were installed in the isolated `/private/tmp/versat-sdd-acceptance-venv` environment from the repository's pinned dependency file. Actual runtime details and command output are in the [walkthrough](walkthrough.json) and [package check](package-check.txt).

```sh
PYTHON=/private/tmp/versat-sdd-acceptance-venv/bin/python ./scripts/validate/run.sh --baseline origin/main --require-archive
PYTHONDONTWRITEBYTECODE=1 /private/tmp/versat-sdd-acceptance-venv/bin/python tests/validators/review_sdd_walkthrough.py --output docs/validation/sdd-acceptance-regression/walkthrough.json
```

The package entry point passed, including **125 tests**: 48 retained v2 cases under explicit fixture compatibility and 77 v3/behavioral cases. The suite now also replays the executable reviewer fixture. That automation does not turn the separately assessed workflow into an autonomous-agent evaluation.

`origin/main` resolved locally to the stated base commit. A separate run with an unavailable base returned exit 1 and `BASELINE`, as expected; synthetic Git cases checked new/modified/removed archives and both sides of moves. The workflow supplies event-derived base data with full checkout history, quoted as an argument. Required suite execution remains unconditional after SDD validation. Remote GitHub execution is unverified.

## Approved check outcomes

| Check | Observed result and supporting evidence |
|---|---|
| CHECK-001 | Pass. Strict v3 fields, scenario positions, many-to-many mappings, missing/duplicate/out-of-range coverage, approved exclusions, complete tasks with missing assessments, failure/unverified aggregation and semantic gaps are exercised in the suite and reviewer payment case. |
| CHECK-002 | Pass. Qualified origins, equal REQ IDs, active/archive moves, missing/changed sources, baseline-only impact, split dispositions, maintained duplicate prevention and reviewed supersession are exercised. Actual payment success passes while duplicate behavior fails before correction; the unchanged retained test passes afterward. |
| CHECK-003 | Pass. Before/after/current input checks detect code, test, fixture and config edits; additions/deletions, missing roots and executable flags are covered. Unsafe paths/symlinks/special files/conflicting outputs fail. Evidence output edits and narrow/broad archive moves preserve snapshots. Historical inventory remains distinct from live readiness. |
| CHECK-004 | Pass. Draft/gate/approval behavior, finding reuse/resolution, changed task planning, missing baseline and archive completion are covered. Exact v2 history/in-flight bindings reject changes, unknown/overlapping exceptions and mixed records. Original legacy records and v2 schemas are byte-identical to the base. |
| CHECK-005 | Pass as a recorded reviewer walkthrough. Seven observed steps execute positive/error/boundary/duplicate behavior, repeat validation without code edits, correct within the existing task, detect stale resumption/new task scope, inspect no-impact/manual cases, retain unavailable verification and execute approved synthetic replacement behavior. [Reviewer assessment](reviewer-walkthrough.md) maps all acceptance positions and states the limits. |
| CHECK-006 | Pass locally. Complete package/suite run; source/input/stage digest helpers, planning/implementation/selected delivery and baseline CLI cases; schema-compatible four-file templates; unchanged base composition/exact-release adoption; local links, byte preservation and diff checks. Remote CI and PR review remain separate unobserved gates. |

[Document audit](document-audit.json) records local link resolution and comparison of 39 existing history/schema files. A final diff whitespace check passed. The original pre-v2 manifest, legacy artifacts, archived quickstart dossier and v2 schemas remain unchanged. No source work remained outside the approved scope.

## Trust and delivery limits

The [reviewer walkthrough](reviewer-walkthrough.md) assesses the behavior and workflow; the package check enforces declared records. Neither proves arbitrary test adequacy, unlisted dependency coverage, authenticated execution or human identity. Before/after hashes cover selected inputs; external service/runtime changes still require observed context and appropriate reruns.

This change uses its approved v2 in-flight compatibility entry, so its selected delivery pass is expressly limited to that contract. New v3 assurance is demonstrated by the v3 fixtures and observed behavior; no retrospective approval or pass is fabricated. Historical inventory alone does not establish current delivery readiness. CI, mandatory PR review, merge, release publication and consumer adoption have not been observed or claimed.

## Pre-PR enforcement and final archival

The [pre-PR review](pr-preflight-review.md) records the enforcement gap, the explicit administrative link authorization and eleven new regression cases. Ordinary delivery remains the pre-move check; `--require-archive` checks the mandatory archive location, prepared closure and live readiness before submitting completed implementation. Non-draft PR CI, draft-to-ready transitions and main pushes enable the guard with affected active/archive baseline selection. Draft planning remains supported. The initial active dossier correctly failed this guard; final records show its post-move outcome.
