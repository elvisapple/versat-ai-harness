---
sdd_version: 2
change: sdd-acceptance-regression
tasks:
- id: TASK-001
  description: Implement strict v3 metadata and digest dispatch with explicit bounded
    v2 compatibility.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-002
  description: Enforce local scenario coverage and cross-change impact and regression
    reference integrity.
  requirements:
  - REQ-001
  - REQ-004
  - REQ-005
  - REQ-007
  status: completed
- id: TASK-003
  description: Implement safe check-input snapshots and detect stale local execution
    evidence.
  requirements:
  - REQ-006
  - REQ-007
  status: completed
- id: TASK-004
  description: Validate acceptance assessments and findings without bypassing correction
    and approval gates.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-005
  - REQ-006
  - REQ-007
  status: completed
- id: TASK-005
  description: Integrate live delivery and historical inventory modes with trusted
    CI baseline selection.
  requirements:
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-006
  description: Apply the accepted policy and lifecycle contract through canonical
    Standards, workflows and v3 templates.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-008
  status: completed
- id: TASK-007
  description: Update living architecture, developer guidance and compatibility examples
    to match implemented behavior.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
- id: TASK-008
  description: Exercise and record behavioral walkthroughs for acceptance completeness,
    archived regression and authorized correction.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-008
  status: completed
- id: TASK-009
  description: Run the complete regression and documentation checks and record current
    evidence for all six planned checks.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  - REQ-007
  - REQ-008
  status: completed
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: f94ce3cf326057fa19ba58542c9e8ccbfa2226b9d916eb07f7367ceb4e5d9b66
    design: f04ed5cc2df7bac8f5a4181f9a9dabc9f99ee11260189ab71df5e96c195faaf4
  approval:
    source: Developer message in this conversation approving Tasks R1 and explicitly
      authorizing implementation and validation.
    quote: Aprovado, implemente e valide.
    revision: 1
    digest: 88506d87af07148903a82779fad85b6a2f3f6def79697aa809ce0d1b095b84ed
validation:
  plan_digest: 88506d87af07148903a82779fad85b6a2f3f6def79697aa809ce0d1b095b84ed
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/sdd-acceptance-regression/validation.md
    revision: Local working-tree snapshot a80442368084187f5f8f6ab8686824edb2b94830c19c849e41742584de0e4778;
      full 125-test run and reviewer walkthrough; 2026-10-01
  - check: CHECK-002
    result: pass
    evidence: docs/validation/sdd-acceptance-regression/validation.md
    revision: Local working-tree snapshot a80442368084187f5f8f6ab8686824edb2b94830c19c849e41742584de0e4778;
      full 125-test run and reviewer walkthrough; 2026-10-01
  - check: CHECK-003
    result: pass
    evidence: docs/validation/sdd-acceptance-regression/validation.md
    revision: Local working-tree snapshot a80442368084187f5f8f6ab8686824edb2b94830c19c849e41742584de0e4778;
      full 125-test run and reviewer walkthrough; 2026-10-01
  - check: CHECK-004
    result: pass
    evidence: docs/validation/sdd-acceptance-regression/validation.md
    revision: Local working-tree snapshot a80442368084187f5f8f6ab8686824edb2b94830c19c849e41742584de0e4778;
      full 125-test run and reviewer walkthrough; 2026-10-01
  - check: CHECK-005
    result: pass
    evidence: docs/validation/sdd-acceptance-regression/reviewer-walkthrough.md
    revision: Local working-tree snapshot a80442368084187f5f8f6ab8686824edb2b94830c19c849e41742584de0e4778;
      full 125-test run and reviewer walkthrough; 2026-10-01
  - check: CHECK-006
    result: pass
    evidence: docs/validation/sdd-acceptance-regression/validation.md
    revision: Local working-tree snapshot a80442368084187f5f8f6ab8686824edb2b94830c19c849e41742584de0e4778;
      full 125-test run and reviewer walkthrough; 2026-10-01
closure: prepared
---

# Tasks

- [x] TASK-001 — Implement v3 metadata, digest dispatch and bounded compatibility.
- [x] TASK-002 — Enforce scenario coverage, impact and regression references.
- [x] TASK-003 — Implement safe input snapshots and evidence freshness.
- [x] TASK-004 — Validate acceptance assessments, findings and correction gates.
- [x] TASK-005 — Integrate historical inventory, live delivery and CI selection.
- [x] TASK-006 — Apply the contract through Standards, workflows and templates.
- [x] TASK-007 — Update living documentation and exercise its examples.
- [x] TASK-008 — Record behavioral acceptance and regression walkthroughs.
- [x] TASK-009 — Run all planned checks and record current validation evidence.

