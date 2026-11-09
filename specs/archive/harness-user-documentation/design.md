---
sdd_version: 3
change: harness-user-documentation
requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007]
adrs: [ADR-0010, ADR-0011, ADR-0013]
validation:
  - id: CHECK-001
    description: Content ownership, product context and canonical behavior
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-006, REQ-007]
    required: true
    method:
      kind: review
      procedure: "Review every English page against the page inventory and ownership tables below, the approved scenarios, index-resolved Standards, current Skills and SDD. Compare source/version claims with observed files; inspect the product overview against the base topic model and Issue 22. Confirm one concise first action, no empty guides or duplicate full procedures, accurate approval/archive boundaries, exact-version limits, source links and explicit unknowns. Record page/section observations and every gap in content-review.md."
      reason: "Meaning, duplication, product evidence and applicability require editorial assessment; syntax or file counts cannot establish them."
    inputs:
      include: [AGENTS.md, README.md, README.pt.md, README.es.md, VERSION, CHANGELOG.md, plugin.json, .codex-plugin, .agents/plugins, requirements-validation.txt, standards, skills, sdd, schemas, validators, scripts, tests, project-templates, .github, docs, specs]
      exclude: [docs/validation/harness-user-documentation/runs]
    outputs: [docs/validation/harness-user-documentation/runs]
    execution: local
  - id: CHECK-002
    description: Navigation, translated content and rendered Markdown
    requirements: [REQ-001, REQ-002, REQ-003, REQ-005, REQ-006, REQ-007]
    required: true
    method:
      kind: review
      procedure: "Inventory all in-scope English/PT/ES files and traverse every local link and anchor in the changed pages, including the organization candidate snapshot. Check cross-repository links against the pinned target snapshot and CHECK-004 remote observations. Compare each translated section, example, command, warning and locale switch with English. Preview representative rendered README, quickstart, guide, product and organization pages in each language. Verify no living guide links into this change dossier; recheck navigation after archival. Record a per-file link/locale matrix and mismatches in navigation-translations.md."
      reason: "Semantic translation alignment and rendered navigation need review; use existing link or Markdown tooling where available without introducing a new enforcement subsystem."
    inputs:
      include: [AGENTS.md, README.md, README.pt.md, README.es.md, VERSION, CHANGELOG.md, plugin.json, .codex-plugin, .agents/plugins, requirements-validation.txt, standards, skills, sdd, schemas, validators, scripts, tests, project-templates, .github, docs, specs]
      exclude: [docs/validation/harness-user-documentation/runs]
    outputs: [docs/validation/harness-user-documentation/runs]
    execution: local
  - id: CHECK-003
    description: Observed first use and changed usage examples
    requirements: [REQ-002, REQ-003, REQ-006, REQ-007]
    required: true
    method:
      kind: manual
      procedure: "Follow the final workspace/quickstart instructions in an available supported Codex environment using synthetic disposable repository data and the declared exact provider. Perform the documented planning request and inspect actual Proposal/Requirements and the Gate 1 stop with no fabricated approval, Design, Tasks or implementation. Exercise a missing prerequisite and confirm the documented recovery route. For each other newly introduced or materially changed runnable example, record inputs, actual actions and expected-versus-observed results; reuse current functional evidence only when it covers the same steps and inputs. Capture environment/version and gaps in usage-walkthrough.md; unavailable required UI or execution evidence is unverified."
      reason: "Actual user interaction and runtime availability cannot be inferred from Markdown or deterministic validator success. This is documentation verification, not a change to Skill behavior or a mandatory rerun of every historical evaluation."
    inputs:
      include: [AGENTS.md, README.md, README.pt.md, README.es.md, VERSION, CHANGELOG.md, plugin.json, .codex-plugin, .agents/plugins, requirements-validation.txt, standards, skills, sdd, schemas, validators, scripts, tests, project-templates, .github, docs, specs]
      exclude: [docs/validation/harness-user-documentation/runs]
    outputs: [docs/validation/harness-user-documentation/runs]
    execution: local
  - id: CHECK-004
    description: Organization consolidation, public access and cross-repository delivery
    requirements: [REQ-001, REQ-003, REQ-005, REQ-006, REQ-007]
    required: true
    method:
      kind: review
      procedure: "Compare original and candidate organization snapshots with the ownership map; verify detailed setup/process content is replaced by descriptive links, local identity/default behavior/checks and repository precedence survive, and translations agree. Check a public/no-Harness-access reading path without changing permissions. Once source publication is authorized, fetch every linked Harness file at the full immutable content commit, verify anchors and intended-reader access, and compare bytes with reviewed targets. Inspect Issue 22 traceability and prepared delivery metadata in both repositories, and the fail-closed rollout/rollback instructions. Exercise a missing-target case by withholding the candidate activation and confirming the existing organization entry is retained; never activate a real broken link. Record observed refs, hashes, link results, local review readiness and separate remote publication/merge facts in organization-review.md. Missing source publication or access prevents a full pass."
      reason: "Organization defaults, private access and ordered delivery need review and external observations; the local SDD validator cannot authenticate remote contents, PR review or merge."
    inputs:
      include: [AGENTS.md, README.md, README.pt.md, README.es.md, VERSION, CHANGELOG.md, plugin.json, .codex-plugin, .agents/plugins, requirements-validation.txt, standards, skills, sdd, schemas, validators, scripts, tests, project-templates, .github, docs, specs]
      exclude: [docs/validation/harness-user-documentation/runs]
    outputs: [docs/validation/harness-user-documentation/runs]
    execution: local
  - id: CHECK-005
    description: Maintained package validation and repository checks
    requirements: [REQ-001, REQ-003, REQ-006, REQ-007]
    required: true
    method:
      kind: automated
      procedure: "Run PYTHON=<prepared-python> ./scripts/validate/run.sh from the Harness checkout with requirements-validation.txt installed and retain the full result in package-validation.txt. Expect package/SDD validation and both complete maintained test suites to pass. Run git diff --check on both actual implementation checkouts and inspect added files for whitespace. Before an authorized completed-work submission run the existing selected delivery --require-archive check; retain final CI outcomes separately. No new tests or executable link validator are required solely for these prose edits."
    inputs:
      include: [AGENTS.md, README.md, README.pt.md, README.es.md, VERSION, CHANGELOG.md, plugin.json, .codex-plugin, .agents/plugins, requirements-validation.txt, standards, skills, sdd, schemas, validators, scripts, tests, project-templates, .github, docs, specs]
      exclude: [docs/validation/harness-user-documentation/runs]
    outputs: [docs/validation/harness-user-documentation/runs]
    execution: local
