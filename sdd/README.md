# Versat SDD — Developer Guide

Use `$versat-sdd` to plan, implement, validate or prepare delivery of a change. Describe the outcome and, when available, its change ID. The skill identifies the current state and reads the applicable internal workflow. The former `new-change` skill's planning behavior now belongs to this single entry point.

The four files in `sdd/workflows/` are procedures for the agent, not separate skills, slash commands or scripts you must run. Planning has three human review gates; the other workflows cover implementation, validation and documentary closure.

```text
PLAN: Proposal + Requirements -> approval -> Design -> approval -> Tasks -> approval
  |
  | explicit implementation request
  v
IMPLEMENT: implementation, tests, task progress and living specifications
  |
  v
VALIDATE: requirement coverage, executed checks and actual evidence
  |
  v
PREPARE DELIVERY: documentary archive in the same change branch/PR
  |
  v
PR review + final required checks -> merge -> read-only delivery confirmation
```

## Phases and deliverables

| Phase | Internal workflow | Deliverables | Completion condition |
|---|---|---|---|
| Plan | [new-change.md](workflows/new-change.md) | `proposal.md`, `requirements.md`, `design.md`, `tasks.md`; necessary ADR drafts. | Three current human approvals; no material unresolved decision. |
| Implement | [implement-change.md](workflows/implement-change.md) | Implementation, relevant tests, truthful task progress and updated living product/architecture specifications. | Approved tasks implemented and development checks performed or blockers reported. |
| Validate | [validate-change.md](workflows/validate-change.md) | Requirement-to-evidence coverage, actual check results in Tasks, gaps and a prepared PR summary. | Required local checks pass; external checks remain unverified until observed. |
| Prepare delivery | [archive-change.md](workflows/archive-change.md) | Dossier moved to documentary archive in the same branch, checked references and delivery summary. | Delivery eligibility passes, ready for PR review and final CI; no merge claim. |

PR review, required CI checks and merge are delivery checkpoints. They do not require a fifth specification file. Merge is separate from deployment and any project-specific operational follow-up.

## Before starting

Open the intended project. The skill uses its repository instructions, selected Harness version, resolved Standards and existing changes. Supply a real issue or Story if one exists; do not invent an ID to satisfy a template. Follow the project's normal branch convention and the resolved Git Standard. Starting a specification does not itself authorize PR publication, merge or deployment.

The examples below use English to match the canonical technical artifacts. You can speak to the chat in your preferred language; document language follows the project's Standards.

## 1. Plan the change

```text
Use $versat-sdd to plan a change: add a Greet button to the home page.
When clicked, show an accessible inline greeting. Follow the existing
English, Portuguese and Spanish translations. Do not implement it yet.
```

The skill chooses or reuses a stable ID, such as `home-greeting`, under `specs/changes/home-greeting/`. It reads enough repository context to explain the plan and asks focused questions when behavior or scope remains ambiguous.

### Gate 1 — Proposal and Requirements

The chat generates `proposal.md` and `requirements.md` together. Proposal explains the problem, outcome, scope, exclusions and risks. Requirements specify observable behavior and acceptance scenarios with stable IDs such as `REQ-001`.

Read both files, including assumptions and edge cases. The chat presents their shared revision and asks for approval. It waits before creating Design or Tasks.

```text
I approve Proposal/Requirements R1. Proceed to Design.
```

To request changes instead:

```text
Revise the requirements: repeated clicks must reuse the same message
area, and keyboard activation must work. Present the revised documents.
```

### Gate 2 — Design

After approval, the chat generates `design.md`. It describes the approach, affected components, contracts, alternatives and relevant operational concerns. Its validation plan maps each requirement to identifiable required checks. Significant architecture decisions include ADRs for review.

Review the proposed approach and how it will prove the accepted behavior, then reply:

```text
I approve Design R1. Proceed to Tasks.
```

### Gate 3 — Tasks

The chat generates `tasks.md` after Design approval. Each task has a stable ID, requirement references, dependencies and a verifiable completion condition. The plan covers implementation, testing and documentation actually needed for the change.

First-use documentation follows the resolved [Documentation Standard](../standards/core/documentation.md): plan updates to the existing guide or create one when useful product behavior needs explanation. Keep this work with the affected functionality. The [Testing Standard](../standards/core/testing.md) guides coverage of relevant acceptance scenarios, including errors and boundaries. Existing scenarios, checks and tasks carry this work without additional SDD artifacts or gates.

```text
I approve Tasks R1. Conclude planning.
```

Planning is now complete. Tasks remain pending: approving them does not mean implementation happened or tests passed. To also authorize execution after reviewing the current Tasks revision, use:

```text
I approve Tasks R1. Implement the approved home-greeting change.
```

This combines an actual planning approval with an explicit execution instruction. An initial “implement everything” still goes through the three gates when there is no approved plan.

## 2. Implement the approved change

If you concluded planning without authorizing execution:

```text
Use $versat-sdd to implement the approved home-greeting change.
```

The skill checks that the approvals and upstream revisions are current, reads the implementation workflow, performs the tasks and runs appropriate development checks. It maintains task status and updates living product/architecture specifications and affected usage instructions alongside the implemented behavior.

