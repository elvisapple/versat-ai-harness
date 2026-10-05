# Implementation review — 2026-10-02

Change: `automated-test-execution`. Approved Proposal/Requirements R1, Design R2 and Tasks R1 remain unchanged. This report records local implementation review, not live model behavior, remote configuration or delivery.

## Continuation after runtime selection — 2026-10-02

The developer's current Codex configuration selects `gpt-6-astra` with `high` reasoning. The [reviewable runtime candidate](runtime-candidate.json) binds that choice with the approved case/suite bounds. A real [Codex CLI 0.159.2 sandbox probe](sandbox-probe/result.json) passed under the built-in `:workspace` permission profile: a fixture write succeeded, while a write outside the nested Git root and a local network bind were denied. The CLI was run from an empty temporary `CODEX_HOME`; the probe made no model request.

The [CHECK-004 preflight attempt](live/4e962b33a5534309805e4b513e9d5b4b/summary.json) is **unverified** and records zero model invocations. This host did not supply a dedicated isolated evaluation environment attestation or `CODEX_API_KEY`. Existing local account authentication was not substituted for that transport credential. The SDD input digest matched before and after the preflight, and no result was relabeled as live behavior. The repository's GitHub API showed no environments and no `VERSAT_EVAL_RUNTIME_JSON` variable, so protected CI is likewise unavailable. The old paragraphs below are the earlier review state; these findings supersede only its statement that model/reasoning were unspecified.

The [current local test attempt](local-1c25c0969f214d9ab7c157eb795d893c/results.json) passed CHECK-001, CHECK-002, CHECK-003 and CHECK-005. CHECK-007 failed at its SDD inventory step because the prior run's six recorded input digests had become stale after adapter edits; its 131 maintained tests and 52 new tests passed. That failed attempt is retained. The Tasks results were rebound to the new, actually executed check attempts before repeating the package validation. The [final local rerun](local-e9f35bafe37c4e50996de2d3f303406e/results.json) passed all five local automated checks, including the full package command with 131 maintained and 52 new tests. The failed intermediate attempt remains preserved. CHECK-006 remains unverified: the CLI sandbox first-use path is proven, while real model use is not.

## Observed evidence

The [local execution record](local-5a09a0127812475188ec868c4bcba76a/results.json) records five actual Design checks with matching before/after source digests and the approved Tasks digest. CHECK-001, CHECK-002, CHECK-003, CHECK-005 and CHECK-007 passed. CHECK-007 executed all 131 existing validator tests and 51 new execution/adapter tests on macOS with Python 3.11. Offline mocked CLI events are explicitly adapter tests. No canned event was reported as live evaluation.

CHECK-003 composes base plus optional Python assets in disposable directories, provides actual payment code/tests, resolves synthetic identity and lockfile through the canonical index, creates a clean synthetic Git provider and executes the documented full consumer wrapper. Its assertions observe pass on the correct implementation and fail after duplicate-payment, zero-amount and empty-key defects. Custom command adoption, restoration/rollback and missing retained coverage are exercised. The incomplete happy-path suite can pass despite a defect; restoring the retained assertion catches it, demonstrating why command success alone is insufficient. Canonical v3 fixtures additionally check reviewed replacement and justified manual dispositions.

The consumer provider is explicitly synthetic; this does not claim installation from a published release. An unresolved pin fails. No version, marketplace release or installed plugin cache was changed.

CHECK-002 executes real subprocesses under approved synthetic SDD plans. It verifies fragments and unchanged dossier bytes, refuses stale/unapproved plans, targeted export and manual relabeling, withholds fresh success after input/plan changes, preserves old attempts and verifies archive-safe paths. CHECK-001 covers full/targeted semantics, retained failure, empty/all-skipped discovery, mixed subtests, unavailable tools, malformed reports, safe output scope, log bounds, environment inheritance, cancellation and timeouts. Optional unavailable suites no longer block a required run.

CHECK-005 runs local CI dispatch functions and the structural workflow's shell branches against harmless metadata/command fixtures, including trusted-baseline/archive forwarding, draft opt-in/removal, exact-ref dispatch, current-head recheck, missing protection and aggregate nonpassing results. Action references are immutable commits. These checks do not establish that a GitHub environment, secret, variable, ruleset or required check exists.

