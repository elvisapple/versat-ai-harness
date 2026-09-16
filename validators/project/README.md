# Project validation

Validate `.versat/project.yaml`, required directories for the resolved profile, ownership, README, instructions, SDD initialization and validation entry points.

## Agent artifact coverage

The [Agent Artifact Standard](../../standards/core/agent-artifacts.md) defines consumer paths, format requirements and workflow readiness. Future project validation must resolve this contract through the index, distinguish Plugin exports from project artifacts and report missing dependencies without implying successful execution.

No executable consumer artifact validator is implemented here yet. The repository entry point validates the Harness Plugin package, not generated project discovery, Codex agent TOML semantics, workflow completeness or external integrations. During adoption, review these contracts manually and run the target project's executor and integration checks. A passing Harness check does not prove consumer readiness.
