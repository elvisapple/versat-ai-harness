# H02 authorized route verification — 2026-11-11

The owner authorized PVR enablement in versat-labs/.github, synthetic PVR and internal Harness email tests, completion of H02/CI, and later closure of both private tests. No merge, effective license or public advisory is authorized. The owner separately requested notification configuration and confirmed “Notificação recebida.”

## Public repository pilot

PVR was enabled with explicit authorization; authenticated GET confirmed enabled. Reporter oscarcareaga89 submitted marker H02-20261110-PVR-01 in two clearly synthetic reports, GHSA-435c-c8r3-9mw8 (2026-11-11T11:39:42Z) and GHSA-73mc-fm4x-p58f (2026-11-11T12:00:31Z). Authenticated reads verified their author, full marker, synthetic/no-impact description, triage state, null published_at and null cve_id. Repository permission API returned read/read for the reporter, independently establishing non-administrator submission.

Elvis confirmed viewing the report; the authenticated administrator API independently returned both reports. Anonymous, credential-free GET of the second advisory API URL returned HTTP 404. Existing repository administrators Elvis and Everton and no organization security-manager teams were observed; no roles were added. Advisory collaborating_users lists the reporter and collaborating_teams is empty. This supports the permitted repository-security boundary, not a claim to enumerate or test every organization owner/account.

Repository Watch / Custom / Security alerts was saved and verified by reopening the UI. Watching Email and on-GitHub delivery were already enabled. Gmail independently returned the matching subscribed notification in INBOX, message 1a1ca7b7e8a4def1 at 2026-11-11T12:00:53Z; collaborator notification 1a1ca7b7d8005b54 also arrived. The matching GitHub inbox notification was marked Done at the owner's request, preserving other notifications and both reports. Receipt remains evidence after cleanup.

## Private Harness route

The authorized internal test, H02-20261110-INTERNAL-01, was sent on 2026-11-10T21:44:10Z to Elvis with Everton copied, using actual directory contacts. Gmail thread/message 1a1c76b2731e70ac independently contains the expected marker, intended To/Cc and INBOX/SENT/UNREAD labels. Elvis is the accountable owner and current default CODEOWNER. Receipt is established in Elvis's mailbox. Sender and one recipient are the same; Everton's receipt/acknowledgment is not asserted. No BCC, attachment, real exploit or sensitive payload was included. Recipient headers and authenticated mailbox access were observed; delegation/forwarding/domain-admin configuration was not audited. Exact email addresses remain in internal services, outside the public payload.

## Recovery and limits

The earlier administrator PVR submission returned 403 and created nothing. For denied/missing PVR, missing internal contact or an unavailable replacement, all locales direct a non-sensitive request for private routing; no vulnerability details go into Bug report or any public issue. Public reporter submission is established by the actual read-only reporter, not by administrator access. No SLA, retention term or acknowledgment by every CODEOWNER is inferred.

The pilot verifies .github PVR and the Harness owner's internal receipt. Other repositories need their own adoption/configuration checks. The seven-file custom template remains in unmerged .github PR #4; native default-form receipt does not prove candidate rendering or inheritance. The tests will be closed only after remote CI succeeds; no publication/CVE is requested.
