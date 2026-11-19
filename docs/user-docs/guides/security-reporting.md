# Report a security concern safely

[English](security-reporting.md) | [Português](security-reporting.pt.md) | [Español](security-reporting.es.md)

GitHub Private Vulnerability Reporting is enabled for this public repository. External-reporter access, receipt and confidentiality remain **unverified** until the deferred external test is performed. Enabling the channel and completing the internal PR review test do not prove external report delivery.

Earlier H02 observations covered a different public pilot and an internal Harness receipt. They remain historical evidence and do not establish a public Harness route. @elviszoz and @evertonspohrversat share monitoring, triage and coordination; Elvis remains accountable coordinator. Either maintainer may handle a report. Record one actual handler and an explicitly acknowledged handover if that person is unavailable; two replies are not required. Assignment and CODEOWNERS do not configure notification delivery or prove report access/receipt. Both maintainers’ participation in shared triage and future tests is confirmed by the owner. Public report receipt remains unverified. An actual handover is recorded when needed; it is not a separate pre-publication simulation requirement.

The PR review policy requires one eligible non-author CODEOWNER approval; it is separate from security triage. An author's own approval cannot satisfy it, and shared ownership does not require two approvals. The actual base branch determines reviewer eligibility; see the [ownership transition](../../handoffs/harness-publication-blockers/transition.md#general-ownership-and-base-branch-transition).

The earlier GitHub Free transition procedure is historical: public opening, main protection and channel activation have occurred. The later external report/receipt/exclusion test remains pending; the [candidate notes](../../releases/0.4.0-candidate.md) distinguish these states.

## Before sharing details

Read the target repository's actual security instructions. Confirm a confidential destination, intended reporters, permitted recipients and data-handling scope before sending sensitive information. Do not post exploit details, credentials, customer information or sensitive attachments in ordinary issues. An administrator session or working URL cannot establish external-reporter access or confidentiality.

## When the route is unavailable

Use an existing visible maintainer contact only for a non-sensitive request: “I need confidential security-reporting instructions for this repository.” Wait for a verified appropriate route before sharing details. If access is denied or the destination changes, stop and request updated instructions. Keep the report private if no suitable route is available. This example does not send a message or authorize an agent to do so.

Expected result: safe instructions or an explicit verification gap, not an assumed report receipt. No internal email address, new endpoint, response-time promise or retention period is supplied here.

## Maintainer verification

For the later separately authorized public test, use one labelled non-sensitive report from an intended reporter. Verify applicable report access for both Elvis and Everton through service configuration/access evidence. Observe actual receipt by one accountable handler and denial to an unauthorized viewer. Duplicate notifications, replies and a simulated handover are not required. An actual access or receipt failure remains unresolved; record a real handover when needed. Do not infer notification delivery from assignment, send another report automatically or use another person's credentials. Keep report identifiers and payloads restricted. Reverify after visibility or audience changes; never use real vulnerability payloads for this test.

Controls, channel activation, permission changes and messages require their own scoped authority. A fallback guide does not complete required route verification. Every product verifies its own scope. See [Security](../../../standards/core/security.md), [current blocker resolution](../../handoffs/harness-publication-blockers/README.md) and [contribution](contributing.md).

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
