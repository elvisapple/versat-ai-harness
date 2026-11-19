# Marketplace transition

[English](marketplace-transition.md) | [Português](marketplace-transition.pt.md) | [Español](marketplace-transition.es.md)

The local 0.4.0 candidate changes the catalog to `versat` / `Versat Plugins`. The plugin stays `versat-ai-harness`; the intended local qualified key is `versat-ai-harness@versat`. The legacy key `versat-ai-harness@versat-internal` is not an automatic alias. Source preparation is not integration, a release or an installation. The exact `v0.4.0` tag was still absent on 2026-11-19.

## Bounded source delivery

The owner reports that only Elvis and Everton currently use the Harness, the managed catalog follows `main`, and both will reinstall manually later. This is reported scope, not a member audit or either person's installation result. Under the approved decision, no preliminary workspace pin/pause or disposable native rehearsal is required for source delivery. Synchronization can expose the changed catalog before reinstallation and may cause temporary interruption or require manual repair. Actual Source/Path/sync settings and managed IDs remain unverified. If another affected user is identified, stop activation and reassess scope.

Source acceptance requires deterministic package checks, complete maintained suites and truthful guidance. Future integration still requires successful CI and eligible nonauthor CODEOWNER approval on the actual PR revision. Review changes since the recorded source baseline before submission. Local acceptance does not waive those controls. A tag/release requires separate authority; recheck v0.4.0 availability and never retag an existing release.

## Later manual reinstallation

Read [workspace setup](workspace-setup.md) and the [candidate notes](../../releases/0.4.0-candidate.md). Elvis and Everton perform their own later reinstallations. No installation, workspace change or consumer migration is performed by this source preparation.

1. Record the current catalog reference separately from the exact plugin package reference, qualified identity/version, effective provider and compatible project lock/snapshots. Keep private paths and managed identifiers in restricted evidence, without credentials. Earlier personal 0.4.0 and managed cached 0.3.0 observations do not establish the effective provider in a new session.
2. Verify an available supported exact package and its canonical resources before attempting installation. A catalog revision selecting an absent package tag is insufficient; current main selecting unreleased v0.4.0 is not a verified recovery pair. Preserve a known compatible source/package/project record. Never silently select `latest` or downgrade active SDD v3 to an incompatible provider.
3. Check the installed client's supported controls/help for registration, identity selection and recovery. Transition command routes, same-Git-URL registration, name collision and managed identity continuity are unverified. Historical legacy commands are not current transition instructions. Stop if the required route is unsupported or needs administrator action; scope that concrete action separately.
4. After an actual manual reinstallation, record the returned identity and exact version and confirm one intended effective provider. From a synthetic project, ask that provider to locate the five Skills and their matching canonical resources, then use `versat-sdd` to prepare a small Proposal/Requirements draft without implementation. Expected result: a draft from the selected matching provider, stopped at its planning gate, or an explicit recorded prerequisite/failure. This representative action remains unexecuted here.
5. Record Elvis's and Everton's outcomes separately: qualified identity, exact version, effective provider/resources, representative Skill result and error/recovery disposition. Source acceptance and one person's result do not establish the other person's success.

## Failure and recovery

On unavailable exact ref, collision, ambiguous providers, missing resources or incompatible runtime, stop the affected installation. Preserve or reselect a verified compatible provider/project pair using supported controls; record recovery or unresolved failure. If no compatible recovery is verified, leave it unresolved instead of inventing a successful rollback. Do not rename caches, edit installation databases, copy credentials, change project locks as a side effect, or use `pluginId` or delete/reimport as generic workarounds.

Workspace import/ref/policy changes, managed deletion and automated installs need their own applicable authority. Local qualified identity does not prove managed sharing, roles or ID continuity. Optional legacy cleanup comes later under the affected owner/admin authority, after dependencies and recovery are checked; deleting a marketplace merely to rename it is not part of this handoff.

## Deferred observations

The [pending register](../../validation/harness-marketplace-transition/inputs/transition-r2.json) keeps seven native scenarios unverified: fresh discovery/resources; legacy retained; same Git URL handling; name collision; two providers/one effective provider; unavailable exact ref; failure recovery. A later reinstall records only scenarios actually observed, without requiring simulation of all seven before source delivery. No VM, container or test account is provisioned here; disposable fixture paths prove packaged resource resolution, not security isolation or native execution.

External fork/CI, private security-report receipt/confidentiality and external native installation/update/recovery remain independently pending. Neither local validation, documentary archival nor source merge closes those observations.
