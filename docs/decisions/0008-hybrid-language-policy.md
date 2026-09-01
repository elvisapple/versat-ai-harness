# ADR-0008 — Adopt a hybrid language policy

- Status: Superseded by [ADR-0010](0010-refine-language-policy.md)
- Date: 2026-08-28

## Context

The team needs to combine international technical interoperability with product documentation that is accessible in the corporate context.

## Decision

Use English in code, identifiers, APIs, database objects, technical names and commits. Use Spanish in specifications, requirements, decisions and business documentation. Interface content follows the product locale.

## Consequences

- validators must distinguish technical artifacts from business documents;
- widely accepted terms may remain in the technical language when translation reduces precision;
- exceptions must be recorded in the canonical language document.
