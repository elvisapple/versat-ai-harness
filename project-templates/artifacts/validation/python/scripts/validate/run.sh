#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
: "${VERSAT_HARNESS_ROOT:?Set VERSAT_HARNESS_ROOT to the reviewed exact Harness checkout}"
validation_python="${PYTHON:-python3}"
"$validation_python" "$VERSAT_HARNESS_ROOT/scripts/testing/provider.py" --root "$project_root"
exec "$validation_python" "$VERSAT_HARNESS_ROOT/scripts/testing/run.py" run --root "$project_root" "$@"
