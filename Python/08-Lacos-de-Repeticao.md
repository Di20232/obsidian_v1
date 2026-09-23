---
tags: [python, basico]
cssclasses: [cerebro-nota, cerebro-python]
---

# Laços de Repetição (for, while)

## O problema que isso resolve

Imagine imprimir os números de 1 a 1000, ou processar cada linha de um arquivo com 50 mil linhas. Escrever `print()` mil vezes é inviável. **Laços (loops)** permitem repetir um bloco de código várias vezes sem repetir o código em si — a máquina é boa exatamente nisso.

## `for`: repetir um número definido de vezes / percorrer uma sequência

```python
for numero in range(5):
    print(numero)
```

Saída: `0 1 2 3 4`. `range(5)` gera uma sequência de números de 0 até 4 (5 números, mas para em 4 — o limite é **exclusivo**). O `for` pega cada valor dessa sequência, guarda temporariamente na variável `numero`, roda o bloco indentado, e repete até acabar.

Variações de `range`:

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 5)     # 2, 3, 4          (início, fim exclusivo)
range(0, 10, 2) # 0, 2, 4, 6, 8    (início, fim exclusivo, passo)
```

`for` também percorre diretamente listas, strings e outras coleções (você vai ver isso com mais detalhe em [[09-Listas-Tuplas-Dicionarios]]):

```python
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)
```

## `while`: repetir enquanto uma condição for verdadeira

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Use `while` quando você **não sabe de antemão** quantas repetições vai precisar — por exemplo, repetir até a pessoa digitar a senha certa.

```python
senha_correta = "python123"
tentativa = input("Digite a senha: ")

while tentativa != senha_correta:
    print("Senha incorreta, tente novamente.")
    tentativa = input("Digite a senha: ")

print("Acesso liberado")
```

## O perigo do `while`: loop infinito

Se a condição nunca ficar `False`, o programa nunca para. Isso é o erro mais comum de quem começa com `while`:

```python
contador = 0
while contador < 5:
    print(contador)
    # esqueceu de fazer contador += 1 -> loop infinito!
```

Sempre confira: existe algo dentro do loop que **muda a variável usada na condição**, aproximando ela do momento em que a condição vira falsa?

## `break` e `continue`

- `break` **encerra o loop imediatamente**, mesmo que a condição ainda fosse verdadeira.
- `continue` **pula para a próxima repetição**, ignorando o restante do bloco atual.

```python
for numero in range(10):
    if numero == 5:
        break            # para completamente ao chegar em 5
    print(numero)         # imprime 0, 1, 2, 3, 4

for numero in range(10):
    if numero % 2 == 0:
        continue          # pula os pares
    print(numero)         # imprime só os ímpares: 1, 3, 5, 7, 9
```

## Loops aninhados

Um loop dentro do outro — comum para trabalhar com "tabelas" (linhas x colunas):

```python
for linha in range(3):
    for coluna in range(3):
        print(f"({linha}, {coluna})", end=" ")
    print()  # pula linha depois de cada linha da "tabela"
```

## `for` vs `while` — qual usar

- Sabe exatamente **quantas vezes** ou tem uma coleção para percorrer? Use `for`.
- Depende de uma **condição que só se sabe em tempo de execução** (senha, "continuar jogando?", etc.)? Use `while`.

## Exercício

Escreva um programa que use `for` para imprimir a tabuada de um número (peça o número com `input()`), de 1 a 10. Depois, escreva um programa com `while` que peça números até a pessoa digitar `0`, e ao final mostre a soma de todos os números digitados (não conte o `0`).

---
Veja o exemplo em `Python/exemplos/08_lacos.py`. Próxima nota: [[09-Listas-Tuplas-Dicionarios]]
