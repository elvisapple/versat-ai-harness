# Quickstart and scenario coverage validation

This is evidence for the approved change, not a reusable report template or a consumer guide.

- Observed UTC time: 2026-09-29T15:05:06.328279+00:00
- Base commit: `0b0471f7b0fcaa0e4784892197439f8c61ffba48`
- Tested source snapshot: `671e90e76e44aced6859b8f5a8abd20b244b6ae016ea3aedcb4fa07ab3cfa406`
- Approved Tasks plan digest: `aa7006716772e96fa2f356a714418c03af7f3d9adcca09998bbf3eee6f14ce67`

The snapshot is SHA-256 of Python `json.dumps(files, sort_keys=True).encode()` for the source file/hash mapping below. It covers the nine implementation files, not this evidence file or SDD bookkeeping. No merge, remote CI or consumer adoption is claimed.

## CHECK-001 — First-use decisions and illustrative layouts: pass

Manual application of the revised Documentation Standard and base authoring guidance:

| Case | Observed review outcome |
|---|---|
| Usable CLI with no guide | The default guide includes audience, Python prerequisite, no-install preparation, a runnable synthetic CSV example and exact expected output. The temporary command produced the expected two CSV lines. |
| Graphical workflow | The temporary guide describes opening the workspace and choosing Export, with a CSV download as the observable outcome. UI steps are permitted; a shell command is not required. This is a guide-content review, not execution of a real UI. |
| Existing separate guide | A temporary README links to `help/start.md`; no second quickstart is created. |
| Existing README section | A section anchor points to first-use instructions without a second file. |
| Empty scaffold | The new base prompt is removed in the illustrative generated README. Each of the five composed profiles has no empty guide or guide directory and no broken first-use link. |
| Supporting guide and archive | The quickstart links to export detail, which links back to shared setup. Moving an illustrative dossier from changes to archive leaves README and guide links valid. |

A temporary Python check copied the actual base and profile modules, applied the illustrative authoring decisions and checked real link targets/anchors. It did not implement or test an automated bootstrap composer. Synthetic layout files were confined to a temporary directory and removed after the check.

```text
PASS: 45 local Markdown links/anchors in 9 changed source files
PASS: illustrative software empty scaffold reuses base; no guide or broken first-use link
PASS: illustrative agent empty scaffold reuses base; no guide or broken first-use link
PASS: illustrative hybrid empty scaffold reuses base; no guide or broken first-use link
PASS: illustrative library empty scaffold reuses base; no guide or broken first-use link
PASS: illustrative infrastructure empty scaffold reuses base; no guide or broken first-use link
PASS: illustrative CLI guide prerequisites and documented action yield the expected synthetic CSV output
PASS: guide and supporting-guide links survive illustrative dossier archival
PASS: existing README section anchor works without a duplicate guide
PASS: existing separate guide location is preserved
PASS: git diff --check
Source snapshot SHA-256: 671e90e76e44aced6859b8f5a8abd20b244b6ae016ea3aedcb4fa07ab3cfa406
```

## CHECK-002 — Documentation throughout SDD: pass

Reviewed the actual planning, implementation, validation and developer-guide edits against these cases:

| Change or limitation | Outcome of applying the revised instructions |
|---|---|
| Setup command changes | Include the affected existing instructions with the implementation task; execute the changed command and compare its output with the documented result. |
| UI action changes | Update the action and observable result; validate the affected UI steps manually or automatically as appropriate. No CLI-only requirement was introduced. |
| Internal-only refactor | No new usage guide or documentation task is required where documented usage is unaffected. |
| Later revision of a workflow | Update the same living guide, preserving its README entry point instead of making a guide per change. |
| Missing environment/access | The existing validation step records `unverified` with a reason; it does not infer success from metadata or a planned command. |
| Shared functional/documentation check | Reuse the existing check and its actual evidence when it covers the same action and outcome; no second result or separate documentation report is required. |

