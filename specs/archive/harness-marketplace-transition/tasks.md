---
sdd_version: 3
change: harness-marketplace-transition
tasks:
- id: TASK-001
  description: Reconcile the retained candidate and record the approved two-user main-tracking disposition.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-006
  status: completed
- id: TASK-002
  description: Verify retained marketplace tests and close any deterministic package-resource coverage gap.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-003
  description: Align active EN/PT/ES guidance with source delivery and later manual reinstallation.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-004
  description: Prepare and review the deferred-native register and separate per-user acceptance records.
  requirements:
  - REQ-003
  - REQ-004
  - REQ-006
  status: completed
- id: TASK-005
  description: Review the bounded handoff and reconcile historical findings under the approved scope decision.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-006
  description: Collect final local suite evidence and complete source acceptance and delivery documentation.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
review:
  revision: 3
  state: approved
  blockers: []
  upstream:
    proposal: e2cf501301bc4a8ef482631a8ad3d4f60a060a43087ceca9914537622340e773
    design: 6d8be8c8d53182f0b6e7a3672f1c441a1764623a48d7be31ec1b17c06b9dc17b
  approval:
    source: 'Current conversation: explicit Tasks R3 approval and local implementation instruction'
    quote: Aprovo as Tasks R3. Prossiga com a implementação local, sem alterar o workspace, migrar consumidores
      ou criar tag ou release.
    revision: 3
    digest: a96c4d2681b6c9eb1a889d1e0ecd31ff9d9367d880f3d72ba6b5ddcb1d1b5e8c
