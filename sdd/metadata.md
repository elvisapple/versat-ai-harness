# SDD artifact metadata

The four [templates](templates/) and [JSON Schemas](schemas/) define the machine-readable format. This document explains the review and evidence semantics enforced by the [validator](../validators/sdd/README.md). The [process](process.md) defines when an agent may act; schemas alone do not grant authorization.

## Version and identity

Every new artifact has YAML frontmatter with `sdd_version: 2` and the same `change` ID as its containing directory. Requirements and Tasks retain stable `REQ-001` and `TASK-001` identifiers. IDs must be unique within their collections and cross-file references must resolve. Design and Tasks cover all Requirements; Design supplies at least one required check for every requirement.

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
```

Each check has a unique stable ID, nonempty description, existing requirement references and a Boolean `required`. Planned checks say what will be verified; they are not results. Every requirement needs at least one required check. Tasks must also cover every requirement and use only known IDs. Each task has one matching Markdown checkbox, checked if and only if its metadata status is `completed`.

ADR references must be resolvable `ADR-0001` identifiers under `docs/decisions/`, existing repository-relative files or recorded HTTPS links. Local references must remain inside the repository and avoid symlinks; remote links are recorded without fetching or verifying them. Prefer stable repository-relative references for content that will move with documentary closure.

## Validation evidence

Tasks holds observed results separately from Design's plan:

```yaml
validation:
  plan_digest: null
  results: []
closure: active
```

When checks actually run, set `plan_digest` to the current Tasks digest and record one result for each executed planned check:

```yaml
results:
  - check: CHECK-001
    result: pass
    evidence: docs/validation/home-greeting/check-001.txt
    revision: "Observed tested commit, working-tree snapshot or CI run identifier"
```

Use actual records in place of the illustrative evidence and revision. Each check ID must exist in Design and appear at most once in current results. `result` is `pass`, `fail` or `unverified`; explain gaps in the human-readable Validation evidence section. A local `evidence` value is a repository-relative existing file, preferably outside the movable dossier. An HTTPS value may identify an actual run/report, but the local validator does not retrieve or authenticate it. Absolute, escaping or symlink paths are rejected.

For delivery, all required checks must have recorded passes, all tasks must be completed and all reviews must be current with no blockers. Missing/unverified checks yield `unable-to-verify`; actual failures yield `fail`. Neither is readiness. The plan digest detects changed task planning; approval chaining detects upstream changes. An editable revision label cannot establish that the results cover current implementation, so rerun applicable checks after code changes and verify final CI on the delivery revision. Local file existence does not prove that a test was valid or acceptance behavior passed.

## Legacy dossiers

`sdd/legacy-changes.json` explicitly lists immutable pre-v2 dossiers by ID and raw SHA-256 digest for all four files. Each entry includes a governance reason. Only an exact ID/content match, valid legacy schemas and basic traceability qualify for exemption from v2 review/evidence fields. Missing version fields elsewhere do not opt out of the new contract. Unknown, changed or malformed entries must be reviewed rather than silently grandfathered.

The validator reports legacy exemptions as warnings, never as verified planning gates. `--phase implementation` and `--phase delivery` return `unable-to-verify` for an exempt dossier until it is migrated. Consumer validation uses the target project's manifest; provider exemptions do not automatically exempt consumer changes.

Migration is a deliberate reviewed update: retain genuine historical context, adopt v2 fields, present the current plan for real approvals and obtain current validation evidence. Remove the corresponding exemption when migration is complete. Do not synthesize retrospective approvals or automatically archive legacy work from a descriptive status. Existing delivered history need not be rewritten merely to pass new fields; continuing its execution or preparing new delivery does require the current contract.

For administrative relocation of already merged history, a reviewed legacy entry may additionally carry `historical_archive` with exactly `merge_commit` (a full lowercase 40- or 64-character Git object ID) and `evidence` (an existing repository-relative file or an HTTPS reference documenting the observed merge). Verify the merge against the default branch before recording it. Preserve all four artifact hashes and bytes, require completed historical tasks, and keep the dossier only under `specs/archive/`. Do not add v2 approvals or `closure: prepared` to this immutable record.

This explicit record permits historical storage during the default `planning` check, with warnings. Missing or malformed records, changed artifacts and incomplete tasks do not qualify. Explicit `implementation` and `delivery` checks still return `unable-to-verify` for these legacy dossiers. The validator checks recorded structure and local references, not Git ancestry or remote evidence authenticity; the maintenance PR must review those facts. See the provider's [historical archive evidence](../docs/validation/legacy-archive.md).
