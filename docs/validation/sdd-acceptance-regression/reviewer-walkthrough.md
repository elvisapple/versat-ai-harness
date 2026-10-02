# Acceptance and regression reviewer walkthrough

This records a local reviewer walkthrough on 2026-10-01, using disposable projects and synthetic data. It is **not** an autonomous-agent evaluation or a remote CI run. Synthetic approval records exercise gates; they are never offered as human approval evidence. The actual human approvals for this Harness change remain in its own dossier.

The [reproducer](../../../tests/validators/review_sdd_walkthrough.py) executes real Python payment assertions, captures results and input hashes, applies the bounded correction and checks resulting records. The reviewer inspected the implementation diff, plan references and canonical workflow instructions. [Observed output](walkthrough.json) contains commands, assertions, exit statuses, before/after hashes, findings, final fixture artifacts and validator reports. Reproduce with:

```sh
PYTHONDONTWRITEBYTECODE=1 python tests/validators/review_sdd_walkthrough.py --output /tmp/sdd-review.json
```

## Observed behavior

| Step | Action and evidence | Outcome |
|---|---|---|
| 1. Validate complete tasks | Execute positive-payment, invalid-amount and duplicate-request assertions; inspect the broken implementation. | Positive payment passes. Negative/zero amounts and repeated requests fail. All task boxes are complete, but acceptance fails. The reviewer also identifies disabled auditing and an unrequested synthetic export. |
| 2. Repeat validation only | Record three stable findings, validate twice and compare source hash. | Failure remains visible, the source is unchanged and the finding count remains three. There is no appended corrective task. |
| 3. Correct within approved task | Add amount validation and duplicate protection, remove unrequested code, retain the exact maintained test file and rerun all three checks. | Old evidence is first detected as stale. New executions all pass, snapshots match, findings have explicit resolutions, task-plan digest is unchanged and selected delivery passes. |
| 4. Resume/change planning | Change execution configuration after the pass; separately propose a task description outside the approved scope. | Configuration edit produces unable-to-verify. Task edit produces stale approval and blocks dependent implementation. The experiment restores the unchanged approved plan; it does not invent a renewed human approval. |
| 5. No-impact | Inspect the isolated greeting fixture and its scope with no affected prior contract. | Assessed empty impact is accepted. The reviewer grounds this conclusion in the tiny project; the validator does not discover all real dependencies. |
| 6. Manual/unavailable | Review the documented source literal with a justified method and actual source observation; then model a required executable absent from the disposable project. | Manual review is recorded with observed matching snapshots. The unavailable execution remains unverified, rather than passed or excluded. |
| 7. Supersede intentionally | Use a synthetic approved replacement of Hello world with Welcome; edit source and execute the replacement assertion. | Welcome passes, the replacement requirement/check is explicit and the historical origin bytes remain unchanged. Supersession retires obsolete behavior for a reason, not to hide a failing retained test. |

The payment origin is a synthetic archived Requirements record used for reference resolution. It does not claim a real old payment release or historical execution. Complete archived dossiers, byte-bound v2 history, unchanged legacy records and CI live-selection behavior are covered by the separate deterministic suite. The duplicate test stays in `tests/` and its file hash is unchanged through correction; nothing moves it into the archive.

## Workflow review

The reviewed procedures preserve the three human gates and the same public skill. New-change requires scenario mappings and current-contract impact; implementation maintains regression suites; validation compares each scenario with implementation, not task boxes; archival runs live selected delivery before and after moving the dossier. The canonical Testing Standard retains full required CI suites alongside selected regressions.

Validation-only is expressly limited to diagnostics/evidence. The recorded first step performs no product mutation. The authorized correction uses the existing task, while new task scope triggers the existing Tasks gate. These observations demonstrate the executed reviewer procedure and deterministic boundary checks; they do not establish how every autonomous agent will respond in a new conversation.

## Requirement/scenario review

The notation below uses the unchanged acceptance array positions in this change's approved Requirements. Deterministic cases live in [the v3 suite](../../../tests/validators/test_sdd_v3.py); established controls remain in [the v2 suite](../../../tests/validators/test_sdd.py). The [validation report](validation.md) records the current complete run.

| Requirement positions | Evidence and assessment |
|---|---|
| REQ-001/1–3 | Missing boundary mapping fails; many-to-many reuse passes; approved exclusions require reasons and are not counted as passes. Steps 1–3 demonstrate why positive-path success cannot establish full acceptance. |
| REQ-002/1–4 | Steps 1–3 observe partial/contradictory/unrequested code despite completed tasks; step 6 preserves unavailable execution. Individual assessments and aggregate outcomes remain separate from executed checks and record validation. |
| REQ-003/1–4 | Steps 1–4 retain source during validation-only, correct under existing task authority, reject new task content and reuse findings. Tests cover resolved/dangling/duplicate findings and upstream reopening. |
| REQ-004/1–5 | Payment preserves a qualified archived origin against an explicit current baseline. Tests resolve equal REQ IDs in distinct changes, disjoint dispositions, missing/digest-changed origins and unresolved current baselines. Steps 5/7 cover grounded no-impact and reviewed replacement. |
| REQ-005/1–5 | Actual positive-payment success coexists with duplicate failure; the same maintained regression test passes after correction. Methods/rationales and profile CI obligations remain explicit; manual/unavailable and supersession are observed in steps 6/7. No failing retained test was deleted. |
| REQ-006/1–4 | Execution uses before/after/current input hashes and an unchanged task-plan digest. Tests cover code/test/config/fixture-root edits, additions/deletions, executable flags, missing paths, changed requirements, evidence exclusions and broad/narrow archive moves. Step 4 demonstrates stale resumption. Historical/reference authenticity limits remain explicit. |
| REQ-007/1–4 | Strict schemas and tests cover duplicate/dangling/ambiguous mappings, failure/unverified/missing/stale outcomes and partial drafts. CLI scope explicitly withholds proof of semantic adequacy, execution authenticity, human identity and remote state. |
| REQ-008/1–5 | Historical bytes and original manifests/schemas are compared with the Git baseline. v2 compatibility and v3 positive/negative tests pass. Guide examples use the same public skill/four files; maintained regression and missing-source work stay with the new change. Consumer templates still extend base and adoption remains an exact-release maintenance action. |

The introducing dossier deliberately remains v2 under its approved in-flight exception. This review supplies semantic evidence about its implementation; its v2 validator result does not claim v3 certification. Remote CI, PR review, merge, release and consumer adoption have not been observed here.
