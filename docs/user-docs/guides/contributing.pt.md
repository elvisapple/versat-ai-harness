# Contribuir com procedência clara

[English](contributing.md) | [Português](contributing.pt.md) | [Español](contributing.es.md)

O repositório do Harness é público. O material elegível de autoria da Versat está disponível sob a [licença Apache-2.0](../../../LICENSE) na raiz do repositório. O material de terceiros mantém seus próprios termos e [avisos](../../../THIRD-PARTY-NOTICES.md).

## Preparar e contribuir

1. Escolha o repositório real e leia README, AGENTS e instruções de contribuição. Suas regras prevalecem sobre padrões da organização. Outros produtos mantêm termos e rotas independentes.
2. Selecione uma issue existente ou formulário disponível de bug, funcionalidade ou manutenção. Descreva necessidade, resultado esperado e reprodução quando pertinente. Não invente números de issue ou Story.
3. Identifique material próprio/de terceiros, fontes, versões, permissões e avisos. Direitos ausentes impedem aceitação. Leia [licenciamento](licensing.pt.md); a licença da ferramenta não determina termos de material independente no destino.
4. Siga a [preparação](workspace-setup.pt.md). No checkout do Harness, use Python 3.11+, instale `requirements-validation.txt` em ambiente virtual e execute `./scripts/validate/run.sh --quality-base origin/main` na raiz. Em outros projetos, use suas verificações próprias.
5. Para contribuir com o Harness de fora da organização, faça um fork do repositório público, crie uma branch no seu fork e abra uma pull request para a branch `main` do Harness. Siga a [convenção Git](../../../standards/core/git.md). Um mantenedor pode precisar aprovar a execução do workflow antes de a CI começar. O acesso público permite ler e fazer fork do repositório. Escrita, merge e release no repositório original exigem permissões próprias.
6. Para mudanças materiais, siga os [três gates do SDD](sdd-with-codex.pt.md); solicite implementação explicitamente após aprovar Tasks. Inclua documentação mantida e verificações relevantes. Siga a [entrega](github-delivery.pt.md) para arquivo documental, revisão do PR e verificações finais, com autorização efetiva para operações remotas.

Resultado esperado: contribuição revisável com referências reais de issue/procedência e verificações observadas. Informe verificações indisponíveis; aprovação local não comprova proteção de branch nem aceitação.

## Termos de contribuição

A seção 5 da [licença Apache-2.0](../../../LICENSE) na raiz do repositório rege as contribuições enviadas intencionalmente para inclusão, salvo indicação expressa em contrário, conforme as definições da licença e eventual acordo separado. Este guia não acrescenta CLA, DCO ou cessão de propriedade intelectual. Para outros repositórios ou versões, confira os termos aplicáveis e peça esclarecimentos se eles estiverem indisponíveis.

## Revisão e recuperação

O mantenedor deve revisar escopo, procedência e verificações obrigatórias. CODEOWNERS identifica contatos técnicos, sem comprovar qualificação jurídica ou proteção ativa. Direitos ou revisão obrigatória ausentes impedem aceitação. Corrija falhas e obtenha novas evidências; mudanças de escopo reabrem o gate pertinente. Sem acesso, use a rota pública existente do destino sem o Harness quando apropriado, ou solicite instruções ao mantenedor visível sem divulgar informações confidenciais.

Não exponha vulnerabilidades em issues públicas; use [reporte de segurança](security-reporting.pt.md). Política canônica: [Contribution](../../../standards/core/contribution.md).

[Quickstart](../quickstart.pt.md) · [Harness](../../../README.pt.md)
