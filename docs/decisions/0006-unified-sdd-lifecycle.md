# ADR-0006 — Adotar um ciclo SDD para todos os perfis

- Status: Accepted
- Data: 2026-08-28

## Contexto

Processos separados para software, agentes e infraestrutura duplicariam governança e criariam experiências inconsistentes.

## Decisão

Adotar um único ciclo Versat SDD. O perfil do projeto seleciona módulos, documentos e critérios adicionais, mas não altera o fluxo corporativo principal.

## Consequências

- toda mudança possui intenção, especificação, implementação, validação e revisão;
- agentes passam a ser tratados como software versionado, com testes e evals;
- o SDD deve permitir proporcionalidade para mudanças pequenas sem remover controles essenciais.
