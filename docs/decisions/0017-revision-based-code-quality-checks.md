# ADR-0017 — Validate code and changelog changes against a reviewable Git baseline

- Status: Accepted with Design R1
- Date: 2026-11-18
- Related: ADR-0003, ADR-0004, ADR-0011, ADR-0014, ADR-0015
- Change: `coding-standards`, Design R1
- Decision evidence: The developer approved Design R1 and ADR-0017 in the issue #27 Codex chat with “Aprovo o Design R1 e o ADR-0017 da issue #27.” The accepted Design digest is `c2d456db6f44c604141519558f7be127564ffac2c20a16a45c94721cc4045bcc`.

## Context

The Harness and its Python reference consumer already run project checks. The
new contract needs to detect objective violations and missing changelog entries
without making unrelated formatting debt part of every change.

## Decision

Resolve the coding policy through the Standards index. Run an explicit,
read-only quality command from local validation and CI. Compare trusted Git
revisions to select changed paths and detect new Unreleased notes. Apply pinned
lint and formatting rules to complete Python files added or modified by the
change. Require human PR review for semantic design, changelog accuracy and
changes to the quality policy or its enforcement.

Keep the comparison for code quality separate from the SDD archive selector.
Preserve required suites and the SDD validator's read-only evidence contract.
Adopt the consumer integration through the existing exact-provider and template
composition contracts.

## Alternatives and consequences

Full-tree enforcement would require immediate cleanup of unrelated files.
Line-level filtering could miss file-wide lint violations and formatter edits.
File-level adoption makes the entire touched file subject to the rules. Teams
can separate substantial mechanical edits from functional edits for review.

A dedicated command makes comparison and diagnostics reusable without adding
Git event semantics to the suite executor or a new SDD gate.
