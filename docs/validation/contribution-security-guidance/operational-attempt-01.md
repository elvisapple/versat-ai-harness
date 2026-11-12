# H02 operational verification attempt — 2026-11-10

Historical sequence: earlier pending statements below describe their observation time. Final bounded receipt/access evidence is recorded in final-20261111/operational.md; it supersedes the pending state without deleting failed attempts. Initial source PR heads: Harness `abde65cc25346108b32edb883f6ae5a0ca413503`; organization `97d7f4c1ceb76ea42cc37250fc47bdecec7a677b`. Initial partial evidence was published in Harness commit `2a91262d310ee4822fb475b9bfd78a81699210ad`. The observations below dated 2026-11-10 preserve the earlier blocked attempt.

## Follow-up evidence — 2026-11-11

Subsequent successful notification observation supersedes the earlier email-delivery gap: the owner confirmed "Notificação recebida." An independent Gmail search found the notification for the second synthetic report `GHSA-73mc-fm4x-p58f`, authored by `oscarcareaga89`, created at `2026-11-11T12:00:31Z`. The subscribed notification arrived at `2026-11-11T12:00:53Z` from GitHub, Gmail message `1a1ca7b7e8a4def1`, present in INBOX. A related collaborator event notification is message `1a1ca7b7d8005b54`. The GitHub notification inbox also displayed the matching report with reason `subscribed`.

Authenticated API inspection found two reports with the exact H02 test title and marker: `GHSA-435c-c8r3-9mw8` and `GHSA-73mc-fm4x-p58f`, both in triage, with null publication timestamps and CVE IDs. Both descriptions explicitly identify non-sensitive synthetic tests. The owner requested cleanup; clarification distinguishes marking notifications Done from closing the private test reports. The single matching H02 inbox notification was selected and marked Done in GitHub; the refreshed UI showed it removed while unrelated notifications remained. Neither advisory was closed or deleted. A request to clarify whether the reports should also be closed remains pending. Original report receipt, notification configuration and observed email delivery remain evidence even after notification cleanup.

The owner reported: "Pude visualizar o teste enviado pelo usuário oscarcareaga89. Porém não recebi notificação por e-mail. Como configurar?"

An authenticated repository-advisory API read independently returned `GHSA-435c-c8r3-9mw8`, author `oscarcareaga89`, title `TESTE AUTORIZADO H02 — sem vulnerabilidade real`, created at `2026-11-11T11:39:42Z`, state `triage`, with null `published_at` and `cve_id`. Private URL: https://github.com/versat-labs/.github/security/advisories/GHSA-435c-c8r3-9mw8. This resolves the absence of a submitted test report and records actual maintainer visibility. Reporter permissions, full marker/content and anonymous denial still require bounded inspection before a complete access claim. No public advisory or CVE is recorded.

The owner has not received an email notification. Official GitHub configuration documentation checked on 2026-11-11 requires a repository subscription to All Activity or Custom / Security alerts, plus account Settings / Notifications / Subscriptions / Watching / Notify me / Email. Guidance was prepared for the owner; no preference was changed by this read. Email receipt remains unverified and must not be inferred from browser visibility.

## Authority and scope

### Notification configuration observed on 2026-11-11

The owner explicitly asked the agent to configure the notification. In the authenticated GitHub browser session for `elviszoz`, the repository subscription initially showed Participating and @mentions. The agent selected Custom, checked only Security alerts and applied it. After navigating away and reopening the repository subscription dialog, Security alerts remained checked; Issues, Pull requests, Releases and Discussions were unchecked. This verifies saved subscription state for `versat-labs/.github`.

Account notification settings already had Email and on-GitHub delivery enabled for both Watching and Participating/@mentions/custom. The default notification destination was the owner's existing corporate `versat.ag` address, and Custom Routing showed no organization overrides. No email address, account-wide delivery option, credential, role, PVR setting or repository content was changed by this browser operation. Actual receipt of a new notification email remains unverified; saved configuration does not retrospectively prove delivery of the original report notification.

