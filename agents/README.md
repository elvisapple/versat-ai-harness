# Harness execution role guidance

The Markdown files in this directory describe reusable Harness roles. They are package resources for explicit reading, not native Codex custom-agent registrations.

For a consumer project, use the resolved [Agent Artifact Standard](../standards/core/agent-artifacts.md) and the [authoring templates](../project-templates/artifacts/README.md) to create an executor configuration when needed. Translating a role into TOML requires choosing its instructions and supported runtime settings; copying or renaming the Markdown file does not register an agent.

The orchestrator can guide the SDD lifecycle or an explicitly supplied operational workflow. Its role does not implement a scheduler, grant connector access or replace the workflow's execution and recovery contract.
