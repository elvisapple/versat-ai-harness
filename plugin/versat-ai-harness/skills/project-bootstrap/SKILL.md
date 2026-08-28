---
name: project-bootstrap
description: Create a new Versat repository or initialize an empty project using the governed profile, Standards, SDD, templates and readiness workflow. Do not use to retrofit an established repository; use project-maintenance instead.
---

# Project Bootstrap

Create one reviewable bootstrap change rather than assembling a project manually.

## Workflow

1. Collect only missing identity fields required by `schemas/project.schema.yaml`.
2. Classify the project as software, agent, hybrid, library or infrastructure.
3. Resolve applicable context from `standards/index.yaml`; do not let the caller hand-pick mandatory Standards.
4. Compose `project-templates/base` with the selected profile modules.
5. Initialize the `project-bootstrap` change using `sdd/process.md` and its templates.
6. Generate `.versat/project.yaml` and an exact `.versat/standards.lock`.
7. Run the validation entry point and report gaps without hiding or bypassing them.
8. Prepare a bootstrap branch and Pull Request only when the user has authorized remote repository changes.

## Constraints

- Do not duplicate Standards into this Skill or silently select `latest`.
- Do not create remote repositories, teams, rulesets or Pull Requests without scope and authorization.
- Keep the generated project profile-specific but the lifecycle uniform.
- A successful result is a reviewable repository skeleton, initialized SDD change and explicit readiness result.

Read [references/project-lifecycle.md](references/project-lifecycle.md) when orchestrating the complete corporate bootstrap sequence.
