# Changelog

All notable changes to this project will be documented in this file.

The format follows Keep a Changelog, and the project follows Semantic Versioning.

## [Unreleased]

### Changed

- separated consumer Skills, Codex custom agents and Versat operational workflows through a canonical artifact Standard and updated agent/hybrid template guidance;
- added explicit authoring templates, a supplier-payment workflow example and reviewed migration guidance while preserving the Harness Plugin package layout;
- clarified Plugin role guidance, SDD procedures and validation limits; recorded ADR-0012 and the `agent-project-layout` SDD change.
- replaced the obsolete nested Plugin CODEOWNERS path with current Skills, role guidance and project-template ownership.
- defined Shortcut-linked branch names and typed commit messages in the canonical Git Standard, preserving English technical descriptions and gradual adoption;
- added Story traceability prompts to SDD and PR review, with explicit squash, parser compatibility and validation guidance.

## [0.2.0] - 2026-09-08

### Added

- portable Agent Plugins manifest at the repository root;
- private GitHub marketplace metadata for ChatGPT workspace distribution;
- deterministic validation for portable and compatibility manifests, marketplace pinning and version agreement;
- ADR-0011 and SDD artifacts governing the package-boundary migration.

### Changed

- made the repository root the installable Plugin package boundary;
- moved Skills and reusable agent roles to root-level directories;
- updated Skills to resolve canonical artifacts from the installed Plugin root;
- aligned legacy technical documentation, ADRs, SDD templates and Plugin metadata with the canonical language standard;
- superseded ADR-0008 with ADR-0010 to record the refined language policy;
- superseded ADR-0001 and ADR-0002 with ADR-0011.

## [0.1.0] - 2026-08-28

### Added

- initial Versat AI Harness architecture;
- Plugin manifest and five foundational Skills;
- declarative Standards catalog;
- initial SDD process, schemas, templates and workflows;
- composable templates for project profiles;
- validation contracts and minimum CI pipeline;
- architecture documentation and foundational ADRs.
