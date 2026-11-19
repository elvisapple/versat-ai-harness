# Python Standard

- Supported Python versions MUST be explicit and pinned in automation.
- Dependencies MUST use a lockfile or equivalent reproducible resolution.
- Public functions and complex domain logic SHOULD use type annotations.
- Formatting, linting and tests MUST run through a single documented entry point.
- The Harness Python reference uses pinned Ruff with lint families `E4`, `E7`,
  `E9` and `F` and a versioned formatter configuration. Check complete added
  and modified Python source files, including rename destinations. Apply
  exclusions for generated or vendored sources only through a documented and
  reviewed rule.
- The [project validation guide](../../docs/guides/project-validation.md)
  documents the local and CI commands and the Git comparison scope.
