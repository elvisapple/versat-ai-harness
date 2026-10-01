# SDD validation

Run from the selected Harness checkout with Python 3.11+ and `requirements-validation.txt` installed in a virtual environment. Target consumer records with `--root`; schemas come from this version-matched Harness package.

```sh
python validators/sdd/validate.py --root /path/to/project --json
python validators/sdd/validate.py --root /path/to/project --change home-greeting --phase implementation
python validators/sdd/validate.py --root /path/to/project --change home-greeting --phase delivery --json
python validators/sdd/validate.py --root /path/to/project --change home-greeting --digest tasks
python validators/sdd/validate.py --root /path/to/project --change home-greeting --input-digest CHECK-001
python validators/sdd/validate.py --root /path/to/project --change prevent-duplicates --source-digest
python validators/sdd/validate.py --root /path/to/project --baseline trusted-base --json
./scripts/validate/run.sh --baseline trusted-base --require-archive
```

The package script accepts the optional baseline pair and `--require-archive`, validates this Harness checkout and runs the full validator suite. It never narrows profile-required suites. In CI, trusted-base comes from event metadata, with full history available; a missing ref fails explicitly.

Planning allows absent later-stage artifacts. Implementation requires the current three approvals and no blockers. Delivery also requires completed tasks, passing required checks and v3 scenario/regression assessments. Draft v3 plans receive coverage and input-scope checks; results are required at delivery. Default archive inventory checks stored records without comparing obsolete inputs. Explicit delivery and baseline-selected changed archives use live freshness. Inventory without a baseline does not certify all changed archives.

Exit codes: pass/0, fail/1, unable-to-verify/2. JSON includes findings with codes/paths/severity, warnings, checked IDs, v3 metrics and selected live archives. Digest helpers print a digest or fail; they do not approve or execute anything. The input helper requires an approved structurally valid v3 plan, while stale execution evidence can be replaced only by actually rerunning checks. Source digest binds Requirements from any supported version.

See [metadata](../../sdd/metadata.md) for exact fields, snapshots, compatibility and limits, and the [guide](../../sdd/README.md) for correction and usage examples. Unknown/mixed/unlisted older records fail; bounded v2 and pre-v2 exemptions carry explicit warnings. Schema/hash consistency does not prove semantic completeness, trustworthy execution, approver identity, remote CI, merge or deployment. Agents/reviewers must assess behavior and actual execution independently.

Before creating a PR for completed work or marking its draft ready:

```sh
python validators/sdd/validate.py --root /path/to/project --change home-greeting --phase delivery --require-archive
```

Unlike plain delivery (which checks prerequisites before the move), this guard requires archive storage and `closure: prepared` as well as live delivery readiness. It works without Git for an explicitly selected change. With a baseline, it includes changed active dossiers, so they cannot bypass the guard by never entering archive storage. Empty selection and removed dossiers fail. A selected change plus baseline checks their union. Non-draft PR CI and pushes to main use this flag; draft PRs may carry planning work. The job must remain required by the repository platform to block merge. The local preflight is the check before publication; CI is a separate check after the event.
