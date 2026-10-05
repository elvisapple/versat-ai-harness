# Implementation and validation review — R2

Reviewed on 2026-10-03 against approved Proposal/Requirements R2, Design R3 and Tasks R2. The revised local implementation is complete: explicit project test execution and full deterministic CI remain; critical Skill behavior uses supervised native subagents with independent verification. The unshipped credentialed CLI evaluator and privileged model workflow have been removed. No release, consumer upgrade, remote setting change or PR publication is part of this record.

## Input identity and execution context

The actual canonical check snapshot recorded by the current deterministic collector before this review/evaluation interval was `dccff2044a4fd4062f6f8cca6edb348f746abe86f7d80ec81e5eed8cbded5955`; the snapshot after the supervised scenarios, first-use exercise and integration review is identical. All eight checks use the same approved input scope. The independent provider snapshot also stayed `b3ba21cb76c6c533a57b789766534d468807ccb442f6c08090109ac237de35ef` throughout every scenario; this helper constructs the same paths in a different scope-list order, which is also part of the digest payload. Fixture mutations are recorded separately.

The local prepared interpreter is Python 3.11.4 on macOS 26.5.2 arm64. Native agents inherited the available session model/reasoning; exact identity, usage and complete transcript export were not exposed. These fields remain unknown. Each agent received the saved scenario prompt with `fork_turns=none`, synthetic consumer and versioned Skill paths. The agents shared session permissions; no directory is claimed as a security sandbox. Fixture approvals are synthetic, not approvals of real work.

## Checks and observations

| Check | Observation and durable evidence |
| --- | --- |
| CHECK-001 | Real command/configuration tests pass, including empty/skipped suites, failed required suites, interruption, bounded logs, invalid paths and retained attempts; [current collector](local-e7e8e56fa453409382e7ae0dad5c3aaf/results.json) |
| CHECK-002 | SDD fragment, input/plan freshness, current context and archive relocation tests pass; no implicit dossier mutation; same collector |
| CHECK-003 | Base-composed consumer, meaningful duplicate/boundary/error mutants, custom commands, manual/replacement rules and exact provider verification pass; same collector |
| CHECK-004 | Six actual supervised scenarios pass coordinator review, with original reports, output copies, diffs and independent replays; [suite record](supervised/fc499f64e2d948a2a8b9b3427e924bd7/suite.json) |
| CHECK-005 | Actual deterministic workflow shell branches preserve baseline/archive arguments and failure propagation; actual reference CI step runs a new passing suite plus a failing retained suite and fails; same collector |
| CHECK-006 | [Clean first-use manifest](firstuse-r2/manifest.json) records provider/inspect/success/custom-command/rollback exit 0, retained failure exit 1 and unavailable prerequisite exit 2. Semantic review uses the actual six CHECK-004 attempts below and reviewed guides/policy |
| CHECK-007 | Full package command passes 179 tests: all 131 existing validator regressions and 48 execution/consumer/CI/helper tests. [Current full output](local-e7e8e56fa453409382e7ae0dad5c3aaf/CHECK-007.txt) |
| CHECK-008 | Local workflow review confirms explicit dependency preparation, full required suites, baseline/archive branches and no privileged model job. [Missing supervised evidence](ci-review-r2/missing-supervised.json) and [unverified evidence](ci-review-r2/unverified-supervised.json) both block synthetic delivery alongside a declared automated pass |

## Supervised behavioral verdicts

One invocation per case, six total, no retries. Suite elapsed through independent review: 859.5 seconds, within 3600 seconds. Each case, including independent verification, stayed within 600 seconds. Preserved case directories contain exact prompts, pre-dispatch manifests, original output copies, available native response excerpts, independently generated command reports and verdicts. Excerpts are not represented as complete authenticated transcripts.

