# ADR-0003 — Resolver contexto por metadados declarativos

- Status: Accepted
- Data: 2026-08-28

## Contexto

Pedir que cada equipe escolha manualmente seus Standards gera lacunas e combinações inconsistentes.

## Decisão

Cada projeto declara perfil, domínio, criticidade e tecnologias em `.versat/project.yaml`. O Harness resolve os documentos aplicáveis por `standards/index.yaml` na ordem:

```text
core + profile + domain + technologies + criticality
```

## Consequências

- a experiência de bootstrap permanece simples;
- a seleção de normas é reprodutível e testável;
- o índice se torna um contrato crítico e deve ser validado;
- exceções precisam ser explícitas, justificadas e versionadas.
