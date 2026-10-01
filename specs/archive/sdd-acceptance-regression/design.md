---
sdd_version: 2
change: sdd-acceptance-regression
requirements:
- REQ-001
- REQ-002
- REQ-003
- REQ-004
- REQ-005
- REQ-006
- REQ-007
- REQ-008
adrs:
- docs/decisions/0014-sdd-acceptance-and-regression.md
validation:
- id: CHECK-001
  description: Exercise scenario coverage, exclusions and semantic assessment records
    with valid and invalid synthetic dossiers.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-007
  required: true
- id: CHECK-002
  description: Exercise cross-change references, archived origin, retained behavior
    and approved supersession using synthetic regression fixtures.
  requirements:
  - REQ-004
  - REQ-005
  - REQ-007
  required: true
- id: CHECK-003
  description: Verify input snapshot freshness, added and deleted files, path safety
    and separation of historical from current evidence.
  requirements:
  - REQ-006
  - REQ-007
  required: true
- id: CHECK-004
  description: Verify phase gates, correction records, metadata compatibility and
    immutable historical dossiers.
  requirements:
  - REQ-003
  - REQ-007
  - REQ-008
  required: true
- id: CHECK-005
  description: Run recorded agent or reviewer walkthroughs for incomplete acceptance,
    archived regression, correction authorization and resumption.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-008
  required: true
- id: CHECK-006
  description: Run the complete repository validation entry point and verify revised
    lifecycle usage examples, CI selection and compatibility guidance.
  requirements:
  - REQ-006
  - REQ-007
  - REQ-008
  required: true
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: f94ce3cf326057fa19ba58542c9e8ccbfa2226b9d916eb07f7367ceb4e5d9b66
  approval:
    source: Developer message in this conversation on 2026-10-01 approving the presented
      Design R1 and ADR-0014.
    quote: Sim, aprovado.
    revision: 1
    digest: f04ed5cc2df7bac8f5a4181f9a9dabc9f99ee11260189ab71df5e96c195faaf4
---

# Design

## Current state

Harness 0.3.0 at `ac69894` uses four dossier files, v2 schemas and content-bound approvals. `RepositoryValidator.traceability()` checks requirement/check/task references; `evidence()` checks recorded results and the Tasks plan digest. The validator cannot identify a missed acceptance scenario from a requirement-level check reference, nor detect changed code from the plan digest alone.

The Testing Standard already requires relevant scenario coverage. This design operationalizes that policy and adds cross-change regression records. It preserves ADR-0013's lifecycle, evidence trust boundary and separation of documentary archive from merge.

Applicable policies are resolved through `standards/index.yaml` at this revision, including its `core.always` set. No consumer project identity is inferred. [ADR-0014](../../../docs/decisions/0014-sdd-acceptance-and-regression.md) proposes the versioned extension and the distinction between historical and live validation.

## Proposed design

### 1. Extend the four-file contract with SDD metadata v3

Use `sdd_version: 3` for newly authored dossiers after adoption. Keep v2 schemas and digest behavior available through explicit compatibility handling. Do not add a fifth primary artifact or a second public skill.

| Artifact | Added responsibility |
|---|---|
| Proposal | Reviewed impact on earlier contracts, including a justified no-impact conclusion. |
| Requirements | Existing requirement IDs and acceptance strings remain the source of scenarios. |
| Design | Scenario/check coverage, regression selection, check methods and declared input scopes. |
| Tasks | Current executions, acceptance assessments and tracked findings, separate from the approved task plan. |

New structured fields use strict schemas, reject unknown keys and duplicate identifiers, and participate in the existing phase and approval chain. Planning does not require future execution evidence. Proposed field names below define the implementation contract; illustrative values are not executed results.

### 2. Scenario references and planning coverage

A local scenario reference is `{requirement: REQ-001, scenario: 1}`, where `scenario` is the one-based position in that requirement's existing `acceptance` array. There is no manually maintained scenario ID or duplicate case catalog. A scenario reference is revision-bound by the Proposal/Requirements approval digest; reordering or editing scenarios reopens the existing gate rather than silently changing what a reference means.

Design adds `coverage`, containing exactly one disposition per local acceptance scenario:

- `scenario`: the local reference;
- `applicability`: `required` or `not-applicable`;
- `checks`: existing CHECK identifiers, with at least one required check for a required scenario;
- `reason`: mandatory for an exclusion and optional otherwise.

Existing requirement-to-task coverage connects each scenario to planned work through its requirement. A check may cover multiple scenarios and requirements. Exclusions require Design review, cannot cancel an applicable approved requirement and must not be used to hide unavailable execution. If that review changes scope, reopen Proposal/Requirements first.