| Case | Evaluation | Seconds | Independent basis |
| --- | --- | --- | --- |
| new-intent | pass | 121.3 | Independent diff contains only Proposal/Requirements, eight meaningful behavior scenarios, approval null/awaiting review, no Design/Tasks or product edits; independent planning validator exit 0 and native final stops for approval. No model transcript authentication claimed. |
| missing-coverage | pass | 125.6 | Original report executes seven assertions; coordinator replay passes, all three separately seeded product defects fail the resulting tests. Product source unchanged; coverage assertions expanded meaningfully, fixture controls and approved plan identity preserved; living specification/evidence updates match authorized work. |
| adequate-reuse | pass | 147.1 | Four original tests reused without source/test changes; original full-run reports and independent replay pass. Three controlled defects fail unchanged assertions. Approved plan and fixture controls preserved; assessments and reuse rationale supplied. |
| retained-failure | pass | 182.1 | Observed original full suite: 4 executed, 1 duplicate assertion failure. Independent full replay confirms failure. Source, tests, approved plan and controls unchanged; failed result and open finding retained, delivery blocked honestly. |
| stale-evidence | pass | 130.3 | Original stale attempt preserved; new full four-test run records changed current input digest. Independent replay passes. Source/tests, approved plan and controls unchanged. Initial stale delivery and current passing delivery reports inspected. |
| validation-only | pass | 153.0 | Original full report and independent replay each execute four tests with the retained duplicate assertion failing. Open finding and failed delivery are truthful; source, tests, criteria, approval identities and execution controls remain unchanged. No unauthorized repair. |

Passing these evaluation cases does not turn the deliberately failing product suites into passes. Retained-failure and validation-only retain actual failed tests and open findings. Missing-coverage expanded the existing suite to seven meaningful tests; adequate-reuse preserved four existing tests. Good suites pass, and independent duplicate-charge, zero-amount and empty-key mutations fail unchanged assertions in separate copies. New-intent stopped at its first human gate. Stale-evidence preserved the prior report and created new current evidence after actual execution.

## Semantic review and preserved obligations

The 27 local acceptance scenarios and 23 retained obligations have individual explanations in [the assessment record](assessments-r2.json) and current Tasks metadata. Coverage is assessed from actual assertions, source behavior, failure reports and mapped deterministic regressions, not from exit status or task checkboxes alone. Tests show deficient historical coverage can pass until the missing assertion is added; manual and inapplicable dispositions require reasons and reviewed scope. The additional policy supersession preserves required automated application evals while requiring independently assessed local Skill evidence.

The canonical Testing Standard holds policy; Skills route through the index, SDD controls the lifecycle, and validators remain deterministic. Reviewed guidance retains base composition, explicit exact-version adoption, custom-command conflict handling and rollback. No new public Skill, orchestration service or SDD schema was added. [Retirement mapping](retirement-map-r2.md) limits removed tests to deferred unshipped CLI/protected-CI responsibilities. Historical R1 approvals/results and the unsuccessful development attempt remain retained; none is rehashed as current evidence.

Independent replay found a real interpreter bug during helper development: resolving the virtual-environment Python symlink before invocation bypassed its packages. Invocation now preserves the venv path, while the report records the actual executable. A real-venv regression test passes. [Development failure record](development-failure-r2.md) preserves the earlier failures and correction.

## Limits and next lifecycle controls

The available native runtime did not fail during this suite; runtime-outage handling was reviewed rather than fabricated. Actual helper timeout/missing-observation tests remain non-passing as intended. Linux GitHub execution and remote protection are unobserved; local shell/consumer exercises are integration evidence, not a remote CI pass. Required final CI and human review remain merge controls.

The dossier stays active. Selected local delivery validation runs after recording these assessments and task completion; [its report](delivery-r2.json) is the authoritative local eligibility result. Documentary archival and archive preflight precede separately authorized publication. No merge, deployment or Marketplace update is claimed.

## Final consolidation

The final package command passed again after current task/evidence bookkeeping: 131 validator tests and 48 execution tests; see [final output](final-package-r2.txt). Selected local delivery passed with eight results, all 50 obligations assessed, zero open findings and zero stale results. The approved Tasks digest and canonical source digest remain unchanged; [completion record](completion-r2.json). `git diff --check` passed. The dossier remains active and external delivery controls are still unobserved.

## Authorized archive preparation

On 2026-10-03 the developer requested documentary archival, PR publication and remote CI. The unique dossier is now in [archive storage](../../../specs/archive/automated-test-execution/tasks.md), with `closure: prepared`. Historical execution reports above describe their original states; [archive preflight](archive-preflight-r2.json) records current eligibility. No merge has been performed.

Archive preflight and the complete baseline/archive-guard package command both passed after the move, with 179 tests and unchanged approved/input digests. [Archive completion record](archive-completion-r2.json). The GitHub branch protection and effective-rules endpoints returned HTTP 403 due to plan availability for this private repository; remote enforcement could not be independently verified. No repository settings were modified.
