# Licensing and Publication Standard

Status: private H01 implementation candidate; not yet adopted or released. These rules define the review contract. They do not apply a license, activate terms or authorize publication.

## Scope and canonical ownership

- All products MUST distinguish common policy, concrete component terms, per-repository adoption and operational distribution.
- Public/open-source and private/proprietary components MUST use the terms selected for that component. Public availability of a tool MUST NOT be described as open-source licensing.
- A tool's license MUST NOT be imposed on a project merely because that tool was used to contribute.
- Normative policy remains here and is resolved through [the index](../index.yaml). Skills and guides MUST reference it, not keep their own policy copies.
- Changes to license models, publication scope or rights mechanisms require the accountable owner's decision and the applicable governed change. This Standard does not introduce a CLA, DCO or IP assignment.

## Component evidence

Before recommending licensing or distribution, the reviewer MUST identify the exact component, repository/revision and proposed distribution boundary, and inspect:

1. Original material, authorship and relevant employee/provider/contributor grants or other rights evidence.
2. Direct and transitive dependencies at the actual versions and combinations, copied code, templates, assets, generated/imported material and build provenance.
3. Applicable third-party terms and notices, the mode of use/distribution and any unresolved compatibility question.
4. The actual authorized decision maker, technical reviewer, licensing reviewer and security reviewer, including each person's capacity and evidence references.

A repository owner, copyright label, dependency name, metadata classifier, private visibility or a clean scan is not proof of sufficient rights. Missing evidence MUST remain explicit. A declared company name MUST NOT be treated as verified rights to every file.

Records MUST identify component/revision, rights holder as declared or verified, evidence reference and access status, terms/notices version, reviewer/authority, disposition, date, limitations and owner of the next step. Confidential contracts and personal data MUST stay in approved restricted storage outside the package. A reviewer must be able to inspect the relevant evidence; inaccessible references remain unverified.

## Publication surface and dispositions

A public-export decision MUST cover the actual tree and relevant history, tags, releases, LFS objects, fixtures, CI configuration/artifacts, attachments and other material in the proposed surface. A review of the current tree alone cannot certify that surface. Secrets or sensitive data MUST be remediated and the affected surface re-reviewed before clearance.

| Disposition | Meaning | Required follow-up |
|---|---|---|
| `defer` | Evidence, rights, compatibility, remediation, required approval or controls are incomplete. | Record the gap, accountable owner and condition for reconsideration. |
| `retain-private` | The reviewed component remains private under the owner's decision; no public export is cleared. | Record actual private access/distribution constraints and outstanding rights questions. |
| `publish` | The identified surface has documented evidence and actual required review for the proposed public release. | Obtain separately scoped operational authorization and execute the relevant product/distribution handoff; record the actual outcome. |

Unknown rights, incompatible dependencies, sensitive material, missing reviewer authority or unknown required controls MUST prevent a `publish` disposition. A disposition is neither license application nor an instruction to publish. Do not convert a synthetic example into clearance of a real component.

## Terms and approvals

Concrete terms MUST state their component/audience scope and actual installation, use, modification and redistribution permissions/conditions, and identify applicable third-party notices. An unresolved term MUST NOT be filled by an agent's assumed grant.

An approval record MUST bind the actual text revision and content hash to an observed approval source, reviewer and capacity. Planning approval, CODEOWNERS assignment, an agent-authored approval entry or a generic policy review does not approve legal wording. A substantive edit requires renewed review of the changed text.

Terms review states are `draft`, `review-requested`, `approved-candidate` and `superseded`. They MUST remain distinct from effective adoption and distribution. Do not invent effective dates, signatures, jurisdiction or authority. Record unresolved legal interpretation or required specialist review with an owner.

## Adoption and recovery

Each product MUST retain its own component evidence, concrete terms, adoption and delivery record. Completion of common policy or another product's handoff does not complete it. Preserve canonical root-package resources and exact reviewed release/consumer references; source edits MUST NOT update installed consumers implicitly.

If evidence or terms change, invalidate affected approval/acceptance claims and re-review. Preserve attributable history. Restore previously verified documentation when a later routing update fails; do not describe a code revert as legal revocation or access revocation.

Use [Security](security.md), [Git](git.md), [Testing](testing.md), [Documentation](documentation.md) and [Language](language.md) for their existing responsibilities. The [licensing guide](../../docs/user-docs/guides/licensing.md) supplies a non-normative example.
