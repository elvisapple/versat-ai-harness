---
sdd_version: 3
change: harness-publication-readiness
tasks:
- id: TASK-001
  description: Reconcile the approved baseline, actual authority and restricted evidence setup
  requirements: [REQ-002, REQ-003, REQ-004, REQ-009, REQ-010, REQ-011, REQ-012]
  status: completed
- id: TASK-002
  description: Assess component rights, dependencies and the complete intended public surface
  requirements: [REQ-002, REQ-003, REQ-009, REQ-010, REQ-011]
  status: completed
- id: TASK-003
  description: Prepare and obtain review of concrete Apache candidates and reconcile active policy
  requirements: [REQ-001, REQ-002, REQ-008, REQ-010, REQ-011]
  status: completed
- id: TASK-004
  description: Prepare public contribution/reporting guidance and assess actual controls
  requirements: [REQ-006, REQ-007, REQ-008, REQ-009, REQ-011, REQ-012]
  status: completed
- id: TASK-005
  description: Assemble maintained multilingual guidance, the exact adoption candidate and operational handoff
  requirements: [REQ-001, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011]
  status: completed
- id: TASK-006
  description: Execute the bounded private package/client rehearsals and retained technical suites
  requirements: [REQ-004, REQ-005, REQ-009, REQ-011, REQ-012]
  status: in-progress
- id: TASK-007
  description: Complete current semantic reviews, all required checks and retained-contract assessment
  requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011,
    REQ-012]
  status: pending
- id: TASK-008
  description: Reconcile the final validation ledger and report preparation acceptance and remaining operations
  requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011,
    REQ-012]
  status: pending
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 41081278df433db671e12b7d442b78a446f792977cc976a37407a5113ee62443
    design: 007c4ba449c55cbdf7bd45e139973d678142d5a24bd5e18ed2c6aa53aec87aa0
  approval:
    source: User reply in this chat on 2026-11-13 to the explicit request to approve Tasks R1 while keeping implementation
      and publication suspended.
    quote: sim
    revision: 1
    digest: 3f412d99870c180bf629e21f5501787cf8dbcfebcf2304e1553c0d71f80f6eba
validation:
  plan_digest: 3f412d99870c180bf629e21f5501787cf8dbcfebcf2304e1553c0d71f80f6eba
  results: []
  assessments: []
  findings:
  - id: FIND-001
    source:
      local:
        requirement: REQ-005
        scenario: 1
    category: missing
    state: resolved
    evidence: docs/validation/harness-publication-readiness/personal-client-01/installation.json
    description: Required installation and six-case client rehearsal lack a confirmed disposable supported desktop
      context; help inspection is not a behavioral pass. All cases remain unverified and block preparation acceptance.
    tasks: [TASK-006, TASK-007, TASK-008]
    checks: [CHECK-004, CHECK-007, CHECK-008, CHECK-010]
    resolution: The user selected individual installation under their existing Versat account. Actual bundled-CLI
      installation succeeded into a separate personal cache with exact file equality and unchanged workspace plugin.
      This resolves the missing test context only; all behavioral cases still require current evidence.
closure: active
---

# Tasks

This is Tasks R1 for `harness-publication-readiness`, under approved Proposal/Requirements R1 and Design R1/ADR-0016. All eight tasks describe **future work** and remain pending. The current request authorizes preparation of this plan only. No task, private rehearsal, remote operation or implementation evidence collection begins before current Tasks approval and an explicit implementation request.

## Ordered implementation plan

### Baseline and evidence boundaries

- [x] TASK-001 — Reconcile the approved baseline, actual authority and restricted evidence setup.

**Depends on:** current Gate 3 approval and a subsequent explicit implementation instruction. Reconcile the actual instruction's scope before any action.

**Work:** reverify the three stage digests, source/provider anchors, source baseline and reviewed/annotated ADR identities; inspect any intervening source, tag, runtime or remote drift. Preserve the exact historical dossiers, frozen terms/approvals and other products. Reuse the established owner/reviewer capacities without inventing specialist qualifications or requesting unchanged decisions again. Confirm the existing private strategy repository and actual reviewer access before any authorized evidence write there; otherwise keep that dependency unverified and stop sensitive collection. Define the scrubbed input manifest, actual component/surface boundaries, output locations and private evidence references according to Design. Record the observed runtime and candidate-version availability without creating tags or changing consumers.

