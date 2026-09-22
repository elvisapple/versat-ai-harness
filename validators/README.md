# Validators

Validation is the deterministic enforcement layer. Validators must emit machine-readable results in addition to concise human output and must distinguish pass, fail and unable-to-verify.

The released version 0.2.0 entry point validates repository structure and the portable root Plugin package. The unreleased consolidation also executes the [SDD validator](sdd/README.md) and its regression tests through `scripts/validate/run.sh`. Install `requirements-validation.txt` in a virtual environment first.

SDD checks validate local schemas, recorded approval freshness, traceability and documentary closure prerequisites. They do not authenticate approval records, run product acceptance tests automatically, or prove remote review, CI, merge or deployment. Exact legacy exceptions remain explicitly unverified for the new gates. Other domain and technology validators remain contracts for incremental implementation.