coverage:
  - scenario: {requirement: REQ-001, scenario: 1}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-001, scenario: 2}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-001, scenario: 3}
    applicability: required
    checks: [CHECK-001, CHECK-004]
  - scenario: {requirement: REQ-002, scenario: 1}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-002, scenario: 2}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-002, scenario: 3}
    applicability: required
    checks: [CHECK-001, CHECK-002]
  - scenario: {requirement: REQ-003, scenario: 1}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-003, scenario: 2}
    applicability: required
    checks: [CHECK-001, CHECK-002]
  - scenario: {requirement: REQ-003, scenario: 3}
    applicability: required
    checks: [CHECK-001, CHECK-004]
  - scenario: {requirement: REQ-003, scenario: 4}
    applicability: required
    checks: [CHECK-001, CHECK-003]
  - scenario: {requirement: REQ-004, scenario: 1}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-004, scenario: 2}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-004, scenario: 3}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-005, scenario: 1}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-005, scenario: 2}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-005, scenario: 3}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-005, scenario: 4}
    applicability: required
    checks: [CHECK-002, CHECK-004]
  - scenario: {requirement: REQ-006, scenario: 1}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-006, scenario: 2}
    applicability: required
    checks: [CHECK-003]
  - scenario: {requirement: REQ-006, scenario: 3}
    applicability: required
    checks: [CHECK-001, CHECK-002, CHECK-005]
  - scenario: {requirement: REQ-006, scenario: 4}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-007, scenario: 1}
    applicability: required
    checks: [CHECK-001, CHECK-004]
  - scenario: {requirement: REQ-007, scenario: 2}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-007, scenario: 3}
    applicability: required
    checks: [CHECK-004]
  - scenario: {requirement: REQ-007, scenario: 4}
    applicability: required
    checks: [CHECK-001, CHECK-003, CHECK-004]
  - scenario: {requirement: REQ-007, scenario: 5}
    applicability: required
    checks: [CHECK-002, CHECK-004, CHECK-005]
  - scenario: {requirement: REQ-007, scenario: 6}
    applicability: required
    checks: [CHECK-004]
