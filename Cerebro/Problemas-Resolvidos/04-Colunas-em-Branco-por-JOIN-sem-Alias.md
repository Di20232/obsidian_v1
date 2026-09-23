---
tags: [problema-resolvido, sqlite, python, banco-de-dados]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Colunas aparecem em branco na tela por JOIN sem alias

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · Python · SQLite com `sqlite3.Row` · função `ultimos_despachos()` em `db.py`.

## Sintoma e impacto

No painel e na lista de últimos despachos, as colunas **Filial**, **Departamento** e **Item** apareciam **em branco** — as linhas existiam, os números estavam certos, mas os três nomes sumiam.

## Como reproduzir

Um SELECT com JOIN em três tabelas que têm todas uma coluna chamada `nome`:

```sql
SELECT d.id, d.data, f.nome, dp.nome, i.nome
FROM despachos d
JOIN filiais f ON ... JOIN departamentos dp ON ... JOIN itens i ON ...
```

Depois, no Python, tentar `linha["filial"]`.

## Causa-raiz

O `sqlite3.Row` nomeia cada coluna pelo nome que ela tem **no resultado**, não pela tabela de origem. Como as três se chamam `nome`, o resultado vira:

```
["id", "data", "nome", "nome", "nome"]
```

Três chaves duplicadas. A consequência é dupla e traiçoeira:

- `linha["filial"]` levanta **IndexError** — a chave simplesmente não existe;
- e onde o template acessava por índice ou tolerava a falha, o campo renderizava **vazio em vez de estourar** — por isso parecia problema de interface, não de consulta.

## Correção aplicada

Dar **alias explícito a toda coluna** em consultas com JOIN:

```sql
SELECT d.id, d.data,
       f.nome  AS filial,
       dp.nome AS departamento,
       i.nome  AS item
FROM despachos d ...
```

## Como confirmei

Rodando a consulta direto no Python e imprimindo as chaves antes e depois:

```python
import db
rows = db.ultimos_despachos(3)
print(list(rows[0].keys()))   # antes: ["id","data","nome","nome","nome"]
print(rows[0]["filial"])      # depois: funciona
```

## Prevenção

> [!problema] Regra para levar adiante
> **Toda coluna de um JOIN recebe alias.** Não é questão de estilo — com `sqlite3.Row` é correção. Vale para qualquer driver que devolva linhas acessíveis por nome.

Um teste que apenas imprime `list(row.keys())` de cada consulta com JOIN pega essa classe inteira de bug de uma vez.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Tecnologia: [[../Tecnologias/03-SQLite-na-Pratica|SQLite na prática]] · [[../../SQLite/00-Indice|Trilha SQLite]]
- Relacionado: [[05-Exclusao-Nao-Funciona-em-Cadastros|O bug que também parecia de interface]]
