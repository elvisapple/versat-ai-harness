---
sdd_version: 3
change: contribution-security-guidance
tasks:
- id: TASK-001
  description: Reconcile the current Harness and organization baselines and collect reporting-route inputs.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-002
  description: Implement common contribution/security rules and localized guides using maintained sources.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-003
  description: Bind contribution guidance to the approved H01 terms and verify provenance boundaries.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-006
  status: completed
- id: TASK-004
  description: Verify the actual confidential reporting route with explicitly authorized evidence.
  requirements:
  - REQ-004
  - REQ-006
  status: blocked
- id: TASK-005
  description: Prepare and review the private organization candidate and its coordinated adoption record.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-006
  description: Execute all approved checks and assess the complete acceptance and regression set.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: in-progress
- id: TASK-007
  description: Prepare the verified acceptance package and reconcile the private handoff state.
  requirements:
  - REQ-006
  status: pending
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 6bed2e92d705d83385b31d27364cfcda2b05549678818801c6082132d6dbc8d2
    design: 6f120a41ac76673587dff9355ab7fddc4e40f6f2a1e43af75a0cffa23314f3e2
  approval:
    source: User reply in this chat on 2026-11-10 after presentation of Tasks R1 for both handoffs and the Gate
      3 question.
    quote: Aprovado. Inicie a implementação documental privada de H01/H02, sem publicar, aplicar licenças ou ativar
      canais. Sinalize as decisões que dependerem de mim.
    revision: 1
    digest: d969a531b3de153e562ff06d72c4ad0568b3a88caabbb52ca7b465bd05c2d284