regression:
  - obligation: {impact: 1, scenario: 1}
    checks: [CHECK-001, CHECK-003]
    rationale: Retain useful first-use coverage, reuse and avoidance of empty or fictional guidance.
  - obligation: {impact: 1, scenario: 2}
    checks: [CHECK-001, CHECK-003]
    rationale: Retain useful first-use coverage, reuse and avoidance of empty or fictional guidance.
  - obligation: {impact: 1, scenario: 3}
    checks: [CHECK-001, CHECK-003]
    rationale: Retain useful first-use coverage, reuse and avoidance of empty or fictional guidance.
  - obligation: {impact: 2, scenario: 1}
    checks: [CHECK-002]
    rationale: Retain actual README destinations, proportional guide structure, shared setup links and archive-independent navigation.
  - obligation: {impact: 2, scenario: 2}
    checks: [CHECK-002]
    rationale: Retain actual README destinations, proportional guide structure, shared setup links and archive-independent navigation.
  - obligation: {impact: 2, scenario: 3}
    checks: [CHECK-002]
    rationale: Retain actual README destinations, proportional guide structure, shared setup links and archive-independent navigation.
  - obligation: {impact: 2, scenario: 4}
    checks: [CHECK-002]
    rationale: Retain actual README destinations, proportional guide structure, shared setup links and archive-independent navigation.
  - obligation: {impact: 3, scenario: 1}
    checks: [CHECK-001, CHECK-003]
    rationale: Retain the single SDD entry point and phase-specific expected outcomes.
  - obligation: {impact: 3, scenario: 2}
    checks: [CHECK-001, CHECK-003]
    rationale: Retain the single SDD entry point and phase-specific expected outcomes.
  - obligation: {impact: 4, scenario: 1}
    checks: [CHECK-001, CHECK-002, CHECK-003]
    rationale: Retain real human approval and separate execution authority in English and translations.
  - obligation: {impact: 4, scenario: 2}
    checks: [CHECK-001, CHECK-002, CHECK-003]
    rationale: Retain real human approval and separate execution authority in English and translations.
  - obligation: {impact: 5, scenario: 1}
    checks: [CHECK-001, CHECK-004]
    rationale: Retain pre-submission archive prerequisites and separate observed merge from local readiness.
  - obligation: {impact: 5, scenario: 2}
    checks: [CHECK-001, CHECK-004]
    rationale: Retain pre-submission archive prerequisites and separate observed merge from local readiness.
  - obligation: {impact: 6, scenario: 0}
    checks: [CHECK-002]
    rationale: Retain the current English/PT/ES translation contract.
  - obligation: {impact: 7, scenario: 1}
    checks: [CHECK-003, CHECK-004]
    rationale: Retain observed command/UI verification, honest unavailable evidence and adequate evidence reuse.
  - obligation: {impact: 7, scenario: 2}
    checks: [CHECK-003, CHECK-004]
    rationale: Retain observed command/UI verification, honest unavailable evidence and adequate evidence reuse.
  - obligation: {impact: 7, scenario: 3}
    checks: [CHECK-003, CHECK-004]
    rationale: Retain observed command/UI verification, honest unavailable evidence and adequate evidence reuse.
  - obligation: {impact: 7, scenario: 4}
    checks: [CHECK-003, CHECK-004]
    rationale: Retain observed command/UI verification, honest unavailable evidence and adequate evidence reuse.
  - obligation: {impact: 8, scenario: 0}
    checks: [CHECK-002, CHECK-004]
    rationale: Retain organization-specific and public contribution behavior while consolidating detailed instructions.
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 1ca3de32bdea8b921030786aea349b2dc5a50a3a265aa75ee25a39e1b3308f24
  approval:
    source: Developer reply in this chat after Design R1 was presented for Gate 2 approval.
    quote: aprovado
    revision: 1
    digest: a0f7141be1f9302d1824c2c181457d1c243bf7c2f5722db505bcdd755af4652a
---

# Design

## Current state

