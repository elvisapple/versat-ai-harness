# CHECK-005 — fail

Observed 2026-11-10 in local isolated Harness checkout, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec plus private working-tree changes. Reviewer: coding agent; human legal/technical approval is not implied.

Ran same full maintained package suite on combined stable source, exit 0: Plugin/SDD inventory, 131 validator tests, 48 execution tests. See package-validation.txt. Retained legacy/v2 warnings do not approve historical/current legal or channel evidence. Organization has no added application suite; manual access/translation review is distinct.

Input SHA-256 before and after: `4315e28ad911a4df0dd842fd8a49b4b6f16508ee8b41af8d0658e33a7a69d5e0`. Both snapshots observed identical.

Environment: macOS-26.5.2-arm64-arm-64bit, Python 3.11.4, /private/tmp/versat-issue22-venv/bin/python. GitHub reads were authenticated; no public-reader access inferred.

Final rerun after recording acceptance findings: exit 1 from SDD ACCEPTANCE_GAP, while all 131 validator and 48 execution tests still pass. See final-package-validation.txt. Earlier successful package output is preserved in package-validation.txt. The current check result is fail; a passing test suite does not waive the recorded acceptance gaps. No validator or required scope was weakened.
