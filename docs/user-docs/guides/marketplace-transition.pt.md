# Transição do marketplace

[English](marketplace-transition.md) | [Português](marketplace-transition.pt.md) | [Español](marketplace-transition.es.md)

A candidata local 0.4.0 muda o catálogo para `versat` / `Versat Plugins`. O plugin continua `versat-ai-harness`; a chave local pretendida é `versat-ai-harness@versat`. A chave legada `versat-ai-harness@versat-internal` não é um alias automático. Preparação do código não equivale a integração, release ou instalação. A tag exata `v0.4.0` ainda não existia em 19/11/2026.

## Entrega do código no escopo aprovado

O proprietário informa que somente Elvis e Everton usam o Harness, que o catálogo gerenciado acompanha `main` e que ambos reinstalarão manualmente depois. É um escopo informado, não auditoria de membros ou resultado de instalação de qualquer um deles. A decisão aprovada dispensa pin/pausa prévia do workspace e ensaio nativo descartável antes da entrega do código. A sincronização pode expor o catálogo alterado antes da reinstalação, causar interrupção temporária ou exigir reparo manual. Source/Path/sync e IDs gerenciados continuam não verificados. Se outro usuário afetado for identificado, interrompa a ativação e reavalie o escopo.

A aceitação do código exige verificações determinísticas do pacote, suítes mantidas completas e documentação fiel. A integração futura continua exigindo CI aprovada e aprovação elegível de CODEOWNER que não abriu a PR, na revisão efetiva. Revise as mudanças desde a base registrada antes da submissão. Aceitação local não dispensa esses controles. Tag/release exige autorização separada; confira novamente a disponibilidade de v0.4.0 e nunca recrie uma tag existente.

## Reinstalação manual posterior

Leia [configuração do workspace](workspace-setup.pt.md) e [notas da candidata](../../releases/0.4.0-candidate.pt.md). Elvis e Everton farão suas próprias reinstalações depois. Esta preparação do código não instala, altera o workspace ou migra consumidores.

1. Registre a referência do catálogo separadamente da referência exata do pacote, identidade/versão, provedor efetivo e lock/snapshots compatíveis do projeto. Guarde caminhos privados e IDs gerenciados em evidência restrita, sem credenciais. As observações anteriores de 0.4.0 pessoal e 0.3.0 em cache gerenciado não demonstram o provedor efetivo de uma nova sessão.
2. Confirme um pacote exato disponível e suportado e seus recursos canônicos antes de instalar. Um catálogo que seleciona tag inexistente não basta; a main selecionando v0.4.0 ainda não lançada não é um par de recuperação verificado. Preserve um registro compatível de origem/pacote/projeto. Nunca selecione `latest` silenciosamente nem reduza SDD v3 ativo a provedor incompatível.
3. Confira os controles/ajuda suportados no cliente instalado para registro, seleção de identidade e recuperação. Comandos da transição, registro com a mesma URL Git, colisão de nomes e continuidade da identidade gerenciada não estão verificados. Comandos legados históricos não são instruções atuais. Pare se a rota necessária não for suportada ou exigir administrador; delimite essa ação concreta separadamente.
4. Após reinstalar de fato, registre identidade e versão exatas retornadas e confirme um único provedor efetivo pretendido. Em projeto sintético, peça a esse provedor para localizar as cinco Skills e seus recursos canônicos correspondentes; depois use `versat-sdd` para preparar uma pequena Proposal/Requirements sem implementação. Resultado esperado: rascunho do provedor correspondente, parado no gate de planejamento, ou pré-requisito/falha explícito. Esta ação representativa não foi executada aqui.
5. Registre separadamente os resultados de Elvis e Everton: identidade, versão exata, provedor/recursos efetivos, resultado da Skill e erro/recuperação. A aceitação do código ou o resultado de uma pessoa não comprova o sucesso da outra.

## Falha e recuperação

Diante de referência indisponível, colisão, provedores ambíguos, recursos ausentes ou runtime incompatível, interrompa a instalação afetada. Preserve ou selecione novamente um par provedor/projeto compatível e verificado pelos controles suportados; registre recuperação ou falha não resolvida. Se não houver recuperação compatível verificada, mantenha a pendência. Não renomeie caches, edite bancos de instalação, copie credenciais, altere locks como efeito colateral ou use `pluginId` ou exclusão/reimportação como solução genérica.

Mudanças de importação/ref/política do workspace, exclusão gerenciada e instalações automatizadas exigem autoridade própria. Identidade local não comprova compartilhamento, funções ou continuidade de IDs gerenciados. A limpeza legada é opcional e posterior, sob autoridade do proprietário/admin, após verificar dependências e recuperação; excluir um marketplace somente para renomeá-lo não faz parte deste handoff.

## Observações adiadas

O [registro de pendências](../../validation/harness-marketplace-transition/inputs/transition-r2.json) mantém sete cenários nativos não verificados: descoberta/recursos novos; legado preservado; mesma URL Git; colisão de nomes; dois provedores/um efetivo; referência exata indisponível; recuperação de falha. A reinstalação posterior registra apenas cenários realmente observados, sem exigir simulação dos sete antes da entrega do código. Nenhuma VM, contêiner ou conta de teste é provisionada aqui; fixtures descartáveis verificam caminhos do pacote, não isolamento de segurança ou execução nativa.

Fork/CI externo, recebimento/confidencialidade de relatos privados e instalação/atualização/recuperação nativa externa continuam pendentes de forma independente. Validação local, arquivamento documental e merge não encerram essas observações.