Proposal/Requirements R2 is approved by the developer's “Ok aprovado” response. This Design binds that approved digest and retains its seven requirements, 27 acceptance scenarios and 19 regression obligations.

The Harness checkout declares version 0.3.0 and also documents explicitly unreleased source capabilities. Its README combines installation, architecture, validation and lifecycle information. Detailed SDD collaboration guidance already lives in `sdd/README.md`; specialized validation/evaluation instructions live in `docs/guides/`. The approved Proposal captures the observed organization README, CONTRIBUTING, AGENTS and profile contents and Git blob IDs. No local CONTRIBUTING file exists in the Harness checkout.

Policy resolution uses this checkout's `standards/index.yaml`, including its applicable core rules. The architecture overview and accepted ADRs 0010, 0011 and 0013 establish language, package ownership and lifecycle boundaries. Organization edits follow that repository's own reviewed `AGENTS.md`; those instructions are not inherited automatically by other repositories. This design applies existing policy and requires no new ADR or policy change.

## Proposed design

### Entry flow and page inventory

The primary route is organization contribution entry or Harness README → quickstart → one first SDD planning result → the guide appropriate to the next job. Every new page has a purpose, intended reader, applicability/version notes where needed, useful content and links to its next destinations.

Each of the following eleven English files has matching `.pt.md` and `.es.md` siblings. The inventory is 33 Harness user-facing files, including the existing English README; this is not a requirement to translate existing technical references.

| Canonical path | Content owned here | Reused detail |
|---|---|---|
| `README.md` | Purpose, audience, accountable team, current state, concise capability map, navigation and validation entry | Quickstart, product overview, guides and architecture |
| `docs/user-docs/quickstart.md` | Prerequisite checklist, preparation route, one planning request, observable result and next action | Workspace preparation and SDD guide |
| `docs/product/overview.md` | Pitch, value, Issue #22 problem/JTBD/persona, ownership, origin, current solution/boundaries, proportional product context and open questions | Base product topic model, source issue and technical references |
| `docs/user-docs/guides/workspace-setup.md` | Repository access, selected Harness/provider availability, local project/repository preparation, verification and recovery | Verified current Codex usage; existing exact-version installation sources |
| `docs/user-docs/guides/sdd-with-codex.md` | Choosing a planning, implementation, validation or resumption request; how to recognize outputs and the next allowed action | `sdd/README.md`, canonical process/workflows and metadata |
| `docs/user-docs/guides/github-delivery.md` | Real issue linkage, work branch, draft versus completed review, archive/preflight, PR evidence, final checks and merge observation | Git Standard and SDD delivery sections |
| `docs/user-docs/guides/project-bootstrap.md` | When to bootstrap, required identity/product inputs, discovery gaps, expected skeleton and review/readiness output | Bootstrap Skill, composition guide and base product template |
| `docs/user-docs/guides/project-maintenance.md` | Existing-project migration inputs, exact target release, local deviations, reviewable diff and rollback | Maintenance Skill and template migration guidance |
| `docs/user-docs/guides/project-audit.md` | Audit inputs, profile/lock resolution, evidenced findings and read-only/remediation distinction | Audit Skill and relevant validator documentation |
| `docs/user-docs/guides/architecture-review.md` | Review inputs, boundary/risk questions, expected findings and ADR decisions | Architecture-review Skill and decision conventions |
| `docs/user-docs/guides/validation-and-evaluations.md` | Choosing package validation, consumer test execution or supervised evaluation; reading pass/fail/unverified and evidence limits | Existing `docs/guides/project-validation.md` and `docs/guides/skill-evaluations.md` |

Use a compact guide pattern: when to use it; prerequisites/inputs; one representative request or action; expected outputs and stopping conditions; recovery/limitations; next links. A guide is not a complete copy of its Skill or process. Bootstrap and maintenance must remain distinct. Audit and architecture review do not imply permission to remediate. Source-only validation features are labeled with their availability limits.

The README retains a short package/consumer distinction and a pointer to architecture rather than becoming another complete architecture document. Keep the working validation entry point discoverable. Detailed workspace steps move to their guide. Do not create a local Harness CONTRIBUTING file solely to mirror the organization entry.

### Quickstart behavior

