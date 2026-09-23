---
tags: [github, conceito, autenticacao, seguranca]
cssclasses: [cerebro-nota, cerebro-seguranca]
verificado_em: 2026-09-15
---
# Sessão, expiração e permissões atuais

## Problema 1: a conta foi desativada, mas o token ainda vale

Um token assinado identifica uma sessão. Um papel gravado nele pode ficar desatualizado depois de uma mudança administrativa.

**Solução no Contro Vend:** [[Cerebro/GitHub/contro-vend-public/Fontes/src/auth.js.md|authenticate]] verifica a assinatura e consulta o usuário atual no banco. A conta precisa continuar ativa e o papel usado na autorização vem dessa consulta. Assim, uma desativação ou mudança de papel não depende de aguardar a expiração do token.

## Problema 2: a tela continua “logada”, mas toda operação falha

**Solução no ByteShop:** o [[Cerebro/GitHub/byteShop/Fontes/frontend/src/api/client.ts.md|cliente HTTP]] identifica um 401 em requisição autenticada, remove o token local e encaminha ao login. Erros no próprio login/cadastro seguem o tratamento da tela.

## Diferença entre os projetos

| Tema | ByteShop | Contro Vend |
|---|---|---|
| Transporte do token | Bearer no cabeçalho | Cookie |
| Persistência consultada no cliente | localStorage | Cookie HttpOnly |
| Verificação de administrador | Dependência FastAPI | Middleware de papel |
| Controle do usuário atual | Consulta de usuário | Consulta de usuário ativo e papel |

São decisões da versão consultada. A proteção completa depende também de validação, política de origem, prevenção de XSS, transporte e configuração do servidor.

## Verificações úteis

Teste sessão expirada, token inválido, usuário sem papel administrativo e mudança de papel com uma sessão já existente. Não basta ocultar um botão: a rota precisa rejeitar a ação não autorizada.

[[Cerebro/Mapas/04-Mapa-Seguranca|Segurança]] · [[Cerebro/GitHub/00-Indice|GitHub]]

