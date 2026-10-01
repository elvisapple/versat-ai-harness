---
sdd_version: 2
change: sdd-acceptance-regression
status: accepted
owner: versat
summary: Make SDD acceptance completeness and regression obligations traceable across
  current and historical changes.
risk: medium
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: 'Developer message in this conversation on 2026-10-01 approving the presented
      Proposal/Requirements R1 and requesting Design. Administrative link-only amendment:
      explicitly approved in the subsequent conversation response; original planning
      approval preserved by that authorization.'
    quote: Aprove o plano e avançe para o design.
    revision: 1
    digest: f94ce3cf326057fa19ba58542c9e8ccbfa2226b9d916eb07f7367ceb4e5d9b66
---

# Proposal

## Context and problem

The developer requested planning after reviewing the Harness testing lifecycle and the Spec Kit approach to requirement coverage, implementation convergence and regression across earlier changes.

The initial conversation inspected an older 0.2.0 checkout. This proposal uses Harness 0.3.0 at `ac69894`, fetched from `origin/main`, so that it extends the delivered contract rather than recreating it. This is work on the Harness source repository, not an upgrade of a consumer or installed Plugin.

The existing baseline already provides:

- v2 review records, stage digests and three human planning gates;
- deterministic requirement-to-design, required-check and task coverage;
- recorded check results, evidence references and delivery eligibility checks;
- policy requiring relevant acceptance scenarios, including error and boundary behavior, to be covered;
- preservation of living documentation and explicit legacy exemptions.

The executable validator checks recorded relationships and evidence references. It does not decide whether a test exercises all relevant acceptance behavior or whether the current implementation still satisfies it. The existing plan digest does not establish freshness against changed implementation files. The current contract also lacks explicit cross-change impact and regression records connecting current obligations to their historical sources.

Consequently, a linked passing check may leave another relevant scenario unverified, and a new change may overlook behavior introduced by an archived change. A historical passing result establishes neither current behavior nor current delivery readiness.

## Expected outcome

For each change, a reviewer can determine which requirements and scenarios were assessed, which checks support the assessment, what remains incomplete or unverified, and which earlier behaviors were preserved or intentionally replaced. Relevant regression checks remain executable after the originating dossier is archived. Current failures or missing evidence prevent a claim that validation or documentary closure is complete.

Semantic assessment by an agent or reviewer and deterministic enforcement have distinct responsibilities. The former interprets behavior and identifies gaps; the latter validates the declared contract and rejects inconsistent or incomplete records without claiming to prove semantic correctness.

## Scope

- Extend the existing planning coverage review to expose scenario gaps while reusing requirement, task and check identifiers.
- Define a validation review of implementation completeness, including completed tasks, with evidence-linked findings and an explicit correction/revalidation loop.
- Record affected current contracts and related changes, including archived sources, and distinguish preserved, extended and superseded behavior.
- Keep regression tests/evals in the active project suites and record risk-based selection, justified exclusions and current execution evidence.
- Extend the existing metadata and validator only where deterministic checks can enforce the declared acceptance, impact and evidence contract.
- Define evidence freshness, resumption and archive behavior without equating editable declarations or file existence with authenticated execution.
- Update canonical policy, lifecycle guidance, templates, usage examples and meaningful validator/agent evaluation cases during implementation.
- Provide explicit compatibility and exact-release adoption guidance for existing dossiers and consumers.

The approved four-file dossier, public `versat-sdd` entry point and three planning gates remain the default. Design will select the smallest sufficient representation; this proposal does not prescribe a new report file or a separate global test catalog.

## Out of scope

- Installing or adopting Spec Kit or its community extensions.
- Proving arbitrary software correctness, authenticating human approvals or replacing required CI and PR review with an LLM judgment.
- Automatically discovering every dependency, parsing every test framework, or building a project-wide test scheduler.
- Requiring universal TDD, fixed case counts, a new ID for every scenario, or exhaustive input enumeration.
- Rewriting delivered historical dossiers or fabricating historical validation results.
- Publishing a release, upgrading consumers, creating remote issues/PRs, merging or deploying as part of this planning request.

## Work tracking