Use a small synthetic planning example in an already prepared repository, not a production change or an instruction to create a remote repository. The example names a simple desired behavior, a stable illustrative change ID and the intention to plan only. Label it as an example. One invocation should produce Proposal and Requirements and stop for Gate 1 review; the guide explains how to recognize those artifacts and links to later lifecycle detail. It does not ask the reader to manufacture approval metadata.

Prerequisites distinguish repository access, an available exact Harness provider, a prepared project and capability availability. Missing setup leads to the relevant workspace section. Missing access leads to the target repository/workspace owner, without claiming an automatic grant. Existing organization claims about the ChatGPT/Codex UI and automatic Plugin installation must be verified or qualified before reuse. Do not make those observations prerequisites for every external contributor.

### Product context and evidence

Use the base product overview as a topic checklist, not a copied unfilled template. Retain its substantive product topics in concise sections: pitch/value, problem and JTBD, solution/current boundaries, origin, customers/users, internal value and market applicability, timing, alternatives/differentiation, innovation, scalability, social/environmental considerations and open questions.

Issue #22 supplies the known problem, JTBD and persona. The repository supplies current capabilities. Avoid invented adoption figures, market estimates or impact claims. Internal market/revenue sections can explain non-applicability and how internal value would be evaluated. Where a topic lacks evidence, state the specific unknown and next validation action; this is useful content, not an empty placeholder.

Link the issue in the overview. Link the Codex recording from workspace/SDD context and the GitHub recording from delivery context, preserving the exact URLs captured in Proposal. Label them access-restricted supplemental training. They are not required to complete the first-use route, and their unreviewed contents cannot establish instructions.

### Translations and navigation

English remains canonical. Use language links near the start of each page; the localized page links to the same-language version of other in-scope user pages. Translate prose and human example requests, preserving path names, identifiers, command semantics, approval boundaries and operational meaning.

Link to existing English-only Standards, Skills, SDD and specialized guides with an explicit English-language label in PT/ES pages. Do not translate those policy/process files as part of this change. Maintain each language set together in the same logical delivery; do not add parallel translated examples that behave differently.

Relative links stay within a repository. Cross-repository links are full HTTPS GitHub URLs with an explicit ref. Use actual verified heading anchors, including localized headings, rather than assume the English anchor works in every locale. In-scope pages must not depend on `specs/changes/harness-user-documentation/` or its archive path.

### Organization consolidation

The organization README remains a repository guide. CONTRIBUTING becomes a short, welcoming contribution entry point. The public profile keeps its mission, vision and short participation invitation.

| Organization artifact | Change |
|---|---|
| `README.md`, `README.pt.md`, `README.es.md` | Keep purpose, GitHub default-file behavior, file map, issue entry and local validation. Replace the duplicated lifecycle sequence with a concise pointer to Harness guidance; update descriptions of CONTRIBUTING. |
| `CONTRIBUTING.md`, `CONTRIBUTING.pt.md`, `CONTRIBUTING.es.md` | Maintain aligned entry pages: ways to participate, target-repository precedence, minimal public first step, access note and descriptive links to detailed Harness setup/SDD/delivery/language guidance. Create locale siblings if absent after refreshing the target checkout. |
| `AGENTS.md` | Correct descriptions only if they still claim CONTRIBUTING contains the removed detailed material. Keep local editing rules and validation responsibilities; do not weaken its SDD requirement. |
| `profile/README.md` | Preserve content and its CONTRIBUTING destination. Adjust only a now-inaccurate description if necessary. |
| Issue templates and unrelated files | No edits. Verify their contents remain unchanged in the candidate diff. |

Reusable Codex preparation detail moves to `workspace-setup.md`. SDD prose is reconciled with `sdd/README.md`, not copied into a second manual. Generic validation/PR detail moves to user guides, which link to actual canonical procedures. Organization-specific validation remains in the organization repository. Language guidance links to the canonical Standard instead of reproducing an incomplete list.

A reader without private Harness access can still choose a repository, find its issue forms, read its own setup/contribution guidance and learn what information to supply. Restricted links are clearly labeled. No visibility change or copy of private content into public documentation is implied.

## Boundaries and contracts

This is a documentation change across two repositories. It changes neither the Plugin package layout nor consumer paths, version pins, schemas, validator semantics, Skills or SDD gates. The Harness remains the source of detailed internal practice; the organization repository owns public identity and default contribution entry points.

