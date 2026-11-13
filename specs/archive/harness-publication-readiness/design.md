---
sdd_version: 3
change: harness-publication-readiness
requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011,
  REQ-012]
adrs: [docs/decisions/0016-public-harness-preparation-boundary.md]
validation:
- id: CHECK-001
  description: Review concrete candidate terms, rights, dependencies and actual review capacity
  requirements: [REQ-001, REQ-002, REQ-010, REQ-011]
  required: true
  method:
    kind: review
    procedure: 'Follow the licensing/rights procedure in Design: compare the exact Apache candidate, notices, adoption
      patch and component ledger with H01 frozen wording/evidence; inspect the actual private supporting records
      with authorized reviewers. Exercise missing-grant, incompatible-dependency and absent-review cases. Expect
      explicit permissions/third-party preservation, unchanged historical approval, exact-text hashes and actual
      review state, and defer with owner/exit condition for every unresolved condition. A generic SDD approval or
      metadata scan cannot pass a missing real review.'
    reason: Permission, provenance and reviewer capacity require attributable human evidence; package tests cannot
      establish them.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-002
  description: Assess complete publication surface and safe evidence handling
  requirements: [REQ-002, REQ-003, REQ-008, REQ-009, REQ-010]
  required: true
  method:
    kind: review
    procedure: Follow the surface procedure in Design. Enumerate current/tracked/untracked intended content, reachable
      refs/history and each remote surface; retain dated scope and unavailable-access results privately. Review
      every category, compare to the scrubbed input manifest, and exercise sensitive-old-commit, unavailable-attachment
      and post-review-drift cases without destructive remediation. Expect complete categories, observed-reviewed/observed-absent/unverified
      distinctions and a blocking disposition for unknown or sensitive scope. Review public candidates for private
      links/payloads and confirm restricted evidence remains outside the candidate.
    reason: Remote coverage, confidentiality classification and rights context are not proven by grep or a clean
      current tree.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-003
  description: Verify root package, candidate version and immutable prior release
  requirements: [REQ-004, REQ-011]
  required: true
  method:
    kind: automated
    procedure: In approved implementation, verify the exact v0.3.0 base object, adoption.patch base/hash and candidate
      tree manifest; apply the reviewed patch only in a disposable private checkout and run python validators/plugin/validate.py
      there and in the preparation checkout. Compare VERSION, both manifests, marketplace ref/identity and template
      lock. Expect candidate 0.4.0 with matching canonical resources and unchanged original v0.3.0; negative disposable
      copies with one version mismatch or legacy nested package path must fail the unchanged validator. Do not tag,
      push, rename marketplace identity or alter consumers.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-004
  description: Observe real private installation, first use, explicit update and recovery
  requirements: [REQ-004, REQ-005, REQ-012]
  required: true
  method:
    kind: review
    procedure: Execute the bounded rehearsal cases in Design on the selected installed Codex target using a disposable
      client context and synthetic consumer. Record actual installation/loading steps and observed version/resource
      paths; exercise one fresh first-use planning invocation, absent provider/version, incompatible version, explicit
      old-to-new migration and failed-update recovery. Independently inspect outputs and canonical digests. Expect
      only Proposal/Requirements and a Gate 1 stop for first use, actionable failures and preserved/recovered last
      verified compatible state. Retain every attempt; no narrative-only, mocked install or implicit public-access
      pass.
    reason: Client installation and real Skill stopping behavior require supervised observation and independent
      artifact inspection; deterministic helpers alone are insufficient.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-005
  description: Review public contribution flow and actual control observations
  requirements: [REQ-006, REQ-011, REQ-012]
  required: true
  method:
    kind: review
    procedure: Follow the contribution/control procedure in Design. Walk the proposed fork/branch/PR route without
      submitting remote work, inspect repository-specific precedence and provenance, read actual rulesets/protections/required-check
      settings when available, and audit fork workflow events/token/secret access. Exercise missing-rights and missing-control
      cases. Expect maintainer-only write/merge/release, no secret-bearing untrusted execution, honest unknowns
      and an operational block until controls are verified; organization entry points remain unchanged.
    reason: Local workflow YAML and CODEOWNERS cannot establish live branch rules or actual account capabilities;
      remote observations are distinct inputs.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-006
  description: Review scoped reporting evidence and the Harness-specific operational verification plan
  requirements: [REQ-007, REQ-009, REQ-011]
  required: true
  method:
    kind: review
    procedure: Follow the reporting procedure in Design. Verify unchanged scope of the .github pilot/internal receipt,
      existing responsible CODEOWNERS and the proposed public Harness destination/audience/recipient/data boundaries.
      Review the authorized synthetic-report protocol and safe unavailable/denied/changed-route cases without sending
      messages. Expect no promoted pilot evidence, no internal addresses or fabricated active endpoint/SLA, a non-sensitive
      fallback, and explicit pending public-audience receipt verification. Active availability may be claimed only
      with the actual separately authorized repository-specific result.
    reason: A reporting plan and an administrator view cannot prove intended-reporter access or receipt; this check
      validates preparation and truthful state, not a future report delivery.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-007
  description: Verify maintained multilingual guidance, navigation and observed usage
  requirements: [REQ-005, REQ-008, REQ-010, REQ-011, REQ-012]
  required: true
  method:
    kind: review
    procedure: Follow the documentation procedure in Design across README, quickstart, product context and all affected
      guides/entry candidates. Resolve local links/anchors and access-classify external targets, compare EN/PT/ES
      permissions/gates/status/recovery, and trace every affected documented action to real rehearsal evidence or
      an explicit unavailable result. Expect self-contained public instructions, preserved canonical workflows,
      safe provenance, stable living paths and no unsupported installation/publication claim. Verify unrelated guides
      and organization-owned entry contracts remain usable.
    reason: Link automation is useful but cannot assess translated semantics, user comprehension, private access
      or the correctness of observed UI behavior.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-008
  description: Independently review every retained effective contract and historical integrity
  requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011,
    REQ-012]
  required: true
  method:
    kind: review
    procedure: For every preserve/extend impact item, read each qualified source scenario and the effective current
      baseline, inspect its mapped current documents/code/tests and the relevant original check observations; record
      one meaningful disposition per obligation. Compare historical dossiers, frozen terms and approval records
      byte-for-byte with the reviewed base, subject only to expressly planned administrative current-status annotations
      outside frozen history. Verify all seven supersessions retain their replacement behavior rather than silently
      delete obligations. Expect independent products, canonical sources, honest evidence, unchanged history and
      no authority expansion; a list of IDs or old passing reports alone cannot satisfy this check.
    reason: Semantic regression assessment spans policy, documentation and human authorization and is not established
      by structural mappings or task checkboxes.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-009
  description: Run all maintained package, SDD, validator and execution suites
  requirements: [REQ-004, REQ-009, REQ-011, REQ-012]
  required: true
  method:
    kind: automated
    procedure: With Python 3.11+ and the exact requirements-validation.txt environment, run PYTHONDONTWRITEBYTECODE=1
      PYTHON=<verified-interpreter> ./scripts/validate/run.sh in the preparation checkout and the exact private
      candidate checkout. Preserve complete output and actual counts, exit 0 required, with no empty/all-skipped
      suite. Keep legacy warnings attributable to unchanged historical exemptions. Final required CI uses the existing
      trusted baseline/archive policy separately; local results never claim remote CI or public runtime success.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