A material requirements or design change reopens the affected gate. Routine fixes inside the approved approach continue under the existing execution request. At handoff, the chat distinguishes completed implementation, pending validation, PR status and actual delivery.

## 3. Validate

```text
Use $versat-sdd to validate home-greeting against its approved requirements.
```

The skill traces requirements to Design's check plan, runs applicable tests/evals/validators, records actual evidence in `tasks.md` and prepares a PR summary. Check results identify what ran and its actual revision/run. The validation plan and the validation result are separate records.

Validation also exercises changed documented commands or UI steps and checks their expected outcomes. Functional checks can supply the same evidence. Relevant scenarios with missing coverage or unavailable verification remain explicit gaps even when structural validation passes.

A validation-only request produces findings and evidence; it does not authorize code fixes. You can request implementation and validation together when you want both. There is no additional mandatory human gate between those authorized phases.

The validator reports `pass`, `fail` or `unable-to-verify`. Missing evidence or unavailable external checks remain unverified. A local pass checks recorded structure and consistency; it does not authenticate the developer's approval, prove semantic acceptance or establish remote CI/merge status.

## 4. Prepare the archive and PR

```text
Use $versat-sdd to prepare documentary archival of home-greeting
in the current change branch. Prepare the PR summary.
```

The skill checks current approvals, completed tasks, passing required checks and coherent living specifications. It preserves the change ID, approvals, evidence and ADR references, moves the dossier to `specs/archive/home-greeting/`, marks documentary closure `prepared` and reruns affected checks.

This prepares the dossier in the implementation branch before merge. The archive folder is not evidence of delivery. A draft PR may already exist; preparation belongs to that same PR. Publication occurs when explicitly requested or already included in the authorized delivery scope. PR review and final required checks follow the repository's policies; planning approval does not replace them.

When you ask to submit a completed implementation for PR review, this archive preparation is part of the request. The agent confirms the archive path, `closure: prepared` and passing delivery validation in the existing PR summary. A planning/draft PR may still have an active dossier, with the remaining closure work stated explicitly.

Review feedback stays in the same branch and change ID. An unmerged archived dossier can be revised. Scope/design changes reopen gates; checks must be rerun after implementation changes. The dossier can move back to active storage while replanning. It cannot claim delivery readiness with stale approvals or evidence simply because it was previously archived.

## 5. Confirm delivery after merge

Merge brings implementation, living specifications and the documentary archive into the default branch together. No mandatory second branch, commit, PR or merge is needed solely to move the dossier or record that the first PR merged.

```text
Use $versat-sdd to check whether home-greeting was merged
and summarize its delivery status.
```

This is a read-only confirmation. Actual Git/PR evidence and final checks establish delivery status. If those cannot be observed, the chat says unverified. It does not infer delivery from completed tasks, a proposal status or the archive path. Deployment is reported separately.

Record actual tested revisions/runs; do not require a document to contain the SHA of the commit that contains that same document. The platform records the final merge. Migration/closure of older changes may need a maintenance PR, but it does not recursively create another functional SDD change. New behavior after delivery receives a new change ID.

Use the existing sources to distinguish delivery states:

| State | Evidence |
|---|---|
| Documentary closure prepared | Dossier in `specs/archive/<change-id>/`, `closure: prepared` and passing delivery checks. |
| Integrated into the default branch | Observed merged PR and merge commit. |
| Published | A release or artifact version containing that change. |
| Available in an environment | Observed deployment or installed version, including feature enablement where applicable. |

Keep living product specifications and usage guides in their normal locations; archive only the change dossier. For the Harness itself, a merge does not update installed plugins or consumer projects: they adopt an explicit release.

