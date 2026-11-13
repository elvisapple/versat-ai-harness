---
sdd_version: 3
change: harness-publication-readiness
requirements:
- id: REQ-001
  statement: Prepare a separately reviewed Apache-2.0 licensing candidate for eligible first-party Harness and Plugin
    material.
  acceptance:
  - Given the existing proprietary candidate, the successor identifies the exact files and clauses to replace, prepares
    concrete Apache-2.0 license/notice and contribution wording for review, and preserves the earlier approved text
    and approval as historical evidence without transferring that approval.
  - Given the proposed Apache scope, the candidate covers eligible first-party code, documentation and templates
    explicitly, allows general and commercial use, modification, redistribution and forks under the applicable terms,
    and retains third-party terms and notices without imposing the tool license on destination projects.
  - Given proposed license text, owner selection, SDD approval and CODEOWNERS are distinguished from review of that
    exact text and effective adoption; the reviewed revision/hash, actual reviewer capacity and remaining specialist
    questions are recorded without inventing an effective date, signature, CLA, DCO or IP assignment.
- id: REQ-002
  statement: Refresh component rights and dependency evidence for the exact proposed distribution surface.
  acceptance:
  - Given the bounded H01 first-party attestation, source inventory and reviewed dependency texts, the successor
    reuses their actual scope and dates, inspects changes since that baseline and records original/copied/generated
    material, grants, direct/transitive dependencies, versions, distribution modes and required notices for the
    proposed candidate.
  - Given a missing grant, incompatible dependency, inaccessible evidence or unconfirmed reviewer capacity, the
    affected component remains defer or retain-private with an accountable contact and exit condition; a clean scan,
    declaration of ownership or passing package check is not clearance.
  - Given a reviewed component, the decision record identifies repository/revision, rights holder as declared or
    verified, evidence access, concrete terms/notices, actual reviewer and capacity, method/date, disposition and
    remaining limitations; sensitive contracts or personal data remain in approved restricted storage.
- id: REQ-003
  statement: Assess the complete surface exposed by making the existing repository public.
  acceptance:
  - Given the proposed public repository, inventory the working tree and reachable history, branches/tags, releases/assets,
    LFS, fixtures, SDD/validation records, issues/PRs/comments/attachments, discussions/wiki/Pages where present,
    packages and CI logs/artifacts/caches plus relevant metadata; classify each as observed-reviewed, observed-absent
    or inaccessible/unverified.
  - Given confidential material in a current file, an old commit, an attachment or an execution record, record the
    finding and bounded evidence privately outside the future public surface, defer clearance, and require authorized
    remediation and re-review; moving or deleting the current file alone cannot clear history.
  - Given unavailable remote surfaces or drift after a review, retain the unknowns and invalidate affected readiness
    claims; if safe publication requires history rewriting, destructive cleanup, a different destination or loss
    of immutable evidence, stop for separately scoped authorization and material replanning instead of silently
    changing the agreed existing-repository approach.
- id: REQ-004
  statement: Preserve the canonical root package and exact-version compatibility while preparing a releasable candidate.
  acceptance:
  - Given a candidate version, VERSION, portable/Codex manifests, marketplace reference and template/provider references
    agree, and all supported Skills resolve matching Standards, SDD, templates, schemas and validators from the
    same root without copied policy trees or a separate SDK/mirror.
  - Given the current versat-internal marketplace pinned to v0.3.0, source/main edits do not imply release availability
    or consumer updates; preserve identity by default, select a new exact release only after version-impact review,
    and never retag an existing release or silently choose latest.
  - Given a justified identity or supported-runtime compatibility change, review concrete old-to-new migration and
    recovery before adoption, retain the existing usable installation path until its replacement is verified, and
    distinguish source-snapshot behavior from behavior actually shipped in a release.
- id: REQ-005
  statement: Prepare and exercise an external-user installation, first-use, update and recovery guide within authorized
    rehearsal boundaries.
  acceptance:
  - Given a reviewed candidate and stated prerequisites, a controlled private rehearsal exercises the documented
    package installation and a representative planning contribution, observes the expected Proposal/Requirements
    and Gate 1 stop, and verifies access to matching resources; record exact candidate/runtime/actions/results without
    claiming anonymous public access.
  - Given missing access, an unavailable or incompatible version, absent Skill resources or a failed update, the
    documented workflow reports the specific failure and retains or restores the previous verified compatible version
    without silently upgrading or pretending success.
  - Given an explicit old-to-new update, instructions identify both exact references and separately reviewed consumer
    lock migration, with checks and recovery; publishing source or refreshing a marketplace does not automatically
    migrate installed consumers.
  - Given later separately authorized publication, the operational follow-up must verify anonymous source/package
    access and installation, update and representative contribution by an intended external user without private
    repository or Versat workspace membership; until observed, these outcomes remain unverified and cannot be relabelled
    as rehearsal passes.
