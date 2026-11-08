---
sdd_version: 3
change: harness-user-documentation
requirements:
  - id: REQ-001
    statement: The README MUST provide a complete and concise entry point to the Harness documentation.
    acceptance:
      - Given a team member opening the README, when they orient themselves, then they can identify purpose, audience, accountable team, lifecycle, version availability and the validation entry point.
      - Given the delivered documentation, when the reader follows the README navigation, then working links reach the actual quickstart, product overview, feature guides and existing SDD collaboration reference without empty targets.
      - Given existing useful README information, when it is reorganized, then installation prerequisites, package-versus-consumer boundaries and exact-version adoption remain discoverable without presenting unreleased source behavior as installed functionality.
  - id: REQ-002
    statement: A concise quickstart at docs/user-docs/quickstart.md MUST enable one representative first-use result without duplicating the SDD contribution manual.
    acceptance:
      - Given a developer with the stated access and selected Harness version, when they follow preparation and the example planning request, then they can identify proposal.md and requirements.md for a stable change ID and understand that Gate 1 review is the next action.
      - Given missing repository access, Plugin availability or required setup, when the developer follows the quickstart, then it identifies the missing prerequisite and a concrete recovery route without claiming successful execution.
      - Given a need for later planning stages, implementation or delivery details, when the reader continues from the quickstart, then links lead to focused Harness guides and sdd/README.md; any organization contribution link uses the actual versat-labs/.github entry point rather than a nonexistent local CONTRIBUTING.md file.
  - id: REQ-003
    statement: Focused guides under docs/user-docs/guides/ MUST explain the Harness's distinct supported workflows using maintained canonical references.
    acceptance:
      - Given a user choosing a workflow, when they browse the guides, then workspace preparation, SDD in Codex, GitHub delivery, bootstrap, maintenance, audit, architecture review and validation/evaluations are covered with purpose, prerequisites, representative inputs, expected outputs and relevant recovery or stopping conditions.
      - Given existing shared setup, SDD procedures or specialized validation guidance, when detailed user guidance is written, then it links to those maintained sources and contributes workflow context without creating competing policy or copying full procedures.
      - Given SDD and GitHub examples, when a reader follows the described stages, then three planning approvals, explicit implementation authorization, archive preparation before completed-work submission, PR review, required checks and observed merge remain distinguishable; planning-only reviews remain drafts.
      - Given an unsupported capability, unavailable integration or a source-only feature, when guidance describes its boundary, then it states applicability and verification limits rather than offering fictional execution or implying automatic consumer upgrades.
  - id: REQ-004
    statement: docs/product/overview.md MUST describe the Harness product using the Issue 22 problem, job to be done and persona with evidence-aware product context.
    acceptance:
      - Given a reader unfamiliar with the Harness, when they read the overview, then they find the problem, job to be done, Versat team persona, pitch, value proposition, solution, ownership, origin, current capabilities and boundaries, with a link to Issue 22.
      - Given the base product overview topic model, when it is applied to this internal product, then timing, alternatives, innovation, scalability and social/environmental considerations are addressed proportionately, while market size and monetization are sourced, explicitly unknown or explained as not applicable.
      - Given an unsupported product claim or an unreviewed training recording, when the overview uses the source, then evidence, assumptions and open questions remain distinct, with a next validation step and links to supporting material instead of fabricated metrics or duplicated manuals.
  - id: REQ-005
    statement: English MUST remain canonical and changed organization entry guidance and every Harness README and new user-facing guide or product overview in scope MUST have aligned Portuguese and Spanish Markdown siblings.
    acceptance:
      - Given an English file in the delivered set, when its language alternatives are inspected, then matching .pt.md and .es.md files exist, including README.pt.md, README.es.md, quickstart.pt.md, quickstart.es.md and the corresponding overview and feature-guide siblings.
      - Given a translated document, when a reader switches language or follows an internal user-documentation link, then the equivalent localized page is reachable; links to English-only canonical technical references clearly identify that language and resolve correctly.
      - Given examples, commands, identifiers, approvals, prerequisites, risks and version limitations, when translations are compared with English, then their meaning and operational effect match and source revisions are reflected in all three languages before delivery.
      - Given organization README and CONTRIBUTING consolidation, when those entry points are delivered, then their English, Portuguese and Spanish versions reflect the same content ownership and access conditions and route to corresponding localized Harness guidance where available.
  - id: REQ-006
    statement: Documentation MUST preserve source traceability and have observed content, navigation, translation and usage verification before delivery.
    acceptance:
      - Given Issue 22 and the Codex and GitHub recordings, when documentation cites its sources, then the issue linkage and both exact training links are retained, restricted access is identified and unviewed video contents are not presented as verified instructions.
      - Given affected commands or UI steps, when documentation is validated, then observed outcomes are compared with documented expectations using adequate existing evidence where available; missing access or unavailable execution is recorded as unverified rather than passed.
      - Given the complete English, Portuguese and Spanish set, when delivery checks run, then links and anchors resolve, no empty placeholders remain, translation semantics are reviewed and ./scripts/validate/run.sh passes without treating structural success as proof of user acceptance.
      - Given the change dossier is archived, when users follow README and guide links, then the living documentation remains usable at its normal paths and no current usage instruction depends on the active dossier location.
  - id: REQ-007
    statement: Organization README and CONTRIBUTING guidance MUST route to a single maintained Harness source for detailed setup and development instructions while retaining organization-specific context and usable contribution entry points.
    acceptance:
      - Given the reviewed organization README, locale siblings and CONTRIBUTING, when content is consolidated, then reusable Codex setup, SDD, validation, PR and language detail is mapped to maintained Harness destinations and overlapping organization sections become descriptive links rather than a second detailed manual.
      - Given organization-specific identity, participation routes, GitHub default-file behavior and local maintenance checks, when the duplicated Harness instructions are removed, then this organization-owned information remains available and profile purpose, issue forms and repository-specific guidance precedence remain unchanged.
      - Given a reader without private Harness access, when they open organization contribution guidance, then restricted links are identified and a concise public route still explains how to choose the target repository, use its issue forms and follow its own setup and contribution requirements without requiring access to internal instructions.
      - Given existing organization claims about Codex UI, automatic Plugin installation or abbreviated SDD approval semantics, when these are reused or replaced, then current evidence and canonical Harness contracts determine the resulting instructions; unverified claims are qualified and no approval or archive boundary is weakened.
      - Given coordinated changes in the two repositories, when replacement links are activated, then the Harness destinations already exist at the linked published revision, their anchors and intended-reader access have been checked, both changes are traceable to Issue 22 and each repository's applicable review and validation requirements have been met.
      - Given an unavailable destination or an incomplete Harness delivery, when the organization routing change is prepared, then the existing entry guidance remains available until the dependency is satisfied and the handoff reports the organization work as pending rather than claiming full consolidation.
