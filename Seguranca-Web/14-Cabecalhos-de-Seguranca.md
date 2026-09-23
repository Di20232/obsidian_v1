---
tags: [seguranca, web, http, cabecalhos, flashcards]
aliases: [Security Headers, Cabeçalhos HTTP de Segurança]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# Cabeçalhos de segurança

Alguns cabeçalhos HTTP ativam proteções que já existem no navegador. São baratos de configurar e fecham classes inteiras de ataque. Nenhum substitui código correto — são camadas de [[01-Principios-e-Modelo-de-Ameacas|defesa em profundidade]].

## Os que valem para quase todo site

| Cabeçalho | Valor inicial sugerido | Protege contra |
|---|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | acesso por HTTP interceptado → [[03-HTTPS-e-TLS\|HTTPS]] |
| `Content-Security-Policy` | política restritiva, testada antes em modo relatório | XSS, injeção de scripts de terceiros → [[10-XSS-e-CSP\|CSP]] |
| `X-Content-Type-Options` | `nosniff` | o navegador "adivinhar" que um upload é HTML ou script |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | vazar caminhos e parâmetros da URL para outros sites |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` | scripts usando recursos do dispositivo sem necessidade |
| `frame-ancestors` (na CSP) ou `X-Frame-Options` | `'none'` / `DENY` | clickjacking → [[11-CSRF-e-Cookies\|cookies]] |
| `Cross-Origin-Opener-Policy` | `same-origin` | páginas abertas por outro site manipularem a janela |
| `Cache-Control` em páginas com dado pessoal | `no-store` | dados sensíveis guardados em cache de computador compartilhado |

## O que remover

- **`X-Powered-By: Express`** e **`Server: nginx/1.18.0`** com versão: contam ao atacante qual vulnerabilidade procurar. No Express, `app.disable('x-powered-by')`; no nginx, `server_tokens off`.
- **`X-XSS-Protection`**: o filtro que ele controlava foi removido dos navegadores e o cabeçalho pode até criar problemas. Não use (ou defina `0`); a proteção moderna é a CSP.

## Como configurar

### Express: Helmet

```js
import helmet from 'helmet';
app.use(helmet());          // aplica um conjunto seguro de cabeçalhos, incluindo CSP padrão
```

Ajuste a CSP do Helmet para os scripts que o site realmente usa.

### Flask: manualmente

```python
@app.after_request
def cabecalhos(resp):
    resp.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    resp.headers["Content-Security-Policy"] = "default-src 'self'; object-src 'none'; frame-ancestors 'none'"
    return resp
```

Existe também a extensão **Flask-Talisman**, que faz o mesmo e força HTTPS.

### No proxy ou na hospedagem

nginx, Caddy, Cloudflare, Vercel e Netlify permitem definir cabeçalhos na configuração — útil para sites estáticos, onde não há código de servidor.

## Cuidados

- **HSTS é difícil de desfazer.** O navegador lembra pelo tempo do `max-age`. Comece com um valor curto (um dia), confirme que tudo funciona em HTTPS, inclusive os subdomínios, e só então aumente para um ano.
- **CSP quebra coisas** se aplicada de uma vez: comece com `Content-Security-Policy-Report-Only`.
- Cabeçalho aplicado só na página inicial não protege as outras: confira em várias rotas, inclusive nas respostas de erro e nos arquivos estáticos.

## Como conferir

- **DevTools do navegador → Rede (Network)** → clique na requisição → cabeçalhos da resposta.
- No terminal: `curl -I https://seusite.exemplo`.
- Serviços de análise de cabeçalhos (como o Mozilla HTTP Observatory) dão uma nota e explicam o que falta — use só no **seu** site.

## Perguntas de revisão

Para que serve o X-Content-Type-Options nosniff? :: Impede que o navegador adivinhe o tipo de um arquivo, por exemplo tratando um upload como HTML ou script.

Qual Referrer-Policy é um bom padrão? :: strict-origin-when-cross-origin, que envia só a origem para outros sites e nada ao sair de HTTPS para HTTP.

Para que serve o Permissions-Policy? :: Para desativar recursos do dispositivo, como câmera, microfone e localização, que o site não usa.

Como proteger contra clickjacking com cabeçalhos? :: Com frame-ancestors 'none' na CSP ou X-Frame-Options DENY.

Por que remover X-Powered-By e a versão do Server? :: Porque revelam a tecnologia e a versão, ajudando o atacante a escolher a vulnerabilidade.

Ainda se deve usar X-XSS-Protection? :: Não; o filtro foi removido dos navegadores. A proteção moderna é a CSP.

Por que começar o HSTS com max-age curto? :: Porque o navegador lembra da regra por todo o prazo; se algum subdomínio não funcionar em HTTPS, ele fica inacessível até expirar.

Qual biblioteca aplica cabeçalhos de segurança no Express? :: Helmet, com app.use(helmet()).

Quando usar Cache-Control no-store? :: Em páginas com dados pessoais ou sensíveis, para não ficarem em cache de computadores compartilhados.

---
Anterior: [[13-SSRF-Uploads-e-Caminhos|SSRF e uploads]] · Próxima: [[15-Segredos-e-Configuracao-Segura|Segredos e configuração]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
