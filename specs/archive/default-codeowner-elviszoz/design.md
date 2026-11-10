---
sdd_version: 3
change: default-codeowner-elviszoz
requirements: [REQ-001, REQ-002, REQ-003]
adrs: []
validation:
  - id: CHECK-001
    description: Review fallback precedence and preservation of specific owners against the PR base
    requirements: [REQ-001, REQ-002]
    required: true
    method:
      kind: review
      procedure: Compare .github/CODEOWNERS against base 597b81c71a0fc0908ff5264fe9987bb5c0d8feec; verify the leading fallback and all 12 unchanged subsequent rules; apply GitHub last-matching-rule semantics to README.md, an unmatched nested file, CODEOWNERS and representative standards, skills and tests files; expect the owners in the acceptance scenarios.
      reason: The repository has no maintained CODEOWNERS matcher; an explicit bounded review avoids claiming a new parser matches GitHub semantics.
    inputs:
      include: [.github/CODEOWNERS]
      exclude: []
    outputs: []
    execution: local
  - id: CHECK-002
    description: Verify real approvals and delivery readiness with existing validation
    requirements: [REQ-003]
    required: true
    method:
      kind: review
      procedure: Review recorded approval quotes and stage digests against the actual chat, verify scenario assessments and recorded results, run ./scripts/validate/run.sh and review existing tests; assess delivery evidence before archive preparation. Run selected delivery validation before the move and the baseline-aware submission guard after archive preparation as separate delivery preflight steps. Confirm remote CI separately after any authorized publication.
      reason: Approval authenticity and evidence require human review in addition to deterministic checks.
    inputs:
      include: [specs, sdd, validators, tests, scripts/validate, .github/workflows/validate.yml, .github/CODEOWNERS, requirements-validation.txt]
      exclude: []
    outputs: []
    execution: local
coverage:
  - scenario: {requirement: REQ-001, scenario: 1}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-001, scenario: 2}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-002, scenario: 1}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-002, scenario: 2}
    applicability: required
    checks: [CHECK-001]
  - scenario: {requirement: REQ-003, scenario: 1}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-003, scenario: 2}
    applicability: required
    checks: [CHECK-002]
  - scenario: {requirement: REQ-003, scenario: 3}
    applicability: required
    checks: [CHECK-002]
regression:
  - obligation: {impact: 1, scenario: 0}
    checks: [CHECK-001]
    rationale: Compare every existing ownership entry and exercise representative specific paths.
  - obligation: {impact: 2, scenario: 0}
    checks: [CHECK-002]
    rationale: Run the existing complete suite, including the empty-selection regression, and review that governance enforcement is unchanged.
review:
  revision: 3
  state: approved
  blockers: []
  upstream:
    proposal: a9d71d5ce472824ef7d24e4e0055dc894838be94fbf0f65e737fb01f59ec6eb8
  approval:
    source: "User chat response to Design revision 3 approval request"
    quote: "sim"
    revision: 3
    digest: ad4951502141c954366e8662e6cced82caf2a3971ca8acbb2dd02ba9886d3a7b
---

# Design

## Current state

PR #36 places the default rule above 12 existing specific rules. CI fails because no affected SDD dossier was selected. Proposal and Requirements revision 2 are approved; the implementation predates that approval and must be independently checked.

## Proposed design

Retain the existing ownership change and complete this dossier under the current lifecycle. Review the base and final CODEOWNERS files and representative paths; record actual approval and validation evidence; prepare the dossier for archive only when its prerequisites are satisfied. No change to the submission guard is planned.

## Boundaries and contracts

The version 0.3.0 Harness process governs the dossier; standards/index.yaml resolves applicable Standards. GitHub interprets CODEOWNERS patterns. This work does not change project architecture, consumer contracts, permissions, rulesets or required checks. No ADR is needed for this bounded configuration and documentary change.

## Data, security and permissions

Ownership references existing GitHub accounts and grants no access. Validate that specific rules retain both owners. No sensitive data or new dependencies are introduced.

## Operations and observability

Local checks provide reproducible evidence; remote CI is a separate observation and is not assumed successful. Review the workflow output and selected revision after any authorized update.

## Migration, rollout and rollback

No consumer migration or release is required. The PR supplies the ownership change and documentary archive together. If ownership routing is wrong, restore the prior CODEOWNERS rules through a reviewed change; do not rewrite approval history. Publishing, merge and remote configuration remain separately authorized.

## Alternatives considered

Disabling the archive guard would violate the current contract and weaken enforcement. Inventing a completed dossier would misrepresent approvals and evidence. A new parser solely for this small change would add maintenance and could diverge from GitHub; use bounded review instead.

## Validation plan

CHECK-001 covers all fallback and preserved ownership scenarios by base comparison and explicit representative matching. CHECK-002 covers genuine approval sequencing and the existing submission-guard regression through review plus the complete validation suite. Selected delivery validation is a pre-archive prerequisite; the archive guard is a separate post-move preflight and is not a prerequisite to its own execution. Record actual observations and input revisions rather than treating these planned checks as results. Existing CI remains required.

## Planning review

Design revision 2 approval (user response: "sim", digest e0c82ab584c28c963be8292c846eb6b4594c229807a75e4ae68f38cfd11b3a55) is superseded by Proposal/Requirements revision 2. Design revision 1 was approved in the user chat (response: "sim"). Revision 2 separates pre-archive delivery validation from the post-archive guard to remove the circular dependency; it was approved in the user chat (response: "sim"). Design revision 3 corrects the verified count to 12 and binds Proposal/Requirements revision 2. This revision was approved in the user chat (response: "sim"). Tasks revision 3 is presented for review.
