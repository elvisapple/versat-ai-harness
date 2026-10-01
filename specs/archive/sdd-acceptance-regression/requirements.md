---
sdd_version: 2
change: sdd-acceptance-regression
requirements:
  - id: REQ-001
    statement: Planning MUST expose coverage of relevant acceptance scenarios by planned work and checks before implementation readiness is claimed.
    acceptance:
      - Given success, error and boundary scenarios for a requirement, when planning is reviewed, then each relevant scenario is associated with planned checks and work, and uncovered scenarios are reported even if another check references the requirement.
      - Given existing checks covering several scenarios or requirements, when planning is prepared, then those checks may be reused without duplicate tests, a separate case catalog or a new identifier for every scenario.
      - Given a scenario excluded as inapplicable, when planning is reviewed, then the exclusion has a reviewable scope-based reason and cannot silently remove an applicable obligation.
  - id: REQ-002
    statement: Validation MUST assess current implementation completeness against each requirement and relevant acceptance scenario independently of task completion declarations.
    acceptance:
      - Given all tasks marked completed but a required behavior absent or partial, when validation runs, then the gap is linked to its requirement and scenario and validation is not reported complete.
      - Given code contradicting the approved intent or adding behavior outside it, when the implementation is assessed, then the conflict or scope concern is reported with observed evidence for review.
      - Given an unavailable environment or no behavioral evidence for an applicable scenario, when validation reports its result, then it remains unverified with a reason rather than passing on the strength of metadata or an unrelated test.
      - Given coverage of every applicable obligation supported by current passing checks and review, when validation concludes, then it distinguishes semantic assessment, executed checks and deterministic contract validation in its report.
  - id: REQ-003
    statement: Findings MUST feed a traceable correction and revalidation loop that preserves the existing authorization and planning revision rules.
    acceptance:
      - Given a validation-only request with a finding, when the review ends, then the finding identifies its source obligation and needed correction without silently changing implementation or acceptance criteria.
      - Given authorized implementation and a routine defect within the approved plan, when it is corrected, then affected checks are rerun and the finding is reassessed without inventing another planning gate.
      - Given remediation requiring changed requirements, design or task-plan content, when further work is proposed, then the earliest affected gate is reopened and obsolete downstream approvals are not reused.
      - Given repeated validation, when a finding is resolved or remains open, then the report preserves traceability and does not create duplicate corrective work for the same unresolved gap.
  - id: REQ-004
    statement: Each change MUST declare the impact on relevant existing contracts and related changes, including archived sources, without treating historical text as automatically current.
    acceptance:
      - Given a new change affecting behavior introduced by an archived change, when planning occurs, then the impact identifies the source change and requirement, the current contract or documented baseline, and whether that behavior is preserved, extended or superseded.
      - Given two source changes both containing REQ-001, when impact references are resolved, then their identities remain distinct and the intended source is unambiguous.
      - Given an intentional replacement of an earlier behavior, when the new requirements are approved, then the replacement and its rationale are explicit, current specifications are updated with implementation and delivered history remains unchanged.
      - Given no affected earlier contract, when impact is assessed, then an explicit justified no-impact conclusion is sufficient without fabricating dependencies or reviewing every historical dossier.
      - Given an affected source or current contract that cannot be established, when readiness is assessed, then the missing context is reported as unresolved and is not silently treated as no impact.
  - id: REQ-005
    statement: Relevant retained behavior MUST remain covered by maintained regression tests, evals or justified explicit checks that continue to apply after dossier archival.
    acceptance:
      - Given an archived change that introduced duplicate-payment prevention and a new change altering payment processing, when validation runs, then current evidence verifies both the new behavior and retained duplicate prevention, even when only the new happy path passes.
      - Given an existing adequate regression test, when a new change affects its behavior, then the test is reused in the active project suite and linked to the current validation obligation without being moved into the archive.
      - Given a selected regression set, when the plan is reviewed, then its affected behaviors and selection rationale are visible, required suites remain required in CI and omitted relevant checks need an explicit justification.
      - Given behavior that cannot be usefully automated, when coverage is planned, then an explicit manual or other suitable check records the reason, method and actual outcome; inability to execute it remains unverified.
      - Given approved supersession of a behavior, when its regression tests are changed or retired, then the change traces to that approved replacement and a failing test is not deleted merely to obtain a pass.
  - id: REQ-006
    statement: Acceptance and regression evidence MUST identify the assessed plan and implementation state and MUST be renewed when relevant changes invalidate it.
    acceptance:
      - Given previously passing evidence followed by a relevant implementation, test, fixture or execution-configuration change, when validation resumes, then affected results are treated as stale until rerun even if the Tasks plan digest is unchanged.
      - Given changed requirements or scenario/check mappings, when previous evidence is considered, then it cannot establish readiness under the revised plan without renewed validation.
      - Given an evidence file or HTTPS run reference, when it is recorded, then the outcome identifies the exercised check and assessed revision or snapshot, while the report distinguishes observed execution from a declared reference whose authenticity was not verified.
      - Given documentary archival without changed assessed behavior, when the dossier moves, then evidence references remain valid and neither the move nor an old passing result is presented as proof of merge or deployment.
  - id: REQ-007
    statement: Deterministic validation MUST enforce the declared coverage, impact and evidence contract while reporting its semantic and execution trust limits.
    acceptance:
      - Given malformed, duplicate, dangling or ambiguous references within the selected validation scope, when the validator runs, then it reports actionable failures identifying the affected source records.
      - Given an otherwise well-formed record with an applicable obligation declared failed, missing, unverified or detectably stale, when delivery readiness is checked, then it returns fail or unable-to-verify rather than pass.
      - Given a Proposal/Requirements draft with later stages absent, when planning validation runs, then no execution result or implementation artifact is required prematurely.
      - Given well-formed declared coverage and passing evidence references, when deterministic checks pass, then the output does not claim that test assertions are sufficient, an LLM verdict is correct or a remote execution was authenticated.
  - id: REQ-008
    statement: Adoption MUST preserve established SDD governance and immutable history and provide tested, proportional instructions for the extended contract.
    acceptance:
      - Given a delivered archived or explicitly exempt legacy dossier, when the new contract is introduced, then its historical bytes and approval evidence are not silently rewritten and new obligations follow a documented versioned compatibility policy.
      - Given new work extending a historical change, when it is planned, then missing old tests or evidence become visible obligations of current work rather than fabricated retrospective approvals or passes.
      - Given implementation of this contract, when repository validation runs, then behavioral tests cover valid cases and failure cases for coverage, cross-change references, regression evidence, stale results, gate sequencing and archive behavior.
      - Given a developer using the revised lifecycle, when following the guide and examples, then acceptance review, regression selection and correction/resumption are understandable through the existing public skill and four primary dossier files.
      - Given a consumer pinned to an older release, when this source change is delivered, then adoption remains an explicit reviewed update to an exact release and template composition still extends base.
