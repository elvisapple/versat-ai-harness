# Contribute with clear provenance

[English](contributing.md) | [Português](contributing.pt.md) | [Español](contributing.es.md)

The Harness repository is public. Eligible Versat-authored material is available under the root [Apache-2.0 license](../../../LICENSE). Third-party material retains its own terms and [notices](../../../THIRD-PARTY-NOTICES.md).

## Prepare and contribute

1. Choose the actual target repository and read its README, AGENTS and contribution instructions. Its own guidance takes precedence over organization defaults. Other products retain their independent terms and routes.
2. Select an existing issue or an available bug, feature or maintenance form. Describe the need, expected result and reproduction where relevant. Do not invent an issue or Story number.
3. Identify original/third-party material, sources, versions, applicable grants and notices. Missing rights prevents acceptance. Read the [licensing guide](licensing.md); a tool's license does not determine unrelated destination-project terms.
4. Follow [setup](workspace-setup.md). For a Harness checkout, use Python 3.11+, install `requirements-validation.txt` in a virtual environment and run `./scripts/validate/run.sh --quality-base origin/main` from the root. Use the target project's own checks elsewhere.
5. To contribute to the Harness from outside the organization, fork the public repository, create a branch in your fork and open a pull request against the Harness `main` branch. Follow the [Git convention](../../../standards/core/git.md). A maintainer may need to approve the workflow run before CI starts. Public access lets you read and fork the repository; upstream write, merge and release require separate permissions.
6. For material changes, follow the [three SDD planning gates](sdd-with-codex.md); explicitly request implementation after Tasks approval. Include living documentation and meaningful checks. Follow [delivery](github-delivery.md) for archival, PR review and final checks, with actual remote-operation authority.

Expected result: a reviewable contribution with genuine issue/provenance links and observed checks. Describe unavailable verification; a local pass does not prove effective branch protections or acceptance.

## Contribution terms

Section 5 of the root [Apache-2.0 license](../../../LICENSE) governs contributions intentionally submitted for inclusion unless explicitly stated otherwise, subject to the license's definitions and any separate agreement. This guide introduces no additional CLA, DCO or IP assignment. For other repositories or versions, check their applicable terms and ask for clarification if those terms are unavailable.

## Review and recovery

The actual maintainer must review scope, provenance and required checks. CODEOWNERS identifies technical contacts, not proof of legal qualification or enforced protection. Missing rights or required review prevents acceptance. Failed checks need correction and fresh evidence; changed scope reopens the affected SDD gate. If access is unavailable, use the target's existing public participation route without the Harness when appropriate, or ask its visible maintainer for access instructions without sharing confidential information.

Keep vulnerability details out of public issues; use [security reporting](security-reporting.md). Canonical policy: [Contribution](../../../standards/core/contribution.md).

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
