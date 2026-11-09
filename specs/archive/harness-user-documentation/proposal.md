---
sdd_version: 3
change: harness-user-documentation
status: accepted
owner: elviszoz
summary: Consolidate detailed Harness guidance in one multilingual documentation set and make organization contribution entry points link to it.
risk: low
impact:
  state: assessed
  summary: Extend Harness user documentation and consolidate overlapping organization guidance while preserving first-use, SDD, language, public contribution access and exact-version contracts; no executable behavior or consumer migration changes.
  items:
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-001
        scenarios: [1, 2, 3]
        requirements_digest: e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc
      current_contract:
        path: standards/core/documentation.md
        locator: "## First-use guides"
        digest: f81e9a85570e4cd5699e113395e80bc92fba13401e57e8b7186bc6cd6bc785e0
      effect: extend
      targets: [REQ-002, REQ-003]
      reason: Apply first-use guidance to the Harness itself at the explicitly requested user-docs path, reuse maintained detail and avoid empty or fictional guides.
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-002
        scenarios: [1, 2, 3, 4]
        requirements_digest: e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc
      current_contract:
        path: standards/core/documentation.md
        locator: "## First-use guides"
        digest: f81e9a85570e4cd5699e113395e80bc92fba13401e57e8b7186bc6cd6bc785e0
      effect: extend
      targets: [REQ-001, REQ-002, REQ-003]
      reason: Add discoverable living documentation with focused guides for distinct workflows and stable links independent of dossier archival.
    - source:
        change: consolidate-sdd-workflow
        requirement: REQ-001
        scenarios: [1, 2]
        requirements_digest: 04a4f00939eeabdabe21e739a419f80f29ca80aa7801c6b6c03d43ace415694a
      current_contract:
        path: sdd/README.md
        locator: "## Phases and deliverables"
        digest: debce894a5e1efe3b0c236705de2e7faf19204b449776811c969167eb6631ac4
      effect: preserve
      targets: [REQ-002, REQ-003]
      reason: New onboarding examples refer to the single public SDD entry point and maintained developer guide rather than define another lifecycle.
    - source:
        change: consolidate-sdd-workflow
        requirement: REQ-002
        scenarios: [1, 2]
        requirements_digest: 04a4f00939eeabdabe21e739a419f80f29ca80aa7801c6b6c03d43ace415694a
      current_contract:
        path: sdd/README.md
        locator: "## Approvals, changes and resumption"
        digest: debce894a5e1efe3b0c236705de2e7faf19204b449776811c969167eb6631ac4
      effect: preserve
      targets: [REQ-002, REQ-003, REQ-005]
      reason: Preserve actual review of each planning stage and explicit implementation authority in examples and translations.
    - source:
        change: consolidate-sdd-workflow
        requirement: REQ-003
        scenarios: [1, 2]
        requirements_digest: 04a4f00939eeabdabe21e739a419f80f29ca80aa7801c6b6c03d43ace415694a
      current_contract:
        path: sdd/README.md
        locator: "## 4. Prepare the archive and PR"
        digest: debce894a5e1efe3b0c236705de2e7faf19204b449776811c969167eb6631ac4
      effect: preserve
      targets: [REQ-003, REQ-005]
      reason: GitHub guidance must retain pre-submission archive checks and separate local readiness from remote review, CI and observed merge.
    - current_contract:
        path: standards/core/language.md
        locator: "## Translation requirements"
        digest: a287cabaf0609331541afd18cc1b3f3d1aead42642446263fe44bc3bc9100f3f
      effect: preserve
      targets: [REQ-005]
      reason: Apply the current translation contract to the new user-facing documentation; the historical language migration did not specify this documentation set.
    - source:
        change: quickstart-scenario-coverage
        requirement: REQ-004
        scenarios: [1, 2, 3, 4]
        requirements_digest: e40660bbb1ff3b10633c8ca617cd0a5ff4addc2d70eb93bfa7d1fd09a79dd0cc
      current_contract:
        path: standards/core/documentation.md
        locator: "## First-use guides"
        digest: f81e9a85570e4cd5699e113395e80bc92fba13401e57e8b7186bc6cd6bc785e0
      effect: preserve
      targets: [REQ-006]
      reason: Verify affected usage against observed results; unavailable video or UI evidence cannot be replaced by structural validation.
    - current_contract:
        change: harness-user-documentation
        artifact: proposal
        locator: "## Organization documentation baseline"
      effect: extend
      targets: [REQ-001, REQ-002, REQ-003, REQ-005, REQ-007]
      reason: Replace overlapping organization setup and process explanations with links to maintained Harness documentation while preserving organization-specific guidance and an accessible public contribution route.
