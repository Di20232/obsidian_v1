---
tags: [javascript, web, dom, flashcards]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# DOM e Eventos

## A primeira nota desta trilha que só funciona no navegador

Tudo até aqui rodou com `node arquivo.js`, no terminal. Esta nota é diferente: o **DOM** só existe dentro de um navegador — é a árvore de elementos que representa a página HTML carregada (o conceito foi adiantado em [[../Programacao-Geral/07-HTML-e-CSS]] e em [[01-O-que-e-JavaScript]]). Não existe DOM no Node.js puro.

## Por que isso é o motivo original de JavaScript existir

HTML ([[../Programacao-Geral/07-HTML-e-CSS]]) descreve conteúdo estático. Sem JavaScript, uma página nunca muda depois de carregada, exceto recarregando inteira. O DOM é a "ponte" que permite ao JavaScript **ler e modificar** essa estrutura depois que a página já carregou — mudar texto, estilo, adicionar/remover elementos, tudo sem recarregar.

## Selecionando elementos

```html
<h1 id="titulo">Olá</h1>
<p class="texto">Um parágrafo</p>
```

```javascript
const titulo = document.getElementById("titulo");
const paragrafo = document.querySelector(".texto");    // seleciona pelo mesmo tipo de seletor do CSS
const todosOsParagrafos = document.querySelectorAll("p"); // vários de uma vez
```

`document` é o objeto global que representa a página inteira — o "ponto de entrada" para o DOM, disponível automaticamente em qualquer script rodando no navegador.

## Lendo e alterando conteúdo

```javascript
console.log(titulo.textContent);      // lê o texto atual
titulo.textContent = "Novo título";    // altera o texto

paragrafo.innerHTML = "Texto <strong>com HTML</strong> dentro";  // interpreta tags HTML
```

**Cuidado com `innerHTML`**: se o conteúdo vier de um usuário (não confiável, como visto em [[../Programacao-Geral/13-Boas-Praticas-de-Codigo]]), inserir diretamente com `innerHTML` permite que alguém injete código malicioso na página (um ataque chamado **XSS**). Prefira `textContent` sempre que só precisar de texto puro.

## Alterando estilo e classes

```javascript
titulo.style.color = "blue";
titulo.style.fontSize = "32px";

paragrafo.classList.add("destaque");     // adiciona uma classe CSS
paragrafo.classList.remove("antiga");     // remove uma classe
paragrafo.classList.toggle("ativo");       // liga/desliga uma classe
```

Isso conecta diretamente com os seletores de classe (`.destaque`) vistos em [[../Programacao-Geral/07-HTML-e-CSS]] — o CSS já define a aparência da classe `.destaque`; o JavaScript só decide **quando** aplicá-la.

## Criando e removendo elementos

```javascript
const novoParagrafo = document.createElement("p");
novoParagrafo.textContent = "Fui criado por JavaScript";
document.body.appendChild(novoParagrafo);   // adiciona à página

novoParagrafo.remove();   // remove da página
```

## Eventos: reagindo a ações do usuário

Um **evento** é algo que acontece na página — um clique, uma tecla pressionada, um formulário enviado. `addEventListener` registra uma função (callback, visto em [[14-Assincronismo]]) para rodar quando esse evento acontecer:

```javascript
const botao = document.getElementById("meu-botao");

botao.addEventListener("click", () => {
    console.log("Botão clicado!");
    paragrafo.textContent = "Você clicou!";
});
```

Outros eventos comuns: `"input"` (toda vez que o valor de um campo muda), `"submit"` (formulário enviado), `"keydown"` (tecla pressionada), `"mouseover"` (mouse passando por cima).

## Exemplo completo: HTML + JavaScript juntos

```html
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo DOM</title>
</head>
<body>
    <h1 id="titulo">Contador: 0</h1>
    <button id="botao">Clique aqui</button>

    <script>
        let contador = 0;
        const titulo = document.getElementById("titulo");
        const botao = document.getElementById("botao");

        botao.addEventListener("click", () => {
            contador++;
            titulo.textContent = `Contador: ${contador}`;
        });
    </script>
</body>
</html>
```

Isso é uma página funcional e interativa — o começo real de qualquer front-end web. Repare que a `<script>` fica no fim do `<body>`, depois dos elementos que ela referencia — isso garante que `getElementById` já encontre os elementos, porque eles já foram carregados antes do script rodar.

## Formulários: lendo o que o usuário digitou

```html
<input type="text" id="campo-nome">
<button id="botao-enviar">Enviar</button>
<p id="resultado"></p>

<script>
    document.getElementById("botao-enviar").addEventListener("click", () => {
        const nome = document.getElementById("campo-nome").value;   // .value lê o texto digitado
        document.getElementById("resultado").textContent = `Olá, ${nome}!`;
    });
</script>
```

Esse é, na prática, o equivalente no navegador do `input()` de Python ([[../Python/06-Entrada-e-Saida]]) — a diferença é que, em vez de pausar o programa esperando, você registra um evento que roda quando o usuário decide agir.

## Exercício

Abra `JavaScript/exemplos/16_dom.html` diretamente no navegador (duplo clique no arquivo, ou arraste para uma aba). Interaja com o botão e o campo de texto, depois abra o console (`F12`) para ver mensagens extras que o script escreve lá. Depois, tente adicionar você mesmo um segundo botão que muda a cor do título.

## Perguntas de revisão

O que é o DOM? :: A árvore de elementos que representa a página HTML carregada, permitindo ao JavaScript ler e modificar a página.

O DOM existe no Node.js? :: Não; só dentro do navegador.

Como selecionar elementos da página? :: Com document.getElementById, document.querySelector ou document.querySelectorAll.

Por que preferir textContent a innerHTML com dados do usuário? :: Porque innerHTML interpreta HTML e permite injetar código malicioso, o ataque XSS.

Como reagir a um clique num botão? :: Com addEventListener("click", funcao) no elemento.

Por que colocar o script no fim do body? :: Para que os elementos já existam quando o script procurá-los.

Como ler o texto digitado num campo input? :: Pela propriedade .value do elemento.

---
Próxima nota: [[17-Boas-Praticas-e-Proximos-Passos]]
