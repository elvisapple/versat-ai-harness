# SDD artifact metadata

The four [templates](templates/) and [v3 JSON Schemas](schemas/v3/) define the machine-readable format. This document explains the review and evidence semantics enforced by the [validator](../validators/sdd/README.md). The [process](process.md) defines when an agent may act; schemas alone do not grant authorization.

## Version and identity

Every new artifact has YAML frontmatter with `sdd_version: 3` and the same `change` ID as its containing directory. Requirements and Tasks retain stable `REQ-001` and `TASK-001` identifiers. IDs must be unique within their collections and cross-file references must resolve. Design and Tasks cover all Requirements; Design supplies at least one required check for every requirement.

Proposal's legacy-compatible `status` values (`draft`, `proposed`, `accepted`, `rejected`, `implemented`, `archived`) remain descriptive. Neither `accepted` nor any other value replaces stage approvals. `archived` never proves a PR merged. Tasks `closure` is `active` or `prepared`; the latter requests delivery eligibility regardless of directory.

## Review records

Proposal holds the combined Proposal/Requirements review. Design and Tasks each hold their own review:

```yaml
review:
  revision: 1
  state: awaiting-approval
  blockers: []
  upstream: {}
  approval: null
```

`revision` is a positive integer. `state` is `draft`, `awaiting-approval`, `approved`, `blocked` or `superseded`. Record actual unresolved decisions in `blockers`; an approved stage cannot retain blockers. Proposal has no upstream stages. Design's `upstream` records `proposal: <digest>`; Tasks records both `proposal: <digest>` and `design: <digest>`, using the current approved upstream digests.

Only an approved review has a non-null `approval`:

```yaml
approval:
  source: "Conversation turn containing the developer's approval"
  quote: "I approve Design R1. Proceed to Tasks."
  revision: 1
  digest: "<actual 64-character stage digest>"
```

The example digest is explanatory, not valid artifact data. Populate `source` and `quote` from the actual observed approval, and use the stage's current revision and computed digest. Approval comes after the files have been presented to the developer. Do not fabricate evidence or count a generated example as approval. The optional Markdown `## Planning review` section can preserve human-readable history, including superseded records; the structured current record is authoritative for local checks.

To reopen a gate, increment that stage's revision, set an appropriate non-approved state and clear `approval`. Mark dependent reviews `superseded` with `approval: null`, retaining their historical record in the review section. Update upstream digests only as the corresponding stages are revisited after renewed approval. Do not silently edit the digest of an already approved record to make it match changed content.

## Content digests

Use the canonical helper rather than an ad hoc hash:

```sh
python validators/sdd/validate.py --root /path/to/project --change home-greeting --digest proposal
python validators/sdd/validate.py --root /path/to/project --change home-greeting --digest design
python validators/sdd/validate.py --root /path/to/project --change home-greeting --digest tasks
```

Run these commands from the selected Harness root with its validation dependencies installed. The digest looks up the ID in active or archive storage. Proposal's digest covers both Proposal and Requirements; each other stage covers its own artifact. The approval chain additionally binds the approved upstream digests. JSON-normalized frontmatter and normalized Markdown line endings/trailing spaces make formatting of YAML and incidental whitespace immaterial.

The digest excludes:

- `review` bookkeeping, Proposal `status`, task item `status`, Tasks `validation` and `closure`.
- Generated body sections named `## Planning review`, `## Validation evidence`, `## Progress` and `## Delivery`, up to the next level-two heading.
- The checked/unchecked distinction of task checkbox markers.

These exclusions permit progress and evidence updates without reapproving task descriptions, scope, requirements or design. Keep all substantive decisions outside excluded sections. Content edits beyond those exclusions conservatively invalidate approval even if described as editorial. A digest binds recorded contents; it cannot authenticate the reviewer. Linked ADR contents are not included in the digest: review their substantive revisions under the same Design gate.

## Checks and traceability

Design's `validation` array is the check plan:

