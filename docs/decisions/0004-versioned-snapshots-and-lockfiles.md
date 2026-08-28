# ADR-0004 — Distribuir snapshots versionados com lockfile

- Status: Accepted
- Data: 2026-08-28

## Contexto

Consumir `latest` faz branches antigos mudarem de comportamento sem alteração no Git. Submodules adicionam complexidade operacional para a equipe.

## Decisão

Projetos consumidores recebem snapshots versionados dos artefatos aplicáveis e registram as versões exatas em `.versat/standards.lock`. Novas releases são propostas por Pull Request automatizado. Git submodules não serão o mecanismo padrão.

## Consequências

- builds e execuções permanecem reprodutíveis;
- atualizações têm diff, CI e revisão;
- existe custo de armazenamento por snapshot;
- automação deverá identificar consumidores desatualizados sem atualizá-los silenciosamente.
