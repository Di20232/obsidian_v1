---
tags: [problema-resolvido, seguranca, sql, python, sqlite, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Nome de tabela montado com f-string no SQL

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · `db.py` · funções genéricas de listar e excluir que recebiam o nome da tabela como parâmetro.

## Sintoma e impacto

Nenhum sintoma visível — foi encontrado numa auditoria de segurança pedida pelo usuário, não por uma falha em uso.

## Causa-raiz

O código montava a consulta interpolando o nome da tabela direto na string:

```python
cur.execute(f"SELECT * FROM {tabela}")     # PERIGOSO
```

O ponto importante: **parâmetros com `?` protegem valores, não identificadores.** Você não pode escrever `SELECT * FROM ?` — o nome da tabela precisa mesmo entrar na string. Por isso ele tem que ser validado antes.

O que a sondagem empírica mostrou:

- o SQLite **recusa múltiplos comandos** num único `execute()`, o que barra o clássico `DROP TABLE` — mitigação parcial e acidental;
- mas ainda assim o parâmetro permitia **ler ou remover outras tabelas** e provocar falhas controladas;
- e, mesmo sem exploração, é um **vazamento de abstração**: quem chama a função escolhe a tabela.

Classificado como **achado real de severidade alta** — não pelo estrago imediato, mas porque a única barreira era um detalhe do driver.

## Correção aplicada

Lista de permissão fechada, validada antes de qualquer consulta:

```python
TABELAS_VALIDAS = {"filiais", "departamentos", "itens", "entradas", "despachos"}

def listar(tabela):
    if tabela not in TABELAS_VALIDAS:
        raise ValueError(f"tabela invalida: {tabela}")
    ...
```

## Prevenção

> [!seguranca] A regra dos dois mundos
> **Valor** → sempre parâmetro `?`, nunca f-string.
> **Identificador** (tabela, coluna, direção de ordenação) → nunca chega cru do exterior; valide contra uma **lista de permissão fechada**.
>
> Se você precisa interpolar, o dado tem que vir de um conjunto que *você* definiu no código — não de quem chama.

O mesmo padrão apareceu no [[21-SQL-Injection-por-Token-de-URL|Projeto W]], por um caminho diferente. Vale procurar `f"SELECT` e `f"DROP` em qualquer projeto.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Prática: [[../Praticas/07-Seguranca-em-Apps-Locais|Segurança em apps locais]]
- Relacionado: [[21-SQL-Injection-por-Token-de-URL|O mesmo erro no Projeto W]]
- Trilha: [[../../Seguranca-Web/09-Injecao-SQL-e-Comandos|Injeção de SQL e comandos]]

## Perguntas de revisão

O parâmetro ? protege nomes de tabela? :: Não; protege só valores. Identificadores como tabela ou coluna não podem ser parâmetros.

Como usar com segurança um nome de tabela variável? :: Validando contra uma lista de permissão fechada definida no código.

Qual a regra dos dois mundos no SQL? :: Valor sempre como parâmetro ?; identificador nunca cru de fora, sempre validado por lista de permissão.

O que procurar num projeto para achar esse tipo de falha? :: Trechos com f"SELECT e f"DROP.
