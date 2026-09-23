---
tags: [problema-resolvido, seguranca, sql, python, streamlit, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# SQL injection latente por token vindo da URL

## Contexto

[[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]] · Streamlit · `app/data/repository.py` e `app/state.py` · encontrado na auditoria de segurança pedida pelo usuário.

## Sintoma e impacto

Nenhum sintoma em uso. É uma falha **latente**: não explorável hoje, mas armada para o dia em que alguém mudar uma linha de configuração.

## Causa-raiz

Duas peças que, separadas, pareciam inofensivas.

**Peça 1 — o nome da tabela entra cru na consulta:**

```python
def carregar(self, nome):
    return pd.read_sql(f'SELECT * FROM "{nome}"', conexao)

def remover(self, nome):
    conexao.execute(f'DROP TABLE IF EXISTS "{nome}"')
```

**Peça 2 — esse nome vem da URL, sem validação:**

```python
atual = st.query_params.get(CHAVE_SESSAO)   # ?s=...
return str(atual)
```

O nome da tabela vira `f"vendas:{token}"`, e o `token` é lido direto da query string.

**Por que não explode hoje:** o backend ativo é `MemoriaRepositorio`, que usa a string apenas como chave de dicionário. Nada de SQL acontece.

**Por que é grave mesmo assim:** o próprio arquivo documenta o `SQLiteRepositorio` como substituto direto, com um comentário sugerindo a troca para persistir entre sessões. No dia em que alguém trocar, uma URL com aspas dentro do parâmetro `?s=` vira injeção de SQL — sem que ninguém tenha tocado no código vulnerável.

> É o perfil clássico de falha latente: **a vulnerabilidade já está escrita; falta só alguém ativar o caminho até ela.**

## Correção aplicada

Sanitizar o token na origem, aceitando apenas caracteres seguros, e validar o nome da tabela antes de qualquer consulta — de modo que o `SQLiteRepositorio` já nasça seguro quando for ativado.

Severidade classificada como **média (latente)**: risco prático baixo hoje, alto após uma mudança de uma linha.

## Prevenção

> [!seguranca] Duas regras que se reforçam
> 1. **Todo dado que vem da URL é entrada hostil** — query string é tão externa quanto um formulário.
> 2. **Código morto que documenta como ser ativado não é código morto.** Se o comentário diz "troque por isto para persistir", trate esse caminho como se já estivesse em produção.

O mesmo padrão de identificador interpolado apareceu no [[09-Nome-de-Tabela-em-F-String-no-SQL|CTL-TINTA-FL]], por outro caminho. Vale procurar `f"SELECT` e `f"DROP` em qualquer projeto.

## Links relacionados

- Projeto: [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]]
- Prática: [[../Praticas/07-Seguranca-em-Apps-Locais|Segurança em apps locais]] · [[../Praticas/06-Caca-de-Bugs|Caça de bugs]]
- Relacionado: [[09-Nome-de-Tabela-em-F-String-no-SQL|O mesmo erro no CTL-TINTA-FL]]

## Perguntas de revisão

O que é uma falha latente? :: Uma vulnerabilidade já escrita no código que só fica explorável quando alguém ativa o caminho até ela.

Dados vindos da URL são confiáveis? :: Não; a query string é entrada tão externa e hostil quanto um formulário.

Por que código documentado para ser ativado não é código morto? :: Porque basta seguir o comentário para ativá-lo; deve ser tratado como se estivesse em produção.
