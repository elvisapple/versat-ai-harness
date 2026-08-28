# Versat AI Harness

Este repositório é a fonte de verdade para os padrões e workflows de desenvolvimento assistido por IA da Versat.

## Regras obrigatórias

- Leia `docs/architecture/overview.md` e os ADRs relacionados antes de alterar limites arquiteturais.
- Não duplique padrões dentro de Skills. Skills devem localizar e aplicar os documentos canônicos de `standards/`.
- Mantenha separadas as responsabilidades: `plugin/versat-ai-harness/` define capacidades, `standards/` define políticas, `sdd/` define o processo e `validators/` define enforcement determinístico.
- Trate alterações de política corporativa como mudanças governadas: branch, Pull Request e revisão obrigatória.
- Use o índice `standards/index.yaml` para resolver contexto; não codifique listas paralelas de padrões nas Skills.
- Preserve a composição dos templates. Um perfil estende `base` em vez de copiar seus arquivos.
- Não atualize consumidores silenciosamente para `latest`. Releases devem ser versionadas semanticamente e consumidas por referência exata.
- Registre decisões arquiteturais significativas em `docs/decisions/`.
- Execute `./scripts/validate/run.sh` antes de concluir uma mudança.

## Idiomas

- Código, identificadores, APIs, objetos de banco, commits e nomes técnicos: inglês.
- Especificações, requisitos, decisões e documentação de negócio: espanhol.
- Este repositório de bootstrap foi consolidado em português a partir do projeto Architecture. Novas especificações normativas devem seguir `standards/core/language.md`.

## Autoridade

Orientações de LLM ajudam a produzir resultados aderentes, mas não substituem validação mecânica, revisão humana, GitHub Rulesets ou checks obrigatórios.
