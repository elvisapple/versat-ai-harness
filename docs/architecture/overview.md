# Architecture overview

## Purpose

Versat AI Harness is the governance runtime that connects agents, Enterprise Standards, Versat SDD, local projects and GitHub. The repository root is both the product's source of truth and the portable installable Plugin boundary.

## Components

```text
                    VERSAT AI HARNESS
                         source of truth
                                |
          +---------------------+---------------------+
          |                     |                     |
      Standards                SDD               Validators
        (rules)              (process)           (enforcement)
          |                     |                     |
          +---------------------+---------------------+
                                |
                        execution adapters
                                |
                +---------------+---------------+
                |               |               |
          Codex Plugin        CI/CD          future tools
                |
         project-bootstrap
                |
         standards resolver
                |
        project repository
```

## Context model

Each project declares only its identity:

```yaml
project:
  profile: agent
  domain: finance
  criticality: high
technologies:
  - python
```

The resolver uses `standards/index.yaml` to compose:

```text
core + profile + domain + technologies + criticality
```

The exact resolved versions are recorded in `.versat/standards.lock`. Consumers do not manually select standards packages and do not silently follow `latest`.

## Package boundary

```text
versat-ai-harness/
├── plugin.json                 portable package manifest
├── .codex-plugin/plugin.json   Codex compatibility overlay
├── skills/                     capabilities and procedures
├── agents/                     reusable execution roles
├── standards/                  canonical policies
├── sdd/                        canonical change process
├── project-templates/          composable project structures
├── schemas/                    metadata contracts
└── validators/                 deterministic enforcement
```

Keeping the canonical core and its execution capabilities inside one package boundary prevents an installed Skill from losing access to its version-matched Standards, process or templates. Directory responsibilities remain separate even though they share the portable package root.

## Consumer artifacts and execution

The consumer contract is defined in the [Agent Artifact Standard](../../standards/core/agent-artifacts.md) and resolved through `standards/index.yaml`. It separates capabilities, execution roles and operational composition:

```text
consumer-project/
├── AGENTS.md
├── .agents/skills/<skill-name>/SKILL.md
├── .codex/agents/<agent-name>.toml
├── workflows/<workflow-name>/workflow.md
├── evals/
└── tests/
```

A workflow explicitly calls Skills and passes their results between steps. The chosen executor loads the workflow document and provides the tool access and execution state. Codex agents use the TOML adapter; the workflow convention does not itself register agents, schedule runs or implement integrations. These artifacts may implement business operations or development assistance. Separately deployed application agents retain the architecture of their application runtime.

The agent template extends `base`; hybrid composition adds the software module and its application source directories. Authoring templates and illustrative examples are supplied separately and are not automatically installed as active capabilities. See [template composition](../../project-templates/README.md) and [ADR-0012](../decisions/0012-consumer-agent-artifacts.md).

The Harness root `agents/*.md` files remain reusable role guidance requiring explicit loading or conversion; they are not native Codex custom-agent registrations. `sdd/workflows/` contains development lifecycle procedures, while consumer `workflows/` describes operational flows. GitHub Actions retain their separate `.github/workflows/` contract.

## Unified lifecycle

```text
Intent -> Proposal -> Requirements -> Design -> Tasks
       -> Implementation -> Tests/Evals -> Validation
       -> Pull Request -> Merge -> Living Specification
```

The same lifecycle applies to software, agent, library, automation, infrastructure and hybrid projects. The profile changes the applicable modules and criteria, not the corporate process.

## Knowledge governance

| Level | Example | Allowed change |
|---|---|---|
| Operational memory | contextual customer preference | automatic learning within retention boundaries |
| Skill | how to prepare a recurring analysis | proposal and human approval |
| Corporate policy | security, language, Git, `AGENTS.md` | branch, PR, review and required checks |

## Distribution and enforcement

- The Plugin distributes capabilities and instructions on demand.
- The repository marketplace selects an exact semantic Plugin release from GitHub.
- Versioned snapshots and lockfiles make Standards application reproducible.
- Pull Requests propagate new releases to consumer repositories.
- GitHub Rulesets and reusable workflows enforce policies that cannot rely on agents alone.
- The Marketplace is a distribution channel, not the normative authority.

## Version 0.2.0 boundaries

This version makes the source repository a self-contained portable Plugin package and defines workspace distribution metadata. Remote repository creation, automated workspace import, consumer release resolution, GitHub organization configuration and technology-specific semantic validators are not yet part of the executable implementation.

The unreleased consumer artifact revision changes templates and guidance. Automated project composition, operational workflow execution and semantic validation of consumer agent artifacts are not implemented by it. The existing repository validator checks Plugin structure; consumer loading and workflow behavior require separate verification.
