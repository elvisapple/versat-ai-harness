# CHECK-005 — fail

Observed 2026-11-10 in local isolated Harness checkout, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec plus private working-tree changes. Reviewer: coding agent; human legal/technical approval is not implied.

Ran full maintained package script with selected interpreter, exit 0: Plugin and SDD inventory plus 131 validator tests and 48 execution tests. See package-validation.txt. Historical legacy/v2 warnings remain qualified. This verifies package behavior, not legal acceptance, confidential receipt or remote CI.

Input SHA-256 before and after: `7ec222e0fa6a1363aa6011ce957e1ea78eb2df1c6422462895fed976e72442c1`. Both snapshots observed identical.

Environment: macOS-26.5.2-arm64-arm-64bit, Python 3.11.4, /private/tmp/versat-issue22-venv/bin/python. GitHub reads were authenticated; no public-reader access inferred.

Final rerun after recording acceptance findings: exit 1 from SDD ACCEPTANCE_GAP, while all 131 validator and 48 execution tests still pass. See final-package-validation.txt. Earlier successful package output is preserved in package-validation.txt. The current check result is fail; a passing test suite does not waive the recorded acceptance gaps. No validator or required scope was weakened.