Living product information goes to `docs/product/overview.md`, as explicitly confirmed by the user. It does not relocate the consumer template's `specs/product/overview.md`. Guide paths use the approved `docs/user-docs/` convention without editing the default Documentation Standard.

Full manuals, a generated documentation site, new link-validation infrastructure and a language-policy exception were considered unnecessary. No new unit tests that merely assert prose wording will be added.

## Data, security and permissions

Use only repository documentation, the supplied issue and necessary source metadata. Do not copy video payloads, credentials or unrelated Slack messages. Evidence uses synthetic project content and scrubbed runtime observations. A temporary directory is not a security sandbox.

The two repositories keep their existing access controls. Refresh organization instructions and source revisions before editing. Any real workspace administration, remote branch publication, PR creation or merge needs its applicable authorization; this Design approval is not that authorization.

## Operations and observability

There is no service, deployment, database or production telemetry change. Documentation verification records document/provider revisions, actual steps, observed results, exceptions and review findings. Local checks, publication, final CI, merge and installed availability remain separate facts.

The Harness owns current user content and translation upkeep. Organization maintainers own the contribution entry points and reviewed destination updates. Changes to a linked guide's meaning or path require checking its three language versions and organization entry links in the same coordinated maintenance work.

## Migration, rollout and rollback

### Stable targets without a merge dependency cycle

Prepare both repositories' edits before requesting any publication permission. Organization-to-Harness links will use one full immutable Harness Git commit containing the reviewed documentation, such as the URL shape `https://github.com/versat-labs/versat-ai-harness/blob/<full-content-commit>/docs/user-docs/quickstart.md`. The actual commit is selected during implementation; this illustrative placeholder must never ship.

The content commit precedes the final evidence/archive commit, so no document must contain its own final commit SHA. Publishing that source revision, when authorized, makes the target files inspectable before either PR merges. Compare the published bytes with the approved candidate; then finalize the organization URLs and verify intended-reader access. A source revision is not a semantic release or proof of installed availability.

This pin makes the initial cross-repository link check reproducible and avoids claiming that future `main` paths already exist. It also means organization links deliberately retain that reviewed documentation revision until a subsequent reviewed update. Relative navigation inside that revision stays coherent. Do not silently redirect to an unreleased or moving version.

### Delivery sequence

1. Prepare the Harness documentation, locale sets and candidate organization edits in their respective working copies. Preserve the organization baseline and review its diff.
2. Verify local content, navigation, translations and usage. After scoped authorization, publish the reviewed Harness content commit. Until it is available and verified, retain current organization entry guidance and report the source-publication prerequisite as pending.
3. Bind the organization candidate to that exact commit, check all destination files/anchors and intended-reader access, and complete the local checks and evidence for both candidate trees. The same reviewed plan governs this consolidation; do not create a duplicate policy process or copy the full dossier into the organization repository.
4. Prepare the Harness dossier archive before completed-work submission under the existing SDD contract. The immutable target commit is earlier than this final archival commit; rerun affected checks if documentation changed. The organization candidate must be reviewable and linked to Issue #22, with its applicable local checks complete.
5. When PR publication is authorized, create the two reviewed delivery PRs, link Issue #22 and cross-link the PRs. Apply each repository's actual review and required-check controls. Merge Harness first, then activate the organization routing change through its own reviewed merge.
6. Confirm both merges and active destinations from actual GitHub evidence. This is a separately observed delivery follow-up, not a task requiring a PR's own merge before its pre-merge checks can finish. A prepared organization patch or passing local check must never be reported as an activated organization change.

CHECK-004 cannot fully pass while the source commit is unpublished or intended access is unverified. Keeping remote publication pending is an honest dependency, not permission to omit the check. No readiness claim is made from this Design. The later Tasks will expose the preparation/publication dependency and the separate final delivery observations.

If a target is unavailable or validation fails, do not activate the organization patch; retain the current contribution route. After activation, rollback restores the previous organization entry text or a verified prior target first, then rolls back affected Harness prose if needed. Preserve source provenance and evidence. No runtime rollback or consumer pin migration is involved.

## Alternatives considered

