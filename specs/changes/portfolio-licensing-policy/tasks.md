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
  status: pending
- id: TASK-002
  description: Implement the canonical licensing/publication Standard and evidence-based review ledger.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-004
  - REQ-005
  status: pending
- id: TASK-003
  description: Prepare concrete Harness/plugin terms and notices and obtain attributable approval of the exact candidate.
  requirements:
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-006
  status: pending
- id: TASK-004
  description: Add localized licensing guidance and connect existing navigation to the reviewed artifacts.
  requirements:
  - REQ-001
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: pending
- id: TASK-005
  description: Execute all approved checks and assess the complete acceptance and regression set.
  requirements:
  - REQ-001
  - REQ-002
  - REQ-003
  - REQ-004
  - REQ-005
  - REQ-006
  status: pending
- id: TASK-006
  description: Prepare the verified acceptance package and reconcile the private handoff state.
  requirements:
  - REQ-004
  - REQ-006
  status: pending
review:
  revision: 1
  state: superseded
  blockers: []
  upstream:
    proposal: 5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7
    design: 801894d789455496c072bc19b29947ff2c5900df09e4725d9d9e7c8d5f8acd55
  approval: null
validation:
  plan_digest: null
  results: []
  assessments: []
  findings: []
closure: active
---

# Tasks — H01