validation:
  plan_digest: a96c4d2681b6c9eb1a889d1e0ecd31ff9d9367d880f3d72ba6b5ddcb1d1b5e8c
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-001/pr43-01/report.json
    revision: 'Local working tree incorporating PR #43 on a7d80172b3aeb054464a7ea3075d0ce6af4f223d; pr43-01 snapshots'
    input_digest_before: 691fdfe7d25f5679eaeaf0a97b62800260325608b9464bf1f464b2fce8a5373d
    input_digest_after: 691fdfe7d25f5679eaeaf0a97b62800260325608b9464bf1f464b2fce8a5373d
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; PyYAML 6.0.2; jsonschema 4.23.0
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-002/pr43-01/report.json
    revision: 'Local working tree incorporating PR #43 on a7d80172b3aeb054464a7ea3075d0ce6af4f223d; pr43-01 snapshots'
    input_digest_before: 2cc9c0545c90084d60c5067b71590b64eff44c9a9b679e974e11aa03bfcc5ee0
    input_digest_after: 2cc9c0545c90084d60c5067b71590b64eff44c9a9b679e974e11aa03bfcc5ee0
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; PyYAML 6.0.2; jsonschema 4.23.0
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-003/pr43-01/report.json
    revision: 'Local working tree incorporating PR #43 on a7d80172b3aeb054464a7ea3075d0ce6af4f223d; pr43-01 snapshots'
    input_digest_before: 0037236323f2ec17f0cf9a43ab094ce6fef0f31d2241f820a55ccf179021154a
    input_digest_after: 0037236323f2ec17f0cf9a43ab094ce6fef0f31d2241f820a55ccf179021154a
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; PyYAML 6.0.2; jsonschema 4.23.0
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-004/pr43-01/report.json
    revision: 'Local working tree incorporating PR #43 on a7d80172b3aeb054464a7ea3075d0ce6af4f223d; pr43-01 snapshots'
    input_digest_before: af926acd67c014f6b6cceb8bb1ea3d4974b6dc579bd56019cd1eb6b609418a44
    input_digest_after: af926acd67c014f6b6cceb8bb1ea3d4974b6dc579bd56019cd1eb6b609418a44
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; PyYAML 6.0.2; jsonschema 4.23.0
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-005/pr43-01/report.json
    revision: 'Local working tree incorporating PR #43 on a7d80172b3aeb054464a7ea3075d0ce6af4f223d; pr43-01 snapshots'
    input_digest_before: 6ec9e40ff6772c24c786dc6697c9b9bc756d03324755d45886e5df626eea1ed5
    input_digest_after: 6ec9e40ff6772c24c786dc6697c9b9bc756d03324755d45886e5df626eea1ed5
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; PyYAML 6.0.2; jsonschema 4.23.0
      observed: true
  - check: CHECK-006
    result: pass
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/report.json
    revision: 'Local working tree incorporating PR #43 on a7d80172b3aeb054464a7ea3075d0ce6af4f223d; pr43-01 snapshots'
    input_digest_before: 0e215377b116e3f26e24e86266c045b072b46d8e86fea2e976711acd1af35af8
    input_digest_after: 0e215377b116e3f26e24e86266c045b072b46d8e86fea2e976711acd1af35af8
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; PyYAML 6.0.2; jsonschema 4.23.0
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Actual catalog comparison permits only name/display delta; manifests, URL, policy, legal files
      and canonical root unchanged; positive/negative tests pass.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Guide and catalog identify versat-ai-harness@versat and legacy versat-internal without an automatic
      alias; wrong legacy identity is rejected in new-package tests.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: 'Read-only 2026-11-19 refs show v0.4.0 absent; exact metadata remains consistent. Guide requires
      subsequent reviewed version if occupied, never retag. PR #43 is incorporated locally; remote delivery remains
      separately authorized.'
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Current input records the exact owner two-user quote, earlier main report and later manual reinstall
      intent; no audit or Everton individual result is inferred.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Dated personal 0.4.0, managed cached 0.3.0 and project exact locks remain differentiated; effective
      session and Source/Path/sync/IDs explicitly unknown.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Guide and reviewed disposition accept possible main-sync interruption/manual repair without preliminary
      pin; additional affected users stop activation and trigger reassessment.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Fourteen deterministic marketplace/package cases and full 204-test suites pass; truthful EN/PT/ES
      guidance verified. No VM/account/native-rehearsal prerequisite recreated.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Seven native rows remain executed=false/unverified, including same source, collision and provider
      selection. No alias/upgrade/managed continuity success claimed.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Separate pending Elvis/Everton acceptance records require exact identity/version, one effective
      provider/resources and synthetic Skill draft or actual failure/recovery. This is review of instructions, not
      executed acceptance.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 4
    result: pass
    checks:
    - CHECK-003
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: All seven prior native cases and independent external cases are retained as unverified follow-up;
      guide records only future observed cases and separates merge from installation.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Exact source/package/project records and current locks preserved; guide explicitly warns that main
      synchronization can interrupt availability and absent v0.4.0 is not a verified recovery pair.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-003
    - CHECK-004
    - CHECK-005
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Manual prerequisites, client-supported route verification and per-user postchecks documented without
      untested CLI instructions. Cache/database/implicit-lock edits forbidden.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Guide assigns later manual work to Elvis/Everton and separately scopes admin intervention. No automated
      install, workspace change, generic pluginId or delete/reimport workaround executed.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 4
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Cleanup remains optional separately authorized work; failed reinstall/unknown managed continuity
      remain operational unknowns, not a native success inferred from source review.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: pass
    checks:
    - CHECK-005
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Actual active EN/PT/ES diff, links/anchors and translated scope reviewed. Historical ledger, execution-01,
      command blocks and original 17-file candidate verified unchanged.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Existing 12 identity/label/ref/plugin regression tests retained, with 2 resource-path cases; Plugin
      validator and complete 156+48 suites passed. Native compatibility still unknown.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 3
    result: pass
    checks:
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Earlier 17-file candidate corrections incorporated and original archive-selection failure retained.
      Complete local source evidence now supports independent delivery guards; results of those gates are recorded
      separately, without rewriting the earlier failure.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Canonical resources/manifests/version/ref and exact project lock unchanged; copied-package tests
      validate all five Skill paths and detect removed index. No provider migration.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    - CHECK-005
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Rights/license/CODEOWNERS/workflows and historical evidence unchanged on approved baseline. Active
      guides preserve public protected-main/internal-control/end-of-pause facts and external pending cases.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: 'Guide separates preparation, protected integration, exact release and manual reinstall; required
      CI and nonauthor approval remain mandatory. PR #43 quality/format/changelog and suite checks passed locally;
      no remote mutation or release authority inferred.'
  - obligation:
      regression:
        impact: 2
        scenario: 2
    result: pass
    checks: &id001
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: EN/PT/ES living guidance and historical evidence reviewed; independent product/consumer boundaries
      remain unchanged.
  - obligation:
      regression:
        impact: 2
        scenario: 3
    result: pass
    checks: *id001
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: EN/PT/ES living guidance and historical evidence reviewed; independent product/consumer boundaries
      remain unchanged.
  - obligation:
      regression:
        impact: 3
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Copied package resolves matching canonical files and all Skill relative links from each of the
      five directories; removed index detected. No duplicated Standards or resource relocation; native execution
      remains unverified.
  - obligation:
      regression:
        impact: 3
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Copied package resolves matching canonical files and all Skill relative links from each of the
      five directories; removed index detected. No duplicated Standards or resource relocation; native execution
      remains unverified.
  - obligation:
      regression:
        impact: 3
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Copied package resolves matching canonical files and all Skill relative links from each of the
      five directories; removed index detected. No duplicated Standards or resource relocation; native execution
      remains unverified.
  - obligation:
      regression:
        impact: 4
        scenario: 1
    result: pass
    checks: &id002
    - CHECK-002
    - CHECK-004
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Repository catalog retains exact v0.4.0 package selection and policy; reviewed manual handoff separates
      reported scope, available exact source, supported user/admin actions and failure handling. Managed outcomes
      not claimed.
  - obligation:
      regression:
        impact: 4
        scenario: 2
    result: pass
    checks: *id002
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Repository catalog retains exact v0.4.0 package selection and policy; reviewed manual handoff separates
      reported scope, available exact source, supported user/admin actions and failure handling. Managed outcomes
      not claimed.
  - obligation:
      regression:
        impact: 4
        scenario: 3
    result: pass
    checks: *id002
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    explanation: Repository catalog retains exact v0.4.0 package selection and policy; reviewed manual handoff separates
      reported scope, available exact source, supported user/admin actions and failure handling. Managed outcomes
      not claimed.
  findings:
  - id: FIND-001
    source:
      plan: Managed main tracking and unresolved synchronization exposure
    category: missing
    state: resolved
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    description: Owner reports the managed source follows main; exact sync and approved containment/disposition
      are missing. Rename activation/merge remains blocked.
    tasks:
    - TASK-005
    - TASK-006
    checks:
    - CHECK-002
    - CHECK-003
    - CHECK-004
    resolution: Original source-delivery prerequisite superseded by approved Proposal/Requirements R2 and Design
      R3 plus genuine execution-02 CHECK-002/003/004 document reviews. Reported two-user main exposure/manual repair
      is accepted; no pin, isolated rehearsal or reinstall is claimed. Original observations remain in history;
      operational native/managed unknowns remain unverified in inputs/transition-r2.json.
  - id: FIND-002
    source:
      plan: Supported isolated native rehearsal unavailable
    category: missing
    state: resolved
    evidence: docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md
    description: Owner confirms no disposable native environment. Seven client compatibility/recovery scenarios
      and evidence-based handoff remain unverified.
    tasks:
    - TASK-004
    - TASK-005
    - TASK-006
    checks:
    - CHECK-002
    - CHECK-003
    - CHECK-004
    resolution: Original source-delivery prerequisite superseded by approved Proposal/Requirements R2 and Design
      R3 plus genuine execution-02 CHECK-002/003/004 document reviews. Reported two-user main exposure/manual repair
      is accepted; no pin, isolated rehearsal or reinstall is claimed. Original observations remain in history;
      operational native/managed unknowns remain unverified in inputs/transition-r2.json.
