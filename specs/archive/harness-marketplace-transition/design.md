---
sdd_version: 3
change: harness-marketplace-transition
requirements: &id001
- REQ-001
- REQ-002
- REQ-003
- REQ-004
- REQ-005
- REQ-006
adrs:
- docs/decisions/0011-root-portable-plugin-package.md
validation:
- id: CHECK-001
  description: Verify canonical marketplace identity and retained package contracts with positive and negative fixtures.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-005
  - REQ-006
  required: true
  method:
    kind: automated
    procedure: Run the maintained Plugin validator and the marketplace/package regressions on final inputs. Accept
      only versat / Versat Plugins with unchanged plugin name, exact ref/version, policy, legal files and canonical
      root resources; retain wrong/missing/empty name, wrong label, plugin/ref drift and root-resource negative
      cases. Reuse adequate tests and, where missing, add a deterministic disposable-package check that resolves
      canonical resources referenced from each of the five Skill directories after copying the package root, with
      a missing-resource failure case. This proves packaged paths, not native client discovery, registration or
      Skill execution.
  inputs:
    include:
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - validators/plugin
    - tests/validators/test_plugin_marketplace.py
    - tests/fixtures/marketplace-transition
    - project-templates/base/.versat/standards.lock
    - skills
    - standards
    - sdd
    - schemas
    - project-templates
    - LICENSE
    - NOTICE
    - THIRD-PARTY-NOTICES.md
    exclude: []
  outputs:
  - docs/validation/harness-marketplace-transition/execution-02/check-001
  execution: local
- id: CHECK-002
  description: Review the reported two-user scope, accepted main-sync exposure and exact-release precondition.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-006
  required: true
  method:
    kind: review
    procedure: Verify the recorded owner reports (Elvis and Everton only, managed source follows main, later manual
      reinstallation) against their attributed evidence and the current approved Proposal. Separate reported facts
      from observed cache/config data and unknown Source/Path/sync/managed-ID details. Record the approved acceptance
      of possible interruption/manual repair, no preliminary pin/pause requirement, and the stop condition if additional
      users are identified. Recheck the target tag/version before source delivery without creating or modifying
      refs. Pass only for a truthful bounded-scope disposition and exact-version eligibility; do not assert native
      continuity or a workspace audit.
    reason: A recorded owner scope/decision and read-only ref observation establish this source-delivery condition;
      managed behavior remains unknown.
  inputs:
    include:
    - .agents/plugins/marketplace.json
    - VERSION
    - .github/CODEOWNERS
    - .github/workflows/validate.yml
    - docs/user-docs/guides/workspace-setup.md
    - docs/user-docs/guides/marketplace-transition.md
    - docs/validation/harness-marketplace-transition/inputs/inventory.json
    - docs/validation/harness-marketplace-transition/inputs/transition-r2.json
    exclude: []
  outputs:
  - docs/validation/harness-marketplace-transition/execution-02/check-002
  execution: local
- id: CHECK-003
  description: Review truthful deferral of native observations and concrete later per-user reinstallation acceptance.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-006
  required: true
  method:
    kind: review
    procedure: Review the deferred-native register and manual reinstallation guide. All seven former isolated scenarios
      must remain identified as unexecuted/unverified unless genuine later observations exist; no missing environment
      becomes pass or not-applicable. Confirm Elvis and Everton have separate pending post-install records for qualified
      identity, exact version, one effective provider, canonical resources, representative Skill behavior and failure/recovery
      disposition. Confirm no pre-merge VM/account/native rehearsal prerequisite is recreated. This check can pass
      only for the reviewed deferral/acceptance instructions, never for native compatibility or actual reinstallations.
    reason: Approved Requirements R2 separates pre-merge source acceptance from later observed native behavior;
      an explicit documentary review prevents those different outcomes being conflated.
  inputs:
    include:
    - VERSION
    - plugin.json
    - .codex-plugin/plugin.json
    - .agents/plugins/marketplace.json
    - skills
    - standards
    - sdd
    - schemas
    - validators
    - project-templates
    - tests/fixtures/marketplace-transition
    - docs/user-docs/guides/marketplace-transition.md
    - docs/validation/harness-marketplace-transition/inputs/transition-r2.json
    exclude: []
  outputs:
  - docs/validation/harness-marketplace-transition/execution-02/check-003
  execution: local
