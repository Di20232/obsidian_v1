---
tags: [javascript, basico]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Primeiro Programa

## O ritual do "Olá, mundo", de novo

Mesma ideia de [[../Python/03-Primeiro-Programa]]: o primeiro programa serve para validar que o ambiente funciona ponta a ponta, não para ensinar algo profundo.

```javascript
console.log("Olá, mundo!");
```

Veja o exemplo completo em `JavaScript/exemplos/03_ola_mundo.js`.

## Executando

```bash
node 03_ola_mundo.js
```

Saída:

```
Olá, mundo!
```

## Desmontando a linha

- `console` é um **objeto** global (ver mais em [[09-Arrays-e-Objetos]] e [[15-Classes-e-POO]]) que dá acesso a funcionalidades do ambiente — nesse caso, escrever no terminal/console.
- `.log(...)` é um **método** desse objeto (a mesma ideia de método já vista em `"oi".upper()` no Python, [[../Python/10-Strings]]).
- `(...)` — chamando o método, passando o que está dentro como **argumento**.
- `"Olá, mundo!"` — uma **string**, texto entre aspas.
- `;` no final — marca o fim da instrução. É tecnicamente opcional na maioria dos casos (o motor JS costuma inferir onde termina), mas colocar sempre é a convenção adotada pela imensa maioria do código profissional, porque evita ambiguidades raras e sutis.

## Chaves `{ }` em vez de indentação

Diferente de Python (visto em [[../Python/03-Primeiro-Programa]]), onde a indentação **define** onde um bloco começa e termina, em JavaScript isso é feito com **chaves**:

```javascript
if (true) {
    console.log("dentro do bloco");
}
```

A indentação aqui é só estética — o código funcionaria igual sem ela. Mesmo assim, **sempre indente** (o padrão é 2 ou 4 espaços; escolha um e seja consistente) — código sem indentação é praticamente ilegível para outra pessoa (ou para você, depois).

## Comentários

```javascript
// Isto é um comentário de uma linha — o motor JS ignora esta linha.
console.log("Isto é executado.");

/* Isto é um comentário
   de várias linhas */
```

## Aspas: simples, duplas ou crase

```javascript
let a = 'texto com aspas simples';
let b = "texto com aspas duplas";
let c = `texto com crase (template string)`;
```

As três funcionam para texto comum — a diferença aparece com a crase, que permite inserir variáveis diretamente dentro do texto (equivalente às f-strings do Python, visto em [[../Python/06-Entrada-e-Saida]]); isso é detalhado em [[10-Strings]].

## Erros comuns

- Esquecer de fechar uma chave `{` sem a `}` correspondente — o erro geralmente aparece bem depois do ponto real do problema, então confira sempre contando os pares.
- Misturar tipos de aspas sem fechar direito (`"texto'` é inválido).
- Salvar o arquivo sem a extensão `.js`.

Assim como o traceback do Python ([[../Python/03-Primeiro-Programa]]), o Node.js mostra uma mensagem de erro com o tipo do problema e a linha — leia de cima a baixo procurando a primeira linha que menciona seu próprio arquivo.

## Exercício

Altere `03_ola_mundo.js` para imprimir seu nome em uma linha e uma frase sobre por que você está aprendendo JavaScript em outra (dois `console.log`).

---
Próxima nota: [[04-Variaveis-e-Tipos]]