- id: CHECK-010
  description: Review readiness disposition, operational handoff and non-circular lifecycle
  requirements: [REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-009, REQ-010, REQ-011, REQ-012]
  required: true
  method:
    kind: review
    procedure: Follow the handoff procedure in Design using the exact candidate, scrubbed immutable input manifests
      and actual private evidence. Check gates/digests, real review identities, ADR text hash and each readiness
      prerequisite. Exercise missing prerequisite, wrong revision, unauthorized publication, post-visibility failure
      and containment cases. Expect prepared/deferred versus publish-ready distinctions, pre-action drift recheck,
      separately authorized bounded adoption/visibility/release and mandatory later anonymous install/update/contribution/reporting/control
      verification. No pre-merge task depends on its own merge, future publication or this check's own result; the
      delivery/archive guard runs separately after the full ledger exists.
    reason: Readiness and operational authority are human decisions across multiple evidence sources; the structural
      guard cannot authorize or execute operations.
  inputs:
    include: [.]
    exclude: [docs/validation/harness-publication-readiness]
  outputs: [docs/validation/harness-publication-readiness]
  execution: local
coverage:
- scenario:
    requirement: REQ-001
    scenario: 1
  applicability: required
  checks: [CHECK-001]
- scenario:
    requirement: REQ-001
    scenario: 2
  applicability: required
  checks: [CHECK-001]
- scenario:
    requirement: REQ-001
    scenario: 3
  applicability: required
  checks: [CHECK-001]
- scenario:
    requirement: REQ-002
    scenario: 1
  applicability: required
  checks: [CHECK-001, CHECK-002]
- scenario:
    requirement: REQ-002
    scenario: 2
  applicability: required
  checks: [CHECK-001, CHECK-002]
- scenario:
    requirement: REQ-002
    scenario: 3
  applicability: required
  checks: [CHECK-001, CHECK-002]
- scenario:
    requirement: REQ-003
    scenario: 1
  applicability: required
  checks: [CHECK-002]
- scenario:
    requirement: REQ-003
    scenario: 2
  applicability: required
  checks: [CHECK-002]
- scenario:
    requirement: REQ-003
    scenario: 3
  applicability: required
  checks: [CHECK-002]
- scenario:
    requirement: REQ-004
    scenario: 1
  applicability: required
  checks: [CHECK-003, CHECK-004, CHECK-009]
- scenario:
    requirement: REQ-004
    scenario: 2
  applicability: required
  checks: [CHECK-003, CHECK-004, CHECK-009]
- scenario:
    requirement: REQ-004
    scenario: 3
  applicability: required
  checks: [CHECK-003, CHECK-004, CHECK-009]
- scenario:
    requirement: REQ-005
    scenario: 1
  applicability: required
  checks: [CHECK-004, CHECK-007]
- scenario:
    requirement: REQ-005
    scenario: 2
  applicability: required
  checks: [CHECK-004, CHECK-007]
- scenario:
    requirement: REQ-005
    scenario: 3
  applicability: required
  checks: [CHECK-004, CHECK-007]
- scenario:
    requirement: REQ-005
    scenario: 4
  applicability: required
  checks: [CHECK-010]
- scenario:
    requirement: REQ-006
    scenario: 1
  applicability: required
  checks: [CHECK-005]
- scenario:
    requirement: REQ-006
    scenario: 2
  applicability: required
  checks: [CHECK-005]
- scenario:
    requirement: REQ-006
    scenario: 3
  applicability: required
  checks: [CHECK-005]
- scenario:
    requirement: REQ-007
    scenario: 1
  applicability: required
  checks: [CHECK-006]
- scenario:
    requirement: REQ-007
    scenario: 2
  applicability: required
  checks: [CHECK-006]
- scenario:
    requirement: REQ-007
    scenario: 3
  applicability: required
  checks: [CHECK-006]
- scenario:
    requirement: REQ-008
    scenario: 1
  applicability: required
  checks: [CHECK-002, CHECK-007]
- scenario:
    requirement: REQ-008
    scenario: 2
  applicability: required
  checks: [CHECK-002, CHECK-007]
