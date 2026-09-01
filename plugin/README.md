# Execution Adapter

This layer describes how agents execute Harness capabilities. The installable package is under `plugin/versat-ai-harness/`; its manifest and Skills follow the native Plugin structure.

Skills must resolve and consult the canonical artifacts under `standards/`, `sdd/` and `project-templates/`. Corporate rules must not be copied into a Skill.