These are manual instruction walkthroughs, not fabricated consumer test runs. The guides describe implemented behavior; planning records future work without publishing that behavior as delivered. The existing evidence fields and gates remain sufficient.

## CHECK-003 — Relevant scenario coverage: pass

Applied the revised Testing Standard and SDD check-planning/validation instructions to a synthetic requirement accepting integer quantities from 1 through 100:

| Supplied scenario evidence | Review outcome |
|---|---|
| Only quantity 50 succeeds | Identify missing relevant invalid-input and boundary coverage even if this is a required passing check linked to the requirement. |
| Success and invalid input covered, boundaries absent | Keep boundary coverage explicit as a remaining gap; a structural SDD pass does not resolve it. |
| Adequate existing checks cover 0, 1, 50, 100 and 101 | Reuse those checks and observed results without a new test catalog, duplicate tests or new scenario identifiers. |
| All relevant checks are planned but some not executed | Report missing observed evidence; a named check does not establish a pass. |
| Low-risk change without these input constraints | Select meaningful behavior checks for that change; do not impose this illustrative case count, exhaustive enumeration or test-first development. |

The numerical examples are review inputs, not executed product tests or normative minimum case counts. The text supports these decisions without adding schema fields or a new validator. Existing regression and CI rules are preserved.

## CHECK-004 — Scope, composition and links: pass

- Exactly the nine approved implementation files changed. The change dossier and this evidence file are additional records, not new consumer artifacts.
- Forty-five local Markdown links/anchors in those files resolve. Temporary consumer README/guide links were also checked as described above.
- Software, agent, library and infrastructure still extend base; hybrid still composes base, software and agent. No profile content was copied to introduce first-use rules.
- `git diff --check` passed; new dossier/evidence files are reviewed separately for whitespace and links during final bookkeeping verification.
- SDD schemas/templates, validators, tests, profile modules/manifests, VERSION, the legacy exemption manifest and the baseline failing dossier are unchanged.
- Policy is defined in Standards; procedures and bootstrap reference it. No new gate, report type, quickstart template, mandatory directory, language/security exception or consumer pin update was introduced.
- The bootstrap Skill's preexisting duplicate workflow numbering is unchanged and outside this scope.

## CHECK-005 — Required repository checks: fail

The package structure check and all 48 existing validator tests passed. This change's implementation-phase SDD validation passed. The full required entry point exited 1 because the existing `bootstrap-product-context` dossier lacks v2 metadata and has legacy-shaped Design checks. This failure was present before this implementation and its files are unchanged. It is not hidden, exempted or repaired by this change.

TASK-005 cannot complete until the required package-wide validation genuinely passes. The other four tasks can complete because their edits and focused checks passed. No delivery readiness is claimed.

### package

Command: `PYTHON=<validation interpreter> ./scripts/validate/run.sh`

Exit status: `1`

