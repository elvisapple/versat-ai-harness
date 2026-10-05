# Skill tests

Use realistic requests and verify artifacts, authorization boundaries and Standards resolution. Follow the [supervised evaluation guide](../../docs/guides/skill-evaluations.md). `cases/` contains prompts; `fixtures.py` creates fresh synthetic projects; `verification.py` provides factual snapshot, integrity and independent replay helpers. None starts a model or supplies semantic approval. Maintained deterministic helper tests live in `tests/execution/test_supervised.py` and run in the full package suite.

## Supervised attempt record

Record each actual attempt in a separate stable evidence directory using this template. Unknown or unavailable fields remain explicit. Do not infer tool actions from the final answer alone.

- Identity: run, case, repetition, native agent ID, start/end time, coordinator.
- Inputs: exact prompt, Skill/provider identity, case version, fixture before manifest, approved plan identity where applicable, provider/check input digest before execution.
- Runtime: observed model/reasoning/settings, unknown fields, shared permissions and fresh-context selection, reviewed time/attempt limits, actual elapsed time, interruptions/overruns, available usage.
- Scenario output: available action/message observations, original runner report paths and raw outputs, fixture after manifest and changes, preserved original artifacts before coordinator replay.
- Independent checks: actual argv, exit/status, test counts, original replay, separate mutation copies/identities, resulting failed assertion and unchanged tests, plan/approval and source integrity.
- Verdicts: each expected observation as pass/fail/unverified, evidence references and explanation; no narrative-only or mocked-event pass.
- Freshness: provider/check input digest after execution, known external changes, required reruns.
- Outcome: current attempt result and reason, all earlier attempts retained, remaining unknowns and follow-up. The coordinator separately records the SDD result and semantic assessments.

An expected product test failure can satisfy a failure-handling scenario, but the product's own result remains failed. Fresh fixture directories organize test data; they are not a security boundary. No production data, secret or unrelated conversation belongs in retained artifacts.