- id: CHECK-004
  description: Review the bounded manual handoff, recovery records and separate operational authority.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  required: true
  method:
    kind: review
    procedure: Walk through successful and failed manual-reinstallation decisions as a document review, explicitly
      not an executed rehearsal. Require available exact package source before advertising installation, preservation
      of compatible provider/project records, one effective provider, no silent lock migration or downgrade of active
      SDD v3, and stop/report on collision, access failure or unsupported managed operation. Keep workspace intervention,
      deletion, automated installs and legacy cleanup outside current authority. Main tracking and unknown native
      continuity alone do not block source delivery under the two-user decision; extra users or unsupported destructive
      actions require reassessment. Record later user outcomes only after observed.
    reason: Review verifies the handoff rules and authority boundaries; it neither performs nor proves manual or
      managed migration.
  inputs:
    include:
    - docs/user-docs/guides/marketplace-transition.md
    - docs/user-docs/guides/workspace-setup.md
    - docs/validation/harness-marketplace-transition/inputs/inventory.json
    - .github/CODEOWNERS
    - .github/workflows/validate.yml
    - docs/validation/harness-marketplace-transition/inputs/transition-r2.json
    exclude: []
  outputs:
  - docs/validation/harness-marketplace-transition/execution-02/check-004
  execution: local
- id: CHECK-005
  description: Review multilingual active guidance, candidate reconciliation and immutable history.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  required: true
  method:
    kind: review
    procedure: Review the final diff and affected EN/PT/ES links/anchors, candidate notes and current handoff. Retain
      the incorporated 17-file candidate corrections and all historical failures/approvals. Replace obsolete mandatory
      pin/isolated-rehearsal language only in active guidance with the approved two-user/manual-reinstallation scope;
      distinguish both identities, two refs, accepted possible interruption, exact release availability and pending
      native/external cases. Describe any unexercised native command as unverified; do not claim supported behavior
      without real evidence. Preserve legacy command blocks as historical and verify consistent meaning across translations.
    reason: Semantic guidance, translated obligations and preservation of approved history require review. Link
      checks alone cannot establish installation or migration behavior.
  inputs:
    include:
    - README.md
    - README.pt.md
    - README.es.md
    - CHANGELOG.md
    - docs/user-docs
    - docs/releases
    - docs/handoffs/harness-publication-blockers
    - docs/licensing
    - specs/archive
    - docs/validation/harness-publication-blockers
    - .agents/plugins/marketplace.json
    exclude: []
  outputs:
  - docs/validation/harness-marketplace-transition/execution-02/check-005
  execution: local
- id: CHECK-006
  description: Collect genuine local Plugin validation and maintained regression-suite results before documentary
    delivery verification.
  requirements: *id001
  required: true
  method:
    kind: automated
    procedure: After current planning approvals and authorized implementation, run validators/plugin/validate.py
      and both complete maintained unittest discovery suites (tests/validators and tests/execution, pattern test_*.py)
      with the verified Python environment on final inputs. Record each actual exit status, counts, logs and unchanged
      before/after input digests as local evidence. These existing component commands are the suite-evidence portion
      of scripts/validate/run.sh, not a replacement for its final contract guard. Only after genuine CHECK-001 through
      CHECK-006 results are recorded, verify documentary delivery/archive eligibility with the unchanged full entry
      point and selected delivery validator as a separate closure gate. CI then repeats the unchanged required entry
      point on the authorized PR and must succeed before merge. The closure gate and remote CI are separate observed
      outcomes, never inputs needed to fabricate this local check result.
  inputs:
    include:
    - .
    exclude:
    - docs/validation/harness-marketplace-transition
  outputs:
  - docs/validation/harness-marketplace-transition/execution-02/check-006
  execution: local
