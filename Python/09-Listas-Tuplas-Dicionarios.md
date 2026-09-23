---
tags: [python, basico, estruturas-de-dados, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Listas, Tuplas e Dicionários

## O problema que isso resolve

Uma variável guarda **um** valor. Mas problemas reais envolvem coleções: uma lista de compras, os nomes de uma turma, o cadastro de um cliente com vários campos. Python tem estruturas prontas para guardar **vários valores organizados**, cada uma com um propósito diferente.

## Listas: coleção ordenada e alterável

```python
frutas = ["maçã", "banana", "uva"]

print(frutas[0])     # "maçã"  -> índice começa em 0, não em 1
print(frutas[-1])    # "uva"   -> índice negativo conta do fim

frutas.append("pera")        # adiciona no fim
frutas.remove("banana")      # remove pelo valor
frutas[0] = "abacaxi"        # troca o valor na posição 0

print(len(frutas))           # tamanho da lista
print(frutas)
```

**Por que índice começa em 0**: é uma convenção herdada de como a memória do computador é endereçada (a posição é medida como "deslocamento a partir do início"). É estranho no começo, mas se torna automático com a prática.

Listas são **mutáveis**: você pode mudar seu conteúdo depois de criadas — diferente de tuplas, abaixo.

Percorrendo uma lista (conecta com [[08-Lacos-de-Repeticao]]):

```python
for fruta in frutas:
    print(fruta)

# Quando você precisa também do índice:
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
```

Fatiamento (pegar um pedaço da lista):

```python
numeros = [10, 20, 30, 40, 50]
print(numeros[1:3])   # [20, 30]  -> do índice 1 até o 3 (exclusivo)
print(numeros[:2])    # [10, 20]  -> do início até o índice 2 (exclusivo)
print(numeros[2:])    # [30, 40, 50] -> do índice 2 até o fim
```

## Tuplas: coleção ordenada e **imutável**

```python
coordenada = (10, 20)
print(coordenada[0])   # 10
```

A sintaxe é quase igual à lista, mas com parênteses em vez de colchetes, e — o ponto central — **depois de criada, não pode ser alterada**. Por que isso é útil: quando você quer garantir que um dado não vai ser acidentalmente modificado em algum ponto do programa (por exemplo, uma coordenada geográfica fixa, ou os dias da semana). Também são um pouco mais rápidas que listas por serem imutáveis.

## Dicionários: coleção de pares chave → valor

```python
pessoa = {
    "nome": "Diego",
    "idade": 25,
    "cidade": "São Paulo"
}

print(pessoa["nome"])       # acessa pelo nome da chave, não por índice numérico
pessoa["idade"] = 26        # altera o valor de uma chave existente
pessoa["profissao"] = "Dev" # adiciona uma nova chave

for chave, valor in pessoa.items():
    print(chave, "->", valor)
```

**Por que dicionários existem**: uma lista só localiza dados por posição numérica (`frutas[0]`), o que exige lembrar a ordem. Um dicionário localiza por um **nome significativo** (`pessoa["nome"]`), o que é como pensamos sobre dados do mundo real — um cadastro tem campos nomeados, não posições numeradas.

Verificando se uma chave existe (evita erro ao tentar acessar uma chave inexistente):

```python
if "profissao" in pessoa:
    print(pessoa["profissao"])
```

## Quando usar cada uma

- **Lista**: uma sequência de itens do mesmo tipo de "coisa", que pode crescer, encolher ou mudar de ordem. Ex.: lista de tarefas.
- **Tupla**: um agrupamento fixo de valores que anda junto e não deve mudar. Ex.: coordenada `(latitude, longitude)`.
- **Dicionário**: dados identificados por nome, geralmente descrevendo "um objeto com vários atributos". Ex.: um usuário, um produto.

## Listas de dicionários (muito comum na prática)

```python
usuarios = [
    {"nome": "Ana", "idade": 30},
    {"nome": "Bruno", "idade": 22},
]

for usuario in usuarios:
    print(f"{usuario['nome']} tem {usuario['idade']} anos")
```

Isso é basicamente como se representa uma "tabela" de dados em Python puro, e é o formato que você vai encontrar o tempo todo ao consumir APIs (dados vindos da internet no formato JSON viram exatamente listas e dicionários).

## Erros comuns

- Tentar acessar um índice que não existe (`IndexError`).
- Tentar acessar uma chave que não existe em um dicionário (`KeyError`) — sempre confira com `in` antes se não tiver certeza.
- Tentar alterar uma tupla (`TypeError: 'tuple' object does not support item assignment`).

## Exercício

Crie uma lista de dicionários representando 3 produtos, cada um com `nome` e `preco`. Use um `for` para imprimir o nome e o preço de cada um, e calcule (usando uma variável acumuladora, como no exercício de [[08-Lacos-de-Repeticao]]) o preço total de todos os produtos.

## Perguntas de revisão

Qual a diferença entre lista e tupla em Python? :: Lista é mutável e usa colchetes; tupla é imutável depois de criada e usa parênteses.

Em que índice começa uma lista em Python? :: Em 0; índices negativos contam a partir do fim, e -1 é o último item.

O que é um dicionário em Python? :: Uma coleção de pares chave e valor, acessados pelo nome da chave em vez de posição numérica.

Como evitar KeyError ao acessar um dicionário? :: Conferindo antes se a chave existe com o operador in.

O que retorna numeros[1:3] em [10, 20, 30, 40, 50]? :: [20, 30]: do índice 1 até o 3, exclusivo.

Como percorrer uma lista com índice e valor ao mesmo tempo? :: Com enumerate: for indice, item in enumerate(lista).

Como dados JSON de uma API aparecem em Python? :: Como listas e dicionários, geralmente uma lista de dicionários.

---
Veja o exemplo em `Python/exemplos/09_estruturas.py`. Próxima nota: [[10-Strings]]
