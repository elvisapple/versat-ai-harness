---
sdd_version: 3
change: portfolio-licensing-policy
requirements:
- REQ-001
- REQ-002
- REQ-003
- REQ-004
- REQ-005
- REQ-006
adrs:
- docs/decisions/0004-versioned-snapshots-and-lockfiles.md
- docs/decisions/0011-root-portable-plugin-package.md
- docs/decisions/0013-consolidated-sdd-workflow.md
- docs/decisions/0014-sdd-acceptance-and-regression.md
validation:
- id: CHECK-001
  description: Review policy dispositions, portfolio separation and accountability
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  required: true
  method:
    kind: review
    procedure: 'Read the new licensing/publication Standard, index entry and review record. Exercise synthetic public-Apache
      and private-proprietary component cases, then missing grant, incompatible dependency, secret in history, missing
      reviewer and missing control cases. Compare each mapped acceptance position and baseline obligation: per-product
      evidence and explicit publish/defer/retain-private disposition, with named follow-up; full export surface
      must be required and no license application or clearance inferred. Verify actual review record references
      without copying confidential contracts. Expected: all stated governance rules and failure boundaries hold;
      unresolved actual evidence remains unverified and cannot certify product publication.'
    reason: Rights, authority and semantic policy decisions require attributable human review; package validators
      cannot establish them.
  inputs:
    include: &id001
    - standards
    - docs/licensing
    - docs/governance
    - docs/user-docs
    - docs/handoffs
    - README.md
    - README.pt.md
    - README.es.md
    - .github/CODEOWNERS
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
  outputs:
  - docs/validation/portfolio-licensing-policy
  execution: local
- id: CHECK-002
  description: Review the concrete versioned terms and actual approval evidence
  requirements:
  - REQ-003
  - REQ-004
  - REQ-006
  required: true
  method:
    kind: review
    procedure: 'Inspect the exact non-operative terms candidate, version/hash, component scope, notices and rights-review
      references. Compare installation/use/modification/redistribution permissions and conditions with explicit
      owner decisions; check tool/project license separation and declared Versat E.A.S. identity versus verified
      rights. Retrieve actual approval of this text from the identified authorized reviewer and bind it to its version/hash;
      record limits or required specialist input. Technical CODEOWNERS, SDD approval, a policy pass or an agent-authored
      approval record are insufficient. Expected: concrete wording and genuine approval are evidenced; absent decisions,
      terms, grants or review yield unverified/fail, never approved by template. Approval of the candidate does
      not apply a license or activate terms.'
    reason: Legal wording and approval cannot be certified by syntactic tests. This check requires observed human
      evidence, without assuming professional qualification.
  inputs:
    include: *id001
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
  outputs:
  - docs/validation/portfolio-licensing-policy
  execution: local
- id: CHECK-003
  description: Verify canonical policy resolution and package boundaries
  requirements:
  - REQ-005
  required: true
  method:
    kind: review
    procedure: 'Parse standards/index.yaml and confirm core/licensing-publication.md appears once in core.always
      and resolves to a real file. Compare the canonical root directories, Skills references, manifests, VERSION,
      marketplace exact release ref and consumer lock template with baseline 597b81c71a0fc0908ff5264fe9987bb5c0d8feec.
      Inspect the diff for copied Standards inside Skills, nested plugin paths or accidental release/consumer changes.
      Expected: all profiles inherit the new common policy by index composition, source paths remain version-matched
      and no release ref or consumer installation changes. This explicit index review supplements the existing package
      validator; no executable general Standards resolver is claimed.'
    reason: The maintained package validator covers root and manifest invariants but does not implement the full
      index-resolution or no-copy semantic review.
  inputs:
    include:
    - standards
    - skills
    - agents
    - project-templates
    - schemas
    - sdd
    - validators/plugin
    - plugin.json
    - VERSION
    - .codex-plugin
    - .agents/plugins
    - docs/architecture
    - docs/decisions
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
  outputs:
  - docs/validation/portfolio-licensing-policy
  execution: local
