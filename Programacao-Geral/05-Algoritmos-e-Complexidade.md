---
tags: [programacao, algoritmos, fundamentos]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Algoritmos e Complexidade

## O que é um algoritmo

Um algoritmo é uma sequência finita e precisa de passos para resolver um problema — o "como fazer", independente da linguagem usada para escrevê-lo. Toda função que você escreveu em [[../Python/11-Funcoes]] implementa algum algoritmo, mesmo que pequeno.

## Por que "funciona" não é suficiente

Dois algoritmos podem resolver o mesmo problema e dar a mesma resposta certa, mas um pode levar 1 segundo e o outro 3 horas para os mesmos dados, dependendo de como foram escritos. Entender **complexidade** é entender como o tempo (ou memória) que um algoritmo gasta cresce conforme a quantidade de dados cresce.

## Notação Big O (a ideia, sem susto)

Big O descreve **como o tempo de execução cresce** conforme o tamanho da entrada (`n`) aumenta — não o tempo exato em segundos, que depende do computador, mas a "forma" do crescimento.

- **O(1)** — tempo constante: não importa quantos dados existem, a operação leva o mesmo tempo. Ex.: acessar `dicionario["chave"]` ([[04-Estruturas-de-Dados]]).
- **O(n)** — tempo linear: dobrar os dados dobra o tempo. Ex.: um `for` percorrendo uma lista inteira uma vez.
- **O(n²)** — tempo quadrático: dobrar os dados **quadruplica** o tempo. Ex.: um `for` dentro de outro `for`, ambos percorrendo os mesmos dados (comum em comparações "todos contra todos").
- **O(log n)** — cresce muito devagar: dobrar os dados soma só um passo a mais. Típico de buscas que descartam metade das opções a cada passo (busca binária, abaixo).

```python
# O(n): olha cada elemento uma vez
def contem(lista, alvo):
    for item in lista:
        if item == alvo:
            return True
    return False

# O(n²): para cada elemento, compara com todos os outros
def tem_duplicado(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                return True
    return False
```

**Por que isso importa na prática**: com 100 itens, O(n²) ainda parece rápido (10 mil operações). Com 1 milhão de itens, O(n²) vira 1 trilhão de operações — o programa trava. Saber identificar isso evita escrever código que "funciona no teste, mas quebra em produção".

## Busca

- **Busca linear**: percorre item por item até achar (ou terminar a lista). O(n). Funciona em qualquer lista, ordenada ou não.
- **Busca binária**: só funciona em dados **já ordenados**. Compara o elemento do meio; se o alvo é maior, descarta a metade de baixo; se é menor, descarta a de cima; repete. O(log n) — absurdamente mais rápido em listas grandes.

```python
def busca_binaria(lista_ordenada, alvo):
    inicio, fim = 0, len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1  # não encontrado
```

## Ordenação

Ordenar dados é um dos problemas mais estudados em programação, porque acelera muitas outras operações depois (busca binária, por exemplo, exige dados ordenados). Você raramente implementa isso do zero — Python já traz `sorted()` e `.sort()`, altamente otimizados:

```python
numeros = [5, 2, 8, 1, 9]
print(sorted(numeros))     # [1, 2, 5, 8, 9] -> cria uma nova lista ordenada
numeros.sort()               # ordena a lista original, no lugar
```

Vale saber que existem algoritmos de ordenação com complexidades diferentes (bubble sort é O(n²) e ingênuo; merge sort e quicksort são O(n log n) e são o que bibliotecas reais usam) — o importante aqui não é implementá-los na mão, é saber que a escolha do algoritmo afeta diretamente a performance.

## Recursão

Uma função que **chama a si mesma** para resolver uma versão menor do mesmo problema, até chegar em um caso base simples o suficiente para responder diretamente:

```python
def fatorial(n):
    if n <= 1:          # caso base -> impede recursão infinita
        return 1
    return n * fatorial(n - 1)   # chama a si mesma com um problema menor

print(fatorial(5))   # 5 * 4 * 3 * 2 * 1 = 120
```

**Todo caso base é obrigatório** — sem ele, a função chamaria a si mesma para sempre, até estourar a memória (`RecursionError`). Recursão é elegante para problemas naturalmente "aninhados" (percorrer pastas dentro de pastas, árvores da nota anterior), mas quase tudo que recursão faz também pode ser feito com `for`/`while` ([[../Python/08-Lacos-de-Repeticao]]) — a escolha é sobre clareza, não sobre ser "mais poderoso".

## Exercício

Escreva uma função recursiva `soma_ate(n)` que soma todos os números de 1 até `n` (ex.: `soma_ate(5)` = 1+2+3+4+5 = 15). Depois, escreva a mesma lógica usando um `for` em vez de recursão, e compare as duas versões.

---
Próxima nota: [[06-Paradigmas-e-Panorama-de-Linguagens]]
