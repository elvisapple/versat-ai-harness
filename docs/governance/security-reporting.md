# H02 security-reporting record

Private, non-sensitive implementation record · Observed 2026-11-10.
Accountable contact: Elvis Luis Zoz (@elviszoz), as appointed by the user.

## Current state

**Owner-selected routing on 2026-11-10:** public repositories use GitHub Private Vulnerability Reporting; private repositories email the relevant CODEOWNERS using existing internal Versat channels. This supersedes the earlier tentative selection of info@versat.ag. Do not advertise that address as the selected route.

The user's instruction: "Então vamos adotar essa solução para os repositórios públicos, criando um template no repositório .github. Para os repositórios privados mantemos instrução para enviar email aos codeowners pelos canais internos da Versat."

This is the concrete route decision anticipated by H02 TASK-001/002/004/005, within the approved common-guidance/candidate approach. Existing issue forms and their fields/types/project associations remain unchanged. No new service, public central intake repository, CLA or runtime is introduced; the approved planning scope/digests remain unchanged.

| Required input/evidence | Current status |
|---|---|
| Public route | GitHub PVR on the affected public repository; default native form prepared at candidate/.github/VULNERABILITY_REPORT.yml. No automatic enabling or verified reception claimed. |
| Private route | Relevant CODEOWNERS via internal Versat email contacts. No addresses guessed or copied into the public candidate. Monitoring/triage responsibility is assigned to those CODEOWNERS; actual contact availability remains an operational observation. |
| Reporter access | Public GitHub reporting audience subject to enabled feature; private reporters need an existing internal contact route. Missing contact/owner uses non-sensitive routing request. |
| Responsibility and operational configuration | The relevant CODEOWNERS own monitoring, triage and remediation coordination for both routes. This responsibility is settled. Actual GitHub permissions/subscriptions, internal access and receipt remain unverified operational facts. |
| Minimization, retention and response commitment | Minimize sensitive data; no retention period or SLA invented. |
| Synthetic submission, receipt and access observations | Not authorized or performed in this documentary phase. |
| Live configuration, activation or publication | None performed; previous private-documentary boundary retained. |

Prepared SECURITY EN/PT/ES and localized contribution/reporting instructions. Native form text is canonical English and accepts reports in EN/PT/ES. Its destination is the private security workflow, not .github/ISSUE_TEMPLATE or a Bug report issue. Repository-specific forms/policies take precedence; template inheritance does not enable PVR.

Sources checked 2026-11-10: [GitHub PVR configuration and organization-default form](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository), [default community health files and precedence](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file). These verify documented platform capability, not live Versat configuration.

## State and publication behavior

- **Unselected/unverified:** guides state that no route has been verified here. Use only an existing repository/maintainer contact to request private instructions without vulnerability details.
- **Selected, unverified:** record the actual route privately; do not advertise it as verified or submit a test without explicit scoped authorization.
- **Verified:** only after authorized configuration/access observations and safe synthetic receipt evidence. Record the exact scope, performer, authorization, time/environment, destination version and safe evidence reference.
- **Changed/failed/withdrawn:** remove the active claim, restore safe fallback and rerun affected verification under appropriate authority.

Fallback is safe failure behavior, not full H02 acceptance. Never place exploit details, credentials or customer data in a public issue. Do not infer public reporter access from an authenticated administrator request. Missing intended-user observations remain unverified.

## Future bounded verification

After a concrete route and explicit test authorization exist, an authorized performer sends only a non-sensitive unique marker. Observe receipt by the intended responder and permitted access/configuration evidence. Do not include real vulnerabilities or secrets. Record limits and inaccessible observations honestly; environment changes invalidate affected evidence even if local document hashes match.

This procedure is not permission to configure a route or send a marker now. Additional access/configuration changes require their own scope. The public organization candidate and each product's adoption remain separate and pending.

## Responsibility clarification — 2026-11-10

The user clarified that reporting to CODEOWNERS includes their duty to monitor the reports. No additional appointment or confirmation of that duty is needed. The agent had incorrectly presented responsibility as undecided; this record corrects it. Only actual delivery/access/receipt remains to be checked under future operational authorization.

Read-only observation during final documentary review: organization .github at a762582c6585ae967c37f7f7f1c69c06c07e9071 contains `.github/CODEOWNERS` with `* @elviszoz`. This confirms the target repository owner and is preserved unchanged. It does not establish live PVR permissions, subscriptions or receipt.
