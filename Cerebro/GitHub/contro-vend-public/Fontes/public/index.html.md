---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-dados]
source: https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/public/index.html
source_commit: 8ca882161809413bbadfe4997e80a2ec7ae29991
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# public/index.html

Origem: [Di20232/contro-vend-public](https://github.com/Di20232/contro-vend-public/blob/8ca882161809413bbadfe4997e80a2ec7ae29991/public/index.html). Versao consultada: 8ca882161809.

[[Cerebro/GitHub/contro-vend-public/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--contro-vend-public--8ca882161809.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Contro Vend — Entrar</title>
  <link rel="stylesheet" href="/css/style.css" />
</head>
<body>
  <main class="login-wrap">
    <form id="login-form" class="card login-card">
      <div class="brand-mark" aria-hidden="true">CV</div>
      <h1>Contro Vend</h1>
      <p class="muted">Controle de vendas e estoque</p>

      <label for="email">E-mail</label>
      <input id="email" name="email" type="email" autocomplete="username" required maxlength="255" />

      <label for="password">Senha</label>
      <input id="password" name="password" type="password" autocomplete="current-password" required maxlength="200" />

      <button type="submit">Entrar</button>
      <p id="login-error" class="error" role="alert" hidden></p>
    </form>
  </main>

  <script src="/js/api.js"></script>
  <script src="/js/login.js"></script>
</body>
</html>

```
