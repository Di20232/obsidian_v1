---
tags: [programacao, linguagens, fundamentos]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Paradigmas e Panorama de Linguagens

## Por que existem tantas linguagens

Se Python é fácil de ler, por que não usar Python para tudo? Porque cada linguagem faz **trade-offs** diferentes entre facilidade de uso, velocidade de execução, controle sobre a máquina, e o tipo de problema para o qual foi desenhada. Conhecer esse panorama ajuda a entender por que um projeto usa uma linguagem e outro usa outra, e facilita aprender uma linguagem nova depois — os conceitos de [[../Python/00-Indice|todo o curso de Python]] (variáveis, condicionais, loops, funções) existem, com sintaxe diferente, em praticamente todas elas.

## Eixo 1: Compilada vs. Interpretada

Já visto em [[../Python/01-O-que-e-Programacao]] e [[01-Como-Computadores-Funcionam]]:
- **Compilada** (C, C++, Rust, Go): todo o código é traduzido para binário antes de rodar. Resultado: execução muito rápida, mas você precisa recompilar a cada mudança.
- **Interpretada** (Python, JavaScript, Ruby): o código é lido e executado em tempo real por um interpretador. Resultado: mais lento em execução pura, mas com ciclo de desenvolvimento mais rápido (mudou o código, roda na hora, sem etapa de compilação).
- Muitas linguagens modernas (Java, C#) usam um meio-termo: compilam para um "bytecode" intermediário, executado por uma máquina virtual.

## Eixo 2: Tipagem estática vs. dinâmica

- **Dinâmica** (Python, JavaScript): o tipo de uma variável é decidido em tempo de execução, e pode mudar — visto em [[../Python/04-Variaveis-e-Tipos]]. Mais flexível para escrever rápido, mas erros de tipo só aparecem quando aquela linha específica roda.
- **Estática** (Java, C, C++, Rust, TypeScript): o tipo de cada variável é declarado (ou inferido) e checado **antes** do programa rodar. Mais verboso, mas captura uma classe inteira de erros antes mesmo de executar.

```java
// Java: tipagem estática — o tipo é declarado explicitamente
int idade = 25;
String nome = "Diego";
```

```python
# Python: tipagem dinâmica — o tipo é inferido do valor
idade = 25
nome = "Diego"
```

## Eixo 3: Paradigmas

Um paradigma é um "estilo" de organizar a lógica do programa:

- **Procedural**: código organizado como uma sequência de instruções e funções que operam sobre dados — é como o curso de Python começou, até [[../Python/11-Funcoes]].
- **Orientado a objetos**: dados e comportamento agrupados em classes/objetos — visto em [[../Python/15-Programacao-Orientada-a-Objetos]]. Java e C++ são fortemente orientados a objetos por design.
- **Funcional**: o programa é construído principalmente combinando funções, evitando alterar estado compartilhado. Presente com força em Haskell, Elixir, e parcialmente utilizável em Python (funções como `map`, `filter`) e JavaScript.
- Na prática, a maioria das linguagens modernas é **multiparadigma** — Python, por exemplo, suporta procedural, orientado a objetos e um pouco de funcional, e você escolhe conforme o problema.

## Tour rápido por linguagens importantes

- **Python**: interpretada, tipagem dinâmica, sintaxe legível. Forte em ciência de dados, automação, back-end web, IA. Você já aprendeu o essencial dela neste cofre.
- **JavaScript**: interpretada, tipagem dinâmica. A única linguagem que roda nativamente em **todo** navegador — por isso é a base do front-end web. Também roda no servidor via Node.js. Ver [[08-JavaScript-Basico]].
- **Java**: compilada para bytecode (roda na "JVM"), tipagem estática, fortemente orientada a objetos. Muito usada em sistemas corporativos grandes e Android (historicamente).
- **C**: compilada, tipagem estática, sem gerenciamento automático de memória (você aloca e libera manualmente). Extremamente rápida e próxima do hardware — usada em sistemas operacionais, drivers, sistemas embarcados. Ver [[11-C-e-Memoria]].
- **C++**: C com orientação a objetos e mais recursos. Usada em jogos, software de alta performance, sistemas com restrição de tempo real.
- **Go**: compilada, tipagem estática, sintaxe simples de propósito, com suporte nativo forte a concorrência (fazer várias coisas "ao mesmo tempo"). Popular em back-ends de infraestrutura e serviços de rede.
- **Rust**: compilada, tipagem estática, garante segurança de memória sem depender de um "coletor de lixo" automático (usa um sistema de regras checado em tempo de compilação). Usada onde performance e segurança de memória são críticas.
- **SQL**: não é uma linguagem de propósito geral — é declarativa e feita **especificamente** para consultar e manipular bancos de dados. Ver [[09-SQL-e-Bancos-de-Dados]].
- **HTML/CSS**: tecnicamente não são "linguagens de programação" no sentido de terem lógica (`if`, loops) — HTML descreve estrutura de conteúdo, CSS descreve aparência. Ver [[07-HTML-e-CSS]].

## Um exemplo lado a lado: "somar dois números e mostrar"

```python
# Python
a = 5
b = 3
print(a + b)
```

```javascript
// JavaScript
let a = 5;
let b = 3;
console.log(a + b);
```

```java
// Java
int a = 5;
int b = 3;
System.out.println(a + b);
```

```c
// C
#include <stdio.h>
int main() {
    int a = 5, b = 3;
    printf("%d\n", a + b);
    return 0;
}
```

Repare: a **lógica** é idêntica (variáveis, soma, exibição) — o que muda é sintaxe, se o tipo precisa ser declarado, e o quanto de "cerimônia" (código extra obrigatório, como `#include`, `main()`, ponto e vírgula) a linguagem exige.

## Como isso te ajuda na prática

Depois de aprender bem uma primeira linguagem (como você fez com Python), aprender a segunda é muito mais rápido — você já sabe **o que** procurar (como declara variável? como faz `if`? como faz loop?), só precisa mapear para a sintaxe nova.

## Exercício

Pegue o exercício resolvido de [[../Python/07-Condicionais]] (par/ímpar) e, sem se preocupar em rodar de verdade, escreva no papel/editor como você imagina que ficaria em pseudocódigo (uma mistura de português e lógica de programação, sem sintaxe de linguagem nenhuma). Isso é o que muitos programadores fazem para planejar antes de escrever na sintaxe real.

---
Próxima nota: [[07-HTML-e-CSS]]
