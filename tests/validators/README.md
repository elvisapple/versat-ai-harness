# Validator tests

Each validator requires passing, failing and indeterminate fixtures with stable machine-readable results.

Run the complete deterministic suite with Python 3.11+ and the pinned validation dependencies:

```sh
python -m unittest discover -s tests/validators -p 'test_*.py'
```

`test_sdd.py` retains v2 gate/evidence cases under explicit synthetic compatibility. `test_sdd_v3.py` covers scenario mappings, snapshots, impact, findings, compatibility and local Git-baseline selection. Fixtures use synthetic approvals, not human review evidence.

The separate reviewer walkthrough actually executes synthetic payment assertions and records observations and corrections:

```sh
python tests/validators/review_sdd_walkthrough.py --output /tmp/sdd-review.json
```

Its behavioral replay also runs in the unit suite. It remains separate from an autonomous-agent evaluation: the reviewer follows and assesses workflow boundaries, while local checks exercise behavior and records. No network or real payment system is used. See the [recorded evidence](../../docs/validation/sdd-acceptance-regression/reviewer-walkthrough.md).