validation:
  plan_digest: d969a531b3de153e562ff06d72c4ad0568b3a88caabbb52ca7b465bd05c2d284
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/contribution-security-guidance/technical-001.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: 04506ed6c29218b581c0f3af457ff09630e28fbbaea8133798ec8d310025ab93
    input_digest_after: 04506ed6c29218b581c0f3af457ff09630e28fbbaea8133798ec8d310025ab93
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/contribution-security-guidance/technical-002.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: 04506ed6c29218b581c0f3af457ff09630e28fbbaea8133798ec8d310025ab93
    input_digest_after: 04506ed6c29218b581c0f3af457ff09630e28fbbaea8133798ec8d310025ab93
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-003
    result: unverified
    evidence: docs/validation/contribution-security-guidance/technical-003.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: 7ee7a8b54f0a38c5749612980d1fcdf78f59ae5424e08b01af9733bff81c2fd4
    input_digest_after: 7ee7a8b54f0a38c5749612980d1fcdf78f59ae5424e08b01af9733bff81c2fd4
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/contribution-security-guidance/technical-004.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: 04506ed6c29218b581c0f3af457ff09630e28fbbaea8133798ec8d310025ab93
    input_digest_after: 04506ed6c29218b581c0f3af457ff09630e28fbbaea8133798ec8d310025ab93
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-005
    result: fail
    evidence: docs/validation/contribution-security-guidance/technical-005.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: 5ba917ba6a09a13ae5ba9dff19606c05483339aef2bb70b03bad92f759a45111
    input_digest_after: 5ba917ba6a09a13ae5ba9dff19606c05483339aef2bb70b03bad92f759a45111
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-006
    result: unverified
    evidence: docs/validation/contribution-security-guidance/technical-006.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: 2e0cae75bc42df6f5fedcc6003fcf9cdb1400f9770ef60ffb4e1db68e0101623
    input_digest_after: 2e0cae75bc42df6f5fedcc6003fcf9cdb1400f9770ef60ffb4e1db68e0101623
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  assessments:
  - obligation:
      local:
        requirement: REQ-001
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Existing issue22/PR33/orgPR3 history and baseline instructions are retained; issue35 owns only
      new coordination.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Candidate names target README/AGENTS, real existing bug/feature/chore forms, setup/checks and actual
      issue-to-PR linkage.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Repository-specific instructions/forms take precedence; 13 baseline files and seven-file patch
      preserve forms/profile/README and newly added CODEOWNERS.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Six immutable optional private Harness references were fetched at their existing revision; detailed
      manuals remain maintained there.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Anonymous retrieval of all public CONTRIBUTING locales matches baseline; self-contained contribution
      text does not require private Harness or installed tooling.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Existing public instructions remain live; uncommitted replacement has no claimed public URL/activation,
      and unavailable reporting uses non-sensitive request only.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Seven-file public payload contains no strategy/customer data, credentials or mandatory private
      resources; existing private links are explicitly optional.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Original/third-party contributions require source/terms/notices and actual review; H01 inventory/owner
      attestation and copied-illustration missing-permission example cover evidence and refusal.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Guide links actual approved terms and approval record; both hashes verify and project/tool permissions
      remain separate. Candidate effectiveness is not claimed.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Missing rights/review prevents acceptance; no CLA/DCO/IP assignment was introduced. Actual H01
      wording is approved rather than treated as perpetually missing.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: unverified
    checks:
    - CHECK-003
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Actual PVR/internal-email access/receipt is not tested under the current scope; route choice and
      CODEOWNERS duty alone do not complete verification. Required mapped checks not passing: CHECK-003. No complete
      acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: unverified
    checks:
    - CHECK-003
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'All locales keep exploit details/secrets out of issues and provide non-sensitive private-routing
      recovery; live route method is still unavailable. Required mapped checks not passing: CHECK-003. No complete
      acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-004
        scenario: 3
    result: unverified
    checks:
    - CHECK-003
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Guides state no route was verified here, avoid response promises and retain missing-feature/contact/owner
      fallback; full required route check is pending. Required mapped checks not passing: CHECK-003. No complete
      acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-004
        scenario: 4
    result: unverified
    checks:
    - CHECK-006
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'No report, synthetic message, channel activation, access edit or third-party communication occurred.
      Required mapped checks not passing: CHECK-006. No complete acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: EN/PT/ES policies and guides preserve identical public/private routes, CODEOWNERS duty, recovery,
      permission and approval boundaries; native form is English and accepts three response languages.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Current local paths/anchors resolve; public source was read anonymously, private immutable references
      with authenticated access; canonical English links are identified.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Issue23 documentation automation and issue26 multilingual CI remain separate; no claim of their
      completion.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 1
    result: unverified
    checks:
    - CHECK-001
    - CHECK-006
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Common guides retain independent P01/P03 adoption and H03 distribution responsibilities. Required
      mapped checks not passing: CHECK-006. No complete acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: Current .github baseline refreshed to a762582c6585ae967c37f7f7f1c69c06c07e9071; newly added CODEOWNERS
      preserved; forward/reverse patch checked; activation withheld.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 3
    result: unverified
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-003
    - CHECK-004
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'All 35 obligations assessed; technical suites pass but actual reporting route and aggregate/lineage
      acceptance remain incomplete. No full delivery asserted. Required mapped checks not passing: CHECK-003, CHECK-005,
      CHECK-006. No complete acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 4
    result: unverified
    checks:
    - CHECK-006
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Historical planning-only state is preserved; later explicit scoped private implementation is recorded,
      without inferring public publication/license/release authority. Required mapped checks not passing: CHECK-006.
      No complete acceptance claimed.'
  - obligation:
      regression:
        impact: 1
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Extend maintained contribution routes with
      rights and confidential reporting while retaining source ownership, access conditions and safe replacement
      behavior. Compare the specific historical acceptance position or captured baseline with current observable
      behavior; do not reuse historical results as fresh evidence. Observed unchanged historical dossiers/root/version
      inputs and preserved current contribution/security/language boundaries; see the actual linked check reports.'
  - obligation:
      regression:
        impact: 1
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Extend maintained contribution routes with
      rights and confidential reporting while retaining source ownership, access conditions and safe replacement
      behavior. Compare the specific historical acceptance position or captured baseline with current observable
      behavior; do not reuse historical results as fresh evidence. Observed unchanged historical dossiers/root/version
      inputs and preserved current contribution/security/language boundaries; see the actual linked check reports.'
  - obligation:
      regression:
        impact: 1
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Extend maintained contribution routes with
      rights and confidential reporting while retaining source ownership, access conditions and safe replacement
      behavior. Compare the specific historical acceptance position or captured baseline with current observable
      behavior; do not reuse historical results as fresh evidence. Observed unchanged historical dossiers/root/version
      inputs and preserved current contribution/security/language boundaries; see the actual linked check reports.'
  - obligation:
      regression:
        impact: 1
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Extend maintained contribution routes with
      rights and confidential reporting while retaining source ownership, access conditions and safe replacement
      behavior. Compare the specific historical acceptance position or captured baseline with current observable
      behavior; do not reuse historical results as fresh evidence. Observed unchanged historical dossiers/root/version
      inputs and preserved current contribution/security/language boundaries; see the actual linked check reports.'
  - obligation:
      regression:
        impact: 1
        scenario: 6
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Extend maintained contribution routes with
      rights and confidential reporting while retaining source ownership, access conditions and safe replacement
      behavior. Compare the specific historical acceptance position or captured baseline with current observable
      behavior; do not reuse historical results as fresh evidence. Observed unchanged historical dossiers/root/version
      inputs and preserved current contribution/security/language boundaries; see the actual linked check reports.'
  - obligation:
      regression:
        impact: 3
        scenario: 1
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Retain canonical English and semantically
      aligned localized community entry points. Compare the specific historical acceptance position or captured
      baseline with current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged
      historical dossiers/root/version inputs and preserved current contribution/security/language boundaries; see
      the actual linked check reports.'
  - obligation:
      regression:
        impact: 3
        scenario: 2
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Retain canonical English and semantically
      aligned localized community entry points. Compare the specific historical acceptance position or captured
      baseline with current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged
      historical dossiers/root/version inputs and preserved current contribution/security/language boundaries; see
      the actual linked check reports.'
  - obligation:
      regression:
        impact: 3
        scenario: 3
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Retain canonical English and semantically
      aligned localized community entry points. Compare the specific historical acceptance position or captured
      baseline with current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged
      historical dossiers/root/version inputs and preserved current contribution/security/language boundaries; see
      the actual linked check reports.'
  - obligation:
      regression:
        impact: 3
        scenario: 4
    result: pass
    checks:
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Retain canonical English and semantically
      aligned localized community entry points. Compare the specific historical acceptance position or captured
      baseline with current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged
      historical dossiers/root/version inputs and preserved current contribution/security/language boundaries; see
      the actual linked check reports.'
  - obligation:
      regression:
        impact: 4
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Keep canonical procedures, human gates, exact-version
      and availability limits in reused guidance. Compare the specific historical acceptance position or captured
      baseline with current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged
      historical dossiers/root/version inputs and preserved current contribution/security/language boundaries; see
      the actual linked check reports.'
  - obligation:
      regression:
        impact: 4
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Keep canonical procedures, human gates, exact-version
      and availability limits in reused guidance. Compare the specific historical acceptance position or captured
      baseline with current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged
      historical dossiers/root/version inputs and preserved current contribution/security/language boundaries; see
      the actual linked check reports.'
  - obligation:
      regression:
        impact: 4
        scenario: 4
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Keep canonical procedures, human gates, exact-version
      and availability limits in reused guidance. Compare the specific historical acceptance position or captured
      baseline with current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged
      historical dossiers/root/version inputs and preserved current contribution/security/language boundaries; see
      the actual linked check reports.'
  - obligation:
      regression:
        impact: 5
        scenario: 0
    result: unverified
    checks:
    - CHECK-002
    - CHECK-003
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Extend provenance and confidential handling
      to contribution/reporting guidance without claiming a configured channel. Compare the specific historical
      acceptance position or captured baseline with current observable behavior; do not reuse historical results
      as fresh evidence. Observed unchanged historical dossiers/root/version inputs and preserved current contribution/security/language
      boundaries; see the actual linked check reports. Complete retained-obligation acceptance remains unverified
      because required mapped checks are not passing: CHECK-003.'
  - obligation:
      regression:
        impact: 6
        scenario: 0
    result: unverified
    checks:
    - CHECK-002
    - CHECK-003
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Add the missing approved-terms references,
      actual channel verification and per-product adoption evidence. Compare the specific historical acceptance
      position or captured baseline with current observable behavior; do not reuse historical results as fresh evidence.
      Observed unchanged historical dossiers/root/version inputs and preserved current contribution/security/language
      boundaries; see the actual linked check reports. Complete retained-obligation acceptance remains unverified
      because required mapped checks are not passing: CHECK-003, CHECK-006.'
  findings:
  - id: FIND-001
    source:
      plan: Exact terms approval and component rights evidence
    category: missing
    state: resolved
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    description: 'Owner approved the presented H01 wording on 2026-11-10; exact approval is recorded. Remaining
      gap: complete component rights/notices evidence, not another text-approval request.'
    tasks:
    - TASK-003
    checks:
    - CHECK-002
    resolution: Actual exact-text approval plus owner first-party provenance attestation, bounded 1,040-file inventory
      and seven inspected dependency license texts resolve the documentary gap. See docs/governance/h01-approval.md
      and docs/licensing/technical-review/README.md; final CHECK-002 report records current review.
  - id: FIND-002
    source:
      plan: Confidential reporting route verification
    category: missing
    state: open
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    description: CODEOWNERS responsibility is settled. Actual PVR/internal-email permissions, notifications and
      authorized receipt/access verification remain pending.
    tasks:
    - TASK-004
    checks:
    - CHECK-003
  - id: FIND-003
    source:
      plan: Final acceptance scenario assessment
    category: missing
    state: open
    evidence: docs/validation/contribution-security-guidance/technical-review.md
    description: Final delivery acceptance remains incomplete while mandatory package/lineage checks surface active
      operational gaps; documentary review and individual assessments are being recorded without waiving those requirements.
    tasks:
    - TASK-006
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-003
    - CHECK-004
