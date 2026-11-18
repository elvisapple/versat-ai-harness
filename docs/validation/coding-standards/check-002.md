# CHECK-002 — Git and Unreleased changelog cases

Outcome: pass. Ran
`python -m unittest discover -s tests/validators -p test_quality.py -v`
from the prepared validation environment. All 11 tests passed with real Git
history and pinned Ruff in disposable repositories.

The check required a new entry for source and mixed changes. Duplicates,
entries moved from history, edits limited to historical sections, fenced
examples, ambiguous Unreleased headings and missing required notes failed.
A fresh changelog with an entry passed when no changelog existed at the base.
An empty diff and SDD planning-only paths were exempt. Moving a file from source
to an exempt directory still required a note, and deleted Python files were not
passed to Ruff. Missing Git history and symlink inputs produced diagnostics.

The same suite also exercised actual lint and formatting diagnostics, missing
Ruff, branch creation, an initial default-branch root commit, branch updates and
a synthetic two-parent PR merge revision.
