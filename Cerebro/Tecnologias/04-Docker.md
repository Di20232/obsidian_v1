---
tags: [tecnologia, docker, ambiente, containers]
cssclasses: [cerebro-nota, cerebro-engenharia]
---

# Docker na prática

Usado no [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] (app + PostgreSQL) e no [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]] (Streamlit).

## Comandos do dia a dia

```bash
docker compose up -d
```
```bash
docker compose ps
```
```bash
docker compose logs -f app
```
```bash
docker compose down
```

## As quatro armadilhas que custaram tempo aqui

**1. Rodar a partir do diretório errado.** O Compose nomeia o projeto pela pasta onde está o arquivo. Um `docker compose up` executado de `C:\Windows\System32` criou containers órfãos que ficaram dias no ar sem ninguém notar. **Confirme o diretório antes.** → [[../Problemas-Resolvidos/17-Containers-Orfaos-em-System32|caso real]]

**2. Colidir com serviço nativo do Windows.** Um PostgreSQL instalado na máquina ocupava a 5432, e `localhost:5432` resolvia para ele — o app conectava **no banco errado, sem erro**. Solução: expor o container em porta deslocada (`5433:5432`). → [[../Problemas-Resolvidos/16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|caso real]]

**3. Docker Desktop fechado derruba o banco silenciosamente.** O app continua servindo páginas e só quebra nas rotas que precisam de dados — erro 500. → [[../Problemas-Resolvidos/19-Docker-Parado-Causa-Erro-500|caso real]]

**4. Git Bash converte caminhos destinados ao container.** `/tmp/x.py` vira `C:/Program Files/Git/tmp/x.py`. Prefixe com `MSYS_NO_PATHCONV=1`. → [[../Problemas-Resolvidos/23-Docker-Exec-no-Git-Bash-do-Windows|caso real]]

## Padrões que funcionaram

**Volume nomeado para dados.** Foi o que garantiu que os dados sobrevivessem ao container ser parado e recriado.

**Migrations no start do container.** No Mercadinho, o Prisma roda as migrations automaticamente ao subir — não há passo manual esquecível.

**Dois modos contra o mesmo banco.** Expor a porta do banco ao host permite rodar o app em Docker *ou* direto no host, sempre contra os mesmos dados.

**Copiar arquivo para dentro do container** (sem problema de conversão de caminho):

```bash
docker cp script.py nome-do-container:/tmp/script.py
```

## Links relacionados

- Projetos: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho]] · [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]]
- Ambiente: [[../Ambiente/02-Portas-e-Conflitos|Portas e conflitos]]
- Mapa: [[../Mapas/03-Mapa-Engenharia|Engenharia de Software]]
