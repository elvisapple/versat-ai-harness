# Historical SDD archive reconciliation

## Scope and authorization

On 2026-10-01, the repository owner identified all dossiers remaining in `specs/changes/` on `main` as already implemented history that belongs in `specs/archive/`. This maintenance corrects their storage after the SDD workflow transition. It does not resume implementation or retrospectively assert the three v2 planning approvals.

The baseline is local `main` commit `ac69894d94461f7e891dc817bd9ec81498978d0a` (`v0.3.0`), also the observed `origin/main` reference at inspection. Remote state was not refreshed and remote CI/review state was not queried.

## Observed merge evidence

The local first-parent history of `main` contains these merge commits. Each commit introduces the corresponding proposal, and each is an ancestor of the baseline. PR links are derived from the configured Git remote and observed merge subjects; their live platform state was not independently queried.

| Archived dossier | Observed merge commit | Pull request |
|---|---|---|
| [align-language-standard](../../specs/archive/align-language-standard/proposal.md) | `776b8235326fc892e75d06167e5b342672a1011d` | [#2](https://github.com/versat-private/versat-ai-harness/pull/2) |
| [root-plugin-package](../../specs/archive/root-plugin-package/proposal.md) | `85194bf7fb6c708de6a0f29acabb90eaaa1d055f` | [#3](https://github.com/versat-private/versat-ai-harness/pull/3) |
| [shortcut-git-convention](../../specs/archive/shortcut-git-convention/proposal.md) | `5a383f7e74b823f4cf972672216aa2ee4fcfd449` | [#4](https://github.com/versat-private/versat-ai-harness/pull/4) |
| [agent-project-layout](../../specs/archive/agent-project-layout/proposal.md) | `5e303dbd007977ec010e5863f35402ff305399d9` | [#5](https://github.com/versat-private/versat-ai-harness/pull/5) |
| [consolidate-sdd-workflow](../../specs/archive/consolidate-sdd-workflow/proposal.md) | `bd6d3b311da3d0b7e4d7828fdc19c21536ad4685` | [#6](https://github.com/versat-private/versat-ai-harness/pull/6) |
| [bootstrap-product-context](../../specs/archive/bootstrap-product-context/proposal.md) | `0b0471f7b0fcaa0e4784892197439f8c61ffba48` | [#7](https://github.com/versat-private/versat-ai-harness/pull/7) |

Reproduction commands, substituting a row's ID and merge commit:

```sh
git log --first-parent --diff-filter=A --format='%H %s' ac69894d94461f7e891dc817bd9ec81498978d0a -- specs/changes/<change-id>/proposal.md
git merge-base --is-ancestor <merge-commit> ac69894d94461f7e891dc817bd9ec81498978d0a
```

## Preservation and validation scope

All six manifest entries retain their existing raw SHA-256 hashes. All 25 dossier files, including the agent layout documentation review, retain their baseline bytes. Their historical statuses, task evidence and limitations remain as recorded. The living ADR backlink follows the relocated dossier; old paths quoted in historical validation logs and planning context remain unchanged.

The compatibility adjustment implements the immutable-history distinction in [ADR-0013](../decisions/0013-consolidated-sdd-workflow.md): an explicit `historical_archive` record permits default structural validation of already merged history. It does not grant v2 execution/delivery readiness. Dossiers without that record retain the prior archive checks, and v2 dossiers retain their existing approval/evidence requirements.

Acceptance checks for this maintenance are: no remaining active dossier from the baseline, exactly one archived copy per ID, unchanged dossier bytes and manifest hashes, valid live links, passing package/regression checks, and explicit implementation/delivery checks returning `unable-to-verify` for every historical dossier. Review must assess the merge evidence; the validator does not authenticate Git or platform records. This maintenance itself remains subject to PR review and required checks before merge.

## Observed local results

Validation ran on the maintenance working tree based on the baseline above:

- `PYTHON=/private/tmp/versat-sdd-acceptance-venv/bin/python ./scripts/validate/run.sh`: passed Plugin validation, default SDD validation and all 54 validator tests. Legacy warnings remained visible.
- Baseline byte comparison: all 25 relocated files matched `git show HEAD:specs/changes/<change-id>/<file>`; all six manifest hash maps remained unchanged.
- Inventory: no active dossiers remained, and each baseline ID had one archived directory.
- Explicit validation of each historical ID in both `implementation` and `delivery`: all 12 checks returned `unable-to-verify` with `LEGACY_UNVERIFIED`, as required.
- Affected local Markdown file targets resolved; `git diff --check` passed.

Regression coverage includes historical archival without a readiness claim, missing archive authorization records, modified dossier contents, reactivation in active storage, malformed records, missing/escaping evidence paths and unfinished tasks. Existing v2 archive and delivery regression cases also passed.
