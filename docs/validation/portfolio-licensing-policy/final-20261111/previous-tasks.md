---
sdd_version: 3
change: portfolio-licensing-policy
tasks:
- id: TASK-001
  description: Confirm the implementation baseline and collect the component rights and decision inputs.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-002
  description: Implement the canonical licensing/publication Standard and evidence-based review ledger.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  status: completed
- id: TASK-003
  description: Prepare concrete Harness/plugin terms and notices and obtain attributable approval of the exact candidate.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  status: completed
- id: TASK-004
  description: Add localized licensing guidance and connect existing navigation to the reviewed artifacts.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: completed
- id: TASK-005
  description: Execute all approved checks and assess the complete acceptance and regression set.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: in-progress
- id: TASK-006
  description: Prepare the verified acceptance package and reconcile the private handoff state.
  requirements:
  - REQ-004
  - REQ-006
  status: pending
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7
    design: 801894d789455496c072bc19b29947ff2c5900df09e4725d9d9e7c8d5f8acd55
  approval:
    source: User reply in this chat on 2026-11-10 after presentation of Tasks R1 for both handoffs and the Gate
      3 question.
    quote: Aprovado. Inicie a implementação documental privada de H01/H02, sem publicar, aplicar licenças ou ativar
      canais. Sinalize as decisões que dependerem de mim.
    revision: 1
    digest: ac2e801e4908448c2e534f8865970d979dbb751097b11b89532ee7a26299c138