```yaml
validation:
  - id: CHECK-001
    description: Verify accessible greeting behavior and repeated activation
    requirements: [REQ-001]
    required: true
    method:
      kind: automated
      procedure: Run python -m unittest tests.test_greeting; expect success, empty input and repeated activation assertions to pass.
    inputs:
      include: [src, tests, pyproject.toml]
      exclude: []
    outputs: [docs/validation/home-greeting]
    execution: local
coverage:
  - scenario: {requirement: REQ-001, scenario: 1}
    applicability: required
    checks: [CHECK-001]
regression: []
```

Each check has a unique stable ID, nonempty description, existing requirement references and a Boolean `required`. Planned checks say what will be verified; they are not results. Every requirement needs at least one required check. Tasks must also cover every requirement and use only known IDs. Each task has one matching Markdown checkbox, checked if and only if its metadata status is `completed`.

ADR references must be resolvable `ADR-0001` identifiers under `docs/decisions/`, existing repository-relative files or recorded HTTPS links. Local references must remain inside the repository and avoid symlinks; remote links are recorded without fetching or verifying them. Prefer stable repository-relative references for content that will move with documentary closure.

## Validation evidence

Tasks holds observed results separately from Design's plan:

```yaml
validation:
  plan_digest: null
  results: []
  assessments: []
  findings: []
closure: active
```

When checks actually run, set `plan_digest` to the current Tasks digest and record one result for each executed planned check:

```yaml
results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/home-greeting/check-001.txt
    revision: "Observed tested commit, working-tree snapshot or CI run identifier"
    input_digest_before: "<actual SHA-256 immediately before execution>"
    input_digest_after: "<actual SHA-256 immediately after execution>"
    context:
      execution: local
      environment: "Observed runtime, platform and relevant service state without secrets"
      observed: true
```

Use actual records in place of the illustrative evidence and revision. Each check ID must exist in Design and appear at most once in current results. `result` is `pass`, `fail` or `unverified`; explain gaps in the human-readable Validation evidence section. A local `evidence` value is a repository-relative existing file, preferably outside the movable dossier. An HTTPS value may identify an actual run/report, but the local validator does not retrieve or authenticate it. Absolute, escaping or symlink paths are rejected.

For delivery, all required checks must have recorded passes, all tasks must be completed and all reviews must be current with no blockers. Missing/unverified checks yield `unable-to-verify`; actual failures yield `fail`. Neither is readiness. The plan digest detects changed task planning; approval chaining detects upstream changes. An editable revision label cannot establish that the results cover current implementation, so rerun applicable checks after code changes and verify final CI on the delivery revision. Local file existence does not prove that a test was valid or acceptance behavior passed.

## Legacy dossiers

`sdd/legacy-changes.json` explicitly lists immutable pre-v2 dossiers by ID and raw SHA-256 digest for all four files. Each entry includes a governance reason. Only an exact ID/content match, valid legacy schemas and basic traceability qualify for exemption from v2 review/evidence fields. Missing version fields elsewhere do not opt out of the new contract. Unknown, changed or malformed entries must be reviewed rather than silently grandfathered.

The validator reports legacy exemptions as warnings, never as verified planning gates. `--phase implementation` and `--phase delivery` return `unable-to-verify` for an exempt dossier until it is migrated. Consumer validation uses the target project's manifest; provider exemptions do not automatically exempt consumer changes.

Migration is a deliberate reviewed update: retain genuine historical context, adopt v3 fields, present the current plan for real approvals and obtain current validation evidence. Remove the corresponding exemption when migration is complete. Do not synthesize retrospective approvals or automatically archive legacy work from a descriptive status. Existing delivered history need not be rewritten merely to pass new fields; continuing its execution or documentary closure does require the current contract.

## Impact and coverage

Proposal `impact` has `state: assessed | unresolved`, a nonempty `summary` and `items`. Empty items with an assessed summary means a reviewed no-impact conclusion. Unresolved is a draft state and blocks approval readiness. Each item contains:

