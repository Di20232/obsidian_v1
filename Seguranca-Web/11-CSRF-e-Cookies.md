---
tags: [seguranca, web, csrf, cookies, flashcards]
aliases: [CSRF, SameSite, Cookies Seguros]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# CSRF e cookies

## O ataque

**CSRF** (Cross-Site Request Forgery) faz o navegador da vítima enviar uma requisição a um site em que ela **está logada**, a partir de outro site. Funciona porque o navegador anexa os cookies do site de destino automaticamente.

```html
<!-- página do atacante -->
<form action="https://loja.exemplo/conta/email" method="POST">
  <input type="hidden" name="email" value="atacante@exemplo.com">
</form>
<script>document.forms[0].submit()</script>
```

Se a loja só confere o cookie de sessão, o e-mail da vítima é trocado — e com ele a recuperação de senha. O atacante não lê a resposta; ele só precisa que a **ação** aconteça.

**Condições para o CSRF:** a autenticação é enviada automaticamente (cookie, autenticação básica do navegador) e a ação muda estado sem nenhuma prova de que partiu do próprio site.

Uma API que só aceita `Authorization: Bearer` colocado por JavaScript não sofre CSRF clássico, porque o navegador não envia esse cabeçalho sozinho.

## As defesas

### 1. Token anti-CSRF (a principal)

Um valor aleatório, ligado à sessão, colocado em cada formulário e conferido no servidor. O site do atacante não consegue ler o token, então não consegue montar uma requisição válida.

```python
# Flask
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)          # exige o token em todo POST, PUT, PATCH e DELETE
```

```html
<form method="post">
  <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
  ...
</form>
```

A `SECRET_KEY` que assina o token precisa ser **fixa e persistida** — se mudar a cada reinício, todas as sessões e formulários abertos quebram. O cofre registrou isso em [[Cerebro/Praticas/07-Seguranca-em-Apps-Locais|segurança em apps locais]].

Para APIs chamadas por JavaScript, o padrão é enviar o token num cabeçalho (`X-CSRF-Token`).

### 2. Cookie com `SameSite`

Diz ao navegador quando **não** enviar o cookie em requisições vindas de outro site.

| Valor | Comportamento | Quando usar |
|---|---|---|
| `Strict` | nunca envia a partir de outro site, nem ao clicar num link | painel administrativo, banco |
| `Lax` | envia só em navegação de nível superior com método seguro (clicar num link, GET); não envia em POST de outro site nem em iframe/fetch | padrão bom para a maioria dos sites |
| `None` | envia sempre; **exige `Secure`** | widget embutido em outro domínio, SSO específico |

O Chrome trata cookies sem `SameSite` como `Lax`, mas nem todo navegador faz isso — **defina explicitamente**. E `SameSite` é camada extra: subdomínios do mesmo site ainda contam como "mesmo site".

### 3. Conferir a origem

Recusar requisições que mudam estado quando o cabeçalho `Origin` (ou `Sec-Fetch-Site: cross-site`) indica outro site.

### 4. GET nunca muda estado

`GET /pedidos/42/cancelar` pode ser disparado por uma simples imagem (`<img src=...>`) em qualquer página. Ação que muda dado usa POST, PUT, PATCH ou DELETE.

## Os atributos de um cookie de sessão

```http
Set-Cookie: __Host-sessao=9f3c...; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=28800
```

| Atributo | Protege contra |
|---|---|
| `Secure` | envio sem HTTPS |
| `HttpOnly` | leitura por JavaScript, ou seja, roubo por [[10-XSS-e-CSP\|XSS]] |
| `SameSite` | CSRF |
| `Max-Age` / `Expires` | sessão eterna |
| `Path=/` e **sem** `Domain` | vazamento para subdomínios |
| Prefixo `__Host-` | o navegador só aceita o cookie se tiver `Secure`, `Path=/` e nenhum `Domain` — impede que um subdomínio sobrescreva |

No Flask:

```python
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)
```

No Express (`express-session`): `cookie: { secure: true, httpOnly: true, sameSite: 'lax', maxAge: 8 * 3600 * 1000 }`. Atrás de proxy reverso com HTTPS, configure `app.set('trust proxy', 1)` para o `secure` funcionar.

## Clickjacking, o primo do CSRF

O atacante carrega o seu site num `iframe` invisível e faz a vítima clicar num botão real ("confirmar", "excluir") achando que clica em outra coisa. Defesa: `Content-Security-Policy: frame-ancestors 'none'` (ou `X-Frame-Options: DENY`). → [[14-Cabecalhos-de-Seguranca|cabeçalhos]]

## Perguntas de revisão

O que é CSRF? :: Cross-Site Request Forgery: outro site faz o navegador da vítima enviar uma requisição a um site em que ela está logada, aproveitando que os cookies são anexados automaticamente.

Quais as condições para um ataque CSRF funcionar? :: A autenticação é enviada automaticamente pelo navegador, como cookie, e a ação muda estado sem prova de que partiu do próprio site.

Qual a defesa principal contra CSRF? :: Um token aleatório ligado à sessão, incluído em cada formulário ou cabeçalho e conferido no servidor.

Por que a SECRET_KEY do Flask precisa ser persistida? :: Porque ela assina sessões e tokens CSRF; se mudar a cada reinício, todas as sessões e formulários abertos deixam de valer.

Qual a diferença entre SameSite Strict, Lax e None? :: Strict nunca envia o cookie a partir de outro site; Lax envia só em navegação com método seguro, como clicar num link; None envia sempre e exige Secure.

Por que uma ação que muda dados nunca deve usar GET? :: Porque um GET pode ser disparado por uma simples tag de imagem em qualquer página, sem interação da vítima.

O que faz o atributo HttpOnly de um cookie? :: Impede que JavaScript leia o cookie, protegendo a sessão contra roubo por XSS.

O que garante o prefixo __Host- no nome de um cookie? :: O navegador só aceita o cookie com Secure, Path=/ e sem Domain, impedindo que subdomínios o sobrescrevam.

Uma API que usa só Authorization Bearer definido por JavaScript sofre CSRF clássico? :: Não, porque o navegador não envia esse cabeçalho automaticamente a partir de outro site.

O que é clickjacking e como evitar? :: Carregar o site num iframe invisível para a vítima clicar em botões reais sem perceber; evita-se com frame-ancestors 'none' na CSP ou X-Frame-Options DENY.

---
Anterior: [[10-XSS-e-CSP|XSS e CSP]] · Próxima: [[12-CORS|CORS]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