- id: CHECK-004
  description: Walk through operator guidance, confidentiality and authorization boundaries
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-006
  required: true
  method:
    kind: review
    procedure: 'Follow the proposed licensing guide from each README locale for one component review and one blocked
      decision. Compare EN/PT/ES meaning, local links/anchors and policy versus examples. Read every intended public
      candidate independently of strategy access and inspect text/examples/URLs for private rationale, credentials
      or sensitive evidence. Compare the complete tracked/untracked implementation diff and authorized action record:
      H01/H02 planning and later explicitly authorized candidate work must not apply licenses, change effective
      terms, grant access, publish, activate channels or complete P01/P03/H03. Expected: usable versioned references,
      named recovery, truthful scope and separate adoption/operation. Missing access or actual review is reported,
      not hidden by translation or templates.'
    reason: Human reading is needed for translation equivalence, confidentiality and truthful authorization claims;
      mechanical link checks may supplement it.
  inputs:
    include: *id001
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
  outputs:
  - docs/validation/portfolio-licensing-policy
  execution: local
- id: CHECK-005
  description: Run the maintained package and regression suites
  requirements:
  - REQ-005
  - REQ-006
  required: true
  method:
    kind: automated
    procedure: From the selected Harness checkout with Python 3.11+ and requirements-validation.txt installed, run
      PYTHONDONTWRITEBYTECODE=1 PYTHON=<selected-interpreter> ./scripts/validate/run.sh. Preserve actual command/stdout/exit
      code. Expected exit 0 with Plugin validation, SDD inventory, full validator and execution suites; do not narrow
      to targeted tests, alter legacy exceptions or treat existing warnings as current approval. This local run
      does not assert remote CI, legal acceptance or release.
  inputs:
    include:
    - AGENTS.md
    - VERSION
    - plugin.json
    - .codex-plugin
    - .agents/plugins
    - standards
    - skills
    - agents
    - project-templates
    - schemas
    - sdd
    - validators
    - scripts
    - tests
    - .github
    - requirements-validation.txt
    - docs
    - README.md
    - README.pt.md
    - README.es.md
    - specs/archive
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
    - specs/archive/contribution-security-guidance/tasks.md
  outputs:
  - docs/validation/portfolio-licensing-policy
  execution: local
- id: CHECK-006
  description: Verify planning lineage and truthful evidence bookkeeping without a closure cycle
  requirements:
  - REQ-006
  required: true
  method:
    kind: review
    procedure: 'Use the canonical digest helpers to verify the three stage revisions/approvals once they exist,
      qualified historical source digests, every local scenario and retained obligation mapping, unique active dossier
      and referenced evidence paths. Run --root . --change portfolio-licensing-policy --phase planning --json; after
      actual Tasks approval and implementation authorization also run --phase implementation --json. Compare files
      to authorization and keep planned, observed, unavailable and approved states distinct. Expected structural
      pass at the applicable stage and unchanged historical dossiers. This check never requires its own passing
      result, completed Tasks, delivery or archival; final closure gates execute separately after acceptance completion.
      R2: during this check, verify canonical Proposal/Design/Tasks digests and real approvals for BOTH portfolio-licensing-policy
      and contribution-security-guidance; run selected planning and implementation for both after their actual gates
      permit execution. A peer Tasks plan/approval change blocks readiness until its own gate and affected checks
      are current; exclusion of its raw evidence-bearing tasks.md never waives that independent contract. Diagnose
      snapshot behavior on disposable copies: sibling evidence-only edits must not change CHECK-005/006 inputs;
      real source and sibling Proposal/Requirements/Design edits must still invalidate applicable snapshots; a substantive
      sibling task edit must invalidate its canonical Tasks approval. Do not substitute this diagnostic for the
      complete required suite or final delivery/archive guards. Rechecking final records is a separate closure audit
      after this check has actually finished; no part of CHECK-006 requires its own result or final delivery to
      exist.'
    reason: Recorded approvals and semantic evidence need review in addition to the deterministic metadata checker;
      this procedure must not depend on final delivery.
  inputs:
    include:
    - sdd
    - validators/sdd
    - specs/archive
    - docs/governance
    - docs/licensing
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
    - specs/archive/contribution-security-guidance/tasks.md
  outputs:
  - docs/validation/portfolio-licensing-policy
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
- scenario:
    requirement: REQ-001
    scenario: 3
  applicability: required
  checks:
  - CHECK-001
  - CHECK-004
- scenario:
    requirement: REQ-002
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-002
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-002
    scenario: 3
  applicability: required
  checks:
  - CHECK-001