closure: prepared
---

# Tasks

Proposal/Requirements R2 and Design R3 are approved. This turn prepares Tasks R3 only. The six tasks below describe the remaining reconciliation and verification against that approved scope; all are pending and unchecked until execution is explicitly authorized. No source implementation is undone or claimed newly completed.

- [x] TASK-001 — Reconcile the retained candidate and record the approved two-user main-tracking disposition.
- [x] TASK-002 — Verify retained marketplace tests and close any deterministic package-resource coverage gap.
- [x] TASK-003 — Align active EN/PT/ES guidance with source delivery and later manual reinstallation.
- [x] TASK-004 — Prepare and review the deferred-native register and separate per-user acceptance records.
- [x] TASK-005 — Review the bounded handoff and reconcile historical findings under the approved scope decision.
- [x] TASK-006 — Collect final local suite evidence and complete source acceptance and delivery documentation.

## Retained work and evidence

The previous implementation already changed the catalog to `versat` / `Versat Plugins`, retained plugin identity, added 12 marketplace tests and reconciled the 17-file documentary candidate. Its local suites passed 191 tests. The exact [superseded Tasks R2 ledger](../../../docs/validation/harness-marketplace-transition/history/tasks-r2.txt) preserves the three completed tasks, three blocked tasks, six observed check records, 28 assessments, two findings and actual approval history. The original execution-01 reports and earlier candidate remain unchanged.