coverage:
- scenario:
    requirement: REQ-001
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-001
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-003
  - CHECK-005
- scenario:
    requirement: REQ-001
    scenario: 3
  applicability: required
  checks:
  - CHECK-002
  - CHECK-006
- scenario:
    requirement: REQ-002
    scenario: 1
  applicability: required
  checks:
  - CHECK-002
- scenario:
    requirement: REQ-002
    scenario: 2
  applicability: required
  checks:
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-002
    scenario: 3
  applicability: required
  checks:
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-003
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
  - CHECK-005
  - CHECK-006
- scenario:
    requirement: REQ-003
    scenario: 2
  applicability: required
  checks:
  - CHECK-003
- scenario:
    requirement: REQ-003
    scenario: 3
  applicability: required
  checks:
  - CHECK-003
  - CHECK-004
- scenario:
    requirement: REQ-003
    scenario: 4
  applicability: required
  checks:
  - CHECK-003
  - CHECK-006
- scenario:
    requirement: REQ-004
    scenario: 1
  applicability: required
  checks:
  - CHECK-002
  - CHECK-003
  - CHECK-004
- scenario:
    requirement: REQ-004
    scenario: 2
  applicability: required
  checks:
  - CHECK-003
  - CHECK-004
  - CHECK-005
- scenario:
    requirement: REQ-004
    scenario: 3
  applicability: required
  checks:
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-004
    scenario: 4
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-005
    scenario: 1
  applicability: required
  checks:
  - CHECK-005
- scenario:
    requirement: REQ-005
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-006
- scenario:
    requirement: REQ-005
    scenario: 3
  applicability: required
  checks:
  - CHECK-005
  - CHECK-006
- scenario:
    requirement: REQ-006
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
  - CHECK-006
- scenario:
    requirement: REQ-006
    scenario: 2
  applicability: required
  checks:
  - CHECK-004
  - CHECK-005
- scenario:
    requirement: REQ-006
    scenario: 3
  applicability: required
  checks:
  - CHECK-004
  - CHECK-006
regression:
- obligation:
    impact: 2
    scenario: 2
  checks: &id002
  - CHECK-005
  - CHECK-006
  rationale: Retain truthful multilingual guidance and unchanged independent products/consumers.
- obligation:
    impact: 2
    scenario: 3
  checks: *id002
  rationale: Retain truthful multilingual guidance and unchanged independent products/consumers.
- obligation:
    impact: 3
    scenario: 1
  checks:
  - CHECK-001
  - CHECK-006
  rationale: Retain canonical package directories, reproducible resource-path resolution from the copied package
    root and absence of duplicated Standards using genuine deterministic checks; native client provider selection
    remains deferred, not asserted passed.
- obligation:
    impact: 3
    scenario: 2
  checks:
  - CHECK-001
  - CHECK-006
  rationale: Retain canonical package directories, reproducible resource-path resolution from the copied package
    root and absence of duplicated Standards using genuine deterministic checks; native client provider selection
    remains deferred, not asserted passed.
- obligation:
    impact: 3
    scenario: 3
  checks:
  - CHECK-001
  - CHECK-006
  rationale: Retain canonical package directories, reproducible resource-path resolution from the copied package
    root and absence of duplicated Standards using genuine deterministic checks; native client provider selection
    remains deferred, not asserted passed.
- obligation:
    impact: 4
    scenario: 1
  checks: &id003
  - CHECK-002
  - CHECK-004
  - CHECK-005
  - CHECK-006
  rationale: Retain a repository catalog, exact release selection and usable managed-installation handoff without
    claiming real migration.
- obligation:
    impact: 4
    scenario: 2
  checks: *id003
  rationale: Retain a repository catalog, exact release selection and usable managed-installation handoff without
    claiming real migration.
- obligation:
    impact: 4
    scenario: 3
  checks: *id003
  rationale: Retain a repository catalog, exact release selection and usable managed-installation handoff without
    claiming real migration.