Planning coverage reports missing scenario mappings, missing required checks and missing task coverage separately. Semantic review must still assess whether the selected method is adequate: a reference is not proof that assertions exercise the scenario.

### 3. Cross-change impact and the effective contract

Proposal adds `impact` with `state: assessed | unresolved`, a nonempty `summary`, and `items`. An empty item list with `state: assessed` requires a scope-based no-impact rationale in the summary. An unresolved assessment may be drafted but blocks approval/implementation readiness.

Each impact item records:

- `source`: an earlier `{change, requirement, scenarios, requirements_digest}`; `scenarios` selects the affected acceptance positions, and the digest binds the canonical parsed Requirements metadata and normalized body, independent of its active/archive path;
- `current_contract`: `{path, locator, digest}`, identifying the reviewed living document and section; when no suitable living document exists, use `{change, artifact: proposal, locator}` for an explicitly established baseline in this proposal, resolved by dossier identity rather than its movable directory;
- `effect`: `preserve`, `extend` or `supersede`;
- `targets`: local requirement IDs defining the current work;
- `reason`: affected behavior, selection rationale and any intentional replacement.

A source is resolved by change ID in both `specs/changes/` and `specs/archive/`; duplicate copies are an error. A requirement ID without its change ID is insufficient. A source may be legacy, but reading its historical requirement does not confer current approval or execution evidence. Only direct declared sources are resolved; this is not an automatic transitive dependency graph. An affected baseline with no historical dossier can use a current-contract-only item with an explicit origin-unavailable reason and reviewed local requirements; it cannot fabricate a source ID. Missing declared sources remain unresolved.

Use a canonical content helper for source digests. The current proposal's own baseline locator uses the approved Proposal/Requirements digest as its revision binding rather than embedding a self-referential file hash. External URLs can provide context but cannot replace a local reviewable baseline for offline enforcement.

During live planning, verify source and baseline bindings. Editing a living contract as part of an approved implementation is expected: impact retains the reviewed pre-change baseline, while current behavior and the replacement contract are checked by the approved validation plan. Do not invalidate approval simply because the planned living-document update happened. A changed historical source, however, requires re-resolving the origin and its impact before readiness is claimed.

### 4. Regression obligations and selection

Design adds `regression` entries pointing to impact source/scenario tuples, or to the current-contract locator for baseline-only items. Entries contain `checks` and a `rationale`. Every affected scenario marked `preserve` or `extend` needs a required check. Superseded scenarios require replacement local requirements/checks and an explicit explanation of any test retirement; they do not require the obsolete behavior to continue passing.

Tests and evals stay in the consumer's normal maintained suites, independent of dossier location. A reference to a prior passing run is historical context only. Reuse an adequate existing test and record its current result against the new change's CHECK identifier. Missing historical tests become work in the new change.

Each planned check extends its existing fields with:

- `method.kind`: `automated`, `manual` or `review`;
- `method.procedure`: a reproducible command or concrete steps and expected observations;
- `method.reason`: required when a manual/review method substitutes for useful automation;
- `inputs`: reviewed repository-relative file/directory roots and explicit exclusions;
- `outputs`: declared evidence/output paths excluded from input hashing;
- `execution`: `local` or `ci`, identifying where the required result must be observed.

An agent/reviewer selects checks based on affected behavior and risk. This does not remove profile-required CI suites. The plan lists those suites as required CI checks even if targeted local tests are also used. No command is executed merely because a validator reads `method.procedure`; invocation remains with the authorized executor.

For example, a new payment-processing change maps an archived duplicate-prevention scenario to `CHECK-002`, whose method invokes an existing duplicate-submission test. The new success-path test alone cannot satisfy that retained scenario. If the old test is removed, missing coverage or a changed input snapshot prevents reuse of its old evidence.

### 5. Acceptance assessment and corrections

Tasks extends the existing `validation` object with `assessments` and `findings`. These are evidence bookkeeping, excluded from task-plan approval digests like existing `validation.results`; scope and check definitions remain in approved artifacts.

`assessments` contains one record for each local scenario and retained regression obligation. Each record references its obligation, supporting CHECK IDs and evidence, and records `pass`, `fail`, `unverified` or `not-applicable`. A passing assessment requires current passing results for its required supporting checks, plus an explanation connecting observed behavior to the obligation. `not-applicable` is valid only for a previously approved exclusion. The report derives requirement summaries from their scenarios: any failure fails the requirement; otherwise any missing/unverified item leaves it unverified; exclusions are listed rather than counted as passes.

