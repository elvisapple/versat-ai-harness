# Approved evaluator migration and test retirement

This implements Design R3's explicit deferral of the unshipped autonomous CLI/protected-CI responsibilities. Existing historical results and source/plan identities remain in this evidence directory; none is relabeled as supervised behavior.

| Prior test/asset | Current disposition |
| --- | --- |
| `test_all_fixtures_have_valid_synthetic_plans` | Retained/strengthened as supervised fixture validity and actual stale-evidence checks; development snapshot identity is explicit |
| `test_final_answer_alone_cannot_pass_grading` | Retained as rejection of narrative-only runner observations and independent artifact/replay review |
| `test_rewriting_plan_and_approval_cannot_pass` | Retained as comparison to captured plan identity even after an attacker rehashes approval |
| `test_case_deadline_also_bounds_independent_grading_process` | Replaced by a real timeout of bounded independent replay, retaining incomplete observations |
| `test_parser_requires_observations_not_final_answer`, `test_parser_retains_failed_command_and_usage` | CLI JSONL parser removed; no automatic native transcript or usage accounting is claimed |
| `test_missing_runtime_does_not_invoke_model`, `test_missing_transport_credential_is_unverified`, `test_adapter_restricts_command_environment_and_arguments` | CLI transport/auth adapter removed; supervised unavailable observations remain explicit and ordinary runner environment tests remain |
| `test_budget_exhaustion_preserves_unverified_result` | Automatic scheduler removed; coordinator monitors the reviewed case/suite limits and retains attempts |
| `test_unavailable_sandbox_is_not_a_live_success`, `test_independent_replay_uses_sandbox_without_credentials` | CLI/outer sandbox removed; shared permissions stated explicitly; bounded command replay and safe-path/link checks retained |
| Deterministic CI baseline/archive branch test | Retained, plus missing-baseline rejection, exit propagation and actual consumer full-suite failing-regression execution |
| Draft eligibility/label changes, fork/dispatch checks, live aggregate, environment reviewer checks, current head/label recheck, CLI eligibility entry point and protected workflow dependency tests | Removed together with the never-published privileged workflow and `scripts/eval/ci.py`; no replacement successful skip or secret-bearing job exists |
| `scripts/eval/fixtures.py` and reusable grader logic | Moved/reworked into `tests/skills/fixtures.py` and `verification.py`; mutation replays use separate copies and do not alter original artifacts |
| `scripts/eval/{run,codex,ci}.py`, runtime schema and `.github/workflows/skill-evaluations.yml` | Removed from active delivery, not kept as unverified optional functionality |

All retained runner, consumer, SDD, regression and governance assertions remain. New helper tests cover fresh-directory refusal, source/control changes, deficient test coverage, real retained failure, output overlap and symlinks. Independent replay exposed a runner bug: resolving a venv interpreter symlink before launch selected the base interpreter. The runner now preserves the invocation path while recording the real executable, with a real-venv regression test. Counts may change because responsibilities changed; complete current suite execution remains mandatory.