review:
  revision: 3
  state: approved
  blockers: []
  upstream:
    proposal: e2cf501301bc4a8ef482631a8ad3d4f60a060a43087ceca9914537622340e773
  approval:
    source: Current conversation reply to the explicit request to approve Design R3 and prepare only revised Tasks
    quote: sim
    revision: 3
    digest: 6d8be8c8d53182f0b6e7a3672f1c441a1764623a48d7be31ec1b17c06b9dc17b
---

# Design

## Current state and authority

Proposal/Requirements R2 is approved under the digest recorded upstream. This turn prepares Design R3 only. Existing local catalog/validator/tests and EN/PT/ES documentation were implemented under the earlier plan; the complete local suite passed 191 tests on its recorded inputs. No code or living-guide implementation is changed by this Design turn. Tasks R2 remains superseded with its actual progress and results preserved.

The owner reports only Elvis and Everton use the Harness, the managed catalog follows main, no disposable native environment exists, and they will reinstall manually later. Approved R2 accepts possible sync exposure, temporary interruption or manual repair for this bounded population. It removes the preliminary workspace pin and isolated native rehearsal as source-delivery prerequisites without claiming that the missing behavior has passed.

Use the [recorded exact provider](../../../docs/validation/harness-marketplace-transition/provider.json) from source `c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa`, declared 0.4.0 and not a release. Its anchors were verified. Installed plugin versions do not replace this source. Resolve applicable Language, Documentation, Git, Security, Licensing/Publication, Contribution, Testing, Library and Python Standards through the index. ADR-0011 remains applicable; no package architecture change or new ADR is needed.

## Retained implementation and package contracts

| Surface | Required result |
|---|---|
| Catalog | `name: versat`, `interface.displayName: Versat Plugins`; one Harness entry. |
| Plugin/package | Keep `versat-ai-harness`, repository URL, AVAILABLE/ON_INSTALL policy, category, root layout, legal text and notices. |
| Versions | Keep VERSION/manifests/template lock and exact package reference aligned. Recheck v0.4.0 before delivery; if released, stop and review the next version rather than retagging. |
| Consumer state | No implicit lockfile, Standards snapshot, in-flight SDD provider or installed cache migration. |
| Validation | Reuse the 12 marketplace regressions and both complete maintained suites; keep required CI and review controls intact. |

The catalog revision followed by the workspace and the package's exact tag are different references. Merging source cannot make an absent v0.4.0 tag installable. Existing `versat-ai-harness@versat-internal` is not an alias for `versat-ai-harness@versat`; managed IDs do not necessarily follow either key.

The 17-file prior documentary candidate and earlier ARCHIVE_SELECTION failure remain preserved. Later authorized implementation reconciles active guidance with R2 instead of mass-renaming history or rewriting approvals. Scope remains the catalog, validator/meaningful regression coverage, current dossier/evidence and active documentation; no workflow, protection, licensing, access-policy or distribution architecture change is introduced.

## Source acceptance for two users

The source review consumes the owner's attributed scope and decision, not an invented fleet audit. Keep the bounded inventory and add a sanitized `docs/validation/harness-marketplace-transition/inputs/transition-r2.json` during later implementation. It records:

- the actual owner instruction and approved revision/digest;
- the reported two-user population and main tracking, distinguishing observations from unknown sync/managed-ID fields;
- accepted possibility of interruption/manual repair and removal of pin/isolated-runtime prerequisites for source delivery;
- pending per-user manual checks and unexecuted native/external cases;
- the stop condition if another affected user is identified.

No credential, private member detail or raw local path belongs in this public-safe record. Restricted observations remain in private evidence. Unknown sync timing/managed identity alone is no longer a merge blocker for the accepted two-user scope. Extra affected users, wrong package reference, failed required source tests or claims of unsupported native success remain blockers. Neither this decision nor the record operates on the workspace.

## Later manual reinstallation and observed acceptance

Manual reinstallation happens after source delivery and availability of a usable exact package, when each user proceeds. A source merge is not release, installation or a completed migration. Do not invent a tested command route from documentation alone. Later instructions must distinguish verified client operations from unexercised steps and stop if the real client cannot perform the intended operation without an unapproved workspace/admin action.

