---
tags: [javascript, conceitos]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# O que é JavaScript

## De onde vem, e por que é tão espalhado

JavaScript foi criado em 1995 para dar comportamento a páginas web dentro do navegador — antes dele, uma página era só texto e imagens estáticas, sem reagir a nada que o usuário fizesse. Décadas depois, é a única linguagem que **todo navegador do mundo** executa nativamente, o que a tornou, por consequência, a linguagem mais usada para código que roda no front-end da web (ver [[../Programacao-Geral/07-HTML-e-CSS]] e [[../Programacao-Geral/10-Como-a-Web-Funciona]] para o contexto de HTML/CSS/HTTP em torno disso).

Mais tarde, um ambiente chamado **Node.js** permitiu rodar JavaScript **fora** do navegador — em servidores, scripts de linha de comando, ferramentas de automação. É por isso que hoje se vê "front-end e back-end, tudo em JavaScript" no mesmo projeto.

## JavaScript vs. Python: mesma lógica, sintaxe diferente

Se você fez o [[../Python/00-Indice|curso de Python]], boa notícia: **os conceitos não mudam**. Variável, condicional, loop, função — tudo isso existe do mesmo jeito conceitualmente. O que muda é como se escreve. Ao longo desta trilha, vamos comparar com Python sempre que ajudar a fixar.

| Conceito | Python | JavaScript |
|---|---|---|
| Blocos de código | indentação (espaços) | chaves `{ }` |
| Fim de instrução | quebra de linha | `;` (geralmente opcional, mas convencional) |
| Exibir na tela | `print(...)` | `console.log(...)` |
| Comentário | `# comentário` | `// comentário` |

## Compilado ou interpretado?

Como visto em [[../Python/01-O-que-e-Programacao]], Python é interpretado. JavaScript também é — mais precisamente, os motores modernos (o **V8**, usado no Chrome e no Node.js, é o mais conhecido) compilam o código para uma forma intermediária **na hora**, bem rápido, logo antes de rodar (chamado JIT — Just-In-Time compilation). Na prática, para você, o efeito é o mesmo de uma linguagem interpretada: escreve o código, roda na hora, sem uma etapa manual de compilação separada.

## Onde JavaScript roda, hoje

- **No navegador**: toda página web interativa usa JS — é o que faz um botão reagir a um clique, um formulário se validar sem recarregar a página.
- **No servidor**, via **Node.js**: back-ends inteiros, scripts de automação, ferramentas de linha de comando.
- **Em apps mobile**: frameworks como React Native usam JavaScript para gerar apps nativos.
- **Em desktop**: frameworks como Electron (o VS Code, mencionado em [[../Python/02-Instalando-Python]], é construído com ele) usam JavaScript para criar aplicativos de desktop.

Essa presença em praticamente qualquer ambiente é o que torna JavaScript uma linguagem tão valiosa de conhecer, independente da área de programação que você escolher depois (ver [[../Programacao-Geral/14-Proximos-Passos-Trilhas]]).

## Vocabulário que você vai ver sempre

- **Motor JavaScript (JS engine)**: o programa que executa o código — V8 (Chrome, Node.js), SpiderMonkey (Firefox), entre outros.
- **Runtime**: o ambiente completo em que o código roda, incluindo o motor mais funcionalidades extras (o navegador adiciona o DOM, ver [[16-DOM-e-Eventos]]; o Node.js adiciona acesso a arquivos, rede, etc.).
- **ECMAScript**: o nome oficial do **padrão** da linguagem — "JavaScript" é, tecnicamente, a implementação mais popular desse padrão. Você vai ver termos como "ES6" (ou "ES2015") se referindo a uma versão específica desse padrão que trouxe mudanças importantes (como `let`/`const`, vistos em [[04-Variaveis-e-Tipos]]).

## Exercício

Sem escrever código ainda: liste três coisas que você usa no dia a dia que provavelmente rodam JavaScript por trás (dica: qualquer site que reage sem recarregar a página inteira — um feed que carrega mais posts ao rolar, um carrinho de compras que atualiza o total sem sair da página).

---
Próxima nota: [[02-Preparando-o-Ambiente]]