- scenario:
    requirement: REQ-008
    scenario: 3
  applicability: required
  checks: [CHECK-002, CHECK-007]
- scenario:
    requirement: REQ-009
    scenario: 1
  applicability: required
  checks: [CHECK-010, CHECK-009]
- scenario:
    requirement: REQ-009
    scenario: 2
  applicability: required
  checks: [CHECK-010, CHECK-009]
- scenario:
    requirement: REQ-009
    scenario: 3
  applicability: required
  checks: [CHECK-010, CHECK-009]
- scenario:
    requirement: REQ-009
    scenario: 4
  applicability: required
  checks: [CHECK-010, CHECK-009]
- scenario:
    requirement: REQ-010
    scenario: 1
  applicability: required
  checks: [CHECK-008, CHECK-001, CHECK-002]
- scenario:
    requirement: REQ-010
    scenario: 2
  applicability: required
  checks: [CHECK-008, CHECK-001, CHECK-002]
- scenario:
    requirement: REQ-010
    scenario: 3
  applicability: required
  checks: [CHECK-008, CHECK-001, CHECK-002]
- scenario:
    requirement: REQ-011
    scenario: 1
  applicability: required
  checks: [CHECK-008, CHECK-003, CHECK-005, CHECK-007]
- scenario:
    requirement: REQ-011
    scenario: 2
  applicability: required
  checks: [CHECK-008, CHECK-003, CHECK-005, CHECK-007]
- scenario:
    requirement: REQ-011
    scenario: 3
  applicability: required
  checks: [CHECK-008, CHECK-003, CHECK-005, CHECK-007]
- scenario:
    requirement: REQ-012
    scenario: 1
  applicability: required
  checks: [CHECK-008, CHECK-010]
- scenario:
    requirement: REQ-012
    scenario: 2
  applicability: required
  checks: [CHECK-008, CHECK-010]
- scenario:
    requirement: REQ-012
    scenario: 3
  applicability: required
  checks: [CHECK-008, CHECK-010]
