# Manter um projeto existente

[English](project-maintenance.md) | [Português](project-maintenance.pt.md) | [Español](project-maintenance.es.md)

Use manutenção para upgrades ou divergências em um repositório existente. Informe identidade/lockfile atual, release alvo explícita, adaptações locais e comandos de validação mantidos.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $project-maintenance para comparar este repositório com a release alvo exata do Harness que forneci. Preserve mudanças locais, apresente conflitos de migração e um plano de rollback, e não publique mudanças remotas.
```

## Resultado esperado

Espere um diff revisável de snapshots de Standards, templates, referências de capacidades e metadados. Classifique os artefatos do consumidor antes de movê-los. Preserve wrappers e testes próprios. Valide com o provedor alvo; registre a versão exata adotada e os resultados de integração.

## Recuperação e limites

Se nenhum alvo foi fornecido, resolva-o antes de alterar pins; nunca use latest. Apresente conflitos em vez de sobrescrevê-los. Reverta configurações e referências do provedor em conjunto e execute a suíte original restaurada.

## Referências

- [Skill (inglês)](../../../skills/project-maintenance/SKILL.md)
- [Changelog (inglês)](../../../CHANGELOG.md)
- [Migration (inglês)](../../../project-templates/README.md)

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
