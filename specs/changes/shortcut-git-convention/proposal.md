---
change: shortcut-git-convention
status: implemented
owner: versat
summary: Adopt Shortcut-linked branch names and typed commit messages
risk: medium
---

# Proposal

## Context and problem

The supplied business convention introduces Shortcut Story IDs in branch names and commit subjects, with an initial mapping from Feature, Bug and Chore to feat, fix and chore. The current Git Standard requires concise English commits but defines no naming format. The Spanish examples in the supplied document do not explicitly replace the canonical language policy.

## Expected outcome

Contributors can apply the convention through one canonical Git Standard, with SDD and Pull Request prompts that preserve Story traceability without changing the delivery lifecycle.

## Scope

- Define branch and commit formats, optional bodies and scopes, logical commit units and gradual adoption.
- Clarify English technical descriptions and Spanish internal Pull Requests.
- Connect SDD proposals and review steps to the resolved Git Standard.
- Document parser compatibility and the limits of current validation.

## Out of scope

- Changing architecture, Shortcut configuration, merge strategy or protected-branch rules.
- Introducing commit linting, automated changelogs or releases.
- Rewriting existing Git history or changing consumer version pins.

## Work tracking

No Shortcut Story ID or type was supplied. Do not invent one. Local preparation uses the existing executor branch convention; associate a real Story if one is provided.

## Impact and risks

This is a corporate policy change requiring a branch, Pull Request, mandatory review and required checks before merge. All profiles resolve core/git.md through standards/index.yaml. Installed consumers receive the policy only through a reviewed, exact version update. A leading Shortcut marker is not strict Conventional Commits syntax, so stock parsers cannot be assumed compatible. The workspace's actual Shortcut linkage has not been verified.

## Proposal acceptance criterion

The documented convention is applicable without duplicate policies in Skills, language conflicts or claims of automation that the Harness does not implement.
