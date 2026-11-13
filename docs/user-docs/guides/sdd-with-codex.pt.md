# SDD com Codex

[English](sdd-with-codex.md) | [Português](sdd-with-codex.pt.md) | [Español](sdd-with-codex.es.md)

Use este caminho para transformar uma história em especificações revisadas e retomar o trabalho entre chats. Comece com um repositório preparado, suas instruções, uma issue real quando disponível e a versão selecionada do Harness.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $versat-sdd para inspecionar a mudança <change-id> e informar fase atual, aprovações, bloqueios e próxima ação permitida. Não altere arquivos.
```

## Resultado esperado

O relatório identifica o mesmo dossiê e as evidências de cada aprovação. No planejamento novo, espere primeiro Proposal/Requirements; Design e Tasks vêm após as respectivas aprovações. Depois de revisar Tasks, solicite explicitamente a implementação. Para pedir correções junto com validação, inclua isso no pedido.

## Recuperação e limites

Se faltar evidência de revisão, revise a versão apresentada em vez de recriar aprovações. Um requisito alterado reabre os gates afetados. Ao retomar, mantenha o ID da mudança; a localização no arquivo não comprova entrega.

## Referências

- [SDD (inglês)](../../../sdd/README.md)
- [Process (inglês)](../../../sdd/process.md)
- [Metadata (inglês)](../../../sdd/metadata.md)

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
