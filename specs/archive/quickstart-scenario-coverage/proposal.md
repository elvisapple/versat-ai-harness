---
sdd_version: 2
change: quickstart-scenario-coverage
status: accepted
owner: versat
summary: Keep practical usage guides current and verify relevant acceptance scenarios within the existing SDD lifecycle
risk: low
review:
  revision: 1
  state: approved
  blockers: []
  upstream: {}
  approval:
    source: "Developer reply in this conversation immediately after the request to approve Proposal and Requirements R1 and proceed to Design"
    quote: "sim"
    revision: 1
    digest: 5a1170e5847ce0e113aa1ea89032a5e27b63ec9619db62c5e292636a5a317f7f
---

# Proposal

## Context and problem

The Harness already requires observable acceptance criteria, a required check for every requirement, implementation tests and actual validation evidence. Planning includes necessary documentation, but the Documentation Standard focuses on repository context, architecture and living specifications. It does not explicitly cover instructions for using the delivered product or verification of documented examples. The base README links to the product overview but has no quickstart guidance.

A check linked to a requirement can cover its successful path while missing relevant error or boundary scenarios. The SDD guide mentions edge cases, but the planning and validation instructions do not make this coverage expectation explicit.

The developer requested these improvements without additional bureaucracy or unnecessary Harness artifacts. A quickstart should help a user reach a first useful result and provide a reproducible usage scenario for validation.

## Expected outcome

Consumer projects maintain one discoverable, concise starting guide for actual product usage. Changes update affected usage instructions and verify relevant acceptance scenarios, including meaningful failures and boundaries, through the existing planning, implementation and validation records.

## Scope

- Clarify the canonical Documentation and Testing Standards, resolved through `standards/index.yaml`.
- Use `docs/quickstart.md` as the default living guide in consumer projects without an equivalent guide. Reuse an existing suitable location and link the actual guide from the root README.
- Keep the first useful workflow in one guide. Add focused guides under `docs/guides/` only when distinct workflows need more explanation; link them from the quickstart instead of duplicating setup instructions.
- Keep usage documentation outside the movable SDD dossier so archival preserves its public entry point.
- Integrate documentation impact, affected examples and relevant scenario coverage into existing SDD planning, implementation and validation instructions. Reuse existing requirement/check/task identifiers and evidence records.
- Align shared bootstrap/template guidance and the SDD developer guide with this behavior, preserving base/profile composition and creating content only when meaningful product instructions are available.

## Out of scope

New SDD phases or approval gates; a fifth mandatory dossier artifact; a separate test-case catalog or test-plan file; scenario IDs or metadata/schema changes; new validators or coverage quotas; mandatory TDD; exhaustive user manuals; documentation websites; a file per feature or change; automatic test generation; rewriting historical dossiers; retrofitting existing consumers; release publication or installed Plugin updates.

## Work tracking

No Shortcut Story is associated with this request. The local branch is `codex/quickstart-scenario-coverage`; no Story identifier or remote PR is invented. Policy delivery remains subject to the existing PR, review and required-check rules.

## Impact and risks

The source package reports version `0.2.0` and contains unreleased SDD changes. This planning work uses this repository's canonical process and Standards; it does not substitute the older installed Skill's lifecycle or claim consumer adoption. The provider repository has no consumer `.versat/project.yaml` or lockfile; consumer profile selection remains governed by the existing index.

The main risks are duplicate instructions, an oversized quickstart, misleading documentation for unimplemented features and testing ceremony disproportionate to risk. Reusing existing documentation, keeping a short first-use path, updating it alongside implementation and selecting meaningful scenarios address these risks. Documentation language, translations and sensitive-data handling continue to follow the existing resolved Standards.

The responsibilities of Standards, SDD, Skills, templates and validators remain unchanged. This proposal does not introduce an architectural boundary change.

## Proposal acceptance criterion

The revised guidance lets a project expose a working first-use guide through its root README, keep affected instructions and examples synchronized with implementation, and assess relevant acceptance scenarios using existing SDD records. A small or internal change can comply without creating a new guide, test catalog, approval step or empty artifact.

## References

- [Documentation Standard](../../../standards/core/documentation.md)
- [Testing Standard](../../../standards/core/testing.md)
- [SDD planning](../../../sdd/workflows/new-change.md) and [validation](../../../sdd/workflows/validate-change.md)
- [Project template composition](../../../project-templates/README.md)
- [Spec Kit quickstart planning instructions](https://github.com/github/spec-kit/blob/main/templates/commands/plan.md): comparative reference inspected during this conversation; its per-feature dossier location is not the proposed consumer convention.
- [OpenSpec default workflow](https://github.com/Fission-AI/OpenSpec/blob/main/schemas/spec-driven/schema.yaml): comparative reference for delivering and checking necessary tests and documentation with the work that requires them.

External references are contextual, mutable upstream sources, not normative dependencies or consumer version pins.

## Planning review

The developer approved the presented Proposal and Requirements R1 with the reply "sim" to the explicit request to approve those documents and proceed to Design. The canonical combined digest was computed before recording the approval. This approval unlocks Design only; it does not approve Design, Tasks, implementation or publication.
