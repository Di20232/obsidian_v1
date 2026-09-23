---
tags: [python, basico]
cssclasses: [cerebro-nota, cerebro-python]
---

# Entrada e Saída (input / print)

## O problema que isso resolve

Até agora, todo dado no seu código estava fixo (você escreveu `nome = "Diego"` diretamente). Um programa útil normalmente precisa **receber informação de quem o usa** (entrada) e **mostrar resultados** (saída). Isso é o que torna um programa interativo em vez de estático.

## Saída: `print()` a fundo

Você já usa `print()` desde [[03-Primeiro-Programa]]. Ele aceita várias formas de montar a mensagem:

```python
nome = "Diego"
idade = 25

# Concatenação com +  (exige que tudo seja string)
print("Nome: " + nome + ", Idade: " + str(idade))

# Múltiplos argumentos separados por vírgula (print junta com espaço)
print("Nome:", nome, "Idade:", idade)

# f-string (RECOMENDADO): coloque um f antes das aspas e {variavel} dentro do texto
print(f"Nome: {nome}, Idade: {idade}")
```

**Por que f-string é a forma recomendada**: ela lê como o texto final vai ficar, não precisa converter tipos manualmente, e é o padrão usado no código Python moderno. `{idade}` dentro de uma f-string pode conter até expressões: `f"Ano que vem: {idade + 1}"`.

## Entrada: `input()`

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

`input()` **pausa o programa**, mostra a mensagem entre parênteses (o "prompt"), espera a pessoa digitar algo e pressionar Enter, e devolve o que foi digitado.

## A pegadinha mais importante deste tópico

**`input()` sempre devolve texto (`str`)**, mesmo se a pessoa digitar números. Isso quebra cálculos se você não converter:

```python
idade = input("Sua idade: ")
print(idade + 1)   # ERRO: TypeError — não dá pra somar str + int
```

Correção, convertendo o texto para número (visto em [[04-Variaveis-e-Tipos]]):

```python
idade = int(input("Sua idade: "))
print(idade + 1)   # funciona
```

Se o valor pode ter casas decimais, use `float()` no lugar de `int()`.

## O que acontece se a pessoa digitar algo inválido

```python
idade = int(input("Sua idade: "))
```

Se a pessoa digitar "vinte" em vez de "20", o programa quebra com `ValueError`, porque `int()` não sabe converter essa palavra em número. Você vai aprender a se proteger disso em [[13-Tratamento-de-Erros]]. Por enquanto, só tenha em mente que **entrada do usuário nunca é 100% confiável**.

## Exercício

Escreva um programa que pergunte o nome e a idade da pessoa (dois `input()`), calcule em que ano ela completa 100 anos (você vai precisar saber o ano atual — pode pedir também como entrada), e mostre uma frase final usando f-string.

---
Veja o exemplo em `Python/exemplos/06_entrada_saida.py`. Próxima nota: [[07-Condicionais]]