- id: REQ-006
  statement: Prepare a self-contained public contribution route and assess actual repository controls.
  acceptance:
  - Given an external contributor, maintained guidance explains target repository/issue selection, provenance, applicable
    tool and destination-project terms, fork/branch/PR, setup, SDD gates, required checks and maintainer review;
    repository-specific guidance takes precedence and public read/fork access grants no write, merge or release
    authority.
  - Given pre-publication control assessment, inspect actual CODEOWNERS, required reviews, protected branches/rulesets,
    required checks and fork-workflow token/secret boundaries against the documented acceptance; inaccessible, ineffective
    or unsafe controls remain blockers to operational readiness rather than inferred from local YAML.
  - Given a proposed control change or external contribution test, record its separately authorized operation and
    verify its result, including effects of changed repository visibility; no current planning instruction modifies
    controls or opens a remote contribution, and missing rights/review prevents contribution acceptance.
- id: REQ-007
  statement: Prepare Harness-specific confidential reporting guidance with scoped verification and safe failure
    handling.
  acceptance:
  - Given prior H02 evidence, preserve its limited .github public pilot and private Harness email observations,
    existing accountable contact and CODEOWNER responsibility; neither establishes a public Harness reporting route
    or justifies asking again for the same unchanged ownership decision.
  - Given the intended Harness route, document destination, intended reporters, permitted recipients, accountable
    responder and data-handling boundaries; any claim of availability requires actual access/configuration observations
    and separately authorized non-sensitive synthetic submission/receipt for this repository and audience.
  - Given missing, failed or changed route verification, retain unverified status and a non-sensitive request-for-private-instructions
    fallback through an existing visible maintainer contact; publish no exploit details, invented endpoint, SLA,
    retention period or internal email address. Public-audience checks unavailable before publication remain explicit
    operational follow-up, not waived acceptance.
- id: REQ-008
  statement: Make the maintained developer documentation safe, accessible and aligned in English, Portuguese and
    Spanish.
  acceptance:
  - Given changed README, quickstart, product context, licensing, setup, contribution or reporting guidance, English
    and matching Portuguese/Spanish versions explain actual purpose, audience, ownership, availability, prerequisites,
    expected results and recovery with working localized navigation to canonical technical sources.
  - Given a public-facing candidate, an external reader can follow it without private strategy links, internal recordings,
    confidential evidence or membership; preserve useful canonical workflows and public provenance, qualify unverified
    claims, and retain confidential historical provenance only in approved restricted evidence rather than exporting
    it.
  - Given changed commands, UI steps or translations, compare observed behavior with expected results and review
    semantic parity, links/anchors and access boundaries; missing runtime/access is unverified, structural success
    alone is not user acceptance, and living guides remain outside movable SDD dossiers.
- id: REQ-009
  statement: Produce a truthful preparation record and a separately executable publication handoff.
  acceptance:
  - Given preparation review, record exact candidate, surface inventory, component/text review, control observations,
    actual checks, blockers and accountable next actions; distinguish documentation prepared, candidate reviewed,
    cleared or deferred, merged, license adopted, visibility changed, release available and consumers migrated.
  - Given incomplete rights, surface, controls, channel or required execution evidence, preparation may report a
    completed assessment with defer and explicit blockers, but must not claim publish-ready, effective adoption,
    public availability or completed H03; the later Design must bind meaningful current checks and all retained
    obligations without replacing them with a document-presence check.
  - Given a future operational request, its reviewed runbook identifies exact actions/authority, pre-action drift
    and control checks, bounded sequencing, expected observations and stop/containment decisions; pre-merge preparation
    tasks do not depend on their own final merge or on unauthorized publication.
  - Given a failed rollout, preserve evidence and use separately authorized containment; changing visibility back
    or reverting metadata cannot promise withdrawal of existing public copies, forks or permissions already granted.
    Actual post-action access/install/update/reporting/control results remain separate evidence.
