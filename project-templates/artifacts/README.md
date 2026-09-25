# Artifact authoring templates

Use these templates explicitly after project composition. This directory is not a profile module and is not copied wholesale by bootstrap. The canonical contract is the [Agent Artifact Standard](../../standards/core/agent-artifacts.md), selected through the Standards index.

| Source | Destination in the consumer project |
|---|---|
| `skill/SKILL.md` | `.agents/skills/<skill-name>/SKILL.md` |
| `agent.toml` | `.codex/agents/<agent-name>.toml` |
| `workflow.md` | `workflows/<workflow-name>/workflow.md` |

Replace illustrative names, instructions and placeholders before use. Verify capabilities against the target executor and installed integrations. Do not copy a Plugin Skill already provided by an exact installed release merely to populate the local directory.

The [supplier-payment example](../examples/supplier-payment/workflow.md) demonstrates workflow composition. Its named dependencies are illustrative and are not supplied as working integrations by this package.
