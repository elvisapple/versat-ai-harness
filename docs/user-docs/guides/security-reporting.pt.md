# Relate uma preocupação de segurança com cuidado

[English](security-reporting.md) | [Português](security-reporting.pt.md) | [Español](security-reporting.es.md)

Estado atual do candidato H02: **o responsável indicou um destino, mas nenhuma rota confidencial foi verificada neste trabalho**. Nenhum canal foi ativado e nenhum teste/relato foi enviado. Este guia não promete prazo de resposta nem monitoramento contínuo.

Os CODEOWNERS relevantes são responsáveis por acompanhar, triar e coordenar a resolução dos relatos de segurança dos componentes sob sua responsabilidade, tanto pelo PVR dos repositórios públicos quanto pelo email interno dos privados. Os mantenedores configuram as permissões e notificações necessárias; a atribuição em CODEOWNERS não configura sozinha o recebimento no GitHub.

## Encaminhamento escolhido — candidato privado

Para bugs comuns, use Bug report. Para suspeitas de vulnerabilidade em repositórios públicos, use o Private Vulnerability Reporting do GitHub quando habilitado. Nos privados, envie email aos CODEOWNERS relevantes pelos canais internos existentes da Versat. Não divulgue detalhes de vulnerabilidade em issues comuns. Consulte [reporte de segurança](../../handoffs/contribution-security-guidance/organization/candidate/SECURITY.pt.md) para encaminhamento e recuperação quando o canal estiver indisponível.

## Antes de compartilhar detalhes

Leia as instruções reais de segurança do repositório de destino e confirme seu escopo. O nome de um mantenedor ou um link acessível com autenticação não comprova uma rota confidencial. Não coloque detalhes de exploração, credenciais, dados de clientes ou anexos sensíveis em uma issue pública.

## Quando não houver rota verificada

Use um contato existente e visível do repositório/mantenedor apenas para solicitar instruções de reporte privado, sem revelar a vulnerabilidade. Exemplo seguro: “Preciso de instruções confidenciais de reporte de segurança para este repositório.” Aguarde uma rota adequada antes de enviar detalhes sensíveis. Este exemplo não envia mensagem nem autoriza um agente a fazê-lo.

Resultado esperado: um pedido não sensível de instruções, não um relato verificado ou serviço ativo. Se não conseguir estabelecer uma rota adequada, mantenha o relato privado e a lacuna de verificação explícita.

## O que uma rota verificada deve comprovar

Devem ser registrados destino real, responsável pelo recebimento, público autorizado a reportar, destinatários/limite de acesso e tratamento de dados aprovado pelo responsável. Observações de configuração/acesso e marcador sintético não sensível com recebimento, explicitamente autorizado, devem sustentar qualquer afirmação de verificação. Não suponha acesso público a partir de uma sessão administrativa.

O [registro privado da rota (inglês)](../../governance/security-reporting.md) lista as pendências. Orientação alternativa sem canal verificado não conclui H02. Uma rota alterada ou com falha exige nova verificação e retirada de afirmações de atividade sem suporte.

Regras canônicas: [Security (inglês)](../../../standards/core/security.md). Configuração de canal, alteração de permissões e mensagens de teste exigem autorização específica separada. Cada produto verifica seu próprio escopo adotado.

[Contribuição](contributing.pt.md) · [Harness](../../../README.pt.md)
