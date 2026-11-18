# Coding and Changelog Standard

Use the applicable technology Standards for mechanical checks. Authors and
reviewers MUST assess the following practices where they affect the change.

| Practice | Review question |
| --- | --- |
| Readability | Do names communicate intent and units, and does control flow make the usual and error paths clear? |
| Single responsibility | If persistence and business policy change for different reasons, can each change and be tested independently? |
| Open/closed | Where variation already exists, can a new case extend the documented boundary without editing unrelated behavior? Prefer the simplest design that supports known needs. |
| Liskov substitution | Can callers substitute an implementation without losing guarantees about inputs, results or errors? |
| Interface segregation | Can each caller depend on the operations it uses without implementing unrelated ones? |
| Dependency inversion | Can business rules depend on a narrow contract for external I/O so they can run independently of the concrete adapter? |

Lint and formatting validate configured objective conventions. Reviewer judgment
is required for clarity, responsibility boundaries, substitutability and the
accuracy of release notes.

## Changelog

Add a new, nonblank entry under `## [Unreleased]` in root `CHANGELOG.md` for a
notable change. Describe the impact for users or maintainers. Keep previous
release entries in place. Runtime, policy, compatibility, public guidance,
workflow and template changes require an entry. Treat unknown paths as in scope.

A change limited to the changelog itself, SDD dossiers, maintained test assets,
or internal validation records is exempt. The exemption covers paths under
`specs/changes/`, `specs/archive/`, `tests/` and `docs/validation/`, where these
edits document or test behavior without changing the shipped contract. A mixed
change requires an entry if any affected path is in scope. Review both sides
of a rename and the effects of any deletion. A reviewer MUST ask for an entry
when the effect is notable despite an automated path exemption. Changes to
these rules or their enforcement require governed PR review.
