---
tags: [problema-resolvido, dados, regra-de-negocio, importacao, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Importação renomeava silenciosamente o produto errado

## Contexto

[[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] · importação de produtos por planilha, com opção de identificar o produto **por nome** ou **por código de barras**.

## Sintoma e impacto

Encontrado durante a própria construção da funcionalidade, antes de causar estrago em dados reais — mas o potencial era sério: **um produto existente recebia o nome de outro, sem aviso.**

## Causa-raiz

A lógica de busca tinha um fallback perigoso. Quando a identificação era **por nome** e o nome da planilha **não existia** no cadastro, o código não parava ali: caía no código de barras e encontrava **outro produto** — que então era atualizado com os dados da linha, inclusive o nome.

O efeito é o pior tipo de bug de dados: **destrutivo e silencioso**. Nenhum erro, nenhum aviso, e o registro correto sobrescrito.

## Correção aplicada

**Recusar a linha** em vez de adivinhar.

Se o critério de identificação escolhido pelo usuário não encontra correspondência, a linha é rejeitada com mensagem clara — não se tenta um segundo critério por conta própria.

Junto disso, outras proteções da importação:

| Proteção | O que evita |
|---|---|
| Código de barras de outro produto é **recusado** | Sobrescrever o registro errado |
| Código repetido **dentro do próprio arquivo** é barrado | Duas linhas disputando o mesmo produto |
| Cada linha grava na **própria transação** | Uma linha ruim descartar as boas |
| Toda mudança de estoque entra no **extrato de movimentações** | A importação burlar a auditoria |
| Pré-visualização linha a linha antes de confirmar | Aplicar sem conferir |

## Prevenção

> [!dados] Regra para qualquer importação
> **Na dúvida, recuse a linha — nunca adivinhe.** Um fallback que "tenta outro jeito de encontrar" parece esperto e é, na prática, um caminho para corromper dados sem deixar rastro.
>
> E: toda escrita em massa precisa de pré-visualização antes de confirmar, e de registro de auditoria depois.

## Links relacionados

- Projeto: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]]
- Prática: [[../Praticas/05-Importacao-de-Planilhas|Importação de planilhas]]
- Mapa: [[../Mapas/02-Mapa-Dados|Mapa de Dados]]

## Perguntas de revisão

Por que um fallback na importação é perigoso? :: Porque ao não achar pelo critério escolhido tenta outro e pode sobrescrever o produto errado sem aviso.

Qual a regra para qualquer importação de dados? :: Na dúvida, recusar a linha, nunca adivinhar.

Quais proteções uma importação em massa precisa? :: Pré-visualização antes de confirmar, transação por linha, recusa de códigos de outro produto e registro de auditoria.
