---
sdd_version: 3
change: harness-user-documentation
tasks:
  - id: TASK-001
    description: Refresh source baselines and prepare the two repository working copies.
    requirements: [REQ-001, REQ-003, REQ-004, REQ-006, REQ-007]
    status: completed
  - id: TASK-002
    description: Write the canonical product overview, workspace setup and first-use guide.
    requirements: [REQ-002, REQ-003, REQ-004, REQ-006]
    status: completed
  - id: TASK-003
    description: Write the remaining seven canonical workflow guides using existing references.
    requirements: [REQ-002, REQ-003, REQ-006, REQ-007]
    status: completed
  - id: TASK-004
    description: Complete the Harness README, navigation and all Portuguese and Spanish siblings.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006]
    status: completed
  - id: TASK-005
    description: Prepare the organization contribution consolidation and translated entry pages.
    requirements: [REQ-001, REQ-003, REQ-005, REQ-006, REQ-007]
    status: completed
  - id: TASK-006
    description: Review the prepared content, exercise first use and resolve documentation defects.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007]
    status: in-progress
  - id: TASK-007
    description: Bind organization links to an authorized published Harness content revision and verify targets.
    requirements: [REQ-001, REQ-003, REQ-005, REQ-006, REQ-007]
    status: pending
  - id: TASK-008
    description: Execute all final checks against stable inputs and record scenario and regression assessments.
    requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007]
    status: pending
  - id: TASK-009
    description: Prepare the coordinated delivery handoff and verify documentary closure prerequisites.
    requirements: [REQ-001, REQ-005, REQ-006, REQ-007]
    status: pending
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 1ca3de32bdea8b921030786aea349b2dc5a50a3a265aa75ee25a39e1b3308f24
    design: a0f7141be1f9302d1824c2c181457d1c243bf7c2f5722db505bcdd755af4652a
  approval:
    source: Developer reply in this chat after Tasks R1 approval and implementation authorization were requested together.
    quote: sim
    revision: 1
    digest: 3cfecbf06713997419537a7de6ab0e33e308641b0c37ad3ee68b078cf6e20a33
validation:
  plan_digest: null
  results: []
  assessments: []
  findings: []
closure: active
---

# Tasks

This plan implements approved Proposal/Requirements R2 and Design R1. All nine tasks are future work. Approval of this document completes planning; execution requires an explicit implementation request. Remote publication retains the scoped authorization boundaries in the approved Design.

## Implementation checklist

- [x] TASK-001 — Refresh source baselines and prepare the two repository working copies.
- [x] TASK-002 — Write the canonical product overview, workspace setup and first-use guide.
- [x] TASK-003 — Write the remaining seven canonical workflow guides using existing references.
- [x] TASK-004 — Complete the Harness README, navigation and all Portuguese and Spanish siblings.
- [x] TASK-005 — Prepare the organization contribution consolidation and translated entry pages.
- [ ] TASK-006 — Review the prepared content, exercise first use and resolve documentation defects.
- [ ] TASK-007 — Bind organization links to an authorized published Harness content revision and verify targets.
- [ ] TASK-008 — Execute all final checks against stable inputs and record scenario and regression assessments.
- [ ] TASK-009 — Prepare the coordinated delivery handoff and verify documentary closure prerequisites.

## Dependencies and completion conditions

Dependencies below establish execution order; task progress remains in the frontmatter and checklist. A logical commit may contain several related tasks. No task requires its own PR to have merged before it can complete.

### TASK-001 — Source baselines and working copies

**Dependencies:** approved Tasks and explicit implementation authorization.

Inspect the Harness working tree, current approved digests and selected source/provider. Obtain a suitable local working copy of `versat-labs/.github`, inspect its current `AGENTS.md`, default branch and unrelated changes, and preserve them. Use a scoped work branch for organization edits following its applicable rules. Refresh Issue #22 and the relevant organization source files; compare with the recorded Proposal baseline before editing.

Record the original organization Markdown, observed refs and per-file hashes under the Design's `docs/validation/harness-user-documentation/inputs/organization/` location. Include an inventory/hash comparison for unchanged issue forms and the profile. Preserve a content-ownership map that names the canonical Harness destination for every overlapping source section. Existing source facts do not authenticate current Codex UI or installation state.

