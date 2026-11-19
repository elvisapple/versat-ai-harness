---
sdd_version: 3
change: harness-marketplace-transition
status: proposed
owner: Versat / Elvis
summary: Deliver the versat marketplace source for two current users with later manual reinstallation and explicitly
  deferred native compatibility observations.
risk: medium
impact:
  state: assessed
  summary: Retain catalog/plugin/package boundaries and maintained tests; replace broad pre-merge containment and
    mandatory isolated rehearsal with an owner-directed two-user manual reinstallation transition. Existing source
    and evidence remain preserved.
  items:
  - source:
      change: harness-publication-blockers
      requirement: REQ-008
      scenarios:
      - 1
      requirements_digest: 3a0aad556c3418f8cd45898689daab4d51586adc1d59a9cbce0444433bf19cc0
    current_contract:
      change: harness-marketplace-transition
      artifact: proposal
      locator: '## Current contract baseline'
    effect: supersede
    targets:
    - REQ-001
    - REQ-003
    - REQ-004
    reason: Replace only marketplace identity preservation with a reviewed migration; retain plugin/root identities
      and exact-version recovery.
  - source:
      change: harness-publication-blockers
      requirement: REQ-008
      scenarios:
      - 2
      - 3
      requirements_digest: 3a0aad556c3418f8cd45898689daab4d51586adc1d59a9cbce0444433bf19cc0
    current_contract:
      change: harness-marketplace-transition
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-005
    - REQ-006
    reason: Keep multilingual truthfulness, unchanged independent products and explicit consumer boundaries.
  - source:
      change: root-plugin-package
      requirement: REQ-002
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
    current_contract:
      change: harness-marketplace-transition
      artifact: proposal
      locator: '## Current contract baseline'
    effect: preserve
    targets:
    - REQ-001
    - REQ-006
    reason: No duplicated package tree or relocated canonical resource resolution.
  - source:
      change: root-plugin-package
      requirement: REQ-003
      scenarios:
      - 1
      - 2
      - 3
      requirements_digest: 6f5faf87eb5260aad8df82d300a32216becffca7ae2d318b989342cc737a506d
    current_contract:
      change: harness-marketplace-transition
      artifact: proposal
      locator: '## Current contract baseline'
    effect: extend
    targets:
    - REQ-002
    - REQ-004
    - REQ-005
    reason: Extend exact-ref catalog distribution with explicit legacy/new identity handling; historic private audience
      is not restored.
review:
  revision: 2
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: Current conversation reply to the explicit request to approve Proposal and Requirements R2 and adjust
      Design
    quote: Sim. Avance.
    revision: 2
    digest: e2cf501301bc4a8ef482631a8ad3d4f60a060a43087ceca9914537622340e773
---

# Proposal

## Context and decision input

The owner reports that only Elvis and Everton currently use the Harness and directs proceeding with the update, followed by their manual reinstallation: “Somente eu e Everton estamos utilizando o harness por enquanto. Então, prossiga com a atualização que depois nós reinstalamos o plugin manualmente.” The earlier owner report states that the managed marketplace tracks main and no disposable native environment is available. These are attributed reports, not an independently audited roster or completed reinstallations.

The local source already implements `versat` / `Versat Plugins`, retaining plugin `versat-ai-harness`. Its recorded final suite passed 191 tests, including 12 new marketplace regressions. Under the previous plan, missing native rehearsal and managed-source containment blocked complete delivery. R2 changes those acceptance prerequisites for this bounded population; it does not turn the missing observations into passes.

## Expected outcome

Finish source preparation for a protected PR while accepting that the main-tracking catalog may refresh and require manual repair for the two current users. Do not provision an isolated environment or require a workspace pin solely to unblock this delivery. Elvis and Everton reinstall manually later, with concrete exact-version/resource checks. The plugin/package/legal boundaries, meaningful maintained tests, required CI and eligible nonauthor review remain unchanged.

## Scoped supersession

| Existing requirement | Proposed R2 replacement |
|---|---|
| Broad inventory and pre-merge sync containment, REQ-002 | Reported two-user population and known main tracking; accept possible sync exposure/temporary interruption; reassess if another user is found. |
| Seven-case isolated rehearsal before source delivery, REQ-003 | Keep native outcomes unverified and defer actual observation to later manual use/reinstallation; source acceptance uses deterministic tests and honest guidance. |
| Preserve transparent continuity before any rollout, REQ-004 | Manual per-user handoff without an automatic migration or managed-ID guarantee; retain exact source/project recovery records and prohibit unrequested destructive work. |

This supersedes only those R1 prerequisites and their dependent Design R2/Tasks R2 interpretation. Previous failures, real approvals, code, 191-test results and unknown native outcomes stay preserved. Historical `root-plugin-package` and `harness-publication-blockers` obligations remain scoped as in impact metadata: canonical resources, exact package refs and truthful distribution guidance are retained. No new package architecture or ADR is proposed.

## Scope and boundaries

