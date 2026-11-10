---
sdd_version: 3
change: contribution-security-guidance
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
  description: Walk through maintained contribution routes and restricted access recovery
  requirements:
  - REQ-001
  - REQ-002
  - REQ-006
  required: true
  method:
    kind: review
    procedure: 'Read the existing README, quickstart, SDD/GitHub guides and organization baseline alongside the
      proposed contributing guide and organization candidate. Walk through a public repository contribution without
      Harness access and an authorized private contribution, including missing private resource, missing replacement
      target and repository-specific override. Use a read-only public-access view or actual unauthenticated retrieval
      for any claimed public URL; do not infer public access from the connected account. Expected: real issue/forms
      and setup/review routes, source ownership, private links labeled optional, no invented availability and old
      usable route retained when replacement fails. Compare Issue 22/PR 33/organization PR 3 as delivered history;
      future H02 coordination is linked to Issue 35 and does not reopen prior delivery.'
    reason: Audience access, intended workflows and non-duplicated prose require scenario review; a successful authenticated
      link request alone is insufficient.
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
  - docs/validation/contribution-security-guidance
  execution: local
- id: CHECK-002
  description: Verify provenance and versioned H01 terms consumption
  requirements:
  - REQ-003
  - REQ-006
  required: true
  method:
    kind: review
    procedure: 'Read contribution rules and every tool/project terms reference. Trace the exact H01 candidate version/hash
      to real approval and allowed reference status, inspect a first-party and a third-party contribution example
      and a missing-rights/missing-approval case. Expected: distinct tool versus project permissions, source/rights/notices
      and review obligations, and no fabricated CLA/DCO/IP grant. Missing H01 approval prevents a full pass even
      if surrounding prose is complete; a changed H01 version triggers rerun. Public readers must not need a private
      link merely to contribute without the tool.'
    reason: Provenance and genuine terms approval are semantic/human evidence, not implied by file presence or check
      structure.
  inputs:
    include: *id001
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
  outputs:
  - docs/validation/contribution-security-guidance
  execution: local
- id: CHECK-003
  description: Verify the confidential reporting route and unavailable-channel behavior
  requirements:
  - REQ-004
  - REQ-006
  required: true
  method:
    kind: manual
    procedure: 'Inspect the owner-approved security-reporting record, actual destination/configuration and permitted
      responder list, then the three locale guides and public candidate. Under explicit scoped authorization for
      a synthetic submission, send only a non-sensitive unique test marker through the actual chosen route, observe
      receipt by the intended responder and confirm visibility is limited using permitted configuration/access observations.
      Record environment/time, safe receipt reference, authorized executor and limits; no credentials or real vulnerability
      payloads. Separately walk through absent/unverified channel, denied access and public-issue fallback. Expected:
      no active claim before actual configuration/receipt/access evidence, no sensitive public reporting, no invented
      endpoint or SLA. If authorization, configuration or receipt evidence is unavailable, report this required
      check unverified; a fallback-only guide cannot establish full H02 delivery. No submission or configuration
      is authorized by this Design.'
    reason: Channel confidentiality and actual receipt are external behavior and require bounded human-authorized
      observation, not a mock or agent assertion.
  inputs:
    include:
    - standards/core/security.md
    - standards/core/contribution.md
    - docs/governance/security-reporting.md
    - docs/user-docs/guides/security-reporting.md
    - docs/user-docs/guides/security-reporting.pt.md
    - docs/user-docs/guides/security-reporting.es.md
    - docs/handoffs/contribution-security-guidance
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
  outputs:
  - docs/validation/contribution-security-guidance
  execution: local
- id: CHECK-004
  description: Verify translations, navigation and the coordinated organization candidate
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  - REQ-006
  required: true
  method:
    kind: review
    procedure: 'Compare all changed EN/PT/ES README/guide and organization candidate siblings for permissions, gates,
      access/recovery and channel status. Resolve every new/edited local Markdown path/anchor; verify external targets
      at the exact intended revision and intended-reader access, identifying English-only canonical references.
      Read the organization candidate without private context and compare its diff against the fetched organization
      baseline, AGENTS instructions, profile and issue forms. Expected: no private strategy/customer/secret export,
      no competing detailed SDD manual, preserved repository precedence/forms/profile, verified replacement dependencies
      or explicit pending rollout. Record local preparation separately from public activation; unavailable public
      targets cannot be called activated. H02 does not complete Issues 23/26 or product adoption.'
    reason: Semantic translation, public-reader completeness and cross-repository access require review; deterministic
      path checks are supporting evidence.
  inputs:
    include: *id001
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
  outputs:
  - docs/validation/contribution-security-guidance
  execution: local