---

# Requirements

## Actors and context

The primary persona is the Versat team, especially developers planning or implementing a user story, as specified by [Issue #22](https://github.com/versat-labs/versat-ai-harness/issues/22). Reviewers need to recognize approval and delivery boundaries. Workspace administrators need distinct setup responsibilities; documentation maintainers own alignment and evidence.

The job to be done is to consult repository documentation while planning or implementing a story and understand how to use the Harness within Versat's SDD process. The outcome is successful orientation and a verifiable first action, not new product functionality.

## Functional requirements

REQ-001 defines navigation and repository essentials. REQ-002 defines the minimum first-use interaction. REQ-003 covers deeper supported workflows. REQ-004 provides product context. REQ-005 makes the complete new entry path available in three languages. REQ-006 establishes source and verification quality. REQ-007 defines coordinated organization/Harness consolidation, public access and delivery dependencies.

The acceptance arrays above are the canonical scenarios; Design will map every position and retained impact obligation to proportionate checks after Gate 1 approval.

## Non-functional requirements

- Documentation is living content outside SDD dossiers. Keep policy in Standards, process in SDD, capabilities in Skills and enforcement in validators.
- Keep the quickstart focused on one outcome. Detailed pages must contain useful workflow-specific content; do not create empty scaffolds or duplicate documents solely to fill a directory.
- Preserve existing specialized guide URLs. English-only canonical reference pages do not require translation under this bounded change; localized user pages must explain those references.
- Preserve executable snippets, file paths, Skill identifiers and normative strength across translations. Human examples may be localized without changing their expected result or authority.
- Do not copy sensitive training content or credentials. The documentation must be usable without watching access-restricted videos.
- Verify commands against the selected source/release and UI instructions against available current evidence. Record uncertainty rather than infer a successful installation, run, review, merge or release.
- Organization entry points retain short summaries and routing context, not duplicate detailed manuals. Cross-repository links must use the intended repository/ref and correct anchors rather than relative paths that resolve inside the wrong repository.

## Constraints and assumptions

- The user explicitly selected `docs/product/overview.md` after the issue/request path difference was identified. `docs/user-docs/quickstart.md` and its guides are the requested repository convention; consumer template defaults remain unchanged.
- Locale suffixes are placed before `.md`: `name.pt.md` and `name.es.md`. New SDD artifacts, technical identifiers and canonical references remain English.
- Neither `CONTRIBUTING.md` nor `CONTRIBUTYNG.md` exists in the Harness checkout. The existing organization contribution guide is `versat-labs/.github/CONTRIBUTING.md`; its setup and process sections are reviewed consolidation sources. `sdd/README.md` remains the Harness's maintained lifecycle guide.
- Organization README translations already exist. Changed contribution entry guidance must have aligned `.pt.md`/`.es.md` versions; whole-profile translation and unrelated organization content remain outside scope.
- The organization CONTRIBUTING describes Harness access as private. Consolidation does not change visibility or publish private documentation; preserve a usable public entry and explicitly qualify access to internal links.
- Organization cleanup is part of the coordinated implementation scope, governed by that repository's instructions. Remote publication is not authorized by planning approval. Final Design/Tasks must distinguish each repository's delivery checks from ordered rollout and record pending external delivery truthfully.
- Recording links and the GitHub thread are verified source references; the video contents are not reviewed because they exceed the available connector's file-size limit. Examples can proceed from canonical repository sources, with video-specific claims withheld until reviewed.
- No new runtime, integration, release, consumer migration, corporate policy or architectural boundary change is authorized by this documentation scope.
- Material planning decisions are resolved for R2. Detailed page organization, coordinated delivery mechanics and checks belong to the next stage; unavailable future verification must remain explicit and can prevent delivery readiness.
