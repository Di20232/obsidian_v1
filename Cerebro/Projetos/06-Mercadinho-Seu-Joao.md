---
tags: [projeto, nodejs, express, prisma, banco-de-dados, docker, flashcards]
status: em-uso
cssclasses: [cerebro-nota, cerebro-projetos]
---

# Mercadinho Seu João

> [!projeto] Origem
> Registro extraído das sessões de trabalho no Claude Code. Volta para [[00-Indice|📦 Projetos]].

## O que é

Sistema de **controle de vendas e estoque** para um mercadinho (nome interno do pacote: `contro-vend`). Web, com login, painel, produtos, estoque, relatórios e usuários.

- **Pasta:** `C:\Users\Perim\Documents\proejto\mercadinho-seu-joao`
- **Repositório:** `Di20232/mercadinho-seu-joao` (branch `master`) — publicado como [`Di20232/contro-vend-public`](https://github.com/Di20232/contro-vend-public)
- **Stack:** Node.js · Express · Prisma · PostgreSQL 16 · Docker Compose

> [!projeto] Código-fonte completo
> Todo o código está catalogado, arquivo por arquivo, em [[../GitHub/contro-vend-public/00-Indice|Cerebro/GitHub/contro-vend-public]] — snapshot do commit `8ca8821`, o mesmo enviado ao fim da sessão de 08/09. A leitura de arquitetura está em [[../GitHub/contro-vend-public/01-Arquitetura-e-Aprendizados|Vendas, estoque e segurança]], com o modelo de dados em diagrama e os arquivos-chave linkados.
>
> **Divergência importante:** essa cópia pública **não contém** `src/spreadsheet.js`, `src/productImport.js` nem `src/routes/imports.js` — a aba Importar descrita abaixo não está nesse commit. Não presuma que a importação de planilhas já está na versão publicada; confira antes de dizer a alguém que ela existe lá.

## Dois jeitos de rodar — ambos no mesmo banco

| Modo | URL | Como subir |
|---|---|---|
| Docker (app + banco) | `http://localhost:3100` | `docker compose up -d` |
| Local (Node no host) | `http://localhost:3000` | `npm run dev` |

**Login inicial:** usuário `admin@example.com`. A senha padrão é criada pelo `npm run seed` e está no `.env.example` do projeto — o sistema recomenda trocá-la no primeiro acesso. *(Por política deste cofre, senhas não são registradas aqui.)*

> ⚠️ O Postgres do Docker escuta em **5433**, não 5432. Isso foi deliberado — ver [[../Problemas-Resolvidos/16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|o motivo]].

## Comandos úteis

```bash
docker compose up -d
```
```bash
docker compose logs -f app
```
```bash
docker compose exec app npm run seed:products
```
```bash
docker compose exec app npm run simulate:sales
```

## O que foi construído

### Dados de exemplo
- `seed:products` → 24 produtos (secos e molhados, validades variadas)
- `simulate:sales` → 110 vendas espalhadas em 14 dias, entre dois vendedores

Sem isso, o painel, os relatórios por dia e a previsão de esgotamento mostram só zeros.

### Aba "Importar" (só administrador)

A entrega mais substancial deste projeto. Aceita **Excel (.xlsx)**, **CSV**, **TSV** e **dados colados** direto do Excel ou Google Planilhas — mais um modelo em Excel para baixar já com as colunas certas.

O fluxo tem **4 passos e nada é gravado antes da confirmação**:
1. Escolher o arquivo (ou colar)
2. Conferir as colunas — reconhecidas sozinhas pelo cabeçalho (`EAN`, `VLR VENDA`, `QTDE`, `VENCIMENTO`), com um exemplo real embaixo de cada uma
3. Conferir linha a linha o que será feito — com preço antigo → novo e estoque antigo → novo
4. Confirmar

**Três opções controlam a aplicação:** cadastrar/atualizar/ambos · identificar por código de barras ou nome · o que fazer com a coluna de estoque (só em produtos novos, substituir saldo, ou somar).

→ O parsing brasileiro está documentado em [[../Praticas/05-Importacao-de-Planilhas|Importação de Planilhas]].

### Proteções embutidas na importação
- Toda mudança de estoque entra no **extrato de movimentações** com saldo anterior e novo — a importação não burla a auditoria
- Código de barras de outro produto é **recusado** em vez de sobrescrito ([[../Problemas-Resolvidos/20-Importacao-Renomeia-Produto-Errado|por quê]])
- Código repetido dentro do próprio arquivo é barrado
- **Cada linha grava na própria transação** — uma linha ruim não descarta as boas

**Arquivos:** `src/spreadsheet.js` (leitura) · `src/productImport.js` (colunas e aplicação) · `src/routes/imports.js` (rotas) · `public/app.html` + `public/js/app.js` (interface)

## Problemas que este projeto gerou

- [[../Problemas-Resolvidos/15-Modulo-Express-Nao-Encontrado|Cannot find module express]]
- [[../Problemas-Resolvidos/16-PostgreSQL-Nativo-Ocupa-a-Porta-5432|PostgreSQL nativo do Windows ocupando a 5432]]
- [[../Problemas-Resolvidos/17-Containers-Orfaos-em-System32|Containers órfãos rodando a partir de System32]]
- [[../Problemas-Resolvidos/18-Porta-3000-Presa-por-Processo-Orfao|Porta 3000 presa por processo órfão]]
- [[../Problemas-Resolvidos/19-Docker-Parado-Causa-Erro-500|Docker Desktop encerrado → login retorna 500]]
- [[../Problemas-Resolvidos/20-Importacao-Renomeia-Produto-Errado|Importação renomeando o produto errado]]

## Estado

✅ Rodando nos dois modos · importação completa e testada · testes de integração passando · commit `d654f21` enviado para o GitHub.

## Links relacionados

- Código-fonte: [[../GitHub/contro-vend-public/00-Indice|Todos os arquivos (GitHub)]] · [[../GitHub/contro-vend-public/01-Arquitetura-e-Aprendizados|Arquitetura e soluções reaproveitáveis]]
- Conceito cruzado com outros repositórios: [[../GitHub/Conhecimento/01-Estoque-Concorrente|Estoque concorrente]] · [[../GitHub/Conhecimento/02-Sessao-e-Permissoes|Sessão e permissões]] · [[../GitHub/Conhecimento/04-Previsao-de-Reposicao|Previsão de reposição]]

## Perguntas de revisão

Qual a stack do Mercadinho Seu João? :: Node.js, Express, Prisma, PostgreSQL 16 e Docker Compose.

Por que o Postgres do Mercadinho usa a porta 5433? :: Porque a 5432 estava ocupada pelo PostgreSQL nativo do Windows.

Por que gerar dados de exemplo no Mercadinho? :: Sem produtos e vendas simulados, painel, relatórios e previsão mostram só zeros.

Quais opções controlam a importação de produtos do Mercadinho? :: Cadastrar, atualizar ou ambos; identificar por código de barras ou nome; e como tratar a coluna de estoque.