validation:
  plan_digest: ac2e801e4908448c2e534f8865970d979dbb751097b11b89532ee7a26299c138
  results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/technical-001.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: af7aaf6ac2b93d6819f4430eb23c4599c90496db5bc1260a3ac0e7f5f17c5279
    input_digest_after: af7aaf6ac2b93d6819f4430eb23c4599c90496db5bc1260a3ac0e7f5f17c5279
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-002
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/technical-002.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: af7aaf6ac2b93d6819f4430eb23c4599c90496db5bc1260a3ac0e7f5f17c5279
    input_digest_after: af7aaf6ac2b93d6819f4430eb23c4599c90496db5bc1260a3ac0e7f5f17c5279
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-003
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/technical-003.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: ea585b7f21de8358c14702dc62c28100f71ebcb65f2d2b60b0b09d949d5aa6e6
    input_digest_after: ea585b7f21de8358c14702dc62c28100f71ebcb65f2d2b60b0b09d949d5aa6e6
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-004
    result: pass
    evidence: docs/validation/portfolio-licensing-policy/technical-004.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: af7aaf6ac2b93d6819f4430eb23c4599c90496db5bc1260a3ac0e7f5f17c5279
    input_digest_after: af7aaf6ac2b93d6819f4430eb23c4599c90496db5bc1260a3ac0e7f5f17c5279
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-005
    result: fail
    evidence: docs/validation/portfolio-licensing-policy/technical-005.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: e081c268c9bd22f68599c03cfa5f613c6feeae524eafa20661d8fb38348ff0ab
    input_digest_after: e081c268c9bd22f68599c03cfa5f613c6feeae524eafa20661d8fb38348ff0ab
    context:
      execution: local
      environment: macOS-26.5.2-arm64-arm-64bit; Python 3.11.4; authenticated private refs plus anonymous public
        baseline reads; no live route test
      observed: true
  - check: CHECK-006
    result: unverified
    evidence: docs/validation/portfolio-licensing-policy/technical-006.md
    revision: 2026-11-10 final documentary review, base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec
    input_digest_before: 42a42b91442e6104ce43712965ebdb6acdac7cb2dbb84d5f7e0f39af0146dc0b
    input_digest_after: 42a42b91442e6104ce43712965ebdb6acdac7cb2dbb84d5f7e0f39af0146dc0b
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
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Ledger retains Apache-2.0 intent separately for Platform and Workspace with individual adoption/export
      evidence.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Ledger and terms preserve proprietary/private Harness, Discover and CRM; public plugin installation
      is distinct from source licensing.
  - obligation:
      local:
        requirement: REQ-001
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Policy/guide separate recommended disposition from license application, public export, SDK and
      other handoffs; no operation occurred.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Baseline CSV identifies all 1,040 source files; owner attestation identifies first-party provenance;
      seven installed validation packages have exact versions/license texts, external to source.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Synthetic missing-grant, incompatible-dependency, secret-history, missing-reviewer and unknown-control
      cases all defer; private scope remains restricted.
  - obligation:
      local:
        requirement: REQ-002
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Policy explicitly requires tree/history/tags/releases/LFS/fixtures/CI/attachments scope; technical
      source inventory does not claim H03 export clearance.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 1
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Approved draft-0.2 and status-only current version retain exact installation/use/modification/redistribution
      clauses; reviewed notices identify source and external dependency boundaries.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Actual user approval follows presentation of exact draft; original SHA-256 and current administrative
      hash verify. CODEOWNERS/planning were not used as text approval.
  - obligation:
      local:
        requirement: REQ-003
        scenario: 3
    result: pass
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Terms and guides preserve destination-project terms, including Apache projects, independently of
      proprietary tool permissions.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 1
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Ledger identifies owner/executor/company approver, technical CODEOWNERS, source evidence and limits;
      technical review is by this agent and owner approval is attributable.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 2
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Policy keeps P01/P03 evidence separate and H03 distribution separate; no unrelated product delivery
      is claimed.
  - obligation:
      local:
        requirement: REQ-004
        scenario: 3
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Unknown controls/authority remain explicit in policy; current owner attestation resolves documentary
      provenance only, not future operational controls.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 1
    result: pass
    checks:
    - CHECK-003
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Both new core policies occur exactly once in core.always; no Skills copied or altered.
  - obligation:
      local:
        requirement: REQ-005
        scenario: 2
    result: unverified
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Root package/schema/SDD/template/validator paths and manifests are unchanged; technical suites
      exercise them. Required mapped checks not passing: CHECK-005. No complete acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-005
        scenario: 3
    result: unverified
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'VERSION/marketplace v0.3.0 and consumer locks are unchanged; no release or implicit consumer update
      occurred. Required mapped checks not passing: CHECK-005. No complete acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 1
    result: unverified
    checks:
    - CHECK-004
    - CHECK-006
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Actual later implementation authorization permits private docs/tracking; no effective license,
      release, public write or access change occurred. Required mapped checks not passing: CHECK-006. No complete
      acceptance claimed.'
  - obligation:
      local:
        requirement: REQ-006
        scenario: 2
    result: pass
    checks:
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: Owner text approval and technical source review are explicit; effective adoption/distribution remain
      separately scoped, and unavailable operational evidence stays unverified.
  - obligation:
      local:
        requirement: REQ-006
        scenario: 3
    result: unverified
    checks:
    - CHECK-004
    - CHECK-005
    - CHECK-006
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Guides, all 24 obligations and current check evidence are reviewed; final delivery claim remains
      withheld while required aggregate/lineage results are not passing. Required mapped checks not passing: CHECK-005,
      CHECK-006. No complete acceptance claimed.'
  - obligation:
      regression:
        impact: 1
        scenario: 0
    result: pass
    checks:
    - CHECK-001
    - CHECK-002
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Add the absent portfolio policy and concrete-terms
      approval path without treating strategic selection as operative licensing. Compare the specific historical
      acceptance position or captured baseline with current observable behavior; do not reuse historical results
      as fresh evidence. Observed unchanged historical dossiers/root/version inputs and preserved current contribution/security/language
      boundaries; see the actual linked check reports.'
  - obligation:
      regression:
        impact: 2
        scenario: 0
    result: pass
    checks:
    - CHECK-001
    - CHECK-004
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Preserve least privilege, secret handling,
      provenance and explicit high-impact authorization while specifying evidence for publication decisions. Compare
      the specific historical acceptance position or captured baseline with current observable behavior; do not
      reuse historical results as fresh evidence. Observed unchanged historical dossiers/root/version inputs and
      preserved current contribution/security/language boundaries; see the actual linked check reports.'
  - obligation:
      regression:
        impact: 3
        scenario: 1
    result: unverified
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: New policy must retain canonical root resources
      and avoid copied Standards. Compare the specific historical acceptance position or captured baseline with
      current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged historical
      dossiers/root/version inputs and preserved current contribution/security/language boundaries; see the actual
      linked check reports. Complete retained-obligation acceptance remains unverified because required mapped checks
      are not passing: CHECK-005.'
  - obligation:
      regression:
        impact: 3
        scenario: 2
    result: unverified
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: New policy must retain canonical root resources
      and avoid copied Standards. Compare the specific historical acceptance position or captured baseline with
      current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged historical
      dossiers/root/version inputs and preserved current contribution/security/language boundaries; see the actual
      linked check reports. Complete retained-obligation acceptance remains unverified because required mapped checks
      are not passing: CHECK-005.'
  - obligation:
      regression:
        impact: 3
        scenario: 3
    result: unverified
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: New policy must retain canonical root resources
      and avoid copied Standards. Compare the specific historical acceptance position or captured baseline with
      current observable behavior; do not reuse historical results as fresh evidence. Observed unchanged historical
      dossiers/root/version inputs and preserved current contribution/security/language boundaries; see the actual
      linked check reports. Complete retained-obligation acceptance remains unverified because required mapped checks
      are not passing: CHECK-005.'
  - obligation:
      regression:
        impact: 4
        scenario: 2
    result: unverified
    checks:
    - CHECK-003
    - CHECK-005
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    explanation: 'Inspected retained source/current-contract mapping: Retain the exact semantic release selection
      contract; this proposal neither releases nor enables public distribution. Compare the specific historical
      acceptance position or captured baseline with current observable behavior; do not reuse historical results
      as fresh evidence. Observed unchanged historical dossiers/root/version inputs and preserved current contribution/security/language
      boundaries; see the actual linked check reports. Complete retained-obligation acceptance remains unverified
      because required mapped checks are not passing: CHECK-005.'
  findings:
  - id: FIND-001
    source:
      plan: Exact terms approval and component rights evidence
    category: missing
    state: resolved
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    description: 'Owner approved the presented H01 wording on 2026-11-10; exact approval is recorded. Remaining
      gap: complete component rights/notices evidence, not another text-approval request.'
    tasks:
    - TASK-003
    checks:
    - CHECK-002
    resolution: Actual exact-text approval plus owner first-party provenance attestation, bounded 1,040-file inventory
      and seven inspected dependency license texts resolve the documentary gap. See docs/governance/h01-approval.md
      and docs/licensing/technical-review/README.md; final CHECK-002 report records current review.
  - id: FIND-003
    source:
      plan: Final acceptance scenario assessment
    category: missing
    state: open
    evidence: docs/validation/portfolio-licensing-policy/technical-review.md
    description: Final delivery acceptance remains incomplete while mandatory package/lineage checks surface active
      operational gaps; documentary review and individual assessments are being recorded without waiving those requirements.
    tasks:
    - TASK-005
    checks:
    - CHECK-001
    - CHECK-002
