---
sdd_version: 3
change: portfolio-licensing-policy
status: accepted
owner: "@elviszoz"
summary: Define common portfolio publication policy and separately reviewed proprietary Harness/plugin terms.
risk: high
impact:
  state: assessed
  summary: Reviewed the source baseline, applicable Standards, maintained validators and relevant archived requirements; preserve existing boundaries while extending the missing policy and guidance.
  items:
    - current_contract:
        change: portfolio-licensing-policy
        artifact: proposal
        locator: "## Current contract baseline"
      effect: extend
      targets: [REQ-001, REQ-003, REQ-004, REQ-006]
      reason: Add the absent portfolio policy and concrete-terms approval path without treating strategic selection as operative licensing.
    - current_contract:
        path: standards/core/security.md
        locator: "# Security Standard"
        digest: c16c9832ba9ae5a9b9673289b2c56df709873a1566ecfa52918735357dd096f8
      effect: extend
      targets: [REQ-002, REQ-004, REQ-006]
      reason: Preserve least privilege, secret handling, provenance and explicit high-impact authorization while specifying evidence for publication decisions.
    - source:
        change: root-plugin-package
        requirement: REQ-002
        scenarios: [1, 2, 3]
        requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
      current_contract:
        change: portfolio-licensing-policy
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-005]
      reason: New policy must retain canonical root resources and avoid copied Standards.
    - source:
        change: root-plugin-package
        requirement: REQ-003
        scenarios: [2]
        requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
      current_contract:
        change: portfolio-licensing-policy
        artifact: proposal
        locator: "## Current contract baseline"
      effect: preserve
      targets: [REQ-005]
      reason: Retain the exact semantic release selection contract; this proposal neither releases nor enables public distribution.
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: "User reply in this chat on 2026-11-10, after presentation of both R1 pairs and clarification of the two Harness changes."
    quote: "Aprovado. Avance ao design."
    revision: 1
    digest: 5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7
---

# Proposal

## Context and problem

H01 needs two distinct outcomes: a common portfolio publication/licensing policy and concrete proprietary terms common to the Harness and Codex plugin. The existing Standards define security and review boundaries but do not supply this policy or the actual reviewed terms. A generic policy cannot establish installation/use/modification/redistribution permissions.

## Expected outcome and scope

A discoverable canonical policy records rights/dependency and confidentiality prerequisites, accountable reviewers, evidence, and publish/defer/retain-private decisions. A separate versioned Harness/plugin terms candidate covers the concrete permissions and notices and records real review before any approval claim. Product-specific adoption remains in each executor.

Preserve the selected intent: Platform and Collaborative Workspace Apache-2.0; Discover and CRM private/proprietary; Harness private/proprietary with separately planned public plugin distribution. The tool's terms do not change destination-project licensing. No SDK repository is introduced.

## Out of scope

No policy or terms implementation during this planning stage; no LICENSE/NOTICE application, effective legal terms, repository visibility, distribution, release, access/control changes, public documentation or customer/candidate contact. No product runtime or H03 packaging design. Even eventual completion of H01's policy/terms does not authorize operational publication.

## Work tracking and reconciliation

- Executor: [Harness #34](https://github.com/versat-labs/versat-ai-harness/issues/34), newly created for the uncovered H01 scope after searching existing issues/PRs.
- Strategic source: [strategy #11](https://github.com/versat-labs/strategy/issues/11); preserve its existing scope/type and separate policy delivery.
- [Harness #31](https://github.com/versat-labs/versat-ai-harness/issues/31) is open/unassigned and covers dependency management, compatibility and validation. Reuse applicable evidence without absorbing that broader work or asserting it is complete.
- [Harness #22](https://github.com/versat-labs/versat-ai-harness/issues/22) is closed/completed; [PR #33](https://github.com/versat-labs/versat-ai-harness/pull/33) merged on 2026-11-09. It supplies usage documentation, not H01 terms or legal clearance. Do not reopen it.
- [H02 / Harness #35](https://github.com/versat-labs/versat-ai-harness/issues/35) consumes approved terms and common policy; it can plan concurrently.
- No Shortcut Story is associated. Local branch: `codex/plan-h01-h02`. The two dossiers share a planning checkout and keep separate identities and approvals.

## Current contract baseline

At source 597b81c71a0fc0908ff5264fe9987bb5c0d8feec, `standards/core/security.md` requires least privilege, secret protection, high-impact authorization and reviewable dependencies/provenance. `standards/core/git.md` requires review and CODEOWNERS for corporate-policy changes. The inspected Standards index contains no licensing/publication Standard, and this checkout contains no root LICENSE, NOTICE or concrete proprietary terms file.

`docs/architecture/overview.md` and ADR-0011 preserve the repository-root package and version-matched canonical resources. Archived `root-plugin-package` REQ-002 remains effective for canonical resolution; REQ-003/2 retains exact-release selection. Historical version 0.2.0 examples are not imposed as the current version. Full public distribution from a private source raises package-surface questions that H03 must resolve; H01 cannot certify them by documentary inspection.

The maintained `validators/plugin/validate.py` and `scripts/validate/run.sh` check package invariants and the SDD/validator suites. They do not prove IP ownership, legal approval or confidentiality clearance. No licensing-specific behavioral suite was found in the inspected package entry points; meaningful human evidence review is required in Design, without weakening existing mechanical checks.

## Impact and risks

Retain common policy versus product delivery, canonical source paths, exact versions and security authorization. New legal wording requires actual authorized human review. A missing dependency inventory or unknown reviewer remains a visible prerequisite. No old strategy or Harness documentation check is reused as current H01 acceptance.

## Proposal acceptance criterion

Requirements identify policy and terms as separately verifiable outputs; each affected product retains its chosen model and own adoption, failures prevent clearance, canonical resources stay intact, and operational licensing/publication remain outside current authorization.

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

Proposal/Requirements R1 was presented with both files and its validation. After clarification that H01 and H02 are two separate Harness changes already being handled in this chat, the user replied on 2026-11-10: "Aprovado. Avance ao design." The canonical combined digest was recomputed and matched the presented revision: `5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7`. Gate 1 is approved and Design preparation is authorized. Earlier unapproved-stage descriptions above retain their original context; they are not the current review state. This approval does not authorize Tasks, implementation, terms application, channel activation or publication.
