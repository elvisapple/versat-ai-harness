# Private H02 delivery package

Prepared for versat-labs/.github, base a762582c6585ae967c37f7f7f1c69c06c07e9071. Local preparation only. Do not publish, apply repository settings, send reports or activate channels under the present authorization.

## Contents and scope

Payload: CONTRIBUTING.md, CONTRIBUTING.pt.md, CONTRIBUTING.es.md, SECURITY.md, SECURITY.pt.md, SECURITY.es.md, .github/VULNERABILITY_REPORT.yml. The existing issue forms, names, title prefixes, required fields, types, project association, profile and READMEs are unchanged. candidate.patch is the reviewable exact baseline diff; manifest.json binds baseline and candidate hashes. PR-DRAFT.es.md is proposed internal review text, not a submitted PR.

The form is a native private vulnerability form, outside ISSUE_TEMPLATE. For public repositories use the affected repository's PVR when enabled; for private repositories email relevant CODEOWNERS through existing internal Versat contacts. CODEOWNERS own monitoring, triage and remediation coordination. A template does not configure subscriptions/access or activate the feature.

## Later authorized application

1. Refresh the target repository and read its AGENTS. If the reviewed files changed since the selected base, reconcile instead of forcing the patch.
2. In a private local checkout/branch, run `git apply --check candidate.patch`; inspect the seven-file diff. Applying/publishing to GitHub is a separate scope, not an action performed by this package.
3. When public PR publication is authorized, use the prepared description and the organization's required review. Preserve the existing route if a replacement target is unavailable. Keep these private delivery notes and the full Harness inventory out of the public payload.
4. On separately authorized rollout, enable PVR only for intended public repositories, verify intended reader access, CODEOWNERS/responder permissions and notifications, and any repository-specific override. Do not assume default inheritance overrides local forms or enables the feature.
5. For private repositories, verify CODEOWNERS/contact routing without publishing internal addresses. Under explicit bounded authorization, check non-sensitive receipt/access for the selected routes. No such test or message is authorized here.

Rollback after a future authorized rollout: revert only the seven introduced/changed files through the normal review flow, retaining preexisting forms/profile/instructions. Any channel/permission configuration rollback is distinct and must be separately scoped. Never expose report contents during rollback.

## Acceptance status

Private documentary preparation is complete. Owner terms approval, first-party provenance and dependency-text evidence are recorded in H01. Local YAML, translations, links, exact-source references, unchanged-file checks and forward/reverse patch applicability are review evidence. Live GitHub rendering/inheritance, effective enablement, access and receipt remain unverified; full H02 operational acceptance cannot be certified in a no-activation/no-message phase. No new owner role decision is required.

Baseline refresh: previous ref 4410a8d38ac98bdbc7b17ed8f0c0053052a8ebb5 advanced to a762582c6585ae967c37f7f7f1c69c06c07e9071. The 12 prior file blobs are unchanged; newly observed .github/CODEOWNERS (* @elviszoz) is preserved in baseline and candidate. The seven-file patch does not change it.
