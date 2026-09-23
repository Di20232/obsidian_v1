---
tags: [projeto, python, reflex, sqlite, estoque, flashcards]
status: em-desenvolvimento
cssclasses: [cerebro-nota, cerebro-projetos]
---

# CTL-TINTA-FL

> [!projeto] Origem
> Registro extraído das sessões de trabalho no Claude Code. Volta para [[00-Indice|📦 Projetos]].

## O que é

Sistema **local e offline** para controlar a compra e o despacho de **tinta e toner de impressora** para as **16 filiais** da empresa, com relatórios por filial, departamento e período.

Todo o banco é **um único arquivo**: `controle_suprimentos.db` (SQLite). Backup = copiar esse arquivo.

- **Repositório:** `C:\Users\Perim\Documents\GitHub\CTL-TINTA-FL` — publicado como [`Di20232/CTL-TINTA`](https://github.com/Di20232/CTL-TINTA)
- **Rodar:** duplo clique em `iniciar.bat`, ou `py -m reflex run --loglevel error`
- **URL:** `http://localhost:3000`

> [!problema] Repositório público vazio
> Em 15/09/2026 a API do GitHub retornou `Di20232/CTL-TINTA` **sem nenhum arquivo publicado** — ver [[../GitHub/CTL-TINTA/00-Indice|estado observado]]. Ou seja: todo o trabalho descrito nesta nota existe **localmente**, mas ainda não foi enviado (`git push`) para esse repositório. Vale confirmar com o usuário se o remoto está configurado antes de presumir que o código está salvo em algum lugar além da máquina.

## As três vidas deste projeto

Este projeto trocou de pele duas vezes — vale entender por quê:

| Fase | Stack | Por que mudou |
|---|---|---|
| 1. Original | **Tkinter** (~920 linhas, 5 abas) | Funcional, mas interface datada. Usuário pediu "um front-end bonito" |
| 2. Web | **Flask + Jinja2** (~60 rotas, 7 templates) | Entregue e validado com screenshots. Depois decidiu-se ir para algo mais moderno |
| 3. Atual | **Reflex** (Python puro que compila para React) | Stack atual. `db.py` foi reaproveitado **integralmente** nas três fases |

> 💡 **A lição:** a camada de banco (`db.py`) sobreviveu a duas trocas completas de interface. Separar dados de apresentação pagou-se sozinho.

Em 14/09 o usuário mandou remover tudo relacionado a executável: *"como vai ser apenas um website o app executável na máquina é inútil"*.

## Estrutura atual

```
CTL-TINTA-FL/
├── db.py                      ← camada de banco (sobreviveu às 3 fases)
├── controle_suprimentos.db    ← o banco inteiro
├── iniciar.bat                ← launcher
├── app_reflex/
│   ├── app_reflex.py
│   ├── util_unidade.py        ← regra de litros/ml/unidades
│   ├── util_csv.py
│   ├── estados/               ← lógica Python (dashboard, entrada, despacho, estoque, relatorios, cadastros)
│   ├── paginas/               ← as 6 telas
│   └── componentes/           ← estilos, toast, menu_lateral, selects, cartoes, badges
└── LEIA-ME.txt                ← documentação para o usuário final
```

**Banco:** 5 tabelas — `filiais`, `departamentos`, `itens`, `entradas`, `despachos` — com chaves estrangeiras e integridade referencial.

## Regras de negócio que descobrimos junto

Estas não estavam no pedido inicial; foram surgindo:

| Regra | Detalhe |
|---|---|
| **Unidades por tipo** | Tinta → **litros (L)**, aceita fracionado. Toner e Cartucho → **unidades (un)**, só inteiro |
| **Entrada vs Despacho** | Entrada de tinta em **litros**. Despacho de tinta em **mililitros** (÷1000 antes de gravar) |
| **Garrafinhas** | Código **544** = 65 ml · Código **534** = 120 ml. Selecionar debita o equivalente do estoque |
| **Data de entrada** | Automática — sempre a data do dia em que o produto é adicionado |
| **Alerta de estoque baixo** | Tinta: menos de **1 litro**. Toner: menos de **5 unidades** |
| **Saldo geral** | Nunca somar litros com unidades — o dashboard mostra separado |

→ Detalhe completo em [[../Praticas/08-Unidades-de-Medida|Unidades de Medida]].

## Problemas que este projeto gerou

- [[../Problemas-Resolvidos/04-Colunas-em-Branco-por-JOIN-sem-Alias|Colunas em branco por JOIN sem alias]]
- [[../Problemas-Resolvidos/05-Exclusao-Nao-Funciona-em-Cadastros|Botão de excluir "dá refresh e não exclui"]] ← teve 3 causas diferentes
- [[../Problemas-Resolvidos/06-Selects-Reflex-Nao-Enviam-Valor|Selects não enviam o valor escolhido]]
- [[../Problemas-Resolvidos/07-Operadores-Python-em-Var-do-Reflex|Operadores Python quebram em Var do Reflex]]
- [[../Problemas-Resolvidos/08-Toast-Invisivel-com-Classes-Tailwind|Toast invisível — classe Tailwind como valor de CSS]]
- [[../Problemas-Resolvidos/09-Nome-de-Tabela-em-F-String-no-SQL|Nome de tabela em f-string no SQL]]
- [[../Problemas-Resolvidos/10-Selects-Cinza-com-Texto-Invisivel|Selects cinza com texto invisível]]
- [[../Problemas-Resolvidos/11-Saldo-Geral-Misturando-Unidades|Saldo geral somando litros com unidades]]
- [[../Problemas-Resolvidos/12-Conexao-Recusada-no-Localhost|ERR_CONNECTION_REFUSED no localhost:3000]]
- [[../Problemas-Resolvidos/13-Acesso-Externo-ao-Localhost|Como outra pessoa acessa meu localhost]]
- [[../Problemas-Resolvidos/14-Workflows-Massivos-Falham-em-Arquivos-Grandes|Workflows massivos falhando em arquivos grandes]]

## Estado e pendências

✅ **Feito:** as 6 telas funcionando, unidades corretas, exclusão com confirmação, CSRF (fase Flask), allowlist de tabelas, `.gitignore` endurecido, logging estruturado nos estados do Reflex, documentação (`LEIA-ME.txt`).

⚠️ **Em aberto:**
- `controle_suprimentos.py` (o Tkinter original) e `db.py` **não** receberam a refatoração de exceções/logging — os workflows automáticos travaram nesses dois arquivos por serem os maiores. Precisa ser feito de forma assistida.
- Responsividade da interface foi apontada pelo usuário e mapeada, mas a correção completa não foi concluída.
- Não existem testes automatizados do próprio projeto (só `_teste_fluxos.py` pontual).

## Armadilhas conhecidas

> ⚠️ O banco de exemplo (seed) deixa **100% das filiais, departamentos e itens** com lançamentos vinculados. Como há chave estrangeira, **nada pode ser excluído** até que os lançamentos sejam removidos. Isso já se disfarçou de bug de interface uma vez — ver [[../Problemas-Resolvidos/05-Exclusao-Nao-Funciona-em-Cadastros|o caso completo]].

> ⚠️ Toda alteração visual no Reflex exige **recompilar** (`reflex run`) — editar o arquivo não basta.

## Links relacionados

- GitHub: [[../GitHub/CTL-TINTA/00-Indice|Estado do repositório público (vazio)]]

## Perguntas de revisão

O que é o CTL-TINTA-FL? :: Um sistema local e offline para controlar compra e despacho de tinta e toner para as filiais, com relatórios por filial, departamento e período.

Quais foram as três fases de interface do CTL-TINTA-FL? :: Tkinter, depois Flask com Jinja2 e por fim Reflex.

Quais as regras de unidade do CTL-TINTA-FL? :: Tinta em litros com despacho em mililitros convertido antes de gravar; toner e cartucho em unidades inteiras.

Quais os alertas de estoque baixo do CTL-TINTA-FL? :: Tinta abaixo de 1 litro e toner abaixo de 5 unidades.

Por que nada pode ser excluído no banco de exemplo do CTL-TINTA-FL? :: Porque o seed vincula lançamentos a todos os registros e a chave estrangeira impede a exclusão.