The agent/reviewer inspects current affected code and relevant documented behavior even when Tasks checkboxes are complete. Record gaps as `missing`, `partial`, `contradicts` or `unrequested`. Each finding has a stable local FIND identifier, obligation or affected-plan reference, evidence, `open | resolved` state and corrective task references when they exist. Reuse an existing open finding for the same obligation/gap; do not append duplicate tasks on every run. Resolution records the disposition and current supporting evidence. An unrequested addition must be justified against approved intent, removed under authorized work, or sent through replanning; the validator cannot decide that judgment.

An open confirmed gap prevents completeness. Unavailable evidence remains unverified. Validation-only records findings without fixing code or modifying the approved task plan. Authorized routine fixes within existing tasks can continue and rerun affected checks. New task-plan content reopens Tasks; changes to design or requirements reopen the earliest affected gate. There is no automatic append-only exception to approval rules and no extra public convergence command.

### 6. Evidence freshness against implementation inputs

Extend each execution result with `input_digest_before`, `input_digest_after` and its observed execution context. Preserve the current `check`, `result`, `evidence` and `revision` fields, and the plan digest. For a valid pass, the before/after input digests must agree and, during live validation, equal a freshly computed digest. A change during execution invalidates that run. Never copy a freshly computed digest onto an old result to make it current.

Add a read-only CLI helper `--input-digest CHECK-001 --change <id>` to the existing validator entry point. It resolves the approved check scope and computes a canonical SHA-256 over sorted relative paths, entry types, file bytes and executable flags. Directories are recursively enumerated on every invocation, so new and removed files change the digest; a declared missing path has an explicit absence marker. Include source, tests, fixtures, relevant guides, lockfiles and execution configuration through reviewed roots. The root list and exclusions themselves are bound by Design approval.

The helper rejects absolute/escaping paths, symlinks, special files and conflicting input/output declarations. Exclude `.git`, the current dossier and declared output paths to avoid self-reference. An explicitly named source input cannot also be an output; an output nested under a broad input root is permitted only as an explicit reviewed exclusion. Do not silently apply Git ignore rules: omitted caches, environments and generated files need explicit exclusions. A project may use narrow reviewed roots or a broad root with explicit exclusions. Secrets must not be included; hashes are evidence of file state, not permission to retain sensitive inputs.

The current dossier is represented by approval/plan digests instead of raw file hashes. Referenced historical sources have their own revision bindings. This permits the active-to-archive move and evidence bookkeeping without a circular hash. If a check intentionally tests dossier contents, use a separate synthetic fixture as an ordinary input or a documentary review bound to the stage digests.

Freshness detects changes inside declared scopes, not undeclared dependencies, remote services, installed runtimes or maliciously edited evidence. Record relevant runtime/service/environment context without secrets and rerun on known external changes; unknown external state remains unverified. The executor obtains before/after snapshots around the actual check. The local validator never authenticates execution solely from a digest or HTTPS reference.

### 7. Separate current readiness from historical validation

Retained regression tests operate on the current product. Historical execution records remain evidence about the older assessed snapshot. Rehashing every archived change against today's code would incorrectly fail history after intentional later changes.

- A selected `--change <id> --phase delivery` always performs live freshness, acceptance and completion checks, whether its dossier is active or prepared in the archive.
- A repository inventory check validates archived records under their recorded contract, including completeness, references and stored snapshot consistency, but does not compare historical input digests with today's implementation. Stored current-contract locators are historical baseline descriptions in this mode: later supersession/removal of a living document does not invalidate them. Retained dossier origins and evidence files must still resolve; obsolete local input files need not exist. Its output explicitly labels this historical scope and cannot establish current delivery readiness.
- Active dossiers with recorded results receive live freshness checks; a stale result is reported as `unable-to-verify` even when the default phase is planning. Drafts without results do not require them.
- Repository CI must additionally run live delivery checks for newly archived or modified archive dossiers. Extend the entry point with a trusted local `--baseline <git-ref>` argument and determine changed dossier IDs from NUL-delimited Git paths, accounting for both old and new paths of moves. An explicitly selected change remains usable without Git.
- CI obtains the PR base or push-before revision from event metadata, checks it out/fetches it through normal checkout configuration, and passes it as data. Missing baseline objects produce an explicit failure, not a silently empty selection. Creation or modification of archived artifacts runs live checks; deletion is reported for explicit reviewed retirement and cannot certify delivery. A workflow must not accept a user-supplied arbitrary baseline as proof of the platform's required-check scope.

The baseline is used only to select current delivery candidates, never to infer that an archive was merged. Local users without a baseline can inspect inventory or validate an explicitly selected change, but cannot claim that all changed archives passed live delivery checks. Existing path safety, approval, task-completion and recorded-pass requirements for archives remain in force.

