# Supervised Skill evaluations

Use this procedure when the approved change requires real Skill behavioral evidence. A native scenario subagent exercises the version-matched `versat-sdd` Skill; a coordinator independently checks the resulting artifacts and tests. Deterministic fixture/helper tests and code reviews alone do not establish that behavior.

## Prepare one scenario

Use a prepared Python 3.11 environment with `requirements-validation.txt`, a supported local process runtime and an available native collaboration interface. Review the approved scenarios, limits, verification steps and source revision. The explicit project runner described in [Project validation](project-validation.md) remains the way to execute tests and retained regressions.

From the selected provider checkout, create a fresh synthetic consumer:

```sh
python tests/skills/fixtures.py --case new-intent --output /tmp/versat-new-intent
```

Use a new empty directory each time. The command prepares files, not an agent evaluation. Fixtures use synthetic data and clearly labeled synthetic approvals for applicable cases; they never approve real work. Their Standards lock identifies a development source snapshot, not an unpublished clean release. Installed consumers still require reviewed exact-version adoption.

Capture the case prompt from `tests/skills/cases/`, the fixture manifest using `tests/skills/verification.py`'s `snapshot`, and the provider/check input digest before delegation. In the native collaboration interface, start one fresh agent with no inherited implementation conversation (`fork_turns: none` in this session's adapter). Supply only the absolute fixture path, absolute `skills/versat-sdd/SKILL.md` path, prepared Python executable, scenario prompt, allowed local work and stopping limits. Keep mutation answers and reviewer criteria outside that prompt. Ask the agent to return artifact/report paths and any unavailable observations.

The native agent uses the session's existing access; no dedicated API key or model CI environment is required. Record the model/reasoning identity when observable and unknown fields explicitly. Subagents consume model usage and share filesystem permissions/tools. Fresh context and disposable directories do not create security isolation or guarantee a hidden grader. Scope actions to the synthetic project and supplied provider; do not use production data, external connectors, remote publication or credentials.

## Exercise and independently verify

The versioned six-case suite covers:

| Case | Expected behavior to verify |
| --- | --- |
| `new-intent` | Proposal/Requirements and a first-gate stop; no invented approval, Design/Tasks or product edit |
| `missing-coverage` | Meaningful missing assertions plus maintained regressions actually run |
| `adequate-reuse` | Adequate tests reused and full suite executed without redundant test requirements |
| `retained-failure` | New passing path and old failing check both run; truthful failure, unchanged source/tests |
| `stale-evidence` | Actual new execution after changed inputs; old attempt retained, not rehashed |
| `validation-only` | Defect and findings recorded without unauthorized source/test repair |

For change `automated-test-execution`, Design R3 specifies one fresh invocation per case, sequentially, at most six planned invocations, monitored 600-second case and 3600-second suite limits including independent verification. Other changes choose proportionate bounds in their reviewed plan. Check elapsed time during supervision and interrupt at a reached limit. Native interruption is best effort, not a hard cost ceiling; record overruns and available usage. Do not automatically retry or select only successful attempts. After an authorized fix, use a separately recorded bounded rerun and preserve failures.

After the scenario agent stops, inspect its available actions, file differences, approval identities and original structured runner reports. Compare report command identity, input snapshots, counts, timestamps and retained outputs against the fixture. These are reviewable observations, not authenticated attestations. A final narrative or arbitrary agent-written log alone is insufficient. Where an action cannot be supported by available observations or attributable runner evidence, mark it unverified.

Preserve an untouched copy of the scenario output before replay. The helpers can inspect differences and execute the current suite independently:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path('tests/skills').resolve()))
from verification import replay, mutation_replays

project = Path('/tmp/versat-scenario')
observed = replay(project, Path('/tmp/versat-replay'))
# For missing-coverage and adequate-reuse, after reviewing the generated commands:
mutations = mutation_replays(project, Path('/tmp/versat-mutations'))
```

Use fresh output directories outside the scenario. Replay launches the explicit runner in a subprocess with a timeout; it returns process observations and a structured report, not semantic acceptance. Mutation replay uses separate copies, changing only product code to introduce duplicate-charge, zero-amount and empty-key defects. Verify that the good suite passes and each mutant fails the intended assertion. Tests must remain unchanged. The original scenario directory is not modified by mutation replay.

For failure scenarios, an independently reproduced failing product suite is expected evidence that the evaluation behaved correctly. Do not record the product check itself as passing. Inspect source/test diffs and the recorded gap. For stale evidence, require a new attempt with current inputs and preserve the older run. For planning, inspect resulting stage files and actual stopping behavior.

## Record the attempt

Use the [attempt template](../../tests/skills/README.md). Store prompts, fixture manifests/diffs, original outputs, independent command results, controlled-defect identities, assertions and verdicts at stable reviewed paths outside the SDD dossier. Keep every failure, interruption and unavailable attempt. Record provider/check input digests before and after actual evaluation; changes during the run prevent a fresh pass. Fixture changes are expected scenario outputs and have separate before/after manifests.

Use available native observations; the interface does not promise complete JSONL export or exact usage accounting. Unknown telemetry stays unknown. Store synthetic, scrubbed evidence without dumping session configuration, secrets or unrelated conversation. The coordinator records per-assertion pass/fail/unverified with reasons and separately assesses semantic acceptance. Helpers do not approve plans, close findings or authenticate actions.

Required supervised results use the existing SDD local `review` method. Missing required evidence prevents delivery readiness even when automated tests pass. After source/runtime changes, rerun affected checks with current snapshots rather than relabeling old results.

## CI, delivery and migration

All required automated suites continue running in deterministic CI. Supervised Skill evidence is reviewed locally before delivery; it is never an automated CI pass and cannot waive required application evals. Follow the canonical [Testing Standard](../../standards/core/testing.md).

The delivery sequence is current local tests and supervised evidence, semantic assessment, documentary archival in the same implementation branch, archive preflight, authorized submission, final required CI and PR review before merge. Publishing an intermediate evaluation draft is unnecessary. Remote runs and required-check settings must be observed separately; a local pass cannot establish them.

The unshipped autonomous evaluator and protected model workflow have been removed from this source delivery. Historical CLI probes and old attempts remain historical evidence. Existing consumers keep their exact provider pins until reviewed adoption; no release, remote rule change or cache update is implied. If an actual remote rule still requires the deferred job, prepare its separately authorized reconciliation without bypassing protection. Rollback preserves tests and evidence and restores reviewed consumer configuration/provider pins together; it does not silently restore credentialed model execution.