- Change ID: `sdd-acceptance-regression`.
- Local branch: `codex/sdd-acceptance-regression`, based on `origin/main` at `ac69894`.
- No Shortcut Story is associated or supplied; no Story identifier or type is invented.
- The developer authorized planning in the conversation with: “Sim. Encaminhe o planejamento dessa mudança proposta.” This is not approval of unseen artifacts or authorization to implement.

## Baseline and related work

Resolve Standards from [the repository index](../../../standards/index.yaml) at this source revision. All `core.always` policies apply. The Harness root has no `.versat/project.yaml`; no consumer profile, domain or criticality selection is invented. The proposal risk is the risk of this change, not a consumer identity declaration.

- [SDD metadata](../../../sdd/metadata.md) and [the current validator](../../../validators/sdd/validate.py) are the implementation baseline.
- [ADR-0013](../../../docs/decisions/0013-consolidated-sdd-workflow.md) and [consolidate-sdd-workflow](../../changes/consolidate-sdd-workflow/requirements.md), especially REQ-004 through REQ-006, establish the existing metadata and governance controls to preserve.
- Archived [quickstart-scenario-coverage](../../archive/quickstart-scenario-coverage/requirements.md), especially REQ-004 through REQ-006, establishes scenario coverage, reusable evidence and proportionality. Extend its policy without altering that historical dossier. Its change-specific exclusion of new metadata is historical scope, not a permanent ban on a separately governed extension.
- [Testing](../../../standards/core/testing.md) remains the canonical policy; [the process](../../../sdd/process.md) owns lifecycle behavior and validators own deterministic enforcement.

Spec Kit is an external design reference, not normative authority: its [analysis](https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md), [convergence](https://github.com/github/spec-kit/blob/main/templates/commands/converge.md) and [spec evolution](https://github.com/github/spec-kit/blob/main/docs/guides/evolving-specs.md) informed the requested outcome. These moving links are background references; the acceptance contract below is self-contained and does not depend on future upstream changes.

## Impact and risks

- Overly detailed bookkeeping could duplicate tests and specs. Reuse existing artifacts and allow one check to support several scenarios or requirements when its evidence supports them.
- New fields or readiness rules could invalidate old dossiers. Design must make versioning and adoption explicit while preserving historical records and preventing silent exemptions for new work.
- False confidence could come from a semantic verdict, editable revision label or existing evidence file. State the trust boundary and keep uncertainty visible.
- Reusing change-local `REQ-001` identifiers without their source could mix unrelated obligations. Cross-change references must be unambiguous.
- Intentional behavior changes could be misclassified as regressions. Preserve the distinction between an approved contract change and an unintended loss of retained behavior.
- Corrective work could bypass planning gates. Apply existing revision rules whenever approved scope, design or task content changes; routine fixes within the approved plan retain the existing execution rules.

## Proposal acceptance criterion

The planned solution addresses all requirements in [requirements.md](requirements.md) and demonstrates them with positive and negative cases, including a later change affecting an archived requirement, a missed boundary scenario despite another passing check, stale evidence after an implementation change, and explicitly superseded behavior. Existing SDD approval, archive, legacy, security and composition controls remain effective.

## Planning review

- Stage: Proposal/Requirements R1, approved by the developer in this conversation on 2026-10-01.
- Approval quote: “Aprove o plano e avançe para o design.”
- Approved content digest: `a6f879e8ab8465d45a37049278b22ebb2a0c295adf9e453c48f19d2fb90db1cb`.
- Material blockers for this review: none.
- Metadata representation, freshness mechanism, compatibility version and any necessary ADR are Design decisions after Gate 1 approval.
- Approval unlocks Design R1. Tasks and implementation remain subject to their subsequent gates; no implementation authorization is inferred.
- Administrative link amendment explicitly authorized by the developer in the conversation: “Sim. Mas antes revise o que falta no harness para que seja exigido arquivamento antes do PR e faça o ajuste necessário.” The one-line relocation-safe correction was presented before this authorization. Original Proposal digest: `a6f879e8ab8465d45a37049278b22ebb2a0c295adf9e453c48f19d2fb90db1cb`. Scope and Requirements are unchanged; existing planning approvals are preserved under this explicit exception.

- Current Proposal digest after the authorized link amendment: `f94ce3cf326057fa19ba58542c9e8ccbfa2226b9d916eb07f7367ceb4e5d9b66`.
