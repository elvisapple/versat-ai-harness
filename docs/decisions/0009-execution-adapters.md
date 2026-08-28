# ADR-0009 — Manter o Harness independente do executor

- Status: Accepted
- Data: 2026-08-28

## Contexto

Standards e SDD têm vida útil maior que qualquer agente, IDE ou fornecedor específico.

## Decisão

Tratar Codex Plugin, CI/CD, CLI e futuras integrações como adaptadores de execução sobre o mesmo núcleo versionado. O Marketplace distribui capacidades, mas não é a fonte de autoridade.

## Consequências

- novos executores podem reutilizar Standards, SDD e validadores;
- integrações específicas não podem contaminar contratos canônicos;
- o primeiro adaptador será o Plugin Codex, sem impedir outros.
