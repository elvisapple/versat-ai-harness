#!/usr/bin/env bash
set -euo pipefail
project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
: "${VERSAT_HARNESS_ROOT:?Set VERSAT_HARNESS_ROOT to the reviewed exact Harness checkout}"
validation_python="${PYTHON:-python3}"
"$validation_python" "$VERSAT_HARNESS_ROOT/scripts/testing/provider.py" --root "$project_root"

quality_args=()
suite_args=()
targeted=false
while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --quality-base)
      if [[ "$#" -lt 2 || -z "$2" || "$2" == --* ]]; then
        echo "--quality-base requires a Git comparison revision" >&2
        exit 1
      fi
      quality_args=(--base "$2")
      shift
      ;;
    --suite|--suite=*)
      targeted=true
      suite_args+=("$1")
      ;;
    *)
      suite_args+=("$1")
      ;;
  esac
  shift
done

quality_status=0
if [[ "$targeted" == "true" ]]; then
  echo "Targeted suites only. Run full validation for quality and readiness." >&2
else
  if [[ -n "${VERSAT_QUALITY_EVENT:-}" ]]; then
    quality_args=(--github-event "$VERSAT_QUALITY_EVENT")
  fi
  if [[ "${#quality_args[@]}" -eq 0 ]]; then
    echo "FAIL quality comparison needs --quality-base (for example, origin/main)." >&2
    quality_status=1
  else
    PYTHON="$validation_python" bash "$VERSAT_HARNESS_ROOT/scripts/validate/quality.sh" \
      --root "$project_root" "${quality_args[@]}" >&2 || quality_status=$?
  fi
fi

suite_status=0
"$validation_python" "$VERSAT_HARNESS_ROOT/scripts/testing/run.py" run --root "$project_root" \
  ${suite_args[@]+"${suite_args[@]}"} || suite_status=$?
if [[ "$quality_status" != "0" ]]; then
  exit 1
fi
exit "$suite_status"
