---
sdd_version: 2
change: quickstart-scenario-coverage
requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]
adrs: []
validation:
  - id: CHECK-001
    description: Walk through first-use documentation decisions for usable, existing-guide and empty-scaffold projects; inspect README targets, supporting guides and archive-stable paths.
    requirements: [REQ-001, REQ-002, REQ-006]
    required: true
  - id: CHECK-002
    description: Review the revised SDD instructions against usage-changing and internal-only changes, including runnable examples, UI steps and unavailable validation environments.
    requirements: [REQ-003, REQ-004]
    required: true
  - id: CHECK-003
    description: Exercise a scenario-coverage review with happy-path-only evidence, missing error or boundary checks and reusable existing tests, then verify that gaps remain explicit.
    requirements: [REQ-005]
    required: true
  - id: CHECK-004
    description: Inspect the final diff, base/profile composition and modified Markdown links for policy ownership, proportionality, unchanged schemas and no automatic consumer adoption.
    requirements: [REQ-001, REQ-002, REQ-006]
    required: true
  - id: CHECK-005
    description: Run the existing package, SDD contract and validator test entry point plus phase-appropriate validation for this change; report baseline failures separately.
    requirements: [REQ-006]
    required: true
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 5a1170e5847ce0e113aa1ea89032a5e27b63ec9619db62c5e292636a5a317f7f
  approval:
    source: "Developer message in this conversation after Design R1 was presented"
    quote: "Aprove o design e defina as tasks."
    revision: 1
    digest: 7cc446787e408799dda5f5148d078c7cd891542096ca55af9b0c638ef2e33b6c
---

# Design

## Current state

Proposal/Requirements R1 are approved. The source package reports `0.2.0` with unreleased changes; this design uses its local canonical Standards resolved through `standards/index.yaml`, not another installed release. The always-applicable core Standards govern documentation, language, testing, security, Git, observability and agent artifacts. No new consumer profile or technology selection is introduced.

The existing planning workflow includes acceptance scenarios, one or more required checks per requirement and documentation tasks where needed. Implementation maintains living specifications; validation records actual results in Tasks. The base README provides purpose, ownership, development and architecture prompts but no first-use entry point. Bootstrap composes base/profile files through agent instructions; an executable composer is not available.

## Proposed design

### Policy and documentation shape

Extend `standards/core/documentation.md` with a compact first-use documentation rule covering the intended audience, prerequisites, preparation, one representative action and its observable result. Keep `docs/quickstart.md` as the default for a project that needs a guide; reuse an equivalent existing guide, including a suitable README section. The root README points to that actual entry point, using a section anchor when appropriate.

The same policy defines a stable living location outside `specs/changes/` and `specs/archive/`, optional focused guides under `docs/guides/` and updates alongside affected behavior. Supporting guides reference common setup. No per-feature quickstart is generated automatically and no guide directory is created without useful content.

An empty bootstrap does not produce a guide describing a future product. Once meaningful behavior is implemented, its documentation task creates the guide and README link together. A small project can keep all first-use content in its existing README. The reusable content outline belongs in the Documentation Standard; no new quickstart template or copied normative outline in Skills is needed.

Extend `standards/core/testing.md` with a concise scenario-coverage rule: select meaningful success, error and boundary checks in proportion to risk, reuse adequate existing tests and make uncovered relevant scenarios explicit. There is no prescribed test count, coverage percentage or TDD requirement. A single check may cover several scenarios or requirements when its method actually does so.

### Apply the policy through existing procedures

| Existing file | Planned adjustment | Requirements |
|---|---|---|
| `sdd/workflows/new-change.md` | Consider relevant error/boundary scenarios in Requirements; make Design's checks address relevant scenarios and affected documented usage; include only necessary documentation work in Tasks. | REQ-003, REQ-004, REQ-005 |
| `sdd/workflows/implement-change.md` | Maintain affected usage instructions with the implemented behavior, following the resolved Documentation Standard and using existing task completion conditions. | REQ-001, REQ-002, REQ-003 |
| `sdd/workflows/validate-change.md` | Assess scenario adequacy as well as requirement linkage; exercise changed commands or UI steps; compare expected and observed results; reuse existing checks/evidence and report unavailable verification truthfully. | REQ-004, REQ-005 |
| `sdd/README.md` | Briefly explain how the existing stages maintain and verify first-use documentation and scenario coverage; link to canonical policy for the conventions. | REQ-003, REQ-004, REQ-005, REQ-006 |
| `project-templates/base/README.md` | Add a conditional first-use authoring prompt referencing the resolved documentation policy: link the actual guide only when present, or omit the section for an empty scaffold. Do not add an unconditional Markdown link to a missing file. | REQ-001, REQ-002, REQ-006 |
| `project-templates/README.md` | Explain the conditional base README guidance and point to the Documentation Standard; no additional base file, copied profile content or directory manifest entry. | REQ-001, REQ-002, REQ-006 |
| `skills/project-bootstrap/references/project-lifecycle.md` | During bootstrap and readiness, apply the resolved Documentation Standard to actual usable behavior and verify any emitted README guide link. Keep this as an application of policy, not a second definition of it. | REQ-001, REQ-002, REQ-006 |

