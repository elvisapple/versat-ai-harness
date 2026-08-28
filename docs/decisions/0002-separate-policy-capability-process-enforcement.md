# ADR-0002 — Separar políticas, capacidades, processo e enforcement

- Status: Accepted
- Data: 2026-08-28

## Contexto

Regras corporativas escondidas em Skills podem não ser carregadas. Instruções de agentes também não são garantia suficiente para controles obrigatórios.

## Decisão

Separar responsabilidades:

- `standards/`: políticas canônicas;
- `plugin/versat-ai-harness/skills/`: capacidades e procedimentos;
- `sdd/`: processo de mudança;
- `validators/` e CI: enforcement determinístico.

Skills referenciam Standards, mas não os duplicam.

## Consequências

- políticas continuam auditáveis mesmo sem um executor específico;
- Skills permanecem pequenas e carregadas sob demanda;
- regras críticas precisam de validadores ou controles de plataforma;
- alterações podem exigir coordenação entre orientação e enforcement.
