# Revisão de licenciamento e publicação

[English](licensing.md) | [Português](licensing.pt.md) | [Español](licensing.es.md)

Use este guia para preparar a revisão de um componente. A política e os termos nesta fonte privada são candidatos em implementação, não licenças adotadas nem uma release pública. O [candidato de termos (inglês)](../../licensing/harness-plugin-terms.md) teve o texto aprovado pelo responsável; consulte o [registro de aprovação (inglês)](../../governance/h01-approval.md). Ainda não está vigente; a verificação de direitos e avisos dos componentes é separada.

## Prepare

Identifique o componente, a revisão exata, público/distribuição pretendidos, material original e de terceiros, referências de direitos/autorizações e avisos. Um revisor autorizado precisa acessar as evidências reais; não copie contratos, credenciais ou dados pessoais para o pacote.

Use a [política comum (inglês)](../../../standards/core/licensing-publication.md), o [inventário de avisos (inglês)](../../licensing/harness-plugin-notices.md) e o [registro privado de revisão (inglês)](../../governance/licensing-review.md). Separe os termos da ferramenta dos termos do projeto de destino.

## Experimente uma revisão

Exemplo: um componente proposto para publicação contém um template copiado sem autorização verificada. Registre o componente/revisão e a evidência ausente, use a decisão `defer`, identifique o responsável e exija verificação antes de reconsiderar. Não suponha permissão a partir de uma URL pública ou commit.

Resultado esperado: um registro atribuível com a lacuna e a próxima ação, não aplicação de licença ou publicação. Uma superfície hipotética inteiramente revisada poderia receber recomendação `publish`, mas publicar ainda exige autorização e evidência separadas do executor.

## Resolva pendências e encaminhe

Se faltarem direitos, dependências, autoridade do revisor ou revisão completa da superfície de exportação, mantenha a decisão pendente. Histórico, tags, releases, LFS, fixtures, CI e anexos relevantes fazem parte do handoff de publicação real; uma árvore atual limpa é insuficiente.

Platform, Workspace, Discover e CRM precisam de termos/evidências de adoção próprios. A distribuição do Harness/plugin é separada. Mudar a fonte não atualiza consumidores instalados nem concede direitos. Consulte [contribuição](contributing.pt.md) para participar e [entrega pelo GitHub](github-delivery.pt.md) para o processo governado.

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