**Completion:** a dated, reviewable baseline identifies exact source/provider/runtime, actual authorization, immutable history, evidence access/status and named prerequisites. No confidential payload is stored in Harness. Missing prerequisite records identify affected downstream work and owner/exit condition; documenting an unavailable required setup does not mark the dependent work complete. No unapproved source/provider upgrade or scope expansion occurs.

**Checks supported:** CHECK-001, CHECK-002, CHECK-008, CHECK-010. Final check execution remains TASK-007; this task does not manufacture check results.

### Component and publication-surface assessment

- [x] TASK-002 — Assess component rights, dependencies and the complete intended public surface.

**Depends on:** TASK-001 and authorized access to the relevant evidence and read-only repository/service surfaces.

**Work:** refresh the H01 bounded source/dependency and owner-provenance evidence for the actual candidate delta. Inventory original, copied/generated material, code, templates/assets/docs, direct/transitive dependencies, distribution modes and notices. Assess the current intended tree, reachable history/refs, deleted historical files, releases/assets, LFS, fixtures, SDD/validation history, issues/PRs/comments/attachments, wiki/discussions/Pages where present, packages and CI logs/artifacts/caches and relevant integrations. Record actual scope, pagination/access limits, evidence, review capacity, date/method and dispositions privately. Produce only a scrubbed summary in Harness. Exercise the Design's missing-rights, incompatible-dependency, sensitive-history, unavailable-surface and drift cases with synthetic descriptions.

**Completion:** every required category has an observed-reviewed, observed-absent or inaccessible/unverified classification with attributable scope and owner. Actual component evidence is assessed; unknowns are not silently omitted. A completed negative assessment may legitimately record `defer`, but missing required review remains unverified and no public clearance is claimed. A conflict between confidentiality and immutable history triggers separately scoped remediation/replanning; no deletion, rewrite, mirror or destination change is performed by this task.

**Checks supported:** CHECK-001 and CHECK-002, with retained evidence reviewed through CHECK-008. Later source or remote drift requires re-assessment before final acceptance.

### Concrete licensing candidate and common policy

- [x] TASK-003 — Prepare and obtain review of concrete Apache candidates and reconcile active policy.

**Depends on:** TASK-001 and TASK-002's actual component evidence/dispositions. Missing rights can defer affected components; it cannot be bypassed by a wording approval.

**Work:** prepare official Apache-2.0 text, applicable notice/third-party candidates, exact covered-file/component inventory and review wrapper under `docs/licensing/candidates/apache-2.0/`. Record text provenance and hashes. Reconcile the existing index-resolved common licensing/contribution/security review contract with the approved public-Harness scope, preserving other product models and tool/project separation. Mark the old active proprietary candidate prospectively superseded through transparent status/routing changes; preserve its substantive clauses, frozen draft and actual historical approval. Present the concrete new text, scope and notices for the actual authorized review; record only the response actually received and its capacity/limits.

**Completion:** concrete candidate files and reviewable scope are present, real text review is recorded against exact hashes, unresolved rights/specialist questions remain explicit, and historical wording/approval is preserved. If actual required candidate approval is unavailable, this task remains blocked or incomplete; a draft, SDD gate or CODEOWNER assignment cannot replace it. No root license is applied, effective date invented, CLA/DCO introduced or third-party term silently overridden.

**Checks supported:** CHECK-001, CHECK-007 and CHECK-008. Concrete-text approval is distinct from implementation authorization and effective license adoption.

### Contribution, reporting and controls

- [x] TASK-004 — Prepare public contribution/reporting guidance and assess actual controls.

**Depends on:** TASK-001, TASK-002 and the concrete terms/routing from TASK-003. Work on safe drafts may proceed from the reviewed scope; completion waits for the applicable exact text/status.

**Work:** extend maintained contribution and confidential-reporting guidance for the Harness audience: repository/issue selection, provenance, fork/branch/PR, actual tool/project terms, setup, SDD gates, checks and maintainer review. Inspect actual controls read-only where accessible, including CODEOWNERS, branch protections/rulesets, required reviews/checks, workflow events, token permissions and fork secret boundaries. Reuse H02's actual scoped pilot/internal receipt and established responsibilities. Specify the Harness public PVR verification protocol, intended reporter/recipient scope and safe unavailable/denied/changed-route fallback. Add only thin root EN/PT/ES entry candidates if needed for repository discovery, keeping maintained guides canonical.

