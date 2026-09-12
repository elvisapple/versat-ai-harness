# Standards validation

Validate the Standards index, referenced paths, lockfile completeness, versions and content digests. Report unknown profile, domain, technology and criticality values as explicit resolution errors.

## Git convention coverage

The [Git Standard](../../standards/core/git.md) defines branch and commit naming. During initial adoption, PR review checks compliance. The current structural validation entry point does not inspect Git history, enforce naming or verify Shortcut associations. A passing structural check is not evidence of these checks.

Any future validator must use the canonical policy, support its Shortcut prefix extension and distinguish syntactic validity from externally verified Story association. Blocking CI enforcement requires a separate governed rollout covering commit ranges, existing history and generated merge commits.