The semantic review also inspected:

| Area | Local observation | Remaining evidence |
| --- | --- | --- |
| REQ-001 explicit contract | Versioned config/count schemas; pure validation; required-suite execution | Linux execution is not observed locally |
| REQ-002 coverage | Behavioral payment assertions catch three seeded defects; adequate reuse and canonical manual/replacement checks | Actual agent behavior in CHECK-004 |
| REQ-003 complete regressions | 131 maintained tests plus 51 additions pass; targeted runs cannot export full evidence | Real live suite and remote complete runs |
| REQ-004 current SDD evidence | Plan/input binding, immutable prior attempts and no dossier mutation verified | Live scenario evidence recording |
| REQ-005 CI | Credential-free selection/aggregation; required environment review; revision/label recheck | Actual platform prerequisites and CHECK-008 |
| REQ-006 real evaluation | Six cases twice; immutable fixture controls/plans; observed actions plus replay; deadlines include grading | Real execution in an authorized isolated environment |
| REQ-007 adoption/docs | Disposable clean provider and full wrapper; custom configuration/rollback; 89 relative links resolve | Isolated evaluation guide's complete first-use run |
| REQ-008 truthful limits | Empty discovery, stale results, unavailable prerequisites and failed attempts cannot establish pass | Live failure/approval boundaries and remote observation |

The 23 retained obligations remain mapped by the approved Design. Existing SDD compatibility, gates, archive selection and regression tests remain unchanged and passing. Full acceptance assessments of all 27 local scenarios and 23 retained obligations are intentionally not claimed before the required live/platform observations.

## First-use and architecture review

The guides separate package checks from consumer execution and distinguish full, targeted, manual and live evidence. Composition remains base plus selected profile plus optional artifact; no consumer identity was invented for the Plugin root. Bootstrap and maintenance route through the template guide rather than duplicating Standards. The duplicate bootstrap workflow numbering was consolidated into its existing discovery sequence. Existing commands and lockfiles have an explicit reviewed rollback.

Policies stay in Standards, lifecycle instructions in SDD, pure enforcement in validators and side effects in scripts, matching ADR-0015. Neither SDD method prose nor configuration inspection launches project code. The executor is not a sandbox; real evaluation therefore probes and uses the Codex sandbox for both agent tools and independent replay. Replay receives no API credential environment. Review of trusted code, actual outer isolation and scoped credentials remains required.

The installed CLI reports `codex-cli 0.159.2`. CLI availability alone does not establish usable nested sandboxing, model authorization or a dedicated disposable environment. No model invocation was attempted. The sandbox adapter's unavailable-runtime tests and offline replay-boundary tests pass, but do not replace the real probe/run.

[The link audit](document-links.json) resolved 89 local documentation targets with no missing files. The project first-use path was exercised through CHECK-003. The live evaluation first-use path remains unverified because no reviewed model/reasoning configuration and authorized isolated environment were supplied. Accordingly **CHECK-006 is recorded as unverified**, retaining this useful partial review rather than asserting its full completion.

## Open dependencies

- **DEP-001:** CHECK-004 needs explicit model/reasoning, authorized runtime/authentication and a provisioned isolated environment with a successful real sandbox probe. The earlier request for these inputs remains pending. Do not guess a model or use personal authenticated state.
- **DEP-002:** CHECK-008 needs scoped draft publication/label authority and actual protected-environment prerequisites, followed by observed deterministic and live CI on the tested revision. Linux execution remains unobserved. No remote mutation, publication or CI run was performed.
- **DEP-003:** Complete CHECK-006's live first-use review after the evaluation environment is available. Local project setup and documentation review are already recorded above.

Tasks 1–4, 6 and 7 have their local implementation checks complete; Linux/runtime limitations are explicit. Tasks 5 and 8 retain incomplete full first-use review, Task 9 retains the required live evaluation and Task 10 retains remote CI and final assessment. Closure stays active. No archival, ready-for-review state, merge, release or consumer rollout is claimed.
