# Versat AI Harness

This repository is the source of truth for Versat's AI-assisted development standards and workflows.

## Mandatory rules

- Read `docs/architecture/overview.md` and the related ADRs before changing architectural boundaries.
- Do not duplicate standards inside Skills. Skills must locate and apply the canonical documents under `standards/`.
- Keep responsibilities separate: `plugin/versat-ai-harness/` defines capabilities, `standards/` defines policies, `sdd/` defines the process and `validators/` defines deterministic enforcement.
- Treat corporate policy updates as governed changes: branch, Pull Request and mandatory review.
- Use `standards/index.yaml` to resolve context; do not hard-code parallel lists of standards in Skills.
- Preserve template composition. A profile extends `base` instead of copying its files.
- Do not silently update consumers to `latest`. Releases must use semantic versioning and be consumed by exact reference.
- Record significant architectural decisions under `docs/decisions/`.
- Run `./scripts/validate/run.sh` before completing a change.

## Languages

- Follow `standards/core/language.md` as the canonical language policy.
- Use English for code, identifiers, APIs, database objects, commits, technical names, technical documentation, ADRs, architecture documentation, Skills, agent instructions and SDD artifacts.
- Use Spanish for internal business playbooks, issues, Pull Requests and corporate communication.
- Maintain English as the canonical source for product interfaces and community documentation, with aligned Portuguese and Spanish translations.

## Authority

LLM guidance helps produce compliant results, but it does not replace mechanical validation, human review, GitHub Rulesets or required checks.