**Completion:** contribution/reporting routes and control observations have truthful scope and status, intended audience and next actions. No unknown setting is advertised as configured; no internal address, private evidence URL, vulnerability detail, invented endpoint/SLA or retention period is exported. Existing organization guidance and product adoption remain independent. Lack of a verified public Harness route remains an operational prerequisite rather than being represented as another repository's successful pilot.

**Checks supported:** CHECK-005, CHECK-006, CHECK-007 and CHECK-008. No permission/configuration change, channel activation, synthetic submission, external message or remote PR is part of this task; prepare any necessary operational action for separate authorization.

### Documentation, candidate and handoff assembly

- [x] TASK-005 — Assemble maintained multilingual guidance, the exact adoption candidate and operational handoff.

**Depends on:** TASK-001 through TASK-004. Actual text review and input evidence must be available before the final candidate is accepted for rehearsal.

**Work:** complete coherent EN/PT/ES README, product context, quickstart and affected guides using maintained canonical sources and safe public provenance. Preserve all unrelated workflows and organization-owned entry points; active public instructions must not require private recordings or strategy access. Update the ADR index/current architecture only to describe this implemented preparation boundary accurately, without claiming adoption/publication. Prepare the safe handoff, scrubbed immutable review-input manifest and exact adoption patch with explicit base, patch hash and proposed 0.4.0 metadata/license/notice/changelog changes. Keep the preparation root at 0.3.0, marketplace identity unchanged and all existing consumers untouched. Produce a disposable private checkout of the same repository root for the patch rehearsal; do not create a maintained mirror or copied Standards distribution.

**Completion:** every final candidate input is concrete, inspectable and internally consistent; the preparation source and private 0.4.0 candidate are distinct coherent trees. The handoff distinguishes prepared, reviewed, cleared/deferred, merged, licensed, visible, released and consumer-adopted states and defines the separately authorized operational sequence, drift checks and containment. Do not publish a command or endpoint as available before its actual observation. The patch is not applied to the live repository. Computed rehearsal tree identities belong in excluded run evidence, never a self-referential source manifest.

**Checks supported:** CHECK-003, CHECK-007, CHECK-008 and CHECK-010. Freeze final source/patch/input manifests before acceptance checks. Draft authoring may use bounded observations, but no rehearsal result is relabelled as a current pass after an input edit.

### Actual private package and client verification

- [ ] TASK-006 — Execute the bounded private package/client rehearsals and retained technical suites.

**Depends on:** TASK-005, the required actual preparation evidence, explicit authority for the private rehearsal within a disposable client context, and an available supported loading route. Existing user installations must not be replaced. Missing environment/observations remains unverified, not a mocked pass.

**Work:** execute CHECK-003 on the preparation and exact patched private candidate roots, including disposable manifest-version mismatch and legacy nested-path negative controls. Execute CHECK-004 on the selected observed Codex target with the six Design cases: actual install/load and first-use planning, missing provider/access, unavailable exact version, incompatible runtime/provider/resources, explicit synthetic-consumer update, and failed-update recovery. Reuse the maintained `new-intent` fixture/prompt and independent verification. Confirm only Proposal/Requirements and a real Gate 1 stop, no invented approval or product edit. Verify version-matched canonical resources and the previously verified compatible fallback; reject an unsafe downgrade of a v3 consumer. Execute CHECK-009's complete package/SDD/validator/execution suites on both roots with pinned dependencies.

**Completion:** original commands/actions, exact inputs/patch/tree/runtime, actual counts, observed success/failure and independent artifact checks are retained. The required unmodified package suites pass; expected failures belong only to the documented disposable negative controls. All required private client cases have real observations or remain explicitly unverified, blocking acceptance where required. No source-only file read substitutes for package installation, and no private rehearsal proves anonymous access.

**Bounds:** exactly the Design's one fresh native first-use invocation at most 600 seconds including independent verification; five other cases at most 300 seconds each; suite cap 2,400 seconds including setup/inspection. Monitor and interrupt at limits, retain failures/overruns and unknown telemetry, and do not automatically retry or select only successful attempts. A later correction/rerun is a separately recorded bounded attempt consistent with Design and the actual authorization. Fresh directories/native contexts share permissions and are not security isolation. No rehearsal or agent invocation occurs while merely preparing these Tasks.