Prepare revised Proposal/Requirements now. After actual approval, reconcile the dependent Design and Tasks, then update only affected active guidance and evidence within authority. Reuse the implemented catalog/validator/test work; rerun affected checks on final inputs rather than rewriting historical results. Do not mark obsolete findings resolved by test success: their later disposition must explicitly identify the reviewed scope/acceptance change.

This revision does not operate on the workspace, install/uninstall a plugin, migrate consumers, create tags/releases or perform remote Git operations. The user's direction is recorded; concrete remote delivery remains subject to its applicable scoped authority and mandatory PR controls. Manual reinstallation is the users' future action, not an agent action or a completed event. Wider managed-ID continuity, external installation/update/recovery, external fork/CI and private-report receipt/confidentiality remain pending.

## Current contract baseline

- Reviewed source: main `c13b2f9a8e3188a2e3f74e6a84f87c7ad59189aa`, declaring 0.4.0, originally `versat-internal`. On the last read-only remote listing (2026-11-18), only v0.2.0/v0.3.0 tags existed. No fresh remote observation is claimed by this revision; recheck the exact target before delivery and never retag.
- Current local delta: only catalog name/display changes to `versat` / `Versat Plugins`; plugin `versat-ai-harness`, repository URL, exact `source.ref: v0.4.0`, AVAILABLE/ON_INSTALL policy, manifests, legal files and canonical package resources are preserved. The validator now checks marketplace identity/display, with 12 new maintained tests; full suites passed 191 tests on their recorded inputs.
- Earlier personal 0.4.0 and managed cached 0.3.0 observations are distinct from project/provider locks and actual session selection. The owner reports managed main tracking and only Elvis/Everton as users; exact sync timing and managed identity remain unknown.
- The previous 17-file documentary candidate, its failure report and all approvals remain preserved. Native discovery, same-source registration, collisions and recovery have not been exercised for the renamed candidate.

## Delivery and later verification

1. Review this bounded change of acceptance criteria; update dependent Design/Tasks after their applicable gates.
2. Reconcile active EN/PT/ES instructions and declared check mappings; keep unverified native observations separate from source-delivery requirements. Preserve current source work and rerun the complete required local suite, selected documentary delivery checks and subsequent mandatory CI on the real authorized PR.
3. Integrate only through applicable authorized protected review; do not require an unperformed post-merge reinstall as pre-merge task completion. A source update may expose the catalog to main synchronization, but does not create the unavailable exact package tag.
4. After a supported exact source/package is actually available and users proceed, observe each manual reinstallation's identity, version, effective provider, resources and representative Skill behavior. If it fails, record the concrete failure and use a verified compatible pair; no silent latest, cache/database manipulation or assumed recovery.

## Tradeoffs and alternatives

A fixed managed ref plus isolated rehearsal remains an option if the population or risk changes. For two reported users willing to reinstall, it introduces work the owner now chooses to defer. The proposed simpler route accepts potential disruption and manual repair while keeping native behavior unknown. Deferring the rename to a later version is still possible if a released v0.4.0 or a broader affected audience invalidates this bounded plan. None of these choices changes licensing, existing project locks, required CI or reviewer eligibility.

## Provider and validation

Use the [recorded provider](../../../docs/validation/harness-marketplace-transition/provider.json) at the exact reviewed source commit and its verified dependencies. The selected planning validator checks declared relationships; it cannot prove runtime behavior or turn superseded execution evidence into current acceptance. Downstream Design/Tasks remain superseded with actual progress/results preserved until reviewed revision. Report any pending-approval or stale-evidence diagnostics honestly; do not erase implementation history to obtain a green planning result.

## Work tracking

Change ID `harness-marketplace-transition`; local branch `codex/harness-marketplace-transition`. No associated Shortcut Story or remote issue is invented. No remote mutation occurs during this replanning.

## Proposal acceptance criterion

Approve Proposal/Requirements R2's two-user source-delivery disposition: no mandatory preliminary workspace pin or isolated rehearsal, honest deferred native results, later manual reinstallations, and unchanged local validation/CI/review controls. This is Gate 1; approval permits the dependent Design revision, not a fabricated native pass or release.

## Planning review

Proposal/Requirements R1 was approved under digest `1f6c413f32b209cc764ef3d2ba92ab30412c01c080f02d8fbe8379d421fe8a2e`: “Aprovo a Proposal e os Requirements R1 de harness-marketplace-transition. Prepare somente o Design, sem implementar, alterar o workspace, migrar consumidores ou criar tag ou release.” That approval and subsequent Design/Tasks approvals remain historical. The latest owner instruction above authorizes preparing this simplification; R2 is presented for actual approval, not preapproved by the agent. Dependent Design R2 and Tasks R2 are marked superseded with original progress/evidence preserved.

The owner subsequently approved this presented Proposal/Requirements R2 in response to the explicit Gate 1 question with “Sim. Avance.” The unchanged digest is `e2cf501301bc4a8ef482631a8ad3d4f60a060a43087ceca9914537622340e773`. This advances the Design revision only; the current turn does not implement or perform remote/workspace/release operations.
