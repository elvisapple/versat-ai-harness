# Testing configuration validator

`validate.py --root <consumer>` checks the versioned `.versat/validation.yaml` contract without launching project commands. [Configuration](../../schemas/validation.schema.yaml) and [structured counts](../../schemas/validation-result.schema.yaml) are pure contracts; explicit execution belongs to `scripts/testing/run.py`.

See [Project validation](../../docs/guides/project-validation.md) for complete setup, supported adapters, scope review and evidence limits. The source repository is the Plugin provider, not a fabricated consumer, and does not require a root `.versat/validation.yaml`.