regression:
- obligation:
    impact: 1
    scenario: 1
  checks: [CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 1, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 1
    scenario: 3
  checks: [CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 1, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 3
    scenario: 1
  checks: [CHECK-001, CHECK-002, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 3, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 3
    scenario: 2
  checks: [CHECK-001, CHECK-002, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 3, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 3
    scenario: 3
  checks: [CHECK-001, CHECK-002, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 3, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 5
    scenario: 2
  checks: [CHECK-001, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 5, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 6
    scenario: 1
  checks: [CHECK-001, CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 6, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 6
    scenario: 2
  checks: [CHECK-001, CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 6, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 6
    scenario: 3
  checks: [CHECK-001, CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 6, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 7
    scenario: 1
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 7, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 7
    scenario: 2
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 7, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 7
    scenario: 3
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 7, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 8
    scenario: 1
  checks: [CHECK-008, CHECK-009, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 8, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 8
    scenario: 2
  checks: [CHECK-008, CHECK-009, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 8, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 8
    scenario: 3
  checks: [CHECK-008, CHECK-009, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 8, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 9
    scenario: 1
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 9, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 9
    scenario: 2
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 9, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 9
    scenario: 3
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 9, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 9
    scenario: 4
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 9, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 10
    scenario: 1
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 10, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 10
    scenario: 2
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 10, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 10
    scenario: 3
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 10, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 11
    scenario: 1
  checks: [CHECK-001, CHECK-005, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 11, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 11
    scenario: 3
  checks: [CHECK-001, CHECK-005, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 11, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 13
    scenario: 1
  checks: [CHECK-006, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 13, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 13
    scenario: 2
  checks: [CHECK-006, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 13, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 13
    scenario: 3
  checks: [CHECK-006, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 13, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 13
    scenario: 4
  checks: [CHECK-006, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 13, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 14
    scenario: 1
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 14, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 14
    scenario: 2
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 14, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 14
    scenario: 3
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 14, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 15
    scenario: 1
  checks: [CHECK-006, CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 15, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 15
    scenario: 2
  checks: [CHECK-006, CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 15, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 15
    scenario: 3
  checks: [CHECK-006, CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 15, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 15
    scenario: 4
  checks: [CHECK-006, CHECK-008, CHECK-010]
  rationale: Retain the effective contract identified in Proposal impact 15, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 17
    scenario: 2
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 17, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 17
    scenario: 3
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 17, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 18
    scenario: 1
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 18, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 18
    scenario: 2
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 18, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 18
    scenario: 3
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 18, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 19
    scenario: 1
  checks: [CHECK-003, CHECK-004, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 19, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 19
    scenario: 2
  checks: [CHECK-003, CHECK-004, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 19, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 19
    scenario: 3
  checks: [CHECK-003, CHECK-004, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 19, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 20
    scenario: 1
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 20, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 20
    scenario: 2
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 20, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 20
    scenario: 3
  checks: [CHECK-003, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 20, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 21
    scenario: 1
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 21, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 21
    scenario: 2
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 21, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 21
    scenario: 3
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 21, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 22
    scenario: 1
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 22, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 22
    scenario: 2
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 22, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 22
    scenario: 3
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 22, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 23
    scenario: 1
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 23, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 23
    scenario: 2
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 23, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 23
    scenario: 3
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 23, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 23
    scenario: 4
  checks: [CHECK-004, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 23, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 24
    scenario: 1
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 24, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 24
    scenario: 2
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 24, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 24
    scenario: 3
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 24, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 25
    scenario: 1
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 25, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 25
    scenario: 2
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 25, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 25
    scenario: 3
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 25, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 25
    scenario: 4
  checks: [CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 25, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 27
    scenario: 2
  checks: [CHECK-004, CHECK-007, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 27, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 27
    scenario: 3
  checks: [CHECK-004, CHECK-007, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 27, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 27
    scenario: 4
  checks: [CHECK-004, CHECK-007, CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 27, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 28
    scenario: 1
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 28, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 28
    scenario: 2
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 28, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 28
    scenario: 3
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 28, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 28
    scenario: 4
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 28, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 28
    scenario: 6
  checks: [CHECK-005, CHECK-007, CHECK-008]
  rationale: Retain the effective contract identified in Proposal impact 28, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
- obligation:
    impact: 30
    scenario: 0
  checks: [CHECK-008, CHECK-009]
  rationale: Retain the effective contract identified in Proposal impact 30, using the mapped current observations
    and independent CHECK-008 assessment; do not reuse the historical pass.
review:
  revision: 1
  state: approved
  blockers: []
  upstream:
    proposal: 41081278df433db671e12b7d442b78a446f792977cc976a37407a5113ee62443
  approval:
    source: User reply in this chat on 2026-11-13 explicitly approving the linked Design R1 and ADR-0016 and requesting
      Tasks preparation only.
    quote: Sim, aprovo o Design R1 e o ADR-0016. Prepare somente as Tasks, sem iniciar a implementação ou publicar.
    revision: 1
    digest: 007c4ba449c55cbdf7bd45e139973d678142d5a24bd5e18ed2c6aa53aec87aa0
---

# Design

## Current state

Proposal/Requirements R1 was approved by the user's “Sim” on 2026-11-13; the combined digest remains `41081278df433db671e12b7d442b78a446f792977cc976a37407a5113ee62443`. Work continues in the attached managed worktree at source `d61317d9220b002f0dc3aa606e18a62dd4230477`. The original two-file planning checkout is preserved, not a second active dossier in this working tree. The unique active dossier here retains `harness-publication-readiness`.

The provider, index-resolved Standards and historical sources are those resolved in Proposal. VERSION/manifests are 0.3.0; the marketplace is `versat-internal` at `v0.3.0`. Local tag v0.3.0 resolves to `db04b4aa645e6bef94b60cd172dcaa4183646a1e`. Current source adds SDD v3 assurance, explicit test execution, guides and H01/H02 material beyond that tag. Never describe source behavior as shipped solely because VERSION still says 0.3.0.

The existing root package, v3 planning/evidence contract, package validator and full validation script are reused. H01's approved proprietary text and H02's scoped pilot/internal receipt remain historical evidence. Private/public access and effective adoption remain distinct. The package currently includes governance and validation history requiring full-surface review before any public exposure.

## Proposed design

### 1. Preserve one package; prepare an explicit adoption candidate

Select **0.4.0** for the candidate: a new pre-1.0 minor release reflects the source-level SDD/consumer and public-distribution changes, without claiming backward compatibility for an automatic upgrade. A read-only remote query for `refs/tags/v0.4.0*` on 2026-11-13 returned no tags. Recheck availability and base drift before adoption; if occupied, stop and revise the selected release through review, never overwrite it.

Preparation leaves the active root VERSION/manifests/marketplace at 0.3.0. Future implementation prepares an adoption patch that moves the intended release tree to matching 0.4.0 metadata and applies the exact approved license/notices. The patch has an explicit base commit and hash and is rehearsed in a disposable private checkout of the **same repository root**. No mirrored repository, standalone SDK, copied Standards tree or release automation is introduced. The two metadata states are separate trees: each must be internally consistent; no mixed-version package can pass.

Keep marketplace name `versat-internal`, Plugin name `versat-ai-harness`, repository URL and existing workspace route. A public label change or identity migration is not needed for the selected distribution boundary. Installed releases and consumer locks remain untouched. Current source stays accurately marked as preparation until separately authorized adoption. No v0.4.0 tag, release or public install command is claimed available before observed creation/access.

### 2. Concrete future artifacts and ownership

Paths below are planned outputs of later authorized implementation; only Design and the proposed ADR are created now.

| Artifact/surface | Planned treatment |
|---|---|
| `standards/core/licensing-publication.md`, `contribution.md`, `security.md` | Reconcile the applicable public-Harness review contract through the existing index; preserve common policy and per-product boundaries. No copied policy inside Skills. |
| `docs/licensing/candidates/apache-2.0/` | Concrete official license text candidate, applicable notice/third-party candidate, explicit covered-file/component inventory and review wrapper. Exact candidate text/hash and reviewer capacity are recorded; candidate status is not an effective grant. No invented copyright, notices or terms. |
| `docs/licensing/harness-plugin-terms.md` and active licensing/contribution guidance | Mark the former proprietary candidate as superseded for the future scope through transparent administrative status, retaining its substantive clauses and frozen reviewed copy. Route to the new candidate without pretending adoption. |
| `docs/licensing/reviewed/`, H01 approval, prior dossiers/validation | Preserve exact historical texts and evidence. New replacement decisions live in this successor; do not edit frozen approvals or relabel their results. Any exposure conflict triggers defer and separately governed remediation. |
| `docs/handoffs/harness-publication-readiness/` | Safe preparation summary, immutable scrubbed review-input manifest, exact adoption patch/base/tree manifest and operational handoff. No secret or private evidence payload, internal address, private URL, or customer/personal data. |
| README, `docs/product/overview.*`, quickstart and maintained EN/PT/ES guides | Extend for external readers; remove private dependencies from active public-facing instructions while preserving useful workflow references. Clearly identify candidate availability and unverified operations. |
| Root `CONTRIBUTING.md` / `SECURITY.md` and `.pt.md` / `.es.md` siblings, if needed for GitHub entry discovery | Thin repository-specific entry points to maintained guides; no competing policy manual. Reporting availability is stated only for the verified audience/scope. |
| VERSION, portable/Codex manifests, marketplace and template lock | Remain unchanged in preparation; exact 0.4.0 changes are in the adoption patch and private rehearsal tree. Patch also identifies changelog and approved root license/notice placement. |
| `docs/validation/harness-publication-readiness/` | Safe dated check records and individual assessments only. Raw sensitive evidence stays outside the prospective public repository. |

### 3. Review capacities and private evidence

Reuse the recorded accountable owner `@elviszoz` for execution coordination, licensing/security decisions and approval within the capacity already declared in H01/H02. Use existing scoped technical CODEOWNERS `@elviszoz` and `@evertonspohrversat` for technical review; record who actually reviewed rather than asserting both did. A CODEOWNER assignment does not prove specialist qualification, independent approval or control enforcement. No invitations or messages are sent by this Design.

The existing private **strategy repository** is the selected restricted evidence system; use its `docs/validation/harness-publication-readiness/` area during separately authorized implementation evidence work, with existing repository access controls. Verify it remains private and that actual reviewers can access the relevant records before writing or relying on evidence. If either condition cannot be verified, leave evidence unavailable and the relevant review deferred; do not fall back to the public-candidate root. No new external service or sharing expansion is selected. This Design does not write to that repository.

Keep raw inventory, private remote URLs, rights evidence, control observations and any sensitive finding there. Public-safe summaries use scope, method/date, aggregate status and opaque evidence IDs only. A scrubbed review-input manifest in the Harness handoff identifies the exact reviewed base, evidence revision/digests, categories covered and review/disposition status without exposing confidential content. Private records remain accessible to authorized reviewers; opaque IDs and hashes alone cannot establish real review. Revalidate known remote or evidence changes and rerun affected checks even if local source hashes are unchanged.

Reuse H01's bounded first-party attestation and seven installed dependency license texts; inspect the actual delta and proposed distribution, including any dependencies newly bundled in a candidate. Do not ask again for unchanged provenance merely because the session changed. Missing contributor rights, incompatible terms or a necessary specialist interpretation stays a named blocker to the affected clearance. Gate 2 reviews this method, not unseen legal text or a claim of professional legal review.

### 4. Licensing and full-surface decision

Prepare exact Apache-2.0 candidate text from the official source in later implementation, preserve third-party notices and record the candidate's origin/hash. Review all eligible first-party code/templates/docs rather than assuming a code license covers every asset. No root LICENSE or effective adoption occurs in the preparation tree. Review the adoption patch's license placement and scope explicitly before any separately authorized application.

The surface inventory covers the current tree (including intended untracked content), reachable branches/tags/history and deleted historical content, releases/assets, LFS, fixtures, SDD/validation material, issues/PRs/comments/attachments, wiki/discussions/Pages where present, packages, CI logs/artifacts/caches and metadata/integrations that can become exposed. For each category capture exact scope/revision, observation date and method, reviewer/access, disposition and exit condition. States are observed-reviewed, observed-absent and inaccessible/unverified. An absent result requires an actual observation, not an empty search presumed complete.

Read-only scans and inventories support human review; no clean scan clears rights or confidential history automatically. Known sensitive content, inaccessible required surfaces or drift means `defer`. Do not destroy history or modify immutable evidence. If the selected existing-repository boundary cannot be made safe within scope, record the concrete conflict and reopen the appropriate planning decision instead of publishing a filtered mirror or deleting history silently.

## Boundaries and contracts

- Policy remains in index-resolved Standards; SDD retains the process and evidence semantics; Skills route to them; validators enforce bounded mechanical invariants. No validator weakening, new exemption, automatic public-release engine or duplicated manual is planned.
- Other products retain their own rights, licenses, adoption and integration evidence. Organization default guidance remains usable and unchanged; cross-repository routing changes require their own review/authorization and verified replacement destination.
- Existing root architecture and accepted ADRs remain effective. Proposed [ADR-0016](../../../docs/decisions/0016-public-harness-preparation-boundary.md) records this public preparation/adoption boundary without superseding ADR-0011. Its reviewed SHA-256 is `f3c2749a562959bac21fbde119bd3988046bd154a1da1e68a54d8137fa1b25c6`; any substantive change requires Design re-review. The ADR index and current architecture description will be updated only with authorized implementation.
- The prior Issue-22 linkage and literal historical version 0.2.0 are intentionally replaced where Proposal says so; useful provenance, canonical guides and exact-version semantics are retained. Private recording URLs remain attributable in restricted history rather than mandatory public instructions.

## Runtime and rehearsal target

The selected first rehearsal target is the observed local **Codex desktop 26.915.31945, build 9922, macOS 26.5.2 arm64**, read from the installed application's metadata on 2026-11-13. This identifies a test target, not proven compatibility or a minimum supported Codex release. Python validation support remains 3.11+, with the observed environment Python 3.11.4, PyYAML 6.0.2 and jsonschema 4.23.0 from the pinned requirements. CI retains its current Python 3.11 Ubuntu configuration; record the resolved runner image/runtime when it actually runs. No support for other desktop/CLI/OS combinations is claimed by this plan.

A later installer rehearsal must use a supported client route actually available in that build and record exact UI/command steps, installed candidate identity and resolved resources. Do not invent an installation command from package layout. Use a disposable client context and synthetic consumer so existing user installations are not replaced. If the runtime lacks an independently usable test context or loading route, report the install case unverified and request a concrete test-environment decision; a local file read cannot stand in for installation. Public anonymous acquisition remains a later operational check.

Reuse `tests/skills/fixtures.py --case new-intent` and the corresponding prompt for the real first-use scenario, together with `tests/skills/verification.py` and the [supervised evaluation procedure](../../../docs/guides/skill-evaluations.md). One fresh native scenario invocation, without inherited implementation conversation, is allowed only during the later approved rehearsal. The coordinator independently inspects the resulting files, canonical resources and observed stop. Native subagents share permissions; a fresh directory/context is not security isolation. No such invocation is performed at this planning gate.

## Data, security and permissions

Preparation may read actual settings through existing authorized access but does not change visibility, access, rulesets, required checks, fork permissions, security channels or external records. Later implementation authority must explicitly cover any private rehearsal installation; it never implies changes to existing installed consumers. Synthetic scenarios contain no production payloads, credentials, real vulnerability or private company records.

Assess effective branch protections, reviews, CODEOWNERS, required-check enforcement, workflow events/token permissions, untrusted fork execution and access to write/deployment secrets. Missing or ineffective controls block operational readiness. Source YAML, a repository administrator view and local tests are insufficient. Any remedial configuration operation is separately proposed with exact scope and observed outcome; no bypass is designed.

Reporting keeps current CODEOWNER responsibility and the limited .github PVR/internal email evidence intact. The intended public Harness route is GitHub Private Vulnerability Reporting for this repository, subject to actual availability. The operational protocol uses an authorized non-sensitive marker from an intended external reporter account, verifies private access boundaries and recipient receipt, and retains minimal safe evidence. No message, channel activation, permission change or fabricated test account is authorized now. Until that route is verified, public candidates state the limitation and offer only a non-sensitive request for private instructions through an existing visible maintainer contact. Do not export internal email addresses, promise an unapproved response time or invent retention limits.

## Operations and observability

The handoff has explicit independent fields: documentation prepared; text candidate reviewed; rights/surface/control disposition; private rehearsal observed; source merged; license adopted; repository visibility; exact tag/release available; external walkthrough observed; reporting/controls rechecked; consumers migrated. Each observed field records scope/revision, method/date, actual authority and evidence. Unknown remains unknown; one successful product or stage does not complete another.

A preparation assessment can complete with `defer` and a truthful report of blocked publication. It cannot claim H03 delivered, publish-ready or operational success. Missing required private rehearsal, actual text review or other required preparation evidence prevents preparation acceptance rather than being waived by a comprehensive report. Distinguish a **completed negative assessment** (for example an observed sensitive-history blocker correctly recorded as defer) from an **unexecuted required check** (unverified). A future public-availability claim requires actual post-operation evidence regardless of this dossier's documentary closure.

Record check IDs, exact inputs before/after, candidate tree/patch hashes, runtime identity, real review source and per-obligation outcome. No new telemetry service is introduced. Use approved restricted retention/access practices for sensitive records; preserve non-sensitive attempts and provenance without duplicating private conversations in the Harness package.

## Migration, rollout and rollback

1. After all planning gates and explicit implementation authority, prepare concrete candidates, safe maintained guidance and actual private assessments; produce the exact adoption patch and private candidate checkout. Do not apply that patch to the live repository or tag it merely to make tests pass.
2. Exercise the exact candidate and failure paths; complete private text/rights review and report cleared/deferred scope. Re-run existing package suites in both trees. Preserve v0.3.0 and old consumer configurations.
3. Validate and prepare documentary closure of the preparation change in its implementation branch. Run ordinary delivery after the complete ledger, then the archive move and final `delivery --require-archive` guard. PR publication/merge retain their own actual authority and required checks. No pre-merge task depends on its own final merge or a public operation.
4. Only when requested and prerequisites satisfied, review the actual adopted root tree/patch, recheck source and remote-surface drift, exact release availability and controls, and execute separately authorized license/visibility/release operations in the reviewed sequence. Any source change after preparation requires appropriate revalidation. An available tag alone does not license a different tree or verify anonymous access.
5. Verify anonymous acquisition, external installation/update/contribution without private membership, actual public-audience reporting and post-visibility protections. Failures remain failed/unverified with bounded containment and their next owner; they never become retrospective preparation passes.
6. Consumers explicitly select the new exact reference through their own reviewed migration. Preserve and restore the last verified compatible release and lock/config pair on a failed update. A consumer with active SDD v3 records must not be rolled back to a provider incapable of reading them; retain a verified v3-capable provider or use a separately reviewed migration. Do not remove version markers or silently choose latest.

Rollback of draft metadata/guidance is a reviewable source change. Operational containment requires its own authority and cannot promise erasure of public copies or revocation of existing grants. Preserve evidence before bounded remediation.

## Alternatives considered

| Alternative | Decision |
|---|---|
| Apply root Apache terms immediately during preparation | Reject: conflicts with separate concrete-text review and adoption authority. Stage exact files/patch and test a private candidate. |
| Keep proprietary restrictions for the public Harness | Reject: contradicts approved Apache scope. Retain them only as clearly identified historical candidate text. |
| Public mirror, new SDK, separate packaged policy copy | Reject: changes the selected destination/source-of-truth contract. Escalate if full-surface findings make the existing repository unsafe. |
| Automatically update marketplace identity or consumers | Reject: no need established; preserves existing installations and explicit migrations. |
| Verify only package structure or a release ZIP | Reject: cannot establish rights, remote/history safety, real client use, confidential reporting or actual controls. |
| Require post-publication success before merging preparation | Reject: creates an authority/dependency cycle. Keep operational verification mandatory but separately scoped and recorded. |

## Validation plan

### Common execution and freshness contract

The ten frontmatter checks are **future required checks**, not current results. All source files are declared inputs (`.`) because package/repository publication crosses all existing paths; `.git` and this dossier are automatically excluded by the canonical helper, and the stable `docs/validation/harness-publication-readiness` output subtree is explicitly excluded. Existing historical validation trees remain inputs and must not be edited. No execution output is written elsewhere beneath the input root. The immutable adoption patch and its base are candidate inputs; store a computed rehearsal tree identity only in excluded run evidence or the restricted record, never in a file whose own hash it claims to contain. Safe input manifests bind external evidence revisions and patch content, not their own enclosing tree or mutable check results. Reconstruct and recheck the final candidate after any patch, guide, archive-link or other relevant source change; do not relabel an earlier tree as final. Disposable rehearsal checkouts/consumers and private evidence are outside the Harness tree and have separate manifests.

Before each real check, freeze the candidate/source, adoption patch, scrubbed review-input manifest and private evidence revision. Capture canonical `--input-digest CHECK-NNN` before and after; require equality for a pass. Record external-state acquisition time, method/access, scope, private evidence digest/revision and actual reviewer observation. Any known remote/runtime drift invalidates affected evidence even if local snapshots match. A raw scope hash does not authenticate execution or ensure complete remote inventory.

Each check writes its own dated safe record under the excluded output subtree. No check uses another mutable result record as its input or requires the final delivery guard as a prerequisite. Shared fixed candidate/evidence inputs can be reused; independent observations may support multiple assessments. Only after every actual result is recorded do Tasks receive the individual 38 local and 72 retained-obligation assessments. The final delivery/archive checks remain separate so CHECK-010 never depends on its own completed ledger.

### Licensing and rights procedure — CHECK-001

Compare exact old and proposed permission clauses, covered-file inventory and notices. Confirm the old frozen text/approval hashes match the source baseline. Inspect prior bounded provenance/dependencies and the proposed candidate delta, including whether installed tools are bundled. Authorized reviewers inspect actual underlying evidence and record capacity, exact text/hash, decision and any limitation. Walk three synthetic decision cases (missing grant, incompatible dependency and missing actual reviewer) plus the actual inventory: all unresolved cases must defer with owner/exit condition. A positive hypothetical example must not clear a real component. Missing actual concrete-text review is unverified, not pass.

### Surface and evidence procedure — CHECK-002

Enumerate every category in the full-surface decision above using read-only Git/provider views. Record pagination/completeness limitations and inaccessible areas; compare intended release tree and reachability to observed remote refs. Review all categories for rights/confidentiality and do not assume a scan covers conversations, artifacts or LFS. Use synthetic old-commit/attachment findings and an intentionally changed reviewed fingerprint to verify defer/drift behavior. Inspect the real public candidate for confidential payloads/links and verify sensitive records are held only in the selected restricted system. Unknown surface can produce an observed negative disposition, never publish-ready clearance.

### Package and version procedure — CHECK-003

Check the adoption patch against its exact base and full candidate tree manifest. Run the maintained Plugin validator on both preparation and candidate roots. Verify supported Skills and every canonical resource directory actually exist and are resolved from that candidate. Mutate only disposable copies: mismatch one manifest version, then add the legacy nested package path; each must cause validator failure while the original candidate passes. Assert v0.3.0 remains unchanged. Do not weaken the maintained validator, infer a release from a local version, or create a persistent alternate distribution tree.

### Private client rehearsal — CHECK-004

Use the selected target and actual supported loading route in a disposable client context. Record the observed source/reference, package identity, resource paths and actions. There are six bounded cases: (a) initial install/load plus one real `new-intent` planning invocation; (b) missing provider/access; (c) unavailable exact version; (d) declared incompatible provider/runtime or missing required resources; (e) explicit old-to-new synthetic-consumer migration; (f) simulated update failure with preserved/recovered previous compatible config. Exercise failures through the real wrapper/client path when available, not by printing canned messages. If a client cannot exercise a required failure, report unverified.

For (a), use the maintained synthetic fixture/prompt and verify only Proposal/Requirements, no fabricated approval, no Design/Tasks or product edit, and an actual Gate 1 stop. The coordinator independently checks artifacts/diffs and the version-matched validator; a scenario agent's narrative alone cannot pass. One fresh native invocation, at most 600 seconds including independent verification. The other five cases have at most 300 seconds each; the suite cap is 2,400 seconds including setup/inspection. Monitor elapsed time, interrupt at limits, retain all failures/overruns and available telemetry, and do not automatically retry. A later fix/rerun requires a separately recorded bounded attempt. No public test message, remote contribution or existing consumer change is allowed. A source-only load cannot be relabelled a successful installation when the package installer was not observed.

The previous verified fallback is selected from the actual consumer's compatible provider/config pair, not assumed always to be v0.3.0. Record the source baseline's unreleased v3 semantics and test the refusal to downgrade an active v3 consumer to an incompatible provider. Fresh directories and native contexts share permissions and are not represented as isolation controls.

### Contribution/control procedure — CHECK-005

Trace issue selection, provenance, terms, fork/branch/PR preparation, SDD, checks and review through maintained guides. Prepare a synthetic local contribution/diff without opening a remote PR. Read actual applicable rules/settings when accessible and inspect untrusted fork workflow events, token permissions and secret paths; record what is unobservable. Compare stated controls with real configuration. Evaluate missing permission/provenance and missing required control cases: no contribution acceptance or public-readiness claim. Preserve organization defaults, issue forms and repository-specific precedence; do not modify another repository.

### Reporting procedure — CHECK-006

Read original limited pilot/private receipt evidence and retain its exact scope. Inspect the future Harness route protocol for intended reporter access, permitted recipients, owner responsibility, confidential handling, receipt and withdrawal/reverification. Evaluate unavailable, denied and changed-route cases with safe synthetic descriptions only. Verify candidate languages neither promise an active public route nor expose internal addresses. Actual public Harness submission/receipt, notification and confidentiality checks remain mandatory in the separately authorized operational follow-up; this preparation check verifies truthful status/protocol, not their future outcome.

### Documentation procedure — CHECK-007

Read every affected EN document and PT/ES sibling, including entry navigation, product audience, candidate terms, release prerequisites, explicit upgrade, failure/recovery and gates. Use local path/anchor inspection and access-aware external link observations; never assume authenticated access equals public access. Compare each changed action with CHECK-004's real observations, retaining unverified cases. Verify guidance works without private URLs, internal recordings or evidence while preserving stable canonical references and unrelated workflow information. Exact commands/UI steps are documented only after observed on the selected client. Do not create generic documentation or multilingual automation unrelated to this change.

### Retained-contract procedure — CHECK-008

Use every frontmatter regression row and read the bound historical acceptance text, effective Proposal baseline and relevant current source. Observe actual preserved behavior and cite current check evidence for each of the 72 retained obligations. The common source cases require real policy disposition review, package/version checks, client/guide behavior, translation review and authorization boundaries; enumerating IDs cannot pass them. Check frozen history against the base, identify permitted active-document administrative annotations separately and preserve original approvals. Inspect all seven supersessions and replacement scenarios explicitly, including current candidate version, Apache permissions, safe public provenance and current issue linkage.

### Required suites — CHECK-009

Retain `./scripts/validate/run.sh` and all its package, SDD, validator and execution suites in both preparation and private candidate checkouts, using pinned dependencies. Record actual counts and full exits; no skipped/empty suite may claim success. Existing historical compatibility warnings remain scoped to those dossiers. Fixture/mutation failures expected by CHECK-003 are distinct from this suite's required pass. Remote CI and required-check configuration are observed separately at delivery; this local check cannot claim them.

### Handoff and gate procedure — CHECK-010

Review exact candidate/patch/tree and original evidence against every readiness field; identify actual reviewers, authority, dispositions and all pending post-operation outcomes. Exercise wrong revision, missing evidence, unauthorized action and failed post-visibility cases: stop or defer with a named owner rather than mark ready. Verify the operational runbook includes pre-action drift/permissions, explicit adoption/visibility/release scope, mandatory anonymous obtain/install/update/contribution, Harness reporting/control checks and bounded containment. Ensure rollback does not promise to retract copies/rights.

REQ-012/1 describes the actual Gate 1 event: verify the preserved presented two-file revision and approval source; do not delete subsequently authorized Design to recreate it. REQ-005/4 and future-operation clauses in REQ-006/7/9 are preparation contracts at this change: verify a complete testable handoff and truthful unverified status, not a fabricated future pass. Missing required private preparation evidence still blocks delivery. No operational outcome is excluded as not-applicable. The mapped future requirements remain mandatory for the later public-readiness claim.

## Planning review

Design R1 and proposed ADR-0016 are presented together against approved Proposal/Requirements R1. Gate 2 is awaiting approval; approval is null and no Design decision is left unresolved. Candidate 0.4.0, the observed rehearsal target, restricted evidence system, existing reviewer capacities and separation of preparation/adoption/operations are explicit choices for this review. Their future execution, rights/surface findings and actual availability are not asserted successful.

Approval unlocks Tasks preparation only. No Tasks file, candidate license/patch, live guidance/metadata update, rehearsal, remote mutation or implementation ledger is created at this gate. The observed preparation results are recorded below; they are not executions of the ten future implementation checks.


Preparation verification observed on 2026-11-13:

- Selected planning validation returned exit 0/pass with no findings or warnings: all 38 local scenarios and 72 retained obligations have required check mappings, with no exclusions.
- The full required `./scripts/validate/run.sh` was run with the verified Python 3.11.4 environment and pinned PyYAML/jsonschema dependencies. Final exit 0: portable package and SDD inventory passed, all 131 validator tests and 48 execution tests passed. Existing legacy/v2 inventory warnings remain unchanged historical limitations, not new exemptions or failures. The suite ran after the final check-mapping and evidence-dependency refinements.
- Independent inspection confirmed the 38/72 mappings exactly once, all 11 local Markdown links, no trailing whitespace, unchanged Requirements bytes, no Tasks, and byte-for-byte preservation of all 1,382 pre-existing tracked files. No license, package metadata, living specification, historical dossier or validator was changed.
- Gate 1 remains approved with the unchanged combined digest `41081278df433db671e12b7d442b78a446f792977cc976a37407a5113ee62443`. Canonical Design R1 digest: `007c4ba449c55cbdf7bd45e139973d678142d5a24bd5e18ed2c6aa53aec87aa0`. ADR-0016 remains Proposed at the exact SHA-256 bound in Design.
- Gate 2 is pending. These diagnostics establish planning consistency and retained tooling health, not candidate license acceptance, installation, surface clearance, live control/reporting verification, remote CI or public readiness. No ten-check implementation ledger or approval has been fabricated.

### Gate 2 approval — 2026-11-13

The user explicitly approved Design R1 and ADR-0016: “Sim, aprovo o Design R1 e o ADR-0016. Prepare somente as Tasks, sem iniciar a implementação ou publicar.” Before recording acceptance, the canonical Design digest was reverified as `007c4ba449c55cbdf7bd45e139973d678142d5a24bd5e18ed2c6aa53aec87aa0`, the upstream Proposal/Requirements digest as `41081278df433db671e12b7d442b78a446f792977cc976a37407a5113ee62443`, and the exact reviewed ADR hash as `f3c2749a562959bac21fbde119bd3988046bd154a1da1e68a54d8137fa1b25c6`. Earlier pending statements preserve presentation history; the structured approval records the current state.

ADR-0016 received only a status-line update and an administrative acceptance section. Its substantive reviewed bytes are preserved and independently reconstructable; current annotated SHA-256 is `86166b314d26787aa488385a6c41544661ff0abc8e53eb2eb1bc1eb96abef743`. The bound hash in the substantive Design identifies the original reviewed ADR, not the later administrative annotation. No substantive Design or upstream content changed. This approval unlocks Tasks preparation only and explicitly withholds implementation and publication.