- id: CHECK-005
  description: Run maintained package and regression suites
  requirements:
  - REQ-001
  - REQ-005
  - REQ-006
  required: true
  method:
    kind: automated
    procedure: 'From the selected Harness checkout with Python 3.11+ and requirements-validation.txt installed,
      run PYTHONDONTWRITEBYTECODE=1 PYTHON=<selected-interpreter> ./scripts/validate/run.sh and preserve stdout/exit
      code. Expected exit 0 including Plugin validation, SDD inventory and full validator/execution suites. Existing
      legacy warnings remain qualified; no remote CI or user acceptance follows from this result. Public organization
      files have no application build suite: their focused diff/link/translation checks remain required under CHECK-004.'
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
  outputs:
  - docs/validation/contribution-security-guidance
  execution: local
- id: CHECK-006
  description: Verify stage lineage, dependency evidence and separate delivery boundaries
  requirements:
  - REQ-004
  - REQ-006
  required: true
  method:
    kind: review
    procedure: Recompute canonical current Proposal/Design/Tasks digests and actual approval bindings at the applicable
      stage; inspect all 21 local and 14 retained scenario mappings, H01 version/approval dependency, source digests
      and unchanged historical dossiers. Run --root . --change contribution-security-guidance --phase planning --json;
      after Tasks approval and explicit implementation authorization also run --phase implementation --json. Compare
      the change/action record with approved scope and keep common guidance, organization activation, each product
      adoption and H03 distribution separate. Expected pass for applicable structural checks, no operational action
      inferred from planning, and genuine evidence wherever a completed claim is made. This check does not depend
      on its own result or final delivery/archive guards.
    reason: Canonical metadata checks need contextual review of approvals, dependencies and authorization; final
      delivery is deliberately a later lifecycle step.
  inputs:
    include:
    - sdd
    - validators/sdd
    - specs/archive
    - docs/governance
    - docs/licensing
    - docs/handoffs/contribution-security-guidance
    exclude:
    - docs/validation/portfolio-licensing-policy
    - docs/validation/contribution-security-guidance
  outputs:
  - docs/validation/contribution-security-guidance
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
    requirement: REQ-001
    scenario: 4
  applicability: required
  checks:
  - CHECK-001
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
  - CHECK-004
- scenario:
    requirement: REQ-002
    scenario: 3
  applicability: required
  checks:
  - CHECK-004
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
- scenario:
    requirement: REQ-004
    scenario: 1
  applicability: required
  checks:
  - CHECK-003
- scenario:
    requirement: REQ-004
    scenario: 2
  applicability: required
  checks:
  - CHECK-003
  - CHECK-004
- scenario:
    requirement: REQ-004
    scenario: 3
  applicability: required
  checks:
  - CHECK-003
- scenario:
    requirement: REQ-004
    scenario: 4
  applicability: required
  checks:
  - CHECK-006
- scenario:
    requirement: REQ-005
    scenario: 1
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-005
    scenario: 2
  applicability: required
  checks:
  - CHECK-004
- scenario:
    requirement: REQ-005
    scenario: 3
  applicability: required
  checks:
  - CHECK-004
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
  - CHECK-001
  - CHECK-004
- scenario:
    requirement: REQ-006
    scenario: 3
  applicability: required
  checks:
  - CHECK-001
  - CHECK-002
  - CHECK-003
  - CHECK-004
  - CHECK-005
  - CHECK-006
- scenario:
    requirement: REQ-006
    scenario: 4
  applicability: required
  checks:
  - CHECK-006
regression:
- obligation:
    impact: 1
    scenario: 1
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Extend maintained contribution routes with rights and confidential reporting while retaining source
    ownership, access conditions and safe replacement behavior. Compare the specific historical acceptance position
    or captured baseline with current observable behavior; do not reuse historical results as fresh evidence.
- obligation:
    impact: 1
    scenario: 2
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Extend maintained contribution routes with rights and confidential reporting while retaining source
    ownership, access conditions and safe replacement behavior. Compare the specific historical acceptance position
    or captured baseline with current observable behavior; do not reuse historical results as fresh evidence.
