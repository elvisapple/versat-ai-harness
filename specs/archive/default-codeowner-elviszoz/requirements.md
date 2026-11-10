---
sdd_version: 3
change: default-codeowner-elviszoz
requirements:
  - id: REQ-001
    statement: Repository paths without a more specific ownership rule resolve to elviszoz.
    acceptance:
      - A root file such as README.md resolves to @elviszoz through the fallback rule.
      - A file in a previously unmatched nested directory resolves to @elviszoz through the fallback rule.
  - id: REQ-002
    statement: Every existing specific ownership assignment remains unchanged and takes precedence over the fallback.
    acceptance:
      - All 12 specific entries from the PR base retain their patterns, order and both owners.
      - CODEOWNERS itself and representative files under standards, skills and tests retain @elviszoz and @evertonspohrversat as owners.
  - id: REQ-003
    statement: This change satisfies the existing SDD delivery contract using actual approvals and current validation evidence.
    acceptance:
      - Planning records retain actual approvals for the reviewed revisions before dependent stages advance; missing approvals remain pending.
      - Before delivery readiness is claimed, the unique dossier is archived with prepared closure and passes the required baseline-aware submission validation with all applicable checks recorded.
      - Empty or incomplete delivery selection remains rejected by the existing guard and its regression tests; neither validators nor workflow policy is weakened.
---

# Requirements

## Actors and context

Repository maintainers need ownership coverage, reviewers need preserved specific assignments, and the author needs an auditable delivery record for PR #36.

## Functional requirements

REQ-001 extends the unmatched-path case. REQ-002 preserves every existing specific assignment. REQ-003 completes the missing governance record under the current process.

## Non-functional requirements

Keep the change small and reviewable. Technical artifacts use English. Approval metadata must cite actual review evidence, and check outcomes must distinguish local validation from remote CI.

## Acceptance scenarios

The frontmatter scenarios are the canonical acceptance positions. Check coverage and execution methods will be specified at the Design stage after this revision is approved.

## Constraints and assumptions

Use Harness 0.3.0 and the existing PR branch. CODEOWNERS ownership does not grant repository access or independently prove that GitHub permissions and rulesets enforce review. No changes to those remote settings are requested. Preparing these documents does not resolve CI until the full approved delivery dossier is completed and validated.