## Execution baseline

Implement only after this Tasks revision is approved and execution is explicitly requested. [Proposal/Requirements R1](proposal.md) and [Design R1](design.md) are approved; [ADR-0014](../../../docs/decisions/0014-sdd-acceptance-and-regression.md) records the accepted architectural decision. Their substantive content remains unchanged.

The implementation starts from Harness 0.3.0 at `ac69894` on `codex/sdd-acceptance-regression`. Resolve policies through the repository's `standards/index.yaml`; preserve the separate responsibilities of Standards, SDD, Skills and validators. This dossier stays v2 under the accepted bounded transition. Its actual approved stage digests are recorded in compatibility metadata only during authorized implementation, after Gate 3.

No task requires merge, deployment, release publication or consumer upgrade to complete. Required remote CI remains a separately observed delivery gate; local tests do not prove it ran. Subsequent requested archival uses the existing workflow and this dossier without another functional change.

## Deliverables and completion conditions

### TASK-001 — Versioned metadata and compatibility

Affected locations: `sdd/schemas/`, `sdd/metadata.md`, `validators/sdd/validate.py`, a new `sdd/compatibility.json`, and behavioral tests under `tests/validators/`.

Add strict v3 schema definitions for the approved impact, coverage, regression, check method/input, execution, assessment and finding records. Preserve the existing v2 schema and digest semantics and pre-v2 legacy manifest. Implement version dispatch and compatibility validation, not a fallback that silently accepts old or mixed fields. Provide reusable synthetic v3 dossier builders alongside existing v2 fixtures without changing the contract tested by the old regression cases.

Completion requires:

- v3 drafts accept absent future-stage artifacts and reject invalid shapes, unknown keys, duplicate IDs and mixed versions;
- historical v2 entries bind all four files by exact hashes; in-flight entries bind actual approved stage digests and still require original v2 approvals/evidence rules;
- unlisted v2, changed historical files, changed in-flight planning and duplicate exemptions fail with actionable diagnostics;
- the existing pre-v2 manifest and delivered dossier bytes remain unchanged;
- the introducing change's entry uses real approvals, not generated approval examples or invented future digests;
- tests demonstrate valid and invalid compatibility, bookkeeping exclusions and content edits invalidating approval.

Supports CHECK-001 and CHECK-004. Implement the new machinery without switching authoring defaults until the integrated validator is ready.

### TASK-002 — Coverage and historical origin resolution

Affected locations: SDD validator reference/coverage logic, canonical source-digest helpers and tests under `tests/validators/`.

Resolve local acceptance positions under their approved revision and change-qualified historical requirements in active/archive storage. Validate current-contract references, the proposal-local baseline alternative, impact dispositions, justified no-impact and required regression mappings. Keep origin resolution read-only and bounded to declared references. Preserve existing requirement-to-task/check coverage.

Completion requires tests for many-to-many coverage, omitted error/boundary scenarios despite a passing happy-path check, duplicate/out-of-range references, exclusions without reasons, scenario edits/reordering, duplicate change storage, two origins sharing `REQ-001`, changed/missing historical sources, baseline-only history and approved supersession with replacement checks. Active/archive moves must preserve source identity. Tests must distinguish a reviewed no-impact conclusion from unresolved impact and must not require a new scenario ID or registry.

Supports CHECK-001 and CHECK-002. The validator enforces declared mappings; workflow/reviewer evaluation assesses test adequacy.

### TASK-003 — Check-input snapshots

Affected locations: validator snapshot helpers and `--input-digest` CLI handling, execution-record validation and temporary-filesystem tests.

Implement the approved deterministic file-tree digest including sorted paths, file types, bytes, executable flags, new/deleted files and explicit missing-path markers. Bind scopes/exclusions through approved Design; exclude the current dossier and declared outputs without silently applying Git ignore rules. Compare before/after execution digests and current live inputs while preserving stage/plan digest checks.

Completion requires:

- mutations to code, tests, fixtures or configuration invalidate old results with an unchanged Tasks plan;
- a change during execution makes the result unusable as a pass;
- permitted evidence-output edits and dossier moves do not cause circular invalidation;
- absolute/escaping paths, symlinks, special files and conflicting explicit input/output paths are rejected;
- directory enumeration detects additions and deletions, including previously absent declared paths;
- inventory does not assert current freshness, and editable runtime labels or HTTPS references do not authenticate execution;
- the helper is read-only, executes no check text and uses no network.

Supports CHECK-003. Record external execution context as evidence without attempting automatic remote-state verification.

### TASK-004 — Acceptance outcomes and correction records

Affected locations: validator assessment/finding aggregation, gate/readiness logic and tests under `tests/validators/`.

Validate one disposition per applicable local scenario and retained regression obligation, bind declared passing assessments to required current passing check results, and aggregate requirement status. Require approved exclusions for `not-applicable`. Validate stable finding identity, source, state, evidence and resolution records; retain the original planning approval rules when task content changes.

Completion requires tests showing that completed task boxes cannot hide missing/partial behavior, contradictory implementation, open scope concerns, failed regressions, absent assessments or unverified evidence. Test reused finding identities, resolved findings with supporting evidence, invalid/dangling task references, and stale approvals after changed task planning. Preserve failure versus unavailable-verification outcomes. A successful record check must explicitly disclaim semantic/execution authenticity.

Supports CHECK-001, CHECK-002 and CHECK-004. Actual agent behavior and permission boundaries are exercised in TASK-008.

### TASK-005 — Phase integration and CI delivery selection

Affected locations: `validators/sdd/validate.py`, `scripts/validate/run.sh`, `.github/workflows/validate.yml`, and synthetic Git/CLI tests.

Integrate v3 phases with historical archive inventory and explicit live selected delivery. Add trusted `--baseline` selection for new/modified archive dossiers using NUL-delimited Git paths and both sides of moves. Pass actual platform PR-base/push-before revisions through CI environment data and normal checkout configuration. Missing baseline objects cannot yield an empty successful selection.

Completion requires tests covering archived stored-record checks without rehashing obsolete inputs, live delivery detecting current stale/failed/missing evidence, active drafts requiring no future results, archive moves retaining delivery prerequisites, modified/deleted archived artifacts, unavailable baseline, and explicit selected delivery without Git. Document the limited scope of inventory without a baseline. Existing approval, completed-task, evidence-path and archived-record controls remain enforced.

Supports CHECK-003, CHECK-004 and CHECK-006. Test the baseline integration locally with controlled refs; record remote CI as unverified until observed. Profile-required suites must not disappear when targeted checks are selected.

### TASK-006 — Canonical policy, workflows and authoring

Affected locations: `standards/core/testing.md`, `sdd/process.md`, `sdd/workflows/`, `sdd/templates/`, `sdd/metadata.md`, and skill routing references only where needed.

Apply the approved obligations for scenario coverage, effective-contract impact, maintained regression suites, current evidence and semantic completeness. Describe the findings/correction/revalidation loop within existing gates: validation-only does not fix code; routine authorized fixes remain within approved tasks; new task-plan content reopens the proper gate. Switch templates to v3 after TASK-005 and keep the four-file workflow and public skill unchanged.

Completion requires consistent schemas/templates/workflow examples and an explicit account of exclusions, manual verification, unavailable environments, supersession, test retirement and current versus historical evidence. Policies remain in Standards and are located through the index. No copied standards list, universal TDD rule, fixed test counts, new scenario catalog or extra public convergence command is added. Keep required suites and observed CI obligations visible.

Supports CHECK-001, CHECK-002, CHECK-004 and CHECK-005. Treat any newly discovered substantive departure from the approved Design as replanning rather than an implementation shortcut.

### TASK-007 — Living documentation and adoption guidance

Affected locations: `sdd/README.md`, `validators/sdd/README.md`, `validators/README.md`, `docs/architecture/overview.md`, and relevant root README/project-template guidance.

Explain the implemented v3 records, existing entry point, new snapshot and baseline options, outputs/exit statuses and correction/resumption behavior. Provide concise worked examples for a new feature, a follow-up to an archived requirement, intentional supersession and an unavailable check. Include compatibility adoption, unchanged history, the bounded transition for this change and safe rollback limitations. Reuse shared base guidance without duplicating profile policies.

