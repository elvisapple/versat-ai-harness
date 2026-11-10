# H02 operational verification attempt — 2026-11-10

Status: in progress; not an acceptance pass. Source PR heads: Harness `abde65cc25346108b32edb883f6ae5a0ca413503`; organization `97d7f4c1ceb76ea42cc37250fc47bdecec7a677b`. Both remain draft and unmerged.

## Authority and scope

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
- A non-administrator reporter observation has been requested from the owner using the private reporting flow and marker `H02-20261110-PVR-01`. No test report has yet been observed. Administrator access alone is not substituted for intended-reporter access.
- The custom organization form remains in unmerged PR #4. Enabling PVR does not deploy that candidate or prove its rendered inheritance.

## Observed Harness internal email

- Corporate sender and recipient identities were resolved from the connected Gmail profile and Google Contacts directory, not guessed from usernames. Exact internal addresses remain in those restricted services rather than this package.
- A single HTML test email was sent at `2026-11-10T21:44:10Z`, with marker `H02-20261110-INTERNAL-01`, to Elvis and cc Everton. Both are CODEOWNERS for the governed components under test. No BCC, attachments, exploit, customer data or credentials were included.
- Gmail message/thread ID: `1a1c76b2731e70ac`. An independent inbox search and subsequent thread read observed the actual marker, intended To/Cc headers and `INBOX`, `SENT`, `UNREAD` labels in Elvis's connected mailbox.
- The sender is also one recipient. This proves mailbox presence in that account; it does not establish delivery to Everton or test a separate sender identity. Everton's receipt/acknowledgment has not yet been observed.
- The message requested acknowledgment in the same internal thread. No follow-up or unrelated message was sent.
- The observed message has only the intended recipients. Mailbox delegation, forwarding rules and domain-admin access have not been inspected; confidentiality beyond those observations is not asserted.

## Remaining evidence and current disposition

Obtain a real private PVR report from the intended non-administrator audience, verify its reception and permitted visibility, and inspect actual notification evidence. Complete the internal-route receipt/access observations within available authorized access. Exercise and record denied/unavailable-channel recovery. Then update current source status, capture fresh check input snapshots and rerun affected checks before assigning passes.

TASK-004 and CHECK-003 remain incomplete. No other result is relabeled from this partial attempt. The known CI failure remains until genuine acceptance evidence and the corresponding H01/H02 checks are completed. No merge, effective terms, consumer update or public advisory publication occurred.
