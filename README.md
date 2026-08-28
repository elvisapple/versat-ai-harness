# Versat AI Harness

Fonte de verdade da Versat para desenvolvimento assistido por IA. Este repositório reúne padrões corporativos, o processo de Spec Driven Development (SDD), capacidades distribuídas como Plugin, templates de projetos e validações determinísticas.

## Princípios

- o repositório define as políticas;
- as Skills fornecem capacidades reutilizáveis;
- o SDD define o processo de mudança;
- validadores e GitHub aplicam as regras que precisam de enforcement;
- memória operacional, Skills e políticas possuem níveis de governança distintos;
- um único bootstrap atende software, agentes, projetos híbridos, bibliotecas e infraestrutura.

## Mapa do repositório

| Caminho | Responsabilidade |
|---|---|
| `plugin/versat-ai-harness/` | Pacote instalável com as capacidades do Harness |
| `standards/` | Quais regras corporativas devem ser obedecidas |
| `sdd/` | Como mudanças são especificadas, implementadas e arquivadas |
| `project-templates/` | Estruturas compostas usadas no nascimento de projetos |
| `validators/` | Contratos de validação determinística |
| `scripts/` | Entradas operacionais para bootstrap, validação e release |
| `schemas/` | Contratos dos metadados do Harness |
| `resources/` | Conhecimento institucional verificado, não normativo |
| `docs/architecture/` | Visão arquitetural vigente |
| `docs/decisions/` | Architecture Decision Records (ADRs) |

## Estado inicial

Esta versão materializa a arquitetura e os contratos iniciais. As Skills, padrões, schemas, templates e o pipeline mínimo de validação já são versionados; integrações externas e validadores específicos por tecnologia serão implementados incrementalmente via SDD.

## Validação local

```bash
./scripts/validate/run.sh
```

## Evolução

Toda mudança relevante começa por uma proposta SDD e, quando altera uma decisão estrutural, por um ADR. Consulte `AGENTS.md`, `sdd/process.md` e `docs/decisions/README.md` antes de modificar o Harness.
