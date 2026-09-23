---
tags: [javascript, basico]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Entrada e Saída

## Saída: `console.log()` a fundo

Você já usa `console.log()` desde [[03-Primeiro-Programa]]. Ele aceita várias formas de montar uma mensagem, assim como o `print()` de Python ([[../Python/06-Entrada-e-Saida]]):

```javascript
let nome = "Diego";
let idade = 25;

// Concatenação com +
console.log("Nome: " + nome + ", Idade: " + idade);

// Múltiplos argumentos separados por vírgula (console.log junta com espaço)
console.log("Nome:", nome, "Idade:", idade);

// Template string (RECOMENDADO): use crase ` e ${variavel} dentro do texto
console.log(`Nome: ${nome}, Idade: ${idade}`);
```

**Template strings** (com crase `` ` ``) são o equivalente direto das f-strings do Python — a forma recomendada, porque lê como o resultado final vai ficar e aceita expressões dentro de `${}`:

```javascript
console.log(`Ano que vem: ${idade + 1}`);
```

Outras variações de saída, úteis para depuração (ver [[../Programacao-Geral/12-Debugging-e-Testes]]):

```javascript
console.error("Isto é um erro");    // saída destacada como erro
console.warn("Isto é um aviso");     // saída destacada como aviso
console.table([{nome: "Diego", idade: 25}]);  // exibe dados em formato de tabela
```

## Entrada: o motivo de não ter um `input()` simples

Python tem `input()` como uma função única e simples ([[../Python/06-Entrada-e-Saida]]). JavaScript **não tem equivalente direto** rodando pelo terminal, porque a linguagem foi criada primeiro para o navegador — e receber entrada no navegador é diferente de receber no terminal. Vamos ver as três formas mais comuns.

### 1. No navegador: `prompt()`

```javascript
let nome = prompt("Digite seu nome:");
alert(`Olá, ${nome}!`);
```

`prompt()` abre uma caixa de diálogo pedindo texto, e `alert()` mostra uma mensagem — mas **os dois só existem dentro de um navegador**, não funcionam rodando com `node arquivo.js` no terminal.

### 2. No terminal com Node.js: argumentos de linha de comando

A forma mais simples de "receber entrada" em um script Node é ler valores passados **na hora de chamar o script**, através de `process.argv`:

```javascript
// arquivo: saudacao.js
let nome = process.argv[2];   // as duas primeiras posições são reservadas pelo Node
console.log(`Olá, ${nome}!`);
```

```bash
node saudacao.js Diego
# Olá, Diego!
```

`process.argv` é uma lista (ver [[09-Arrays-e-Objetos]]) com tudo que foi digitado no comando; as posições `0` e `1` são sempre reservadas (o caminho do Node e o caminho do arquivo), então os argumentos reais começam na posição `2`.

### 3. No terminal com Node.js: leitura interativa de verdade

Para pedir texto durante a execução (o comportamento mais parecido com o `input()` do Python), usa-se o módulo embutido `readline`:

```javascript
const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

rl.question("Digite seu nome: ", (nome) => {
    console.log(`Olá, ${nome}!`);
    rl.close();
});
```

Isso é mais verboso que o `input()` do Python porque é **assíncrono** — o programa não trava esperando; ele registra "quando a resposta chegar, rode esta função". Esse conceito (a função `(nome) => {...}` passada como argumento) é aprofundado em [[11-Funcoes]] e em [[14-Assincronismo]] — não se preocupe em dominar agora, só reconheça o padrão.

## Qual usar

- Escrevendo para o navegador: `prompt()`/`alert()`.
- Escrevendo um script de terminal simples, para esta trilha: `process.argv` (mais direto para os exercícios daqui pra frente).
- Escrevendo uma ferramenta de terminal interativa de verdade: `readline`.

## Exercício

Crie um script que receba nome e idade como argumentos de linha de comando (`node script.js Diego 25`), convertendo a idade para número com `Number()` (visto em [[04-Variaveis-e-Tipos]]), e exiba uma frase usando template string dizendo em que ano a pessoa completa 100 anos (você pode fixar o ano atual como uma constante no próprio código para simplificar).

---
Veja o exemplo em `JavaScript/exemplos/06_entrada_saida.js`. Próxima nota: [[07-Condicionais]]
