# Retained development failure observations

The first run of the new `test_supervised.py` executed ten tests with three errors and two failures. Independent replay lacked a structured report, the deadline test observed immediate process exit instead of timeout, and output-overlap detection failed on macOS temporary path aliases.

A separate real replay probe exposed `ModuleNotFoundError: No module named 'jsonschema'`: the command executor resolved the virtual-environment Python symlink to the base interpreter before launching it. The correction preserves the invocation path and still records the resolved binary identity. A regression creates a real virtual environment containing a module unavailable to the base interpreter and verifies its successful import through the executor.

The helper now normalizes both project/output paths before overlap comparison, retaining explicit root-link and descendant-link checks. Replay and mutation outputs remain separate from the source fixture. After these corrections, all ten supervised helper tests passed, followed by the full 179-test package suite. The failure was not recorded as a model scenario failure: no native agent was involved in these helper tests.

The diagnostic probe's original stdout/stderr remains under the session temporary directory `versat-replay-debug-xnk90q_1/out`; this note retains the causal observations if that temporary directory is cleaned. No failed test or assertion was removed to obtain the subsequent pass.

The original diagnostic output was also preserved durably in [development-probe-r2](development-probe-r2/).
