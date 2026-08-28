# Visão arquitetural

## Propósito

O Versat AI Harness é a runtime de governança que conecta agentes, Enterprise Standards, Versat SDD, projetos locais e GitHub. O repositório é simultaneamente a fonte de verdade do produto e a unidade instalável do Plugin.

## Componentes

```text
                    VERSAT AI HARNESS
                         source of truth
                                |
          +---------------------+---------------------+
          |                     |                     |
      Standards                SDD               Validators
       (regras)             (processo)           (enforcement)
          |                     |                     |
          +---------------------+---------------------+
                                |
                        execution adapters
                                |
                +---------------+---------------+
                |               |               |
          Codex Plugin        CI/CD        ferramentas futuras
                |
         project-bootstrap
                |
         standards resolver
                |
       repositório de projeto
```

## Modelo de contexto

Cada projeto declara apenas sua identidade:

```yaml
project:
  profile: agent
  domain: finance
  criticality: high
technologies:
  - python
```

O resolver usa `standards/index.yaml` para compor:

```text
core + profile + domain + technologies + criticality
```

As versões efetivamente resolvidas são registradas em `.versat/standards.lock`. O consumidor não seleciona manualmente pacotes de normas e não segue `latest` silenciosamente.

## Ciclo de vida unificado

```text
Intent -> Proposal -> Requirements -> Design -> Tasks
       -> Implementation -> Tests/Evals -> Validation
       -> Pull Request -> Merge -> Living Specification
```

O mesmo ciclo vale para software, agente, biblioteca, automação, infraestrutura ou projeto híbrido. O perfil altera os módulos e critérios aplicáveis, não o processo corporativo.

## Governança do conhecimento

| Nível | Exemplo | Mudança permitida |
|---|---|---|
| Memória operacional | preferência contextual de um cliente | aprendizagem automática dentro dos limites de retenção |
| Skill | como preparar uma análise recorrente | proposta e aprovação humana |
| Política corporativa | segurança, linguagem, Git, `AGENTS.md` | branch, PR, revisão e checks obrigatórios |

## Distribuição e enforcement

- O Plugin distribui capacidades e instruções sob demanda.
- Snapshots versionados e lockfiles tornam a aplicação de Standards reprodutível.
- Pull Requests propagam novas releases aos repositórios consumidores.
- GitHub Rulesets e workflows reutilizáveis impõem políticas que não podem depender apenas de agentes.
- Marketplace é um canal de distribuição, não a autoridade normativa.

## Limites da versão 0.1.0

Esta versão define contratos, conteúdo basal e validação estrutural. Criação remota de repositórios, resolução de releases, configuração da organização GitHub e validadores semânticos por tecnologia ainda não fazem parte da implementação executável.
