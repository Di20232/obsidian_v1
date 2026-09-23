---
tags: [seguranca, web, xss, csp, frontend, flashcards]
aliases: [XSS, Cross-Site Scripting, CSP, Content Security Policy]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# XSS e CSP

**XSS** (Cross-Site Scripting) é injeção no navegador: texto do usuário que a página exibe **como HTML ou JavaScript** em vez de exibir como texto. O script roda com todos os poderes do usuário logado naquele site.

## O que um XSS consegue fazer

- Agir como a vítima: trocar e-mail da conta, fazer pedido, transferir, apagar.
- Ler o que está na página: dados pessoais, tokens em `localStorage`.
- Roubar o cookie de sessão, se ele **não** for `HttpOnly`.
- Mostrar um formulário falso de login dentro do site verdadeiro.

## Os três tipos

| Tipo | Onde o script fica | Exemplo |
|---|---|---|
| **Armazenado** | no banco; atinge todo mundo que abre a página | avaliação de produto com `<script>` |
| **Refletido** | na URL; atinge quem clica no link | `/busca?q=<script>...</script>` exibido como "Resultados para: ..." |
| **Baseado em DOM** | nunca passa pelo servidor; o próprio JavaScript da página injeta | `el.innerHTML = location.hash.slice(1)` |

## A defesa principal: escapar na saída, de acordo com o contexto

Escapar é transformar `<` em `&lt;`, `"` em `&quot;` e assim por diante, para o navegador mostrar o caractere em vez de interpretá-lo. **O contexto importa:**

| Onde o dado entra | O que fazer |
|---|---|
| Texto dentro de HTML | escape de HTML (o padrão dos motores de template) |
| Valor de atributo | escape de HTML **e** atributo entre aspas |
| URL (`href`, `src`) | aceitar só `https:` (e `http:`/`mailto:` se preciso); recusar `javascript:` |
| Dentro de `<script>` | evitar; passe o dado por `data-*` ou JSON (`tojson` no Jinja) |
| CSS | evitar dado do usuário em estilo |

### Frameworks já escapam — até você desligar

- **Jinja2 (Flask):** escapa automaticamente em arquivos `.html`. Desliga com `|safe`, `Markup()` e `{% autoescape false %}`.
- **React:** escapa o que está em `{}`. Desliga com `dangerouslySetInnerHTML`. Atenção: `<a href={urlDoUsuario}>` ainda aceita `javascript:` em várias versões — valide o esquema.
- **Vue:** `v-html`. **Svelte:** `{@html}`.
- **Streamlit:** `st.markdown(..., unsafe_allow_html=True)` e `st.html`. **Reflex:** `rx.html`.
- **JavaScript puro:** `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `eval`, `setTimeout("texto")`.

```js
el.innerHTML = comentario;     // ERRADO: interpreta HTML
el.textContent = comentario;   // CERTO: sempre texto
```

### Quando o usuário precisa mandar HTML

Editor de descrição de produto, comentário com negrito: aí é preciso **sanitizar** — remover tudo que não estiver numa lista de tags e atributos permitidos. Use biblioteca mantida:

- **Navegador/Node:** DOMPurify.
- **Python:** nh3 (o bleach, que era o padrão, foi descontinuado).

Nunca sanitize com expressão regular própria.

## CSP: a segunda camada

**Content Security Policy** é um cabeçalho que diz ao navegador **de onde** ele pode carregar e executar scripts. Mesmo que um XSS passe, o script injetado não roda.

```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-R4nd0m'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'
```

| Diretiva | Efeito |
|---|---|
| `default-src 'self'` | por padrão, só recursos do próprio domínio |
| `script-src 'self' 'nonce-...'` | só scripts do domínio ou com o *nonce* aleatório gerado a cada resposta |
| `object-src 'none'` | bloqueia plugins antigos |
| `base-uri 'none'` | impede trocar a base dos links relativos |
| `frame-ancestors 'none'` | ninguém coloca o site num iframe (contra clickjacking) |

- **Evite `'unsafe-inline'` e `'unsafe-eval'`** em `script-src`: eles anulam a proteção contra XSS.
- Comece com **`Content-Security-Policy-Report-Only`**: o navegador só avisa o que bloquearia, sem quebrar o site. Ajuste e depois ative.
- Scripts de terceiros (analytics, pixel de anúncio, chat) precisam entrar na política — cada um é um risco a mais. → [[16-Dependencias-e-Cadeia-de-Suprimentos|cadeia de suprimentos]]

## Outras camadas

- Cookie de sessão **`HttpOnly`**: o script não lê. → [[11-CSRF-e-Cookies|cookies]]
- Não guardar token em `localStorage`. → [[06-JWT-e-Tokens|tokens]]
- `X-Content-Type-Options: nosniff` e servir uploads como anexo. → [[13-SSRF-Uploads-e-Caminhos|uploads]]

## Perguntas de revisão

O que é XSS? :: Cross-Site Scripting: texto do usuário exibido pela página como HTML ou JavaScript, que roda com os poderes do usuário logado.

Quais são os três tipos de XSS? :: Armazenado (fica no banco), refletido (vem na URL) e baseado em DOM (o próprio JavaScript da página injeta sem passar pelo servidor).

Qual a defesa principal contra XSS? :: Escapar os dados na saída de acordo com o contexto (HTML, atributo, URL, script), o que os motores de template fazem por padrão.

Quais recursos desligam o escape automático nos frameworks? :: |safe e Markup no Jinja, dangerouslySetInnerHTML no React, v-html no Vue, unsafe_allow_html no Streamlit e innerHTML no JavaScript puro.

Qual a diferença entre innerHTML e textContent? :: innerHTML interpreta o texto como HTML e pode executar código; textContent sempre trata como texto.

O que fazer quando o usuário precisa enviar HTML? :: Sanitizar com biblioteca mantida e lista de tags permitidas, como DOMPurify no navegador ou nh3 em Python; nunca com regex própria.

O que é CSP? :: Content Security Policy, um cabeçalho que diz ao navegador de onde ele pode carregar e executar scripts, servindo de segunda camada contra XSS.

Por que evitar unsafe-inline no script-src da CSP? :: Porque permite scripts inline, exatamente o que um XSS injeta, anulando a proteção.

Como adotar CSP sem quebrar o site? :: Começar com Content-Security-Policy-Report-Only, que só relata o que seria bloqueado, ajustar e depois ativar.

Por que validar o esquema de URLs fornecidas pelo usuário em links? :: Porque href com javascript: executa código ao clicar mesmo quando o texto foi escapado.

---
Anterior: [[09-Injecao-SQL-e-Comandos|Injeção]] · Próxima: [[11-CSRF-e-Cookies|CSRF e cookies]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
