# ADR-0001 — Repositório único como fonte de verdade

- Status: Accepted
- Data: 2026-08-28

## Contexto

Plugin, Standards, SDD, templates e validadores evoluem juntos e precisam permanecer coerentes. Separá-los prematuramente criaria releases coordenadas, descoberta distribuída e risco de divergência.

## Decisão

Manter todos os componentes do Versat AI Harness em um único repositório versionado. O pacote em `plugin/versat-ai-harness/` é a raiz instalável do Plugin dentro deste repositório.

## Consequências

- mudanças transversais podem ser revisadas atomicamente;
- a versão do Harness identifica um conjunto coerente de artefatos;
- limites internos precisam continuar explícitos para evitar acoplamento indevido;
- uma separação futura em pacotes continua possível quando houver necessidade demonstrada.
