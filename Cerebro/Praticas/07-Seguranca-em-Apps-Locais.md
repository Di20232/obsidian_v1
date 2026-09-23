---
tags: [pratica, seguranca, banco-de-dados, flashcards]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# Segurança em aplicações locais

Um sistema que "roda só na minha máquina" costuma ser tratado como isento de segurança. As auditorias do [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] e do [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]] mostraram por que isso não se sustenta.

## Por que local não significa seguro

**1. Local hoje, em rede amanhã.** Basta alguém perguntar *como outra pessoa acessa este link?* — e a pergunta apareceu de fato. → [[../Problemas-Resolvidos/13-Acesso-Externo-ao-Localhost|caso real]]

**2. Falha latente não precisa de atacante para virar problema.** Uma troca de backend documentada em comentário transforma código inofensivo em injeção de SQL. → [[../Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL|caso real]]

**3. Hábito viaja.** O padrão que você aceita no app local é o que vai escrever no app público.

## As regras confirmadas na prática

### SQL: valor e identificador são mundos diferentes

```python
cur.execute("SELECT * FROM itens WHERE id = ?", (item_id,))   # valor → parâmetro
```

```python
if tabela not in TABELAS_VALIDAS:                              # identificador → allowlist
    raise ValueError("tabela invalida")
```

Parâmetro `?` **não funciona** para nome de tabela ou coluna — por isso a lista de permissão fechada é obrigatória, não opcional. → [[../Problemas-Resolvidos/09-Nome-de-Tabela-em-F-String-no-SQL|caso real]]

### Toda entrada externa é hostil — inclusive a URL

Query string é tão externa quanto um formulário. `st.query_params`, `request.args`, parâmetros de rota: tudo entra validado.

### Upload se valida depois da descompressão

Tamanho do arquivo comprimido é métrica enganosa. Limite linhas e bytes **expandidos**. → [[../Problemas-Resolvidos/22-Decompression-Bomb-em-XLSX|caso real]]

### Formulário web precisa de CSRF

Implementado com `hmac` na fase Flask do CTL-TINTA-FL. Detalhe que se esquece: a `secret_key` tem que ser **persistida**, senão cada restart invalida todas as sessões.

### Segredos ficam fora do repositório

`.env` no `.gitignore`. Confirme com:

```bash
git ls-files --error-unmatch .env
```

Se ele **encontrar** o arquivo, há problema.

> [!seguranca] Este cofre também
> Nunca registre aqui senha, token, chave privada, `.env` real ou dado de cliente. Anote o **nome da variável** e onde obtê-la — nunca o valor.

### Exceção genérica esconde falha grave

`except Exception` captura tudo e mascara erros que deveriam ser vistos. Prefira exceções específicas (`ValueError`, `sqlite3.IntegrityError`) e **registre em log**, não em `print` — `print` não persiste e some quando ninguém está olhando o console.

## Links relacionados

- Prática: [[06-Caca-de-Bugs|Caça de bugs]]
- Mapa: [[../Mapas/04-Mapa-Seguranca|Mapa de Segurança]]

## Perguntas de revisão

Por que um app local também precisa de segurança? :: Porque local hoje pode ir para a rede amanhã, falhas latentes podem ser ativadas e o hábito do app local vai para o app público.

Para que serve um token CSRF em formulários? :: Para impedir que outro site envie formulários em nome do usuário; a chave secreta precisa ser persistida para não invalidar sessões a cada reinício.

Como verificar se o .env está no Git? :: Com git ls-files --error-unmatch .env; se o arquivo for encontrado, há um problema.

Por que registrar erros em log e não em print? :: Porque o print não persiste e some quando ninguém está olhando o console.

O que registrar sobre segredos no cofre? :: Só o nome da variável e onde obtê-la, nunca o valor.