**Complete when:** both working copies and their instructions are identified, source baselines are traceable, unrelated work is preserved and no unexplained material source drift remains. Material scope/behavior changes reopen the relevant planning gate; routine source refreshes do not invent a new product requirement.

**Checks supported:** CHECK-001, CHECK-004, CHECK-005.

### TASK-002 — Product context and first use

**Dependencies:** TASK-001.

Create the English `docs/product/overview.md`, `docs/user-docs/guides/workspace-setup.md` and `docs/user-docs/quickstart.md` using the approved content model. Describe the Issue #22 problem, JTBD and persona, current capability boundaries and explicit evidence gaps. Replace product template prompts with relevant content or reasoned non-applicability.

Reconcile organization setup guidance with available current evidence before reusing it. Keep prerequisites and missing-access recovery clear. The quickstart uses one labeled synthetic planning example, expects Proposal/Requirements and the Gate 1 stop, and links to setup and lifecycle detail. Retain the supplied Codex training link as access-restricted supplemental material without claiming its video contents were reviewed.

**Complete when:** all three pages contain useful canonical content, the representative first action and observable result are explicit, no unsupported UI/install claim or fabricated product metric remains, and required next destinations are identified for TASK-003/004 without presenting missing files as delivered.

**Checks supported:** CHECK-001, CHECK-003.

### TASK-003 — Focused workflow guides

**Dependencies:** TASK-001, TASK-002.

Create the English guides `sdd-with-codex.md`, `github-delivery.md`, `project-bootstrap.md`, `project-maintenance.md`, `project-audit.md`, `architecture-review.md` and `validation-and-evaluations.md` under `docs/user-docs/guides/`. Use the approved compact pattern with a representative request/action, real inputs, expected outputs, recovery and stopping conditions.

Reference `sdd/README.md`, canonical Standards/Skills and the existing specialized guides rather than reproducing full procedures. Preserve distinctions between bootstrap and maintenance, audit and remediation, approval and execution, archive preparation and merge, package checks and consumer suites, and current source versus installed availability. Preserve the supplied GitHub training link and its verification limit.

**Complete when:** the eight-guide inventory, including workspace setup from TASK-002, covers each approved user job with substantive content and accurate references; no second lifecycle, duplicate detailed manual or unsupported capability is introduced.

**Checks supported:** CHECK-001, CHECK-002, CHECK-003, CHECK-004.

### TASK-004 — README, navigation and Harness translations

**Dependencies:** TASK-002, TASK-003.

Revise the root README around purpose, audience, accountable team, current state, navigation and the validation entry point. Preserve necessary installation/version and package-versus-consumer information while linking to detailed guides. Link the actual organization contribution entry point where appropriate; do not create a duplicate local CONTRIBUTING manual.

Create aligned Portuguese and Spanish siblings for all eleven canonical Harness pages: 33 files total including the existing English README. Add language switches, localized user-document links and explicit English labels for existing untranslated technical references. Verify localized heading anchors and preserve code/path identifiers and operational meaning.

**Complete when:** the full Harness inventory is populated, every language route has real targets, useful existing README information is retained, and semantic alignment covers prerequisites, approvals, commands, caveats and examples. No empty locale file or unrelated technical-corpus translation is introduced.

**Checks supported:** CHECK-001, CHECK-002, CHECK-005.

### TASK-005 — Organization candidate

**Dependencies:** TASK-001, TASK-003, TASK-004.

Prepare the organization README and CONTRIBUTING changes with aligned English/PT/ES entry pages. Replace detailed reusable setup, process, validation/PR and language explanations with descriptive Harness links according to the approved ownership table. Preserve organization purpose, public participation routes, default-file behavior, repository precedence and organization-local validation.

Correct `AGENTS.md` file descriptions only where they become inaccurate; retain all applicable rules. Preserve the profile, allowing only the approved description adjustment if actually needed, and leave issue forms unchanged. The public reader must have a usable route without private Harness access.

Keep the candidate local and unactivated. During preparation, distinguish unresolved link refs in working notes; TASK-007 must resolve every URL before this task's draft can be delivered. Capture the candidate and its relation to the original snapshot for review without treating snapshots as another maintained manual.

