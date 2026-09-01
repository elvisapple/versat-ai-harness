# Architecture overview

## Purpose

Versat AI Harness is the governance runtime that connects agents, Enterprise Standards, Versat SDD, local projects and GitHub. The repository is both the product's source of truth and the installable Plugin unit.

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
- Versioned snapshots and lockfiles make Standards application reproducible.
- Pull Requests propagate new releases to consumer repositories.
- GitHub Rulesets and reusable workflows enforce policies that cannot rely on agents alone.
- The Marketplace is a distribution channel, not the normative authority.

## Version 0.1.0 boundaries

This version defines contracts, baseline content and structural validation. Remote repository creation, release resolution, GitHub organization configuration and technology-specific semantic validators are not yet part of the executable implementation.
