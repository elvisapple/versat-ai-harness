#!/usr/bin/env bash
set -euo pipefail

provider_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
export GIT_OPTIONAL_LOCKS=0
exec "${PYTHON:-python3}" "$provider_root/validators/quality/validate.py" "$@" </dev/null