Actual owner instruction in this chat:

> Autorizo habilitar o PVR no .github, se necessário, e realizar os testes de relato privado e email interno do Harness. Avance até concluir H02 e deixar o CI verde, sem merge nem aplicação de licenças.

The authorization covers PVR enablement in `versat-labs/.github` and non-sensitive test submissions for that public repository and the private Harness internal-email route. It does not authorize repository merges, license application, public advisory publication, CVE requests, new accounts, or broader role grants.

## Observed PVR configuration

- Authenticated GitHub executor: `elviszoz`, existing administrator. Only this GitHub account is available in the CLI session.
- `GET /repos/versat-labs/.github/private-vulnerability-reporting` initially returned `enabled: false`.
- Authorized `PUT` to that exact endpoint succeeded; a subsequent `GET` returned `enabled: true`.
- Repository collaborators observed: `elviszoz` and `evertonspohrversat` have admin access; `PabloSalinasV` and `rafaelalmeida-versat` have read access. No membership or role was changed.
- `GET /orgs/versat-labs/security-managers` returned an empty list. This records the API observation, not a claim that organization-owner rights cease to apply.
- Reading the authenticated account's repository subscription returned HTTP 404 with an explicit missing `notifications` OAuth scope diagnostic. Notification preferences are unverified; no token scope or subscription was changed.
- The owner answered the reporter-availability question: "Não tenho uma conta ou pessoa disponível para esse teste". No non-administrator reporter is available. Administrator access alone is not substituted for intended-reporter access.
- A single authorized real submission attempt was subsequently made as `elviszoz` through `POST /repos/versat-labs/.github/security-advisories/reports`, with the clearly synthetic title `TESTE AUTORIZADO H02 — sem vulnerabilidade real`, marker `H02-20261110-PVR-01`, no affected packages or CWE, and no CVE request.
- GitHub returned HTTP 403: `You are not authorized to report advisories in this repository via private vulnerability reporting`. No success or receipt is claimed. A subsequent repository-advisory listing found no H02 test advisory. The agent did not substitute direct maintainer advisory creation, create an account or change roles.
- The custom organization form remains in unmerged PR #4. Enabling PVR does not deploy that candidate or prove its rendered inheritance.

## Observed Harness internal email

- Corporate sender and recipient identities were resolved from the connected Gmail profile and Google Contacts directory, not guessed from usernames. Exact internal addresses remain in those restricted services rather than this package.
- A single HTML test email was sent at `2026-11-10T21:44:10Z`, with marker `H02-20261110-INTERNAL-01`, to Elvis and cc Everton. Both are CODEOWNERS for the governed components under test. No BCC, attachments, exploit, customer data or credentials were included.
- Gmail message/thread ID: `1a1c76b2731e70ac`. An independent inbox search and subsequent thread read observed the actual marker, intended To/Cc headers and `INBOX`, `SENT`, `UNREAD` labels in Elvis's connected mailbox.
- The sender is also one recipient. This proves mailbox presence in that account; it does not establish delivery to Everton or test a separate sender identity. Everton's receipt/acknowledgment has not yet been observed.
- The message requested acknowledgment in the same internal thread. No follow-up or unrelated message was sent.
- The observed message has only the intended recipients. Mailbox delegation, forwarding rules and domain-admin access have not been inspected; confidentiality beyond those observations is not asserted.

## Remaining evidence and current disposition

Obtain an authorized available reporter account capable of using PVR, then verify actual reception, permitted visibility and notification evidence. The owner currently has no such account/person. Complete the internal-route receipt/access observations within available authorized access. The actual 403 establishes denied-submission behavior only; the safe fallback is to keep details private and request appropriate private routing, not post them to an ordinary issue. Then update current source status, capture fresh check input snapshots and rerun affected checks before assigning passes.

TASK-004 and CHECK-003 remain incomplete. No other result is relabeled from this partial attempt. The known CI failure remains until genuine acceptance evidence and the corresponding H01/H02 checks are completed. No merge, effective terms, consumer update or public advisory publication occurred.