```yaml
source:                       # optional; omit for baseline-only existing behavior
  change: prevent-duplicates
  requirement: REQ-001
  scenarios: [1]
  requirements_digest: "<canonical source Requirements digest>"
current_contract:
  change: payment-retry        # this change's ID
  artifact: proposal
  locator: "## Current contract baseline"
effect: preserve              # preserve | extend | supersede
targets: [REQ-002]             # affected local requirements
reason: Keep duplicate prevention while adding retries.
```

Alternatively `current_contract` is `{path: docs/payments.md, locator: "## Duplicate prevention", digest: "<raw file SHA-256>"}`. Resolve it before Proposal approval. Its digest captures the pre-change baseline; approved implementation may legitimately update that document. Historical inventory need not resolve a subsequently removed living document. The Proposal alternative captures the real pre-change behavior in the indicated section when no living specification exists.

Use `--source-digest --change prevent-duplicates` for the canonical origin digest. This hashes all Requirements metadata and normalized substantive body. Origins are qualified by change ID and must resolve uniquely from active/archive storage, including immutable older schemas; no historical migration is needed just to cite an origin. Different scenarios from one origin may have distinct dispositions; overlapping source scenario declarations are rejected. Source edits invalidate its binding. A dossier move alone does not.

`coverage` has exactly one row per local one-based acceptance position, referencing known checks that cover its requirement. Required rows need a required check. `applicability: not-applicable` needs `reason` in the approved Design; it never means an unavailable environment. `regression` has one row per retained impact/source scenario:

```yaml
regression:
  - obligation: {impact: 1, scenario: 1}
    checks: [CHECK-002]
    rationale: Reuse the maintained duplicate-submission test against the current implementation.
```

`impact` is the one-based Proposal item index; `scenario` is the origin acceptance position, or zero for a baseline-only item. Preserve/extend require regression rows. Supersede requires reviewed reasons, local replacement targets and required checks rather than continuing obsolete assertions. Each referenced regression check covers an affected target requirement. Multiple scenarios can share a check; a scenario can use several checks. Requirement/task coverage remains required in addition to these mappings.

`method.kind` is automated, manual or review. Every method has a procedure and expected observations; manual/review methods also need a reason. `execution` specifies local or ci. Check text is never executed by the validator. Input scopes must include relevant code, tests, fixtures, guides and configuration. Review adequacy and keep profile-required CI checks; declarations do not discover missing scope.

## Input snapshots

Use `--input-digest CHECK-001 --change <id>` on a structurally valid approved v3 plan immediately before and after actually running its check. It is read-only, does not execute the method, and can compute a new snapshot while old results are stale or failures remain. A passing run needs identical before/after values. Live validation additionally compares current files. Never relabel old execution with a fresh hash.

SHA-256 covers declared scopes, sorted relative paths, types, file bytes, executable flags and explicitly missing roots. Recursion detects added/deleted files, including ignored files. Hashes can be reused only within one invocation using file identity/stat metadata. Reject absolute/traversing paths, symlink components, special files and conflicting explicit input/output scopes. Do not include secrets. There is no implicit Git-ignore filter.

`.git`, the current dossier and declared outputs are excluded. The `specs`, `specs/changes` and `specs/archive` container entries are bookkeeping and are traversed without hashing those directory entries; other files beneath them remain inputs when in scope. This preserves freshness across the current dossier's archive move. An output beneath a broad input root needs an explicit approved exclusion. Use stable preexisting output parent directories or exclude the complete generated output subtree. Referenced sources are independently bound by their Requirements digest. Dossier metadata is bound by the stage/plan digests instead of its mutable raw bytes.

Input hashes detect changes only inside the approved scope. They do not authenticate runs, runtime labels, remote services or HTTPS evidence. Capture relevant environment and rerun on known external changes; unavailable verification remains unverified.

## Assessments and findings

Tasks `validation.assessments` has one disposition per local and retained regression obligation at delivery:

```yaml
assessments:
  - obligation: {local: {requirement: REQ-001, scenario: 1}}
    result: pass
    checks: [CHECK-001]
    evidence: docs/validation/home-greeting/check-001.txt
    explanation: The observed greeting matched the scenario after activation.
```

