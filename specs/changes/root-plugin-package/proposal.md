---
change: root-plugin-package
status: implemented
owner: versat
summary: Make the repository root the portable Versat AI Harness Plugin package
risk: high
---

# Proposal

## Context and problem

The repository currently declares `plugin/versat-ai-harness/` as the installable Plugin root while the Standards, SDD process, templates, schemas and validators required by its Skills live outside that package. Installing the Plugin therefore exposes its Skills without guaranteeing access to the canonical artifacts those Skills must apply.

Maintaining a copied runtime snapshot inside the nested package would add release machinery and create a second representation of the same governed content.

## Expected outcome

The repository root is both the canonical Harness source and a portable Agent Plugins package. Every installed version contains the Skills and the canonical artifacts they require, without duplicated policy trees.

A private GitHub marketplace entry makes an exact semantic version available to the Versat workspace. Workspace administrators retain control over role-based installation.

## Scope

- add a portable `plugin.json` at the repository root;
- keep a root `.codex-plugin/plugin.json` compatibility overlay;
- move installable Skills and agent role references to root-level directories;
- add a repository marketplace catalog for workspace distribution;
- update architecture, ADRs, repository instructions and validation contracts;
- prepare version `0.2.0` for governed release.

## Out of scope

- importing the marketplace into the ChatGPT Business workspace;
- changing remote workspace roles or installation policies;
- pushing the branch, opening a Pull Request or creating the release tag;
- implementing remote repository creation or consumer migration automation.

## Impact and risks

The package boundary changes and invalidates paths used by existing local installations. Consumers must reinstall version `0.2.0`. Installing the root package also includes the complete repository rather than only the former adapter subdirectory, increasing package size while keeping one authoritative copy of every artifact.

## Proposal acceptance criterion

The repository validates as a portable root Plugin, contains no tracked files under the former nested Plugin path, exposes an exact-version marketplace entry and passes all deterministic validation.
