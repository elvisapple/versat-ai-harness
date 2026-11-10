# Licensing and publication review

[English](licensing.md) | [Português](licensing.pt.md) | [Español](licensing.es.md)

Use this guide to prepare a component review. The policy and terms in this private source are implementation candidates, not adopted licenses or a public release. The [terms candidate (English)](../../licensing/harness-plugin-terms.md) has owner text approval; see the [approval record (English)](../../governance/h01-approval.md). It is not effective, and component rights/notices verification remains separate.

## Prepare

Identify the component, exact revision, intended audience/distribution, original and third-party material, rights/grant references and notices. An authorized reviewer needs access to the actual evidence; do not copy contracts, credentials or personal data into the package.

Use the [common policy (English)](../../../standards/core/licensing-publication.md), [notices inventory (English)](../../licensing/harness-plugin-notices.md) and [private review ledger (English)](../../governance/licensing-review.md). Keep tool terms distinct from the target project's terms.

## Try one review

Example: a proposed public component includes a copied template with no verified grant. Record the component/revision and missing evidence, set disposition to `defer`, identify the responsible owner and require verification before reconsideration. Do not assume permission from a public URL or source commit.

Expected result: an attributable decision record with the gap and next action, not license application or publication. A fully reviewed hypothetical surface could receive a `publish` recommendation, but actual publication still needs separate authority and executor evidence.

## Recover and hand off

If rights, dependencies, reviewer authority or the full export-surface review are missing, keep the decision pending. Review relevant history, tags, releases, LFS, fixtures, CI and attachments as part of the actual publication handoff; a clean current tree is insufficient.

Platform, Workspace, Discover and CRM each need their own terms/adoption evidence. Harness/plugin distribution is separate. Source changes do not update installed consumers or grant rights. Use [contribution guidance](contributing.md) for participation and [GitHub delivery](github-delivery.md) for the governed delivery process.

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
