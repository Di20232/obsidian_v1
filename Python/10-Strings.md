---
tags: [python, basico]
cssclasses: [cerebro-nota, cerebro-python]
---

# Strings em Detalhe

## Por que strings merecem uma nota própria

Texto é, provavelmente, o tipo de dado mais manipulado em programas do mundo real: nomes, e-mails, mensagens, arquivos. Python trata strings como uma **sequência de caracteres**, o que significa que muita coisa que você aprendeu sobre listas em [[09-Listas-Tuplas-Dicionarios]] se aplica aqui também.

## Strings são sequências

```python
nome = "Diego"
print(nome[0])       # "D"  -> mesmo índice de listas
print(nome[-1])       # "o"
print(nome[0:3])      # "Die" -> fatiamento, igual listas
print(len(nome))      # 5
```

**Diferença importante**: strings são **imutáveis**, como tuplas. `nome[0] = "d"` dá erro. Para "mudar" uma string, você sempre cria uma nova.

## Métodos úteis de string

Um **método** é uma função que pertence a um valor específico, chamada com `.` depois do valor:

```python
texto = "  Olá, Mundo!  "

texto.strip()          # remove espaços do início/fim -> "Olá, Mundo!"
texto.lower()           # tudo minúsculo -> "  olá, mundo!  "
texto.upper()           # tudo maiúsculo -> "  OLÁ, MUNDO!  "
texto.replace("Olá", "Oi")  # troca um trecho -> "  Oi, Mundo!  "
texto.strip().split(",")    # divide em lista por um separador
```

**Ponto crucial**: nenhum desses métodos altera `texto` — cada um **retorna uma nova string**. Se quiser guardar o resultado, precisa atribuir:

```python
texto = texto.strip()   # agora sim texto foi atualizado
```

Isso é consequência direta de strings serem imutáveis, mencionado acima.

## Concatenação e repetição

```python
saudacao = "Olá" + " " + "mundo"   # "Olá mundo"
linha = "-" * 20                     # "--------------------"
```

## f-strings, revisitando com mais poder

Você já viu f-strings em [[06-Entrada-e-Saida]]. Elas suportam formatação de números:

```python
preco = 19.9
print(f"R$ {preco:.2f}")     # R$ 19.90  -> duas casas decimais

nome = "diego"
print(f"{nome.upper()}")     # dá pra chamar métodos dentro das chaves
```

## Verificando conteúdo

```python
email = "diego@exemplo.com"

"@" in email          # True -> checa se um trecho existe dentro da string
email.startswith("diego")  # True
email.endswith(".com")     # True
```

## Dividindo e juntando

```python
frase = "o rato roeu a roupa"
palavras = frase.split()          # divide por espaço -> lista de palavras
print(palavras)                    # ['o', 'rato', 'roeu', 'a', 'roupa']

nova_frase = " ".join(palavras)   # junta de volta com espaço
print(nova_frase)
```

`split()` e `join()` juntos são a base de praticamente todo processamento simples de texto: separar um CSV por vírgula, juntar uma lista de nomes em uma frase, etc.

## Strings multilinha

```python
mensagem = """
Prezado cliente,
Seu pedido foi confirmado.
Obrigado pela compra.
"""
```

Três aspas (simples ou duplas) permitem texto com quebras de linha, útil para mensagens longas ou documentação.

## Erros comuns

- Esquecer que métodos de string não alteram a variável original — precisam ser reatribuídos.
- Tentar `texto[0] = "x"` (strings são imutáveis).
- Misturar aspas simples e duplas sem fechar corretamente.

## Exercício

Peça um e-mail via `input()`. Verifique se ele contém `"@"` e termina com `.com`; se sim, imprima "e-mail válido", senão "e-mail inválido". Depois, peça uma frase e conte quantas palavras ela tem usando `split()` e `len()`.

---
Veja o exemplo em `Python/exemplos/10_strings.py`. Próxima nota: [[11-Funcoes]]
