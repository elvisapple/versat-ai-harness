# Harness/plugin notices — reviewed private source candidate

State: documentary notices candidate reviewed on 2026-11-10; not applied as a distribution notice. Terms approval: [H01 record](../governance/h01-approval.md). Source baseline: `597b81c71a0fc0908ff5264fe9987bb5c0d8feec`.

Versat E.A.S. is the owner-declared holder of the first-party Harness/plugin material. Elvis Luis Zoz confirmed that the Harness bootstrap, templates/documentation and organization documents were produced by him for the company. The [technical review](technical-review/README.md) records the actual quote, 46-commit/1,040-file inventory and limits. No copyright year, contract or signature has been fabricated.

## External validation dependencies

These packages are installed separately by the validation environment, not vendored in the reviewed tracked source. Versions below are the actual Python 3.11.4 environment observations; only PyYAML and jsonschema are pinned by requirements-validation.txt. Optional extras are excluded.

| Package | Observed version | Inspected license text | Evidence |
|---|---|---|---|
| attrs | 26.1.0 | MIT | [Exact inspected text](technical-review/dependency-license-texts/attrs-26.1.0-LICENSE.txt) |
| jsonschema | 4.23.0 | MIT | [Exact inspected text](technical-review/dependency-license-texts/jsonschema-4.23.0-COPYING.txt) |
| jsonschema-specifications | 2025.9.1 | MIT | [Exact inspected text](technical-review/dependency-license-texts/jsonschema-specifications-2025.9.1-COPYING.txt) |
| PyYAML | 6.0.2 | MIT | [Exact inspected text](technical-review/dependency-license-texts/PyYAML-6.0.2-LICENSE.txt) |
| referencing | 0.37.0 | MIT | [Exact inspected text](technical-review/dependency-license-texts/referencing-0.37.0-COPYING.txt) |
| rpds-py | 2026.9.1 | MIT | [Exact inspected text](technical-review/dependency-license-texts/rpds-py-2026.9.1-LICENSE.txt) |
| typing_extensions | 4.16.0 | PSF terms and notices; see full file | [Exact inspected text](technical-review/dependency-license-texts/typing_extensions-4.16.0-LICENSE.txt) |

Preserve the applicable upstream license/copyright texts when distributing copies of those dependencies. The proprietary Harness terms do not replace their licenses. The evidence copies here are source records for review, not a declaration that these packages are bundled or an application of a license to Versat code.

## Other reviewed surfaces

- Root policies, Skills, SDD, templates, validators, schemas and documentation: inventoried; owner provenance attestation recorded. No unaccounted third-party asset or source implementation identified by the bounded review.
- `.github` source snapshots: 13 baseline files with exact Git blob and SHA-256 identities in the H02 manifest; same owner's provenance confirmation. Candidate changes are separately listed.
- CI actions: actions/checkout@v4 and actions/setup-python@v5 are remote build references, not vendored files. No action code is included in the H02 patch/package.
- Future artifact: if H03 distributes an interpreter, native extension/wheel, copied component or different version, inspect that actual artifact's complete notices and dependencies before distribution. Current source review is not binary/export clearance.

No root LICENSE or NOTICE was applied. Public export, releases and installed consumers remain unchanged. Dependency-management work remains issue 31; per-product adoption remains P01/P03.
