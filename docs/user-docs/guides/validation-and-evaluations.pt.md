# Validação e avaliações

[English](validation-and-evaluations.md) | [Português](validation-and-evaluations.pt.md) | [Español](validation-and-evaluations.es.md)

Escolha a verificação conforme o repositório e o resultado: consistência do pacote Harness, suítes da aplicação consumidora ou comportamento supervisionado de Skills. Prepare Python 3.11+ e as dependências de validação do provedor; dependências da aplicação são separadas.

## Experimente

Pedido ilustrativo; substitua o ID ou forneça os dados reais do projeto:

```text
Use $versat-sdd para validar <change-id> conforme o plano aprovado. Informe evidências reais e lacunas. Não corrija arquivos do produto neste pedido somente de validação.
```

## Resultado esperado

Na raiz do Harness, `./scripts/validate/run.sh --quality-base origin/main` verifica pacote, registros SDD e regressões mantidas. Ele não executa testes da aplicação de outro projeto. Execução de consumidores e avaliação supervisionada dos guias especializados são capacidades de fonte ainda não lançadas: use um provedor exato que as contenha e siga os pré-requisitos de adoção. Suítes obrigatórias completas, execuções direcionadas e observações supervisionadas têm limites de evidência distintos.

## Recuperação e limites

Espere pass, fail ou unable-to-verify com contagens/resultados reais e entradas testadas. Preserve tentativas falhas; falta de acesso, testes vazios ou observações indisponíveis não comprovam sucesso. Avalie cada obrigação de aceitação e regressão; sucesso estrutural não comprova aceitação semântica, identidade humana nem merge remoto.

## Referências

- [Project validation (inglês)](../../guides/project-validation.md)
- [Skill evaluations (inglês)](../../guides/skill-evaluations.md)
- [SDD validation (inglês)](../../../validators/sdd/README.md)

[Início rápido](../quickstart.pt.md) · [Harness](../../../README.pt.md)
