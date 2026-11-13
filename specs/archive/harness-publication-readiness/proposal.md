---
sdd_version: 3
change: harness-publication-readiness
status: proposed
owner: '@elviszoz'
summary: Prepare the existing Harness repository and root Codex Plugin for reviewed public Apache-2.0 distribution,
  with truthful readiness and separately authorized operations.
risk: high
impact:
  state: assessed
  summary: 'Inspect current source, maintained package/tests and four delivered origins: classify all 78 historical
    scenarios exactly once (71 preserve/extend, 7 intentional supersessions), plus one retained current validation-entry
    obligation. This is prospective impact for human review, not current implementation acceptance.'
  items:
  - source:
      change: portfolio-licensing-policy
      requirement: REQ-001
      scenarios:
      - 1
      - 3
      requirements_digest: 62a65c23002c671422bffc464765f3ed5aa537a2a26d8950cbd343000ba4dee8
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-011
    - REQ-012
    reason: Retain independent product decisions and separation of planning, policy, adoption and operations.
  - source:
      change: portfolio-licensing-policy
      requirement: REQ-001
      scenarios:
      - 2
      requirements_digest: 62a65c23002c671422bffc464765f3ed5aa537a2a26d8950cbd343000ba4dee8
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: supersede
    targets:
    - REQ-001
    - REQ-011
    reason: Replace only private/proprietary Harness scope with the selected public Apache candidate; preserve private
      proprietary Discover/CRM and independent destination-project terms.
  - source:
      change: portfolio-licensing-policy
      requirement: REQ-002
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 62a65c23002c671422bffc464765f3ed5aa537a2a26d8950cbd343000ba4dee8
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-002
    - REQ-003
    - REQ-009
    reason: Reuse bounded rights/dependency review and dispositions; extend review to the complete existing repository
      and all potentially exposed remote surfaces.
  - source:
      change: portfolio-licensing-policy
      requirement: REQ-003
      scenarios:
      - 1
      - 3
      requirements_digest: 62a65c23002c671422bffc464765f3ed5aa537a2a26d8950cbd343000ba4dee8
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: supersede
    targets:
    - REQ-001
    - REQ-008
    - REQ-010
    reason: The proprietary tool model and restrictions are replaced prospectively by reviewed Apache scope; concrete
      permissions, third-party notices, target-project independence and historical approval evidence remain required.
  - source:
      change: portfolio-licensing-policy
      requirement: REQ-003
      scenarios:
      - 2
      requirements_digest: 62a65c23002c671422bffc464765f3ed5aa537a2a26d8950cbd343000ba4dee8
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-001
    - REQ-002
    reason: Keep exact-text review and actual authority separate from SDD approval and technical ownership.
  - source:
      change: portfolio-licensing-policy
      requirement: REQ-004
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 62a65c23002c671422bffc464765f3ed5aa537a2a26d8950cbd343000ba4dee8
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-002
    - REQ-009
    - REQ-011
    reason: Reuse established contacts and require actual capacity/evidence; other product adoption remains independent.
  - source:
      change: portfolio-licensing-policy
      requirement: REQ-005
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 62a65c23002c671422bffc464765f3ed5aa537a2a26d8950cbd343000ba4dee8
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-004
    - REQ-011
    reason: Retain index-resolved canonical resources, exact references and explicit consumer migration.
  - source:
      change: portfolio-licensing-policy
      requirement: REQ-006
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 62a65c23002c671422bffc464765f3ed5aa537a2a26d8950cbd343000ba4dee8
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-009
    - REQ-010
    - REQ-012
    reason: Retain authorization boundaries, truthful evidence and semantic acceptance; historical stage events
      are not reenacted or transferred as new approvals.
  - source:
      change: contribution-security-guidance
      requirement: REQ-001
      scenarios:
      - 1
      - 2
      - 3
      - 4
      requirements_digest: 65986d898e8209f80081a5e8522e14d5f54ec040ad2b56391dcb892972b672f3
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-006
    - REQ-008
    - REQ-011
    reason: Reuse delivered entry points and canonical guides while extending them for external Harness contributors.
  - source:
      change: contribution-security-guidance
      requirement: REQ-002
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 65986d898e8209f80081a5e8522e14d5f54ec040ad2b56391dcb892972b672f3
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-005
    - REQ-008
    - REQ-011
    reason: Retain accessible public fallback and repository boundaries; the Harness itself gains a separately verified
      external route without private dependencies.
  - source:
      change: contribution-security-guidance
      requirement: REQ-003
      scenarios:
      - 1
      - 3
      requirements_digest: 65986d898e8209f80081a5e8522e14d5f54ec040ad2b56391dcb892972b672f3
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-001
    - REQ-002
    - REQ-006
    reason: Retain provenance and rights review and prohibit silently introduced contributor agreements or grants.
  - source:
      change: contribution-security-guidance
      requirement: REQ-003
      scenarios:
      - 2
      requirements_digest: 65986d898e8209f80081a5e8522e14d5f54ec040ad2b56391dcb892972b672f3
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: supersede
    targets:
    - REQ-001
    - REQ-008
    - REQ-010
    reason: Replace references to the approved proprietary H01 candidate with the separately reviewed Apache candidate
      and eventual actual adopted version, preserving tool/project separation.
  - source:
      change: contribution-security-guidance
      requirement: REQ-004
      scenarios:
      - 1
      - 2
      - 3
      - 4
      requirements_digest: 65986d898e8209f80081a5e8522e14d5f54ec040ad2b56391dcb892972b672f3
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-007
    - REQ-012
    reason: Reuse the scoped pilot and internal receipt evidence without promoting them to public Harness proof;
      require repository/audience-specific verification and scoped message authority.
  - source:
      change: contribution-security-guidance
      requirement: REQ-005
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 65986d898e8209f80081a5e8522e14d5f54ec040ad2b56391dcb892972b672f3
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-008
    - REQ-011
    reason: Retain multilingual semantics/navigation and avoid absorbing general documentation or language-automation
      initiatives.
  - source:
      change: contribution-security-guidance
      requirement: REQ-006
      scenarios:
      - 1
      - 2
      - 3
      - 4
      requirements_digest: 65986d898e8209f80081a5e8522e14d5f54ec040ad2b56391dcb892972b672f3
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-007
    - REQ-009
    - REQ-011
    - REQ-012
    reason: Preserve independent rollout/adoption, actual reporting verification, maintained regression evidence
      and planning-only boundaries.
  - source:
      change: root-plugin-package
      requirement: REQ-001
      scenarios:
      - 1
      requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: supersede
    targets:
    - REQ-004
    reason: Historical 0.2.0 is no longer the current source version. Require consistent exact reviewed candidate
      versions and the portable schema without freezing a future candidate to that obsolete value.
  - source:
      change: root-plugin-package
      requirement: REQ-001
      scenarios:
      - 2
      - 3
      requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-004
    reason: Retain all supported Skills and valid Codex compatibility metadata.
  - source:
      change: root-plugin-package
      requirement: REQ-002
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-004
    - REQ-011
    reason: Retain canonical root directories, installed resource resolution and absence of duplicated Standards
      trees.
  - source:
      change: root-plugin-package
      requirement: REQ-003
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-004
    - REQ-005
    reason: Keep repository marketplace, exact references and the usable workspace route while adding independently
      verified external installation/update and recovery.
  - source:
      change: root-plugin-package
      requirement: REQ-004
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-004
    - REQ-009
    - REQ-010
    reason: ADR-0011 remains the effective package boundary; retain accepted architectural history and validation
      of paths/version drift without recreating its delivered migration.
  - source:
      change: harness-user-documentation
      requirement: REQ-001
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-004
    - REQ-005
    - REQ-008
    reason: Extend maintained README orientation/navigation and version/access distinctions to the external audience.
  - source:
      change: harness-user-documentation
      requirement: REQ-002
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-005
    - REQ-008
    - REQ-012
    reason: Reuse the representative first-use planning flow, explicit recovery and canonical SDD navigation; add
      public-access preparation without inventing installation success.
  - source:
      change: harness-user-documentation
      requirement: REQ-003
      scenarios:
      - 1
      - 2
      - 3
      - 4
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-004
    - REQ-005
    - REQ-008
    - REQ-012
    reason: Retain all maintained workflow guides, observed applicability, canonical procedures and human gates;
      external setup adds context without replacing them.
  - source:
      change: harness-user-documentation
      requirement: REQ-004
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-008
    - REQ-011
    reason: Preserve original product context and evidence-aware claims while extending audience/availability description;
      no new market or revenue claims are introduced.
  - source:
      change: harness-user-documentation
      requirement: REQ-005
      scenarios:
      - 1
      - 2
      - 3
      - 4
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-008
    - REQ-011
    reason: Retain aligned language siblings, localized links, semantic parity and organization-owned entry boundaries.
  - source:
      change: harness-user-documentation
      requirement: REQ-006
      scenarios:
      - 1
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: supersede
    targets:
    - REQ-008
    - REQ-010
    reason: Public instructions must not require or export internal recording URLs or private provenance. Preserve
      attributable source history in approved restricted evidence and use safe public provenance for the external
      guide.
  - source:
      change: harness-user-documentation
      requirement: REQ-006
      scenarios:
      - 2
      - 3
      - 4
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-005
    - REQ-008
    - REQ-009
    reason: Retain actual usage observations, translation/navigation review, full package validation and stable
      living documentation outside the movable dossier.
  - source:
      change: harness-user-documentation
      requirement: REQ-007
      scenarios:
      - 1
      - 2
      - 3
      - 4
      - 6
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-006
    - REQ-008
    - REQ-011
    - REQ-012
    reason: Keep maintained source ownership, usable organization entry and failure recovery; no organization mutation
      is included in this successor.
  - source:
      change: harness-user-documentation
      requirement: REQ-007
      scenarios:
      - 5
      requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
    current_contract:
      change: harness-publication-readiness
      artifact: proposal
      locator: '## Current contract baseline'
    effect: supersede
    targets:
    - REQ-009
    - REQ-011
    reason: Issue 22 is delivered history, and H02 already superseded this issue-specific new-work linkage. Future
      coordinated work uses its real approved issue/PR and repository checks without reopening Issue 22 or activating
      links early.
  - current_contract:
      path: scripts/validate/run.sh
      locator: validation_python=
      digest: 7cc5d5a3f20927618b613b37090cf792669e0920ffbbf9c60db8f0147e43c013
    effect: preserve
    targets:
    - REQ-004
    - REQ-009
    - REQ-011
    reason: Retain the existing complete validation entry point and maintained suites; planning success cannot establish
      legal, operational or external-user acceptance.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: User reply in this chat on 2026-11-13 to the explicit Gate 1 R1 approval question after both files were
      linked; the reply authorizes advancing only to Design.
    quote: Sim
    revision: 1
    digest: 41081278df433db671e12b7d442b78a446f792977cc976a37407a5113ee62443
