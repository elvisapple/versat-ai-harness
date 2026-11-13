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
  status: completed
- id: TASK-007
  description: Complete current semantic reviews, all required checks and retained-contract assessment
  requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011,
    REQ-012]
  status: completed
- id: TASK-008
  description: Reconcile the final validation ledger and report preparation acceptance and remaining operations
  requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011,
    REQ-012]
  status: completed
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
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/check-001.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/check-002.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/package-check.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/harness-publication-readiness/personal-client-04/client-check.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-005
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/check-005.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-006
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/check-006.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-007
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/check-007.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-008
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/check-008.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-009
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/full-suites.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  - check: CHECK-010
    result: pass
    evidence: docs/validation/harness-publication-readiness/attempt-04/check-010.json
    revision: 2026-11-13 final private preparation; source 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_before: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    input_digest_after: 7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4
    context:
      execution: local
      environment: macOS arm64; Python 3.11.4; pinned validation dependencies; actual personal Codex private rehearsal
        and attributable documentary review
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks: [CHECK-001]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Apache scope identifies replacement of former sections 2–4; approved exact 16-file package and
      frozen proprietary evidence remain separately attributable.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks: [CHECK-001]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: LICENSE/NOTICE/SCOPE cover eligible first-party code, docs and templates; upstream texts preserved;
      commercial use and forks conditional on terms; unrelated destination material independent.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 3
    result: pass
    checks: [CHECK-001]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Actual user answer binds R1 digest and declared company-approver capacity. No effective date, specialist
      clearance, extra CLA/DCO or root license inferred.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks: [CHECK-001, CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Private component assessment reuses bounded H01 owner declaration and seven exact upstream texts.
      Current candidate manifest includes authorized documentation delta; installed packages remain separately distributed.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks: [CHECK-001, CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Missing grants, incompatible bundling and missing reviewer walkthroughs defer to owner and actual
      evidence; no scan or authorship substitutes for clearance.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks: [CHECK-001, CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: HPR-PRIVATE-01 bound revision records source, date/method, declared capacity, dependency mode and
      limitations; sensitive source evidence stays outside Harness.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks: [CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Sixteen categories cover current tree, all reachable blobs, refs, service content, CI and controls
      with observed/inaccessible distinctions.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks: [CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Sensitive historical-reference findings remain privately retained and defer exposure; unchanged
      original history is not cleared by current-guide cleanup.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks: [CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Unavailable packages/cache/external payloads remain unverified. Runbook stops on drift and requires
      separately governed remediation/destination changes.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks: [CHECK-003, CHECK-004, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Both roots pass package validation; private patch coherently selects 0.4.0 and all five installed
      Skills resolve canonical same-root resources.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks: [CHECK-003, CHECK-004, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Preparation metadata remains 0.3.0 and marketplace identity unchanged; actual installer rejects
      unavailable v0.4.0. No tag or automatic consumer update.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 3
    result: pass
    checks: [CHECK-003, CHECK-004, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Synthetic compatible provider/config pair migrated explicitly, unsafe old-provider selection refused;
      prior verified state retained on failed personal update.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: pass
    checks: [CHECK-004, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Actual personal installation plus fresh native scenario produced only Proposal/Requirements, null
      approval and Gate 1 stop; independent validator and file comparison passed.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: pass
    checks: [CHECK-004, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Real wrapper rejects missing provider/resources and wrong pinned provider; actual client rejects
      missing ref/source and preserves installed cache/config.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 3
    result: pass
    checks: [CHECK-004, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Synthetic old/new full commits and Standards locks recorded; full wrapper succeeds before and after
      explicit migration, failed update retains verified candidate pair.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 4
    result: pass
    checks: [CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Runbook requires future intended external user without private membership; same-user rehearsal
      explicitly provides no anonymous/public acceptance.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 1
    result: pass
    checks: [CHECK-005]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Contribution route covers real target/issue, provenance, terms, setup, SDD, fork/branch/PR/checks
      and maintainer decisions; synthetic local patch exercised without submission.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 2
    result: pass
    checks: [CHECK-005]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Reviewed CODEOWNERS and read-only PR workflow against actual private control observations; unprotected
      main/inaccessible rules remain operational blockers.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 3
    result: pass
    checks: [CHECK-005]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: No controls or external PR changed; runbook requires separate scope and post-visibility verification.
      Missing rights/control walkthroughs prevent acceptance.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 1
    result: pass
    checks: [CHECK-006]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Original H02 pilot/internal-receipt files byte-identical; existing owner and CODEOWNERS retained,
      no transferred public proof.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 2
    result: pass
    checks: [CHECK-006]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: PVR is intended, not active-verified; protocol specifies actual destination/audience/recipients,
      non-sensitive marker, receipt and unauthorized-viewer exclusion under separate authority.
  - obligation:
      local:
        requirement: REQ-007
        scenario: 3
    result: pass
    checks: [CHECK-006]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Unavailable/denied/changed-route walkthroughs retain unverified state and non-sensitive instructions
      fallback; no internal address, exploit payload or invented SLA.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 1
    result: pass
    checks: [CHECK-002, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Reviewed EN/PT/ES purpose, ownership, status, setup, results and recovery; relative navigation/anchors
      checked and original Issue 22/social-environment context retained.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 2
    result: pass
    checks: [CHECK-002, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: New maintained guides remove private recording dependencies and use safe optional provenance; immutable
      internal history remains a separate exposure blocker.
  - obligation:
      local:
        requirement: REQ-008
        scenario: 3
    result: pass
    checks: [CHECK-002, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Actual private installer/wrapper/native observations match documented steps; translations preserve
      gates and limits; maintained guides stay outside movable dossier.
  - obligation:
      local:
        requirement: REQ-009
        scenario: 1
    result: pass
    checks: [CHECK-010, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Exact private candidate manifest, patch, text review and private assessment references distinguish
      preparation, defer, adoption, release and migration states.
  - obligation:
      local:
        requirement: REQ-009
        scenario: 2
    result: pass
    checks: [CHECK-010, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Rights/surface/control unknowns produce explicit defer, while all required local checks need actual
      current observations; no H03/public-ready claim.
  - obligation:
      local:
        requirement: REQ-009
        scenario: 3
    result: pass
    checks: [CHECK-010, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Runbook sequences drift, authority, review, adoption, visibility, external verification and recovery
      separately; no task requires its own merge/publication.
  - obligation:
      local:
        requirement: REQ-009
        scenario: 4
    result: pass
    checks: [CHECK-010, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Failure/containment walkthrough preserves evidence and requires bounded authority; runbook states
      public copies/forks/grants cannot be recalled by reverting visibility.
  - obligation:
      local:
        requirement: REQ-010
        scenario: 1
    result: pass
    checks: [CHECK-008, CHECK-001, CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: All archived dossiers, frozen terms and governance records byte-identical to approved base; old
      results retained without relabelling current acceptance.
  - obligation:
      local:
        requirement: REQ-010
        scenario: 2
    result: pass
    checks: [CHECK-008, CHECK-001, CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Active candidate status and maintained guidance route to actual Apache R1 review; original proprietary
      clauses and frozen approval remain reconstructable/preserved.
  - obligation:
      local:
        requirement: REQ-010
        scenario: 3
    result: pass
    checks: [CHECK-008, CHECK-001, CHECK-002]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Private source/history inventory records exposure concerns; new safe reports use opaque HPR identity,
      no destructive cleanup or confidential evidence export.
  - obligation:
      local:
        requirement: REQ-011
        scenario: 1
    result: pass
    checks: [CHECK-008, CHECK-003, CHECK-005, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Standards and handoff retain independent Platform/Workspace/Discover/CRM terms and per-repository
      evidence; no other product changed.
  - obligation:
      local:
        requirement: REQ-011
        scenario: 2
    result: pass
    checks: [CHECK-008, CHECK-003, CHECK-005, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Existing organization route/forms/repository precedence preserved; no cross-repository edit or
      activation; missing access retains usable target-owned guidance.
  - obligation:
      local:
        requirement: REQ-011
        scenario: 3
    result: pass
    checks: [CHECK-008, CHECK-003, CHECK-005, CHECK-007]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: No dependency engine, language CI, infrastructure, business or hiring work introduced; canonical
      Skills/SDD/enforcement/templates unchanged and full suites retained.
  - obligation:
      local:
        requirement: REQ-012
        scenario: 1
    result: pass
    checks: [CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Historical Gate 1 artifact/approval provenance remains the original event, not reenacted; current
      changes follow later explicit implementation authority.
  - obligation:
      local:
        requirement: REQ-012
        scenario: 2
    result: pass
    checks: [CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: All three approved stage digests unchanged; actual implementation request follows Tasks approval,
      and exact candidate text received its own later approval.
  - obligation:
      local:
        requirement: REQ-012
        scenario: 3
    result: pass
    checks: [CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: No source commit/push/PR, merge, root adoption, release, visibility, channel message or real consumer
      update; only authorized private test adapters and synthetic local commits.
  - obligation:
      regression:
        impact: 1
        scenario: 1
    result: pass
    checks: [CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Licensing Standard retains independent Apache intent and evidence for Platform/Workspace.
  - obligation:
      regression:
        impact: 1
        scenario: 3
    result: pass
    checks: [CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Runbook and root metadata separate policy/text from effective adoption and operations.
  - obligation:
      regression:
        impact: 3
        scenario: 1
    result: pass
    checks: [CHECK-001, CHECK-002, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Component assessment and seven dependency records identify versions, declared ownership, notices
      and nonbundled mode.
  - obligation:
      regression:
        impact: 3
        scenario: 2
    result: pass
    checks: [CHECK-001, CHECK-002, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Private assessment and negative grant/dependency/reviewer cases explicitly defer with owner and
      exit conditions.
  - obligation:
      regression:
        impact: 3
        scenario: 3
    result: pass
    checks: [CHECK-001, CHECK-002, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Sixteen categories include full reachable history and remote limitations, beyond current-tree scan.
  - obligation:
      regression:
        impact: 5
        scenario: 2
    result: pass
    checks: [CHECK-001, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Actual user text approval binds exact R1 bytes; CODEOWNERS/SDD approval remain insufficient and
      specialist limits explicit.
  - obligation:
      regression:
        impact: 6
        scenario: 1
    result: pass
    checks: [CHECK-001, CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Owner-declared capacity, actual candidate response, Codex technical review and missing specialist
      verification are separately recorded.
  - obligation:
      regression:
        impact: 6
        scenario: 2
    result: pass
    checks: [CHECK-001, CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: No other product adopted or blocked by this preparation; P01/P03 remain independent.
  - obligation:
      regression:
        impact: 6
        scenario: 3
    result: pass
    checks: [CHECK-001, CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Unknown reviewer grants/controls remain defer; no unconfirmed role promoted to clearance.
  - obligation:
      regression:
        impact: 7
        scenario: 1
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Index and Skill bytes unchanged; changed policy stays in canonical Standards.
  - obligation:
      regression:
        impact: 7
        scenario: 2
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Installed candidate equality and resource checks cover Standards, SDD, templates, schemas and validators.
  - obligation:
      regression:
        impact: 7
        scenario: 3
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Exact source metadata unchanged; synthetic migration is explicit and no real consumer repinned.
  - obligation:
      regression:
        impact: 8
        scenario: 1
    result: pass
    checks: [CHECK-008, CHECK-009, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Original planning-only event and dossier preserved; later user implementation instruction is distinct
      authority.
  - obligation:
      regression:
        impact: 8
        scenario: 2
    result: pass
    checks: [CHECK-008, CHECK-009, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Text acceptance, preparation, adoption and publication remain separate; inaccessible surfaces explicitly
      unverified.
  - obligation:
      regression:
        impact: 8
        scenario: 3
    result: pass
    checks: [CHECK-008, CHECK-009, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Current 38/72 review, multilingual checks, actual client cases and full package/test execution
      supply new evidence; historical pass alone not reused.
  - obligation:
      regression:
        impact: 9
        scenario: 1
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Delivered Issue 22/PR history retained; existing guides extended without reopening delivered H02.
  - obligation:
      regression:
        impact: 9
        scenario: 2
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Maintained contribution steps cover target/issues/provenance/setup/checks and real linkage, with
      no invented Story.
  - obligation:
      regression:
        impact: 9
        scenario: 3
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Repository precedence and organization-owned forms/identity remain intact; no organization edits.
  - obligation:
      regression:
        impact: 9
        scenario: 4
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Guide links canonical setup/SDD/validation/language sources instead of duplicating policy.
  - obligation:
      regression:
        impact: 10
        scenario: 1
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Contributor without private access can use target-owned instructions; Harness availability is qualified
      and no private evidence required.
  - obligation:
      regression:
        impact: 10
        scenario: 2
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Workspace route and fallback retained; private candidate install is distinct from future public
      replacement.
  - obligation:
      regression:
        impact: 10
        scenario: 3
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Active community docs contain no internal recordings/strategy evidence; actual access remains separate
      from instructions.
  - obligation:
      regression:
        impact: 11
        scenario: 1
    result: pass
    checks: [CHECK-001, CHECK-005, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Provenance/rights/notices and maintainer responsibilities specified; synthetic local contribution
      demonstrates reviewable change.
  - obligation:
      regression:
        impact: 11
        scenario: 3
    result: pass
    checks: [CHECK-001, CHECK-005, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Missing grants/terms/review prevent acceptance; no extra agreement or invented grant added.
  - obligation:
      regression:
        impact: 13
        scenario: 1
    result: pass
    checks: [CHECK-006, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Public Harness PVR remains unverified until separately authorized configuration/access/marker/receipt
      checks.
  - obligation:
      regression:
        impact: 13
        scenario: 2
    result: pass
    checks: [CHECK-006, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Guides prohibit public exploit/credential/customer payloads and offer confidential-instructions
      request.
  - obligation:
      regression:
        impact: 13
        scenario: 3
    result: pass
    checks: [CHECK-006, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Unavailable-route example discloses no internal address, invented endpoint, SLA or activation.
  - obligation:
      regression:
        impact: 13
        scenario: 4
    result: pass
    checks: [CHECK-006, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: No report or channel/access mutation made; original planning-only authority event preserved.
  - obligation:
      regression:
        impact: 14
        scenario: 1
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: All language siblings preserve permissions, gates, access limits and recovery/status semantics.
  - obligation:
      regression:
        impact: 14
        scenario: 2
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Local links/anchors verified; canonical English references remain English, private optional provenance
      qualified.
  - obligation:
      regression:
        impact: 14
        scenario: 3
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: No documentation automation or multilingual CI added; Issues 23/26 scope remains separate.
  - obligation:
      regression:
        impact: 15
        scenario: 1
    result: pass
    checks: [CHECK-006, CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Common guidance does not adopt other products or complete H03 distribution.
  - obligation:
      regression:
        impact: 15
        scenario: 2
    result: pass
    checks: [CHECK-006, CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: No organization routing activation; existing fallback retained pending independent work.
  - obligation:
      regression:
        impact: 15
        scenario: 3
    result: pass
    checks: [CHECK-006, CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Current semantic review combines actual private client evidence and honest reporting status; no
      structural-only public receipt claim.
  - obligation:
      regression:
        impact: 15
        scenario: 4
    result: pass
    checks: [CHECK-006, CHECK-008, CHECK-010]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Original Gate 1 preserved; actual later implementation authority and text approval distinguish
      current allowed preparation.
  - obligation:
      regression:
        impact: 17
        scenario: 2
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: All five supported Skills present in candidate and verified installed copy.
  - obligation:
      regression:
        impact: 17
        scenario: 3
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Codex compatibility manifest passes maintained validator and actual installation.
  - obligation:
      regression:
        impact: 18
        scenario: 1
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Canonical directories exist at package root in source, patched copy and installed candidate.
  - obligation:
      regression:
        impact: 18
        scenario: 2
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Actual fresh installed Skill uses same-root Standards and SDD; exact resource hashes verified.
  - obligation:
      regression:
        impact: 18
        scenario: 3
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Skills unchanged; no embedded copied Standards subtree introduced.
  - obligation:
      regression:
        impact: 19
        scenario: 1
    result: pass
    checks: [CHECK-003, CHECK-004, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Root repository marketplace includes Harness and keeps versat-internal identity.
  - obligation:
      regression:
        impact: 19
        scenario: 2
    result: pass
    checks: [CHECK-003, CHECK-004, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Preparation ref v0.3.0 preserved; private patch proposes exact v0.4.0 without publishing it.
  - obligation:
      regression:
        impact: 19
        scenario: 3
    result: pass
    checks: [CHECK-003, CHECK-004, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Workspace instructions retained and individual private test route documented with observed commands.
  - obligation:
      regression:
        impact: 20
        scenario: 1
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Older ADRs byte-identical; accepted ADR-0016 adds preparation boundary without changing package
      history.
  - obligation:
      regression:
        impact: 20
        scenario: 2
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: ADR-0011 remains root-package authority; ADR-0016 explicitly retains it.
  - obligation:
      regression:
        impact: 20
        scenario: 3
    result: pass
    checks: [CHECK-003, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Disposable mismatched version and legacy nested package both rejected by unchanged package validator.
  - obligation:
      regression:
        impact: 21
        scenario: 1
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: README retains purpose, accountable team, lifecycle/version boundaries and actual validation command
      while extending audience.
  - obligation:
      regression:
        impact: 21
        scenario: 2
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: README local navigation resolves to maintained quickstart/product/guides/SDD reference.
  - obligation:
      regression:
        impact: 21
        scenario: 3
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Preparation/release/consumer distinctions remain discoverable; no unreleased source capability
      advertised as old installed release.
  - obligation:
      regression:
        impact: 22
        scenario: 1
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Fresh installed-provider scenario identifies stable change Proposal/Requirements and actual Gate
      1 stop.
  - obligation:
      regression:
        impact: 22
        scenario: 2
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Missing provider/ref/resources fail explicitly; guide directs prerequisite recovery without implicit
      latest selection.
  - obligation:
      regression:
        impact: 22
        scenario: 3
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Quickstart retains focused canonical guide navigation; existing organization route not replaced
      with a fictitious path.
  - obligation:
      regression:
        impact: 23
        scenario: 1
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: All existing workflow guide siblings retained; only setup/audience/policy pointers and optional
      recording dependencies changed.
  - obligation:
      regression:
        impact: 23
        scenario: 2
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Specialized guide and canonical source bytes retained rather than copied into a new manual.
  - obligation:
      regression:
        impact: 23
        scenario: 3
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: SDD/PR guides retain three approvals, explicit execution, archive-before-delivery and observed
      review/merge boundaries.
  - obligation:
      regression:
        impact: 23
        scenario: 4
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Source-only v3/execution and unsupported public outcomes remain explicitly limited; no automatic
      upgrades claimed.
  - obligation:
      regression:
        impact: 24
        scenario: 1
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Overview retains Versat onboarding persona, problem, solution, ownership and optional Issue 22
      provenance alongside external audience.
  - obligation:
      regression:
        impact: 24
        scenario: 2
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Alternatives/scalability and social/environmental limits retained; market/pricing/returns explicitly
      unestablished.
  - obligation:
      regression:
        impact: 24
        scenario: 3
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Productivity/defect benefits remain hypotheses with onboarding/support measurement; unreviewed
      recordings not promoted to instructions.
  - obligation:
      regression:
        impact: 25
        scenario: 1
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: English pages have PT/ES siblings, including README/quickstart/overview/feature guides.
  - obligation:
      regression:
        impact: 25
        scenario: 2
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Language switches and localized guide links resolve; English-only canonical technical references
      remain explicit.
  - obligation:
      regression:
        impact: 25
        scenario: 3
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Commands/identifiers/gates/access/recovery and exact-version status compared across languages.
  - obligation:
      regression:
        impact: 25
        scenario: 4
    result: pass
    checks: [CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Organization-owned EN/PT/ES entry files untouched; no unsupported cross-repository consolidation
      claim.
  - obligation:
      regression:
        impact: 27
        scenario: 2
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Actual final private installation and failure/migration/recovery outcomes compared to documented
      actions.
  - obligation:
      regression:
        impact: 27
        scenario: 3
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Current relative links/anchors plus semantic parity and complete suites support acceptance, beyond
      structural checks alone.
  - obligation:
      regression:
        impact: 27
        scenario: 4
    result: pass
    checks: [CHECK-004, CHECK-007, CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Living guidance stays in normal docs paths; operational navigation does not depend on moving current
      dossier.
  - obligation:
      regression:
        impact: 28
        scenario: 1
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Existing maintained destinations remain usable; no second organization manual or new cross-repository
      rewrite.
  - obligation:
      regression:
        impact: 28
        scenario: 2
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Organization identity/participation/forms/local checks unchanged and target-specific precedence
      explicit.
  - obligation:
      regression:
        impact: 28
        scenario: 3
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Public fallback explains target repository/forms/instructions without requiring internal Harness
      access.
  - obligation:
      regression:
        impact: 28
        scenario: 4
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Documented actual bundled CLI and Gate 1 observation support limited claims; canonical gates/archive
      preserved.
  - obligation:
      regression:
        impact: 28
        scenario: 6
    result: pass
    checks: [CHECK-005, CHECK-007, CHECK-008]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: Existing organization route retained; unknown future destination cannot be advertised as completed
      consolidation.
  - obligation:
      regression:
        impact: 30
        scenario: 0
    result: pass
    checks: [CHECK-008, CHECK-009]
    evidence: docs/validation/harness-publication-readiness/attempt-04/semantic-assessments.json
    explanation: The exact maintained validation entry point and full deterministic suites remain unchanged and
      execute on both roots; package checks are not legal or public-access clearance.
  findings:
  - id: FIND-001
    source:
      local:
        requirement: REQ-005
        scenario: 1
    category: missing
    state: resolved
    evidence: docs/validation/harness-publication-readiness/personal-client-04/client-check.json
    description: Required installation and six-case client rehearsal lack a confirmed disposable supported desktop
      context; help inspection is not a behavioral pass. All cases remain unverified and block preparation acceptance.
    tasks: [TASK-006, TASK-007, TASK-008]
    checks: [CHECK-004]
    resolution: The user selected personal installation under the existing Versat account. Actual same-version installed
      files and all six bounded cases passed with source and patched-root before/after snapshots. The original context
      finding is resolved by its direct CHECK-004 evidence; CHECK-007/008/010 remain required and now separately
      pass. Earlier failure/unknown records are preserved; no external-access or publication claim.
closure: prepared
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

- [x] TASK-006 — Execute the bounded private package/client rehearsals and retained technical suites.

**Depends on:** TASK-005, the required actual preparation evidence, explicit authority for the private rehearsal within a disposable client context, and an available supported loading route. Existing user installations must not be replaced. Missing environment/observations remains unverified, not a mocked pass.

**Work:** execute CHECK-003 on the preparation and exact patched private candidate roots, including disposable manifest-version mismatch and legacy nested-path negative controls. Execute CHECK-004 on the selected observed Codex target with the six Design cases: actual install/load and first-use planning, missing provider/access, unavailable exact version, incompatible runtime/provider/resources, explicit synthetic-consumer update, and failed-update recovery. Reuse the maintained `new-intent` fixture/prompt and independent verification. Confirm only Proposal/Requirements and a real Gate 1 stop, no invented approval or product edit. Verify version-matched canonical resources and the previously verified compatible fallback; reject an unsafe downgrade of a v3 consumer. Execute CHECK-009's complete package/SDD/validator/execution suites on both roots with pinned dependencies.

**Completion:** original commands/actions, exact inputs/patch/tree/runtime, actual counts, observed success/failure and independent artifact checks are retained. The required unmodified package suites pass; expected failures belong only to the documented disposable negative controls. All required private client cases have real observations or remain explicitly unverified, blocking acceptance where required. No source-only file read substitutes for package installation, and no private rehearsal proves anonymous access.

**Bounds:** exactly the Design's one fresh native first-use invocation at most 600 seconds including independent verification; five other cases at most 300 seconds each; suite cap 2,400 seconds including setup/inspection. Monitor and interrupt at limits, retain failures/overruns and unknown telemetry, and do not automatically retry or select only successful attempts. A later correction/rerun is a separately recorded bounded attempt consistent with Design and the actual authorization. Fresh directories/native contexts share permissions and are not security isolation. No rehearsal or agent invocation occurs while merely preparing these Tasks.

**Checks executed:** CHECK-003, CHECK-004 and CHECK-009. Source/input changes after a run invalidate affected evidence; retain the original attempt and actually rerun under the approved bounds rather than changing its hash.

### Semantic acceptance and regression review

- [x] TASK-007 — Complete current semantic reviews, all required checks and retained-contract assessment.

**Depends on:** TASK-001 through TASK-006 and final stable source, candidate and evidence revisions. Missing required private preparation checks cannot be bypassed by a comprehensive written report.

**Work:** perform CHECK-001, CHECK-002, CHECK-005, CHECK-006, CHECK-007, CHECK-008 and CHECK-010 on current inputs using their exact Design procedures. Independently inspect rights/text decisions, full-surface dispositions, actual controls, truthful reporting status, all affected translations/navigation and observed usage. Trace each of the 38 local scenarios and 72 retained obligations to current evidence; inspect the seven intentional supersessions and replacement behavior. Use immutable primary observations and actual external evidence revisions, not another mutable Tasks result or an old dossier's pass. Verify the final handoff and authority boundaries without requiring the delivery guard or this task's own completion as a check input.

**Completion:** all ten required checks have actual current outcomes and reproducible evidence. Required local preparation observations are available, and every applicable obligation has an individual semantic disposition with no unapproved exclusion. Correctable in-scope gaps are resolved under these approved tasks and affected checks rerun; new task content or broader changes reopen the appropriate gate. Unresolved preparation-acceptance findings, missing candidate review or unavailable required rehearsal remain fail/unverified, not completion. A real negative surface/control assessment may yield documented `defer`, but cannot claim public readiness or reclassify a missing required preparation check as future operational work. CHECK-006/010 verify the future operational protocol and honest pending state, not a fabricated future public report/access result.

**Checks executed/reconciled:** CHECK-001 through CHECK-010. All inputs were deliberately broad in the approved Design: changing an included file stales every affected snapshot, potentially all ten checks. Do not narrow scope or silently waive repeated observations to obtain freshness. Any needed bounded rerun follows TASK-006/Design limits and retains prior attempts.

### Ledger and preparation acceptance

- [x] TASK-008 — Reconcile the final validation ledger and report preparation acceptance and remaining operations.

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

### Authorized implementation and final preparation — 2026-11-13

All eight implementation Tasks R1 are completed for the approved **private preparation** scope. The user explicitly authorized implementation, private sensitive inventory, the exact Apache R1 candidate and an individual plugin rehearsal under their existing Versat account. The three planning digests and reviewed ADR identity remain unchanged. Text approval does not adopt the license or clear exposure.

| Tasks | Actual completion |
|---|---|
| TASK-001–002 | Source/authority/private-access reconciliation and 16-category component/surface assessment completed with `defer`; opaque HPR-PRIVATE-01 binds the restricted revision and accountable next actions. |
| TASK-003–004 | Exact 16-file Apache R1 text package approved; seven upstream terms preserved. Maintained contribution/security routes and actual control limitations reviewed. No root license/channel/control activation. |
| TASK-005 | Maintained EN/PT/ES guidance, retained product provenance, exact nine-file adoption patch and separately executable operational handoff prepared. Root metadata remains 0.3.0. |
| TASK-006 | Source/private-candidate package checks, negative version/nested-path cases, real personal installation and six bounded client cases passed. Both complete roots passed 131 validator plus 48 execution tests. |
| TASK-007 | Ten actual current checks; individual 38 local and 72 retained scenario reviews; seven superseded scenarios across six impact items examined. No waived check or false public outcome. |
| TASK-008 | Current source-bound ledger reconciled, FIND-001 resolved by actual client evidence, task checkboxes aligned and safe acceptance/handoff prepared. |

The first personal six-case attempt passed. Product provenance/status corrections required a separately recorded final-source run. A duplicate-catalog registration setup failed safely and its adapter-path initialization error is preserved in `personal-client-02`; neither invoked a scenario agent. The corrected source run is `personal-client-03`. A final separately bounded `personal-client-04` captured both preparation and patched-root input identities before/after actual execution, because their live SDD ledgers cannot reuse each other's hashes. Each of the three successful suites used one fresh native invocation, within the approved 600-second native and 2,400-second suite limits; other cases stayed below 300 seconds. Exact model/reasoning/token telemetry was unavailable. No automatic successful-attempt selection or failed evidence deletion occurred.

The individual 0.4.0 candidate remains a private local test installation in a separate marketplace namespace/cache. All workspace 0.3.0 files remain unchanged. The synthetic consumer migrated explicitly between compatible exact local provider/config pairs; failed updates retained the verified pair. Local synthetic Git commits are test provenance only. No source-branch commit, push, PR, merge, effective root adoption, tag/release, visibility change, report message or real consumer migration occurred.

## Validation evidence

Final actual reports are under `docs/validation/harness-publication-readiness/attempt-04/`, with the dual-root client evidence under `personal-client-04/`. CHECK-001 through CHECK-010 pass for preparation; all share the actual unchanged preparation input `7e15904840093447562ef625076f0b2212cad4c6ceff9b827b47abcb690b4fd4`. The patched root has its own captured input and rehearsal record; it is not a copied acceptance hash. Earlier attempts, unknowns and fixture-ledger correction failures remain historical evidence.

The full suites passed with 179 tests per root. The first-use scenario created only Proposal/Requirements, retained null approval and stopped at Gate 1; independent inspection confirmed unchanged application/tests/config. Actual wrapper/client failures cover missing provider/resources, unavailable exact version and failed update; explicit synthetic migration and compatible recovery passed. All 16 approved text files and seven dependency-license texts match. Frozen policy/approval/archive records plus 1,069 historical validation files remain byte-identical; 365 relative links resolve. Semantic translation and each retained obligation were reviewed, not inferred from structural validation.

This is `prepared / defer-publication`, not H03 completion, legal clearance, public availability or operational reporting verification. Inaccessible package/cache/external payloads, confidential-history disposition, actual effective controls and intended-public-reporter receipt remain explicit later prerequisites. Legacy/v2 inventory warnings are preserved. Final delivery eligibility is checked separately after this ledger; archival and remote CI/PR/merge are not claimed here.

## Delivery

Documentary closure is `prepared` in `specs/archive/harness-publication-readiness/` on the existing private implementation branch. The user instructed “Ok avance” after the proposed implementation review and next delivery preparation. This authorizes the local review/archive step, not remote publication, license adoption, merge or visibility changes.

Implementation review confirmed the current three planning approvals, all eight completed tasks, ten current passing checks and 110 semantic assessments. The exact approved text package and unapplied adoption patch remain unchanged. No additional preparation blocker was found. Current review and before/after archival diagnostics are retained in `docs/validation/harness-publication-readiness/archive-preparation-01/`; earlier active-dossier reports remain historical observations.

The unique dossier moved from active to archive storage without changing its stable ID, approved plan, evidence locations, living specifications or required checks. Closure and this Delivery section are documentary bookkeeping. Selected live delivery with `--require-archive` passed with no findings or stale results. The complete post-move suite with trusted baseline and `--require-archive` also passed: 131 validator tests and 48 execution tests, with the existing historical legacy/v2 warnings retained. Actual reports are `archive-guard.json` and `full-suite.json` in the current archival evidence directory.

No PR, push, source-branch commit, merge, release, root license adoption, visibility change, report message or real consumer migration was performed. Publication remains deferred for the recorded rights/surface/control/reporting prerequisites. The next delivery step is governed review through a private PR when separately authorized; mandatory review and remote CI remain outstanding. Archival does not establish merge or operational publication.

### Private PR submission authorization — 2026-11-13

After documentary closure, the user explicitly requested: “Pode abrir o PR privado para revisão, seguindo o SDD, sem fazer merge, publicar release ou tornar o repositório público.” This authorizes the local commit, normal branch push and private review PR for this completed change. It does not authorize merge, release, root-license adoption, visibility changes or operational reporting. Earlier no-PR observations above describe the state at archival preparation.

The repository was re-observed private and main still matched the approved source base before submission; no existing open PR used this branch. Final local preflight is retained in `docs/validation/harness-publication-readiness/pr-submission-01/`. GitHub records the resulting PR, reviews and remote checks; a local pass does not replace them.
