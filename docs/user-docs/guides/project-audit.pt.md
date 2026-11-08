# Auditar um projeto

[English](project-audit.md) | [Português](project-audit.pt.md) | [Español](project-audit.es.md)

Use uma auditoria para avaliar conformidade, prontidão ou divergências. Prepare instruções, .versat/project.yaml, .versat/standards.lock, especificações ativas e o provedor selecionado. Isso é mais amplo que uma revisão comum de código.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $project-audit para avaliar este repositório conforme o perfil declarado e os Standards resolvidos. Informe evidências, gravidade e opções de correção. Não altere arquivos.
```

## Resultado esperado

Espere achados que distingam conformidade verificada, não conformidade e verificação indisponível, com contratos afetados e próximos passos concretos. A validação determinística fornece evidência limitada; a revisão qualitativa também considera segurança, testes/evals, documentação, operações e perfil/criticidade.

## Recuperação e limites

Identidade ou contexto do provedor ausentes são lacunas explícitas, não evidência de conformidade. Pedir auditoria não autoriza correção. Use manutenção ou uma mudança SDD para tratar achados aprovados.

## Referências

- [Skill (inglês)](../../../skills/project-audit/SKILL.md)
- [Standards index (inglês)](../../../standards/index.yaml)
- [Validators (inglês)](../../../validators/README.md)

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