**Complete when:** the organization diff is reviewable, its six README/CONTRIBUTING language files align, required local context and public fallback remain, duplication is removed from the candidate and any remaining exact-ref dependency is explicitly assigned to TASK-007. Completion here means candidate preparation, not final link verification or activation.

**Checks supported:** CHECK-001, CHECK-002, CHECK-004, CHECK-005.

### TASK-006 — Content review and observed usage

**Dependencies:** TASK-002, TASK-003, TASK-004, TASK-005.

Carry out CHECK-001 and the locally available parts of CHECK-002/004. Preview representative page types in each language. Follow the final first-use instructions and all newly introduced or materially changed runnable examples under CHECK-003 using synthetic data and a supported environment. Verify the Gate 1 stop and a missing-prerequisite recovery route. Reuse adequate current evidence only when it covers the same inputs and steps.

Retain actual attempts and findings at the approved `runs/<attempt>/` paths. Correct in-scope documentation defects and synchronize translations; repeat affected reviews/walkthroughs after corrections. Video content remains unreviewed unless an accessible source is actually inspected. An unavailable required UI or execution observation is unverified, not a pass.

**Complete when:** local content/translation issues are resolved, required usage outcomes have observed supporting evidence and the content is ready to be committed for the stable target revision. Required unavailable usage verification blocks this task; the separate remote-link prerequisite remains in TASK-007. These preparatory results cannot substitute for final checks against the complete stable input snapshot in TASK-008.

**Checks supported:** CHECK-001, CHECK-002, CHECK-003, CHECK-004.

### TASK-007 — Exact published destinations

**Dependencies:** TASK-006; scoped authorization to publish the concrete reviewed Harness content commit, or an already published matching revision whose identity and contents are verified.

Prepare the content commit and finalize the organization candidate URLs against its full immutable SHA. Present the concrete reviewed changes before requesting any missing publication authorization. Publish only within that authorization; this step does not authorize PR creation, merge, release or workspace administration.

Fetch each linked file at the actual published ref and verify its bytes, headings, locale and intended-reader access. Store the observed published target snapshots and provenance at the approved `inputs/published-targets/` location. Refresh the final organization candidate snapshot so it matches the actual organization working copy. Verify public fallback and the unavailable-target behavior without activating broken links.

**Complete when:** all organization-to-Harness links use a real published immutable revision, destination bytes/anchors and intended access have been verified, no placeholder ref remains, and snapshots match both reviewed candidates. If publication authority, target availability or access is missing, keep this task pending/blocked as appropriate and retain the existing organization entry guidance; do not claim CHECK-004 passed.

**Checks supported:** CHECK-002, CHECK-004.

### TASK-008 — Final validation and assessments

**Dependencies:** TASK-007 and stable candidate contents in both repositories.

Freeze the final input snapshots, confirm that the organization export matches its working copy and perform all five approved checks. Use the current Tasks plan digest and before/after check input digests, and store actual per-check outputs under `runs/<attempt>/`. All inputs must remain stable during a passing check. If inputs change, repeat affected checks rather than updating hashes on old results.

Record one current observed result per Design check and all 27 local plus 19 retained regression assessments. Use stable finding IDs for gaps and resolve them with current evidence. Keep historical failed/unverified attempts. Run the full maintained Harness validation suite and the organization repository's actual Markdown/diff checks; do not invent an application build for `.github`. Publication, final CI, PR reviews and merges remain separately observed facts.

**Complete when:** CHECK-001 through CHECK-005 have current passes, all 46 obligations have supported passing assessments, no required evidence or unresolved finding is concealed and both candidate diffs are coherent. CHECK-005's selected archival preflight is a later submission checkpoint after all tasks complete and the dossier moves; it is not falsely reported as executed here. Missing required observations prevent completion.

**Checks supported:** CHECK-001, CHECK-002, CHECK-003, CHECK-004, CHECK-005.

### TASK-009 — Delivery handoff and closure prerequisites

**Dependencies:** TASK-008.

Prepare Spanish PR summaries for both repository changes, referencing Issue #22 and this governed change, with the actual scope, validation, immutable documentation ref, remaining external delivery steps and rollback. Cross-link real PRs only after their creation is authorized and observed; do not invent URLs.

