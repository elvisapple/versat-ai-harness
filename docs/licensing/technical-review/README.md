# H01 technical provenance and notices review

Reviewed 2026-11-10. Scope: the selected private Harness source at 597b81c71a0fc0908ff5264fe9987bb5c0d8feec, the current H01/H02 documentary additions, and the installed validation dependencies. This is not H03 export clearance, a binary distribution audit or remote channel verification.

## First-party evidence

The non-shallow Git history contains 46 commits and only the author names Elvis Zoz and elviszoz. Initial bootstrap 762e654 introduced 98 files. The baseline inventory contains 1,040 files, all UTF-8 text, including 850 under docs (many retained validation fixtures/evidence). No binary assets, fonts, vendor/node_modules/site-packages tree or LICENSE/NOTICE path was found in that baseline. Copyright/provenance-marker searches and package/import review found no separately identified copied third-party source implementation. Absence of markers is not proof of originality.

The actual owner, previously identified as the company approver, was therefore asked specifically about creation for Versat E.A.S., authority to license and unidentified copied material. His reply in this chat was:

> Sim, tudo foi produzido por mim para a Versat E.A.S.

This is the owner attestation supporting first-party provenance for the Harness bootstrap, templates/documentation and organization documents. It is combined with the source inventory, not replaced by Git authorship. No unseen contract, signature or independent legal opinion is asserted. No contradictory third-party origin was identified in this bounded review. New H01/H02 files were drafted in this authorized chat from owner decisions; organization snapshots retain their observed Git blob identities.

`baseline-files.csv` records every baseline path, blob, SHA-256, size, mode and root. `inventory.json` records the dependency closure, actual versions, dependency markers and exact installed license-file hashes. License texts are copied verbatim to `dependency-license-texts/` solely as private review evidence, not as an effective license for Versat material.

## Dependency boundary

The root source references PyYAML==6.0.2 and jsonschema==4.23.0 in requirements-validation.txt. CI installs them into its environment with pip; validators import yaml/jsonschema. No copies of those packages or the interpreter occur in the 1,040 tracked source files. Resolving their active requirements under the observed Python 3.11.4 environment, without extras, yields seven packages; this includes typing_extensions through referencing's python_version marker. Optional format extras and dependencies applicable only to Python <3.9 are not installed by the reviewed manifest.

Six installed packages carry MIT permission texts: PyYAML, jsonschema, attrs, jsonschema-specifications, referencing and rpds-py. The typing_extensions license file contains the PSF licensing terms and historical notices, plus the documentation-code BSD-0-Clause section; preserve that full file if that package is distributed. Reviewed MIT texts require retention of the stated copyright and permission notice with copies/substantial portions. The review records these textual obligations, not a blanket opinion for every future combined distribution.

Current private source delivery does not bundle those runtime packages. H03 must inspect actual artifacts if it later bundles Python, native wheels, LibYAML, Rust dependencies or other payloads; that binary/transitive notice review belongs to the selected distribution and cannot be inferred from this source inventory. CI actions/checkout@v4 and setup-python@v5 are external execution references, not vendored source in this tree. Their action runtime artifacts are likewise outside this candidate package.

Only the two direct dependencies are pinned here. Installed transitive versions are observations, not a lockfile or release promise. Issue 31 retains dependency-management/reproducibility work; no requirements, locks or release refs changed.

## Result and retained limits

The owner has approved the exact H01 terms and attested first-party provenance. The bounded source review found no unresolved author-input gap. Candidate notices identify actual external dependencies, their license evidence and conditional distribution obligations. H02 can consume the approved terms and notices with their private access/effectiveness limits.

Publication, full export/history/attachments clearance, effective license application, H03 packaging and per-product adoption remain separate authorized work. No current document grants rights to third-party material under the proprietary terms. No new legal clause was added to the approved candidate.
