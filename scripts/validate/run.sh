#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
failures=0

required_files=(
  "AGENTS.md"
  "README.md"
  "VERSION"
  "plugin/versat-ai-harness/.codex-plugin/plugin.json"
  "standards/index.yaml"
  "sdd/process.md"
  "schemas/project.schema.yaml"
  "docs/architecture/overview.md"
  "docs/decisions/README.md"
)

for relative_path in "${required_files[@]}"; do
  if [[ ! -s "${repo_root}/${relative_path}" ]]; then
    echo "FAIL missing or empty: ${relative_path}"
    failures=$((failures + 1))
  fi
done

skill_names=(
  "project-bootstrap"
  "versat-sdd"
  "project-audit"
  "architecture-review"
  "project-maintenance"
)

for skill_name in "${skill_names[@]}"; do
  skill_file="plugin/versat-ai-harness/skills/${skill_name}/SKILL.md"
  if [[ ! -s "${repo_root}/${skill_file}" ]]; then
    echo "FAIL missing or empty: ${skill_file}"
    failures=$((failures + 1))
  fi
done

if ! grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+([.-][0-9A-Za-z.-]+)?$' "${repo_root}/VERSION"; then
  echo "FAIL VERSION is not semantic"
  failures=$((failures + 1))
fi

if command -v python3 >/dev/null 2>&1; then
  if ! python3 -m json.tool "${repo_root}/plugin/versat-ai-harness/.codex-plugin/plugin.json" >/dev/null; then
    echo "FAIL invalid JSON: plugin/versat-ai-harness/.codex-plugin/plugin.json"
    failures=$((failures + 1))
  fi
fi

if [[ "${failures}" -gt 0 ]]; then
  echo "Validation failed with ${failures} error(s)."
  exit 1
fi

echo "Versat AI Harness structural validation passed."