---

# Proposal

## Context and problem

The owner selected public availability of the existing Harness repository and its Codex Plugin under Apache-2.0 for eligible first-party material. External developers need a self-contained installation and contribution route without membership in an internal workspace. The source already has the canonical root package, common licensing/contribution candidates and maintained guides, but active Harness-specific guidance still points to the older proprietary candidate and internal distribution/reporting boundaries.

This successor reconciles those effective contracts and prepares reviewable evidence for the new public boundary. The existing package architecture is retained. Publishing a repository exposes more than a release directory: current and historical files, conversations and service artifacts must all be assessed. Prior terms approval, a merged documentation PR or an internal reporting test cannot establish clearance of this changed scope.

## Expected outcome

A reviewed preparation candidate for the existing repository: concrete Apache license/notice candidates; refreshed rights and full-surface assessment; coherent public contribution/reporting and multilingual usage guidance; a version-matched package rehearsal; and an explicit operational handoff. Record cleared and deferred conditions honestly. Completion of a preparation assessment is not permission to label the repository publish-ready when required evidence is missing.

The current deliverable is only this Proposal and its [Requirements](requirements.md). Actual implementation is proposed future work after all three gates and an explicit implementation request. Effective license adoption, remote publication and other operations remain separately authorized.

## Scope

- Reuse H01 common policy, bounded provenance/dependency review and actual owner decisions; prepare the replacement concrete Apache terms and notices for fresh review.
- Reuse H02 guides and actual limited reporting observations; extend the external Harness route and assess repository-specific protections and confidential reporting.
- Cover H03 preparation: complete proposed public surface, root package, exact version/identity, private rehearsals, explicit updates/recovery and separately recorded post-publication verification.
- Maintain canonical Standards and guides, safe public-facing provenance, EN/PT/ES parity, existing validation suites and independent product handoffs.
- Define accountable review, drift checks, evidence handling, publication sequencing and containment requirements. Design will assign actual checks, input scopes and operational dependencies before Tasks are prepared.