**Checks executed:** CHECK-003, CHECK-004 and CHECK-009. Source/input changes after a run invalidate affected evidence; retain the original attempt and actually rerun under the approved bounds rather than changing its hash.

### Semantic acceptance and regression review

- [ ] TASK-007 — Complete current semantic reviews, all required checks and retained-contract assessment.

**Depends on:** TASK-001 through TASK-006 and final stable source, candidate and evidence revisions. Missing required private preparation checks cannot be bypassed by a comprehensive written report.

**Work:** perform CHECK-001, CHECK-002, CHECK-005, CHECK-006, CHECK-007, CHECK-008 and CHECK-010 on current inputs using their exact Design procedures. Independently inspect rights/text decisions, full-surface dispositions, actual controls, truthful reporting status, all affected translations/navigation and observed usage. Trace each of the 38 local scenarios and 72 retained obligations to current evidence; inspect the seven intentional supersessions and replacement behavior. Use immutable primary observations and actual external evidence revisions, not another mutable Tasks result or an old dossier's pass. Verify the final handoff and authority boundaries without requiring the delivery guard or this task's own completion as a check input.

**Completion:** all ten required checks have actual current outcomes and reproducible evidence. Required local preparation observations are available, and every applicable obligation has an individual semantic disposition with no unapproved exclusion. Correctable in-scope gaps are resolved under these approved tasks and affected checks rerun; new task content or broader changes reopen the appropriate gate. Unresolved preparation-acceptance findings, missing candidate review or unavailable required rehearsal remain fail/unverified, not completion. A real negative surface/control assessment may yield documented `defer`, but cannot claim public readiness or reclassify a missing required preparation check as future operational work. CHECK-006/010 verify the future operational protocol and honest pending state, not a fabricated future public report/access result.

**Checks executed/reconciled:** CHECK-001 through CHECK-010. All inputs were deliberately broad in the approved Design: changing an included file stales every affected snapshot, potentially all ten checks. Do not narrow scope or silently waive repeated observations to obtain freshness. Any needed bounded rerun follows TASK-006/Design limits and retains prior attempts.

### Ledger and preparation acceptance

- [ ] TASK-008 — Reconcile the final validation ledger and report preparation acceptance and remaining operations.

**Depends on:** TASK-007 and actual current passing preparation checks, with required review/observations and no unresolved documentary finding. This task does not depend on delivery validation or its own completion marker.

**Work:** populate `validation.plan_digest` with the approved current Tasks digest, one actual result per Design CHECK, observed runtime/context and matching before/after input snapshots. Record all 38 local and 72 retained assessments and stable findings/resolutions. Put safe records in the excluded validation output subtree and raw sensitive records only in the authorized restricted system. Independently verify current digests, source/ADR history, final candidate identity and truthful task checkboxes. Prepare the safe acceptance summary with the exact disposition and separate operational prerequisites. Reuse current CHECK-008/010 observations without requiring those checks to consume this mutable ledger.

**Completion:** the ledger is internally consistent, evidence is current, every requirement is assessed, all eight implementation tasks are truthfully completed and the preparation acceptance summary distinguishes a reviewed/deferred candidate from publish-ready status. Use the planning/implementation validator as appropriate to verify bookkeeping while this task is pending; do not require the delivery guard until after recording its actual completion. No source/patch/manifest changes are hidden as evidence updates. Missing required checks/review leaves this task incomplete; do not create synthetic passes to satisfy closure.

**Checks supported:** the already executed CHECK-008 and CHECK-010 plus canonical bookkeeping diagnostics. Ordinary delivery, archival and the final archive guard follow below after all implementation tasks are complete, eliminating a self-dependent final task.

## Dependencies and checkpoints

The critical sequence is baseline → actual inventory → concrete reviewed terms and contribution/reporting preparation → coherent candidate/guides/handoff → bounded private verification → current semantic/regression acceptance → complete ledger. TASK-003 and TASK-004 may develop drafts concurrently after their stated inputs exist, but neither can claim completion without its required actual evidence. The list defines dependencies, not authorization to delegate or execute now.

Before any later execution, reuse the exact source/provider and current approved digests. CHECKs, methods, input/output scopes, all 38/72 mappings, environment and attempt limits are unchanged from approved Design. The current preparation baseline remains `d61317d9220b002f0dc3aa606e18a62dd4230477`; no implicit update to newer source or to `latest` is authorized.

