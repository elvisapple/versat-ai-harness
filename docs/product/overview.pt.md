# Visão do produto

[English](overview.md) | [Português](overview.pt.md) | [Español](overview.es.md)

## Produto e responsabilidade

O Versat AI Harness ajuda a equipe Versat a transformar intenções de desenvolvimento em mudanças revisadas e rastreáveis. A Versat mantém o produto; os contatos incluem elviszoz e evertonspohrversat, listados em CODEOWNERS nos componentes governados. Esta visão descreve o repositório fonte, sem presumir que todas as capacidades estejam instaladas em todos os workspaces.

## Problema, trabalho e persona

A [Issue #22](https://github.com/versat-labs/versat-ai-harness/issues/22) informa que a equipe não sabe usar o novo Harness. A persona principal é a equipe Versat, especialmente quem desenvolve com SDD. Ao planejar ou implementar uma história, precisa consultar a documentação do repositório para compreender e seguir o processo. A frequência e o custo desse problema de onboarding não foram medidos; valide-os com feedback da equipe após o primeiro uso.

## Solução e valor

Um Plugin versionado reúne Standards canônicos, ciclo SDD, cinco Skills, templates compostos e validação determinística. A equipe recebe orientação reutilizável para bootstrap, mudanças, manutenção, auditoria e revisão arquitetural. O valor esperado é maior clareza nas decisões e verificações reproduzíveis; produtividade maior e menos defeitos são resultados a medir, não resultados comprovados.

## Origem e momento

O histórico de ADRs registra a evolução para um pacote portátil e um ciclo governado único. A issue e os treinamentos mostram a necessidade atual de uma entrada mais clara. Consolidar esse conhecimento apoia a adoção sem criar um processo concorrente. Outras afirmações sobre a origem exigem evidência do responsável pelo produto.

## Limites atuais

VERSION declara 0.3.0. Execução de testes de consumidores e avaliação supervisionada presentes na fonte são explicitamente identificadas como não lançadas nos guias. O Harness não fornece por si um motor de workflows operacionais, provisionamento remoto automático ou upgrades automáticos de consumidores. Sucesso local do validador não comprova aceitação semântica, autenticidade de aprovação, CI remoto nem merge.

## Valor interno e aplicabilidade de mercado

O escopo é uma ferramenta interna de desenvolvimento, sem preço externo ou modelo de comissão fornecido. TAM, SAM, SOM e take rate não se aplicam a esta entrega documental. Avalie valor interno pela conclusão do onboarding, tempo até o primeiro plano revisado e dúvidas recorrentes; não há baseline nem retorno financeiro comprovado.

## Alternativas, diferenciação e inovação

Alternativas incluem instruções dispersas da equipe, checklists próprios de cada repositório e assistência genérica de código. O Harness combina Standards resolvidos por contexto, gates explícitos e verificações vinculadas à versão em um pacote. É uma escolha de integração, sem alegação de novidade de mercado ou superioridade demonstrada.

## Escalabilidade e responsabilidade

Adoção de releases exatas e templates compartilhados apoiam mais repositórios; manutenção de traduções, revisão humana, acesso e compatibilidade continuam sendo restrições. Acessibilidade e orientação multilíngue podem reduzir barreiras. Uso de modelos e avaliações repetidas consomem recursos; meça antes de afirmar ganhos ambientais. Proteja treinamentos privados e informações de clientes.

## Questões abertas e validação

Peça ao responsável pelo produto para confirmar baseline de adoção e medidas de sucesso após a equipe seguir o quickstart. Peça à administração do workspace para confirmar release instalada e política de distribuição. Revise transcrições acessíveis antes de usar passos específicos dos vídeos. Essas lacunas de pesquisa não implicam capacidades adicionais implementadas.

[Começar a usar o Harness](../user-docs/quickstart.pt.md) · [ADRs (inglês)](../decisions/README.md)
