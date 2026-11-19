# Validation and evaluations

[English](validation-and-evaluations.md) | [Português](validation-and-evaluations.pt.md) | [Español](validation-and-evaluations.es.md)

Choose the check for the repository and outcome you need: Harness package consistency, consumer application suites or supervised Skill behavior. Prepare Python 3.11+ and the selected provider’s validation dependencies; application dependencies are separate.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $versat-sdd to validate <change-id> against its approved plan. Report actual evidence and gaps. Do not fix product files under this validation-only request.
```

## Expected result

In the Harness root, `./scripts/validate/run.sh --quality-base origin/main` checks the package, SDD records and maintained regressions. It does not run another project’s application tests. Consumer execution and supervised evaluation described in the specialized guides are unreleased source capabilities: use an exact provider containing them and follow their adoption prerequisites. Full required suites, targeted runs and supervised observations have different evidence limits.

## Recovery and limits

Expect pass, fail or unable-to-verify with actual counts/results and tested inputs. Preserve failed attempts; missing access, empty tests or unavailable observations cannot establish success. Assess every acceptance and retained regression obligation; structural success cannot prove semantic acceptance, human identity or remote merge.

## References

- [Project validation (English)](../../guides/project-validation.md)
- [Skill evaluations (English)](../../guides/skill-evaluations.md)
- [SDD validation (English)](../../../validators/sdd/README.md)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