- obligation:
    impact: 1
    scenario: 3
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Extend maintained contribution routes with rights and confidential reporting while retaining source
    ownership, access conditions and safe replacement behavior. Compare the specific historical acceptance position
    or captured baseline with current observable behavior; do not reuse historical results as fresh evidence.
- obligation:
    impact: 1
    scenario: 4
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Extend maintained contribution routes with rights and confidential reporting while retaining source
    ownership, access conditions and safe replacement behavior. Compare the specific historical acceptance position
    or captured baseline with current observable behavior; do not reuse historical results as fresh evidence.
- obligation:
    impact: 1
    scenario: 6
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Extend maintained contribution routes with rights and confidential reporting while retaining source
    ownership, access conditions and safe replacement behavior. Compare the specific historical acceptance position
    or captured baseline with current observable behavior; do not reuse historical results as fresh evidence.
- obligation:
    impact: 3
    scenario: 1
  checks:
  - CHECK-004
  rationale: Retain canonical English and semantically aligned localized community entry points. Compare the specific
    historical acceptance position or captured baseline with current observable behavior; do not reuse historical
    results as fresh evidence.
- obligation:
    impact: 3
    scenario: 2
  checks:
  - CHECK-004
  rationale: Retain canonical English and semantically aligned localized community entry points. Compare the specific
    historical acceptance position or captured baseline with current observable behavior; do not reuse historical
    results as fresh evidence.
- obligation:
    impact: 3
    scenario: 3
  checks:
  - CHECK-004
  rationale: Retain canonical English and semantically aligned localized community entry points. Compare the specific
    historical acceptance position or captured baseline with current observable behavior; do not reuse historical
    results as fresh evidence.
- obligation:
    impact: 3
    scenario: 4
  checks:
  - CHECK-004
  rationale: Retain canonical English and semantically aligned localized community entry points. Compare the specific
    historical acceptance position or captured baseline with current observable behavior; do not reuse historical
    results as fresh evidence.
- obligation:
    impact: 4
    scenario: 2
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Keep canonical procedures, human gates, exact-version and availability limits in reused guidance. Compare
    the specific historical acceptance position or captured baseline with current observable behavior; do not reuse
    historical results as fresh evidence.
- obligation:
    impact: 4
    scenario: 3
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Keep canonical procedures, human gates, exact-version and availability limits in reused guidance. Compare
    the specific historical acceptance position or captured baseline with current observable behavior; do not reuse
    historical results as fresh evidence.
- obligation:
    impact: 4
    scenario: 4
  checks:
  - CHECK-001
  - CHECK-004
  rationale: Keep canonical procedures, human gates, exact-version and availability limits in reused guidance. Compare
    the specific historical acceptance position or captured baseline with current observable behavior; do not reuse
    historical results as fresh evidence.
- obligation:
    impact: 5
    scenario: 0
  checks:
  - CHECK-002
  - CHECK-003
  rationale: Extend provenance and confidential handling to contribution/reporting guidance without claiming a configured
    channel. Compare the specific historical acceptance position or captured baseline with current observable behavior;
    do not reuse historical results as fresh evidence.
- obligation:
    impact: 6
    scenario: 0
  checks:
  - CHECK-002
  - CHECK-003
  - CHECK-004
  - CHECK-006
  rationale: Add the missing approved-terms references, actual channel verification and per-product adoption evidence.
    Compare the specific historical acceptance position or captured baseline with current observable behavior; do
    not reuse historical results as fresh evidence.
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 6bed2e92d705d83385b31d27364cfcda2b05549678818801c6082132d6dbc8d2
  approval:
    source: User reply in this chat on 2026-11-10 immediately after presentation of both Design R1 documents and
      the Gate 2 approval request.
    quote: Aprovado.
    revision: 1
    digest: 6f120a41ac76673587dff9355ab7fddc4e40f6f2a1e43af75a0cffa23314f3e2
---

# Design — H02

## Current state and approved scope

