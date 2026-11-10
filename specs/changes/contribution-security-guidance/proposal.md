---
sdd_version: 3
change: contribution-security-guidance
status: accepted
owner: "@elviszoz"
summary: Complete contribution and confidential reporting guidance while preserving delivered multilingual entry points.
risk: high
impact:
  state: assessed
  summary: Reviewed the source baseline, applicable Standards, maintained validators and relevant archived requirements; preserve existing boundaries while extending the missing policy and guidance.
  items:
    - source:
        change: harness-user-documentation
        requirement: REQ-007
        scenarios: [1, 2, 3, 4, 6]
        requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
      current_contract:
        change: contribution-security-guidance
        artifact: proposal
        locator: "## Current contract baseline"
      effect: extend
      targets: [REQ-001, REQ-002, REQ-006]
      reason: Extend maintained contribution routes with rights and confidential reporting while retaining source ownership, access conditions and safe replacement behavior.
    - source:
        change: harness-user-documentation
        requirement: REQ-007
        scenarios: [5]
        requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
      current_contract:
        change: contribution-security-guidance
        artifact: proposal
        locator: "## Current contract baseline"
      effect: supersede
      targets: [REQ-006]
      reason: Preserve historical Issue 22 traceability; new H02 coordinated work must instead link Issue 35, with destinations, intended access and repository-specific review still required.
    - source:
        change: harness-user-documentation
        requirement: REQ-005
        scenarios: [1, 2, 3, 4]
        requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
      current_contract:
        change: contribution-security-guidance
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-005]
      reason: Retain canonical English and semantically aligned localized community entry points.
    - source:
        change: harness-user-documentation
        requirement: REQ-003
        scenarios: [2, 3, 4]
        requirements_digest: d37584fff5b035004dcb6fb020f9099f1411ef7cd612ae667c7e1ffc21595773
      current_contract:
        change: contribution-security-guidance
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-001, REQ-002, REQ-006]
      reason: Keep canonical procedures, human gates, exact-version and availability limits in reused guidance.
    - current_contract:
        path: standards/core/security.md
        locator: "# Security Standard"
        digest: c16c9832ba9ae5a9b9673289b2c56df709873a1566ecfa52918735357dd096f8
      effect: extend
      targets: [REQ-003, REQ-004]
      reason: Extend provenance and confidential handling to contribution/reporting guidance without claiming a configured channel.
    - current_contract:
        change: contribution-security-guidance
        artifact: proposal
        locator: "## Current contract baseline"
      effect: extend
      targets: [REQ-003, REQ-004, REQ-006]
      reason: Add the missing approved-terms references, actual channel verification and per-product adoption evidence.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: "User reply in this chat on 2026-11-10, after presentation of both R1 pairs and clarification of the two Harness changes."
    quote: "Aprovado. Avance ao design."
    revision: 1
    digest: 6bed2e92d705d83385b31d27364cfcda2b05549678818801c6082132d6dbc8d2
---

# Proposal

## Context and problem

H02 has substantial delivered foundations but is not complete. Harness Issue 22 and PR 33 delivered usage documentation; organization PR 3 consolidated contribution entry points. Remaining scope is common provenance/review rules, approved tool/project terms and verified confidential security reporting, with separate product adoption.

## Expected outcome and scope

Reuse the living Harness guides and the organization's short contribution entry. Explain authorized public/private participation, provenance, required review/checks and confidential reporting. Keep English canonical with aligned Portuguese and Spanish. A reader without internal access must retain a usable route based on the destination repository.

H01 provides common policy and approved Harness terms; H02 must refer to the actual approved version. Design may prepare guidance concurrently, but missing terms or an unverified reporting route prevent a completion claim. Applying guides in P01/P03 and releasing the plugin in H03 remain separate.

## Out of scope

No implementation, channel activation, genuine vulnerability submission, public organization edits, access grant, license application, CLA/DCO selection, release, runtime work, recruiting launch or consumer update now. General documentation and multilingual automation remain in existing Issues 23/26.

## Work tracking and reconciliation