After merge, cleanup follows the [Git Standard](../standards/core/git.md#branch-and-worktree-cleanup). A branch created from a worktree can be deleted on GitHub; that does not remove its local branch or worktree. Reuse a suitable active worktree or retire it through the managing app when no longer needed. Cleanup can be included in the delivery request; a request only to inspect status remains read-only.

## Approvals, changes and resumption

You approve in the chat after reviewing a presented revision. You do not need to edit YAML headers. The skill maintains review state, revision, upstream references and the real approval quote/source. A short “approved” is sufficient when one gate is unambiguous. Silence, blanket preapproval and conditional acceptance of an unseen revision do not complete a gate.

Changing an approved requirement reopens Proposal/Requirements and dependent Design/Tasks reviews. Changing Design reopens Design and Tasks; changing the task plan reopens Tasks. Progress, result records and completion checkboxes do not themselves reopen planning. The content fingerprint is conservative: content edits beyond its documented bookkeeping/whitespace exclusions require another review, including edits described as editorial. Existing approval evidence is never silently assigned to changed content.

To check where you stopped:

```text
Use $versat-sdd to inspect home-greeting and report the current phase,
approvals, blockers and next permitted action. Do not change files.
```

To continue approved work:

```text
Use $versat-sdd to resume implementation of home-greeting from its
current approved plan. Preserve the same change ID and artifacts.
```

The skill verifies existing records and reuses valid approvals; opening a new chat does not require starting over. If approval evidence or the reviewed revision is missing, it re-presents that gate instead of inventing history.

## Existing changes and verification limits

Older dossiers can remain exact, explicitly grandfathered records. Exemption preserves history and is not current execution or closure approval. Resuming implementation or preparing archival of an exempt change requires a reviewed migration to v3 metadata with actual approvals and evidence. Consumer projects do not inherit exemptions from the provider repository.

The agent workflow supplies human interaction; local checks enforce artifact consistency; the repository platform supplies trusted PR review, required checks and merge evidence. None replaces the other. See [metadata](metadata.md) and the [validator guide](../validators/sdd/README.md) for the exact contract and limits.

## Reference map

- [Process](process.md): canonical phase order, gates and revision/closure rules.
- [Workflows](workflows/): procedures selected and read by the agent.
- [Metadata](metadata.md), [templates](templates/) and [schemas](schemas/): artifact formats and recorded evidence.
- [Standards index](../standards/index.yaml): policy selection for the project.
- [Validator](../validators/sdd/README.md): deterministic checks and adoption behavior.
- [Public skill](../skills/versat-sdd/SKILL.md): context resolution, routing and handoff.

## Worked acceptance and regression examples

New dossiers use v3. Continue using the same skill and four files; the agent maintains the structured records described in [metadata](metadata.md).

| Situation | Planning and observed validation |
|---|---|
| New greeting feature | Proposal explains assessed no-impact when grounded in the project. Requirements include success, empty input and repeated activation. Design maps every acceptance position; one adequate maintained test can cover multiple positions. Missing boundary behavior blocks completion even with every task checked. |
| Payment retry extending archived duplicate prevention | Proposal cites `prevent-duplicates/REQ-001`, its source Requirements digest, and the effective current contract. Preserve maps the old scenario to a current CHECK using the existing duplicate test in the normal suite. Run both the new success path and duplicate prevention. An old archived pass cannot substitute. |
| Intentional supersession | Proposal explicitly replaces the old contract, records why and targets the new local requirement. Design verifies the replacement. Update the living specification and retire only obsolete assertions under that approved scope; preserve delivered dossier bytes. |
| Unavailable environment | Keep the applicable scenario mapped; record unverified with the unavailable prerequisite. Do not use not-applicable, pretend a local run satisfied a required CI context or copy another run's input hash. |
| Manual documentary check | Design gives concrete inspection steps, expected observations and why useful automation is unavailable. Record the actual review and matching input snapshots. It is a reviewer observation, not an autonomous-agent evaluation. |

For the payment example, from the selected Harness root:

```sh
python validators/sdd/validate.py --root /path/to/project --change prevent-duplicates --source-digest
python validators/sdd/validate.py --root /path/to/project --change payment-retry --phase implementation
python validators/sdd/validate.py --root /path/to/project --change payment-retry --input-digest CHECK-002
# Actually run CHECK-002's approved maintained test in the project, then:
python validators/sdd/validate.py --root /path/to/project --change payment-retry --input-digest CHECK-002
python validators/sdd/validate.py --root /path/to/project --change payment-retry --phase delivery --json
```

Record both snapshots around execution; matching hashes alone are not a test run. Missing/failed results or assessments block delivery. A later source/test/configuration edit invalidates affected evidence without changing task planning. On resumption, rerun and reassess. Do not merely replace the stored hashes.

If validation finds missing or contradictory behavior, record/reuse a FIND entry and the affected scenario. Validation-only reports it without a product edit. Existing implementation authorization permits a routine correction within approved tasks and revalidation. Adding new task-plan scope reopens Tasks; broader changes reopen the earliest affected gate. Completed checkboxes never waive unresolved findings.

After documentary archival, `--change payment-retry --phase delivery` is still live. Default inventory preserves historical results; `--baseline <trusted-base>` additionally selects changed archives for live checks. The [validator guide](../validators/sdd/README.md) explains CI's event-derived baseline and exit codes. Run profile-required suites as well as targeted tests.

The introducing change has [recorded reviewer walkthroughs](../docs/validation/sdd-acceptance-regression/reviewer-walkthrough.md), with executable synthetic payment behavior and separate deterministic cases. These show what was actually observed and the remaining trust limits.

## Mandatory archive check before submitting completed work

A completed implementation must be archived before its PR is submitted for review or an existing draft becomes ready. The local command is:

```sh
python validators/sdd/validate.py --root /path/to/project --change home-greeting --phase delivery --require-archive
```

This fails if the dossier is still in `changes`, if `closure` is not `prepared`, or if live delivery requirements fail. Plain delivery remains the pre-move eligibility check. The agent performs archive preparation as part of an authorized submission request; it does not need another functional change to do so. An implementation/validation-only handoff must state archival pending until prepared.

CI uses `./scripts/validate/run.sh --baseline <event-base> --require-archive` for non-draft PRs and pushes to main, including a draft-to-ready event. It selects changed active and archived dossiers and rejects an empty selection. Planning/incomplete reviews use a draft PR. Existing unchanged history is not required to migrate. Required platform checks enforce merge eligibility; CI alone cannot stop all clients from opening a PR.
