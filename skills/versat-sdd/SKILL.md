---
name: versat-sdd
description: Plan, implement, validate or prepare documentary archival of a Versat SDD change, with human planning gates and explicit workflow routing. Use for material product, agent, infrastructure or policy changes and for resuming their lifecycle.
---

# Versat SDD

Use this single public entry point for the lifecycle. The four workflow documents are internal procedures, not independently registered skills or commands. The [developer guide](../../sdd/README.md) provides prompts and deliverables.

## Resolve and route

1. Identify the target repository and read its applicable `AGENTS.md`, project identity, Standards lockfile/snapshot, relevant living specifications and existing change. Preserve unrelated work. Resolve the same Harness version selected by that project; do not silently upgrade it.
2. The packaged Harness root is two directories above this skill's directory. Verify `VERSION`, `sdd/process.md`, `sdd/templates/` and `standards/index.yaml`. Read the version-matched [process](../../sdd/process.md). Resolve Standards through its index, not a parallel list in this skill. If matching resources are unavailable, report the missing dependency instead of substituting another release.
3. Reuse the intended change ID and inspect artifacts in both `specs/changes/` and `specs/archive/`. Reconcile current approvals and evidence before choosing the next action. File existence, proposal status and archive location do not establish readiness or delivery.
4. Select, **read and follow** the workflow below for the authorized intent. Announce the selected phase and its stopping condition. Load only that workflow, its needed templates and [metadata contract](../../sdd/metadata.md); read another workflow when actually transitioning to it.

| Intent | Required workflow |
|---|---|
| Start, plan, revise planning, or implement an intent without a current approved plan | [New change](../../sdd/workflows/new-change.md) |
| Implement a current approved plan | [Implement change](../../sdd/workflows/implement-change.md) |
| Validate, inspect acceptance evidence or report validation gaps | [Validate change](../../sdd/workflows/validate-change.md) |
| Prepare documentary archive/delivery, or confirm merge after delivery | [Archive change](../../sdd/workflows/archive-change.md) |

For “resume” or status, inspect state first. Report-only requests stay read-only; otherwise resume only the authorized next action. When context cannot disambiguate the repository, change or missing approval, ask one focused question.

## Boundaries and handoff

Follow the canonical human gates and revision rules in the process. Planning approval alone does not authorize implementation. After reviewing Tasks, the developer may combine its approval with an explicit implementation request. Validation-only does not authorize code fixes. Scoped authorization for PR creation, merge or deployment is separate from specification approval; never infer it from skill selection.

Run the phase-appropriate checks documented by the selected workflow and [SDD validator](../../validators/sdd/README.md). Report actual results and unknown external state separately. End with the change ID, phase/revision, linked deliverables, blockers and next permitted action. At a pending planning gate, present the reviewable files and ask for that stage's approval, then stop.