R3 does not reset that history. Its new pending status means the revised task completion conditions have not yet been executed/reviewed. Reuse unchanged work after checking applicability; do not recreate the catalog rename or discard useful tests. Keep old results bound to old inputs and methods. Current R3 validation arrays are empty because no check under this new Tasks plan has run; preserve the former ledger rather than re-labeling its unverified native results as passes.

## Ordered work and completion conditions

### TASK-001 — Candidate and two-user disposition

Dependencies: approved Tasks R3 and explicit applicable local implementation authority. Verify the pinned provider anchors and source baseline before use.

Work: reconcile the retained local candidate and exact-version choice. Recheck remote tag/version state read-only before delivery; if v0.4.0 already exists, stop for a reviewed subsequent version, never retag. Add the sanitized `docs/validation/harness-marketplace-transition/inputs/transition-r2.json` specified by Design. Attribute the owner's reports that only Elvis/Everton use the Harness, managed source follows main, and they will reinstall later. Record the approved possible interruption/manual-repair tradeoff, unknown actual Source/Path/sync/managed-ID fields and the stop condition if another affected user is found. Keep raw identifiers private.

Completion: CHECK-002 has genuine reviewed decision evidence and exact-version eligibility. Unknown sync details are explicit and do not recreate the superseded preliminary pin requirement. No workspace configuration is changed. Source/package and project-provider distinctions remain clear; two-user scope is a report, not a member audit or Everton's individual test result.

Requirements: REQ-001, REQ-002, REQ-004, REQ-006. Check: CHECK-002; disposition also supplies CHECK-003/004.

### TASK-002 — Retained deterministic package coverage

Dependencies: TASK-001 establishes the source/version baseline; no native environment is required.

Work: review and retain the existing two-field catalog delta, validator assertions and 12 marketplace regression tests. Confirm plugin name, URL, policy, legal files, manifests, exact version/ref and canonical root resources are unchanged. Inspect maintained coverage of resource resolution from all five Skill directories in a disposable package copy. Reuse adequate tests; add only missing meaningful path-resolution/missing-resource cases under maintained suites if required by Design. Do not claim fixture directories are security isolation, a native installation or a supervised Skill invocation.

Completion: CHECK-001 passes actual positive and rejecting cases plus adequate canonical resource-path coverage. Temporary fixture state is restored; no consumer files or caches are changed. Record whether the final test count changes and why. No alias bypass, generic pluginId workaround, workflow/branch-protection or validator-policy weakening is introduced.

Requirements: REQ-001, REQ-003, REQ-005, REQ-006. Checks: CHECK-001 and the later complete suite in CHECK-006.

### TASK-003 — Truthful active guidance

Dependencies: TASK-001 approved scope/version disposition and TASK-002 confirmed source contracts. Can prepare a draft alongside TASK-004, then review the final guide and register together; neither depends on future actual reinstalls.

Work: update active README/quickstart/setup/transition/release/handoff guidance in EN/PT/ES to the two-user source-delivery decision. Remove obsolete mandatory pre-merge pinning and isolated-environment instructions only from active guidance. Explain that main synchronization may expose the changed catalog, exact package-tag availability is separate, reinstallations happen manually later, and native commands/continuity remain unverified until exercised. Retain historical command blocks, old approvals, original candidate and failure records. Preserve exact references and project locks; no silent latest or downgrade.

Completion: CHECK-005 reviews the actual diff, translated meaning and affected links/anchors. Guides state prerequisites and observable per-user outcomes without promising transparent upgrade or completed native testing. Refer to the TASK-004 deferred register and TASK-005 stop/recovery rules. Document preparation does not require a native installation or new user account.

Requirements: REQ-001, REQ-003, REQ-004, REQ-005, REQ-006. Checks: CHECK-005 and shared guidance inputs for CHECK-003/004.