| Alternative | Assessment |
|---|---|
| Copy organization CONTRIBUTING into the Harness and leave both manuals | Rejected: creates competing maintained instructions. |
| Replace all organization content with private links | Rejected: loses organization purpose and a usable public contribution route. |
| Keep reusable detailed setup only in the organization repository | Rejected: conflicts with the approved consolidation and fragments the Harness user journey. |
| Relocate or translate all existing SDD and specialized guides | Rejected: unnecessary scope and broken-reference risk; reuse them as English canonical detail. |
| Link organization pages directly to future `main` destinations | Simpler ongoing navigation, but unavailable destinations cannot be verified before their delivery. Choose a reviewed immutable content revision for this coordinated change. |
| Generate a site or add a dedicated documentation validator | Rejected: plain Markdown and proportionate content/link/usage checks satisfy this scope. |

## Validation plan

All 27 local scenarios and all 19 retained regression obligations have explicit metadata mappings above. No scenario is marked not applicable. All five checks are required. The proposed reviews supplement the unchanged maintained test suites; they do not reinterpret a structural pass as user acceptance.

| Check | Expected evidence and scope |
|---|---|
| CHECK-001 | Section-level content review: README completeness, correct behavior/boundaries, all guide jobs, product evidence, useful empty-scaffold treatment, no duplicate manuals, recorded source limits. |
| CHECK-002 | File/locale/link matrix and rendered review: all language siblings, semantic parity, correct local/cross-repository destinations and no dependence on dossier location. |
| CHECK-003 | Actual first-use and affected-example walkthroughs: observable outputs, Gate 1 stop, missing-prerequisite recovery, retained attempts and unavailable environments. |
| CHECK-004 | Original/candidate organization comparison, public fallback, pinned-target verification, source identities and separate preparation/publication/merge facts. |
| CHECK-005 | Existing full package validation, validator and execution suites, whitespace checks and phase-appropriate delivery preflight. |

CHECK-001 explicitly reviews the inherited boundary that empty scaffolds do not receive fictional usage guides; this change documents existing Harness behavior and does not change bootstrap generation. CHECK-002 reviews that focused guides add distinct value rather than enforce a guide-per-feature policy on consumer projects. CHECK-003 and CHECK-004 record unavailable command/UI or external checks as unverified and may reuse adequate observed evidence rather than invent a separate report for every scenario.

### Evidence inputs and freshness

The v3 input scopes cover changed user documents, canonical references, Skills, templates, validators/tests, configuration and historical requirements. Before validating an organization candidate, export its relevant original and candidate Markdown files and a manifest under `docs/validation/harness-user-documentation/inputs/organization/`. Include repository identity, observed base/head when present, per-file content hashes and the issue-form/profile unchanged comparison. These are immutable review snapshots, not another maintained contribution manual.

Capture the exact published Harness target files and their ref/provenance under `docs/validation/harness-user-documentation/inputs/published-targets/` before the associated check. Such snapshots bind the reviewed external bytes to the local input digest; they do not prove that later remote content or access remains unchanged. Refresh and revalidate when the candidate, source ref or external access changes. Do not store credentials.

Store actual outputs in `docs/validation/harness-user-documentation/runs/<attempt>/`, outside the reviewed input subtree and explicitly excluded from inputs. Use the existing `--input-digest` helper before and after real execution/review once Tasks is approved. Organization snapshots must match the actual implementation checkout; if they differ, rebuild the snapshot before capturing new input digests and repeat affected checks. Never refresh only the hash of stale evidence.

The five local check results and per-scenario assessments will be recorded in Tasks after implementation, together with findings and external limitations. The organization repository itself remains free of invented application tooling; run its actual Markdown/diff requirements. Its templates are unchanged, so YAML form modification tests are unnecessary.

Existing `./scripts/validate/run.sh` and `.github/workflows/validate.yml` remain unchanged. Final required CI/review and merge facts are recorded only when observed. Remote checks do not silently become local passes.

## Planning review

Design R1 was presented for Gate 2 review and the developer replied "aprovado". The structured record binds that response to the reviewed Design digest. Proposal/Requirements R2 remains approved and bound above. This approval unlocks Tasks only. Publication, runtime access and video contents remain the identified later verification prerequisites/limits. No implementation results or completed tasks are claimed.

