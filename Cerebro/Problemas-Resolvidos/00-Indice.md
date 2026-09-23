---
tags: [moc, problemas-resolvidos, debugging]
aliases: [Problemas Resolvidos]
cssclasses: [cerebro-nota, cerebro-problemas]
---

# 🔧 Problemas Resolvidos

Este é o histórico que converte horas de investigação em atalhos confiáveis para o futuro. Cada nota segue **sintoma → causa-raiz → correção → prevenção**.

Volta para [[../00-Cerebro|🧠 Cérebro]].

## Registrar um novo caso

Use [[../Templates/Template-Problema|Template de Problema]] depois de confirmar a correção. Não registre segredos, dados pessoais, tokens ou dados de produção.

## Ambiente e sistema

| # | Caso | Sinal para reconhecer |
|---|---|---|
| 01 | [[01-Caminho-SMB-nao-encontrado\|Caminho de rede não encontrado (0x80070035)]] | Erro ao acessar pasta compartilhada |
| 03 | [[03-Falha-de-Impressao-e-Spooler\|Falha de impressão e Spooler]] | Fila travada, nada imprime |
| 12 | [[12-Conexao-Recusada-no-Localhost\|ERR_CONNECTION_REFUSED no localhost]] | Nada escutando na porta |
| 13 | [[13-Acesso-Externo-ao-Localhost\|Outra pessoa acessar meu localhost]] | Link copiado não funciona para o colega |
| 17 | [[17-Containers-Orfaos-em-System32\|Containers órfãos em System32]] | `docker ps` mostra containers que você não subiu |
| 18 | [[18-Porta-3000-Presa-por-Processo-Orfao\|Porta presa por processo órfão]] | Porta em uso por processo sem dono |
| 24 | [[24-Push-403-com-Conta-Git-Errada\|Push 403 por conta Git errada]] | Permissão negada com credencial válida |

## Docker e banco de dados

| # | Caso | Sinal para reconhecer |
|---|---|---|
| 16 | [[16-PostgreSQL-Nativo-Ocupa-a-Porta-5432\|PostgreSQL nativo ocupa a 5432]] | ⚠️ Conecta sem erro, **no banco errado** |
| 19 | [[19-Docker-Parado-Causa-Erro-500\|Docker parado causa erro 500]] | Tela abre, ações falham |
| 15 | [[15-Modulo-Express-Nao-Encontrado\|Módulo express não encontrado]] | `MODULE_NOT_FOUND` fora do Docker |
| 23 | [[23-Docker-Exec-no-Git-Bash-do-Windows\|docker exec quebra caminhos no Git Bash]] | Caminho vira `C:/Program Files/Git/...` |
| 04 | [[04-Colunas-em-Branco-por-JOIN-sem-Alias\|Colunas em branco por JOIN sem alias]] | Dados existem, campos aparecem vazios |

## Interface e framework reativo

| # | Caso | Sinal para reconhecer |
|---|---|---|
| 05 | [[05-Exclusao-Nao-Funciona-em-Cadastros\|Excluir dá refresh e não exclui]] | ⭐ Três causas diferentes no mesmo sintoma |
| 06 | [[06-Selects-Reflex-Nao-Enviam-Valor\|Selects não enviam o valor]] | Formulário grava vazio ou não grava |
| 07 | [[07-Operadores-Python-em-Var-do-Reflex\|Operadores Python quebram em Var]] | Página não compila |
| 08 | [[08-Toast-Invisivel-com-Classes-Tailwind\|Toast invisível]] | Elemento no DOM, invisível na tela |
| 10 | [[10-Selects-Cinza-com-Texto-Invisivel\|Selects cinza com texto invisível]] | Não dá para ler o que foi selecionado |

## Dados e regras de negócio

| # | Caso | Sinal para reconhecer |
|---|---|---|
| 11 | [[11-Saldo-Geral-Misturando-Unidades\|Saldo somando litros com unidades]] | Total que não significa nada |
| 20 | [[20-Importacao-Renomeia-Produto-Errado\|Importação renomeia o produto errado]] | Registro sobrescrito sem aviso |

## Segurança

| # | Caso | Severidade |
|---|---|---|
| 09 | [[09-Nome-de-Tabela-em-F-String-no-SQL\|Nome de tabela em f-string no SQL]] | Alta |
| 21 | [[21-SQL-Injection-por-Token-de-URL\|SQL injection por token de URL]] | Média (latente) |
| 22 | [[22-Decompression-Bomb-em-XLSX\|Decompression bomb em .xlsx]] | Baixa/média (DoS) |

## Ferramentas e processo

| # | Caso |
|---|---|
| 02 | [[02-Repositorio-nao-e-Marketplace\|Repositório selecionado não é um marketplace]] |
| 14 | [[14-Workflows-Massivos-Falham-em-Arquivos-Grandes\|Workflows massivos falham em arquivos grandes]] |

## Os padrões que atravessam vários casos

> [!problema] Quatro lições que se repetem
> 1. **Falha silenciosa é a mais cara.** Conectar no banco errado, sobrescrever o produto errado, aviso invisível — todos custaram mais que qualquer erro explícito.
> 2. **O sintoma quase nunca é a causa.** O caso 05 teve três causas sucessivas, cada uma parecendo definitiva.
> 3. **Metade dos bugs é de ambiente, não de código.** Porta, container, dependência, credencial.
> 4. **Evidência executada encerra a discussão.** Contar linhas travadas por chave estrangeira leva trinta segundos e substitui uma hora de teoria.

## Navegação

- [[../Guias/02-Resolver-Problemas|Guia para Resolver Problemas]]
- [[../Praticas/06-Caca-de-Bugs|Prática: Caça de bugs]]
- [[../../Programacao-Geral/12-Debugging-e-Testes|Debugging e Testes]]
- [[../Tecnologias/00-Indice|Tecnologias]]
