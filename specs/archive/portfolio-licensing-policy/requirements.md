---
sdd_version: 3
change: portfolio-licensing-policy
requirements:
  - id: REQ-001
    statement: "A canonical portfolio licensing and publication policy MUST distinguish common governance from each product's concrete terms and delivery."
    acceptance:
      - "Given Platform and Workspace, the policy preserves their selected Apache-2.0 intent and requires separate rights, dependency, notice and publication evidence for each repository."
      - "Given Harness/plugin, Discover and CRM, the policy preserves their proprietary model and private source repositories; public availability of a plugin does not imply open-source licensing."
      - "Given a policy decision, adopting it does not apply a license, publish a product, establish SDK infrastructure or complete another product's handoff."
  - id: REQ-002
    statement: "The policy MUST define evidence-based publication and retention decisions."
    acceptance:
      - "Given a proposed distributable component, reviewers can identify its version, rights holders, grants, dependencies, copied code, templates/assets and required third-party notices."
      - "Given missing rights, incompatible dependencies, sensitive material or absent required approval, the disposition remains defer or retain-private with a named follow-up; no clearance is inferred."
      - "Given intended public distribution, review scope includes the actual tree, relevant history, tags, releases, LFS, fixtures, CI and attachments; a clean current directory alone is insufficient."
  - id: REQ-003
    statement: "Concrete proprietary terms common to Harness and its Codex plugin MUST be separately versioned and reviewed."
    acceptance:
      - "Given the actual terms candidate, installation, use, modification and redistribution permissions and conditions, component scope and third-party notices are explicit."
      - "Given technical CODEOWNERS or a planning approval, neither is treated as legal approval; terms remain unapproved until an identified authorized reviewer accepts the actual version."
      - "Given a contributor using the proprietary tool for an Apache project, the documentation distinguishes tool terms from destination-project contribution and licensing terms."
  - id: REQ-004
    statement: "The policy MUST define accountable decision roles and per-product adoption records."
    acceptance:
      - "Given a publication/licensing decision, the record identifies executor, technical reviewer, licensing/legal reviewer, security reviewer, evidence and authority rather than relying on role labels alone."
      - "Given H01/H02 delivery, each P01/P03 product still has its own acceptance and adoption evidence; H03 distribution does not block unrelated product planning."
      - "Given an unconfirmed owner or control, that gap remains explicit and prevents the affected approval or operational decision."
  - id: REQ-005
    statement: "Canonical package, policy and exact-version boundaries MUST be preserved."
    acceptance:
      - "Given new normative policy, it is resolved through standards/index.yaml; Skills reference canonical resources without copying Standards into Skills."
      - "Given an installed Skill, canonical version-matched Standards, SDD, templates, schemas and validators remain available under the existing root package contract."
      - "Given a future release or consumer update, an exact reviewed reference is required; planning changes do not update installed consumers or imply public distribution."
  - id: REQ-006
    statement: "The handoff MUST provide reviewable policy/terms evidence without executing operational licensing or publication changes."
    acceptance:
      - "Given the current authorization, only planning artifacts and private work-tracking reconciliation are changed; no license application, effective terms, release, visibility, permission or public-documentation change occurs."
      - "Given subsequent approved implementation, candidate policy and terms remain distinct from legal acceptance, adoption and separately authorized distribution; unavailable evidence is reported as unverified."
      - "Given implementation review, affected living guidance, all applicable acceptance and retained regression scenarios, package checks and final review evidence are verified before a completion claim."
---

# Requirements

## Actors and context

Harness maintainers, contributors, licensing/legal and security reviewers, organization-default maintainers, and product owners need explicit boundaries and observable completion criteria.

## Constraints and assumptions

The user authorized planning and reconciliation on 2026-11-10, expressly excluding publication and license changes. This is a Gate 1 candidate, not implementation authorization. Technical CODEOWNERS are Elvis Zoz (`@elviszoz`) and Everton Spohr (`@evertonspohrversat`). The user subsequently appointed `@elviszoz` as executor and responsible contact for licensing/legal and security decisions, and identified Versat E.A.S. as the license-owning entity. This is a declared ownership/accountability input, not verified component rights, professional legal qualification, completed specialist review or security-channel operation. Operational decisions remain blocked until their actual evidence and authority exist.

The acceptance arrays above are authoritative. No Design, Tasks, legal text or adopted policy is created at this stage. The next stage must map every local scenario and retained impact obligation to observable checks, retaining required package validation and proportionate semantic review. No new runtime or validator implementation is requested merely to enforce wording.
