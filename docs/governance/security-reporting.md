# H02 security-reporting record

Observed 2026-11-11. Accountable contact: Elvis Luis Zoz (@elviszoz).

## Selected routing and responsibility

The owner selected GitHub Private Vulnerability Reporting for public repositories and email to relevant CODEOWNERS through existing internal Versat channels for private repositories. This supersedes the tentative info@versat.ag route. CODEOWNERS monitor, triage and coordinate remediation; assigning CODEOWNERS alone does not configure permissions or notifications.

## Verified scope

The authorized .github pilot received two synthetic reports from oscarcareaga89, whose repository permission is read. Maintainer visibility, a credential-free anonymous denial, saved Security alerts subscription and actual notification delivery to Elvis were observed. The private Harness synthetic email was observed in Elvis's inbox with the intended To/Cc; Elvis is the accountable owner and current default CODEOWNER. See [actual methods, timestamps, references and limits](../validation/contribution-security-guidance/final-20261111/operational.md).

| Boundary | Observation and limit |
|---|---|
| Public pilot | PVR enabled only in versat-labs/.github; actual non-administrator report and owner receipt verified. No rollout to other repositories implied. |
| Confidential access | Authenticated maintainer visibility and anonymous HTTP 404; existing administrator/organization rights remain. No roles changed. |
| Private route | Internal recipient headers and Elvis inbox verified; Everton acknowledgment and mailbox forwarding/delegation not asserted. Internal addresses are not exported. |
| Notification | Custom Security alerts saved; GitHub email notification received and independently found in INBOX. |
| Template | Seven reviewed files in public draft PR #4; unmerged custom form rendering/inheritance remains pending rollout. Pilot used native default form. |
| Data and response | Non-sensitive synthetic markers only; minimize data, no invented retention period, SLA or continuous monitoring promise. |

## Safe failure and re-verification

Ordinary bugs use Bug report; vulnerabilities never use ordinary public issues. If PVR is unavailable/denied or an internal contact is missing, use an existing visible maintainer contact only to ask for confidential instructions without vulnerability details. Keep the report private until an appropriate route exists. A changed, failed or withdrawn route invalidates its active claim and requires bounded re-verification.

Configuration, permission changes, messages and publication require their own authorization. The owner's explicit operational authorization covered this pilot and the subsequent test cleanup; it does not authorize merge, license application, wider deployment or publication of advisories. Closing synthetic reports after CI succeeds preserves their receipt evidence.

Prepared EN/PT/ES policies and native English form accept reports in all three languages. Repository-specific policies/forms take precedence; organization defaults do not enable PVR. Platform, Workspace, Discover and CRM retain separate adoption evidence.
