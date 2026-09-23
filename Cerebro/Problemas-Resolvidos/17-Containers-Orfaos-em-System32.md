---
tags: [problema-resolvido, docker, ambiente, windows, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Containers órfãos rodando a partir de System32

## Contexto

[[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] · primeira sessão de setup do projeto.

## Sintoma e impacto

Ao começar o setup, descobrimos que **já existiam containers do mesmo projeto rodando** — `contro-vend-public-app-1` e `contro-vend-public-db-1`, no ar havia dias, respondendo em `http://localhost:3100`.

O problema: o `docker-compose.yml` deles não estava na pasta do repositório. Estava em:

```
C:\Windows\System32\contro-vend-public\
```

## Causa-raiz

Uma sessão anterior executou `docker compose up` a partir do diretório errado. Quando um terminal abre com `C:\Windows\System32` como diretório atual — o que acontece com alguns atalhos e terminais elevados no Windows — qualquer comando relativo cria arquivos ali.

O Docker Compose nomeia o projeto pela **pasta em que o arquivo está**. Daí o nome `contro-vend-public` e a existência de um segundo conjunto de containers, invisível para quem olhasse só o repositório.

## Correção aplicada

1. Parar e remover os containers órfãos, com autorização do usuário:

```bash
docker compose down -v
```

2. Tentar apagar a pasta em System32 — **negado por falta de permissão de administrador**. Ficou inerte (sem containers), mas ainda existe no disco.

3. Seguir o setup a partir da pasta correta do repositório.

## Pendência

> [!problema] Ainda no disco
> A pasta `C:\Windows\System32\contro-vend-public\` continua lá, sem containers associados. Para removê-la é preciso um terminal **como administrador**. Não é urgente, mas é sujeira em um diretório do sistema.

## Prevenção

> [!problema] Sempre confirme o diretório antes de subir containers
> `docker compose` age sobre o diretório atual e usa o nome dele como nome do projeto. Um `pwd` antes de `docker compose up` custa nada.
>
> Sinal de alerta útil: `docker ps -a` mostrando containers com nome que você não reconhece. Vale investigar de onde vieram com:
> ```bash
> docker inspect NOME --format "{{.Config.Labels}}"
> ```

## Links relacionados

- Projeto: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]]
- Tecnologia: [[../Tecnologias/04-Docker|Docker]]
- Ambiente: [[../Ambiente/01-Maquina-Windows|Máquina Windows]]

## Perguntas de revisão

Como o Docker Compose nomeia o projeto? :: Pelo nome da pasta onde está o docker-compose.yml.

Por que containers podem aparecer a partir de C:\Windows\System32? :: Porque alguns terminais abrem nessa pasta, e um docker compose up rodado ali cria o projeto nela.

O que fazer antes de rodar docker compose up? :: Conferir a pasta atual com pwd.

Como investigar de onde veio um container desconhecido? :: Com docker inspect NOME --format "{{.Config.Labels}}".