```text
Portable Plugin package validation passed.
SDD validation: fail
SCHEMA: specs/changes/bootstrap-product-context/proposal.md: frontmatter: 'sdd_version' is a required property
SCHEMA: specs/changes/bootstrap-product-context/proposal.md: frontmatter: 'review' is a required property
SCHEMA: specs/changes/bootstrap-product-context/requirements.md: frontmatter: 'sdd_version' is a required property
SCHEMA: specs/changes/bootstrap-product-context/design.md: frontmatter: 'sdd_version' is a required property
SCHEMA: specs/changes/bootstrap-product-context/design.md: frontmatter: 'review' is a required property
SCHEMA: specs/changes/bootstrap-product-context/design.md: validation.0: 'Harness structural and Plugin validation' is not of type 'object'
SCHEMA: specs/changes/bootstrap-product-context/design.md: validation.1: 'Skill frontmatter validation' is not of type 'object'
SCHEMA: specs/changes/bootstrap-product-context/design.md: validation.2: 'Local Markdown link and whitespace checks' is not of type 'object'
SCHEMA: specs/changes/bootstrap-product-context/design.md: validation.3: 'Manual acceptance scenario review' is not of type 'object'
SCHEMA: specs/changes/bootstrap-product-context/tasks.md: frontmatter: 'sdd_version' is a required property
SCHEMA: specs/changes/bootstrap-product-context/tasks.md: frontmatter: 'review' is a required property
SCHEMA: specs/changes/bootstrap-product-context/tasks.md: frontmatter: 'validation' is a required property
SCHEMA: specs/changes/bootstrap-product-context/tasks.md: frontmatter: 'closure' is a required property
WARNING LEGACY_EXEMPT: specs/changes/agent-project-layout: Immutable legacy dossier: v2 approval and evidence gates were not verified
WARNING LEGACY_EXEMPT: specs/changes/align-language-standard: Immutable legacy dossier: v2 approval and evidence gates were not verified
WARNING LEGACY_EXEMPT: specs/changes/consolidate-sdd-workflow: Immutable legacy dossier: v2 approval and evidence gates were not verified
WARNING LEGACY_EXEMPT: specs/changes/root-plugin-package: Immutable legacy dossier: v2 approval and evidence gates were not verified
WARNING LEGACY_EXEMPT: specs/changes/shortcut-git-convention: Immutable legacy dossier: v2 approval and evidence gates were not verified
................................................
----------------------------------------------------------------------
Ran 48 tests in 2.938s

OK
Validation failed with 1 error(s).
```

### implementation

Command: `python validators/sdd/validate.py --root . --change quickstart-scenario-coverage --phase implementation`

Exit status: `0`

```text
SDD validation: pass
```

## Source file manifest

```json
{
  "project-templates/README.md": "c5f81ad97150752b0ec23e346ffcbd0baa87a53bc19fae16ef4fe672cdef7c2b",
  "project-templates/base/README.md": "d037d87ba6c15a7df95701ba36320a353c2649bc08ec27b59244c3a37cfca3b6",
  "sdd/README.md": "cfa1bbd21fa4b79d133bfcec049e84e3760c71b3ca71603b1801fde4dd85c5db",
  "sdd/workflows/implement-change.md": "638bebcb324b5f24e9e12c24e63fa98d966ba5efb5eb728b2993b35abfe79925",
  "sdd/workflows/new-change.md": "1ca05e0db4fda5e1cf9fd7cf9eec569f8cb4a833907db5d855be9d9817cd46b4",
  "sdd/workflows/validate-change.md": "103cf7347c647a4615ce8886d26fae9eae6790288b3d03283492b2e2db5092af",
  "skills/project-bootstrap/references/project-lifecycle.md": "c77d870ebb80beac33b3d486d1d3bb7d2b828589a0fe7b7204bbb3ef98d2a84b",
  "standards/core/documentation.md": "f81e9a85570e4cd5699e113395e80bc92fba13401e57e8b7186bc6cd6bc785e0",
  "standards/core/testing.md": "74abaff040e350a7da6882d7992e9bc3ebea56735208c6a976bd903ad9f6bfd5"
}
```

## Final bookkeeping verification

Source hashes and all three approved planning digests are unchanged. Whitespace and local links in the four new dossier files and this evidence file were checked. After recording CHECK-005 as failed, implementation-phase validation correctly reports that failure too; the earlier pass above preceded result recording. Delivery assessment also rejects the blocked task. These results reflect the known package-wide failure, not stale approvals or malformed new metadata.

### Final implementation assessment

Exit status: `1`

```text
SDD validation: fail
VALIDATION_FAILED: specs/changes/quickstart-scenario-coverage/tasks.md: CHECK-005 has a recorded failure
```

### Final delivery assessment

Exit status: `1`

```text
SDD validation: fail
TASK_INCOMPLETE: specs/changes/quickstart-scenario-coverage/tasks.md: TASK-005 is not completed
VALIDATION_FAILED: specs/changes/quickstart-scenario-coverage/tasks.md: CHECK-005 has a recorded failure
```
