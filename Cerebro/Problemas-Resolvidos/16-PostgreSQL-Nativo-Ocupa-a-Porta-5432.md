---
tags: [problema-resolvido, docker, postgresql, ambiente, windows, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# PostgreSQL nativo do Windows ocupando a porta do container

## Contexto

[[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] · PostgreSQL 16 em Docker · Windows com PostgreSQL também instalado nativamente.

## Sintoma e impacto

O app rodando no host **conectava no banco errado**. As migrations do Prisma não batiam, e as consultas se comportavam como se o banco estivesse vazio — sem erro de conexão, o que tornava o diagnóstico mais difícil.

## Causa-raiz

Havia **um PostgreSQL nativo instalado no Windows**, já escutando em `5432` (IPv4). O `docker-compose.yml` mapeava o container para essa mesma porta.

Resultado: `localhost:5432` resolvia para o **Postgres do Windows**, não para o do container. O app conectava com sucesso — em um banco completamente diferente.

> Esse é o pior formato de conflito de porta: não dá erro. Dá **o banco errado**, em silêncio.

Confirmado com:

```powershell
Get-NetTCPConnection -LocalPort 5432 -State Listen |
  Select-Object LocalAddress, LocalPort, OwningProcess
```

## Correção aplicada

Mover o container para uma porta livre, em vez de desinstalar ou parar o Postgres nativo:

```yaml
# docker-compose.yml
ports:
  - "5433:5432"     # host 5433 -> container 5432
```

```
# .env
DATABASE_URL=postgresql://...@localhost:5433/...
```

O container continua usando 5432 internamente; só a porta exposta ao Windows mudou.

## Prevenção

> [!problema] Antes de mapear uma porta, veja quem já está nela
> Portas de banco de dados são as mais perigosas de colidir, porque a conexão **funciona** — você só descobre pelos dados errados.
>
> ```powershell
> Get-NetTCPConnection -LocalPort 5432 -State Listen
> ```
>
> Em máquina de desenvolvimento com serviços nativos instalados, vale adotar portas deslocadas por padrão (5433, 3307, 6380) para os containers.

## Links relacionados

- Projeto: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]]
- Ambiente: [[../Ambiente/02-Portas-e-Conflitos|Portas e conflitos]]
- Tecnologia: [[../Tecnologias/04-Docker|Docker]] · [[../Tecnologias/05-Prisma-e-PostgreSQL|Prisma e PostgreSQL]]

## Perguntas de revisão

Por que o conflito de porta de banco é o mais perigoso? :: Porque a conexão funciona, só que no banco errado, sem nenhum erro.

Como descobrir quem ocupa a porta 5432 no Windows? :: Com Get-NetTCPConnection -LocalPort 5432 -State Listen.

Como resolver o conflito entre Postgres nativo e container? :: Mapeando o container para outra porta, como 5433:5432, e ajustando a DATABASE_URL.

Que portas usar nos containers numa máquina de desenvolvimento? :: Portas deslocadas por padrão, como 5433, 3307 e 6380.
