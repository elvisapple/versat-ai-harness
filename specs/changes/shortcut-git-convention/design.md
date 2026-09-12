---
change: shortcut-git-convention
requirements: [REQ-001, REQ-002, REQ-003, REQ-004]
adrs: []
validation:
  - Repository structural and Plugin validation
  - Git whitespace and local Markdown link checks
  - Manual acceptance scenario review
---

# Design

## Current state and resolved context

standards/index.yaml always selects core/language.md, core/documentation.md, core/git.md, core/security.md, core/testing.md and core/observability.md. The Harness has no declared .versat/project.yaml; no profile, domain or technology is invented for this policy-only change. Git policy already requires English commits, PRs and protected branches. Language policy assigns Spanish to internal PRs. CI validates repository and Plugin structure, not Git subjects or external Shortcut associations.

## Proposed design

Expand core/git.md as the canonical naming policy and add explicit Git artifact rows to core/language.md, preserving the existing language decision. Add optional Story context to proposal and PR templates and reference the resolved Git Standard from SDD workflow steps. Document the future parser contract in release guidance and current enforcement limits in validator documentation.

## Boundaries and contracts

No architecture boundary changes or new ADR are needed: ADR-0005, ADR-0010 and ADR-0011 remain applicable. Skills already resolve version-matched Standards; the index already includes Git for all profiles. Templates retain base composition. Story IDs supplement, rather than replace, stable SDD change IDs. Optional Story context stays in Markdown and does not change SDD metadata schemas.

## Data, security and permissions

Use illustrative Story numbers and generic examples without customer names or production data. No Shortcut credentials or API access are introduced. Human policy review and existing platform controls remain required.

## Operations and observability

The supplied [chID] prefix is preserved as a Versat extension to Conventional Commits. Future parsers must handle the marker explicitly. Naming alone does not demonstrate that the current Shortcut workspace associates branches, commits or PRs correctly; verify that behavior in the configured integration before relying on automation.

## Migration, rollout and rollback

Apply the convention to new work after adoption. Do not rename historical branches or rewrite commits to retrofit it. Prepare the policy on a branch and submit it through mandatory review. Release through semantic versioning and exact consumer references, leaving VERSION and current pins unchanged in this unreleased change. Rollback is a reviewed revert; consumers retain their pinned policy until explicitly updated.

## Alternatives considered

- Translate commits to Spanish: rejected because the supplied examples do not explicitly supersede the existing English requirement.
- Move the Story marker to a footer for strict Conventional Commits: rejected because the request preserves the leading marker and existing traceability.
- Introduce blocking commit linting now: deferred to preserve gradual adoption; it needs a separate design for commit ranges, generated merges, bots and workspace integration.
- Duplicate naming guidance in every Skill and profile: rejected because the canonical index already resolves Git policy.

## Validation plan

Run ./scripts/validate/run.sh and git diff --check. Check local Markdown links and manually review REQ-001 through REQ-004, including Story-less work, optional scope/body, type mapping, languages and squash behavior. Record external integration and human review as unverified until evidence exists.
