# Marketplace identity research — 2026-11-18

## Official behavior

[Package documentation](https://developers.openai.com/plugins/build/plugins) distinguishes the marketplace identifier from its display label. Local enablement uses a qualified plugin/marketplace key; cached packages use a marketplace-specific path. Local client configuration does not administer workspace-managed installation policy. The source does not promise a transparent catalog rename or an identity alias.

[Developer commands](https://learn.chatgpt.com/docs/developer-commands) expose add/list/upgrade/remove operations and report plugin/marketplace identity separately. Listing/refresh behavior is not evidence that the same source can be registered twice with different names. No rename operation was documented in the inspected command surface.

[Workspace GitHub management](https://learn.chatgpt.com/docs/enterprise/plugin-management) supports fixed or moving catalog refs and automatic synchronization. Removing an entry differs from deleting an imported marketplace; deleting a marketplace deletes its imported plugins. The documented pluginId adoption mechanism has a limited use case and is not a generic cross-source rename contract. Its applicability to this existing workspace has not been established.

## Repository and bounded host observations

The repository currently declares `versat-internal` / `Versat Internal Plugins`, while the plugin remains `versat-ai-harness` and the candidate version 0.4.0. No source metadata is changed by this research. The package validator lacks an assertion for marketplace top-level name/display and therefore cannot demonstrate identity-transition correctness.

A local configuration read found an enabled qualified legacy plugin from a local rehearsal catalog. Matching personal 0.4.0 and separate workspace-directory 0.3.0 cached manifests were found. No target `versat` Harness cache was found. Cache presence is not proof of enabled managed use or a complete installation inventory. No workspace administrator configuration was inspected; raw local identifiers are retained only in private evidence.

The bundled CLI reported `0.155.0-alpha.9.2`; only version/help were invoked. No plugin add/list/upgrade/remove or app/workspace mutation was run. The official documentation and installed client can differ; the later compatibility test must record its actual runtime.

## Inference and recommendation

Treat this as a qualified-identity transition with opt-in adoption, not a cosmetic rename. The main risks to test are old enabled keys, new cache/provider selection, duplicate-source registration, unknown managed matching and automatically consumed source changes. Preserve the last verified old catalog/package pair and defer active migration until a supported path is observed. A label-only change is a fallback; it is not equivalent to changing the identifier.

## Deferred checks

Full managed inventory, target-name conflicts outside the observed local cache, duplicate registration, upgrade behavior, actual rollback and external installation/reporting/contribution remain unverified. No empirical migration result is claimed by this proposal or its planning validator.
