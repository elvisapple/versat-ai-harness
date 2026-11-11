# Report a security concern safely

[English](security-reporting.md) | [Português](security-reporting.pt.md) | [Español](security-reporting.es.md)

Current verified H02 scope (2026-11-11): **the `.github` PVR pilot and receipt by the Harness owner through internal email were verified with authorized synthetic tests**. Other repositories require their own checks. The custom form remains in an unmerged PR; its deployment and inheritance were not tested. This guide does not promise a response time or continuous monitoring.

The relevant CODEOWNERS are responsible for monitoring, triaging and coordinating the resolution of security reports for their owned components, through both public-repository PVR and private-repository internal email. Maintainers configure the necessary permissions and notifications; CODEOWNERS assignment alone does not configure GitHub delivery.

## Selected routing — private implementation candidate

For ordinary bugs, use Bug report. For suspected vulnerabilities in public repositories, use GitHub Private Vulnerability Reporting when enabled. For private repositories, email the relevant CODEOWNERS through existing internal Versat channels. Do not disclose vulnerability details in ordinary issues. See [security reporting](../../handoffs/contribution-security-guidance/organization/candidate/SECURITY.md) for routing and unavailable-channel recovery.

## Before sharing details

Read the target repository's actual security instructions and confirm their scope. A maintainer name or authenticated working link alone is not evidence of a confidential reporting route. Do not put exploit details, credentials, customer data or sensitive attachments in a public issue.

## When a verified route is unavailable

Use an existing visible repository/maintainer contact only to ask for private reporting instructions, without revealing the vulnerability. Example safe request: “I need confidential security-reporting instructions for this repository.” Wait for an appropriate route before sending sensitive details. This example does not send a message or authorize an agent to do so.

Expected result: a non-sensitive request for instructions, not a verified report or an active service. If you cannot establish an appropriate route, keep the report private and the verification gap explicit.

## What a verified route must establish

An actual destination, accountable responder, intended reporter audience, permitted recipients/access boundary and owner-approved data handling must be recorded. Configuration/access observations and an explicitly authorized non-sensitive synthetic marker/receipt must support any verified claim. Do not infer public reporter access from an administrator session.

The [private route record (English)](../../governance/security-reporting.md) lists the actual evidence and its limits. Fallback-only guidance does not complete H02. A changed or failed route needs re-verification and withdrawal of unsupported active claims.

Canonical rules: [Security (English)](../../../standards/core/security.md). Channel setup, permission changes and test messages require separate scoped authorization. Each product verifies its own adopted scope.

[Contribution](contributing.md) · [Harness](../../../README.md)
