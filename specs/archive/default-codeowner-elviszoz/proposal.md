---
sdd_version: 3
change: default-codeowner-elviszoz
status: proposed
owner: elviszoz
summary: Add default repository ownership while preserving specific owners and completing the required delivery record.
risk: low
impact:
  state: assessed
  summary: Inspected CODEOWNERS, the archived agent-project-layout requirements and documentation review, the SDD submission contract, and its maintained validator tests. Existing specific ownership and submission gates remain effective; previously unmatched paths gain a default owner.
  items:
    - current_contract:
        change: default-codeowner-elviszoz
        artifact: proposal
        locator: '## Current contract baseline'
      effect: extend
      targets: [REQ-001, REQ-002]
      reason: Add fallback ownership without replacing the existing specific rules or their two owners. Historical layout requirements do not define a separate default-ownership scenario.
    - current_contract:
        change: default-codeowner-elviszoz
        artifact: proposal
        locator: '## Current contract baseline'
      effect: preserve
      targets: [REQ-003]
      reason: Supply this change's missing delivery record through the current lifecycle; preserve the submission guard and its existing regression tests.
review:
  revision: 2
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: "User chat response approving Proposal and Requirements revision 2"
    quote: "Aprovo a revisão 2 da Proposta e dos Requisitos, com a contagem corrigida. Pode continuar."
    revision: 2
    digest: a9d71d5ce472824ef7d24e4e0055dc894838be94fbf0f65e737fb01f59ec6eb8
---

# Proposal

## Context and problem

PR [#36](https://github.com/versat-labs/versat-ai-harness/pull/36) adds a default CODEOWNERS entry but contains no SDD dossier. Its head is `e21976a2f7d4ba17239d76565078c12148d8d9ac`, based on `597b81c71a0fc0908ff5264fe9987bb5c0d8feec`.

[CI run 42895576783](https://github.com/versat-labs/versat-ai-harness/actions/runs/42895576783/job/130107716849) passed package validation, 131 validator tests and 48 execution tests, then failed overall because the SDD guard reported `ARCHIVE_SELECTION: No affected dossier selected`. Dependencies were installed successfully in CI. Node.js deprecation and runner migration notices were not the failing condition.

## Expected outcome

All repository paths have a default owner, existing specific assignments remain intact, and the same PR carries a genuinely reviewed and validated SDD dossier before delivery. This proposal documents existing implementation for prospective review; it does not assert retrospective approval.

## Scope

- Retain the proposed `* @elviszoz` fallback before all existing specific rules.
- Verify fallback behavior and preservation of both owners for specifically covered paths.
- Complete this change's planning, execution evidence and documentary archive through Harness 0.3.0.
- Run the existing validation entry point with the PR baseline and submission guard before claiming delivery readiness.

## Out of scope

Changing SDD policy, weakening validators, bypassing required checks, changing GitHub permissions or rulesets, updating action versions, publishing comments, pushing changes, merging, and modifying consumer projects.

## Work tracking

The existing work item is PR #36 on `chore/default-codeowner-elviszoz`. No Shortcut Story is associated in the available context. The stable SDD ID is `default-codeowner-elviszoz`.

## Impact and risks

This is a repository governance configuration change with no executable product behavior or architecture boundary change. Incorrect rule ordering could replace specific ownership with the fallback. Unsupported approval or validation records could falsely imply delivery readiness. Preserve actual approval sources and current check evidence.

Applicable core Standards are resolved through `standards/index.yaml`, notably Git governance, testing, documentation and language. No consumer profile or technology adoption is involved. Existing ownership context was inspected in `specs/archive/agent-project-layout/requirements.md` and `documentation-review.md`; no historical dossier is modified.

## Current contract baseline

At the PR base, `.github/CODEOWNERS` has 12 specific entries, all assigning `@elviszoz @evertonspohrversat`: CODEOWNERS itself, AGENTS.md, skills, agents, project-templates, standards, sdd, docs/decisions, validators, tests, scripts/validate and requirements-validation.txt. There is no fallback, so paths such as README.md and a new top-level directory do not match a rule. The PR head prepends the fallback and a blank line, retaining all 12 entries.

The current submission contract in `sdd/process.md`, `sdd/metadata.md` and `.github/workflows/validate.yml` requires an affected archived/prepared dossier for non-draft PRs. `validators/sdd/validate.py` rejects empty selection, and `tests/validators/test_sdd_v3.py::test_pr_submission_missing_or_empty_selection_fails` preserves that behavior. No existing dossier covers this default-owner change.

## Proposal acceptance criterion

Requirements describe the fallback, retained specific assignments and truthful delivery readiness with no change to the existing submission policy.

## Planning review

Revision 1 was approved by the user: "Aprovo a revisão 1 da Proposta e dos Requisitos. Pode avançar ao desenho da solução." Revision 2 corrects the base count from 13 to 12 after direct verification; it was approved in the user chat with the explicit corrected-count approval.