## Boundaries and contracts

| Location | Planned implementation responsibility |
|---|---|
| `standards/core/testing.md` | Canonical retained-behavior, coverage, evidence freshness and exclusion obligations. |
| `sdd/process.md`, `sdd/workflows/`, `sdd/metadata.md` | Apply obligations within the existing gates; define live versus historical checks and correction behavior. |
| `sdd/templates/`, `sdd/schemas/` | v3 authoring and strict records; preserve v2 parsing/digests for reviewed compatibility. |
| `validators/sdd/validate.py` and small internal helpers | Reference resolution, coverage, snapshots, result aggregation and phase enforcement. Keep the existing public CLI. |
| `scripts/validate/run.sh`, `.github/workflows/validate.yml` | Run inventory, targeted live checks and validator regression tests; pass trusted baseline context. |
| `tests/validators/`, `tests/skills/scenarios.md` | Deterministic behavioral fixtures and separately recorded agent/reviewer evaluations. |
| `sdd/README.md`, relevant README/template guidance | Explain authoring, selection, correction, current validation and historical limitations with working examples. |

Keep Python 3.11+, the existing validation dependencies and output/exit conventions: `pass`/0, `fail`/1, `unable-to-verify`/2. Invalid records and observed failures are failures; missing executions, unresolved context and detectably stale evidence are unverified. Both block a live readiness claim. Do not add network access, automatic test execution or an LLM call to the validator.

## Data, security and permissions

These are versioned repository records, not production business data. Reuse existing strict YAML/JSON parsing and safe reference handling. Hashing must not follow links outside the declared tree, execute check text or disclose file contents. Apply the Security and Language Standards to logs, methods and evidence. Tests use synthetic data and temporary repositories. Remote CI URLs are references whose authenticity remains outside local validation.

Approval records remain auditable declarations bound to content; neither schema changes nor hashes authenticate the approver. This Design authorizes no remote mutation, consumer migration or release. A necessary ADR remains Proposed until its actual review disposition is recorded.

## Operations and observability

Output counts for scenario coverage, preserved regression obligations, observed results, unresolved findings and stale evidence, with affected requirement/check/source paths. Distinguish planning coverage, semantic assessment, execution and historical inventory. Extend structured findings with specific codes while retaining existing status fields and exit meanings.

Use check-scoped hashing with cached file hashes within one validator invocation to avoid rereading shared inputs unnecessarily; do not persist an unchecked cache across runs. No background service, database, automatic retry system or external monitoring is introduced. Failure recovery is correction of the named record or authorized rerun of the affected check, followed by validation.

## Migration, rollout and rollback

1. Add v3 support alongside unchanged v2 schemas and digest normalization. Templates default to v3 only when the new validator and guide are delivered together. The metadata version is independent of the eventual semver release number; publication remains separate work.
2. Preserve the existing pre-v2 `sdd/legacy-changes.json` contract. Add `sdd/compatibility.json` version 1 for explicitly reviewed v2 compatibility: `historical` entries hold the change ID, reason and exact hashes of the four files; `in_flight` entries hold the change ID, reason and three approved stage digests. A dossier may occur in only one compatibility mechanism. Consumer manifests remain project-local.
3. Unknown or mixed-version dossiers fail; an unlisted v2 dossier cannot evade v3 by deleting new fields. A historical entry is immutable and never proves current v3 readiness. An in-flight entry may finish under v2 only with the original stage digests and real v2 approvals, task/evidence rules and explicit output that v3 assurances were not mechanically checked. Changed substantive planning requires a reviewed migration to v3, with actual approvals for the changed artifacts; progress/evidence updates are not planning edits.
4. This change is already being planned under v2. After actual Gate 3 approval, record its real stage digests as the bounded in-flight entry during implementation. Do not invent those values now, migrate its metadata mid-gate or claim a v3 pass for its own dossier. Exercise v3 through positive/negative synthetic dossiers and recorded behavioral walkthroughs, and apply the semantic regression review to this work. The immutable archived `quickstart-scenario-coverage` can be inventoried by exact bytes; pre-v2 dossiers retain their existing exceptions.
5. Keep compatibility rules and any manifest additions reviewable through PR/CODEOWNERS. A manifest is not an authentication mechanism. Additions are never generated automatically merely because validation failed.
6. Consumer adoption is an explicit exact-release maintenance update. Old archived dossiers do not need migration to serve as requirement origins. Resuming substantive work on them creates a new change or performs a specifically reviewed migration.

