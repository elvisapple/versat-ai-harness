# Entrega pelo GitHub

[English](github-delivery.md) | [Português](github-delivery.pt.md) | [Español](github-delivery.es.md)

Use este guia ao preparar uma mudança vinculada a uma issue para revisão humana. Você precisa da URL real da issue, instruções do repositório, escopo aprovado e ambiente de validação do projeto.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $versat-sdd para inspecionar <change-id>, preparar o resumo de entrega e identificar pré-requisitos de arquivo ou validação ausentes. Não publique PR nem faça merge.
```

## Resultado esperado

Trabalhe em uma branch seguindo a convenção Git resolvida. Mantenha rastreabilidade entre issue, requisitos e commits; não invente um ID do Shortcut. Planejamento ou trabalho incompleto é revisado em PR draft. Antes de submeter a implementação concluída, prepare o arquivo documental na mesma branch e passe no preflight de arquivo selecionado. Solicite a publicação do PR explicitamente; depois obtenha revisão humana e CI obrigatório final antes do merge.

## Recuperação e limites

Informe no PR as verificações falhas ou indisponíveis. O feedback da revisão permanece no mesmo ID; mudanças de escopo reabrem a revisão correspondente. Verifique o merge real separadamente da prontidão local. Um merge não publica uma release nem atualiza consumidores instalados.

## Referências

- [Git (inglês)](../../../standards/core/git.md)
- [SDD (inglês)](../../../sdd/README.md)
- [SDD validation (inglês)](../../../validators/sdd/README.md)

[Gravação da equipe](https://versat.slack.com/archives/C0B7G255DPY/p1793910356829109) — requer acesso ao Slack. Treinamento complementar; o conteúdo do vídeo não foi verificado para este guia. Os passos escritos permitem continuar.

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
