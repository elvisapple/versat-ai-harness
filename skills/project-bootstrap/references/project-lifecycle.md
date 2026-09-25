# Project Lifecycle

## 1. Intake

Capture sponsor, objective, expected users, data sensitivity, operational criticality, profile and technologies. Use [guided product discovery](product-discovery.md) to develop the product context with the developer, reusing supplied information and recording unknowns explicitly.

## 2. Bootstrap

Create the repository from the composed template, populate `specs/product/overview.md` and supporting files when needed, add the project identity and lockfile, initialize the first SDD change with references to the product context, and run baseline validation. Present the product draft and evidence gaps for review separately from structural readiness.

## 3. Repository readiness

Verify ownership, default branch protection, required checks, secret scanning, dependency update policy and access boundaries before normal delivery begins.

## 4. Delivery

Use the SDD lifecycle for material changes. Keep proposal, requirements, design, tasks, implementation and validation consistent throughout review.

## 5. Operations

Operate according to the resolved profile and criticality requirements. Preserve observability, recovery, security and ownership evidence.

## 6. Evolution

Adopt Harness and Standards updates only through explicit versioned migrations. Review diffs, update the lockfile, run validation and merge through the governed workflow.

## 7. Retirement

Document owners, data disposition, dependency removal, access revocation and retained records. Retirement is a governed change, not an untracked deletion.
