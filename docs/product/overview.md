# Product overview

[English](overview.md) | [Português](overview.pt.md) | [Español](overview.es.md)

## Product and ownership

Versat AI Harness helps the Versat team turn development intent into reviewed, traceable changes. Versat maintains the product; repository contacts include elviszoz and evertonspohrversat, who are listed in CODEOWNERS for governed components. This overview describes the source repository, not a promise that every capability is installed in every workspace.

## Problem, job and persona

[Issue #22](https://github.com/versat-labs/versat-ai-harness/issues/22) states that the team does not know how to use the new Harness. The primary persona is the Versat team, especially SDD developers. When planning or implementing a user story, they need repository documentation so they can understand and follow the development process. The frequency and cost of this onboarding problem have not been measured; validate them through team feedback after first use.

## Solution and value

One versioned Plugin combines canonical Standards, the SDD lifecycle, five Skills, composable templates and deterministic validation. Developers receive reusable guidance for bootstrap, changes, maintenance, audit and architecture review. Expected value is clearer shared decisions and reproducible checks; improved productivity and fewer defects remain outcomes to measure, not established results.

## Origin and timing

The ADR history records the move toward a portable package and a single governed lifecycle. The issue and team training show a current need for a clearer entry path. Consolidating that knowledge now supports adoption without adding a competing process. Further origin claims require evidence from the product owner.

## Current boundaries

VERSION declares 0.3.0. Source-only consumer test execution and supervised evaluation are explicitly labeled unreleased in their guides. The Harness does not itself provide an operational workflow engine, automatic remote repository provisioning or automatic consumer upgrades. Local validator success does not prove semantic acceptance, human approval authenticity, remote CI or merge.

## Internal value and market applicability

This scope is an internal development tool, with no supplied external pricing or commission model. TAM, SAM, SOM and take rate are not applicable to this documentation delivery. Assess internal value through onboarding completion, time to a first reviewed plan and recurring support questions; no baseline or financial return is established.

## Alternatives, differentiation and innovation

Alternatives include scattered team instructions, repository-specific checklists and generic coding assistance. The Harness combines context-resolved Standards, explicit review gates and version-bound checks in one package. This is a product integration choice, not a claim of market novelty or demonstrated superiority.

## Scalability and responsibility

Exact release adoption and shared templates support more repositories; translation upkeep, human review, workspace access and provider compatibility remain constraints. Accessibility and multilingual guidance can lower onboarding barriers. Model usage and repeated evaluations consume resources; measure usage before claiming environmental gains. Protect private training and customer information.

## Open questions and validation

Ask the product owner to confirm an adoption baseline and success measures after the team follows the quickstart. Ask workspace administration to confirm the installed release and distribution policy. Review accessible training transcripts before using video-specific steps. These research gaps do not imply additional implemented capabilities.

[Start using the Harness](../user-docs/quickstart.md) · [ADRs (English)](../decisions/README.md)