These seven adjustments complement the two canonical Standards edits. The existing bootstrap Skill already reads the composition guide and lifecycle reference. Its policy routing can remain unchanged. Existing duplicate workflow numbering in that Skill is unrelated maintenance and is not repaired by this change.

No modification to the four SDD artifact templates is needed: Requirements already holds acceptance scenarios, Design already holds check methods and Tasks already holds work and evidence. Descriptions can identify the covered behavior without adding scenario IDs. No modification to the archive procedure is needed because living documentation stays outside the dossier and existing reference checks apply.

## Boundaries and contracts

Policies remain in Standards, procedures in SDD, bootstrap capabilities in Skills and shared project guidance in base templates. Validators continue to check structural consistency; passing metadata does not establish scenario adequacy or successful usage instructions. This preserves the architecture and ADR-0013 lifecycle; no new ADR is required.

Only consumer documentation conventions and their production guidance change. The Harness's own SDD developer guide remains its existing user entry point; this change does not create a parallel Harness quickstart. No public command, runtime interface, metadata field, approval gate or validator is added.

## Data, security and permissions

Guides use safe examples and the existing resolved Language and Security Standards. Technical documentation and community-facing documentation retain their respective existing language/translation rules. No new translation exception or quickstart-specific policy is introduced. Exercising a documented operation remains subject to the existing authorization and environment requirements; inaccessible checks are recorded as unverified.

## Operations and observability

There is no deployed component, telemetry change or new operational dependency. Guide execution and behavioral checks use the existing Tasks evidence contract. A shared functional/documentation check records one observed result rather than requiring another report. Re-run affected checks after relevant implementation or instruction changes.

## Migration, rollout and rollback

Deliver source guidance through the existing branch, PR, review and required checks. A subsequent versioned release and explicit consumer adoption are separate work. Preserve existing documentation locations and consumer lockfiles. Historical dossiers and the legacy exemption manifest are unchanged.

Rollback is a reviewed revert of the guidance/template edits. This change has no data migration, live service rollout or automatic consumer file movement.

The last package validation failed on preexisting v2 metadata/schema violations in `specs/changes/bootstrap-product-context/`; this change's planning validation and all 48 validator tests passed. The baseline issue does not block reviewing this design, but CHECK-005 cannot be reported as passing while the full required entry point fails. Any remediation needs separately authorized scope; this change must not weaken validation or alter historical records to conceal it.

## Alternatives considered

- **A quickstart inside every change dossier:** resembles Spec Kit's per-feature validation guide, but would produce overlapping usage instructions and unstable entry points when this Harness archives a dossier. Use one living starting guide instead.
- **A mandatory folder and file per feature:** adds navigation and maintenance overhead for small changes. Introduce supporting guides only for workflows that need them.
- **A new quickstart template, scenario catalog or validator:** unnecessary for this scope. Existing Markdown guidance, acceptance scenarios, checks and evidence can express and review the behavior.
- **Documentation only in a final cleanup task:** increases the risk of stale instructions. Include necessary documentation with the work that changes its behavior.

## Validation plan

These are planned checks, not execution claims. During implementation/validation, capture the reviewed revision, actual commands and concise scenario outcomes using existing Tasks evidence fields. Manual walkthroughs assess instruction quality; they do not claim an automated composer or guarantee future agent behavior.

- **CHECK-001:** Apply the revised guidance to temporary illustrative cases: usable CLI with no guide, GUI workflow, existing guide/README section, and empty scaffold. Confirm necessary content and link destinations, no empty artifacts, and optional supporting detail. Simulate a dossier move in the illustrative layout and confirm living guide links remain valid. These are disposable validation materials, not new consumer templates.
- **CHECK-002:** Walk through a changed setup command, changed UI action, internal-only refactor and later revision of an existing workflow. Verify the instructions lead to updates of affected content, reuse of existing tasks/checks and evidence, and `unverified` results when access is missing. Check that no guide claims unimplemented behavior and no independent documentation report is required.
- **CHECK-003:** Use a requirement with success, invalid-input and boundary scenarios. Compare happy-path-only evidence with complete relevant coverage and with adequate preexisting tests. Confirm the review identifies missing or unexecuted scenarios and permits reuse without duplicate IDs or exhaustive test enumeration. A structural SDD pass must not erase the semantic gap.
- **CHECK-004:** Review the final diff and all affected Markdown targets; inspect base plus software, agent, hybrid, library and infrastructure composition. Confirm no new mandatory artifacts, profile copies, schema/validator changes, version-pin edits or language/security exceptions. Run `git diff --check` and inspect any new files separately.
- **CHECK-005:** Run `./scripts/validate/run.sh` using the declared validation dependencies and `python validators/sdd/validate.py --root . --change quickstart-scenario-coverage --phase <current-phase>` using `planning`, `implementation` or `delivery` as appropriate. The package entry point includes the existing validator regression suite. Keep the known baseline failure visible and do not claim readiness until required checks pass.

No new automated tests that merely assert prose wording are planned. Existing structural tests plus these focused behavioral walkthroughs are appropriate for the guidance-only change.

## Planning review

The developer approved the presented Design R1 and requested Tasks with the message "Aprove o design e defina as tasks." The canonical Design digest was computed before recording this approval. This authorizes preparation of Tasks, not approval of an unseen task plan or implementation. There are no unresolved design decisions; the known repository validation limitation is recorded above.