- id: REQ-010
  statement: Preserve attributable history and the distinction between private evidence and a safe public package.
  acceptance:
  - Given delivered H01/H02, root-package and documentation dossiers, preserve their bytes, approval sources and
    historical results during this planning change; a new successor carries changed requirements and genuine approvals,
    and old passes never become acceptance of the new Apache/public scope.
  - Given active guidance based on historical proprietary restrictions, a later authorized implementation updates
    the effective guidance and clearly identifies superseded candidate status while retaining the exact reviewed
    historical text and its approval provenance; no historical approval is rewritten.
  - Given sensitive history or private evidence currently inside the root package, preserve an attributable restricted
    record and block public exposure until a separately approved disposition is feasible; this plan authorizes neither
    copying confidential evidence into new public-facing material nor destructive history remediation.
- id: REQ-011
  statement: Keep other product deliveries and unrelated Harness capabilities independent.
  acceptance:
  - Given Platform/Workspace, Discover/CRM and destination projects, preserve their independently selected models
    and per-repository rights, adoption, contribution and operational evidence; the Harness successor neither changes
    their terms nor completes or automatically blocks their handoffs.
  - Given existing organization guidance, preserve its usable entry route, identity, issue forms, repository precedence
    and local checks; any future cross-repository routing change needs its own authorization/review and verified
    destination, with the existing route retained on failure.
  - Given adjacent dependency-management, multilingual automation, infrastructure, product, commercial or hiring
    initiatives, do not absorb them or claim their completion; keep canonical Standards, SDD enforcement and all
    maintained validation suites intact without introducing a new distribution engine.
- id: REQ-012
  statement: Observe the three planning gates and the user-authorized planning-only boundary.
  acceptance:
  - Given the current request, create only proposal.md and requirements.md for this stable change ID, with assessed
    impact, review revision 1 awaiting approval and approval null; run planning diagnostics while leaving implementation,
    living documents, licenses, manifests and remote state unchanged.
  - Given approval of the presented Proposal/Requirements revision, only Design becomes permitted; Tasks follows
    Design approval, and implementation requires approved Tasks plus an explicit execution request. Substantive
    scope/design/task revisions reopen the earliest affected gate.
  - Given any local planning pass, it is not approval of unseen artifacts, license text, effective adoption, commit/push/PR,
    merge, release/tag, visibility/permissions/channel changes, test messages, consumer upgrades or destructive
    remediation; each later action requires its applicable scoped authority.
---

# Requirements

## Actors and context

The owner reviews the public Apache direction and each SDD gate. Harness maintainers and actual rights/security reviewers prepare the candidate and evidence; an authorized administrator performs only separately scoped operational actions. External contributors need a self-contained public route, while current internal users retain a verified exact-version path and explicit upgrades.

## Functional requirements

REQ-001–REQ-003 cover candidate licensing, evidence and the entire proposed public surface. REQ-004–REQ-008 cover the root package, installation/update/recovery, contribution controls, confidential reporting and multilingual maintained guides. This change proposes implementation of the preparation candidate after planning approval; none of these outcomes is asserted delivered now.

## Non-functional requirements

REQ-009–REQ-012 govern truthful readiness, attribution/history, private evidence, independent products, retained validation and authorization. Preserve canonical ownership and version consistency; do not duplicate Standards in Skills or create an automatic publication engine. High-risk findings remain visible and prevent the corresponding clearance.

## Acceptance scenarios

The frontmatter acceptance arrays are normative, one-based scenarios. Design will map all positions and every retained impact obligation to checks or an explicitly reviewed exclusion. Preserve success, unavailable-version/update-failure, missing-rights, confidential-history, unavailable-channel/control, drift and recovery cases; missing execution is unverified, not not-applicable.

Preparation acceptance must distinguish an assessment completed with defer from actual publish readiness. A deferred item is never counted as a verified operational outcome. Required package rehearsal and safe guide behavior need actual observations in later implementation; a file or plan alone is insufficient. Public access, public-audience report receipt and post-visibility controls require the separately authorized operational follow-up and cannot be fabricated before it.

## Constraints and assumptions

- Current authority is Proposal/Requirements only. R1 approval permits Design, not implementation or public release.
- The existing repository and canonical root remain the intended destination/package; the license direction is Apache-2.0 for eligible first-party material, with third-party terms preserved.
- No historical dossier or frozen approved terms are edited during planning. Any future remediation conflict involving sensitive immutable history must be explicitly resolved before exposure.
- Existing accountable contacts and bounded evidence are reused; actual current review, complete scope and effective permissions are not inferred from them.
- Private strategy and sensitive review evidence remain outside the future public surface. Public-facing guidance must not depend on that material.
- Exact release number, runtime support and operational sequencing are Design decisions grounded in evidence. Nothing silently repins v0.3.0, alters installed consumers or assumes current source is already shipped.
- Other products, organization repository operations, commercial experiments and hiring retain their independent scope and authorization.
