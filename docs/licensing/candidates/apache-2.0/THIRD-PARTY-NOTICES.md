# Third-party notices candidate — R1

This is a proposed source-distribution notice, not effective adoption. The Apache candidate does not relicense third-party content. The seven full upstream license texts remain in [the existing evidence directory](../../technical-review/dependency-license-texts/); retain their original wording and copyright notices. They are included text records; the corresponding installed packages, Python interpreter and binary wheels are not bundled in the inspected source tree.

| Separately installed dependency | Observed version, 2026-11-13 | Retained terms |
|---|---|---|
| PyYAML | 6.0.2 | MIT, `PyYAML-6.0.2-LICENSE.txt` |
| jsonschema | 4.23.0 | MIT, `jsonschema-4.23.0-COPYING.txt` |
| attrs | 26.1.0 | MIT, `attrs-26.1.0-LICENSE.txt` |
| jsonschema-specifications | 2025.9.1 | MIT, `jsonschema-specifications-2025.9.1-COPYING.txt` |
| referencing | 0.37.0 | MIT, `referencing-0.37.0-COPYING.txt` |
| rpds-py | 2026.9.1 | MIT, `rpds-py-2026.9.1-LICENSE.txt` |
| typing_extensions | 4.16.0 | Full PSF terms, historical notices and documentation-code BSD-0-Clause section, `typing_extensions-4.16.0-LICENSE.txt` |

Only PyYAML and jsonschema are directly pinned by `requirements-validation.txt`; the other versions describe the observed validation environment, not a new dependency lock. Preserve applicable upstream notices when distributing copies or substantial portions. A future distribution that bundles an interpreter, native libraries, wheels, action code, assets or other dependencies needs review of that actual distribution before clearance. CI references to actions/checkout and actions/setup-python do not mean their code is vendored here.

The source contains retained historical snapshots and quoted material. Owner provenance evidence is bounded, and third-party exceptions and confidentiality review remain necessary for those records. Unknown provenance is deferred, not converted to Apache permission by this inventory. No additional attribution, copyright year or contributor grant is invented.
