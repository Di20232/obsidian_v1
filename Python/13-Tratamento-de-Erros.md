---
tags: [python, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Tratamento de Erros (try / except)

## O problema que isso resolve

Você já viu, desde [[06-Entrada-e-Saida]], que entrada do usuário pode quebrar o programa (`ValueError` ao converter texto inválido para número). Em qualquer programa real, coisas dão errado por motivos fora do seu controle: um arquivo que não existe, uma internet que cai, um usuário que digita besteira. Sem tratamento de erros, **qualquer uma dessas situações derruba o programa inteiro**. Tratamento de erros permite **prever essas falhas e decidir o que fazer** em vez de deixar o programa travar.

## Vendo o erro acontecer

```python
idade = int(input("Sua idade: "))   # se digitar "abc", o programa quebra aqui
print(idade)
```

O Python mostra um **traceback** terminando em algo como `ValueError: invalid literal for int() with base 10: 'abc'`. O nome depois dos dois-pontos finais é o **tipo do erro** (chamado de **exceção**).

## `try` / `except`: capturando o erro

```python
try:
    idade = int(input("Sua idade: "))
    print(f"Você tem {idade} anos")
except ValueError:
    print("Isso não é um número válido!")
```

- O bloco `try` é o código "arriscado" que você quer tentar rodar.
- Se der erro **do tipo especificado** (`ValueError`, nesse caso), o Python pula direto para o bloco `except` correspondente, **em vez de** derrubar o programa.
- Se não der erro nenhum, o `except` é simplesmente ignorado.

## Capturando tipos diferentes de erro

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("Isso não é um número.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

Cada `except` trata um tipo específico de problema — isso permite dar uma mensagem clara e adequada para cada caso, em vez de um "deu erro" genérico.

## `else` e `finally`

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido.")
else:
    print(f"Você digitou {numero}, processado com sucesso.")
finally:
    print("Fim da tentativa.")
```

- `else`: roda **só se não houve erro** no `try`.
- `finally`: roda **sempre**, tenha dado erro ou não — útil para "limpeza" (por exemplo, fechar um arquivo, visto em [[14-Arquivos]]).

## Repetindo até dar certo (combinando com `while`)

```python
while True:
    try:
        idade = int(input("Sua idade: "))
        break   # só sai do loop se a conversão funcionar
    except ValueError:
        print("Digite um número válido.")

print(f"Idade registrada: {idade}")
```

Esse padrão — `while True` com `break` só no caminho de sucesso — é muito comum para validar entrada do usuário até que ela esteja correta.

## Não abuse do `except` genérico

```python
try:
    codigo_arriscado()
except Exception:
    print("Deu algo errado")
```

Isso captura **qualquer** erro, inclusive erros de programação que você nem sabia que existiam (o que dificulta descobrir bugs). Prefira sempre capturar o tipo específico de exceção que você espera que aconteça, e deixe os inesperados aparecerem — eles são informação útil para corrigir o código.

## Erros comuns já vistos neste curso, para referência

- `NameError` — usar uma variável que não existe.
- `TypeError` — operação entre tipos incompatíveis (ex.: `str + int`).
- `ValueError` — valor do tipo certo, mas conteúdo inválido (ex.: `int("abc")`).
- `IndexError` — índice fora do intervalo de uma lista/string.
- `KeyError` — chave inexistente em um dicionário.
- `ZeroDivisionError` — divisão por zero.

## Exercício

Escreva um programa que peça dois números e os divida, capturando tanto `ValueError` (entrada não numérica) quanto `ZeroDivisionError` (divisor igual a zero), com uma mensagem específica para cada caso.

## Perguntas de revisão

Para que serve try/except? :: Para prever falhas e decidir o que fazer em vez de deixar o programa travar.

Qual a diferença entre else e finally num try? :: else roda só se não houve erro; finally roda sempre, com ou sem erro.

Por que evitar except Exception genérico? :: Porque esconde erros de programação inesperados, que são informação útil para corrigir o código.

Qual o padrão para repetir a entrada até o usuário digitar um valor válido? :: while True com try/except, e break só no caminho de sucesso.

Qual a diferença entre TypeError e ValueError? :: TypeError é operação entre tipos incompatíveis; ValueError é valor do tipo certo mas conteúdo inválido, como int("abc").

---
Veja o exemplo em `Python/exemplos/13_erros.py`. Próxima nota: [[14-Arquivos]]
