# ADR-0007 — Compor templates a partir de uma base

- Status: Accepted
- Data: 2026-08-28

## Contexto

Templates completos por perfil repetiriam arquivos comuns e divergiriam ao longo do tempo.

## Decisão

Definir uma camada `base` e módulos incrementais por perfil. Um projeto `agent` é `base + agent`; um projeto `hybrid` é `base + software + agent`.

## Consequências

- regras comuns são mantidas uma única vez;
- conflitos de composição precisam ser detectados;
- o bootstrap deve registrar quais módulos e versões foram aplicados.
