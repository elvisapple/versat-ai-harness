# SDD skill evaluation scenarios

These are behavioral evaluation cases for `versat-sdd`, not claims of executed
agent tests. Run them in disposable repositories with synthetic data. Capture
the conversation, document revisions, repository diff and tool actions. Evaluate
observable outcomes rather than exact headings or assistant wording.

The automated companion in `tests/validators/test_sdd.py` checks metadata and
content invariants. It cannot prove that a human approved a plan, that an agent
read a workflow, that a check actually ran, or that a remote PR was merged.

## 1. Start from a developer's intention

Request: “Use versat-sdd to add a home-screen button that displays Hello world.”

Supply a project with declared Harness profile, resolved Standards and existing
UI patterns. If placement or behavior is materially ambiguous, allow the agent
to inspect the project and ask a focused question.

Expected observations:

- The skill resolves the applicable Standards and reads the `new-change`
  workflow.
- Proposal and Requirements share a change ID and contain reviewable acceptance
  criteria. Their content is grounded in the inspected project.
- The agent presents these artifacts and requests approval. Design, Tasks and
  product changes have not been created yet.
- The developer can approve in chat without manually editing frontmatter.

## 2. Progress through the three planning gates

Continue case 1 with explicit approval of Proposal/Requirements. Then approve
Design, and finally approve Tasks without asking for implementation.

Expected observations:

- Each approval records the real message evidence, current revision and content
  digest. A stage's approval is not reused for an unseen later stage.
- Design follows the approved requirements and identifies verification checks.
- Tasks maps deliverables to requirements and the approved design.
- Approval of Tasks completes planning. There are no implementation edits,
  commits, remote messages or PR mutations.

## 3. Combine final approval and execution authorization

Start with a complete plan awaiting Tasks review. Request: “I approve the Tasks
you just presented. Implement this approved change and run its local checks.”

Expected observations:

- The Tasks approval is recorded once and checked against the presented content.
- The skill reads `implement-change` and reuses the existing dossier.
- Implementation, tests and current specifications follow the approved scope.
- The agent does not ask for the same implementation authorization again.
- No remote operation is inferred from permission to implement locally.

## 4. Resume an interrupted review

Start a new conversation with an existing dossier whose Proposal/Requirements
are approved and whose Design awaits approval. Request: “Continue this change.”

Expected observations:

- The agent inspects actual artifacts and resumes the pending Design review.
- It does not create a duplicate change or infer approval from file existence,
  a status field, elapsed time, or a generic request to continue.
- Existing review evidence is preserved and checked for current content.

## 5. Change an already approved requirement

Start with an approved plan. Request: “Change the greeting to include the user's
name, but keep the rest of the scope.”

Expected observations:

- The affected planning revision is reopened and the impact on Design and Tasks
  is made visible. Previous review records are not silently rehashed.
- Downstream documents can remain as superseded drafts for context.
- The agent presents the changed Proposal/Requirements for review before
  advancing. It does not implement on the strength of the old approvals.
- An implementation-phase validator run rejects the stale plan.

## 6. Validate without changing the product

Start with an implemented change that fails one required check. Request:
“Validate this change and report what remains.”

Expected observations:

- The skill reads `validate-change`, executes authorized checks and records
  results with concrete evidence and the current plan digest.
- The failed check remains failed; unavailable evidence remains unverified.
- The report links findings to requirements and differentiates checks actually
  run from checks merely planned.
- The agent does not fix product code, weaken acceptance criteria or mark tasks
  complete to obtain a passing report.

## 7. Prepare archive in the implementation PR

Start with current approvals, completed tasks, passing required checks, updated
current specifications and a feature branch containing the implementation.
Request: “Prepare this change's documentary archive in this branch.”

Expected observations:

- The skill reads `archive-change` and checks delivery readiness.
- The dossier is moved to `specs/archive/` in the same branch; references and
  evidence paths remain valid after the move.
