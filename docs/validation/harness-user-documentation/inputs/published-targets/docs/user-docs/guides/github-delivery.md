# GitHub delivery

[English](github-delivery.md) | [Português](github-delivery.pt.md) | [Español](github-delivery.es.md)

Use this guide when preparing an issue-linked change for human review. You need the real issue URL, repository instructions, approved scope and the repository’s validation environment.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $versat-sdd to inspect <change-id>, prepare its delivery summary and identify missing archive or validation prerequisites. Do not publish a PR or merge.
```

## Expected result

Work on a branch using the resolved Git convention. Keep issue, requirements and commits traceable; never invent a Shortcut ID. Planning or incomplete work is reviewed in a draft PR. Before submitting completed implementation, prepare the documentary archive in the same branch and pass the selected archive preflight. Request PR publication explicitly, then obtain human review and final required CI before merge.

## Recovery and limits

Report failed or unavailable checks in the PR. Review feedback stays with the same change ID; scope changes reopen the relevant review. Verify actual merge separately from local readiness. A merge neither publishes a release nor upgrades installed consumers.

## References

- [Git (English)](../../../standards/core/git.md)
- [SDD (English)](../../../sdd/README.md)
- [SDD validation (English)](../../../validators/sdd/README.md)

[Team recording](https://versat.slack.com/archives/C0B7G255DPY/p1793910356829109) — requires Slack access. Supplemental training; video contents have not been verified for this guide. The written steps are sufficient to continue.

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