Change `portfolio-licensing-policy` · [Harness #34](https://github.com/versat-labs/versat-ai-harness/issues/34) · Tasks R1.
Executor and accountable licensing/security contact: Elvis Zoz (`@elviszoz`). Technical review follows CODEOWNERS, including Everton Spohr (`@evertonspohrversat`). Versat E.A.S. remains the user-declared rights holder, subject to actual component verification.

## Authorized stage and execution boundary

Proposal/Requirements R1 and Design R1 are approved. The current authorization is to prepare this Tasks plan. Every task below is pending. Approval of this document ends planning; implementing even the private candidate documents needs an explicit subsequent instruction, which may be combined with the Tasks approval after review.

The plan implements the approved private policy/terms candidate scope. It does not apply a root LICENSE, activate terms, publish repositories/content/releases, change permissions, activate channels, update consumers, implement product runtime or certify P01/P02/P03/H03 delivery. A concrete owner decision or approval cannot be supplied by an agent-authored record.

## Ordered work

- [ ] TASK-001 — Confirm the implementation baseline and collect the component rights and decision inputs.

  **Depends on:** current three planning approvals and explicit implementation authorization before starting.

  **Work:** compare the current executor checkout/remote baseline with the selected source `597b81c71a0fc0908ff5264fe9987bb5c0d8feec`, preserving unrelated changes and the exact provider. Reconfirm applicable AGENTS/index-resolved Standards and review relevant drift before applying this plan. Inventory the proposed Harness/plugin scope, original material, dependencies, copied code, templates/assets, notices and available rights/grant references. Obtain owner decisions needed for installation, use, modification, redistribution, audience and component scope, plus any entity details required by the eventual wording. Record confirmed facts versus missing inputs in `docs/governance/licensing-review.md`, with responsible follow-up. Keep confidential contracts and personal data outside the package. Do not conduct P01/H03 export clearance or infer permission from repository visibility.

  **Complete when:** the baseline and bounded inventory are documented; every unavailable rights/decision input has an explicit status and owner. Completion of inventory/scoping is not clearance. Missing permissions or rights may prevent TASK-003 and later acceptance even if this inventory task is complete. A materially changed contract/provider reopens the affected planning gate rather than silently changing the approved plan.

  **Evidence/checks:** the ledger becomes reviewed source input to CHECK-001/002/006; initial gaps remain pending evidence, not passing check results.

- [ ] TASK-002 — Implement the canonical licensing/publication Standard and evidence-based review ledger.

  **Depends on:** TASK-001's baseline; it can proceed while actual terms review is pending.

  **Work:** write `standards/core/licensing-publication.md`, add its single `core.always` index entry and complete the policy sections of the ledger. Preserve the selected public-Apache and proprietary-private routes, distinct per-product adoption, reviewer authority and publish/defer/retain-private dispositions. Define the complete export-review prerequisite without claiming that it has been performed. Add clearly synthetic success and failure examples for absent grants, incompatible dependencies, sensitive history, missing reviewer and unavailable controls. Coordinate the additive index change with H02; do not copy policy into Skills, change release refs or alter consumer locks.

  **Complete when:** the common policy resolves through the index, correctly distinguishes policy from licenses/operations, and all synthetic disposition cases have the expected documented result. Actual unreviewed product rows remain pending. Required evidence and authority cannot be waived by an example or role label.

  **Evidence/checks:** CHECK-001 and CHECK-003; retain actual observations for final validation on stable inputs in TASK-005.

- [ ] TASK-003 — Prepare concrete Harness/plugin terms and notices and obtain attributable approval of the exact candidate.

  **Depends on:** TASK-001's actual owner inputs/rights evidence and TASK-002's policy.

  **Work:** draft the non-operative `docs/licensing/harness-plugin-terms.md` and `harness-plugin-notices.md` from explicit owner decisions. Cover the exact component scope and installation/use/modification/redistribution permissions and conditions, third-party rights/notices and tool-versus-destination-project terms. Do not select unprovided contractual grants, jurisdiction, corporate details or signature authority. If required inputs or legal interpretation are unavailable, stop the dependent wording/approval work and ask the accountable owner for the concrete decision or appropriate review. Version and hash the actual candidate; obtain and record genuine acceptance of that precise text in the ledger, including reviewer capacity, source and limits. Any substantive text change requires renewed text review. No approval date, signature, grant or legal qualification is fabricated.

  **Complete when:** concrete terms/notices are substantively complete and the actual authorized reviewer has approved their exact version/hash, with required rights evidence available and no unresolved blocker to that approval. A generic policy, unreviewed draft, SDD approval or CODEOWNERS entry does not complete this task. Candidate approval remains separate from effective license application or distribution.

  **Evidence/checks:** CHECK-002. If evidence is missing, mark this task blocked during execution, keep the required check unverified and record a finding; do not weaken its completion condition to finish the plan.

- [ ] TASK-004 — Add localized licensing guidance and connect existing navigation to the reviewed artifacts.

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

Design R2 is awaiting approval. The R1 substantive task plan is superseded and retained unchanged; its completed work and actual outcomes remain in the historical r1-tasks.md record. Current progress is pending for this reopened revision, not a claim that earlier work or operational evidence never existed. No Tasks R2 is prepared yet.

## Validation evidence

Current ledger intentionally empty. R1 execution records remain in docs/validation and in the preserved r1-tasks.md copy. Design diagnostics are planning evidence only; no R2 check result, acceptance or delivery is claimed.

## Delivery

Active local review candidate, not ready for delivery. Remote draft PRs and the previous green CI remain unchanged. No merge or license application.

## Planning review

The downstream R1 review is superseded by pending Design R2. Its substantive task plan remains unchanged; R1 completion statuses are preserved in the historical copy. Current statuses are pending because R2 has not been approved or executed; no Tasks R2 is drafted before Gate 2. Previous approval and complete evidence ledger are preserved at `docs/validation/portfolio-licensing-policy/design-r2/r1-tasks.md`. Empty current validation records mean R2 has not executed; prior successful checks are not relabeled. Historical approval:

```json
{
  "revision": 1,
  "state": "approved",
  "blockers": [],
  "upstream": {
    "proposal": "5c6662b60f01a33fb143e481dbe0aa13551177a71c91c73b87e8f422c1f982e7",
    "design": "801894d789455496c072bc19b29947ff2c5900df09e4725d9d9e7c8d5f8acd55"
  },
  "approval": {
    "source": "User reply in this chat on 2026-11-10 after presentation of Tasks R1 for both handoffs and the Gate 3 question.",
    "quote": "Aprovado. Inicie a implementação documental privada de H01/H02, sem publicar, aplicar licenças ou ativar canais. Sinalize as decisões que dependerem de mim.",
    "revision": 1,
    "digest": "ac2e801e4908448c2e534f8865970d979dbb751097b11b89532ee7a26299c138"
  }
}
```
