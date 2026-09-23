---
tags: [javascript, assincronismo, flashcards]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Assincronismo

## Um problema que Python, no curso básico, nunca te obrigou a enfrentar

Em todo o [[../Python/00-Indice|curso de Python]], cada linha de código só começa depois que a anterior termina completamente — isso é chamado de execução **síncrona**. JavaScript, principalmente por ter nascido para rodar no navegador, foi desenhado com uma restrição importante: ele roda em **uma única thread** (uma única linha de execução por vez), e essa thread também é responsável por manter a página respondendo a cliques e rolagem. Se uma operação demorada (buscar dados na internet, ler um arquivo grande) **travasse** essa thread esperando, a página inteira congelaria enquanto isso.

A solução de JavaScript foi tornar operações demoradas **assíncronas**: o código dispara a operação, **não espera parado**, continua rodando o resto, e só volta a lidar com o resultado quando ele estiver pronto.

## `setTimeout`: o exemplo mais simples de assincronismo

```javascript
console.log("1");
setTimeout(() => {
    console.log("2 (depois de 1 segundo)");
}, 1000);
console.log("3");
```

Saída, na ordem real:
```
1
3
2 (depois de 1 segundo)
```

Repare: `"3"` aparece **antes** de `"2"`, mesmo `setTimeout` estando escrito antes de `console.log("3")` no código. Isso acontece porque `setTimeout` **não pausa** o programa — ele agenda a função para rodar depois de 1000ms e **imediatamente libera** a execução para continuar nas linhas seguintes.

## Callback: o padrão mais antigo (e o mais confuso em excesso)

Uma **callback** é uma função passada como argumento, para ser chamada quando algo terminar — você já viu esse padrão em `rl.question(..., (nome) => {...})` na nota [[06-Entrada-e-Saida]].

```javascript
const fs = require("fs");

fs.readFile("dados.txt", "utf-8", (erro, conteudo) => {
    if (erro) {
        console.log("Erro ao ler:", erro.message);
        return;
    }
    console.log(conteudo);
});

console.log("Esta linha roda ANTES do conteúdo do arquivo aparecer.");
```

O problema prático de callbacks: encadear várias operações assíncronas em sequência (ler um arquivo, depois processar, depois salvar outro) gera callbacks dentro de callbacks dentro de callbacks — apelidado de "callback hell", difícil de ler e de dar manutenção.

## Promise: um valor que ainda vai existir

Uma **Promise** representa "um valor que, no futuro, vai estar pronto (com sucesso) ou vai falhar". Resolve o aninhamento de callbacks permitindo encadear com `.then()`:

```javascript
const fs = require("fs").promises;   // versão do módulo "fs" baseada em Promises

fs.readFile("dados.txt", "utf-8")
    .then(conteudo => {
        console.log(conteudo);
        return conteudo.toUpperCase();
    })
    .then(conteudoMaiusculo => {
        console.log(conteudoMaiusculo);
    })
    .catch(erro => {
        console.log("Erro:", erro.message);   // mesmo conceito de catch de [[13-Tratamento-de-Erros]]
    });
```

Cada `.then()` roda **depois** que a Promise anterior é resolvida, encadeando de forma bem mais legível que callbacks aninhadas. `.catch()` captura qualquer erro que aconteça em qualquer ponto da cadeia.

## `async`/`await`: a forma moderna e recomendada

`async`/`await` é "açúcar sintático" sobre Promises — o mesmo mecanismo por trás, mas com uma sintaxe que **parece** síncrona, muito mais fácil de ler:

```javascript
const fs = require("fs").promises;

async function processarArquivo() {
    try {
        const conteudo = await fs.readFile("dados.txt", "utf-8");
        console.log(conteudo);
        const conteudoMaiusculo = conteudo.toUpperCase();
        console.log(conteudoMaiusculo);
    } catch (erro) {
        console.log("Erro:", erro.message);
    }
}

processarArquivo();
```

Regras:
- `await` só pode ser usado **dentro** de uma função marcada com `async`.
- `await algo` "pausa" **aquela função específica** até a Promise resolver, sem travar o resto do programa — outras partes do código continuam rodando normalmente enquanto isso.
- `try`/`catch` funciona normalmente ao redor de `await`, exatamente como visto em [[13-Tratamento-de-Erros]] — essa é a grande vantagem de `async`/`await` sobre `.then()`/`.catch()`: reaproveita a mesma estrutura de tratamento de erro que você já usa em código síncrono.

Python tem um mecanismo equivalente (`async def` / `await`), mas ele é usado com muito menos frequência no dia a dia do que em JavaScript — em JS, é praticamente inevitável assim que você trabalha com rede ou arquivos.

## `fetch`: buscando dados da internet

```javascript
async function buscarUsuario() {
    const resposta = await fetch("https://api.github.com/users/octocat");
    const dados = await resposta.json();
    console.log(dados.name);
}

buscarUsuario();
```

Mesma ideia de `requests.get(...)` em Python, vista em [[../Programacao-Geral/10-Como-a-Web-Funciona]] — a diferença é que em JavaScript essa operação é **sempre assíncrona**, por isso o `await` duplo: um para a resposta chegar, outro para o corpo JSON ser interpretado.

## Por que isso importa tanto especificamente em JavaScript

Praticamente toda interação com o mundo externo em JavaScript é assíncrona por padrão: ler arquivos (`fs`), buscar dados de uma API (`fetch`), consultar um banco de dados, esperar uma resposta do usuário no navegador. Entender esse modelo não é opcional para trabalhar com JS a sério — é o que mais separa a linguagem, no dia a dia, do jeito como você programou em Python até aqui.

## Exercício

Escreva uma função `async` que usa `fetch` para buscar dados de `https://api.github.com/users/octocat`, e exiba o nome e a quantidade de repositórios públicos (`public_repos`) dessa conta, tratando possíveis erros com `try`/`catch`.

## Perguntas de revisão

Por que JavaScript usa operações assíncronas? :: Porque roda numa única thread, que também mantém a página respondendo; esperar parado travaria tudo.

Em que ordem aparecem 1, setTimeout(2) e 3? :: 1, 3 e depois 2, porque o setTimeout agenda a função e libera a execução imediatamente.

O que é callback hell? :: Callbacks dentro de callbacks ao encadear operações assíncronas, difícil de ler e manter.

O que é uma Promise? :: Um valor que no futuro estará pronto ou falhará, encadeado com .then() e .catch().

Onde pode ser usado await? :: Só dentro de funções marcadas com async.

Qual a vantagem de async/await sobre .then()? :: O código parece síncrono e usa try/catch normal para tratar erros.

Por que fetch usa await duas vezes? :: Uma para a resposta chegar e outra para interpretar o corpo JSON.

---
Veja o exemplo em `JavaScript/exemplos/14_assincronismo.js`. Próxima nota: [[15-Classes-e-POO]]