Rollback reverts the new implementation and authoring defaults through review without editing delivered history. A prior validator cannot process v3 artifacts: retain the selected newer validator or deliberately migrate those active artifacts with approval before downgrading a consumer. Do not erase version markers to force old tooling to accept them.

## Alternatives considered

- **Workflow prose only:** smaller change, but cannot detect missing declared scenario rows, broken cross-change links or stale local snapshots. Retain prose for semantic judgment and add bounded deterministic checks.
- **One new global requirements/test registry:** unnecessary duplication and ownership complexity. Reuse existing acceptance arrays and maintained suites with change-qualified origin references.
- **One immutable ID per scenario:** stable but adds authoring overhead. Use array positions bound to an approved revision; edits intentionally invalidate old mappings.
- **Whole Git commit as the only freshness key:** misses uncommitted work and causes circular delivery bookkeeping or irrelevant invalidation. Use reviewed input scopes and stage digests, retaining actual run/revision labels as context.
- **Always rerun every historical requirement:** obsolete behavior can intentionally be superseded and historical artifacts are not the effective current contract. Select retained behavior through reviewed impact records while preserving required suites.
- **Automatically append corrective tasks:** can mutate an approved plan without review. Track findings first and use existing revision gates for new task content.
- **Silently strengthen v2:** breaks old schemas and approvals or makes new assurance optional without a clear contract. Introduce v3 with explicit, bounded compatibility.

## Validation plan

All checks below are planned implementation checks, not results of this Design turn. Reuse the existing entry points: `python -m unittest discover -s tests/validators -p 'test_*.py'`, `python validators/sdd/validate.py --root <fixture> --change <id> --phase <phase> --json`, and `./scripts/validate/run.sh`. New flags and record formats above require implementation before they can be exercised.

| Check | Observable validation and relevant boundaries |
|---|---|
| CHECK-001 | Valid many-to-many coverage; missing error/boundary mapping despite a linked happy-path pass; approved exclusion versus unavailable execution; complete task boxes with missing/partial behavior; every assessment outcome and aggregation; scenario edit/reorder invalidates mappings. Use deterministic records and the semantic walkthrough in CHECK-005. |
| CHECK-002 | Two source changes with the same REQ ID resolve distinctly; active/archive moves retain origin identity; missing source and stale source digest fail readiness; justified no-impact and baseline-only history; synthetic payment test where the new path passes but duplicates fail; reused regression test; approved supersession with replacement check; no test deletion solely to mask failure. |
| CHECK-003 | Before/after and current input hashes; source/test/fixture/config edits; file addition/removal and executable-bit changes; unchanged plan with changed code; excluded output changes and archive moves preserve freshness; declared missing path; traversal, symlink and overlapping output/input rejection; current evidence is not inferred from a URL or runtime label; changed current code does not invalidate historical-only inventory. |
| CHECK-004 | Drafts with no future artifacts; upstream gates/digests; repeated finding reuse and resolved evidence; v2 byte/plan-bound compatibility; unknown v2 and mixed versions rejected; existing legacy exceptions unchanged; archive completion checks retained; live selection of newly moved/modified archive, missing baseline, ambiguous source and explicit selected delivery without Git. |
| CHECK-005 | Record disposable-project conversations or reviewer walkthroughs for relevant success/error/boundary scenarios, false completion, archived regression, no-impact, manual verification, unavailable execution, intentional supersession, validation-only versus authorized fix, task-plan reopening and repeated assessment. Capture actions, findings, evidence and unresolved limits; fixture schemas alone cannot prove these behaviors. |
| CHECK-006 | Run the full validator test suite and package/SDD entry point. Exercise documented commands for new planning, regression selection, snapshots, correction and archive inventory/live selection. Inspect CI baseline handling with valid and unavailable local refs. Confirm four-file authoring, retained profile suites, base composition, exact-version adoption and unchanged historical bytes. Remote CI/merge remains unverified until actually observed. |

Before implementation is marked complete, findings must be resolved or left explicitly blocking/unverified under these checks. Passing only the existing 48 validator tests does not demonstrate the new contract. The new positive and negative cases must run, and behavioral evidence must be recorded separately from deterministic assertions.

## Planning review

- Proposal/Requirements R1 approval is recorded in Proposal and bound above.
- Design R1 and ADR-0014 were approved together by the developer in this conversation on 2026-10-01: “Sim, aprovado.” No material blocker remains.
- Approved Design digest: `f04ed5cc2df7bac8f5a4181f9a9dabc9f99ee11260189ab71df5e96c195faaf4`.
- Approval unlocks Tasks R1. Implementation remains unauthorized until the current Tasks plan is approved and execution is explicitly requested.
