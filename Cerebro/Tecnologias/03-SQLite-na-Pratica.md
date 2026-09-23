---
tags: [tecnologia, sqlite, banco-de-dados, python]
cssclasses: [cerebro-nota, cerebro-dados]
---

# SQLite na prática

Banco em **um único arquivo**, sem servidor. Usado no [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]], onde `controle_suprimentos.db` é o banco inteiro — backup é copiar o arquivo.

Complementa a trilha teórica: [[../../SQLite/00-Indice|SQLite]].

## Quando é a escolha certa

✅ Aplicação local, um usuário por vez, dados que cabem em um arquivo, backup simples.
❌ Várias pessoas escrevendo ao mesmo tempo — o SQLite trava o arquivo inteiro na escrita. Foi o motivo de [[../Problemas-Resolvidos/13-Acesso-Externo-ao-Localhost|expor o sistema na rede exigir mudança de arquitetura]].

## As três armadilhas que pegaram este projeto

**1. `sqlite3.Row` e colunas duplicadas.** Um JOIN em três tabelas com coluna `nome` produz três chaves `nome` — e `linha["filial"]` estoura com `IndexError`. **Toda coluna de JOIN precisa de alias.** → [[../Problemas-Resolvidos/04-Colunas-em-Branco-por-JOIN-sem-Alias|caso real]]

**2. Chave estrangeira bloqueia exclusão — e isso é correto.** Quando todos os registros têm lançamentos vinculados, *nada* pode ser apagado. O sistema precisa **dizer isso ao usuário**, com a opção de cascata como escolha explícita. → [[../Problemas-Resolvidos/05-Exclusao-Nao-Funciona-em-Cadastros|caso real]]

**3. Identificador não pode ser parametrizado.** `?` protege **valores**, não nomes de tabela ou coluna. Para esses, use **lista de permissão fechada**. O SQLite recusar múltiplos comandos num `execute()` é mitigação acidental, não proteção. → [[../Problemas-Resolvidos/09-Nome-de-Tabela-em-F-String-no-SQL|caso real]]

## Padrões que funcionaram

```python
TABELAS_VALIDAS = {"filiais", "departamentos", "itens", "entradas", "despachos"}
```

- Conexão sempre com `try/finally` — fechar mesmo quando dá erro
- Capturar `sqlite3.IntegrityError` de forma específica, não `except Exception`
- Uma transação por linha em importações, para que uma linha ruim não descarte as boas

## Inspecionar o banco rapidamente

```bash
py -c "import db; r = db.ultimos_despachos(3); print(list(r[0].keys()))"
```

Imprimir as **chaves** da primeira linha é o teste de dez segundos que pega a classe inteira de bug de alias.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Trilha: [[../../SQLite/00-Indice|SQLite]]
- Mapa: [[../Mapas/02-Mapa-Dados|Mapa de Dados]]