- Executor: [Harness #35](https://github.com/versat-labs/versat-ai-harness/issues/35), for residual H02 scope; new change `contribution-security-guidance`.
- [Harness #22](https://github.com/versat-labs/versat-ai-harness/issues/22) is closed/completed and assigned to `@elviszoz`. [Harness PR #33](https://github.com/versat-labs/versat-ai-harness/pull/33) merged on 2026-11-09 at 18:32:28 UTC; [organization PR #3](https://github.com/versat-labs/.github/pull/3) merged at 18:33:45 UTC. Their old PR body wording about draft/pending review is historical; actual merged fields establish current status.
- Preserve those deliveries. Do not reopen Issue 22, copy its dossier or claim its checks validate new policy/channel behavior.
- [#23](https://github.com/versat-labs/versat-ai-harness/issues/23) remains open/unassigned for general documentation standards and publishing/automation; [#26](https://github.com/versat-labs/versat-ai-harness/issues/26) remains open/unassigned for multilingual workflow/CI. H02 applies existing documentation/language requirements without completing these broader issues.
- [H01 / #34](https://github.com/versat-labs/versat-ai-harness/issues/34) is the approved-terms dependency. [strategy #11](https://github.com/versat-labs/strategy/issues/11) retains strategic coordination.
- No Shortcut Story is associated. Local branch: `codex/plan-h01-h02`.

## Current contract baseline

At source 597b81c71a0fc0908ff5264fe9987bb5c0d8feec, Harness README and `docs/user-docs/` provide maintained multilingual navigation, setup, SDD, GitHub delivery and validation guidance. `sdd/README.md` remains the canonical collaboration reference; the Harness has no local CONTRIBUTING file. Archived `harness-user-documentation` records the completed consolidation and its acceptance obligations.

The organization's live `CONTRIBUTING.md` (Git blob `444ee0ddcadaae8ebb6cc616d6041587ec4563b5`, retrieved 2026-11-10) preserves repository-specific precedence and a public issue/PR contribution route. Private Harness resources are explicitly marked and pinned to `27735687a37e896cd6b0c95cd9d2d848ee166d90`. These references do not constitute public plugin access. The inspected file has no confidential security-reporting route or approved Harness terms reference. Organization `AGENTS.md` requires human SDD checkpoints for material policy/process changes. No organization change is made here.

`standards/core/security.md`, `git.md`, `documentation.md` and `language.md` supply current security, review, documentation and EN/PT/ES rules. CODEOWNERS establishes technical reviewers, not legal authority or reporting-channel operation. No verified channel configuration or confidential receipt evidence has been obtained.

The maintained package validation entry `scripts/validate/run.sh` and documentation change's historical content/navigation/usage checks are relevant reusable methods. Historical results are not fresh H02 acceptance. New channel verification, terms/provenance review and affected access/navigation/translation checks must be specified at Design; structural success alone is insufficient.

## Impact and risks

Preserve public fallback, intended-reader access, repository-specific precedence, canonical policy/process, existing useful documentation and translations. Only the old new-delivery traceability to Issue 22 is superseded for future H02 work; the completed historical deliveries remain unchanged.

`versat-labs/.github` is public and is a future coordinated destination, not an authorized write target now. Export candidates must be independently usable and sanitized. Elvis is the confirmed accountable contact; actual channel configuration, terms review and rights evidence remain prerequisites. No invented endpoint, response promise or legal mechanism fills those gaps.

## Proposal acceptance criterion

The requirements identify residual H02 scope, preserve the completed consolidation, require approved terms and observed confidential-route verification, and keep per-product adoption and public activation separate. They cover success, missing access, unavailable channel, missing rights/review and cross-repository failure boundaries.

## Source and Standards resolution

Executor repository: `versat-labs/versat-ai-harness`. Source baseline: `597b81c71a0fc0908ff5264fe9987bb5c0d8feec`, observed on local main and confirmed through the GitHub connector on 2026-11-10. `VERSION` is `0.3.0`; this exact source snapshot contains SDD v3 and is the planning provider, not a claim that its newer source behavior is present in the installed 0.3.0 release. No consumer lock or release is upgraded.

The Harness is the provider repository, not a consumer requiring a fabricated `.versat/project.yaml` or lockfile. Read its `AGENTS.md`, `standards/index.yaml`, `sdd/process.md`, `sdd/workflows/new-change.md`, `sdd/metadata.md` and v3 templates/schemas. The index's always-applicable language, documentation, agent-artifact, Git, security, testing and observability Standards govern this policy/documentation change. No application technology or profile is invented. Normative policy remains in Standards; process in SDD; capabilities in Skills; deterministic checks in validators.

## Ownership and open inputs

Confirmed technical review owners in `.github/CODEOWNERS`: Elvis Zoz (`@elviszoz`) and Everton Spohr (`@evertonspohrversat`) for Standards and SDD. On 2026-11-10 the user named `@elviszoz` as responsible and offered to hold the licensing/legal and security responsibilities too. Record Elvis as executor and accountable decision/contact owner for these handoffs. This appointment does not claim professional legal qualification, completed specialist review or a configured security channel. Product-specific maintainers and any additional specialist reviewer can be identified during the respective executor planning.

The user identified **Versat E.A.S.** as the license-owning legal entity. Treat that as the declared rights holder, subject to component/contract and third-party rights verification; it does not prove that all authorship, grants or dependency rights are already cleared. No company registration, jurisdiction, address or legal representative powers are invented. Exact legal text must resolve any required legal-entity details before acceptance.

Gate 1 has no unresolved scope or license-model choice: selected product models are inputs, and publication/license changes are excluded. Exact rights inventories, legal wording, channel configuration and distribution evidence are required future work, not facts this proposal asserts.

## Authorization and planning review

The user's 2026-11-10 instruction authorizes initiating handoff planning, confirming repositories/owners and reconciling existing work, starting with H01/H02, without publication or license changes. Proposal/Requirements R1 are presented together with no recorded approval. This permission to prepare the plan is not approval of unseen R1 artifacts.

Only Proposal and Requirements exist for this change. Gate 1 acceptance permits Design; the user has resolved nominal accountability, while component rights, terms review and channel evidence remain future acceptance prerequisites. Design, Tasks, implementation, legal approval, public rollout, merge and release remain separate. Private issue reconciliation is administrative tracking, not policy adoption.

## Planning review

Proposal/Requirements R1 was presented with both files and its validation. After clarification that H01 and H02 are two separate Harness changes already being handled in this chat, the user replied on 2026-11-10: "Aprovado. Avance ao design." The canonical combined digest was recomputed and matched the presented revision: `6bed2e92d705d83385b31d27364cfcda2b05549678818801c6082132d6dbc8d2`. Gate 1 is approved and Design preparation is authorized. Earlier unapproved-stage descriptions above retain their original context; they are not the current review state. This approval does not authorize Tasks, implementation, terms application, channel activation or publication.