- scenario:
    requirement: REQ-003
    scenario: 1
  applicability: required
  checks:
  - CHECK-002
- scenario:
    requirement: REQ-003
    scenario: 2
  applicability: required
  checks:
  - CHECK-002
- scenario:
    requirement: REQ-003
    scenario: 3
  applicability: required
  checks:
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-004
    scenario: 1
  applicability: required
  checks:
  - CHECK-001
  - CHECK-002
- scenario:
    requirement: REQ-004
    scenario: 2
  applicability: required
  checks:
  - CHECK-001
  - CHECK-004
- scenario:
    requirement: REQ-004
    scenario: 3
  applicability: required
  checks:
  - CHECK-001
  - CHECK-002
- scenario:
    requirement: REQ-005
    scenario: 1
  applicability: required
  checks:
  - CHECK-003
- scenario:
    requirement: REQ-005
    scenario: 2
  applicability: required
  checks:
  - CHECK-003
  - CHECK-005
- scenario:
    requirement: REQ-005
    scenario: 3
  applicability: required
  checks:
  - CHECK-003
  - CHECK-005
- scenario:
    requirement: REQ-006
    scenario: 1
  applicability: required
  checks:
  - CHECK-004
  - CHECK-006
- scenario:
    requirement: REQ-006
    scenario: 2
  applicability: required
  checks:
  - CHECK-002
  - CHECK-004
- scenario:
    requirement: REQ-006
    scenario: 3
  applicability: required
  checks:
  - CHECK-004
  - CHECK-005
  - CHECK-006
regression:
- obligation:
    impact: 1
    scenario: 0
  checks:
  - CHECK-001
  - CHECK-002
  - CHECK-004
  rationale: Add the absent portfolio policy and concrete-terms approval path without treating strategic selection
    as operative licensing. Compare the specific historical acceptance position or captured baseline with current
    observable behavior; do not reuse historical results as fresh evidence.
- obligation:
    impact: 2
    scenario: 0
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Preserve least privilege, secret handling, provenance and explicit high-impact authorization while
    specifying evidence for publication decisions. Compare the specific historical acceptance position or captured
    baseline with current observable behavior; do not reuse historical results as fresh evidence.
- obligation:
    impact: 3
    scenario: 1
  checks:
  - CHECK-003
  - CHECK-005
  rationale: New policy must retain canonical root resources and avoid copied Standards. Compare the specific historical
    acceptance position or captured baseline with current observable behavior; do not reuse historical results as
    fresh evidence.
- obligation:
    impact: 3
    scenario: 2
  checks:
  - CHECK-003
  - CHECK-005
  rationale: New policy must retain canonical root resources and avoid copied Standards. Compare the specific historical
    acceptance position or captured baseline with current observable behavior; do not reuse historical results as
    fresh evidence.
- obligation:
    impact: 3
    scenario: 3
  checks:
  - CHECK-003
  - CHECK-005
  rationale: New policy must retain canonical root resources and avoid copied Standards. Compare the specific historical
    acceptance position or captured baseline with current observable behavior; do not reuse historical results as
    fresh evidence.
- obligation:
    impact: 4
    scenario: 2
  checks:
  - CHECK-003
  - CHECK-005
  rationale: Retain the exact semantic release selection contract; this proposal neither releases nor enables public
    distribution. Compare the specific historical acceptance position or captured baseline with current observable
    behavior; do not reuse historical results as fresh evidence.
review:
  revision: 2
  state: awaiting-approval
  blockers: []
  upstream:
    proposal: 5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7
  approval: null
---

# Design — H01

## Current state and approved scope