Each user has one pending outcome record; one user's result does not prove the other's:

| Verification after actual reinstallation | Acceptance or recorded stop |
|---|---|
| Qualified identity and version | Expected `versat-ai-harness@versat` in local scope and intended exact version; managed identity recorded as actually returned. |
| Effective provider | Exactly the intended provider selected in that session, with canonical root resources matching its version. |
| Representative Skill | A bounded action on synthetic project data resolves the actual provider and required resources; files alone do not prove behavior. |
| Failure/recovery | Record error and whether a compatible retained provider/project pair can be selected through supported controls; unresolved recovery stays pending. |

Do not copy caches between identities, edit installation databases, select latest, silently change project locks or downgrade active SDD v3 work. Preserve available exact source/package/project records before later changes. Current main pointing to an unavailable release tag is not a verified fallback. A user may need administrator help; this Design does not authorize an agent to uninstall, delete/reimport, create a second managed plugin or change workspace settings. Legacy cleanup stays optional and separately scoped.

### Deferred native register

Retain the former seven scenarios: fresh discovery/resources; retained legacy installation; same-Git-URL refresh/registration; target-name collision; two installed providers/one effective provider; unavailable exact reference; and recovery. Their actual outcome remains unverified until observed. A later real reinstall can contribute evidence to the cases it actually exercises; do not invent missing failure cases or require all seven to be simulated merely to complete the source PR. The source-delivery check reviews this honest deferral and the manual acceptance instructions; it does not certify runtime compatibility.

External fork/CI, private-report receipt/confidentiality and native external installation/update/recovery remain independent pending observations. Internal manual results do not automatically complete them. If wider use or an incident makes additional native rehearsal necessary, reassess its scope and authority rather than claiming a historical pass.

## Required source checks and evidence semantics

All six checks in the frontmatter are required for source acceptance, with 20 local scenario mappings and eight retained regression obligations. No acceptance position is silently excluded. CHECK-002/003/004 are explicitly revised review methods, not the old runtime checks with changed result labels.

| Check | What a future pass proves | What it does not prove |
|---|---|---|
| CHECK-001 | Actual deterministic metadata, version and canonical-resource checks, including meaningful negative cases. | Native marketplace discovery or migration. |
| CHECK-002 | Attributed two-user/main-tracking disposition and refreshed exact-version eligibility. | Full workspace audit or preserved managed IDs. |
| CHECK-003 | Correct pending-native register and concrete later per-user acceptance/stop rules. | Any native scenario or reinstallation succeeded. |
| CHECK-004 | Reviewed manual handoff and recovery/authority decisions, including adverse outcomes. | Executed migration, recovery or administrator action. |
| CHECK-005 | Truthful aligned active EN/PT/ES guidance and preserved historical evidence. | Unexercised commands work in a real client. |
| CHECK-006 | Actual local Plugin validation and both complete maintained regression suites on final inputs. | Documentary closure, remote CI, merge or release. |

CHECK-001 must retain the root-package regression, not replace it with a prose promise: inspect adequate maintained tests and add only missing meaningful coverage. A disposable package copy may exercise paths from each of the five Skill directories into matching Standards/SDD/templates/schemas/validators, with deliberate missing-resource failure. This is an offline package-contract test, not a security-isolated native environment or a supervised Skill invocation. Native effective-provider selection remains in the deferred register.

The existing 191-test pass remains attributable to its original inputs. New review methods and later guide/input changes require actual new observations; do not copy CHECK-002/003/004's old unverified records into new passes. Use new `execution-02` output locations and keep `execution-01` unchanged. A check's exact declared input hashes, method, local context and actual report must agree. Source scope must not hide changed files merely to avoid rerunning affected tests.

## Evidence, closure and mandatory CI order