review:
  revision: 2
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Developer reply in this chat after Proposal and Requirements R2 were presented for Gate 1 approval.
    quote: Ok aprovado
    revision: 2
    digest: 1ca3de32bdea8b921030786aea349b2dc5a50a3a265aa75ee25a39e1b3308f24
---

# Proposal

## Context and problem

[Issue #22](https://github.com/versat-labs/versat-ai-harness/issues/22) supplies the product need:

- **Problem:** the team does not know how to use the new Versat AI Harness.
- **Job to be done:** when a Versat SDD developer plans or implements a user story, they want to read the repository documentation so they can understand Versat's new SDD development process.
- **Persona:** the Versat team, primarily developers planning, implementing and reviewing SDD changes.

The repository already describes architecture, policy, installation and the SDD lifecycle. It lacks a short user onboarding route, the requested product overview and aligned Portuguese/Spanish user documentation. Organization-level `versat-labs/.github/CONTRIBUTING.md` already explains local setup, SDD and contribution expectations; the organization README also repeats lifecycle guidance. The change must reconcile these sources rather than add another independently maintained explanation. It documents existing capabilities and does not introduce a new development process.

## Expected outcome

A team member can start at the Harness README or organization contribution entry point, find the appropriate English, Portuguese or Spanish documentation, identify the product and its prerequisites, complete one representative SDD planning action, recognize the expected artifacts and review boundary, and follow focused guidance for subsequent work. Detailed shared instructions live in the Harness; organization documents route readers to them and retain organization-specific context. Maintainers have a clear content owner for each topic instead of competing copies of the process.

## Scope

- Review and revise `README.md` as the entry point: purpose, audience, accountable team, current lifecycle/version boundaries, quickstart, feature navigation, product context, contribution reference and validation entry point.
- Create `docs/user-docs/quickstart.md` for one first successful SDD planning interaction, with prerequisites, preparation, expected artifacts and recovery from missing access or setup.
- Add substantive feature guides under `docs/user-docs/guides/`. Cover workspace preparation and exact-version use; SDD use in Codex; GitHub issue/branch/PR delivery; project bootstrap; project maintenance; project audit; architecture review; validation and Skill evaluations. Design will choose final filenames and group topics where that avoids duplicated instructions.
- Create `docs/product/overview.md`, covering the problem, job to be done, persona, value, capabilities, boundaries and product context. Reuse the base product overview's topic model where applicable, with explicit unknowns or reasoned non-applicability for an internal product.
- Provide corresponding `.pt.md` and `.es.md` siblings for the root README and every new user guide and product overview, with English canonical and navigable locale links.
- Link Issue #22 and both team training recordings with accurate provenance and verification status.
- Preserve `sdd/README.md` as the maintained SDD developer reference and the existing specialized guides as maintained technical detail. Add cross-links where useful; do not reproduce their complete instructions in the quickstart.
- Reconcile `versat-labs/.github/README.md`, its Portuguese/Spanish siblings and `CONTRIBUTING.md` with the Harness documentation. Move reusable detailed setup guidance to the Harness, reconcile repeated process explanations against canonical SDD, and replace overlapping organization sections with descriptive links after the targets are available.
- Keep organization identity, repository purpose, GitHub default-file behavior, participation routes and `.github`-specific validation in the organization repository. Provide aligned English/Portuguese/Spanish versions of changed contribution entry guidance; preserve existing profile and issue-form responsibilities. Update file descriptions in `.github/AGENTS.md` only where consolidation makes them inaccurate.

The user confirmed `docs/product/overview.md` in this planning conversation, resolving the difference between the initial `/product/overview.md` request and the issue's directory tree. The requested `docs/user-docs/` location is specific to this repository and does not change default consumer documentation paths.

## Out of scope

- Changes to Standards, the SDD gates, Skills, validator behavior, schemas, runtime capabilities or generated consumer layouts.
- Publishing a release, updating installed Plugins or consumer pins, workspace administration, or changing GitHub organization controls.
- Creating a second detailed contribution manual, migrating historical dossiers, relocating existing specialized guides, or translating the full Standards/SDD/architecture corpus. The organization contribution entry point remains a concise router.
- Changing organization identity, repository visibility, GitHub default-file semantics, issue forms or their metadata. A wholesale rewrite or translation of the organization profile is outside this consolidation.
- Uploading training videos, copying confidential meeting material, building a documentation site, or treating a linked recording as normative policy.
- Publishing a PR or modifying Issue #22 during this planning step. The dossier supplies the requested issue linkage.

## Work tracking

- Issue: [versat-labs/versat-ai-harness#22](https://github.com/versat-labs/versat-ai-harness/issues/22).
- Stable change ID: `harness-user-documentation`.
- Local branch: `codex/22-user-documentation`.
- No Shortcut Story is associated with the supplied context; no Story ID or type is inferred.
- Repository owner for this proposal: `elviszoz`, matching the issue's assignee. The documentation should identify the Versat team and use verified repository ownership contacts.
- Internal PR communication follows the resolved Git/Language Standards when publication is separately requested.
- Implementation has coordinated changes in the Harness and `versat-labs/.github`, each reviewed under its own repository instructions. Link both delivery PRs to Issue #22 and to each other when publication is authorized; do not mark the organization cleanup complete merely because the Harness part is ready.

## Sources and verification status

Reviewed on 2026-11-08:

| Source | What is established | Remaining limit |
|---|---|---|
| [Issue #22](https://github.com/versat-labs/versat-ai-harness/issues/22) | Problem, job to be done, persona, directory proposal and translations | The issue is intent, not evidence of implemented documentation. |
| [Organization README](https://github.com/versat-labs/.github/blob/main/README.md), its `.pt.md`/`.es.md` siblings and [CONTRIBUTING](https://github.com/versat-labs/.github/blob/main/CONTRIBUTING.md) | Existing organizational entry points, setup instructions, repeated SDD guidance and public-reader constraints | Current prose is source material, not proof of current Codex UI or workspace installation state; reconcile against current evidence and canonical Harness contracts. |
| [Organization AGENTS](https://github.com/versat-labs/.github/blob/main/AGENTS.md) and [profile README](https://github.com/versat-labs/.github/blob/main/profile/README.md) | Repository-local editing/validation rules and public profile responsibilities | These instructions are not automatically inherited by other repositories; their scope remains the organization repository. |
| [Codex recording](https://versat.slack.com/files/U04PSSJ2W/F0CF8AH2SVC/pantalla_compartida_-_2026-11-05_16_09_27.mp4), linked in [the issue comment](https://github.com/versat-labs/versat-ai-harness/issues/22#issuecomment-6668698804) | The team supplied it as Codex training context | Slack file reading returned `file_too_large`; the recording has not been watched or transcribed. |
| [GitHub training thread](https://versat.slack.com/archives/C0B7G255DPY/p1793910356829109), linked in [the issue comment](https://github.com/versat-labs/versat-ai-harness/issues/22#issuecomment-6668710866) | The parent message describes work with projects in the Versat Labs organization created for SDD repositories | The attached MP4 is 167.6 MB, above the connector's 10 MB limit; its contents remain unreviewed. |

The GitHub thread also records that both recordings cut off at the end and the author did not consider the omitted closing remarks relevant. This is source context, not evidence that their instructions match today's product. Accessible recordings or reviewed transcripts can inform examples during implementation; until then, link them as access-restricted supplemental material and derive instructions from verified repository behavior. Do not infer unseen steps or permissions.

## Impact and risks

The applicable baseline is this Harness source checkout (`VERSION` 0.3.0, initial HEAD `5fa618aed07703c8181f4f753ca6aac393551089`), including its explicitly unreleased source capabilities. This is the provider repository, not a consumer with a root `.versat/project.yaml` or Standards lockfile. Resolve its current policies through `standards/index.yaml`; do not import a different installed release or assign a consumer profile without evidence.

Reviewed related history includes `quickstart-scenario-coverage`, `consolidate-sdd-workflow`, `bootstrap-product-context` and `align-language-standard`. The first two supply qualified scenario origins above. The product template is a content reference, not a request to change its consumer contract. The current language policy is the effective translation contract. No matching active documentation dossier was present.

`tests/validators/test_sdd.py`, `tests/validators/test_sdd_v3.py` and the `tests/execution/` suites cover existing contract and execution behavior. They do not establish that a user can follow the proposed documentation or that translations are aligned. Design must define proportionate link, translation, content and usage checks, reusing existing functional evidence where adequate. No new executable behavior requires new unit tests merely for this documentation change.

Principal risks are duplicated SDD guidance, translated instructions drifting, broken cross-repository links, public readers losing usable contribution guidance, confusion between released and unreleased behavior, and unverified video/UI instructions. Preserve the current policy/capability/process/enforcement boundaries described in the architecture overview and ADRs 0010, 0011 and 0013. Consolidating explanatory documentation applies these boundaries without moving policy ownership; no architectural boundary change or new ADR is currently proposed.

The organization repository has its own `AGENTS.md` and no application build or automated test suite, as documented in its README. Its future Markdown edits require diff, link, rendering where relevant and translation checks, not invented application tests. Re-read its instructions and current file versions before implementation to account for concurrent changes.

## Current contract baseline

| Artifact | Current observation | Intended treatment |
|---|---|---|
| `README.md` | Explains purpose, package map, 0.3.0 state, validation, SDD and workspace installation; separately labels some execution behavior unreleased. No explicit ownership section, requested quickstart/product links or locale copies. | Preserve useful facts, improve entry navigation and ownership, and verify availability statements. |
| `sdd/README.md` | Detailed contributor/developer workflow, examples, approval gates, validation, archive/PR handling and resumption. | Reference as the existing SDD collaboration guide. |
| Local `CONTRIBUTING.md` / `CONTRIBUTYNG.md` | Neither file exists in the Harness checkout, but `versat-labs/.github/CONTRIBUTING.md` is an existing organization contribution source. | Link to the real organization entry point where relevant; consolidate its detailed Harness instructions rather than create a duplicate local manual. |
| `docs/guides/project-validation.md`, `docs/guides/skill-evaluations.md` | Maintained specialized guides already linked by README and SDD guide. | Preserve paths and detailed content; new user guides explain when to follow them. |
| `docs/user-docs/`, `docs/product/overview.md` | Requested documentation is absent. | Add living documentation after the planning gates. |
| `project-templates/base/specs/product/overview.md` | Consumer product-discovery template with evidence/unknowns and internal-product applicability. | Reuse its topic model without copying the consumer path into this provider or changing template composition. |

## Organization documentation baseline

Read from the default branch of `versat-labs/.github` on 2026-11-08. The following Git blob IDs identify the observed file contents, not a claim about a shared commit or deployed behavior:

| File | Observed blob SHA | Existing content and disposition |
|---|---|---|
| `README.md` | `c6416962c42d31995819cafbcfee6518884554a0` | Retain repository purpose, file/default behavior, issue entry and local maintenance/validation; replace repeated SDD lifecycle detail with Harness links and adjust the contribution-file description. |
| `README.pt.md` | `8ae6199fd7784b19c28fa48cf596c11daf2bb418` | Aligned Portuguese organization README; update alongside English. |
| `README.es.md` | `53ef331484f089f269f05d5db9e1126ec73cfd14` | Aligned Spanish organization README; update alongside English. |
| `CONTRIBUTING.md` | `8d288a65854078cd770cb5e4168ee0dd1a60ccf5` | Contains participation options, repository precedence, private Harness access, automatic workspace installation claim, Codex project/clone setup, SDD lifecycle, validation/PR and language summaries. Consolidate reusable detail in Harness destinations; retain a short organization entry and access-aware links. |
| `AGENTS.md` | `6ee7b042501dcd14ec20087a4727bec5d1169817` | Keep repository-local scope, working rules and validation; correct only descriptions affected by the contribution-guide reduction. |
| `profile/README.md` | `6a412d23f8949d95edddab6b964829452d05b872` | Public mission, vision, areas of work and a short contribution invitation already linking to CONTRIBUTING. Preserve this organization-owned summary; adjust a link description only if the new entry point makes it inaccurate. |

The proposed content ownership is:

| Topic | Maintained destination | Organization treatment |
|---|---|---|
| Codex project preparation, repository cloning and Harness availability | Harness workspace-preparation guide, referenced by its quickstart | Replace detailed setup steps with a descriptive link. Verify current UI and installed-version claims before reusing them. |
| SDD lifecycle, human approvals and resumption | Existing Harness `sdd/README.md` and `sdd/process.md`; user guides supply task context | Replace duplicate lifecycle lists with links; preserve only enough context to choose the contribution route. |
| Validation, issue-to-PR traceability and delivery | Harness GitHub delivery/user validation guides referencing canonical SDD, Git Standard and specialized guides | Link to detail and retain the instruction to follow each target repository's own checks. |
| Language conventions | Harness `standards/core/language.md`, explained through user documentation | Link to the policy rather than maintain an incomplete parallel language list. |
| Organization mission, default community resources, issue forms and `.github` maintenance | Organization profile, README and local AGENTS | Retain locally; these are not Harness usage instructions. |

The organization CONTRIBUTING describes the Harness as private. A public reader without that access must still understand how to choose a target repository, use its available issue forms and follow its own contribution/setup/check requirements. Retain that small public entry contract and label restricted links; do not publish private material or change visibility as a side effect. Detailed internal workflows should exist only in the Harness.

Consolidation must also reconcile semantic differences: the current organization summary says implementation follows plan approval but omits the explicit execution request and pre-submission documentary archive details present in canonical SDD. Do not import the abbreviated summary as a replacement process or preserve stale UI/install claims merely because they already exist.

Prepare coordinated reviewable changes. Harness destinations must be available and verified for intended readers before the organization replacement links are activated; prepare both patches in advance, deliver the Harness targets first, then recheck and deliver the organization routing change. Keep existing organization detail until that dependency is satisfied. The later Tasks must separate pre-merge verification of each deliverable from the external rollout dependency rather than require a PR's own merge as one of its pre-merge completion checks. Link completion remains unverified until observed. Documentation links do not update consumer version pins.

## Proposal acceptance criterion

Proposal and Requirements are ready for Gate 1 review when their scope, language/file conventions, source limitations and acceptance scenarios are coherent and the planning validator passes. Product acceptance requires the later approved documentation work and observed checks; planning success does not claim documentation delivery.

## Planning review

Revision 1 was presented without approval and is superseded. Revision 2 incorporates the user's request to include existing organization README/CONTRIBUTING content and consolidate overlapping instructions into the Harness. After R2 was presented, the developer replied "Ok aprovado", approving Proposal/Requirements R2 and unlocking Design. The structured record binds that response to the canonical digest of the reviewed files. No material scope decision remains unresolved. Video contents and future cross-repository link availability are explicit verification limits, not blockers to planning. Design is the next review stage; Tasks and implementation remain unauthorized.