### TASK-004 — Deferred-native and per-user acceptance review

Dependencies: TASK-001 decision record and TASK-003 draft guidance; the final guide/register are reviewed together.

Work: retain all seven former native scenarios as pending/unverified operational follow-up: fresh discovery/resources, legacy retained, same Git URL handling, name collision, two providers/one effective provider, unavailable exact ref, and recovery. Prepare separate pending outcome records for Elvis and Everton: identity, exact version, effective provider/resources, a representative Skill action on synthetic data, and error/recovery disposition. State what each genuine observation could establish, without inventing a command route or results. A later reinstall may cover only the scenarios actually encountered; do not require simulation of all seven before source delivery.

Completion: CHECK-003 passes a genuine review of the honest deferral and concrete later acceptance/stop criteria. Its pass means documentary review, not native compatibility. No native case or per-user record is marked passed or not-applicable without actual evidence. No VM/container/account provisioning, real-profile install, workspace operation or credential copy is required or executed by this task.

Requirements: REQ-003, REQ-004, REQ-006. Check: CHECK-003.

### TASK-005 — Handoff and historical finding disposition

Dependencies: TASK-001/003/004 reviewed decision and guidance; TASK-002 source check. This consumes document and deterministic evidence, not successful future reinstallations.

Work: review manual handoff decisions for success and failure, preserving compatible provider/project records and one intended provider. Stop on unsupported/destructive operations, unavailable exact package, additional affected users or unapproved administrative changes. Treat managed IDs and sync behavior as unverified; do not copy local behavior into a managed success claim. Reconcile original FIND-001 (main tracking) and FIND-002 (missing isolated runtime) with approved Proposal R2/Design R3 and the actual new CHECK-002/003/004 review reports. Preserve those IDs and their former observations in history; any new disposition says their old pre-merge requirement was superseded for the bounded two-user scope, not that pinning, native rehearsal or reinstallations occurred. Keep underlying operational unknowns in the pending register.

Completion: CHECK-004 passes the real handoff review; the changed finding disposition is attributable to the approved scope and current review evidence. Every source-acceptance obligation mapped to CHECK-001 through CHECK-005 has a genuine disposition or concrete open gap; CHECK-006 remains assigned to TASK-006. Do not close findings solely because planning was approved, and do not require post-merge native outcomes as pre-merge task completion.

Requirements: REQ-002, REQ-003, REQ-004, REQ-005, REQ-006. Checks: CHECK-002/003/004/005 and review of their actual evidence.

### TASK-006 — Local suite and complete source acceptance

Dependencies: TASK-001 through TASK-005 complete against the revised criteria and current inputs. Planning approval is not an execution result.

Work: capture CHECK-006's declared input snapshot, run the Plugin validator and both complete maintained unittest discovery suites (`tests/validators` and `tests/execution`, `test_*.py`) with the verified interpreter and `PYTHONDONTWRITEBYTECODE=1`, and capture the after-input snapshot. Record actual command exits/logs/counts/runtime and matching input digests. Use new execution-02 locations for all revised checks. Assess all 20 local scenarios and eight retained regression obligations against the approved Design mapping and current results; preserve actual failures and rerun affected checks after changed inputs. Prepare final source-delivery documentation and review summary.

Completion: genuine local suites and all six required source checks pass on final inputs, all 28 source obligations have valid acceptance evidence and the transfer documentation is prepared. No current result comes from copying an old pass onto a new method/digest. Pending native/external observations remain operational follow-up and are not falsely assessed as observed source-test success. This task does not claim archive eligibility, remote CI, release, merge or manual reinstallation.

Requirements: all REQ-001 through REQ-006. Check: CHECK-006 and complete consistency of CHECK-001 through CHECK-005.

## Mandatory documentary delivery checks after task completion

After all revised tasks and actual source acceptance are complete, prepare the unique dossier under `specs/archive/harness-marketplace-transition/` with `closure: prepared` for documentary validation. Check references and input freshness after the move. Run the unchanged full `scripts/validate/run.sh --baseline <reviewed-base-sha> --require-archive` using the verified Python environment, and selected `validators/sdd/validate.py --root . --change harness-marketplace-transition --phase delivery --require-archive --json` using the same interpreter.

