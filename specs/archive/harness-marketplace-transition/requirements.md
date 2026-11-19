---
sdd_version: 3
change: harness-marketplace-transition
requirements:
- id: REQ-001
  statement: Prepare a scoped marketplace identity transition to versat while preserving the Harness plugin and
    package.
  acceptance:
  - The proposed catalog changes only its identity from versat-internal to versat and its display label from Versat
    Internal Plugins to Versat Plugins; plugin name versat-ai-harness, repository URL, canonical package root, legal
    text and installation/authentication policy are retained.
  - The proposed local composite identity is versat-ai-harness@versat; versat-ai-harness@versat-internal remains
    identified as the legacy identity, not an automatic alias.
  - The target is the unreleased 0.4.0 candidate only while no such tag exists. Recheck before execution; if already
    released, choose a subsequent reviewed version rather than retagging or modifying the released package.
- id: REQ-002
  statement: Bound this transition to the two reported current users and explicitly accept a moving catalog source
    without requiring a preliminary workspace pin.
  acceptance:
  - Record the owner report that only Elvis and Everton currently use the Harness, the earlier report that the managed
    catalog tracks main, and their intended later manual reinstallation. This is reported scope, not an independent
    member/access audit or evidence of each user completing a migration.
  - Distinguish local personal 0.4.0, managed cached 0.3.0 and exact project/provider locks; preserve current observations
    and mark unknown effective sessions, managed IDs and sync details unknown. A wider fleet inventory is not a
    source-delivery prerequisite within this bounded two-user scope.
  - 'The source update may proceed toward protected integration without first pinning or pausing the workspace:
    main synchronization may expose the new catalog before manual reinstallation, and temporary unavailability or
    manual repair is an explicit proposed tradeoff. Source/Path/sync uncertainty alone does not block source delivery
    for these two users. If another affected user is identified, stop activation and reassess that expanded scope.'
- id: REQ-003
  statement: Keep native compatibility and recovery observations pending for the later manual reinstallations instead
    of requiring a disposable rehearsal before source delivery.
  acceptance:
  - Before source submission, require current deterministic package/identity checks, maintained regression suites
    and truthful guidance. A new VM, container, test OS account or completed seven-case native rehearsal is not
    required for this two-user source delivery.
  - Duplicate-source registration, name collisions, qualified enablement and managed identity transfer remain unverified
    until observed. The update promises no automatic alias, transparent upgrade or managed-ID continuity. Do not
    label these deferred observations passed or not-applicable.
  - After a separately scoped manual reinstallation, each operator verifies exact plugin identity/version, one effective
    provider, matching canonical resources and a representative Skill operation. On failure, stop and preserve or
    reselect a verified compatible provider/project pair through supported controls; record recovery or unresolved
    failure rather than assuming success.
  - Retain the unexecuted isolated scenarios and deferred external-user tests as operational follow-up, distinct
    from pre-merge source acceptance. Record reinstallation and actual native outcomes only after they occur; source
    merge is not installation or external acceptance.
- id: REQ-004
  statement: Prepare a bounded manual reinstallation handoff for Elvis and Everton without automatically changing
    their installations or workspace.
  acceptance:
  - Preserve existing files, exact tags, project locks and historical evidence during source preparation. Do not
    claim that installations following main will remain unchanged or available. Keep a recoverable compatible source/package/project
    record; current main pointing to an unreleased tag is not a verified recovery installation.
  - Document the intended new identity and manual reinstallation prerequisites, supported-client verification and
    per-user post-install checks. Native commands not yet exercised remain unverified. Do not rename caches, edit
    installation databases or silently update consumer locks to simulate a migration.
  - The users will perform the later manual reinstallations; no agent-driven install/uninstall, workspace import/ref/policy
    change or managed plugin deletion is included here. Any necessary administrator intervention is scoped separately
    when its concrete supported action is known. Do not use pluginId or delete/reimport as a generic identity workaround.
  - Legacy cleanup is optional later work under the affected owner/admin authority. Do not delete a workspace marketplace
    merely to rename it. Failed reinstallation or unproven managed continuity remains an operational issue for the
    affected installation rather than retroactive evidence that source acceptance passed native tests.
- id: REQ-005
  statement: Provide truthful multilingual distribution guidance and mechanical checks for the selected identity.
  acceptance:
  - Future implementation aligns active EN/PT/ES setup and release guidance with the new and legacy identities,
    actual migration scope and pending checks; historical approvals, old release notes, observed logs and private
    evidence are not mass-renamed.
  - Maintained validation enforces the intended marketplace identity/display, plugin identity and exact ref agreement,
    including wrong-name negative cases. Retain the implemented regression tests and run the full required suite
    on the final source; deterministic validation does not prove native reinstallation.
  - Reconcile the existing 0.4.0 documentary candidate with this governed delivery before PR submission; preserve
    its original archive-selection failure and obtain actual delivery checks after approved implementation. Creating
    a Proposal alone does not resolve that failure.
- id: REQ-006
  statement: Preserve existing package, consumer and authorization boundaries throughout the transition.
  acceptance:
  - Keep canonical root resources, matching manifests/version and exact release selection. Reuse applicable existing
    checks; changes to marketplace identity do not silently change a consumer lockfile, Standards snapshot or active
    SDD provider.
  - Preserve prior reviewed rights, public main protection, completed internal controls and the end of the opening
    write pause. External fork/CI, security-report receipt/confidentiality and native external installation/update/recovery
    remain explicitly pending.
  - Separate preparation, protected integration, versioned release and manual reinstallation. Required CI and eligible
    nonauthor review must pass on the actual PR revision before merge. Workspace changes, agent-driven installation,
    consumer migration, tag/release and remote push/PR/merge require their concrete applicable authority; this replanning
    step performs none of them.
---

# Requirements

## Actors and context

The owner reports Elvis and Everton as the only current Harness users and directs later manual reinstallation. Maintainers prepare source/tests; each user controls the later personal installation, and a workspace administrator controls any managed operation. No individual test result or approval is attributed to Everton by this report.

## Scope and supersession

R2 retains six requirement IDs and 20 acceptance positions. REQ-001 and the package/legal boundaries remain unchanged. REQ-002 replaces the mandatory pre-merge pin/containment and broad inventory requirement with an explicit two-user moving-source disposition. REQ-003 replaces pre-delivery isolated rehearsal with deferred native observations and real per-user post-install checks. REQ-004 replaces a transparent-preservation rollout expectation with a manual reinstallation handoff. REQ-005/006 retain meaningful tests, honest documentation, exact versions, mandatory CI/review and separately authorized operations.

## Constraints and assumptions

Temporary interruption or manual repair may occur after source synchronization. Successful native behavior is not established by accepting that delivery tradeoff. An exact package tag must exist before advertising versioned installation; do not silently choose latest or create a tag to satisfy a test. Unknown additional users reopen the bounded-scope decision. The previously observed 191-test pass is preserved with its actual inputs, not reused automatically after changes.