A known missing prerequisite discovered during execution becomes a blocked dependent task with the concrete owner and condition for resumption. Current planning has no unresolved task-plan decision. Future rights, environment and operational evidence are required work, not presumed facts.

## Evidence and freshness procedure

1. Prepare/freeze the actual source, candidate patch, scrubbed review-input manifest and relevant private/remote evidence revision before a real check. Use the canonical `--input-digest CHECK-NNN` helper before and after; an eligible pass requires matching values. Record known external-state/runtime identity separately and re-review on drift.
2. Preserve each actual attempt, original action/runner output, input identity, relevant runtime, method/date, actual reviewer and limitations. Store only safe summaries in `docs/validation/harness-publication-readiness/`; use the selected existing private strategy area for authorized sensitive records. An opaque reference or hash does not replace reviewer access.
3. Keep generated outputs outside the included source or in Design's explicitly excluded output subtree. Do not hash a manifest into itself, include another mutable check result as a prerequisite or move outputs into inputs. Immutable primary observations may support more than one check with attributable scope and context.
4. If a check reveals a necessary source/guide/patch correction, retain the failure, implement only within approved tasks after actual implementation authorization, refreeze inputs and perform the required current reruns. Preserve the bounded client-attempt rules; never update a historical hash to simulate re-execution.
5. After actual checks, record every local/retained assessment and stable finding; zero open findings and checked tasks do not substitute for missing mandatory results. Historical warnings, remote CI, actual review, merge and public operations remain separately reported facts.

## Documentary closure after implementation

This is the continuation procedure after TASK-008, not a task whose completion depends on its own final guard. It is not executed under the present planning-only instruction.

- With all tasks actually complete, current approvals and full current evidence, run the ordinary selected `--phase delivery --json` guard. A fail or unable-to-verify result withholds readiness; correct in scope or reopen the affected planning gate rather than weakening a requirement.
- When documentary closure is within the actual requested delivery scope, read/follow the canonical Archive workflow, move the unique dossier into `specs/archive/harness-publication-readiness/`, set `closure: prepared` and update necessary references. Preserve reviewed substantive content and original evidence attribution. If approved content changes beyond administrative exclusions, reopen the relevant gate.
- Recheck references and all affected inputs after the move. The current dossier is automatically excluded by the canonical snapshot contract, but changed incoming links or other included files still require actual current checks, including any affected candidate/rehearsal observations. Do not relabel an older candidate tree as final.
- Run selected `--phase delivery --require-archive --json` on the final unique archived dossier before presenting completed work for PR review. An ordinary delivery pass alone does not certify archival. Record the real final result separately.
- Commit/push/PR, marking a draft ready, review/merge and operational publication retain their actual scoped authority and required platform checks. No remote operation is implicitly authorized by approval of these Tasks. Planning-only work remains active and unimplemented.

## Separately authorized operational follow-up

The Design requires a later reviewed request to apply the exact candidate license/notice/metadata patch, change visibility, create the exact release/tag and activate or change controls/reporting. Before each action, recheck the actual candidate, source/remote-surface drift, tag availability, authority and prerequisites. Then verify actual anonymous acquisition, external installation/update/contribution, public-audience Harness report receipt/confidentiality and post-visibility controls. Consumer migrations remain independent exact-version decisions.

None of those operations is an implementation task above or a prerequisite that forces premature exposure before this preparation can merge. They remain mandatory evidence before claiming public availability or H03 delivery. A prepared/deferred assessment cannot waive them. No message/test report, control change, historical rewrite, destructive remediation, other-repository rollout or public announcement is authorized here. Any containment must preserve evidence and cannot promise to retract public copies or granted rights.

## Stop conditions and recovery

Stop dependent work for mismatched approvals/provider, substantive scope drift, absent actual implementation authority, unsafe/missing evidence access, missing required text review, unavailable required test context or an unresolved confidentiality/history conflict. Report exact blockers and ownership without re-asking unchanged prior decisions. Preserve unrelated work, existing releases and consumer configurations.

Routine authorized corrections use the same tasks and fresh evidence. New task content reopens Gate 3; broader design or requirements changes reopen the earliest affected gate. A request to prepare planning does not authorize a fix, rehearsal, license application or publication.

## Planning review

