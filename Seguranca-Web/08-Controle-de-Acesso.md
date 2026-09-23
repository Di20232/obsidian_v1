---
tags: [seguranca, web, autorizacao, controle-de-acesso, idor, flashcards]
aliases: [IDOR, Autorização]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# Controle de acesso

É o **risco número 1** do [[02-OWASP-Top-10|OWASP Top 10:2025]]. E quase nunca é um erro sofisticado: é uma rota que esqueceu de perguntar **"este dado é deste usuário?"**.

- **Autenticação:** quem é você.
- **Autorização (controle de acesso):** o que você pode ver e fazer.

Estar logado não autoriza nada por si só.

## IDOR: o erro mais comum

**IDOR** (Insecure Direct Object Reference; em APIs, também chamado **BOLA**) acontece quando a rota usa o ID que veio na requisição sem conferir o dono.

```python
# ERRADO: qualquer usuário logado vê qualquer pedido trocando o número na URL
@app.get("/pedidos/<int:pedido_id>")
@login_required
def ver_pedido(pedido_id):
    pedido = db.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,)).fetchone()
    return render_template("pedido.html", pedido=pedido)
```

```python
# CERTO: a consulta já filtra pelo dono
@app.get("/pedidos/<int:pedido_id>")
@login_required
def ver_pedido(pedido_id):
    pedido = db.execute(
        "SELECT * FROM pedidos WHERE id = ? AND cliente_id = ?",
        (pedido_id, current_user.id),
    ).fetchone()
    if pedido is None:
        abort(404)            # não revela se o pedido existe para outra pessoa
    return render_template("pedido.html", pedido=pedido)
```

O mesmo com Prisma:

```js
const pedido = await prisma.pedido.findFirst({
  where: { id: pedidoId, clienteId: usuario.id },   // nunca só { id }
});
if (!pedido) return res.status(404).end();
```

> [!warning] ID difícil de adivinhar não é autorização
> Trocar `/pedidos/123` por um UUID dificulta a tentativa, mas o ID vaza em e-mails, logs, capturas de tela e histórico do navegador. A checagem de dono continua obrigatória.

## Tipos de escalada

| Tipo | Exemplo |
|---|---|
| **Horizontal** — acessar dados de outro usuário do mesmo nível | cliente A vê o pedido do cliente B |
| **Vertical** — fazer o que só um papel superior pode | vendedor acessa `/admin/usuarios` digitando a URL |
| **Por atribuição em massa** (*mass assignment*) | o formulário de perfil aceita `{"nome": "Ana", "papel": "admin"}` porque o código faz `usuario.update(**request.json)` |

Contra atribuição em massa: **lista de campos permitidos** por rota.

```python
CAMPOS_PERFIL = {"nome", "telefone"}
dados = {k: v for k, v in request.json.items() if k in CAMPOS_PERFIL}
```

## Regras que evitam a maioria dos casos

1. **Negar por padrão.** Toda rota exige login e permissão, exceto as liberadas explicitamente.
2. **Checar no servidor, em toda requisição.** Esconder o botão no frontend é experiência de uso, não segurança — a URL e a API continuam lá.
3. **Filtrar pelo dono na própria consulta**, não buscar e comparar depois (é fácil esquecer o "depois").
4. **Centralizar a regra:** um decorador, middleware ou função `pode(usuario, acao, recurso)` usada em todas as rotas, em vez de `if` espalhado.
5. **Preço, desconto, papel e dono vêm do servidor.** O carrinho manda `produto_id` e `quantidade`; o preço é lido do banco.
6. **Ações sensíveis pedem confirmação** (senha de novo, MFA) e ficam em [[17-Logs-Monitoramento-e-Incidentes|log]].
7. **Responder 404 em vez de 403** quando revelar a existência do recurso já é vazamento.

## Modelos de permissão

| Modelo | Como decide | Bom para |
|---|---|---|
| **RBAC** — por papel | admin, gerente, caixa, cliente | a maioria dos sistemas de pequeno negócio |
| **ABAC** — por atributo | "gerente da **mesma loja**", "em horário comercial" | regras que dependem do contexto |
| **Por dono (ownership)** | "o registro é seu" | dados de cliente, pedidos, documentos |

Na prática, combina-se papel **e** dono: o gerente vê os pedidos **da loja dele**.

## Sistemas com várias empresas (multi-tenant)

Quando o mesmo sistema atende várias lojas, **toda** consulta precisa do filtro de empresa (`WHERE loja_id = ?`). Um único relatório esquecido mostra o faturamento de um cliente para outro. Defesas:

- Pegar o `loja_id` da sessão, nunca da requisição.
- Aplicar o filtro numa camada central (repositório, middleware do ORM).
- No PostgreSQL, **Row-Level Security** faz o banco recusar linhas de outra empresa mesmo se o código esquecer.

## Como testar

- Crie **dois usuários comuns** e um admin. Com o usuário A, tente abrir, editar e apagar cada recurso do usuário B pela URL e pela API.
- Com usuário comum, chame cada rota de admin diretamente.
- Automatize esses casos em testes: é a regressão que mais volta.

## Perguntas de revisão

Qual a diferença entre autenticação e autorização? :: Autenticação confirma quem é o usuário; autorização decide o que ele pode ver e fazer.

O que é IDOR? :: Insecure Direct Object Reference: a rota usa o ID enviado pelo cliente sem conferir se o recurso pertence ao usuário.

Como corrigir um IDOR? :: Filtrar pelo dono na própria consulta, por exemplo WHERE id = ? AND cliente_id = usuário logado, e responder 404 se não achar.

Usar UUID no lugar de ID numérico resolve o IDOR? :: Não; dificulta adivinhar, mas o ID vaza em e-mails, logs e histórico. A checagem de dono continua obrigatória.

Qual a diferença entre escalada horizontal e vertical de privilégio? :: Horizontal é acessar dados de outro usuário do mesmo nível; vertical é fazer ações de um papel superior, como admin.

O que é mass assignment e como evitar? :: Aceitar do cliente campos que ele não deveria definir, como papel ou preço; evita-se com lista de campos permitidos por rota.

Esconder o botão de admin no frontend protege a função? :: Não; a rota e a API continuam acessíveis. A checagem tem de ser feita no servidor em toda requisição.

Por que o preço do carrinho deve vir do servidor? :: Porque tudo que vem do cliente pode ser alterado; o cliente envia só produto e quantidade.

Qual o cuidado principal em sistemas multi-tenant? :: Filtrar toda consulta pela empresa da sessão, de preferência numa camada central ou com Row-Level Security no banco.

Como testar controle de acesso na prática? :: Com dois usuários comuns e um admin, tentar abrir, editar e apagar os recursos de um com o outro e chamar rotas de admin com usuário comum, automatizando esses testes.

---
Anterior: [[07-OAuth-e-OpenID-Connect|OAuth e OpenID Connect]] · Próxima: [[09-Injecao-SQL-e-Comandos|Injeção de SQL e comandos]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
