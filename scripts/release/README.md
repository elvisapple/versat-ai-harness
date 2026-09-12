# Release scripts

Release automation must validate semantic versions, changelog state, Plugin manifests, marketplace references and release provenance.

The repository root is the Plugin artifact; release automation does not build or maintain a copied distribution tree. Before creating a tag, it must confirm that:

- `VERSION`, `plugin.json` and `.codex-plugin/plugin.json` contain the same semantic version;
- `.agents/plugins/marketplace.json` selects the exact `v<VERSION>` Git reference;
- repository and Plugin validation pass;
- the release commit contains the canonical Standards, SDD, templates, schemas and validators used by its Skills.

Release automation must never rewrite consumer repositories directly. It proposes exact version updates through reviewable changes.

## Commit parsing

Before adding changelog generation or version inference from commits, implement the compatibility contract in the canonical [Git Standard](../../standards/core/git.md). A stock Conventional Commits parser cannot be assumed to recognize Versat's leading Shortcut marker. Parser support must preserve Story traceability and breaking-change information. No commit-driven release automation is implemented by this change.
