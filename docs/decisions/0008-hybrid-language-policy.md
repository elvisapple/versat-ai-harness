# ADR-0008 — Adotar política híbrida de idiomas

- Status: Accepted
- Data: 2026-08-28

## Contexto

A equipe precisa combinar interoperabilidade técnica internacional com documentação de produto acessível ao contexto corporativo.

## Decisão

Usar inglês em código, identificadores, APIs, banco de dados, nomes técnicos e commits. Usar espanhol em especificações, requisitos, decisões e documentação de negócio. Conteúdo de interface segue o locale do produto.

## Consequências

- validadores devem distinguir artefatos técnicos de documentos de negócio;
- termos consagrados podem permanecer no idioma técnico quando tradução reduzir precisão;
- exceções devem ser registradas no documento canônico de linguagem.
