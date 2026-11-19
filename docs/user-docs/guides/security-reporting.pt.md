# Relatar uma preocupação de segurança com cuidado

[English](security-reporting.md) | [Português](security-reporting.pt.md) | [Español](security-reporting.es.md)

GitHub Private Vulnerability Reporting está habilitado neste repositório público. Acesso do relator externo, recebimento e confidencialidade permanecem **não verificados** até a execução do teste externo adiado. Habilitar o canal e concluir o teste interno de revisão de PR não comprova a entrega de relatos externos.

Observações anteriores do H02 cobriram outro piloto público e um recebimento interno do Harness. São evidências históricas, sem comprovar uma rota pública do Harness. @elviszoz e @evertonspohrversat compartilham monitoramento, triagem e coordenação; Elvis mantém a coordenação responsável. Qualquer um pode atender um relato. Registre um responsável efetivo e uma passagem de atendimento explicitamente reconhecida se essa pessoa estiver indisponível; não são necessárias duas respostas. A atribuição e o CODEOWNERS não configuram notificações nem comprovam acesso ou recebimento. A participação de ambos na triagem compartilhada e nos testes futuros foi confirmada pelo responsável. O recebimento público continua não verificado. Uma passagem real de atendimento será registrada quando necessária; ela não exige uma simulação separada antes da publicação.

A política de revisão exige uma aprovação de CODEOWNER elegível que não seja autor da PR; ela é separada da triagem de segurança. A aprovação do próprio autor não atende ao requisito, e a responsabilidade compartilhada não exige duas aprovações. A branch base efetiva determina a elegibilidade; veja a [transição de responsáveis](../../handoffs/harness-publication-blockers/transition.md#general-ownership-and-base-branch-transition).

O procedimento anterior de transição no GitHub Free é histórico: abertura pública, proteção da main e ativação do canal já ocorreram. O teste externo de relato/recebimento/exclusão permanece pendente; as [notas da candidata](../../releases/0.4.0-candidate.pt.md) distinguem esses estados.

## Antes de compartilhar detalhes

Leia as instruções reais de segurança do destino. Confirme destino confidencial, relatores previstos, destinatários permitidos e tratamento dos dados antes de enviar informações sensíveis. Não coloque detalhes de exploração, credenciais, dados de clientes ou anexos sensíveis em issues comuns. Sessão administrativa ou URL funcional não comprova acesso externo ou confidencialidade.

## Quando a rota estiver indisponível

Use um contato de mantenedor já visível somente para pedir, sem detalhes sensíveis: “Preciso de instruções confidenciais para relatar um problema de segurança neste repositório.” Aguarde uma rota apropriada e verificada. Se houver acesso negado ou mudança de destino, pare e peça instruções atualizadas. Mantenha o relato privado se não houver rota adequada. O exemplo não envia mensagem nem autoriza um agente a fazê-lo.

Resultado esperado: instruções seguras ou uma lacuna explícita de verificação, sem presumir recebimento. Nenhum email interno, endpoint novo, prazo de resposta ou período de retenção é fornecido aqui.

## Verificação pelo mantenedor

Para o teste público posterior, autorizado separadamente, use um relato identificado e não sensível de um relator do público previsto. Verifique o acesso aplicável de Elvis e Everton por evidências de configuração ou acesso ao serviço. Observe o recebimento real por um responsável efetivo e a negação de acesso a uma pessoa não autorizada. Não são necessárias notificações ou respostas duplicadas nem uma passagem de atendimento simulada. Uma falha real de acesso ou recebimento permanece pendente; registre uma passagem real quando necessária. Não presuma entrega de notificações pela atribuição, envie outro relato automaticamente ou use credenciais de outra pessoa. Mantenha identificadores e conteúdo restritos. Verifique novamente após mudanças de visibilidade ou público; nunca use vulnerabilidades reais nesse teste.

Controles, ativação de canais, permissões e mensagens exigem autorização específica. Uma alternativa documental não completa a verificação da rota. Cada produto verifica seu escopo. Veja [Security](../../../standards/core/security.md), [resolução atual das pendências](../../handoffs/harness-publication-blockers/README.md) e [contribuição](contributing.pt.md).

[Quickstart](../quickstart.pt.md) · [Harness](../../../README.pt.md)
