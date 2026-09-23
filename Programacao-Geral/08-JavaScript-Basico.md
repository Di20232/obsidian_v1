---
tags: [programacao, javascript, web, flashcards]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# JavaScript Básico

> Esta nota é um resumo panorâmico. Para uma trilha completa, do zero, com exemplos executáveis nota a nota — igual ao [[../Python/00-Indice|curso de Python]] — veja [[../JavaScript/00-Indice|Curso de JavaScript do Zero]].

## Por que essa linguagem é praticamente obrigatória de conhecer

HTML e CSS ([[07-HTML-e-CSS]]) descrevem estrutura e aparência, mas são **estáticos** — não reagem a cliques, não validam formulários, não atualizam conteúdo sozinhos. **JavaScript** é a linguagem que roda dentro do navegador e dá comportamento e interatividade a uma página. É a única linguagem que todo navegador executa nativamente, o que a torna, de longe, a linguagem mais usada em código que roda no front-end da web.

## Sintaxe comparada ao Python

Se você fez o [[../Python/00-Indice|curso de Python]], os conceitos abaixo já são familiares — só a sintaxe muda:

```javascript
// Variáveis
let idade = 25;         // pode ser reatribuída (equivalente à variável comum do Python)
const nome = "Diego";   // não pode ser reatribuída (constante de verdade, diferente da convenção do Python)

// Condicional
if (idade >= 18) {
    console.log("Maior de idade");
} else {
    console.log("Menor de idade");
}

// Loop
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// Função
function saudacao(nome) {
    console.log(`Olá, ${nome}!`);   // crase + ${} = igual à f-string do Python
}
saudacao("Diego");

// Lista (chamada de "array" em JS) e dicionário (chamado de "objeto")
const frutas = ["maçã", "banana", "uva"];
const pessoa = { nome: "Diego", idade: 25 };

console.log(frutas[0]);
console.log(pessoa.nome);      // ou pessoa["nome"]
```

Diferenças de sintaxe a notar:
- Blocos usam `{ }`, não indentação (a indentação em JS é só estética, não obrigatória como em Python — ainda assim, todo mundo indenta por legibilidade).
- Linhas terminam com `;` (ponto e vírgula), geralmente opcional mas convencional.
- `console.log()` é o equivalente ao `print()` do Python.
- Template strings usam crase `` ` `` em vez de aspas, com `${variavel}` no lugar de `{variavel}`.

## O DOM: onde JavaScript encontra o HTML

JavaScript manipula a árvore de elementos HTML (o **DOM**, mencionado em [[07-HTML-e-CSS]]) para mudar o que a página mostra, sem precisar recarregar:

```javascript
document.getElementById("titulo").textContent = "Novo título";

document.getElementById("botao").addEventListener("click", function() {
    alert("Você clicou!");
});
```

`addEventListener` registra uma função para rodar **quando algo acontece** (um clique, por exemplo) — esse padrão é chamado de **programação orientada a eventos**, muito característico de interfaces gráficas em geral, não só web.

## Assíncrono: o conceito mais importante e mais estranho de JavaScript

Buscar dados de um servidor (ver [[10-Como-a-Web-Funciona]]) leva tempo — às vezes segundos. Se o JavaScript **parasse** esperando a resposta, a página inteira travaria enquanto isso. Por isso, operações demoradas em JS são **assíncronas**: o código "dispara" a operação e continua rodando o resto, tratando o resultado só quando ele chegar.

```javascript
async function buscarDados() {
    const resposta = await fetch("https://api.exemplo.com/dados");
    const dados = await resposta.json();
    console.log(dados);
}
```

`fetch` faz uma requisição HTTP (ver [[10-Como-a-Web-Funciona]]); `await` diz "espere isso terminar antes de seguir para a próxima linha **desta função**", sem travar o resto da página. Python tem um equivalente (`async`/`await` também), mas é bem menos central no dia a dia do que em JavaScript.

## Node.js: JavaScript fora do navegador

Originalmente, JavaScript só rodava dentro de páginas web. O **Node.js** é um ambiente que permite rodar JavaScript no servidor, fora do navegador — como um back-end, competindo diretamente com Python/Django/Flask nesse papel. É por isso que hoje é comum ver "front-end e back-end, tudo em JavaScript" em um mesmo projeto.

## TypeScript, rapidamente

**TypeScript** é JavaScript com **tipagem estática** adicionada por cima (ver o eixo de tipagem em [[06-Paradigmas-e-Panorama-de-Linguagens]]) — você escreve `let idade: number = 25`, e um verificador aponta erros de tipo antes mesmo de rodar. É extremamente popular em projetos JavaScript de médio/grande porte por essa segurança extra.

## Exercício

Crie um arquivo `pagina.html` simples com um botão e um parágrafo vazio. Em uma tag `<script>` (ou um arquivo `.js` separado), escreva uma função que, ao clicar no botão, escreva "Você clicou!" dentro do parágrafo usando `addEventListener` e manipulação do `textContent`.

## Perguntas de revisão

Por que JavaScript é praticamente obrigatório na web? :: Porque é a única linguagem que todo navegador executa, dando interatividade às páginas.

O que é programação orientada a eventos? :: Registrar funções que rodam quando algo acontece, como um clique, com addEventListener.

Por que operações demoradas em JavaScript são assíncronas? :: Para não travar a página enquanto esperam, por exemplo, uma resposta do servidor.

O que é o Node.js? :: Um ambiente que roda JavaScript fora do navegador, no servidor.

O que é TypeScript? :: JavaScript com tipagem estática, que aponta erros de tipo antes de rodar.

---
Próxima nota: [[09-SQL-e-Bancos-de-Dados]]