closure: active
---

# Tasks — H02

Change `contribution-security-guidance` · [Harness #35](https://github.com/versat-labs/versat-ai-harness/issues/35) · Tasks R1.
Executor and accountable security/licensing contact: Elvis Zoz (`@elviszoz`); technical review follows the existing CODEOWNERS. Terms approval is an input from H01, not an approval implied by this assignment.

## Authorized stage and execution boundary

Proposal/Requirements R1 and Design R1 are approved. This stage prepares Tasks only. Every task is pending, and no execution is authorized by the latest Design approval. After reviewing this Tasks revision, the user may approve it and separately or jointly authorize a bounded implementation scope.

This plan covers common guidance and a private organization candidate. It does not authorize public `.github` changes, live channel configuration, synthetic messages, access changes, licenses, releases or consumer/product adoption. The real route check has its own explicit authorization prerequisite; no fallback-only guide can complete H02.

## Ordered work

- [x] TASK-001 — Reconcile the current Harness and organization baselines and collect reporting-route inputs.

  **Depends on:** current three planning approvals and explicit implementation authorization before starting.

  **Work:** inspect drift from selected Harness source `597b81c71a0fc0908ff5264fe9987bb5c0d8feec` and preserve the exact provider and unrelated work. Refresh the read-only `.github` baseline, AGENTS instructions, CONTRIBUTING/README locale files and relevant source references before preparing a patch. Record actual repository/ref/blob and intended-reader access; preserve Issue 22, PR 33 and organization PR 3 as delivered history. Inspect the existing guidelines and obtain the owner's actual reporting-route inputs: destination/provider if any, audience, responder/access boundary, retention/minimization instructions, operational commitments and authorized verification scope. Record only safe metadata in `docs/governance/security-reporting.md`; mark missing or unverified inputs explicitly. Do not choose a fictional endpoint or activate one.

  **Complete when:** current baselines and useful retained behavior are identified; available channel inputs and concrete missing-input follow-ups are recorded; a public/private audience can be identified for every proposed route. This task inventories prerequisites and does not certify an operational channel. A material baseline/contract change reopens the affected gate.

  **Evidence/checks:** baseline/candidate source record for CHECK-001/004/006 and safe reporting record for CHECK-003.

- [x] TASK-002 — Implement common contribution/security rules and localized guides using maintained sources.

  **Depends on:** TASK-001 and the agreed H01 common-policy contract; draft text may proceed while H01's concrete terms approval is pending.

  **Work:** add `standards/core/contribution.md` and its single `core.always` entry; extend the existing Security Standard for verified confidential reporting and safe failure behavior. Create the `contributing` and `security-reporting` user guides in EN/PT/ES using the approved Design paths. Reuse existing setup, SDD, GitHub delivery and validation guides. Preserve repository-specific precedence, provenance/notices, actual review/check requirements, optional labeled private resources and a usable public route for a contributor without the tool. Do not introduce a CLA, DCO, IP assignment or unprovided rights grant. Unknown terms/channel details remain explicitly unavailable in drafts; those drafts cannot be called final accepted guidance.

  **Complete when:** common rules resolve through the index and all six guide files provide useful, aligned journeys with truthful current access/route status, no copied SDD manual and no invented legal or security capability. Final exact terms/active-route content is completed by TASK-003/004; completion here does not satisfy their acceptance.

  **Evidence/checks:** CHECK-001/004 and relevant CHECK-002/003 behavior; final passes are recorded after the dependent facts and source text stabilize.

- [x] TASK-003 — Bind contribution guidance to the approved H01 terms and verify provenance boundaries.

  **Depends on:** TASK-002 and H01 TASK-003's genuinely approved terms/notices candidate, with accessible approval evidence and exact version/hash.

  **Work:** incorporate the actual approved H01 references and applicable audience limits; distinguish tool permissions from destination-project licensing. Verify first-party, third-party and missing-rights examples. Check that a tool-free public contribution does not require access to private terms or internal resources. Do not copy/rewrite approved legal text or invent a public terms URL. If H01 wording, approval or access changes, invalidate the affected references/evidence and rerun the check.

  **Complete when:** every approved-terms assertion has the correct version/hash and actual approval reference, provenance/notice responsibilities are clear, and missing-rights/review cases prevent acceptance without creating a new legal mechanism. A pending H01 candidate blocks this task; neither H01 archive/merge nor H03 distribution is required merely to bind correct private-source references with truthful public-access limits.

  **Evidence/checks:** CHECK-002, including its contribution to REQ-006's final evidence assessment.

- [ ] TASK-004 — Verify the actual confidential reporting route with explicitly authorized evidence.

  **Depends on:** TASK-001's owner-approved real route and verification scope, TASK-002's guide, available configuration/access observations and explicit authorization for the concrete synthetic submission. Private-document implementation authorization alone is insufficient.

  **Work:** finalize safe source configuration/decision metadata before its input digest. Follow CHECK-003 exactly: an authorized performer sends a non-sensitive unique marker through the actual chosen route; observe intended-responder receipt and permitted access/configuration evidence for the intended reporter audience. Record performer, authorization, actual destination scope, time/environment, safe receipt reference and verification limits without credentials or real vulnerability payloads. Exercise unavailable/unverified route, denied access and safe public-contact fallback. Update all guide locales to verified status only after genuine evidence; freeze source changes and repeat affected checks as needed. Do not enable a new service, modify access or send unapproved messages. If a setting change is necessary, stop and obtain that distinct operational authorization first.

  **Complete when:** actual route, receipt and supported access boundary are observed and attributable; safe fallback works; operational promises are owner-approved; no active claim exceeds the evidence. A mock, administrator-only access assumption, supplied address without receipt, or fallback-only guide is insufficient. If prerequisites or permission are unavailable, this task becomes blocked during execution and the required check remains unverified; other independent documentation work can continue.

  **Evidence/checks:** CHECK-003 and the authorization-boundary observations in CHECK-006. Owner-performed evidence is usable only if its actual method, inputs, authorization, receipt and limits can be inspected; no execution is fabricated.

- [x] TASK-005 — Prepare and review the private organization candidate and its coordinated adoption record.

  **Depends on:** TASK-001/002 for drafting; TASK-003/004 for final approved-terms and verified-route claims.

  **Work:** prepare the EN/PT/ES CONTRIBUTING candidate, source baseline/diff and non-sensitive handoff record under `docs/handoffs/contribution-security-guidance/organization/`. Adjust organization README candidate siblings only if their navigation/description actually changes. Keep the profile, issue forms/fields/types/project associations and repository precedence unchanged. Add Harness README locale links only when targets exist. Review the candidate independently of private strategy; preserve a self-contained public route, optional clearly private detail and actual intended-reader access. Verify replacement dependencies and record pending public activation separately; do not create a URL for an uncommitted candidate or write to the public repository.

  **Complete when:** candidate text, localized navigation and reviewed diff preserve the delivered organization behavior; source/reference/access evidence is explicit; a missing replacement target retains the old usable live route. The record identifies separate future organization review/rollout and product adoption responsibilities. Local candidate completion is not public adoption or distribution.

  **Evidence/checks:** CHECK-001/004; retain all old useful paths and Issue 35 traceability for new coordination without reopening Issue 22.

- [ ] TASK-006 — Execute all approved checks and assess the complete acceptance and regression set.

  **Depends on:** TASK-001–005 and stable source inputs, including real H01 text approval and actual confidential-route evidence.

  **Work:** execute all six approved Design methods with actual before/after canonical input digests, environment, revision and safe evidence paths under `docs/validation/contribution-security-guidance/`. Reuse adequate existing methods, not prior passing results. Run the full maintained `./scripts/validate/run.sh`; check the organization candidate through its actual diff, links, translations and intended-access review rather than inventing an application test suite. Assess every one of the 21 local and 14 retained obligations. Retain the planned replacement of new-delivery Issue 22 linkage with Issue 35 while preserving historical delivery. Track failures/unverified findings and fix in-scope defects through the responsible task; rerun affected checks after shared-source, terms, route or remote-state changes.

  **Complete when:** six current required results pass, all 35 applicable assessments pass, no open finding or stale result remains and actual Tasks/input digests bind the evidence. Structural success cannot replace approval, public-reader usability, live reporting-route verification or translation review. Required unavailable checks remain unverified, not excluded. CHECK-006 has no dependency on delivery/archive success.

  **Evidence/checks:** CHECK-001–006; planned `check-001.md` through `check-006.md` or equivalent stable observed evidence. Complete statuses are never inferred from documentation preparation alone.

- [ ] TASK-007 — Prepare the verified acceptance package and reconcile the private handoff state.

  **Depends on:** TASK-006.

  **Work:** inspect task completion, current upstream approvals, six results, all 35 assessments, accessible evidence and source/terms references, unchanged historical dossiers and zero unresolved findings. Prepare the review summary distinguishing common guidance from the still separately authorized organization rollout, per-product adoption and H03 distribution. Reconcile authorized private tracking without closing unrelated issues or claiming live changes. Confirm the independent closure procedure below is ready to follow after accurate task completion.

  **Complete when:** the reviewed acceptance package and truthful handoff summary are ready and all preceding work is actually complete. The final delivery/archive guard is not a prerequisite of this task. If review changes declared source inputs, reopen affected validation before recording completion.

  **Evidence/checks:** reuse CHECK-001–006 and current assessments. No invented new approval or test result is introduced merely to prepare the summary.

## Dependencies and concurrent work

TASK-001 precedes TASK-002. TASK-003 and TASK-004 address independent terms and channel inputs and can progress concurrently where authorized. TASK-005 drafting may proceed after TASK-002, but its final claims depend on TASK-003/004. TASK-006 follows all finalized source work; TASK-007 follows complete acceptance.

H01's actual terms approval is necessary for CHECK-002, but its final archive/merge is not a prerequisite to prepare H02 privately. The confidentiality requirement cannot be satisfied by waiting for unrelated product bootstrap or by assuming H03 will solve it. Platform, Workspace, Discover and CRM retain their own terms/access/adoption evidence through P01/P03.

Serialize shared index/README edits with H01 and revalidate the final relevant combined source. Changes to H01 terms/review records, organization baseline, channel configuration or a sibling archive included in declared scopes require affected checks to be rerun. Do not introduce a circular requirement that either dossier's archive must already be complete before the other can finish its own task work.

## Risks and execution stop conditions

Missing H01 approval, unavailable or unapproved reporting destination, absent synthetic-test authorization, inaccessible evidence and unverified intended-reader access block the affected task/check. Public organization writes, access changes, channel setup and synthetic communications remain separately scoped operational actions. No endpoint, response SLA, retention policy, legal mechanism or reviewer qualification is invented to bypass a gap.

No blocker prevents reviewing Tasks R1; this is not a declaration that route verification or operational prerequisites are already satisfied. Material source drift, new legal mechanism or architectural service requires reopening the applicable planning gate. Scoped documentary execution can progress useful independent work while a genuinely unavailable required external prerequisite remains blocked and visible.

## Independent closure procedure

After actual task completion, all evidence/assessments and resolved findings are recorded, run selected `--phase delivery --json`. On eligibility, move the unique dossier to `specs/archive/contribution-security-guidance/`, apply canonical closure bookkeeping, verify references and run selected `--phase delivery --require-archive --json`. These mandatory lifecycle operations follow task completion; neither a task nor CHECK-006 requires its own final delivery result as a prerequisite. A failing guard reopens the affected work; missing terms/channel evidence is never waived.

Any later PR publication needs its own scoped authorization and required remote CI/review. Organization rollout must keep the old usable route until the actual approved replacement is available and reviewed under that repository's instructions. No merge, release, public activation, consumer migration or product adoption is inferred from local closure.

## Planning review

Tasks R1 is presented for Gate 3 after the actual Proposal/Requirements R1 and Design R1 approvals. All seven tasks are pending and unchecked, with empty implementation validation arrays. The user's latest “Aprovado.” approved Design; it is not approval of this previously unseen Tasks revision or an instruction to execute it.

2026-11-10: the user approved both presented Tasks R1 revisions and explicitly authorized private documentary implementation with the quote: "Aprovado. Inicie a implementação documental privada de H01/H02, sem publicar, aplicar licenças ou ativar canais. Sinalize as decisões que dependerem de mim.". The canonical Tasks digest matched the presented revision: `d969a531b3de153e562ff06d72c4ad0568b3a88caabbb52ca7b465bd05c2d284`. This is current Gate 3 approval and scoped execution authority; earlier presentation-stage wording above is historical. Publication, license application, channel activation and synthetic messages remain outside the authorized scope.

## Progress

2026-11-10 operational authorization and partial execution: the user explicitly authorized enabling PVR in `versat-labs/.github`, private-report and Harness internal-email tests, and completion/CI work, while retaining the no-merge/no-license boundary. PVR was enabled and read back as enabled. One non-sensitive internal test was sent to the two relevant CODEOWNERS; Elvis's connected inbox contains it. Evidence and exact limitations: `docs/validation/contribution-security-guidance/operational-attempt-01.md`. TASK-004 remains blocked on an available non-administrator PVR reporter and the remaining receipt/access observations, not on missing authorization for these tests. Only the administrator account is available to the agent; intended-reporter participation was requested from the user. No route-verification pass, full acceptance or green CI is claimed. Earlier no-activation/no-message statements describe the preceding documentary stage.

2026-11-10 technical review: owner provenance confirmed; H01 terms/notices documentary work and localized guidance complete. H02 approved-terms binding and private organization package complete. H02 channel verification stays blocked by the current no-activation/no-message scope; no new owner decision is needed. Current final acceptance guards remain separate from documentary completion.

2026-11-10: actual user approval “H01 revisado e aprovado.” recorded against the reviewed draft-0.2 hash; current terms differ only in administrative approval status. Relevant CODEOWNERS own monitoring/triage/remediation for both H02 routes; no role-definition question remains. Remaining component evidence and operational checks are separate. Affected previous check results were preserved and invalidated, not relabeled.

2026-11-10 routing decision implemented privately: public GitHub PVR with organization-default native template; private repositories email relevant CODEOWNERS through internal Versat contacts. Earlier tentative info@versat.ag selection is superseded. Affected prior check results are preserved in before-routing-decision.json, removed from current results pending fresh checks; no old result is relabeled with new inputs. Existing forms unchanged. No publication/activation/test message.

Private documentary implementation authorized by the actual Gate 3 reply on 2026-11-10. TASK-001/002 completed within their bounded inventory/rules completion criteria; no rights clearance or final acceptance implied. Remaining task statuses distinguish prepared drafts from blocked terms/channel and pending final acceptance. Owner decisions received: free official plugin use for Versat Labs contributions; authorized Versat developers may modify; users may not redistribute, commercialize or fork; company Paraguay, approver Elvis Luis Zoz. The earlier tentative info@versat.ag choice was superseded by the public-PVR/private-CODEOWNERS decision above. No public writing, license application, channel activation or synthetic message occurred. Earlier planning-only wording is historical; this Progress and structured status record are current.

## Validation evidence

Current final documentary observations and individual assessments are in `docs/validation/contribution-security-guidance/technical-review.md`, with current check reports, stable before/after input snapshots and selected validator outputs. The owner approved H01 wording and confirmed first-party provenance. No concrete user-input gap remains for this documentary scope. All planned local/regression obligations are assessed, without exclusions. Technical suites pass (131 validator plus 48 execution tests); aggregate acceptance remains blocked by required operational/lineage checks. Prior attempts remain preserved as historical evidence. H02's private package is complete; no publication, activation or message occurred.

## Delivery

Closure remains active. No delivery, archive, PR, merge, channel activation, product adoption or publication is claimed.