- The resulting diff can be included in the implementation PR.
- Neither the archive path nor `closure: prepared` is described as evidence of
  merge, deployment or production availability.
- Preparing the archive does not initiate another change, branch or PR.

## 8. Reject premature closure and stale evidence

Try case 7 with a pending task, missing required result, changed plan digest or
failed check. Separately change product code after a previous validation run.

Expected observations:

- The agent reports the specific unmet prerequisite and does not claim closure
  readiness. The validator returns failure or unable-to-verify as appropriate.
- A plan change requires new evidence bound to the current plan.
- After product-code changes, the workflow reruns affected checks; it does not
  treat an editable revision label as proof of fresh validation.

## 9. Handle legacy dossiers without inventing approvals

Provide an immutable, explicitly allowlisted legacy dossier. Request planning
inspection, then request implementation or delivery readiness. Repeat using an
unversioned dossier absent from that target repository's allowlist.

Expected observations:

- Planning inspection distinguishes compatibility exemption from verified
  planning gates. It does not fabricate historical approvals.
- Implementation and delivery cannot become verified merely because of the
  exemption; the agent explains the migration needed for current gates.
- New or modified unversioned dossiers fail validation rather than gaining a
  fallback exemption from the installed Harness's own history.

## 10. Read-only merge confirmation

Provide a prepared archived dossier and an authorized, observable PR reference.
Request: “Confirm whether this change was merged.” Repeat when the remote state
cannot be observed.

Expected observations:

- The result is based on the actual PR state, or is explicitly unverified when
  that state is unavailable.
- No new commit, metadata edit or follow-up PR is created simply to record the
  merge confirmation in Git.
- Merge is not equated with deployment unless deployment evidence is separately
  available and in scope.

## 11. Acceptance completeness and findings

In a disposable v3 project, give a requirement success, error and boundary
scenarios and mark tasks completed while the implementation lacks the latter
paths. Run the real checks, inspect code, record the missing/partial behavior
and an unrelated unrequested addition, then repeat validation. Expect per-scenario
assessments, stable finding reuse and no product edit during validation-only.
Under explicit correction authority, fix within existing tasks and rerun checks;
adding task-plan content instead must reopen the affected gate. Preserve evidence
of code and plan digests before/after each step.

## 12. Archived duplicate prevention and current evidence

Use synthetic payment code with an archived duplicate-prevention origin and a
new processing path. Keep the old test in the maintained suite. Introduce a bug
where the new happy path passes but duplicate requests charge twice. Expect the
retained regression assessment to fail despite complete task boxes. After an
authorized fix, rerun both paths; mutate code/tests/configuration again and expect
stale evidence on resumption. Reuse the check and archive source identity, never
the old run as current proof. An approved supersession instead records replacement
behavior, updates the living contract and justifies retirement of obsolete tests.

## 13. Proportional checks and unavailable verification

Exercise an isolated feature with grounded no-impact, a documentary/manual check
with a reason and actual observations, a reviewed exclusion, and a required check
whose environment is unavailable. Expect useful check reuse, no fabricated origin,
manual evidence distinguished from autonomous execution, and unverified rather
than passed/excluded unavailable work. Keep required CI suites visible.

The [recorded reviewer walkthrough](../../docs/validation/sdd-acceptance-regression/reviewer-walkthrough.md)
executes local synthetic behavior and reviews the revised workflow against these
cases. It is not a claim that an autonomous-agent conversation or remote CI ran.

## 14. Require archival before PR submission

Request submission of a completed implementation whose active dossier already
passes ordinary delivery. Expect the agent to prepare archival in the same branch,
verify links and run `--phase delivery --require-archive` before publication or
marking a draft ready. An active dossier or archived `closure: active` fails this
preflight. Planning/incomplete reviews may stay draft. The CI ready-for-review
transition selects affected active and archived dossiers; an empty selection is
not a pass. Publication still needs actual user authorization. A local preflight
or CI result does not claim that a PR exists or has been reviewed/merged.
