# Changelog

All notable changes to this project will be documented in this file.

The format follows Keep a Changelog, and the project follows Semantic Versioning.

## [Unreleased]

### Added

- central SDD developer guide, structured review/evidence contracts and a stage-aware JSON Schema validator;
- regression cases for approval freshness, traceability, delivery readiness and explicit legacy migration;
- ADR-0012 governing single-Skill routing and documentary closure in the implementation PR.

### Changed

- consolidated SDD access in `versat-sdd`, with explicit routing to canonical workflows and three human planning gates;
- prepared documentary archival alongside code and living specifications before merge, with read-only delivery confirmation;
- included SDD validation and regression tests in the local and CI entry points, and corrected Skill review ownership;
- defined Shortcut-linked branch names and typed commit messages in the canonical Git Standard, preserving English technical descriptions and gradual adoption;
- added Story traceability prompts to SDD and PR review, with explicit squash, parser compatibility and validation guidance.

### Removed

- the standalone `new-change` Skill; its planning behavior and developer guidance now belong to the canonical SDD process.

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