## Out of scope

Under this request: implementation changes, Design/Tasks placeholders, ADR drafts, candidate license files, changes to living guidance/manifests/Standards, commit/push/remote issues or PRs, merge, license application, visibility/access/ruleset changes, releases/tags, marketplace activation, consumer upgrades, channel activation or messages. Local planning files, a separate worktree and read-only diagnostics are authorized preparation.

For the proposed implementation scope: no public mirror, new repository or SDK, copied Standards distribution, automatic release/consumer migration engine, unrelated product runtime/commercial/hiring work, or organization-wide adoption. Destructive remediation, history rewriting and changes to the intended publication destination require separate authorization and material replanning. Operational publication and post-publication acceptance are a distinct follow-up, not circular prerequisites for merging the preparation documents.

## Work tracking

- Change ID: `harness-publication-readiness`, a new successor; no matching active/archive dossier existed at preparation.
- Related existing work: [H01 #34](https://github.com/versat-labs/versat-ai-harness/issues/34), [H02 #35](https://github.com/versat-labs/versat-ai-harness/issues/35), and their integrated [PR #37](https://github.com/versat-labs/versat-ai-harness/pull/37). Preserve their real identities and delivered dossiers. Old issue prose describing an unmerged PR is historical, not evidence against the observed merge.
- No new issue or Shortcut Story is associated or created. Do not invent one or close the earlier issues as an effect of this plan. The open-PR search returned no results and the scoped Apache issue search found H01, not an existing public-readiness successor.
- Local branch: `codex/harness-publication-readiness`, based on fetched `origin/main` at `d61317d9220b002f0dc3aa606e18a62dd4230477`. No remote changes are requested.

## Repository and Standards context

This is the Harness provider repository, not a consumer. It has no root consumer `.versat/project.yaml` or Standards lock to fabricate. Use this checkout's exact source snapshot as the provider: declared VERSION and portable/Codex manifests `0.3.0`, baseline `d61317d9220b002f0dc3aa606e18a62dd4230477`, SDD v3. The installed plugin tagged 0.3.0 is not assumed to contain the same unreleased source. No provider or consumer upgrade is performed.

Applicable instructions: root [AGENTS](../../../AGENTS.md), [architecture](../../../docs/architecture/overview.md), [ADR-0011](../../../docs/decisions/0011-root-portable-plugin-package.md), [process](../../../sdd/process.md), [New change](../../../sdd/workflows/new-change.md), [metadata](../../../sdd/metadata.md), v3 Proposal/Requirements templates/schemas and [validator instructions](../../../validators/sdd/README.md). There are no more-specific AGENTS under this dossier path.

Resolve `core.always` through [standards/index.yaml](../../../standards/index.yaml): language, documentation, agent artifacts, Git, security, licensing/publication, contribution, testing and observability. The H01/H02 policy extensions are indexed private implementation candidates; their file presence is not adopted policy or operational configuration. They supply the existing review contract to reconcile. No consumer profile/domain or irrelevant application technology is invented; Python is the observed validation runtime. Preserve top-level policy/process/capability/enforcement boundaries.

| Provider anchor | SHA-256 |
|---|---|
| `sdd/process.md` | `488b63b3ad26e4779db69d4b6ea9bd28b629936f58ccb42493cdaa99c940ccdb` |
| `sdd/metadata.md` | `788c3a0ae8ac265a66546d3dddbf35e2c0c81bfa932940f3e5eae34990a0a064` |
| `sdd/workflows/new-change.md` | `3fed9300f21ecc17d799b188179efb5a149a0afec4a91098f613a007c40f7cd4` |
| `standards/index.yaml` | `0a70db972dc3ba14cecf27a1617e404f63ab32ec1222ae8632c30698ecbcccee` |
| `validators/sdd/validate.py` | `94f152e14dbe1dbb60fcd3d0ef40ba896fd9a71234d28d44ac8ba1d172d329bb` |

## Current contract baseline

Observed on 2026-11-13 at the exact source above:

| Effective contract | Repository-backed baseline and consequence |
|---|---|
| Terms and rights | `docs/licensing/harness-plugin-terms.md` is an approved-candidate proprietary draft, with no effective adoption. `docs/governance/h01-approval.md` binds the frozen draft-0.2 and actual approval. `docs/governance/licensing-review.md` and `docs/licensing/technical-review/README.md` preserve bounded owner provenance, source/dependency observations and limitations. Reuse that evidence; new Apache wording and full public scope need their own review. No root LICENSE/NOTICE was found in the tracked-file inventory. |
| Publication review | `standards/core/licensing-publication.md` requires component evidence, actual reviewers, dispositions and full export scope; missing evidence defers clearance. The prior bounded inventory is not a complete current/history/remote-surface audit. Historical requirements retain obsolete private/proprietary Harness assumptions that this successor intentionally replaces. |
| Contribution and reporting | `standards/core/contribution.md`, the security extension and maintained contribution/reporting guides distinguish target-project terms, private access, actual verification and safe fallback. `docs/governance/security-reporting.md` records the .github PVR pilot and internal Harness email receipt; neither verifies the proposed public Harness route. No new message or control mutation occurred. |
| Package and versions | ADR-0011 makes the repository root the installable package. `VERSION`, `plugin.json` and `.codex-plugin/plugin.json` are 0.3.0; `.agents/plugins/marketplace.json` is `versat-internal`, exact `v0.3.0`. Root-package Requirements mention historical 0.2.0; the current invariant is agreement of the selected candidate's version, not returning to 0.2.0. |
| Usage and languages | README, `docs/user-docs/quickstart.md` and maintained guides already explain first-use, SDD, validation and recovery with EN/PT/ES siblings. `workspace-setup.md` assumes administrator-managed workspace access and links optional internal training; licensing/contribution guides reference private approval evidence. Public-facing guidance must be self-contained while preserving useful workflows and restricted history. |
| Existing enforcement | `validators/plugin/validate.py` checks root paths, supported Skills, schema/manifest/template-lock/marketplace agreement. `scripts/validate/run.sh` runs package/SDD checks and maintained validator/execution suites. `.github/workflows/validate.yml` uses a trusted baseline and the archive guard for non-draft PRs/main. Local files do not prove actual required-check enforcement or fork-secret safety. |
| Historical and remote state | Four source dossiers used by impact are unique under `specs/archive/`; there is no active matching successor. Fetched main includes PR #37 at the baseline commit. The repository was observed private; marketplace ref unchanged. Remote full-surface clearance, protections, release/install behavior and public reporting remain unverified. |

The impact table binds every acceptance position from H01, H02, root-plugin-package and harness-user-documentation once. Current contracts above govern where a historical requirement is obsolete. In particular, H02 already replaced Issue-22-specific new-work linkage, and a source manifest's old 0.2.0 assertion does not override current 0.3.0 metadata. The replacement requirements retain public provenance and human gates while eliminating mandatory private links and incompatible future proprietary restrictions.

## Impact and risks

- Rights and wording: preserve earlier genuine approvals, but do not transfer them to a different license. Concrete candidate review and third-party evidence are separate acceptance obligations.
- Confidentiality: the root package contains historical governance/validation material. Its exact sensitivity is not presumed cleared. If immutable history cannot safely become public, defer and escalate the specific conflict; do not quietly delete evidence or substitute a mirror.
- Version compatibility: keep source snapshots, releases, marketplace identity and installed consumers distinct. Design must assess semantic version impact and exact supported runtimes before selecting a new candidate.
- Controls and channels: reuse established ownership and limited tests, but assess real repository/audience behavior. Written instructions and administrator access do not prove external-user access or confidentiality.
- Evidence quality: maintained package/tests verify mechanical behavior; actual rights, surface, multilingual usage and operational observations require their own reproducible checks. Do not weaken suites or turn unknowns into passes to finish a dossier.

## Ownership and decisions to resolve during Design

Reuse the previously recorded accountable executor/licensing/security contact `@elviszoz` and the declared first-party holder from H01, with their original scope and evidence limits. Current `.github/CODEOWNERS` assigns `@elviszoz` by default and `@elviszoz` plus `@evertonspohrversat` to governed paths including Standards, SDD, Skills and validators; these assignments do not prove actual independent review, professional qualification or configured controls. No identical ownership or provenance question is reopened merely because this is a successor.

Gate 1 has no unresolved choice of repository or license model. Future evidence work is explicitly required, not represented as completed. Before Design approval, resolve the concrete candidate/release and supported runtime assessment, private evidence location/access using an already approved restricted system, exact preparatory versus operational action boundaries, and actual reviewer capacities. Reuse existing answers; ask only for a genuinely missing material decision. Findings can yield defer rather than speculative clearance. If discovery changes the chosen scope, reopen Gate 1.

## Proposal acceptance criterion

The paired Requirements define observable preparation, success/error/boundary behavior and preserved obligations; identify what will remain unverified until a separately authorized operation; and establish a safe, reviewable Gate 1 decision without implementing it. Design must map every local scenario and retained obligation to meaningful checks, preserve all required suites and separate pre-merge preparation from post-publication verification.

## Planning review

Stage: Proposal/Requirements R1. State: awaiting approval, no current Gate 1 blocker, approval null. The user's instruction authorizes only preparation of these two files; it is not approval of their unseen contents. Approval of R1 unlocks Design only. Tasks, implementation and publication remain unauthorized.

Initial planning validation returned `unable-to-verify` for one `IMPACT_BASELINE`: the validation-script locator was a description rather than a literal source excerpt. The unapproved R1 locator was corrected to an existing excerpt; its actual file hash was unchanged. The first full package run consequently exited 1 for that same draft defect, while all 131 validator tests and 48 execution tests passed. The final re-execution results are recorded below. No implementation acceptance ledger or completion claim is created at this stage.


Final preparation checks observed on 2026-11-13:

- Selected `validators/sdd/validate.py --root . --change harness-publication-readiness --phase planning --json`: exit 0, pass, no findings or warnings; 38 local scenarios and 72 retained regression obligations. These are planning declarations, not executed acceptance results.
- Required `./scripts/validate/run.sh`, with `PYTHON` set to the verified virtual-environment interpreter and `PYTHONDONTWRITEBYTECODE=1`: exit 0; portable package and SDD inventory pass, 131 validator tests and 48 execution tests pass. Historical legacy/v2 inventory warnings remain attributable to the pre-existing exempt dossiers; no exemption was added or modified.
- Runtime observed: Python 3.11.4, PyYAML 6.0.2 and jsonschema 4.23.0, matching `requirements-validation.txt`. Use a Python 3.11+ environment with that pinned requirements file and this exact source provider to reproduce the commands; the installed 0.3.0 Plugin is not a substitute for the source snapshot.
- Independent inspection: all 1,382 pre-existing tracked files are byte-identical to HEAD, all nine local Markdown links resolve, whitespace checks pass, and the only new repository files are this Proposal and Requirements. All 78 qualified source scenarios are classified exactly once; seven intentional supersessions have replacement targets, 71 are retained, and one additional current validation-entry obligation is retained.
- Both files use SDD v3 and the same change ID. Proposal review is R1/awaiting-approval with approval null and no Gate 1 blocker. No Design, Tasks, implementation evidence, license candidate, or archive copy was created. No remote write or publication occurred.
- Canonical combined Proposal/Requirements R1 digest: `41081278df433db671e12b7d442b78a446f792977cc976a37407a5113ee62443`. This is an identity for the presented revision, not an approval. Local checks do not establish rights clearance, remote CI, public usability or operational readiness.

### Gate 1 approval — 2026-11-13

The user replied “Sim” to the explicit question approving Proposal and Requirements R1 and advancing only to Design. The presented files were copied byte-for-byte into the subsequently attached managed worktree on the same source baseline, and their canonical combined digest was reverified as `41081278df433db671e12b7d442b78a446f792977cc976a37407a5113ee62443` before recording approval. The original temporary planning checkout remains untouched; this managed worktree on `codex/harness-publication-design` is the continuation. Earlier pending statements above preserve presentation history. Gate 1 is approved; Design and a necessary proposed ADR may be prepared. Tasks, implementation and operational actions remain unauthorized.
