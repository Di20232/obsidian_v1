---
tags: [python, basico]
cssclasses: [cerebro-nota, cerebro-python]
---

# Estruturas Condicionais (if / elif / else)

## O problema que isso resolve

Até aqui, todo programa que você escreveu executa **todas** as linhas, sempre, na ordem. Programas reais precisam **decidir** o que fazer dependendo da situação: "se a pessoa for maior de idade, deixe entrar; senão, negue". Condicionais são o mecanismo de decisão do Python.

## Sintaxe básica

```python
idade = 20

if idade >= 18:
    print("Pode entrar")
```

Desmontando:
- `if` seguido de uma condição (uma expressão que resulta em `True` ou `False`, como visto em [[05-Operadores]]).
- **dois-pontos `:`** no final da linha — obrigatório, marca "aqui começa o bloco".
- A linha seguinte, **indentada com 4 espaços**, é o que roda **somente se** a condição for `True`. Essa é a mesma regra de indentação mencionada em [[03-Primeiro-Programa]], agora com um uso concreto.

## if / else

```python
idade = 15

if idade >= 18:
    print("Pode entrar")
else:
    print("Não pode entrar")
```

`else` roda quando a condição do `if` é `False`. Sempre um dos dois blocos roda, nunca os dois, nunca nenhum.

## if / elif / else

Para mais de duas possibilidades:

```python
nota = 7

if nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Reprovado")
```

`elif` é a contração de "else if" — só é checado se o `if` anterior (e os `elif` anteriores) foram falsos. O Python testa **de cima para baixo** e para no primeiro que for verdadeiro — os de baixo nem são avaliados. Por isso a ordem importa: se a primeira condição fosse `nota >= 5`, o `nota >= 9` nunca seria alcançado corretamente.

## Condições dentro de condições (aninhamento)

```python
idade = 20
tem_ingresso = True

if idade >= 18:
    if tem_ingresso:
        print("Entrada liberada")
    else:
        print("Falta o ingresso")
else:
    print("Menor de idade")
```

Repare que o segundo `if` está indentado **um nível a mais** que o primeiro — isso é o que diz ao Python que ele está "dentro" do primeiro bloco. Isso costuma ser reescrito com `and` (visto em [[05-Operadores]]) para ficar mais legível:

```python
if idade >= 18 and tem_ingresso:
    print("Entrada liberada")
else:
    print("Entrada negada")
```

## Valores "verdadeiros" e "falsos" (truthy/falsy)

Você pode usar qualquer valor em um `if`, não só comparações. Python considera **falsos**: `False`, `0`, `""` (texto vazio), `None`, listas/dicionários vazios. Todo o resto é considerado **verdadeiro**:

```python
nome = ""
if nome:
    print(f"Olá, {nome}")
else:
    print("Nome não informado")
```

## Erros comuns

- Esquecer o `:` no final da linha do `if`/`elif`/`else`.
- Indentação inconsistente (misturar espaços de formas diferentes) — o Python acusa `IndentationError`.
- Usar `=` em vez de `==` dentro da condição.

## Exercício

Escreva um programa que peça um número via `input()` (convertido com `int()`) e diga se ele é positivo, negativo ou zero. Depois, expanda para também dizer se o número é par ou ímpar (dica: use `%` de [[05-Operadores]]).

---
Veja o exemplo em `Python/exemplos/07_condicionais.py`. Próxima nota: [[08-Lacos-de-Repeticao]]
