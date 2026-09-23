---
tags: [seguranca, web, cors, api, navegador, flashcards]
aliases: [CORS, Same-Origin Policy, Política de Mesma Origem]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# CORS

Todo desenvolvedor web já viu no console: *"blocked by CORS policy"*. Entender o que está acontecendo evita a "solução" mais comum — liberar tudo — que abre um buraco real.

## Primeiro: a política de mesma origem

**Origem** = esquema + host + porta.

| URL | Mesma origem que `https://loja.exemplo`? |
|---|---|
| `https://loja.exemplo/carrinho` | sim (só o caminho muda) |
| `http://loja.exemplo` | não (esquema) |
| `https://api.loja.exemplo` | não (host) |
| `https://loja.exemplo:8443` | não (porta) |

A **Same-Origin Policy** do navegador impede que o JavaScript de uma origem **leia a resposta** de outra. Sem ela, qualquer site que você abrisse poderia ler seu e-mail em outra aba.

## O que é CORS

**CORS** (Cross-Origin Resource Sharing) é o mecanismo para o **servidor** dizer ao navegador: "estas outras origens podem ler minhas respostas". Ele **relaxa** a política de mesma origem; não acrescenta proteção.

Três consequências que costumam confundir:

1. **Quem bloqueia é o navegador.** `curl`, Postman, um script Python ou outro servidor ignoram CORS completamente. CORS **não protege a API** de ninguém que não seja um navegador.
2. **A requisição pode chegar ao servidor mesmo quando o navegador bloqueia a leitura.** Em requisições simples (um POST de formulário, por exemplo) a ação já aconteceu; o navegador só esconde a resposta. Por isso CORS **não substitui** [[11-CSRF-e-Cookies|proteção contra CSRF]] nem [[08-Controle-de-Acesso|autorização]].
3. **Erro de CORS se corrige no servidor**, não no frontend.

## Preflight

Para requisições "não simples" — métodos como PUT, PATCH, DELETE; `Content-Type: application/json`; cabeçalhos próprios como `Authorization` — o navegador pergunta antes com um `OPTIONS`:

```http
OPTIONS /api/pedidos
Origin: https://painel.loja.exemplo
Access-Control-Request-Method: PATCH
Access-Control-Request-Headers: content-type, authorization
```

O servidor responde o que permite:

```http
Access-Control-Allow-Origin: https://painel.loja.exemplo
Access-Control-Allow-Methods: GET, POST, PATCH
Access-Control-Allow-Headers: content-type, authorization
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 600
Vary: Origin
```

## Os cabeçalhos

| Cabeçalho | Função |
|---|---|
| `Access-Control-Allow-Origin` | a origem liberada (uma só, ou `*`) |
| `Access-Control-Allow-Credentials: true` | permite enviar e ler com cookies; **não funciona com `*`** |
| `Access-Control-Allow-Methods` / `-Headers` | o que o preflight libera |
| `Vary: Origin` | avisa caches que a resposta muda conforme a origem |

## Configuração segura

**Lista fechada de origens**, comparação exata:

```js
import cors from 'cors';
app.use(cors({
  origin: ['https://loja.exemplo', 'https://painel.loja.exemplo'],
  credentials: true,
}));
```

```python
from flask_cors import CORS
CORS(app, origins=["https://loja.exemplo"], supports_credentials=True)
```

## Os erros que viram falha de segurança

| Erro | Por que é grave |
|---|---|
| Refletir qualquer `Origin` recebido **com** `Allow-Credentials: true` | qualquer site lê os dados do usuário logado — é como não ter a política de mesma origem |
| Validar com `endsWith("loja.exemplo")` ou regex frouxa | aceita `ataqueloja.exemplo` ou `loja.exemplo.atacante.com` |
| Liberar a origem `null` | páginas em sandbox e arquivos locais enviam `Origin: null`, e o atacante consegue gerá-la |
| `origin: '*'` numa API interna "porque dava erro" | expõe a quem estiver na rede ou na VPN |

`Access-Control-Allow-Origin: *` sem credenciais é aceitável para dados **realmente públicos** (catálogo aberto, CEP, fontes).

## Como evitar CORS no desenvolvimento

Com frontend em `localhost:5173` e API em `localhost:3000`, as origens são diferentes. Em vez de afrouxar o CORS da API, use o **proxy do servidor de desenvolvimento** (Vite, Next.js, Create React App): o navegador fala só com uma origem.

## Perguntas de revisão

O que define uma origem na web? :: A combinação de esquema, host e porta; mudar qualquer um dos três muda a origem.

O que a Same-Origin Policy impede? :: Que o JavaScript de uma origem leia as respostas de outra origem.

O que é CORS? :: Um mecanismo para o servidor dizer ao navegador quais outras origens podem ler suas respostas; ele relaxa a política de mesma origem.

CORS protege a API contra acessos de scripts e ferramentas como curl? :: Não; só o navegador aplica CORS. Outros clientes ignoram, então a API precisa de autenticação e autorização próprias.

CORS substitui a proteção contra CSRF? :: Não; em requisições simples a ação chega ao servidor mesmo quando o navegador bloqueia a leitura da resposta.

O que é uma requisição de preflight? :: Um OPTIONS que o navegador envia antes de requisições não simples para perguntar ao servidor quais origens, métodos e cabeçalhos ele permite.

Por que refletir qualquer Origin com Allow-Credentials true é grave? :: Porque qualquer site passa a ler os dados do usuário logado, anulando a política de mesma origem.

Access-Control-Allow-Origin * funciona com cookies? :: Não; com credenciais o navegador exige uma origem específica.

Onde se corrige um erro de CORS? :: No servidor, liberando a origem certa; no desenvolvimento, pode-se usar o proxy do servidor de desenvolvimento.

---
Anterior: [[11-CSRF-e-Cookies|CSRF e cookies]] · Próxima: [[13-SSRF-Uploads-e-Caminhos|SSRF, uploads e caminhos]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
