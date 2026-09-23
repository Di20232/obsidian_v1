---
tags: [seguranca, web, jwt, tokens, api, flashcards]
aliases: [JWT, JSON Web Token]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# JWT e tokens

Um **token** é uma credencial que o cliente apresenta a cada requisição, normalmente no cabeçalho `Authorization: Bearer <token>`. Existem dois tipos:

| Tipo | Como funciona | Revogar |
|---|---|---|
| **Opaco** | string aleatória sem significado; o servidor consulta o banco para saber de quem é | fácil: apaga a linha |
| **JWT** | carrega os dados dentro dele, assinados; o servidor confere a assinatura sem consultar o banco | difícil: vale até expirar |

## Anatomia de um JWT

```text
eyJhbGciOiJIUzI1NiJ9 . eyJzdWIiOiI0MiIsImV4cCI6MTc5MDAwMDAwMH0 . <assinatura>
      cabeçalho                        conteúdo (payload)
```

- As três partes são **Base64url** — isso é codificação, **não criptografia**. Qualquer pessoa lê o conteúdo colando o token num decodificador.
- A **assinatura** só garante que ninguém alterou o conteúdo sem a chave.

> [!danger] Nunca coloque segredo no payload
> CPF, e-mail, permissões internas detalhadas, dados de pagamento: tudo fica legível. Coloque só o mínimo (`sub` com o ID, `exp`, papéis quando necessário).

## As afirmações (claims) que importam

| Claim | Significado | Conferir? |
|---|---|---|
| `sub` | de quem é o token (ID do usuário) | sim |
| `exp` | quando expira | **sempre** |
| `iat` / `nbf` | quando foi emitido / a partir de quando vale | sim |
| `iss` | quem emitiu | sim, se houver mais de um emissor |
| `aud` | para qual sistema o token foi feito | sim — impede usar o token de um serviço em outro |

## Validação correta

O erro clássico é aceitar o algoritmo que **o token diz** usar. Ataques conhecidos:

- **`alg: none`**: o atacante remove a assinatura e diz que o token não é assinado.
- **Confusão de algoritmo**: o servidor espera RS256 (chave pública/privada), o atacante manda HS256 usando a chave **pública** como segredo.

Defesa: **fixar o algoritmo no servidor** e usar biblioteca madura.

```python
import jwt   # PyJWT

dados = jwt.decode(
    token,
    CHAVE,
    algorithms=["HS256"],          # lista fixa, nunca vinda do token
    audience="api-mercadinho",
    issuer="auth-mercadinho",
)                                   # exp é conferido automaticamente
```

```js
import jwt from 'jsonwebtoken';

const dados = jwt.verify(token, CHAVE, {
  algorithms: ['HS256'],
  audience: 'api-mercadinho',
  issuer: 'auth-mercadinho',
});
```

**HS256 ou RS256/ES256?** Com HS256, quem valida também pode emitir (mesmo segredo). Com RS256 ou ES256, só quem tem a chave privada emite e os outros serviços validam com a pública — melhor quando vários sistemas conferem o token.

A chave HS256 precisa ser **longa e aleatória** (32 bytes ou mais), guardada como [[15-Segredos-e-Configuracao-Segura|segredo]]. Chave curta pode ser quebrada por força bruta a partir de um único token.

## Vida curta + refresh token

Como um JWT não pode ser "desligado" antes de expirar:

- **Access token curto** (minutos).
- **Refresh token** longo, **opaco**, guardado no banco, usado só para pedir um access token novo.
- **Rotação:** cada uso do refresh token gera outro e invalida o anterior. Se um refresh token antigo aparecer de novo, é sinal de roubo — invalide a família inteira.
- Logout e "sair de todos os dispositivos" apagam os refresh tokens.

## Onde guardar no navegador

| Lugar | Risco |
|---|---|
| `localStorage` / `sessionStorage` | qualquer script da página lê: um [[10-XSS-e-CSP\|XSS]] rouba o token |
| Cookie `HttpOnly; Secure; SameSite` | script não lê; em troca, precisa de proteção contra [[11-CSRF-e-Cookies\|CSRF]] |
| Memória (variável JS) | some ao recarregar; costuma ser combinado com refresh token em cookie |

Para um sistema web próprio, a recomendação prática é **sessão no servidor com cookie `HttpOnly`**. JWT faz mais sentido entre serviços, em APIs para apps mobile e quando outro sistema emite o token (→ [[07-OAuth-e-OpenID-Connect|OAuth]]).

## Chaves de API

Para integrações entre sistemas (webhook, parceiro, script):

- Gerar aleatória, mostrar **uma única vez** e guardar só o **hash**.
- Usar um prefixo reconhecível (`mcd_live_...`), o que facilita achar vazamentos em repositórios.
- Dar **escopo** (só leitura, só pedidos) e permitir revogar e rotacionar.
- Nunca colocar no código do frontend: tudo que vai para o navegador é público.

## Perguntas de revisão

O conteúdo de um JWT é criptografado? :: Não; é só codificado em Base64url e qualquer pessoa lê. A assinatura garante apenas que não foi alterado.

Qual a diferença entre token opaco e JWT? :: O opaco é aleatório e o servidor consulta o banco para saber de quem é, podendo revogar fácil; o JWT carrega os dados assinados e vale até expirar.

Quais claims de um JWT devem ser sempre conferidas? :: A assinatura com algoritmo fixo, exp (expiração) e, quando houver, aud (destinatário) e iss (emissor).

O que é o ataque alg none? :: O atacante tira a assinatura e declara no cabeçalho que o token não é assinado; funciona em bibliotecas que aceitam o algoritmo indicado pelo próprio token.

Como evitar ataques de confusão de algoritmo no JWT? :: Fixando no servidor a lista de algoritmos aceitos, sem nunca usar o que vem no cabeçalho do token.

Quando preferir RS256 ou ES256 a HS256? :: Quando vários serviços precisam validar o token: só quem tem a chave privada emite, e os outros validam com a chave pública.

Por que usar access token curto com refresh token? :: Porque o JWT não pode ser revogado antes de expirar; vida curta limita o estrago e o refresh token, guardado no banco, pode ser revogado.

O que é rotação de refresh token? :: Cada uso gera um refresh token novo e invalida o anterior; se um antigo reaparecer, é sinal de roubo e toda a família é invalidada.

Qual o risco de guardar token no localStorage? :: Qualquer script da página consegue ler, então um XSS rouba o token.

Como guardar chaves de API no servidor? :: Só o hash, mostrando a chave uma única vez ao criar, com escopo limitado e possibilidade de revogar.

---
Anterior: [[05-Autenticacao-Sessoes-e-MFA|Autenticação e sessões]] · Próxima: [[07-OAuth-e-OpenID-Connect|OAuth e OpenID Connect]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
