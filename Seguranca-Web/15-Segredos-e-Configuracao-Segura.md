---
tags: [seguranca, web, segredos, configuracao, devops, flashcards]
aliases: [Segredos, .env, Security Misconfiguration]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# Segredos e configuração segura

**Configuração insegura** é o risco número 2 do [[02-OWASP-Top-10|OWASP Top 10:2025]]. O código pode estar perfeito e o sistema cair por uma chave no GitHub, um modo debug esquecido ou uma senha padrão.

## O que é segredo

Tudo que dá acesso: senha do banco, `SECRET_KEY` do Flask, chave de API (pagamento, e-mail, IA, frete), token de acesso a marketplace, chave privada de certificado, credencial da nuvem, segredo de webhook.

## Onde os segredos ficam

- Em **variáveis de ambiente**, carregadas de um `.env` só na máquina local ou definidas no painel da hospedagem.
- **`.env` no `.gitignore`** desde o primeiro commit. Confira com `git ls-files --error-unmatch .env` — se ele encontrar o arquivo, há problema (→ [[Cerebro/Praticas/07-Seguranca-em-Apps-Locais|segurança em apps locais]]).
- Um **`.env.example`** versionado, com os **nomes** das variáveis e valores de mentira, documenta o que precisa ser configurado.
- Em produção maior: um cofre de segredos (do provedor de nuvem, Doppler, Vault).
- **Segredos diferentes por ambiente**: desenvolvimento, homologação e produção nunca compartilham a mesma chave.

```python
import os
SECRET_KEY = os.environ["SECRET_KEY"]        # falha na hora se faltar — melhor que um padrão inseguro
```

> [!danger] Variável "pública" do frontend é pública de verdade
> Tudo que vai para o navegador pode ser lido por qualquer um. No Vite, variáveis `VITE_*`; no Next.js, `NEXT_PUBLIC_*`; em Create React App, `REACT_APP_*` — entram no JavaScript enviado ao usuário. **Chave secreta de API nunca vai para o frontend**: o frontend chama o seu backend, e o backend chama a API.

## Quando um segredo vaza

Um commit com a chave, mesmo apagado no commit seguinte, **continua no histórico** — e repositórios públicos são varridos por robôs em minutos.

1. **Revogar e gerar outra chave imediatamente.** Esse é o passo que resolve; o resto é limpeza.
2. Conferir nos logs do serviço se a chave foi usada por outro.
3. Remover do histórico (`git filter-repo`) se o repositório for público ou for ser compartilhado — sabendo que clones e forks antigos continuam com a chave.
4. Registrar o incidente. → [[17-Logs-Monitoramento-e-Incidentes|incidentes]]

**Prevenção:** o GitHub tem *secret scanning* e *push protection*, que bloqueiam o push quando reconhecem uma chave conhecida; ferramentas como o **gitleaks** fazem a mesma varredura localmente ou num gancho de pré-commit.

> [!seguranca] Este cofre também
> Nunca registre aqui senha, token, chave ou `.env` real. Anote o **nome** da variável e onde obtê-la.

## Configuração insegura: os clássicos

| Erro | Consequência |
|---|---|
| **Flask com `debug=True` em produção** | o depurador do Werkzeug permite **executar código Python** no servidor pelo navegador, protegido só por um PIN |
| Mensagens de erro detalhadas para o usuário | revelam SQL, caminhos, versões e trechos de código |
| Senha padrão (`admin/admin`, `postgres/postgres`) | primeira coisa que qualquer robô testa |
| Banco, Redis ou painel escutando em `0.0.0.0` sem necessidade | exposto a toda a rede ou à internet → [[Cerebro/Ambiente/02-Portas-e-Conflitos\|portas]] |
| Listagem de diretório ligada | qualquer um navega pelos arquivos |
| `.git` ou `.env` acessíveis pela web | download do código e dos segredos |
| Bucket de armazenamento na nuvem público | vazamento de backups, notas fiscais, documentos |
| Rotas de teste, `/admin` sem senha, Swagger aberto em produção | superfície de ataque desnecessária |
| CORS `*` com credenciais | → [[12-CORS\|CORS]] |

## Erros e exceções (A10)

A categoria nova do Top 10:2025, **tratamento ruim de condições excepcionais**, cobre:

- **Falhar aberto:** `try: checa_permissao() except: pass` libera o acesso quando a checagem quebra. Falhe **fechado**.
- **Vazar detalhes:** mostre ao usuário uma mensagem genérica com um **código de referência**; os detalhes vão para o log com o mesmo código.
- **Estado pela metade:** pagamento aprovado e estoque não baixado porque uma exceção interrompeu no meio. Use **transações** no banco para operações que precisam acontecer juntas.
- **`except Exception` genérico** esconde a falha real. → [[Cerebro/Praticas/07-Seguranca-em-Apps-Locais|segurança em apps locais]]

```python
@app.errorhandler(500)
def erro_interno(e):
    ref = uuid4().hex[:8]
    app.logger.exception("erro %s", ref)                  # detalhes só no log
    return render_template("erro.html", ref=ref), 500      # usuário vê só o código
```

## Configuração como código

- Toda configuração de produção **documentada e reproduzível** (arquivo de deploy, Dockerfile, variáveis listadas no `.env.example`), não ajustada à mão no servidor.
- **Menor privilégio** para cada credencial: o usuário do banco da aplicação não é superusuário; a chave de API da loja só tem os escopos usados.
- Revisar a configuração a cada mudança de infraestrutura, com a [[18-Checklist-de-Seguranca-Web|checklist]].

## Perguntas de revisão

Onde guardar segredos de uma aplicação? :: Em variáveis de ambiente, carregadas de um .env fora do Git na máquina local, definidas no painel da hospedagem ou num cofre de segredos em produção.

Para que serve o .env.example? :: Para documentar no repositório os nomes das variáveis necessárias, com valores de mentira.

Variáveis como VITE_ ou NEXT_PUBLIC_ podem guardar chaves secretas? :: Não; elas entram no JavaScript enviado ao navegador e qualquer pessoa pode ler.

Qual o primeiro passo quando uma chave vaza no Git? :: Revogar a chave e gerar outra imediatamente; apagar o commit não basta porque ela continua no histórico e em clones.

Que ferramentas detectam segredos antes do push? :: O secret scanning com push protection do GitHub e ferramentas locais como o gitleaks.

Por que debug=True do Flask em produção é grave? :: Porque o depurador do Werkzeug permite executar código Python no servidor pelo navegador, protegido apenas por um PIN.

Como mostrar erros sem vazar detalhes? :: Exibir ao usuário uma mensagem genérica com um código de referência e gravar os detalhes no log com o mesmo código.

O que significa falhar aberto e por que é um erro? :: Liberar o acesso quando a checagem de segurança dá erro, como um except pass em volta da checagem de permissão; o certo é negar.

Como evitar estado pela metade quando uma exceção interrompe uma operação? :: Usando transação no banco para as etapas que precisam acontecer juntas.

Por que usar segredos diferentes por ambiente? :: Para que o vazamento da chave de desenvolvimento ou de teste não dê acesso à produção.

---
Anterior: [[14-Cabecalhos-de-Seguranca|Cabeçalhos]] · Próxima: [[16-Dependencias-e-Cadeia-de-Suprimentos|Dependências e cadeia de suprimentos]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
