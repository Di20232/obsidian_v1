---
tags: [problema-resolvido, reflex, python, interface, banco-de-dados, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# O botão de excluir dá refresh e não exclui nada

> [!problema] O caso mais instrutivo deste cofre
> O mesmo sintoma teve **três causas diferentes** em três momentos. Cada correção parecia definitiva — e o sintoma voltava.

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · aba **Cadastros** · Reflex (Python que compila para React) · SQLite com chaves estrangeiras.

## Sintoma e impacto

Clicar na lixeira de uma filial, departamento ou item fazia a tela **piscar como se recarregasse**, e o registro continuava lá. Nenhuma mensagem de erro visível. Impacto: impossível limpar cadastros de teste.

## Causa 1 — link fazendo o papel de botão

Os três controles de exclusão eram `rx.link` **sem href válido**. O Reflex compilava isso como `RadixThemesLink` com `href="#"`. O clique disparava duas coisas ao mesmo tempo: o evento `on_click` do Reflex e a **navegação do navegador**. A navegação vencia e **interrompia o evento WebSocket** antes de ele chegar ao servidor — daí o refresh que não faz nada.

**Correção:** trocar por botão de verdade.

```python
rx.button(type="button", variant="ghost", on_click=Estado.excluir(...))
```

Verificado no *bundle compilado*: os três controles passaram a ser `RadixThemesButton` com `type:"button"`, e o app inteiro ficou com **zero** ocorrências de `href="#"`. O mesmo defeito existia no botão X do toast e foi corrigido junto.

## Causa 2 — o banco inteiro travado por chave estrangeira

O sintoma voltou. Desta vez a investigação foi no banco, e o resultado foi categórico:

| Entidade | Total | Com lançamentos vinculados |
|---|---|---|
| Filiais | 14 | **14 (100%)** |
| Departamentos | 6 | **6 (100%)** |
| Itens | 10 | **10 (100%)** |

Cada filial tinha de 1 a 5 despachos, cada departamento de 3 a 9, cada item de 2 a 7 movimentos. Ou seja: o **seed de exemplo** vinculou lançamentos a *todos* os registros. Com integridade referencial ativa, `db.excluir()` retornava `False` (IntegrityError) para **qualquer linha**.

O evento funcionava perfeitamente. O banco é que se recusava — corretamente.

## Causa 3 — o aviso existia, mas era invisível

E por que o usuário não via o erro? O handler *mostrava* um toast dizendo que o registro estava em uso — mas o toast injetava classes do Tailwind como **valor de CSS** (`background: "bg-red-50"`), que é inválido e simplesmente não renderiza.

→ detalhado em [[08-Toast-Invisivel-com-Classes-Tailwind|Toast invisível]].

Resultado combinado: **clica, nada some, e nem percebe o aviso.**

## Correção aplicada

1. Botões reais em vez de links (causa 1).
2. Cores do toast e dos badges em **hex de verdade**, não classes Tailwind (causa 3).
3. **Confirmação de exclusão** mostrando o nome do registro e avisando quando ele está em uso.
4. Oferecer **exclusão em cascata** como escolha explícita do usuário — apagar o registro junto com seus lançamentos — ou bloquear com mensagem clara.

## Prevenção

> [!problema] As três lições
> 1. **Controle que age não é link.** Link navega; botão age. Um link com `on_click` é uma corrida que o evento perde.
> 2. **Falha silenciosa é pior que erro na cara.** Se a operação pode ser recusada pelo banco, a recusa precisa chegar ao usuário de forma visível.
> 3. **Dado de exemplo molda o que você consegue testar.** Um seed que vincula tudo esconde o caminho feliz da exclusão.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Tecnologia: [[../Tecnologias/01-Reflex|Reflex]]
- Relacionados: [[08-Toast-Invisivel-com-Classes-Tailwind|Toast invisível]] · [[04-Colunas-em-Branco-por-JOIN-sem-Alias|Colunas em branco]]
- Prática: [[../Praticas/06-Caca-de-Bugs|Caça de bugs]]

## Perguntas de revisão

Por que um link com on_click pode não executar a ação? :: Porque a navegação do link acontece junto e interrompe o evento antes de ele chegar ao servidor.

Qual a lição sobre controles que agem? :: Controle que age é botão, não link: link navega, botão age.

Por que nenhum cadastro podia ser excluído no CTL-TINTA-FL? :: Porque o seed de exemplo vinculou lançamentos a 100% dos registros, e a chave estrangeira recusava toda exclusão.

Qual a lição sobre falhas silenciosas? :: Falha silenciosa é pior que erro visível; se o banco pode recusar a operação, a recusa precisa chegar ao usuário.

Como dados de exemplo podem atrapalhar os testes? :: Um seed que vincula tudo esconde o caminho feliz, como uma exclusão bem-sucedida.

Por que o mesmo sintoma pode ter várias causas? :: Porque cada correção resolve uma camada; o sintoma de excluir e nada acontecer teve três causas diferentes.