---

# Requirements

## Actors and context

Developers and coding agents plan and implement changes. Reviewers assess whether observable requirements are satisfied and retained behavior remains intact. Local validators and CI check records and execute project suites within their respective authority. Maintainers approve policy and release adoption.

The baseline is Harness 0.3.0 and its v2 SDD contract. This is an extension of the delivered scenario-coverage and evidence rules, not a replacement lifecycle. It applies proportionally to software, agent, library, infrastructure and policy/documentation changes; the appropriate verification method varies with the artifact and risk.

## Functional requirements

REQ-001 through REQ-003 define planning coverage, acceptance assessment and correction. REQ-004 and REQ-005 define cross-change impact and retained-behavior verification. REQ-006 and REQ-007 define current evidence and deterministic enforcement. REQ-008 defines compatible adoption, documentation and verification of the Harness changes themselves.

## Non-functional requirements

- Reuse existing requirements, checks, tests, evals and evidence where they are sufficient. Do not require one test per requirement, a parallel scenario catalog, fixed coverage percentages or universal TDD.
- Keep policy in Standards resolved through the index, lifecycle instructions in SDD, routing in Skills and deterministic checks in validators. Preserve security restrictions on evidence paths and sensitive data.
- Keep default local structural validation independent of network access and external services. Missing semantic or external verification must remain explicit.
- Bound impact analysis to affected behavior and its justified dependencies. Absence of an automatically discovered link is not evidence that no dependency exists.
- Keep assessment records understandable to reviewers and failures actionable. A pass is limited to the checks actually performed and the stated scope.

## Acceptance scenarios

The frontmatter scenarios are the canonical acceptance scenarios for this change. Design will map them to planned checks and distinguish deterministic fixtures from agent/reviewer behavioral evaluations. Payment processing is a synthetic example for cross-change regression; it does not add a finance integration to the Harness.

## Constraints and assumptions

- Preserve the three planning gates and separate implementation authorization. Proposal/Requirements approval unlocks Design only.
- Preserve the existing four primary artifacts and single `versat-sdd` entry point. Extend their contracts where justified rather than requiring a new primary dossier file.
- Schema representation, stable scenario referencing without mandatory new IDs, freshness detection scope and metadata-version compatibility are decisions for Design. The implementation must disclose what can and cannot be detected mechanically.
- An unverified or stale relevant check cannot be waived by calling it inapplicable. Exclusions concern accepted scope and require a reviewable reason; scope changes follow existing gate rules.
- Cross-change impact records must distinguish historical origin from the currently effective contract. Where no living specification exists, establish and review the affected current baseline rather than assuming every archived requirement still applies.
- No material unresolved decision blocks Proposal/Requirements R1 review. This stage records intended outcomes and does not claim implementation readiness or completed tests.
