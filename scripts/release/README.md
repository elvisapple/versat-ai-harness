# Release scripts

Release automation must validate semantic versions, changelog state, Plugin manifests, marketplace references and release provenance.

The repository root is the Plugin artifact; release automation does not build or maintain a copied distribution tree. Before creating a tag, it must confirm that:

- `VERSION`, `plugin.json` and `.codex-plugin/plugin.json` contain the same semantic version;
- `.agents/plugins/marketplace.json` selects the exact `v<VERSION>` Git reference;
- repository and Plugin validation pass;
- the release commit contains the canonical Standards, SDD, templates, schemas and validators used by its Skills.

Release automation must never rewrite consumer repositories directly. It proposes exact version updates through reviewable changes.