Completion requires exercising affected documented commands and comparing results with their stated outcomes. Verify local links and use disposable fixtures for examples, including the synthetic duplicate-payment case without adding a real finance integration. Architecture documentation must describe delivered behavior and trust limits. Do not claim a published release, consumer upgrade or remote delivery.

Supports CHECK-005 and CHECK-006. Reuse functional evidence when it also verifies an example; no separate report is required solely for documentation.

### TASK-008 — Behavioral walkthroughs

Affected locations: `tests/skills/scenarios.md` and durable evidence under `docs/validation/sdd-acceptance-regression/`.

Extend existing behavioral cases and execute recorded agent or reviewer walkthroughs against disposable projects as allowed by CHECK-005. Exercise success/error/boundary completeness, all tasks checked with a missing behavior, an archived duplicate-prevention regression despite a passing new path, reused tests, justified no-impact, manual verification, unavailable execution and approved supersession. Exercise validation-only versus authorized correction, changed task-plan approval, stale evidence on resumption and repeated findings without duplicated work.

Completion requires actual observations, artifact revisions/diffs, actions and outcomes. A reviewer walkthrough is labeled as such and cannot claim that an autonomous-agent evaluation ran. Mocked validator metadata alone is insufficient. If a required behavioral check cannot be exercised, retain `unverified` and its cause rather than treating scenario prose as execution. No delegation or new external agent service is required by this task.

Supports CHECK-005 and the semantic aspects of CHECK-001/CHECK-002/CHECK-004. Fixtures use synthetic data and may reuse the deterministic suite's test setup.

### TASK-009 — Final regression and evidence

Affected locations: validator regression tests, durable check evidence and this dossier's validation bookkeeping.

Run all six CHECK methods from the approved Design after the integrated implementation and relevant documentation settle. Use `python -m unittest discover -s tests/validators -p 'test_*.py'`, `./scripts/validate/run.sh`, selected phase checks and the newly implemented snapshot/baseline commands on controlled fixtures. Confirm retained approval/gate, reference-safety, legacy, template-composition and language behavior alongside the new positive and negative cases. Fix in-scope defects and rerun affected checks.

Completion requires:

- all eight requirements and their relevant acceptance scenarios have observed evidence, including retained historical behavior;
- CHECK-001 through CHECK-006 each have an actual recorded outcome and durable evidence at a repository-relative path outside the movable dossier or an observed HTTPS run URL;
- results bind to the real current Tasks digest and identify the tested working-tree snapshot/run;
- local document links and diffs pass checks and historical bytes/exceptions remain intact;
- v3 fixture results are distinguished from this dossier's explicitly permitted v2 transition; no v3 assurance claim is inferred from its v2 status;
- unavailable verification, semantic limits and remote CI/review/merge status are stated separately.

Do not mark this task complete with a required CHECK failing or unverified. Leave any unavailable requirement visibly pending/blocked, explaining the external prerequisite. Remote publication or archive preparation occurs only under its separately authorized lifecycle step; neither is a hidden completion dependency here.

## Dependencies

| Task | Prerequisites | Checks supported |
|---|---|---|
| TASK-001 | Current Gate 3 approval and explicit implementation request | CHECK-001, CHECK-004 |
| TASK-002 | TASK-001 | CHECK-001, CHECK-002 |
| TASK-003 | TASK-001 | CHECK-003 |
| TASK-004 | TASK-002, TASK-003 | CHECK-001, CHECK-002, CHECK-004 |
| TASK-005 | TASK-004 | CHECK-003, CHECK-004, CHECK-006 |
| TASK-006 | TASK-005 | CHECK-001, CHECK-002, CHECK-004, CHECK-005 |
| TASK-007 | TASK-006 | CHECK-005, CHECK-006 |
| TASK-008 | TASK-007 | CHECK-005; semantic portions of CHECK-001, CHECK-002, CHECK-004 |
| TASK-009 | TASK-001 through TASK-008 | CHECK-001 through CHECK-006 |

TASK-002 and TASK-003 have no mutual functional dependency, but shared validator edits must be coordinated. This dependency statement is not authorization to spawn agents. Behavioral tests belong with each implementation task; TASK-009 consolidates current evidence rather than postponing all testing until the end.

## Requirement coverage

