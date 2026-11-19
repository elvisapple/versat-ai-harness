# CHECK-003 — Changelog meaning and exemption review

Outcome: pass. Reviewed the Standard and guide against two PR cases. A change to
API behavior under `src/` needs an Unreleased note that describes the change to
callers. For example, a note saying the endpoint now rejects an empty identifier
describes the externally visible result. A note saying only “update API” would
not describe that impact. A change confined to an SDD proposal is exempt
because the planning edits document intent without altering shipped behavior.
The PR checklist asks for the impact or the reason for exemption.

Reviewed the actual new Unreleased entry. It identifies the index-resolved
policy and the addition of pinned lint, formatting and Git-based changelog
checks in both the Harness and the Python reference. Compared the candidate and
historical release content against `origin/main`; those sections matched byte
for byte.