Review the final file inventory, task statuses, input/evidence freshness and requirement coverage. Verify the change can proceed to documentary archive preparation and that the organization candidate still preserves the public route and correct targets. Keep original organization content recoverable. Run phase-appropriate consistency checks; report pending remote review/CI/merge distinctly.

**Complete when:** both deliverables and their local evidence are reviewable, truthful delivery summaries and rollout/rollback instructions are prepared, and no implementation work remains before the administrative archive/submission checkpoints below. This task requires neither a PR nor a merge and does not claim either occurred.

**Checks supported:** CHECK-002, CHECK-004, CHECK-005.

## Execution order and limits

The dependency chain is TASK-001 → TASK-002 → TASK-003 → TASK-004 → TASK-005 → TASK-006 → TASK-007 → TASK-008 → TASK-009. These steps deliberately put a complete local candidate and local usage review before source publication. No parallel-agent execution or new validation framework is required by this plan.

All tasks remain pending at this planning stage. Runtime access and source publication are known execution dependencies, not evidence that those actions have been authorized or performed. If they are unavailable during execution, record the specific affected task/check as blocked or unverified, continue independent authorized work and report the concrete remaining dependency.

## Risks and recovery

- **Source drift:** refresh the organization baseline before editing and reconcile concurrent work; material scope changes reopen the appropriate gate.
- **Duplicate or inconsistent instructions:** compare each source section with the ownership map and synchronize translations after corrections.
- **Private access and unavailable targets:** retain a usable public route and do not activate the organization candidate until all linked destinations are verified.
- **Stale pinned revision:** if Harness documentation changes after the content commit, select a new reviewed content commit, rebind the organization candidate and repeat affected target/content checks; a pinned old snapshot is not evidence for a modified candidate.
- **Unverified usage:** preserve missing evidence as unverified. Do not substitute the package test suite for actual first-use observations.
- **Evidence drift:** original/candidate/published snapshots are inputs; reports are excluded outputs. Refresh snapshots before checks, never after execution to relabel old results.

## Administrative closure and external follow-up

After implementation tasks are complete, follow the canonical archive workflow in the same Harness branch: run delivery eligibility, move the unique dossier to `specs/archive/harness-user-documentation/`, set `closure: prepared` only when eligible, verify references after the move and run selected delivery with `--require-archive` before completed-work submission. These are existing documentary delivery operations, not a new product implementation task or a requirement for a PR to merge itself.

When separately authorized, publish the coordinated PRs and attach/link their real URLs, retaining the source commit and Issue #22 traceability. Observe each repository's mandatory review and final checks. Merge Harness first and organization routing second only under applicable authority. Confirm both merges and active links afterward; local task completion or documentary archive storage never proves activation or full external delivery.

If the organization delivery is still pending, state that explicitly even when the Harness change has merged. Rollback restores a verified organization entry/target first and affected Harness prose second, preserving the evidence and existing consumer pins.

## Planning review

The developer replied "sim" to the combined request to approve Tasks R1 and authorize implementation. This approves the bound Tasks digest and authorizes implementation. Proposal/Requirements R2 and Design R1 remain approved. Remote publication retains the scoped authorization requirements in Design.

## Progress

Tasks 001–005 are complete: all 33 Harness user pages and the organization candidate are written. TASK-006 is in progress. The same-session synthetic quickstart exercise produced only Proposal/Requirements, passed planning validation and preserved the home page. Local links and whitespace passed for both candidates; the full package suite passed (131 validator and 48 execution tests). Browser preview remains unavailable until the requested setting change takes effect. TASK-007 still requires scoped source publication authorization; no remote changes have been made. Organization preparation uses a local connector export, not a full remote clone; the supplied patch must be reapplied against a fresh remote baseline before actual publication.

## Validation evidence

No implementation checks have run for this Tasks plan. Results, assessments and findings remain empty. Planning-validator and repository regression runs performed while drafting this document validate the plan/current repository only; they are not CHECK-001 through CHECK-005 acceptance evidence for future documentation.

## Delivery

Closure remains active. Archival, PR publication, final remote checks, merge and organization activation are pending their prerequisites and authorization.
