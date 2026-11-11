---
sdd_version: 3
change: contribution-security-guidance
requirements:
  - id: REQ-001
    statement: "Contribution guidance MUST reuse maintained Harness and organization entry points and preserve repository-specific precedence."
    acceptance:
      - "Given the completed Issue 22 and merged Harness PR 33 and organization PR 3, their useful documentation and public contribution route are retained rather than recreated or reopened as unfinished H02."
      - "Given a contributor, the guide identifies the target repository, available issue forms, setup, contribution requirements, review/checks and actual issue/PR linkage."
      - "Given repository-specific instructions, they take precedence over organization defaults; organization identity, issue forms and local maintenance checks are preserved."
      - "Given detailed setup, SDD, validation and language procedures, guidance links to maintained sources rather than creating a competing manual."
  - id: REQ-002
    statement: "Public and private contribution routes MUST remain usable within their actual access boundaries."
    acceptance:
      - "Given a reader without private Harness access, a concise public route works through the target repository's available instructions and forms; private resources are identified and not mandatory for that route."
      - "Given a proposed destination or resource not yet available to the intended audience, existing usable guidance remains until verified replacement and separately authorized activation."
      - "Given private source or business context, no public candidate exports confidential strategy, customer information, credentials or required private links; no repository access is granted by guidance."
  - id: REQ-003
    statement: "Guidance MUST distinguish project contribution rights, provenance and approved Harness/tool terms."
    acceptance:
      - "Given a contribution containing original or third-party material, the contributor and reviewer can identify provenance, applicable rights/notices, required checks and acceptance responsibilities."
      - "Given use of the Harness/plugin, the guide references the actual approved H01 terms/version and distinguishes those terms from the destination project's license."
      - "Given missing terms, rights evidence or required review, completion remains pending; no new CLA, DCO, IP assignment or legal grant is silently selected by the planning agent."
  - id: REQ-004
    statement: "Security-reporting guidance MUST provide a verified confidential route and a safe unavailable-channel fallback."
    acceptance:
      - "Given an active reporting route, the actual destination, accountable responder, access controls and synthetic submission/receipt are checked before the route is described as available."
      - "Given a vulnerability report, instructions keep exploit details, credentials and sensitive data out of public issues and describe how to obtain confidential instructions."
      - "Given no verified channel, the guide states the limitation and allows only a non-sensitive request for private contact; it does not invent an address, promise an unapproved response time or claim activation."
      - "Given the current planning authorization, no real vulnerability submission, channel activation, access change or message to third parties is performed."
  - id: REQ-005
    statement: "Community guidance MUST use canonical English with semantically aligned Portuguese and Spanish versions."
    acceptance:
      - "Given changed community-facing material, EN/PT/ES versions preserve permissions, access limits, approval boundaries, recovery steps and channel status."
      - "Given language navigation and external references, localized equivalents and immutable or otherwise reviewed destinations resolve with the intended access; English-only canonical references are identified."
      - "Given Issues 23 and 26, H02 reuses documentation/language rules without claiming delivery of general documentation automation or multilingual CI."
  - id: REQ-006
    statement: "Completion MUST distinguish common guidance, cross-repository rollout and product-specific adoption."
    acceptance:
      - "Given H02 common guidance, Platform, Workspace, Discover and CRM still record their own adoption through P01/P03; the Codex plugin release remains H03."
      - "Given an organization entry change, its repository instructions and review apply; source availability and access are verified before activation, with existing guidance retained on failure."
      - "Given completed-work review, current content, translation, navigation, actual reporting-route verification and all applicable retained regression evidence are assessed; package structural checks alone do not establish user acceptance."
      - "Given a plan at Gate 1, implementation, public documentation changes, licensing, publication, releases and consumer upgrades remain unauthorized."
---

# Requirements

## Actors and context

Harness maintainers, contributors, licensing/legal and security reviewers, organization-default maintainers, and product owners need explicit boundaries and observable completion criteria.

## Constraints and assumptions

The user authorized planning and reconciliation on 2026-11-10, expressly excluding publication and license changes. This is a Gate 1 candidate, not implementation authorization. Technical CODEOWNERS are Elvis Zoz (`@elviszoz`) and Everton Spohr (`@evertonspohrversat`). The user subsequently appointed `@elviszoz` as executor and responsible contact for licensing/legal and security decisions, and identified Versat E.A.S. as the license-owning entity. This is a declared ownership/accountability input, not verified component rights, professional legal qualification, completed specialist review or security-channel operation. Operational decisions remain blocked until their actual evidence and authority exist.

The acceptance arrays above are authoritative. No Design, Tasks, legal text or adopted policy is created at this stage. The next stage must map every local scenario and retained impact obligation to observable checks, retaining required package validation and proportionate semantic review. No new runtime or validator implementation is requested merely to enforce wording.