Tasks R1 is presented after the genuine Design R1/ADR-0016 approval. The user's exact instruction was: “Sim, aprovo o Design R1 e o ADR-0016. Prepare somente as Tasks, sem iniciar a implementação ou publicar.” Proposal/Requirements and Design digests remain unchanged; the ADR received only a status update and administrative acceptance annotation, preserving its reviewed decision bytes.

All eight tasks are pending and unchecked. Review is awaiting-approval with approval null; validation plan digest is null, all results/assessments/findings are empty, and closure is active. No task-plan blocker has been identified. Approval of Tasks completes planning only; the user's explicit prohibition on implementation/publication remains until a later scoped instruction. Current diagnostics validate this plan and the existing tools, not the ten future acceptance checks.

Preparation verification observed on 2026-11-13:

- Selected planning validation returned exit 0/pass with no findings or warnings. The declared contract retains 38 local scenarios, 72 regression obligations and all 12 requirements; their implementation outcomes remain unverified.
- The required `./scripts/validate/run.sh` returned exit 0 with portable package and SDD validation passing, 131 validator tests passing and 48 execution tests passing. It used the verified Python 3.11.4 environment and pinned dependencies. Existing historical legacy/v2 warnings remain; these are not new exemptions or proof of historical delivery.
- Independent inspection confirmed eight pending tasks and eight unchecked entries, coverage of all 12 requirements, empty implementation evidence, active closure, unchanged Proposal/Requirements bytes, unchanged approved stage digests and exact reconstruction of the originally reviewed ADR bytes. All 1,382 pre-existing tracked files remain byte-identical; only the five planning/ADR files are untracked. All 11 local Markdown links resolve and the five files have no trailing whitespace.
- Canonical Tasks R1 digest: `3f412d99870c180bf629e21f5501787cf8dbcfebcf2304e1553c0d71f80f6eba`. Gate 3 remains awaiting approval. These planning diagnostics do not execute or pass CHECK-001–CHECK-010, and authorize no implementation, remote operation or publication.

### Gate 3 approval — 2026-11-13

The user replied “sim” to the explicit question: “Você aprova as Tasks R1 para concluir o planejamento, mantendo a implementação e a publicação suspensas?” This approves Tasks R1 at canonical digest `3f412d99870c180bf629e21f5501787cf8dbcfebcf2304e1553c0d71f80f6eba`. Both approved upstream digests were reverified unchanged before recording this approval. Earlier awaiting-approval statements preserve the presentation history; the structured review is authoritative for the current state.

Planning is approved through Gate 3. All eight tasks remain pending and unchecked, implementation validation remains empty and closure remains active. This response does not authorize implementation, private rehearsals, publication or remote mutations. Execution requires a later explicit scoped instruction.

Post-approval diagnostics on 2026-11-13: selected planning and implementation-readiness validators both returned pass/exit 0 with no findings or warnings, confirming the current three approvals and absence of planning blockers. The implementation phase here is a read-only prerequisite check, not execution of any task. The mandatory `./scripts/validate/run.sh` returned exit 0 with 131 validator tests and 48 execution tests passing; existing historical legacy/v2 inventory warnings remain. No implementation CHECK result was created. The canonical Tasks digest remains unchanged.

## Progress

### Current private test context — 2026-11-13

The user asked to use their own Versat user with an individual plugin installation. This concrete environment choice is accepted for the private rehearsal: the actual selected bundled CLI installed `versat-ai-harness@versat-internal` 0.4.0 into a separate personal cache, while every workspace 0.3.0 file remained unchanged. No external account is needed for this preparatory test; external-user/public-access observations remain mandatory later. FIND-001's context prerequisite is resolved, not its unexecuted behavior checks. TASK-006 is now in progress.

Guides now describe the actually observed installation route and its limits. Prior source-bound results and task ledger are preserved in `personal-client-01/prior-tasks.md` and original run files. Current results are cleared pending real reruns on the changed guide/source revision; no old hash is relabelled. Earlier progress and pending-context statements below are historical.


### Actual authority and approvals — 2026-11-13

The user explicitly authorized implementation: “Pode iniciar a implementação das Tasks R1 aprovadas, seguindo o SDD, sem publicar nem tornar o repositório público.” The subsequent actual replies “Autorizar inventário privado” and “Aprovar o candidato R1” resolve the prior sensitive-collection and concrete-text approval dependencies. Exact approved Apache package digest: `894308c5f1921f28677d55d39b9bf5fb386467dc652e5dca5908d54756fe9f48`; all 16 bound files remain unchanged. These replies do not authorize publication, effective root adoption or unseen future scope. Earlier planning-only observations and attempt-01 records are historical.

