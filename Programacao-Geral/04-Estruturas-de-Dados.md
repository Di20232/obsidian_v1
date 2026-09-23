---
tags: [programacao, estruturas-de-dados, fundamentos, flashcards]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Estruturas de Dados

## Por que ir além de listas e dicionários

Em [[../Python/09-Listas-Tuplas-Dicionarios]] você aprendeu listas, tuplas e dicionários — o suficiente para a maioria dos scripts do dia a dia. Mas essas são implementações específicas do Python de conceitos **mais gerais**, que existem (com outros nomes e detalhes) em toda linguagem. Entender esses conceitos ajuda a escolher a estrutura certa para cada problema — a estrutura errada pode tornar um programa absurdamente mais lento sem motivo.

## Array (vetor)

Um bloco de memória **contíguo** onde cada posição guarda um valor, acessado por índice numérico. A lista do Python funciona de forma parecida por fora, mas internamente é mais flexível (redimensiona sozinha). Em linguagens como C ([[11-C-e-Memoria]]), o array é literal: um tamanho fixo, definido na criação.

**Por que importa**: acessar um elemento por índice (`array[5]`) é extremamente rápido (tempo constante), porque a posição na memória pode ser calculada diretamente. Inserir no meio de um array grande é caro, porque tudo depois precisa se deslocar.

## Lista encadeada (linked list)

Cada elemento ("nó") guarda seu valor **e um ponteiro/referência para o próximo elemento**. Diferente do array, os elementos não precisam estar em posições contínuas de memória.

**Trade-off**: inserir/remover no início é muito rápido (só reorganiza referências), mas acessar um elemento no meio exige percorrer a lista do começo — não existe acesso direto por índice como no array.

## Pilha (stack)

Estrutura onde o último elemento que entrou é o primeiro a sair (**LIFO**: Last In, First Out) — como uma pilha de pratos. Operações: `push` (empilhar) e `pop` (desempilhar o topo).

**Onde aparece na prática**: o botão "desfazer" de um editor, a navegação de "voltar" do navegador, e — muito importante — a forma como chamadas de função são gerenciadas internamente pelo próprio interpretador (a "pilha de chamadas").

Em Python, uma lista já serve como pilha:

```python
pilha = []
pilha.append(1)   # push
pilha.append(2)
pilha.append(3)
print(pilha.pop())  # 3 -> remove e devolve o último (o topo)
```

## Fila (queue)

O primeiro elemento que entra é o primeiro a sair (**FIFO**: First In, First Out) — como uma fila de banco.

**Onde aparece**: processamento de tarefas na ordem de chegada, impressão de documentos, mensagens entre sistemas.

```python
from collections import deque

fila = deque()
fila.append(1)       # entra no fim
fila.append(2)
fila.append(3)
print(fila.popleft())  # 1 -> remove e devolve o primeiro que entrou
```

## Hash table (tabela hash)

É o conceito por trás do **dicionário do Python** (visto em [[../Python/09-Listas-Tuplas-Dicionarios]]). Internamente, a chave (`"nome"`, por exemplo) passa por uma função matemática (função hash) que calcula diretamente **onde** guardar/buscar aquele valor na memória — por isso `dicionario["chave"]` é, na prática, quase tão rápido quanto acessar um array por índice, mesmo com milhões de itens.

## Árvore (tree)

Estrutura hierárquica: um elemento "raiz" com "filhos", que por sua vez podem ter seus próprios filhos. O sistema de pastas do seu computador é uma árvore (uma pasta contém subpastas, que contêm subpastas...). Árvores binárias de busca, muito usadas em bancos de dados e índices, mantêm os dados ordenados de um jeito que permite buscas muito rápidas.

## Grafo (graph)

Generalização de árvore: elementos ("nós") conectados por relações ("arestas"), sem hierarquia obrigatória — um nó pode se conectar a vários outros livremente. Redes sociais (quem segue quem), mapas de rotas (GPS) e a própria estrutura de links da internet são grafos.

## Como escolher

| Preciso de... | Estrutura provável |
|---|---|
| Acesso rápido por posição numérica | Array / lista |
| Inserir/remover muito no início/meio | Lista encadeada |
| Desfazer última ação | Pilha |
| Processar na ordem de chegada | Fila |
| Buscar por um nome/identificador único, rápido | Hash table (dicionário) |
| Dados hierárquicos (pastas, categorias) | Árvore |
| Conexões livres entre itens (rede) | Grafo |

## Exercício

Sem escrever código, pense: qual estrutura você usaria para representar o histórico de páginas visitadas em um navegador (com suporte a "voltar")? E para representar os amigos de um usuário em uma rede social? Justifique.

## Perguntas de revisão

Qual a vantagem e a desvantagem do array? :: Acesso por índice muito rápido, mas inserir no meio é caro porque os elementos seguintes precisam se deslocar.

O que é uma pilha (LIFO)? :: Uma estrutura em que o último a entrar é o primeiro a sair, como o desfazer de um editor.

O que é uma fila (FIFO)? :: Uma estrutura em que o primeiro a entrar é o primeiro a sair, como uma fila de impressão.

Por que o dicionário do Python é tão rápido? :: Porque é uma tabela hash: uma função calcula direto onde guardar e buscar cada chave.

Que estrutura representa bem pastas e subpastas? :: Uma árvore.

Que estrutura representa conexões livres, como amigos numa rede social? :: Um grafo.

---
Próxima nota: [[05-Algoritmos-e-Complexidade]]
