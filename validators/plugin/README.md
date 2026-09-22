# Plugin validation

`validate.py` enforces the portable root package contract:

- portable and Codex compatibility manifests are valid and agree;
- Plugin identity matches the semantic repository version;
- the marketplace selects the exact release tag;
- required Skills and canonical runtime directories exist;
- former nested Plugin entry points are absent.

The repository validation entry point invokes this validator.

Root `skills/` and `agents/` are package-level checks. They do not impose that layout on consumer projects or register Markdown role guidance as native Codex custom agents. Consumer checks are described separately in [project validation](../project/README.md).