closure: active
---

# Tasks — H01

Change `portfolio-licensing-policy` · [Harness #34](https://github.com/versat-labs/versat-ai-harness/issues/34) · Tasks R1.
Executor and accountable licensing/security contact: Elvis Zoz (`@elviszoz`). Technical review follows CODEOWNERS, including Everton Spohr (`@evertonspohrversat`). Versat E.A.S. remains the user-declared rights holder, subject to actual component verification.

## Authorized stage and execution boundary

Proposal/Requirements R1 and Design R1 are approved. The current authorization is to prepare this Tasks plan. Every task below is pending. Approval of this document ends planning; implementing even the private candidate documents needs an explicit subsequent instruction, which may be combined with the Tasks approval after review.

The plan implements the approved private policy/terms candidate scope. It does not apply a root LICENSE, activate terms, publish repositories/content/releases, change permissions, activate channels, update consumers, implement product runtime or certify P01/P02/P03/H03 delivery. A concrete owner decision or approval cannot be supplied by an agent-authored record.

## Ordered work

- [x] TASK-001 — Confirm the implementation baseline and collect the component rights and decision inputs.

  **Depends on:** current three planning approvals and explicit implementation authorization before starting.

  **Work:** compare the current executor checkout/remote baseline with the selected source `597b81c71a0fc0908ff5264fe9987bb5c0d8feec`, preserving unrelated changes and the exact provider. Reconfirm applicable AGENTS/index-resolved Standards and review relevant drift before applying this plan. Inventory the proposed Harness/plugin scope, original material, dependencies, copied code, templates/assets, notices and available rights/grant references. Obtain owner decisions needed for installation, use, modification, redistribution, audience and component scope, plus any entity details required by the eventual wording. Record confirmed facts versus missing inputs in `docs/governance/licensing-review.md`, with responsible follow-up. Keep confidential contracts and personal data outside the package. Do not conduct P01/H03 export clearance or infer permission from repository visibility.

  **Complete when:** the baseline and bounded inventory are documented; every unavailable rights/decision input has an explicit status and owner. Completion of inventory/scoping is not clearance. Missing permissions or rights may prevent TASK-003 and later acceptance even if this inventory task is complete. A materially changed contract/provider reopens the affected planning gate rather than silently changing the approved plan.

  **Evidence/checks:** the ledger becomes reviewed source input to CHECK-001/002/006; initial gaps remain pending evidence, not passing check results.

- [x] TASK-002 — Implement the canonical licensing/publication Standard and evidence-based review ledger.

  **Depends on:** TASK-001's baseline; it can proceed while actual terms review is pending.

  **Work:** write `standards/core/licensing-publication.md`, add its single `core.always` index entry and complete the policy sections of the ledger. Preserve the selected public-Apache and proprietary-private routes, distinct per-product adoption, reviewer authority and publish/defer/retain-private dispositions. Define the complete export-review prerequisite without claiming that it has been performed. Add clearly synthetic success and failure examples for absent grants, incompatible dependencies, sensitive history, missing reviewer and unavailable controls. Coordinate the additive index change with H02; do not copy policy into Skills, change release refs or alter consumer locks.

  **Complete when:** the common policy resolves through the index, correctly distinguishes policy from licenses/operations, and all synthetic disposition cases have the expected documented result. Actual unreviewed product rows remain pending. Required evidence and authority cannot be waived by an example or role label.

  **Evidence/checks:** CHECK-001 and CHECK-003; retain actual observations for final validation on stable inputs in TASK-005.

- [x] TASK-003 — Prepare concrete Harness/plugin terms and notices and obtain attributable approval of the exact candidate.

  **Depends on:** TASK-001's actual owner inputs/rights evidence and TASK-002's policy.

  **Work:** draft the non-operative `docs/licensing/harness-plugin-terms.md` and `harness-plugin-notices.md` from explicit owner decisions. Cover the exact component scope and installation/use/modification/redistribution permissions and conditions, third-party rights/notices and tool-versus-destination-project terms. Do not select unprovided contractual grants, jurisdiction, corporate details or signature authority. If required inputs or legal interpretation are unavailable, stop the dependent wording/approval work and ask the accountable owner for the concrete decision or appropriate review. Version and hash the actual candidate; obtain and record genuine acceptance of that precise text in the ledger, including reviewer capacity, source and limits. Any substantive text change requires renewed text review. No approval date, signature, grant or legal qualification is fabricated.

  **Complete when:** concrete terms/notices are substantively complete and the actual authorized reviewer has approved their exact version/hash, with required rights evidence available and no unresolved blocker to that approval. A generic policy, unreviewed draft, SDD approval or CODEOWNERS entry does not complete this task. Candidate approval remains separate from effective license application or distribution.

  **Evidence/checks:** CHECK-002. If evidence is missing, mark this task blocked during execution, keep the required check unverified and record a finding; do not weaken its completion condition to finish the plan.

- [x] TASK-004 — Add localized licensing guidance and connect existing navigation to the reviewed artifacts.

  **Depends on:** TASK-002; drafts may progress alongside TASK-003, but final approved-term references depend on TASK-003.

  **Work:** create `docs/user-docs/guides/licensing.md`, `.pt.md` and `.es.md` with prerequisites, a representative component review, expected disposition and missing-evidence recovery. Link maintained Standards and exact terms/notice references without copying them. Add localized README navigation only to existing targets. Preserve useful setup/contribution guidance and explain the limits of source-only behavior and candidate approval. Read all proposed public-facing explanation independently of private strategy; keep private legal analysis, customer information and sensitive evidence out. Do not publish the content or create a public endpoint.

  **Complete when:** all three versions are semantically aligned, links/anchors resolve, the representative journey and blocked case are usable, and no passage implies operative terms, complete product adoption or publication. H02 can consume the reviewed references with their actual approval and audience/access status.

  **Evidence/checks:** CHECK-004, plus CHECK-002/003 where terms or canonical references are affected.

- [ ] TASK-005 — Execute all approved checks and assess the complete acceptance and regression set.

  **Depends on:** TASK-001–004 and stable source inputs, including the real text approval. A blocked earlier task blocks complete acceptance.

  **Work:** follow all six methods in the approved Design without narrowing their input scopes or required suites. Before each actual check, capture its canonical input digest; run/observe the method; capture the after digest and record matching snapshots, environment, revision and evidence. Reuse adequate methods from existing work, not historical pass claims. Keep outputs under `docs/validation/portfolio-licensing-policy/` as designed. Run the full `./scripts/validate/run.sh` with the selected Python environment. Assess each of the 18 local scenarios and six retained regression obligations against actual observations; preserve failed/unverified attempts and stable finding IDs. Fix in-scope defects through the originating task and rerun affected checks; substantive scope/design changes reopen the relevant gate.

  **Complete when:** six required checks pass with current evidence, all 24 obligations have passing applicable assessments, no open finding/stale result remains, and the actual Tasks digest binds the recorded execution. Complete checkboxes or package success cannot replace rights, text-approval or semantic acceptance evidence. CHECK-006 inspects structure/lineage; it does not execute or depend on final delivery/archive guards.

  **Evidence/checks:** CHECK-001–006; planned reports `docs/validation/portfolio-licensing-policy/check-001.md` through `check-006.md` or equivalent stable evidence paths. Reports are created only from actual execution.

- [ ] TASK-006 — Prepare the verified acceptance package and reconcile the private handoff state.

  **Depends on:** TASK-005.

  **Work:** verify task statuses against their completion conditions, current upstream approvals, six results and all 24 assessments, source digests, evidence accessibility, unchanged historical dossiers and no open findings. Prepare the review summary identifying policy/candidate status, exact approved text, remaining operational dependencies and H02/P01/P03/H03 boundaries. Update authorized private tracking truthfully without closing unrelated issues or claiming adoption/publication. Confirm the independent closure steps below can be executed after this task's completion; do not require a delivery pass as a precondition of this task.

  **Complete when:** the acceptance package and review summary are accurate and reviewable, and all preceding work/evidence is complete. This task's completion is recorded before final delivery/archive validation. It does not assert merge, release, license activation or public export.

  **Evidence/checks:** reuse current CHECK-001–006 evidence. If this review changes declared source inputs, reopen affected validation before completion; do not relabel an old run with a new digest.

## Dependencies and concurrent work

The default order is TASK-001 → TASK-002 → TASK-003 → TASK-004 → TASK-005 → TASK-006. Only independent drafting in TASK-002/004 may proceed while TASK-003 inputs are pending; their final acceptance still respects the dependencies above.

H01 provides H02 with the exact policy and terms/notices version/hash, approval source and intended-reader access status. H02 does not require H01's final archive or merge merely to prepare private guidance; it does require real text approval for its terms check. Product adoption and H03 distribution remain independent follow-up work.

Both changes currently share a checkout. Serialize shared index/README edits. Run affected checks against the final relevant combined inputs; a later sibling change or newly archived sibling dossier can alter a declared snapshot and require rerunning affected checks. This does not make either change's closure depend on the other's closure. Separate issues, approvals, results and assessments remain intact.

## Risks and execution stop conditions

Missing rights or contractual choices, unverified authority, inaccessible evidence and absent text approval block the affected task/check. No legal or security capability is inferred from the owner's assignment. Provider drift, a new architecture boundary or a changed license model requires review at the earliest affected gate. These are explicit future execution inputs and stop conditions; no new planning decision is silently delegated to implementation.

No blocker prevents reviewing Tasks R1. This is not a claim that every later operational prerequisite is already satisfied. An instruction limited to private documentary implementation would still not authorize public writes, effective license changes or distribution.

## Independent closure procedure

After accurate task completion and acceptance recording, run selected `--phase delivery --json`. If eligible, move the unique dossier to `specs/archive/portfolio-licensing-policy/`, set closure bookkeeping as required by the canonical process, verify references and run selected `--phase delivery --require-archive --json`. These mandatory lifecycle operations are separate from the six task completion conditions and CHECK-006. A failed guard reopens the affected state; `closure: prepared` is never a substitute for an observed pass.

Only separately authorized PR publication may follow local readiness. Required remote CI/review and actual merge remain separately observed. No release, terms activation, public documentation export or consumer adoption is part of this closure. Preserve recovery instructions and the previous reviewed navigation if later authorized delivery fails.

## Planning review

Tasks R1 is presented for Gate 3 after actual approval of Proposal/Requirements R1 and Design R1. All tasks are pending and unchecked; no implementation result, assessment or finding is prepopulated. The user's latest “Aprovado.” approved the presented Designs only. Approval of these Tasks does not by itself authorize execution.

2026-11-10: the user approved both presented Tasks R1 revisions and explicitly authorized private documentary implementation with the quote: "Aprovado. Inicie a implementação documental privada de H01/H02, sem publicar, aplicar licenças ou ativar canais. Sinalize as decisões que dependerem de mim.". The canonical Tasks digest matched the presented revision: `ac2e801e4908448c2e534f8865970d979dbb751097b11b89532ee7a26299c138`. This is current Gate 3 approval and scoped execution authority; earlier presentation-stage wording above is historical. Publication, license application, channel activation and synthetic messages remain outside the authorized scope.

## Progress

2026-11-10 technical review: owner provenance confirmed; H01 terms/notices documentary work and localized guidance complete. H02 approved-terms binding and private organization package complete. H02 channel verification stays blocked by the current no-activation/no-message scope; no new owner decision is needed. Current final acceptance guards remain separate from documentary completion.

2026-11-10: actual user approval “H01 revisado e aprovado.” recorded against the reviewed draft-0.2 hash; current terms differ only in administrative approval status. Relevant CODEOWNERS own monitoring/triage/remediation for both H02 routes; no role-definition question remains. Remaining component evidence and operational checks are separate. Affected previous check results were preserved and invalidated, not relabeled.

2026-11-10 routing decision implemented privately: public GitHub PVR with organization-default native template; private repositories email relevant CODEOWNERS through internal Versat contacts. Earlier tentative info@versat.ag selection is superseded. Affected prior check results are preserved in before-routing-decision.json, removed from current results pending fresh checks; no old result is relabeled with new inputs. Existing forms unchanged. No publication/activation/test message.

Private documentary implementation authorized by the actual Gate 3 reply on 2026-11-10. TASK-001/002 completed within their bounded inventory/rules completion criteria; no rights clearance or final acceptance implied. Remaining task statuses distinguish prepared drafts from blocked terms/channel and pending final acceptance. Owner decisions received: free official plugin use for Versat Labs contributions; authorized Versat developers may modify; users may not redistribute, commercialize or fork; company Paraguay, approver Elvis Luis Zoz. The earlier tentative info@versat.ag choice was superseded by the public-PVR/private-CODEOWNERS decision above. No public writing, license application, channel activation or synthetic message occurred. Earlier planning-only wording is historical; this Progress and structured status record are current.

## Validation evidence

Current final documentary observations and individual assessments are in `docs/validation/portfolio-licensing-policy/technical-review.md`, with current check reports, stable before/after input snapshots and selected validator outputs. The owner approved H01 wording and confirmed first-party provenance. No concrete user-input gap remains for this documentary scope. All planned local/regression obligations are assessed, without exclusions. Technical suites pass (131 validator plus 48 execution tests); aggregate acceptance remains blocked by required operational/lineage checks. Prior attempts remain preserved as historical evidence. H02's private package is complete; no publication, activation or message occurred.

## Delivery

Closure remains active. No archive, commit, PR, merge, policy adoption, effective license change or publication is claimed for this change.
