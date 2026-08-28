# Architecture Decision Records

Os ADRs preservam o contexto e as consequências das decisões estruturais do Harness.

## Estados

- `Proposed`: em discussão;
- `Accepted`: decisão vigente;
- `Superseded`: substituída por outro ADR;
- `Deprecated`: mantida apenas por histórico.

## Regra de evolução

Não reescreva silenciosamente uma decisão aceita. Crie um novo ADR, referencie o anterior e atualize seu estado quando uma decisão for substituída.

## Índice

- [ADR-0001 — Repositório único como fonte de verdade](0001-single-source-repository.md)
- [ADR-0002 — Separar políticas, capacidades, processo e enforcement](0002-separate-policy-capability-process-enforcement.md)
- [ADR-0003 — Resolver contexto por metadados declarativos](0003-declarative-context-resolution.md)
- [ADR-0004 — Distribuir snapshots versionados com lockfile](0004-versioned-snapshots-and-lockfiles.md)
- [ADR-0005 — Governar conhecimento em três níveis](0005-three-level-knowledge-governance.md)
- [ADR-0006 — Adotar um ciclo SDD para todos os perfis](0006-unified-sdd-lifecycle.md)
- [ADR-0007 — Compor templates a partir de uma base](0007-composable-project-templates.md)
- [ADR-0008 — Adotar política híbrida de idiomas](0008-hybrid-language-policy.md)
- [ADR-0009 — Manter o Harness independente do executor](0009-execution-adapters.md)