For retained behavior use `obligation: {regression: {impact: 1, scenario: 1}}`. Allowed results are pass, fail, unverified and not-applicable. Checks must match the planned mapping. A pass requires current passing required checks and observed matching execution context. An approved exclusion is listed separately, not counted as a pass. Missing/unverified scenarios leave the requirement unverified; any failed scenario fails it. Open gaps block completeness independently of checked tasks.

`validation.findings` records stable IDs, obligation or `{plan: "affected scope"}` source, category (missing, partial, contradicts, unrequested), state (open, resolved), evidence, description, task/check references and a resolution when resolved. For example:

```yaml
findings:
  - id: FIND-001
    source: {local: {requirement: REQ-001, scenario: 1}}
    category: partial
    state: open
    evidence: docs/validation/home-greeting/review.md
    description: Empty input silently discards the greeting.
    tasks: [TASK-001]
    checks: [CHECK-001]
```

Reuse the open finding instead of duplicating tasks each run. Resolution needs its disposition and current supporting check evidence. Evidence recording is bookkeeping, not authorization to change the plan. Validation-only does not fix code; authorized in-scope fixes reuse existing tasks and rerun checks. New task-plan content reopens Tasks; broader changes reopen the earliest affected gate.

## Historical inventory and live delivery

Default repository inventory validates archived records, including stored snapshot consistency and completeness, without comparing historical input hashes with today's code. Active results are checked live. `--change <id> --phase delivery` always checks current inputs, even in archive storage. Both fail and unable-to-verify block readiness.

`--baseline <trusted-git-ref>` additionally selects newly archived or modified archive IDs for live delivery. Git paths are NUL-delimited and both sides of moves are considered. Missing refs and deleted/reopened archive records fail selection for explicit review. CI uses the platform PR-base or push-before revision and a full checkout; argument text is passed as data, never executed. Without a baseline, an inventory pass cannot certify changed archives. Explicit selected delivery works without Git. None of these operations proves merge.

## v2 compatibility

The existing root schemas preserve v2 exactly; v3 schemas live in `schemas/v3/`. Unknown and mixed versions fail. New unlisted v2 records are rejected. Consumer `sdd/compatibility.json` is an explicitly reviewed version 1 manifest with `historical` and `in_flight` maps, disjoint from each other and the pre-v2 legacy manifest:

- A historical entry has a reason and `files` mapping of all four filenames to raw SHA-256 hashes. It remains immutable and cannot certify current readiness.
- An in-flight entry has a reason and `digests` for proposal, design and tasks using actual already-approved stage digests. Original v2 gates and results still apply; only progress/evidence bookkeeping may change. Substantive planning edits require a reviewed v3 migration and genuine approvals.

The introducing `sdd-acceptance-regression` change finishes under its actual v2 approvals; `quickstart-scenario-coverage` remains byte-bound history. Their compatibility warnings explicitly withhold v3 assurance. v3 is exercised through synthetic repositories and recorded reviewer walkthroughs. Never add exemptions automatically to silence failures. Adoption is a deliberate exact-release consumer update. Rollback must retain tooling capable of reading existing v3 dossiers or explicitly migrate active work through review; removing version markers is not migration.

## PR archive guard

`--require-archive` adds a submission precondition without adding another planning phase. Use `--change <id>` for a local pre-publication check, or `--baseline <trusted-ref>` for affected dossiers. Every selected dossier must exist in archive storage with Tasks `closure: prepared` and pass live delivery checks. With both selectors, their union is checked. Invalid/empty selection fails rather than accepting a vacuous success.

Baseline selection for this guard includes both `specs/changes/` and `specs/archive/`, including removed paths. Unchanged active/history records remain ordinary inventory. Without the flag, existing planning, implementation and pre-move delivery behavior stays available. Digest-only helper operations cannot substitute for the guard. CI enables it for non-draft PRs, ready-for-review transitions and pushes to main; drafts retain inventory plus the existing live checks for changed archives.
