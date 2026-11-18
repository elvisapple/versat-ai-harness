# CHECK-004 — Ruff, GitHub event comparison and retained validation

Outcome: pass. Ran `./scripts/validate/run.sh --quality-base origin/main`
with CPython 3.11.14 on arm64 macOS, Git 2.54.0 and Ruff 0.14.14. The observed
base was `c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa`. The package identified
the new Unreleased entry and checked four changed Python files. Lint and
formatting passed. Package and SDD inventory validation passed, followed by
142 validator tests and 48 execution tests. Existing historical inventory
warnings remained visible.

The Git fixtures used the same command as the Harness workflow. They
observed checkout verification and base selection for a PR merge revision,
an existing branch push, a new branch, a same-tip branch and an initial
root commit. The local and event paths share the same Ruff and changelog
checks. A seeded unused import and a formatting violation failed with named
diagnostics and without file edits. Absent Ruff or Git history failed with
install or fetch instructions. The consumer wrapper passed an event-based
full run, ran its suites after a quality failure, and also exposed a suite
failure when quality passed.

Reviewed the Harness workflow conditions. Quality applies to branch pushes
and PR activity. Structural validation still applies to PRs and main pushes
and uses its prior base, draft and archive conditions. The maintained
`tests/execution/test_ci.py` cases exercised the structural shell step in
both inventory and archive modes, rejected a missing base, preserved failure
propagation, and kept missing supervised evidence non-passing. Its consumer
case ran a current suite and a deliberately failing retained suite.

Earlier attempts: lint initially reported an unused import in the touched
consumer fixture, which was removed. The first Python 3.11 full run reached
the existing virtual-environment test and failed to launch a copied Python
binary because the distribution locates its dylib relative to that binary.
The fixture now creates the interpreter symlink its test is intended to
exercise. The targeted regression and the subsequent full run both passed.

This is local evidence, including synthetic GitHub events and workflow
commands. A remote Actions run and remote ruleset coverage remain unverified.
