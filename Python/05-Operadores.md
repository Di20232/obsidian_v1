---
tags: [python, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Operadores

## O que são

Operadores são símbolos que fazem uma operação entre valores: somar, comparar, combinar condições. Você já usou um operador em [[04-Variaveis-e-Tipos]]: o `=` de atribuição.

## Operadores aritméticos

```python
soma = 10 + 3        # 13
sub = 10 - 3         # 7
mult = 10 * 3        # 30
div = 10 / 3         # 3.3333... (divisão sempre retorna float)
div_inteira = 10 // 3  # 3 (descarta o resto — divisão inteira)
resto = 10 % 3       # 1 (resto da divisão, chamado de "módulo")
pot = 10 ** 2        # 100 (potência)
```

**Por que `//` e `%` existem**: são úteis para problemas do dia a dia como "quantas caixas de 6 ovos preciso" (`//`) e "quantos ovos sobram soltos" (`%`). São operações muito comuns em lógica de programação, por isso ganham símbolo próprio.

## Operadores de comparação

Retornam sempre `True` ou `False` (tipo `bool`, visto em [[04-Variaveis-e-Tipos]]):

```python
5 == 5   # True  -> igual a
5 != 3   # True  -> diferente de
5 > 3    # True  -> maior que
5 < 3    # False -> menor que
5 >= 5   # True  -> maior ou igual
5 <= 4   # False -> menor ou igual
```

**Atenção, o erro mais comum de iniciante**: `=` atribui, `==` compara. `if idade = 18` é erro de sintaxe; o correto é `if idade == 18`.

## Operadores lógicos

Combinam condições (mais detalhes de uso em [[07-Condicionais]]):

```python
idade = 20
tem_carteira = True

idade >= 18 and tem_carteira   # True somente se AMBAS forem verdadeiras
idade >= 18 or tem_carteira    # True se PELO MENOS UMA for verdadeira
not tem_carteira               # inverte: True vira False e vice-versa
```

- `and`: verdadeiro só quando os dois lados são verdadeiros.
- `or`: verdadeiro quando pelo menos um lado é verdadeiro.
- `not`: inverte o valor.

## Operadores de atribuição compostos

Atalhos para "pegar o valor atual, operar, e guardar de novo":

```python
contador = 10
contador += 1   # equivalente a: contador = contador + 1  -> 11
contador -= 2   # contador = contador - 2  -> 9
contador *= 3   # contador = contador * 3  -> 27
contador /= 3   # contador = contador / 3  -> 9.0
```

Isso é extremamente comum em loops (ver [[08-Lacos-de-Repeticao]]), por exemplo para contar quantas vezes algo aconteceu.

## Precedência (ordem das operações)

Python segue a mesma ordem da matemática: parênteses primeiro, depois potência, depois multiplicação/divisão, depois soma/subtração. Na dúvida, **use parênteses** para deixar explícito — isso não é "para iniciante", profissionais fazem isso o tempo todo para evitar ambiguidade:

```python
resultado = 2 + 3 * 4      # 14 (multiplicação primeiro)
resultado = (2 + 3) * 4    # 20 (parênteses primeiro)
```

## Exercício

Calcule, usando variáveis, quantas semanas completas e quantos dias sobram em 100 dias (dica: use `//` e `%`). Depois escreva uma condição que verifique se uma pessoa pode dirigir (`idade >= 18`) **e** tem CNH (`tem_cnh == True`), guardando o resultado em uma variável `pode_dirigir` e imprimindo-a.

## Perguntas de revisão

Qual a diferença entre / e // em Python? :: / faz divisão e sempre retorna float; // faz divisão inteira, descartando o resto.

O que faz o operador %? :: Retorna o resto da divisão, chamado de módulo; 10 % 3 é 1.

Qual a diferença entre = e ==? :: = atribui um valor a uma variável; == compara se dois valores são iguais.

Como funcionam and, or e not? :: and é verdadeiro só se os dois lados forem; or é verdadeiro se pelo menos um for; not inverte o valor.

O que faz contador += 1? :: Soma 1 ao valor atual de contador e guarda o resultado nele mesmo.

Quanto é 2 + 3 * 4 em Python? :: 14, porque a multiplicação vem antes da soma; com parênteses, (2 + 3) * 4 dá 20.

---
Veja o exemplo em `Python/exemplos/05_operadores.py`. Próxima nota: [[06-Entrada-e-Saida]]