| Task | Current completion evidence or blocker |
|---|---|
| TASK-001 | Complete: current source/provider, actual authority, selected restricted-system privacy/reviewer access and observed runtime reconciled; `attempt-01/baseline.json`. |
| TASK-002 | Complete as a bounded assessment with `defer`: 16 categories, initial tree/remote inventory, all 1,069 reachable blobs and 56 run-log archives/111 entries assessed with explicit missing package/cache/external content and confidential-history dispositions. HPR-PRIVATE-01 binds actual methods, reviewer capacity, limits and owner/exit conditions. It does not clear publication or claim inaccessible content reviewed. |
| TASK-003 | Complete: exact official Apache candidate, notices/scope/inventory and actual R1 text approval recorded. Installed license bytes match all seven retained upstream texts. Former proprietary clauses/frozen approval preserved; active status and common policy reconciled. Rights/surface defer remains separate from text acceptance. |
| TASK-004 | Complete for preparation: maintained EN/PT/ES contribution/reporting instructions, thin root entries and actual read-only control observations. Public reporting and ineffective/inaccessible controls remain explicit operational prerequisites, with no messages or changes. |
| TASK-005 | Complete for candidate assembly: coherent multilingual purpose/setup/recovery/first-use guidance, architecture/ADR index, immutable scrubbed inputs, nine-file adoption patch with exact preimages/base/hash and operational runbook. A private checkout of the same repository root received the patch; preparation remains 0.3.0 without root LICENSE/NOTICE. Candidate tests pass; actual installation behavior remains a TASK-006 prerequisite, not an advertised capability. |
| TASK-006 | Blocked: CHECK-003 and both CHECK-009 suites passed, but the required supported disposable desktop installation/context is not confirmed. CHECK-004 is unverified; zero installer or native scenario invocations. User test-context question remains pending. No user's installation was replaced or source-only reading relabelled as installation. |
| TASK-007 | Pending: final semantic and retained-contract acceptance depends on the required client observations. No missing check is waived. |
| TASK-008 | Pending: only actual partial results and FIND-001 are recorded; all 38/72 final assessments and preparation acceptance remain incomplete. |

Run evidence is under `docs/validation/harness-publication-readiness/attempt-02/`; the [safe handoff](../../../docs/handoffs/harness-publication-readiness/README.md) separates observed/deferred preparation from later operations. Initial and expanded private collection attempts are preserved in the selected restricted area. The approved Design/Tasks content and all three stage digests remain unchanged. No commit, push, PR, merge, release, visibility change, channel message, consumer migration or destructive remediation occurred.

## Validation evidence

Current recorded results: CHECK-003 pass with real private patch application, both package roots and negative version/legacy-path controls; CHECK-009 pass with 131 validator plus 48 execution tests in each root; CHECK-004 unverified after observed client-prerequisite inspection. Each record binds actual equal before/after input digests. No other acceptance check or final scenario assessment is claimed.

Development review also checked 377 local Markdown links, no selected private-reference patterns in changed active community guides, all 16 exact approved candidate files and seven installed dependency-license text matches. These observations do not substitute for actual client use, full semantic acceptance, rights clearance, public access or remote CI. Historical legacy/v2 inventory warnings remain. The existing frozen dossiers, prior approval records, installed consumers and active root version metadata are unchanged.

The current selected implementation guard returns fail/exit 1 with `ACCEPTANCE_GAP` for FIND-001 and zero stale results; see `attempt-02/current-gate.json`. The earlier two-root test runs passed before this gap was entered in the ledger. Their retained results do not mean the current acceptance gate passes.

FIND-001 remains open. Resolve the concrete disposable test-context dependency, then run the Design's real bounded six-case rehearsal with current inputs and proceed to TASK-007/008. Source changes require affected check reruns; original attempts remain evidence. Preparation is not delivery-ready.

## Delivery

Closure remains active. Five preparation tasks are completed; required runtime evidence and final acceptance remain outstanding. No archive move or completed-preparation claim is made. Publication and visibility changes remain prohibited; root-license adoption and remote operations need their own actual scoped authority. The next permitted action is resolving the disposable client test context and continuing the approved Tasks without weakening their checks.
