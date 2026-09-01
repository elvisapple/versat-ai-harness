# ADR-0004 — Distribute versioned snapshots with a lockfile

- Status: Accepted
- Date: 2026-08-28

## Context

Consuming `latest` causes old branches to change behavior without a Git change. Submodules add operational complexity for the team.

## Decision

Consumer projects receive versioned snapshots of applicable artifacts and record the exact versions in `.versat/standards.lock`. New releases are proposed through automated Pull Requests. Git submodules will not be the default mechanism.

## Consequences

- builds and executions remain reproducible;
- updates have a diff, CI and review;
- each snapshot incurs a storage cost;
- automation must identify outdated consumers without silently updating them.