Change `portfolio-licensing-policy`, [Harness #34](https://github.com/versat-labs/versat-ai-harness/issues/34). Proposal/Requirements R1 is approved by the user's 2026-11-10 reply, “Aprovado. Avance ao design.” This document is Design R1 for Gate 2; no implementation is authorized.

The selected provider is Harness source `597b81c71a0fc0908ff5264fe9987bb5c0d8feec`, VERSION 0.3.0, with its source SDD v3 resources. All seven `core.always` Standards in `standards/index.yaml` remain applicable. The root package, exact release selection and separation of Standards, Skills, SDD and validators are unchanged. Existing package validation does not implement a licensing audit or legal approval.

The approved strategy already chooses license models. This design organizes evidence, canonical policy and a concrete terms review; it does not select a different license model or decide substantive contractual permissions on the owner's behalf.

## Proposed design

### Files and responsibilities

These are intended implementation targets, not files created during Design.

| Target | Responsibility and effect |
|---|---|
| `standards/core/licensing-publication.md` | Canonical portfolio policy: rights/provenance, dependencies/notices, publication-surface review, accountable decision roles and evidence/disposition rules. |
| `standards/index.yaml` | Add `core/licensing-publication.md` once to `core.always`, so every applicable profile receives the common governance rule through the existing composition contract. No per-Skill copy. |
| `docs/licensing/harness-plugin-terms.md` | Versioned proprietary terms candidate common to Harness/plugin, explicitly non-operative until separately adopted. Concrete permissions are based on actual owner decisions and reviewed wording. It is not a root LICENSE or an implicit grant. |
| `docs/licensing/harness-plugin-notices.md` | Component-specific third-party scope and notices for the reviewed terms candidate. Separate original Versat material from dependencies, copied material, templates and assets. Do not imply a complete inventory before inspection. |
| `docs/governance/licensing-review.md` | Maintained, non-sensitive review ledger: candidate version/hash, evidence references, actual reviewer/authority, disposition, unresolved items and per-product adoption references. Do not copy contracts or personal data into it. |
| `docs/user-docs/guides/licensing.md`, `.pt.md`, `.es.md` | Concise operator/contributor guide: prerequisites, one component review, observable disposition and recovery for missing evidence. Link policy and terms without duplicating them. |
| `README.md`, `README.pt.md`, `README.es.md` | Add localized navigation only once those targets exist. Existing setup, access, version and contribution links remain. |

The common Standard describes public Apache and proprietary-private routes generically. The ledger records the five actual product decisions and separate adoption obligations. Harness-specific terms are not embedded into every consumer Standard or imposed on a destination project.

The terms candidate and notices are English technical/legal review artifacts. The user-facing explanation is EN/PT/ES and must not imply that an explanatory translation is an independently approved legal grant. If additional operative translations are requested, their exact scope and review must be included before delivery; no translation becomes effective through this Design.

### Review data and decision flow

A component record contains a stable component identifier, repository and reviewed revision, boundaries, declared rights holder, third-party source/license/version, grant or contract references, applicable notices, review scope, reviewers, disposition, reasons and outstanding follow-up. Evidence locations must be accessible to the actual authorized reviewer; an inaccessible reference is unverified. Store only minimal non-sensitive references in the root package.

The disposition algorithm is documentary and human-reviewed:

1. Identify the exact component/version and intended distribution surface. Record any incomplete inventory explicitly.
2. Check ownership/grants, dependency combinations, copied code/templates/assets and notices. An automated dependency listing can support this step but cannot establish all legal rights.
3. For intended public export, require review of the actual tree and relevant history, tags, releases, LFS, fixtures, CI and attachments. H01 defines this prerequisite; it does not execute H03/P01's full export clearance.
4. Match the reviewers and authority to the proposed decision. Missing rights, incompatible dependencies, sensitive material, missing approval or unknown controls yield `defer` or `retain-private`, with an owner and concrete follow-up.
5. A `publish` disposition records a reviewed recommendation/clearance for a specific surface; it is not execution authority. Actual publication still requires its executor, authorization and evidence. All unreviewed product rows stay explicitly pending.

Synthetic examples cover an adequately reviewed Apache component, a retained proprietary component, an absent grant, incompatible dependency, secret found only in history, missing reviewer and unavailable control. Clearly label examples; none certifies actual product rights or a real public surface.

### Concrete terms review

Prepare the actual candidate only during later authorized implementation. Capture owner decisions for installation, use, modification and redistribution, audience and component scope, restrictions/conditions, treatment of third-party material and applicability to the plugin. Capture any further legal-entity or jurisdiction information needed by the chosen wording. This Design chooses neither those legal details nor a CLA/DCO/IP transfer.

Record **Versat E.A.S.** as the user-declared holder, subject to verification. Elvis Zoz (`@elviszoz`) is the executor and accountable licensing/security contact. Technical reviewers remain Elvis and Everton Spohr (`@evertonspohrversat`) under CODEOWNERS. A person acting in several roles must identify the capacity of each actual decision; technical review or Gate 2 approval does not silently become legal acceptance. If authority, rights or specialized review is unavailable, keep the corresponding terms decision pending.

Use a document revision plus exact content hash to bind a real approval source and quote/reference to the text. `draft`, `review-requested`, `approved-candidate` and `superseded` are review states, not license activation states. Do not prepopulate an effective date, signature or approval. Any substantive edit invalidates the old text approval until reviewed again. A non-operative but substantively approved candidate can satisfy terms preparation; it does not license the source checkout or permit distribution.

## Boundaries and handoff contracts

| Consumer | H01 supplies | Remains with that consumer |
|---|---|---|
| H02 / #35 | Common policy reference; exact terms/notices revision and hash; real approval status; intended-audience access limits. | Provenance/contribution guidance, confidential reporting route and EN/PT/ES usability. Missing H01 approval blocks H02's approved-terms assertion. |
| P01 — Platform | Common policy and evidence format; selected Apache-2.0 intent. | `versat-labs/versat-platform-2` inventory, rights, license/notices, export review and separately authorized publication. |
| P01 — Workspace | Same common policy; separate Apache-2.0 intent. | `versat-labs/collaborative-ai-workspace` inventory, rights, license/notices and publication. Platform completion does not complete it. |
| P03 — Discover and CRM | Common proprietary route, review format and policy. | Their own terms, private access, rights evidence and integration on P02, separately per repository. Harness terms do not automatically apply to them. |
| H03 | Approved Harness/plugin terms candidate, notices and policy requirements. | Actual distribution/package surface, accessible resources, install/update/use evidence and publication authorization. |
| P02 | Relevant rights/provenance constraints for integration. | Runtime interfaces, installation, permissions, isolation and compatibility. |

No new product change, SDK repository, installer, policy engine, generated distribution tree or Standards resolver is introduced. The inherited root-package contract means all tracked material could travel with a future distribution; H03 must review the actual complete surface and cannot rely on H01 to certify export.

## Data, security and permissions

Contracts, employment/provider records, personal data, credentials and sensitive legal analysis remain in approved restricted storage outside the package. The ledger contains minimal reviewer identities already authorized for this work and non-sensitive locators. If even a locator is confidential, keep it out of public candidates and record its existence/verification in the restricted review process. Do not invent a storage endpoint.

Public candidates must be independently readable without private strategy links or commercial rationale. No changes to permissions, repository visibility, security configuration or live terms are part of this stage. Later implementation authorization must be scoped explicitly; source edits never imply those operational actions.

## Operations, dependencies and observability

There is no runtime deployment, database migration, API, telemetry pipeline or new CI job. Observability consists of attributable review records, exact revisions, check outcomes, missing evidence and separately observed executor adoption.

H01 policy and H02 guide design can progress together. H01's actual terms approval precedes H02's final approved-terms check. Neither H03 distribution nor all product bootstraps are prerequisites to writing the common policy. Missing terms decisions/rights evidence may block H01's later delivery but do not prevent reviewing this design's process for obtaining them.

Both changes currently share a planning checkout. Keep their dossier IDs, checks, evidence and approvals separate. For implementation, order shared-index/README edits explicitly and run affected checks on the final combined tree. If concurrent or upstream changes alter a check's declared inputs, rerun it; do not transplant an earlier input hash. Inspect the current remote/base and source drift before implementation; no automatic provider upgrade.

## Migration, rollout and rollback

During future authorized implementation, add policy/candidate documents and their navigation in the private Harness. Record the source-only state; do not change VERSION, marketplace references, consumer locks, root LICENSE or active licensing metadata. Integrating a policy is a governed PR action and does not itself publish a release or update consumers.

Public distribution, legal activation and per-product adoption remain separate operations. If a candidate fails review, revise or supersede it and retain truthful history. If a later authorized code/documentation rollout needs rollback, restore the previously reviewed navigation/policy through a reviewed change, retain decision evidence and notify dependent executor work records. Do not describe a code revert as a legal revocation; any separately executed legal action requires its own authorized review and lies outside this rollback scope.

## Alternatives and architectural decision

- Put policy and terms only in strategy: rejected because executors/Skills need canonical policy within the version-matched Harness package.
- Use a root LICENSE immediately: rejected because actual wording/rights and operational license application are not authorized.
- Duplicate policy in Skills or create a new licensing service: rejected because existing canonical Standards and human review suffice for this bounded scope.
- Block all products on H03: rejected; product publication and integration have independent acceptance and authority.

No new ADR is needed: adding a Standard and review documents follows ADR-0011's current responsibilities and ADR-0004's exact adoption contract. This design does not alter the package boundary, lifecycle, resolver architecture or enforcement mechanism. If H03 later needs a different package boundary, it must make and review that architectural decision in its own scope. Existing ADR references in metadata are the governing decisions, not new approvals.

## Validation plan and closure order

The six checks above cover all 18 local scenarios and six preserved/extended regression obligations, with no exclusions. CHECK-001/002/004 review semantic rights, approval and usage; CHECK-003 explicitly reviews index/canonical boundaries; CHECK-005 retains the complete existing package suites; CHECK-006 checks lineage without depending on delivery.

Input paths for future files intentionally represent absent-until-implemented resources. No planned method is executed or claimed passed merely by defining it. Before each later check, prepare stable source inputs, capture its canonical input digest, execute the method, record observed outcomes, then capture the after digest. Changes during a check require a fresh run. Outputs under `docs/validation/portfolio-licensing-policy/` are excluded from broad source roots; excluded output files are evidence, not product policy inputs. Actual third-party/source metadata belongs in the reviewed ledger, not mutable test output. Record remote environment/version and revalidate after known external changes.

At future closure, finish actual task work, required evidence, individual assessments and resolved findings first. Only then record accurate completion and run selected `--phase delivery`; if eligible, move the unique dossier to archive and run selected `--phase delivery --require-archive`. These final guards are lifecycle steps, not prerequisites of CHECK-006 or a self-referential acceptance task. Failure reopens the affected work. PR/merge and final required CI remain separately observed and authorized; the existing workflow stays in place.

No blocker prevents Gate 2 review. Concrete terms decisions, rights verification, actual reviewer acceptance and future operational permission remain explicit delivery inputs; the design does not claim them complete.

## Design R2 — acyclic evidence inputs

### Exact problem and bounded decision

This revision prepares joint documentary closure in the existing private Harness PR #37. It changes only the input contract and lineage verification of CHECK-005 and CHECK-006. Proposal/Requirements, all six check IDs per change, required flags, 24 H01 and 35 H02 scenario/regression obligations, their mappings, terms, live reporting rules and product boundaries are unchanged. Harness 0.3.0 validators, schemas, CI and required suites remain unchanged; no new runtime or ADR is needed.

At reviewed commit `1198c2cd2d39f69a12e4f5abae727725b577593a`, `input_digest` excludes its own dossier but traverses other files in `specs/archive`. A sibling `tasks.md` combines approved task planning with mutable results, assessments, findings and closure bookkeeping. Once both dossiers are archived, updating either result changes the other's CHECK-005/006 inputs, preventing both records from remaining fresh together. The earlier green draft CI tested H02 archived and H01 active; it is valid for that state, not proof of joint archival readiness.

For this change, add exactly `specs/archive/contribution-security-guidance/tasks.md` to the existing exclusions of CHECK-005 and CHECK-006. Keep `specs/archive` included. Do not exclude the sibling directory, its Proposal/Requirements/Design, any other dossier's Tasks, product sources, Standards, documentation, approved terms, validators, tests, scripts or workflow configuration. The sibling active Tasks path is not beneath the existing included archive root; no wildcard or global exclusion is introduced. The current dossier remains excluded by the existing canonical algorithm.

### Separate evidence bytes from approval enforcement

The excluded file is not discarded or exempted from validation. Its schema, task coverage, substantive Tasks digest, real review/upstream approvals, results, assessments, findings and closure continue to be checked by the unchanged SDD validator for its own change. CHECK-006 explicitly checks both changes' current stage bindings before recording its observed result. A separate closure audit rechecks the bindings after final records are written; that audit is not a prerequisite of CHECK-006 or its own result. Final selected delivery/archive guards must pass for each change; event-baseline CI must pass for the combined result. A changed task description, unapproved Design, missing result, open finding or incomplete task must still prevent readiness. A snapshot exclusion does not grant approval or turn an unavailable check into a pass.

The H01-to-H02 source dependency stays intact: concrete terms/notices, the exact approval record and governance/guidance inputs remain hashed. This does not exclude any acceptance or retained regression scenario. Historical source bindings remain unchanged. An unrelated archived dossier's `tasks.md` remains hashed as before.

### Planned observable checks and convergence

Reuse CHECK-005's full maintained command and CHECK-006's review; add no second suite or validator implementation. In disposable copies with both dossiers in archive storage:

1. Reproduce R1: an evidence-only edit in either sibling Tasks changes the other's CHECK-005/006 snapshot.
2. Under R2, perform the same edit: those sibling snapshots remain equal. The edited change's own evidence must still satisfy its current validator; a failing/missing result is never waived.
3. Change a real term/source file or sibling Design/Requirements: affected snapshots must change. Edit a sibling task description: its canonical Tasks digest must change and the unchanged approval must no longer match. An unrelated archived Tasks edit must still affect CHECK-005/006.
4. Restore every probe byte. With both dossiers in their final locations and source plans frozen, execute actual affected checks with before/after snapshots, record each result once, and verify both current snapshots still equal their observed values. Record order must not require relabeling a prior run or repeatedly rewriting the peer's result hash.
5. Run selected `--phase delivery --require-archive` for both IDs and the complete maintained validation with the trusted PR baseline and `--require-archive`. Only then transition the existing draft PR toward review and observe its final CI. Approval of this Design alone does not authorize that transition.

The raw path of a sibling plan still matters: moving a dossier can invalidate the other's checks once. Repeat affected verification on the final layout rather than promising relocation-invariant hashes. Final evidence-only updates then converge because neither check hashes the other's result container.

### Revision, rollout and rollback

This is Design R2 awaiting Gate 2 approval, not completed implementation. Preserve R1 designs, Tasks approvals and observed evidence as historical records. In this local review branch only, reopen H02 from archive to active storage, set closure active and mark both downstream Tasks reviews superseded; preserve their substantive plans and do not draft Tasks R2 before Design approval. Historical checks and authorized PVR/email observations remain evidence of their original scope, not new R2 check results. No repeated live report or notification is required solely by this planning correction; known external drift would reopen affected verification under its actual authority.

After Gate 2, prepare Tasks R2 with the approved upstream digests and existing stable task IDs; obtain the applicable Tasks approval/implementation authority before executing. During validation, preserve previous attempts outside the input scope, start a truthful pending ledger for the new attempt, and record results only after observation. Pre-move delivery, unique archive moves and final guards remain separate lifecycle steps. The `.github` seven-file candidate is unaffected.

Rollback before approval discards this local planning candidate and retains the existing remote PR heads. Later rejection/failure restores an honestly pending state; it never relabels R1 evidence as current R2 validation. No merge, effective licensing, public publication, new channel action or broader repository rollout is part of this revision.

### Alternatives

- Keep alternating evidence updates: rejected; raw sibling result bytes retain the cycle.
- Exclude all of `specs/archive` or the whole sibling dossier: rejected; unnecessarily removes real plan/history inputs.
- Merge one change first to evade the simultaneous check: rejected; merge is unauthorized and does not correct the declared dependency.
- Change the generic snapshot algorithm to normalize all dossiers: deferred; wider runtime/schema/regression scope is unnecessary for this bounded correction.
- Exclude only the exact sibling Tasks file, plus independent canonical plan/approval and final-delivery checks: selected; reuses existing enforcement while separating source inputs from mutable result bookkeeping.

## Planning review

R1 was approved by the actual user reply recorded below. It is retained as history, not current R2 approval.

```json
{
  "revision": 1,
  "state": "approved",
  "blockers": [],
  "upstream": {
    "proposal": "5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7"
  },
  "approval": {
    "source": "User reply in this chat on 2026-11-10 immediately after presentation of both Design R1 documents and the Gate 2 approval request.",
    "quote": "Aprovado.",
    "revision": 1,
    "digest": "801894d789455496c072bc19b29947ff2c5900df09e4725d9d9e7c8d5f8acd55"
  }
}
```

R2 is presented for approval under the user instruction to prepare a correction for the H01/H02 circular dependency. Gate 1 remains approved and unchanged. No R2 approval, Tasks revision, implementation or new operational result is asserted. The original R1 design sections describe their planning baseline; subsequent authorized implementation, PRs, terms approval and bounded route evidence are preserved at commit 1198c2cd2d39f69a12e4f5abae727725b577593a. R2 changes only the bounded input/lineage contract specified above.
