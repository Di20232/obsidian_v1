---
tags: [seguranca, web, oauth, oidc, autenticacao, flashcards]
aliases: [OAuth, OpenID Connect, OIDC, PKCE]
cssclasses: [cerebro-nota, cerebro-seguranca]
verificado_em: 2026-09-23
fonte: https://www.rfc-editor.org/rfc/rfc9700.html
---

# OAuth e OpenID Connect

"Entrar com Google", "Conectar sua conta do Mercado Livre", "Autorizar este app a ler sua agenda": tudo isso é **OAuth 2.0**. Ele resolve um problema específico — **dar a um sistema acesso limitado a outro sem entregar a senha** — e é fácil de usar errado.

## OAuth não é login

| | Para que serve | Entrega |
|---|---|---|
| **OAuth 2.0** | **autorização delegada**: o app pode fazer X na minha conta de Y | *access token* |
| **OpenID Connect (OIDC)** | **autenticação**: uma camada sobre o OAuth que diz quem é o usuário | *ID token* (um [[06-JWT-e-Tokens\|JWT]] com `sub`, `email`, `iss`, `aud`...) |

"Entrar com Google" é OIDC. Usar um access token do OAuth como prova de identidade é um erro antigo: um token emitido para **outro** app pode ser apresentado ao seu.

## Os papéis

- **Dono do recurso** — o usuário.
- **Cliente** — o seu sistema, que quer acesso.
- **Servidor de autorização** — quem mostra a tela de login e consentimento e emite tokens (Google, Mercado Livre, Auth0, Keycloak).
- **Servidor de recursos** — a API que aceita o token (Google Calendar, API do Mercado Livre).

## O fluxo certo: authorization code + PKCE

```text
1. Seu app gera code_verifier (aleatório) e code_challenge = SHA-256(code_verifier)
2. Redireciona o usuário para o servidor de autorização com:
     client_id, redirect_uri, scope, state (aleatório), code_challenge
3. Usuário faz login lá e consente
4. Servidor redireciona de volta para redirect_uri com ?code=...&state=...
5. Seu app confere se o state é o mesmo que gerou
6. Seu servidor troca o code por tokens, enviando o code_verifier
7. O servidor de autorização confere que SHA-256(code_verifier) = code_challenge
```

- **`state`** amarra a resposta à requisição que o seu app iniciou (proteção contra CSRF no retorno).
- **PKCE** (lê-se "pixie") garante que só quem começou o fluxo consegue trocar o código por token, mesmo que o código seja interceptado.
- **`nonce`**, no OIDC, amarra o ID token à sessão e impede reaproveitamento.

## O que a RFC 9700 (janeiro de 2025) determina

A RFC 9700 é a "melhor prática atual" de segurança do OAuth 2.0 publicada pela IETF:

| Regra | Nível |
|---|---|
| Clientes públicos (SPA, app mobile) **devem** usar PKCE | obrigatório |
| Clientes confidenciais (com backend) — PKCE **recomendado** | recomendado |
| Fluxo **implícito** (token direto na URL) | **não deve** ser usado |
| Fluxo de **senha do dono do recurso** (o app pede usuário e senha e repassa) | **não pode** ser usado |
| `redirect_uri` comparada por **igualdade exata** de string | obrigatório |

Por que a URL de retorno exata importa: se o servidor aceitar curingas como `https://*.loja.exemplo/*`, uma implementação ingênua pode aceitar um domínio do atacante — e o código de autorização vai para ele.

## Outros fluxos

- **Client credentials:** sistema falando com sistema, sem usuário (ex.: seu backend chamando a API de um ERP). O segredo do cliente fica **só no servidor**.
- **Device code:** TVs e terminais sem teclado ("acesse este site e digite o código").

## Checklist para integrar "Entrar com..."

- [ ] Usar a **biblioteca oficial ou certificada** (Authlib em Python, openid-client ou Auth.js em Node) em vez de montar o fluxo à mão.
- [ ] Authorization code + PKCE; `state` e `nonce` aleatórios, conferidos no retorno.
- [ ] **Validar o ID token:** assinatura, `iss`, `aud` igual ao seu `client_id`, `exp`, `nonce`.
- [ ] Identificar o usuário por **`iss` + `sub`**, não pelo e-mail — e-mail muda e, em alguns provedores, não é verificado.
- [ ] Pedir o **mínimo de escopos** (`openid email`, não "acesso total ao Drive").
- [ ] `client_secret` só no backend, nunca no frontend nem no repositório.
- [ ] Guardar os tokens de acesso a APIs de terceiros (ex.: token do Mercado Livre para o ERP) **criptografados** no banco e renovar antes de expirar.

## Perguntas de revisão

Qual a diferença entre OAuth 2.0 e OpenID Connect? :: OAuth faz autorização delegada e entrega um access token; OpenID Connect é uma camada sobre ele que faz autenticação e entrega um ID token dizendo quem é o usuário.

Por que não usar um access token do OAuth como prova de login? :: Porque um token emitido para outro aplicativo pode ser apresentado ao seu; a prova de identidade é o ID token do OIDC, com aud igual ao seu client_id.

Qual o fluxo OAuth recomendado para aplicações com usuário? :: Authorization code com PKCE.

O que o PKCE garante? :: Que só quem iniciou o fluxo, e tem o code_verifier, consegue trocar o código de autorização por tokens.

Para que serve o parâmetro state no OAuth? :: Para amarrar o retorno à requisição que o próprio app iniciou, protegendo contra CSRF no callback.

O que a RFC 9700 diz sobre o fluxo implícito e o de senha? :: O implícito não deve ser usado; o de senha do dono do recurso não pode ser usado.

Como a RFC 9700 manda comparar a redirect_uri? :: Por igualdade exata de string, sem curingas.

Qual fluxo usar quando um sistema chama outro sem usuário envolvido? :: Client credentials, com o segredo guardado só no servidor.

Por que identificar o usuário do login social por iss e sub em vez do e-mail? :: Porque o e-mail pode mudar e nem sempre é verificado pelo provedor; iss mais sub é o identificador estável.

---
Anterior: [[06-JWT-e-Tokens|JWT e tokens]] · Próxima: [[08-Controle-de-Acesso|Controle de acesso]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
