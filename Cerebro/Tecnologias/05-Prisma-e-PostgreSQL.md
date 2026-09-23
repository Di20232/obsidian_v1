---
tags: [tecnologia, prisma, postgresql, banco-de-dados, nodejs, flashcards]
cssclasses: [cerebro-nota, cerebro-dados]
---

# Prisma e PostgreSQL

Camada de acesso a dados do [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]]. O Prisma é um ORM que gera um cliente tipado a partir de um schema declarativo.

## O essencial do fluxo

```bash
npx prisma migrate status
```
```bash
npx prisma migrate deploy
```

O **Prisma Client é gerado** no `npm install` — por isso rodar o projeto no host exige `npm install` mesmo quando o Docker já funciona. → [[../Problemas-Resolvidos/15-Modulo-Express-Nao-Encontrado|caso real]]

## A configuração que resolveu o conflito de porta

```
DATABASE_URL=postgresql://postgres:SENHA@localhost:5433/contro_vend?schema=public
```

A porta **5433** não é arbitrária: a 5432 estava ocupada pelo PostgreSQL nativo do Windows. → [[../Problemas-Resolvidos/16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|por quê]]

## Banco separado para testes

Os testes de integração rodam contra um banco próprio, passando a URL na hora:

```bash
DATABASE_URL="postgresql://...@localhost:5433/contro_vend_test?schema=public" npm test
```

Antes, aplicar as migrations nesse banco com `migrate deploy`. Isso mantém os testes reais (banco de verdade, não mock) sem tocar nos dados de desenvolvimento.

## Verificações úteis

```bash
docker compose exec db psql -U postgres -c "\l"
```

> [!dados] Sobre credenciais
> O `.env` fica **fora do Git** (`.gitignore`). Guarde neste cofre apenas o **nome** da variável e onde obtê-la — nunca o valor. A senha do ambiente local vale o mesmo cuidado, porque hábito ruim viaja para produção.

## Links relacionados

- Projeto: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]]
- Tecnologia: [[04-Docker|Docker]]
- Trilha: [[../../MySQL/00-Indice|MySQL]] (conceitos de SQL relacional aplicáveis)

## Perguntas de revisão

O que é o Prisma? :: Um ORM que gera um cliente tipado a partir de um schema declarativo.

Quando o Prisma Client é gerado? :: No npm install; por isso rodar no host exige npm install mesmo com o Docker funcionando.

Como rodar testes de integração sem tocar nos dados de desenvolvimento? :: Usando um banco de teste separado, passando a DATABASE_URL dele e aplicando as migrations nele.

Quais comandos verificam e aplicam migrations do Prisma? :: npx prisma migrate status e npx prisma migrate deploy.