| Requirement | Principal delivery tasks | Required Design checks |
|---|---|---|
| REQ-001 — Planning scenario coverage | TASK-001, TASK-002, TASK-006 | CHECK-001, CHECK-005 |
| REQ-002 — Implementation completeness | TASK-001, TASK-004, TASK-008 | CHECK-001, CHECK-005 |
| REQ-003 — Correction and revalidation | TASK-004, TASK-006, TASK-008 | CHECK-004, CHECK-005 |
| REQ-004 — Cross-change impact | TASK-002, TASK-006, TASK-008 | CHECK-002, CHECK-005 |
| REQ-005 — Permanent regression coverage | TASK-002, TASK-004, TASK-006, TASK-008 | CHECK-002, CHECK-005 |
| REQ-006 — Current evidence | TASK-003, TASK-005, TASK-009 | CHECK-003, CHECK-006 |
| REQ-007 — Deterministic enforcement | TASK-001 through TASK-005 | CHECK-001, CHECK-002, CHECK-003, CHECK-004, CHECK-006 |
| REQ-008 — Compatible adoption | TASK-001, TASK-005 through TASK-009 | CHECK-004, CHECK-005, CHECK-006 |

TASK-007 documents the affected usage and TASK-009 validates the complete scope. The table supplements, rather than replaces, each requirement's acceptance scenarios and the detailed check methods in Design.

## Risks and controls

- **Compatibility becoming an escape hatch:** use only explicitly reviewed entries, verify hashes/digests and preserve the original v2 gates. Do not automatically create exemptions for failing dossiers.
- **False confidence in coverage or hashes:** tests verify structural enforcement; recorded walkthroughs assess behavior; input scope and external-state limits remain visible.
- **Archive inventory mistaken for readiness:** retain separate live selection and fail when required baseline context is unavailable.
- **Stale validation during ongoing edits:** rerun affected checks after implementation/test/config changes and record actual inputs, never refresh a hash on an old result.
- **Policy drift or excess ceremony:** reuse canonical rules, four dossier files, existing IDs, maintained suites and evidence; keep profile-required CI checks.

No material unresolved decision blocks review of Tasks R1. External CI, PR review and release are later delivery facts, not claims made by this plan.

## Planning review

- Proposal/Requirements R1 and Design R1 remain approved. The authorized administrative Proposal link amendment and its updated upstream binding are recorded explicitly; Design and Tasks content digests remain unchanged.
- ADR-0014 is Accepted based on the same explicit Design approval.
- Tasks R1 was approved in this conversation with “Aprovado, implemente e valide.” The same message explicitly authorizes implementation and validation.
- Approved Tasks digest: `88506d87af07148903a82779fad85b6a2f3f6def79697aa809ce0d1b095b84ed`. Planning is complete; execution follows the approved scope.

## Progress

TASK-001 through TASK-009 are complete. Implemented strict v3 records, scenario/impact/regression enforcement, safe input snapshots, acceptance findings, explicit compatibility and CI baseline selection. Updated canonical Standards, workflows, templates and living guidance. The full suite passed with 125 tests and the recorded reviewer walkthrough exercised actual synthetic behavior. Design and Tasks substantive digests remain unchanged; the authorized relocation-only Proposal amendment is recorded in its review history.

## Validation evidence

CHECK-001 through CHECK-006 passed locally on the source snapshot recorded in [the validation report](../../../docs/validation/sdd-acceptance-regression/validation.md). The [reviewer walkthrough](../../../docs/validation/sdd-acceptance-regression/reviewer-walkthrough.md) maps requirement scenarios to actual observations and deterministic cases. Source inputs, logs and byte/link checks are retained outside the dossier. This change uses its approved bounded v2 transition; its own validator result is not v3 certification. Remote CI, PR review, merge, release and consumer adoption remain unverified.

## Delivery

The developer explicitly authorized the presented one-line administrative link correction while preserving the planning approvals, and requested correction of missing pre-PR archival enforcement before closure. The existing precondition is now enforced by a local `--require-archive` preflight and non-draft PR/main-push CI, with changed active/archive selection and regression tests. See [the review](../../../docs/validation/sdd-acceptance-regression/pr-preflight-review.md).

All 125 tests and the reviewer walkthrough passed against the renewed source snapshot before archival. Documentary closure is prepared in specs/archive/sdd-acceptance-regression in this implementation branch. Final live preflight, reference audit and package checks verify the resulting content before any PR submission. No PR, merge, deployment, release publication or consumer adoption is claimed.
