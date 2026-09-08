# Plugin validation

`validate.py` enforces the portable root package contract:

- portable and Codex compatibility manifests are valid and agree;
- Plugin identity matches the semantic repository version;
- the marketplace selects the exact release tag;
- required Skills and canonical runtime directories exist;
- former nested Plugin entry points are absent.

The repository validation entry point invokes this validator.
