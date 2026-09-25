---
name: project-bootstrap
description: Create a new Versat repository or initialize an empty project through guided product discovery, product documentation, governed profiles, Standards, SDD and readiness checks. Do not use to retrofit an established repository; use project-maintenance instead.
---

# Project Bootstrap

Create one reviewable bootstrap change rather than assembling a project manually.

## Workflow

1. Locate the installed Plugin root two directories above this file and read its [project schema](../../schemas/project.schema.yaml).
2. Reuse supplied context and collect missing identity fields required by the project schema.
3. Classify the project as software, agent, hybrid, library or infrastructure.
4. Resolve applicable context from the Plugin root [Standards index](../../standards/index.yaml); do not let the caller hand-pick mandatory Standards.
5. Read [product discovery](references/product-discovery.md) and guide the developer through the [product overview template](../../project-templates/base/specs/product/overview.md). Ask about missing product context in short rounds; use the resolved language policy for the generated artifacts.
6. Compose the Plugin root [base template](../../project-templates/base/) with the selected profile modules. Populate `specs/product/overview.md` in the target repository and create supporting product files only when the discovery guidance warrants them. Keep unknowns explicit and present the draft and remaining questions for developer review without claiming approval.
7. Initialize the `project-bootstrap` change using the Plugin root [SDD process](../../sdd/process.md) and its templates. Link its proposal to the product overview and relevant supporting sections; distinguish product ambitions from the scope of the repository bootstrap.
8. Generate `.versat/project.yaml` and an exact `.versat/standards.lock` in the target project.
9. Review product coverage using the discovery guidance, then run the Plugin root validation entry point and report gaps without hiding or bypassing them. Structural validation does not establish product evidence or approval.
10. Prepare a bootstrap branch and Pull Request only when the user has authorized remote repository changes.
5. Read the Plugin root [template composition guide](../../project-templates/README.md) and compose the [base template](../../project-templates/base/) with the selected profile modules. Use the matching authoring artifacts only for concrete capabilities requested by the project; keep illustrative examples out of active execution paths.
6. Initialize the `project-bootstrap` change using the Plugin root [SDD process](../../sdd/process.md) and its templates.
7. Generate `.versat/project.yaml` and an exact `.versat/standards.lock` in the target project.
8. Run the Plugin root validation entry point, then verify the generated project against the resolved artifact contracts and its documented validation commands. Report executor loading and integration readiness separately; package validation alone does not verify the consumer.
9. Prepare a bootstrap branch and Pull Request only when the user has authorized remote repository changes.

## Constraints

- Treat the installed Plugin root as the source of version-matched bootstrap artifacts.
- Do not duplicate Standards into this Skill or silently select `latest`.
- Do not create remote repositories, teams, rulesets or Pull Requests without scope and authorization.
- Keep the generated project profile-specific but the lifecycle uniform.
- A successful result is a reviewable repository skeleton, populated product overview with explicit evidence gaps, initialized SDD change and explicit readiness result.

Read [references/project-lifecycle.md](references/project-lifecycle.md) when orchestrating the complete corporate bootstrap sequence.
