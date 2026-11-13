# ADR-0016 — Separate public Harness preparation from adoption and publication

- Status: Accepted in `harness-publication-readiness` Design R1 on 2026-11-13; not operationally applied.
- Date: 2026-11-13.
- Related: ADR-0004, ADR-0009, ADR-0011, ADR-0013, ADR-0014 and ADR-0015.
- Scope: Candidate distribution, public-facing instructions and private evidence boundaries. No existing ADR is superseded.

## Context

The owner selected public distribution of the existing Harness repository and root Codex Plugin under Apache-2.0 for eligible first-party material. The current source includes a reviewed proprietary terms candidate, bounded rights evidence, internal guidance and historical evaluation/governance material. Those artifacts and approvals do not establish public distribution readiness. The root is the package, so publication review must include both its complete content and reachable repository/service history.

## Proposed decision

Keep the existing repository, canonical root package and separation of Standards, SDD, Skills and validators. Preserve marketplace identity `versat-internal` and Plugin identity `versat-ai-harness`. Prepare candidate version 0.4.0 as a new pre-1.0 release; do not retag v0.3.0. The exact release ref is an intended future artifact, not a claim of current availability or permission to release.

Separate three outcomes:

1. Preparation: refresh the exact component/surface assessment, prepare reviewed Apache license and notice candidates, public contribution/security/usage guides, actual private package rehearsal and a bounded operational handoff. The assessment can finish with `defer`; that cannot be advertised as publish-ready.
2. Adoption: through separately scoped authority and reviewed changes, apply the exact approved license/notices and candidate metadata to the canonical root. Existing proprietary approvals remain historical and do not approve the changed wording. No effective date or grant is inferred from planning.
3. Publication and adoption by consumers: separately authorized visibility/release operations followed by actual anonymous/external-user checks; consumers opt into exact versions through reviewable changes.

During preparation, retain root release metadata at its existing version and store proposed metadata/license changes in one reviewable adoption patch and candidate files. Exercise that patch in a disposable private checkout of the same repository root. This is a test fixture, not a mirror, new maintained package or copied Standards source. Record exact base, patch and tree identity. A package check on the unchanged source alone cannot validate the candidate.

Keep sensitive surface/rights/control evidence in the existing restricted strategy repository, outside all prospective public Harness trees, history and artifacts. Public-facing documentation and the safe verification summary use no private URLs or internal addresses. A minimal scrubbed input manifest binds the reviewed evidence revision without copying confidential payloads. Actual authorized reviewer access is still required; an opaque identifier alone is not evidence of review.

Do not silently alter historical dossiers or approved frozen wording to satisfy a publication scan. If retaining original history conflicts with confidentiality, defer publication and obtain a separately governed remediation or destination decision. Returning a public repository to private cannot retract copies, forks or rights already granted.

## Alternatives considered

- Add an effective root license during preparation: rejected because candidate review and effective adoption require different authority and evidence.
- Publish a filtered mirror or standalone SDK: rejected because it changes the selected repository boundary and introduces another maintained source.
- Publish a clean ZIP while ignoring repository history: rejected because visibility exposes surfaces beyond that artifact.
- Rewrite old approvals or replace historical pass records: rejected because this destroys attribution and cannot establish current acceptance.
- Require anonymous public access before preparation can merge: rejected because it would force an unauthorized operation into a pre-merge task. The operational follow-up remains mandatory for a public-availability claim.

## Consequences and verification

Preparation has a concrete candidate and reproducible private tests, while unresolved rights or exposure findings remain visible. The source and candidate package are checked separately; the final adopted tree must match the reviewed patch and rerun affected checks. Technical approval does not establish legal qualification or configured remote controls. Design R1 defines ten checks, actual evidence boundaries, supported rehearsal target, review capacities and the acceptance distinction between prepared/deferred and publish-ready.

Acceptance of this ADR would accept the approach and unlock Tasks planning only. It would not approve unseen license wording, apply a license, publish a repository, create a tag, send a report or migrate a consumer. The ADR index and current architecture description remain unchanged until authorized implementation.

## Administrative acceptance record — 2026-11-13

The user explicitly approved Design R1 and ADR-0016 in this chat: “Sim, aprovo o Design R1 e o ADR-0016. Prepare somente as Tasks, sem iniciar a implementação ou publicar.” The reviewed ADR had SHA-256 `f3c2749a562959bac21fbde119bd3988046bd154a1da1e68a54d8137fa1b25c6`. Only the status line and this acceptance record were added or changed; all reviewed decision, alternatives, boundaries and consequences remain byte-identical. Removing this section and restoring the original Proposed status line reconstructs the exact reviewed bytes. Earlier conditional language is the presentation snapshot, not a pending approval.

This accepts the design and authorizes Tasks preparation only. It does not approve unseen license text, authorize implementation, apply a license, publish, create a tag, send messages or change consumers. The ADR index and living architecture are unchanged.
