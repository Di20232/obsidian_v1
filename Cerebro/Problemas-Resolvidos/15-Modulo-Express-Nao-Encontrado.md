---
tags: [problema-resolvido, nodejs, docker, ambiente]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Cannot find module express ao rodar fora do Docker

## Contexto

[[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] · Node.js · projeto que até então só havia sido executado dentro do Docker.

## Sintoma e impacto

O servidor local morria no start:

```
Error: Cannot find module "express"
Require stack:
- ...\src\app.js
- ...\src\server.js
code: "MODULE_NOT_FOUND"
```

## Causa-raiz

Simples e muito comum: **não havia `node_modules` na máquina host**.

O projeto tinha sido configurado para rodar via `docker compose`, e o `npm install` acontecia **dentro da imagem**. O container tinha todas as dependências; a pasta do Windows, nenhuma. Ao tentar `npm run dev` direto no host, o Node procurou `express` e não achou.

> É a diferença entre "o projeto está configurado" e "o projeto está configurado **neste ambiente**". São duas coisas.

## Correção aplicada

```bash
npm install
```

127 pacotes instalados e o Prisma Client gerado.

## O segundo problema, escondido atrás do primeiro

Resolver esse erro revelou outro imediatamente: com as dependências instaladas, o app subiu — e então falhou ao conectar no banco, porque havia um **PostgreSQL nativo do Windows ocupando a porta 5432**.

→ [[16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|ver o caso]]

## Prevenção

> [!problema] Rodar em Docker e rodar no host são dois setups
> Se o projeto oferece os dois modos, os dois precisam ser preparados — e documentados. Um `README` que só ensina `docker compose up` deixa o modo local quebrado à espera de quem tentar.

Depois de resolvido, o projeto ficou com os dois caminhos funcionando **contra o mesmo banco**:

| Modo | URL | Como subir |
|---|---|---|
| Docker | `http://localhost:3100` | `docker compose up -d` |
| Local | `http://localhost:3000` | `npm run dev` |

## Links relacionados

- Projeto: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]]
- Tecnologia: [[../Tecnologias/04-Docker|Docker]]
- Relacionado: [[16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|Porta 5432 ocupada]]
