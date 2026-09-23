---
tags: [javascript, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Módulos e NPM

## Mesmo problema resolvido em [[../Python/12-Modulos-e-Pacotes]]

Dividir código em vários arquivos, e reaproveitar código pronto de terceiros, sem reinventar tudo do zero.

## Criando e importando seus próprios módulos

```javascript
// arquivo: utilidades.js
function dobro(numero) {
    return numero * 2;
}

module.exports = { dobro };
```

```javascript
// arquivo: programa.js
const { dobro } = require("./utilidades.js");

console.log(dobro(5));   // 10
```

Essa é a sintaxe tradicional do Node.js, chamada **CommonJS**: `module.exports` define o que o arquivo disponibiliza para fora, e `require(...)` importa. Repare no `./` antes do nome do arquivo — indica "procure na mesma pasta", parecido com o caminho relativo visto em [[../Python/14-Arquivos]].

## A sintaxe mais moderna: `import`/`export` (ES Modules)

```javascript
// arquivo: utilidades.mjs (ou .js com configuração de projeto adequada)
export function dobro(numero) {
    return numero * 2;
}
```

```javascript
// arquivo: programa.mjs
import { dobro } from "./utilidades.mjs";

console.log(dobro(5));
```

Essa sintaxe (`import`/`export`) é a que você vai ver na maioria dos tutoriais e projetos modernos, e é a mesma usada em JavaScript rodando no **navegador**. Ela exige a extensão `.mjs`, ou que o arquivo `package.json` do projeto declare `"type": "module"` (visto abaixo).

## `import` do jeito Python — a mesma ideia, nomes diferentes

```python
# Python ([[../Python/12-Modulos-e-Pacotes]])
from math import sqrt, pi
```

```javascript
// JavaScript
import { sqrt, pi } from "mathjs";  // exemplo com um pacote hipotético
```

A lógica é a mesma: trazer só partes específicas de um módulo para o arquivo atual.

## NPM: o `pip` do JavaScript

**npm** (Node Package Manager) já vem instalado junto com o Node.js ([[02-Preparando-o-Ambiente]]) e cumpre o mesmo papel do `pip` em Python ([[../Python/12-Modulos-e-Pacotes]]): instalar pacotes de terceiros.

```bash
npm init -y             # cria um arquivo package.json descrevendo o projeto
npm install axios        # instala um pacote (equivalente a pip install)
```

Isso cria:
- Uma pasta `node_modules/` com o código do pacote instalado (equivalente conceitual ao ambiente virtual do Python, [[../Python/16-Boas-Praticas-e-Proximos-Passos]], mas sempre local ao projeto por padrão, sem precisar ativar nada).
- Um arquivo `package.json`, que lista as dependências do projeto (equivalente ao `requisitos.txt` mencionado em [[../Python/16-Boas-Praticas-e-Proximos-Passos]]).

```javascript
const axios = require("axios");

axios.get("https://api.exemplo.com/dados")
    .then(resposta => console.log(resposta.data));
```

`axios` é um pacote popular para fazer requisições HTTP — o equivalente do `requests` em Python ([[../Programacao-Geral/10-Como-a-Web-Funciona]]). `.then(...)` aparece porque essa operação é assíncrona — detalhado em [[14-Assincronismo]].

## `package.json`, rapidamente

```json
{
  "name": "meu-projeto",
  "version": "1.0.0",
  "type": "module",
  "dependencies": {
    "axios": "^1.6.0"
  }
}
```

`"type": "module"` habilita a sintaxe `import`/`export` em arquivos `.js` comuns, sem precisar da extensão `.mjs`.

## `.gitignore` para projetos Node

Assim como mencionado em [[../Programacao-Geral/03-Git-e-Controle-de-Versao]], `node_modules/` **nunca** deve ser versionado no Git — é recriado a partir do `package.json` com `npm install`, e pode ter dezenas de milhares de arquivos:

```
# .gitignore
node_modules/
```

## Módulos embutidos do Node.js (equivalente à biblioteca padrão do Python)

```javascript
const fs = require("fs");          // sistema de arquivos, ver [[14-Assincronismo]]
const path = require("path");       // manipulação de caminhos de arquivo
const os = require("os");           // informações do sistema operacional
```

## Exercício

Crie um arquivo `matematica.js` com uma função `quadrado(numero)`, exportando-a. Em outro arquivo `principal.js`, importe essa função e use-a para imprimir o quadrado dos números de 1 a 5.

## Perguntas de revisão

Qual a diferença entre CommonJS e ES Modules? :: CommonJS usa require e module.exports; ES Modules usa import e export, a sintaxe moderna também usada no navegador.

Como habilitar import/export em arquivos .js no Node? :: Declarando "type": "module" no package.json, ou usando a extensão .mjs.

Para que serve o package.json? :: Descreve o projeto e lista suas dependências, como o requirements do Python.

Por que node_modules não vai para o Git? :: Porque é recriado com npm install a partir do package.json e pode ter milhares de arquivos.

Qual o equivalente do pip em JavaScript? :: O npm.

---
Veja o exemplo em `JavaScript/exemplos/utilidades.js` + `JavaScript/exemplos/12_modulos.js`. Próxima nota: [[13-Tratamento-de-Erros]]
