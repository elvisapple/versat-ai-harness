# CHECK-005 — Python consumer adoption and rollback

Outcome: pass. Ran
`python -m unittest discover -s tests/execution -p test_consumer.py -v`.
All six tests passed. The walkthrough composed the base with the optional Python
validation assets and used a clean synthetic provider at its actual exact
commit, with index-resolved Standard digests. The package was prepared with the
pinned dependencies. The exact wrapper and the documented base argument
reported a passing full run when a changed Python file and new note complied.

A run missing the required note failed overall and still ran the existing
customized test command successfully. A seeded behavior regression failed the
required suite with passing quality checks. The targeted run explicitly
reported its limited scope. The unresolved provider pin case failed provider
verification. A synthetic push event exercised the same wrapper with the
GitHub event input and produced full suite output after selecting the prior
commit.

The existing validation configuration survived adoption, including the custom
test pattern. Restoring the previous wrapper and running its original suite
succeeded. The guide also instructs adopters to retain and restore the provider
pin, CI and both configurations together if those files change. Its
supervised Skill evaluation reference remains separate from execution of the
deterministic suites. This walkthrough used local synthetic repositories.