Both gates must genuinely pass before claiming submission readiness. They consume previously recorded local evidence and completed work; CHECK-006 does not require its own future closure report. On failure, preserve the report and reopen affected work/evidence rather than bypassing a guard. No preliminary pin or native rehearsal is recreated by this closure step. Preserve a portable local patch and exact review summary; this does not publish a PR or release.

## Separate operational follow-up

- An authorized PR still requires actual successful `structural-validation` CI and eligible nonauthor CODEOWNER approval on its current revision before merge. Local test/documentary passes waive neither control.
- Recheck target-version availability and whether the bounded two-user scope still holds near delivery. Additional affected users require reassessment. The approved main-tracking tradeoff does not authorize direct workspace mutation or a global write freeze.
- Exact tag/release creation, workspace changes, agent-driven installs/uninstalls, consumer migrations and cleanup each retain their applicable scoped authority. Source merge does not create an absent package tag.
- Elvis and Everton reinstall manually later using an available supported exact package, with separate observed outcomes. Problems requiring administrative or destructive work receive concrete handling then; no generic delete/reimport or cache/database manipulation is prescribed now.
- Native and external fork/reporting/installation cases remain pending until actual observations. Source archival or merge does not silently close them.

## Planning review

The owner approved Proposal/Requirements R2 with “Sim. Avance.” and Design R3 with “sim”, each replying to the explicit stage approval question. Their exact current digests are recorded upstream. Tasks R3 awaits Gate 3 approval. The earlier Tasks R2 approval and substantive digest `61b7c6c5226f98795c740d251e36f95e31ffa3e33b5089b05b5cd8c0d435bf8d`, real progress and evidence are preserved in the linked history snapshot; R3 does not retroactively rewrite their meaning.

Approval of these Tasks completes the revised planning stage. The developer may combine that approval with explicit local implementation authority; this turn itself prepares Tasks only. No remote/workspace/tag/release authority is inferred.

The owner subsequently approved Tasks R3 and authorized local implementation: “Aprovo as Tasks R3. Prossiga com a implementação local, sem alterar o workspace, migrar consumidores ou criar tag ou release.” The exact approved digest remains `a96c4d2681b6c9eb1a889d1e0ecd31ff9d9367d880f3d72ba6b5ddcb1d1b5e8c`. This later instruction supersedes the preparation-only status above, with operational exclusions preserved.

The owner subsequently authorized: “Prossiga com a incorporação das mudanças da PR #43 à candidata local e valide as novas regras de qualidade, sem alterar o workspace, migrar consumidores, fazer push ou criar tag ou release.” This is integration/validation authority, not a new remote delivery approval.

## Progress

All six Tasks R3 remain completed. Under the subsequent explicit local integration instruction, PR #43 is incorporated at a7d80172b3aeb054464a7ea3075d0ce6af4f223d. The original candidate and ledger are preserved. The only content conflict (CHANGELOG) was resolved by retaining both changes and adding the required new Unreleased note. Both affected Python files were formatted without AST changes; PR #43 policy, workflow and validator files are unchanged. The exact original SDD provider remains valid because its implementation is byte-identical; new Coding/Python Standards are applied from the integrated index.

## Validation evidence

All six current checks pass on final integrated before/after snapshots. Complete suites passed 156 validator and 48 execution tests (204 total), including 14 marketplace tests and the upstream quality regressions. Ruff 0.14.14 lint/format and the new Unreleased rule pass after a preserved initial formatting failure. The 20 local scenarios and eight regression obligations were reassessed. See [integration review](../../../docs/validation/harness-marketplace-transition/execution-02/check-006/pr43-01/review.md). Historical execution-02 reports and [prior ledger](../../../docs/validation/harness-marketplace-transition/history/tasks-r3-before-pr43.txt) retain their actual old inputs. Native/external cases and both manual reinstalls remain pending.

## Delivery

The unique archived dossier retains closure: prepared. Local integrated source now uses trusted baseline a7d80172b3aeb054464a7ea3075d0ce6af4f223d; the full unchanged PR #43 entry point and selected archive gate are verified independently after these genuine check records. No remote CI, human approval, merge or release is claimed. No source commit, push, workspace change, consumer migration, native install, tag or release was performed. Required CI and eligible nonauthor review remain mandatory for a later authorized PR.
