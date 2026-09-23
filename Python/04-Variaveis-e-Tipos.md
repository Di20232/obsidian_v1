---
tags: [python, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Variáveis e Tipos de Dados

## O problema que isso resolve

Um programa quase sempre precisa **guardar informação temporariamente** para usar depois — o nome digitado por alguém, um total calculado, o resultado de uma pesquisa. Sem um jeito de guardar e nomear esses valores, cada dado existiria só no instante em que foi criado e se perderia.

Uma **variável** é um nome que você dá para um espaço na memória do computador onde um valor fica guardado, para você poder usá-lo (e trocá-lo) depois pelo nome.

## Sintaxe

```python
nome = "Diego"
idade = 25
altura = 1.78
```

O sinal `=` aqui **não é "igual" no sentido matemático** — é o operador de **atribuição**: "pegue o valor da direita e guarde na variável da esquerda". Por isso `idade = 25` se lê "idade recebe 25", não "idade é igual a 25".

Você pode trocar o valor a qualquer momento:

```python
idade = 25
idade = 26  # o valor antigo (25) é substituído
```

## Regras de nomes de variáveis

- Só pode ter letras, números e `_` (underscore); não pode começar com número.
- Não pode ter espaços (`meu nome` é inválido; use `meu_nome`).
- É sensível a maiúsculas/minúsculas: `idade` e `Idade` são variáveis diferentes.
- Convenção do Python (chamada **snake_case**): nomes em minúsculas, palavras separadas por `_`, ex.: `nome_completo`.
- Use nomes que **dizem o que o valor representa**. `x = 25` funciona, mas `idade = 25` explica a si mesmo — isso importa muito quando o código cresce.

## Tipos básicos

Todo valor em Python tem um **tipo**, que define o que pode ser feito com ele:

| Tipo | Exemplo | Representa |
|---|---|---|
| `int` | `25` | número inteiro |
| `float` | `1.78` | número com casas decimais |
| `str` | `"Diego"` | texto (string) |
| `bool` | `True` / `False` | verdadeiro ou falso |

Você pode conferir o tipo de qualquer valor com a função `type()`:

```python
print(type(25))      # <class 'int'>
print(type(1.78))    # <class 'float'>
print(type("oi"))    # <class 'str'>
print(type(True))    # <class 'bool'>
```

## Por que o tipo importa

O tipo determina quais operações fazem sentido. `25 + 5` funciona porque ambos são números. `"25" + 5` **dá erro**, porque `"25"` é texto e `5` é número — o Python não vai adivinhar se você quer somar ou concatenar. Isso é uma escolha deliberada da linguagem: erro explícito é melhor do que comportamento silenciosamente errado.

Quando precisar, você converte um tipo em outro (isso se chama **casting**):

```python
idade_texto = "25"
idade_numero = int(idade_texto)   # str -> int
print(idade_numero + 1)            # 26

numero = 10
numero_texto = str(numero)         # int -> str
print("Tenho " + numero_texto + " anos")
```

## Variáveis sem tipo fixo

Em Python, a variável em si não tem tipo — quem tem tipo é o **valor** guardado nela. Por isso você pode reatribuir uma variável para um valor de outro tipo (embora, na prática, seja uma boa prática evitar isso, para não confundir quem lê o código):

```python
x = 10        # x é int agora
x = "dez"     # agora x é str — permitido, mas geralmente uma má ideia
```

## Constantes (por convenção)

Python não tem uma forma nativa de travar um valor para nunca mudar, mas por convenção, quando um valor não deve ser alterado, escreve-se o nome todo em maiúsculas:

```python
PI = 3.14159
```

Isso é apenas um sinal visual para quem lê o código — o Python não impede a alteração.

## Erros comuns

- Usar uma variável antes de criá-la (`NameError: name 'x' is not defined`).
- Misturar tipos incompatíveis em operações (`TypeError`).
- Confundir `=` (atribuição) com `==` (comparação de igualdade — vista em [[05-Operadores]]).

## Exercício

Crie variáveis `nome`, `idade` e `cidade` com seus próprios dados, e depois use `print()` para exibir uma frase juntando as três, como "Diego, 25 anos, mora em São Paulo". Dica: você vai precisar converter `idade` para texto antes de juntar com `+`, ou aprender o atalho em [[06-Entrada-e-Saida]].

## Perguntas de revisão

O que é uma variável? :: Um nome dado a um espaço na memória onde um valor fica guardado para ser usado e trocado depois.

O que significa o sinal = em Python? :: Atribuição: guarda o valor da direita na variável da esquerda; não é igualdade matemática.

Quais são os quatro tipos básicos do Python? :: int (inteiro), float (decimal), str (texto) e bool (verdadeiro ou falso).

Por que "25" + 5 dá erro em Python? :: Porque soma texto com número; o Python não adivinha a intenção e gera TypeError em vez de agir silenciosamente errado.

O que é casting? :: Converter um valor de um tipo para outro, como int("25") ou str(10).

Qual a convenção de nomes de variáveis em Python? :: snake_case: letras minúsculas com palavras separadas por underscore, como nome_completo.

Como indicar uma constante em Python? :: Escrevendo o nome todo em maiúsculas, como PI = 3.14159; é só convenção, o Python não impede a alteração.

---
Veja o exemplo em `Python/exemplos/04_variaveis.py`. Próxima nota: [[05-Operadores]]