1. After current Tasks approval and explicit applicable implementation authority, reconcile living guides and sanctioned source/check work. Record the sanitized decision/pending-native input and execute the six required source checks on final inputs. Local CHECK-006 runs the Plugin validator and both complete unittest discovery suites independently of closure.
2. Record genuine results and all local/regression assessments against the current plan. Preserve FIND-001/FIND-002 and their historical observations. Their old pre-merge-blocking disposition may be replaced only with the approved R2 scope decision and completed new source-review evidence, never described as a successful native rehearsal. Keep the underlying operational unknowns in the deferred register. Preserve old ledger snapshots when Tasks is revised; do not erase history to turn validation green.
3. Once actual revised work/source acceptance is complete, prepare the unique dossier for documentary archive and run the unchanged full entry point with the trusted baseline and `--require-archive`, plus selected live delivery validation. These gates consume check evidence; they are not a prerequisite for creating CHECK-006's own result. Missing source evidence or a failed gate still blocks delivery.
4. Only an authorized remote operation submits the candidate. Actual `structural-validation` CI and applicable nonauthor CODEOWNER approval must pass on the current PR revision before merge. Local passes, the owner scope decision and anticipated reinstallations waive neither requirement.
5. Tag/release and actual reinstallation remain separate outcomes requiring their applicable authority and available exact package. Record later results without forcing a post-merge action into a pre-merge task completion gate.

Illustrative future validation commands, not executed in this Design turn:

```sh
PYTHONDONTWRITEBYTECODE=1 /absolute/path/to/verified-venv/bin/python validators/plugin/validate.py
PYTHONDONTWRITEBYTECODE=1 /absolute/path/to/verified-venv/bin/python -m unittest discover -s tests/validators -p 'test_*.py'
PYTHONDONTWRITEBYTECODE=1 /absolute/path/to/verified-venv/bin/python -m unittest discover -s tests/execution -p 'test_*.py'
# After genuine acceptance evidence and archive preparation:
PYTHONDONTWRITEBYTECODE=1 PYTHON=/absolute/path/to/verified-venv/bin/python bash scripts/validate/run.sh --baseline c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa --require-archive
PYTHONDONTWRITEBYTECODE=1 /absolute/path/to/verified-venv/bin/python validators/sdd/validate.py --root . --change harness-marketplace-transition --phase delivery --require-archive --json
```

A later rebase requires reviewing/recording its trusted baseline. No validator change, archive bypass, workflow dispatch or synthetic CI result is proposed.

## Alternatives and limitations

A pinned catalog with prior isolated rehearsal remains available if scope/risk expands, but is no longer a mandatory prerequisite for the accepted two-user delivery. A visible-label-only change does not achieve the approved identifier. Automatic aliases, cache moves, generic pluginId workarounds and delete/reimport are not substitutes for unknown native behavior. If the exact version has already been released or another affected user appears, stop the affected delivery and review that changed fact.

## Planning review

The owner approved Proposal/Requirements R2 by replying “Sim. Avance.” to the explicit Gate 1 request. Its unchanged digest is `e2cf501301bc4a8ef482631a8ad3d4f60a060a43087ceca9914537622340e773`. Design R3 is now awaiting Gate 2 approval; no approval is inferred from preparation authority.

Design R2 was approved under digest `5ad1056a9bf2689839292e03767f9a480ab8c30efcac4b4c60340cf1e37db9cb` with “Aprovo o Design R2 de harness-marketplace-transition. Prepare somente as Tasks revisadas, sem implementar, alterar o workspace, migrar consumidores ou criar tag ou release.” R1/R2 approvals and snapshots remain historical. R3 replaces the scoped prerequisite/check semantics described above while retaining package boundaries and the corrected local-evidence/closure/CI order. Tasks R2 remains superseded; its genuine three-completed/three-blocked progress and old evidence are unchanged until a separately reviewed Tasks revision.

The owner subsequently approved the presented Design R3 with “sim”, responding to the explicit Gate 2 question authorizing only revised Tasks preparation. The unchanged approved digest is `6d8be8c8d53182f0b6e7a3672f1c441a1764623a48d7be31ec1b17c06b9dc17b`. This approval does not execute Tasks or authorize remote/workspace/tag/release operations.