Change `contribution-security-guidance`, [Harness #35](https://github.com/versat-labs/versat-ai-harness/issues/35). Proposal/Requirements R1 is approved by “Aprovado. Avance ao design.” on 2026-11-10. This is Design R1, pending Gate 2 review.

Use the same exact Harness source `597b81c71a0fc0908ff5264fe9987bb5c0d8feec` and index-resolved core Standards as H01. VERSION 0.3.0 does not assert that installed 0.3.0 consumers contain every newer source capability.

Issue 22, Harness PR 33 and organization PR 3 provide the maintained multilingual entry and guides. The organization's contribution route is public; its detailed Harness links are explicitly private and pinned to `27735687a37e896cd6b0c95cd9d2d848ee166d90`. Preserve that useful behavior. No terms approval or operational confidential route has been verified. No earlier documentation result certifies these new outcomes.

## Proposed design

### Canonical rules and maintained guides

These are intended implementation targets; this Design creates none of them.

| Target | Responsibility |
|---|---|
| `standards/core/contribution.md` | Common provenance, applicable terms, contributor/reviewer responsibilities, repository-specific precedence and review/check requirements. Reference H01 licensing policy and existing Git/Testing/Documentation/Language Standards. |
| `standards/index.yaml` | Add `core/contribution.md` once to `core.always`; coordinate with H01's distinct index entry. No copied per-profile policy or new resolver. |
| `standards/core/security.md` | Extend the existing Standard with confidential-reporting principles, verified route ownership, minimization and safe unavailable-channel behavior. Keep this canonical security rule here. |
| `docs/user-docs/guides/contributing.md`, `.pt.md`, `.es.md` | One useful contribution journey and a missing-access/rights recovery path. Link existing setup, SDD, GitHub delivery and validation guides instead of copying them. |
| `docs/user-docs/guides/security-reporting.md`, `.pt.md`, `.es.md` | Distinct reporting journey: safe prerequisites, actual approved route when verified, otherwise explicit unavailable status and non-sensitive contact request. No unapproved SLA. |
| `docs/governance/security-reporting.md` | Non-sensitive route configuration/decision record, accountable contact, intended audience, access scope, authorization and verification status; no vulnerability payloads or secrets. |
| `README.md`, `.pt.md`, `.es.md` | Localized navigation to real guides only. No new competing root CONTRIBUTING manual in Harness. |
| `docs/handoffs/contribution-security-guidance/organization/` | Reviewable organization baseline/candidate/diff and safe provenance record for a future authorized update. It is private preparation in Harness, not public activation. |

Normative rules stay in Standards. The guides explain practical use, prerequisites and recovery. `sdd/README.md` remains the detailed SDD manual. The organization entry retains a short self-contained public route and optionally links to private internal detail with explicit access labels.

The organization candidate includes EN/PT/ES CONTRIBUTING files. Change organization README locale siblings only if navigation or descriptions actually change; preserve profile and issue forms unchanged. Record original repository/ref/blob, permitted content snapshot and candidate diff under `baseline/`, `candidate/` and a small handoff record. Never invent an organization commit URL for an uncommitted candidate. Refresh the organization baseline and its AGENTS instructions during implementation before preparing a patch; existing PR 3's evidence is historical, not a lease against future remote changes.

### Contribution flow

1. Choose a target repository and read its available README/instructions; repository-specific contribution guidance takes precedence.
2. Use its available issue forms and identify an existing or new actual work item. Describe the expected result, scope and relevant reproduction context without sensitive data.
3. Identify original and third-party material, provenance, applicable project terms and required notices. Unclear rights require resolution before acceptance; this guide creates no implied IP transfer or blanket licensing permission.
4. If using Harness/plugin, refer to the actual approved H01 terms/notices version. Tool terms do not alter the destination project license. If tool access/terms are unavailable, report that limitation; an external contributor can still follow the target's public route without the tool.
5. Follow the target's setup, approved SDD stages where applicable, checks and PR review. Reuse maintained guides for detail; preserve the distinctions among planning approval, implementation authorization, archive, PR, merge and release.

Do not introduce CLA, DCO, copyright assignment or a new contribution-license mechanism without an explicit rights decision and, where material, reopening the affected plan. The approved H01 terms are an input, not text H02 rewrites.

### Confidential route and its states

Elvis Zoz (`@elviszoz`) is the accountable security contact and coordinator. A named owner alone is not a working channel. This design defines a provider-neutral reporting contract and verification method; it does not choose or enable a mailbox, GitHub setting or external service without observed availability and scoped authorization.

The route record must identify the actual destination/provider, applicable repository/product scope, intended reporters, intended recipients/access boundary, owner authorization, data-minimization/retention instructions, verification time, safe evidence references and known limits. Keep endpoint status separate from documentation readiness:

| State | Allowed guide behavior | Completion effect |
|---|---|---|
| No selected/approved route | State that confidential reporting is not yet verified; permit only a non-sensitive request for private instructions through an existing visible maintainer/repository contact. Do not invent an address or ask for vulnerability details publicly. | Draft/review progress only; not full H02 delivery. |
| Selected but unverified | Describe internal setup/verification work as pending; do not advertise the route as active. | Required route check remains unverified. |
| Verified | Use the actual destination, supported audience and safe reporting instructions backed by configuration/access and synthetic receipt evidence. | Supports H02 acceptance for that stated scope only. |
| Changed, failed or withdrawn | Withdraw the active claim and use the safe fallback; reverify affected configuration and receipt. | Reopen affected acceptance evidence until resolved. |

Verification requires a separately authorized synthetic submission containing only a non-sensitive unique marker. Observe actual receipt by an intended responder and available access/configuration evidence. Do not send a real exploit, customer information, credentials or an unrequested message. If the test needs a setting/permission change, obtain that separately scoped authorization; this Design and eventual Tasks approval alone do not activate it. An authenticated administrator view alone cannot prove reporter access or confidential isolation; capture intended-user observations or state the missing verification.

A fallback demonstrates safe failure behavior. It cannot replace the approved requirement for a verified confidential route at complete H02 delivery. No promise of response time, continuous monitoring or retention period is invented. The owner must supply any operational commitments before they appear in instructions.

## H01 dependency and external handoffs

| Boundary | Input or output | Completion limit |
|---|---|---|
| H01 → H02 | Canonical common policy; exact proprietary terms/notices revision, hash and real approval reference; audience/access conditions. | A pending/changed H01 text blocks or invalidates the corresponding H02 approved-terms check. H02 does not apply the terms. |
| Harness → public `.github` | Sanitized short organization candidate, EN/PT/ES, real target references, baseline/diff and validation evidence. | Local candidate preparation is not live adoption. No public write, PR or link activation is currently authorized. |
| H02 → P01/P03 | Common rules, reusable guides and explicit per-repository adoption/route checks. | Each product must identify its own terms, owner, applicable channel and evidence; no automatic adoption. |
| H02 → H03 | Approved contribution/security resources and reference status. | H03 owns public package accessibility and external install/update/use verification. A public contributor route that does not use the tool remains independent. |
| Issues 23/26 | Reuse current documentation/language standards. | H02 does not implement general documentation automation or multilingual CI. |

Public candidate text must stand alone without private strategy, internal commercial rationale or mandatory private terms links for a tool-free contribution. Internal private links remain optional and explicitly marked; do not mark a new public tool-terms URL available until it really exists for the intended reader. If H03 has not made the tool available, the entry states that limitation and preserves the independent public contribution route.

The organization repository's AGENTS and review rules apply to any future write there. Preserve the profile, issue-form fields/types/projects and repository precedence. Future routing changes use an existing verified immutable target; keep the old usable route if the replacement is unavailable. H02 can prepare a sanitized candidate and its dependencies privately, but must report the live organization rollout pending until actually authorized and observed.

## Data, security and permissions

Never copy vulnerability reports, credentials, private customer data, employment/legal documents or unneeded private strategy into guides or evidence. Keep configuration credentials in the approved secret store. The source record contains only safe route metadata and restricted evidence references that authorized reviewers can actually inspect; a broken or inaccessible reference cannot pass.

Input snapshots bind local configuration records, guides, terms and candidate text, not live remote state. Record remote provider/repository revision, safe configuration observations, intended reader and time for each relevant check. Known external changes invalidate affected evidence even if local hashes match. The entire repository is the current package boundary; H03 must clear the actual export surface before distributing any of these materials.

## Operations, migration, rollout and rollback

This is documentary policy/guidance work with no new service, schema, database, installer or policy engine. Operational records are owner decisions, actual terms and route evidence, input versions and per-repository adoption. No monitoring or response service is claimed merely because a guide exists.

Future authorized implementation proceeds in this dependency order: complete private policy/guides and local organization candidate; obtain the required exact H01 terms approval and real confidential-route evidence; finish current acceptance checks; prepare the Harness dossier for delivery. Source-only preparation does not upgrade consumers. A later authorized organization rollout checks that its approved source/links already exist for the intended reader and follows that repository's review requirements. Publication/distribution remains outside current authorization.

H01 and H02 currently share a planning checkout. H01 owns licensing policy/terms; H02 owns contribution/reporting policy/guides. Coordinate additive index and README edits and revalidate the final combined inputs. If either terms/version, the organization baseline or another shared input changes, rerun affected checks rather than carrying forward old results. Verify upstream drift before implementation while preserving the selected provider.

On failure, keep existing public entry guidance and mark new material pending. If an authorized later rollout introduces a broken link or invalid reporting claim, restore the last verified entry/fallback first, then review a corrective Harness change. Preserve superseded evidence; do not delete an actual report as part of documentation rollback or represent a Git revert as a security access revocation.

## Alternatives and architectural decision

- Reopen Issue 22/rewrite the complete user manual: rejected; the delivered foundations remain useful and the new work is residual contribution/security policy.
- Publish only links into the private Harness: rejected; external contributors need an independently usable public route.
- Add a full duplicate CONTRIBUTING manual to every repository: rejected; short local adoption and canonical guidance preserve ownership while letting each project override defaults.
- Choose/enable a new security service now: rejected; availability, access and operational authority are unverified. The selected provider must satisfy the same concrete route contract and observed test before delivery.
- Treat unavailable-channel fallback as complete H02: rejected; it covers failure behavior but cannot satisfy required live verification.

No new ADR is required: this extends current Standards and maintained guides within ADR-0011 and the existing SDD/exact-version contracts. It does not change package boundaries or add a runtime service. If implementation discovery requires a new architectural service/boundary or different contribution-rights mechanism, reopen the affected planning stage and review an ADR when appropriate.

## Validation plan and closure order

The six planned checks cover all 21 local scenarios and 14 retained regression obligations, with no exclusions. The intentional supersession of old Issue 22 traceability is covered by current REQ-006 and CHECK-001/004/006: old delivery remains historical, new coordination uses Issue 35 and preserves destination/access/review checks.

CHECK-001 exercises actual audience/recovery workflows; CHECK-002 requires actual approved terms; CHECK-003 requires the real authorized route test; CHECK-004 reviews localized content and coordinated candidate; CHECK-005 retains complete package suites; CHECK-006 reviews lineage and boundaries without a closure dependency. Historical acceptance methods may be reused, not their old passing results. Full required CI on any later PR remains separate from local evidence.

Prepare stable source inputs before capture. Record a canonical input digest immediately before and after each real check, along with environment and remote-state observations where relevant. Outputs under `docs/validation/contribution-security-guidance/` are excluded from broad roots. Both check output directories are excluded to avoid treating sibling check reports as product inputs; H01 terms and review records remain included as true dependencies. Missing future input paths are explicit, not evidence that corresponding implementation or verification is unnecessary.

Once later Tasks and implementation are authorized, finish actual task work, all required checks, individual assessments and resolved findings before recording completion. Then run selected delivery, move the unique dossier when eligible, and run selected delivery with `--require-archive`. These are mandatory lifecycle guards after acceptance; they are not self-prerequisites of a required check or task. Missing H01 approval or confidential-route evidence blocks delivery even when structural checks and translations pass. Reopen affected work after failure; never mark unavailable checks not-applicable.

No technical blocker prevents Gate 2 review. Exact channel selection/configuration, owner operational commitments and actual H01 terms approval are future delivery inputs handled by the specified contract and stop conditions. They remain unverified today. No live channel test, public organization change or actual terms application has been performed by Design preparation.

## Planning review

Design R1 awaits review. The actual Proposal/Requirements R1 approval and unchanged upstream digest are recorded. No Tasks file exists. Approval permits Tasks preparation for this change; it does not authorize implementation, messages, channel activation, public rollout or license changes.

2026-11-10: after both Design R1 documents were presented with the Gate 2 question, the user replied "Aprovado." The recomputed canonical Design digest matched the presented revision: `6f120a41ac76673587dff9355ab7fddc4e40f6f2a1e43af75a0cffa23314f3e2`. This records Gate 2 approval and authorizes Tasks preparation only. Earlier awaiting-review wording in this bookkeeping section describes the presentation; it is superseded by this actual approval. No implementation or operational authorization is inferred.
