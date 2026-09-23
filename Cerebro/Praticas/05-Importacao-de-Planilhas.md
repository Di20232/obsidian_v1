---
tags: [pratica, dados, importacao, flashcards]
cssclasses: [cerebro-nota, cerebro-praticas]
---

# Importação de planilhas que não corrompe dados

Destilado da funcionalidade de importação do [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] e do mapeamento de colunas do [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]].

## O fluxo de quatro passos

O princípio que organiza tudo: **nada é gravado antes da confirmação.**

1. **Escolher** o arquivo — ou colar dados direto do Excel/Google Planilhas
2. **Conferir as colunas** — reconhecidas sozinhas pelo cabeçalho, com um exemplo real embaixo de cada uma
3. **Conferir linha a linha** o que será feito — mostrando `preço antigo → novo` e `estoque antigo → novo`
4. **Confirmar**

O passo 3 é o que transforma uma operação assustadora em uma operação segura: o usuário vê o efeito antes de aceitá-lo.

## O que o parser brasileiro precisa entender

Esta lista é a diferença entre "importa" e "importa de verdade":

| Entrada | Interpretação |
|---|---|
| `R$ 1.234,56` | 1234.56 — ponto é milhar, vírgula é decimal |
| `31/12/2026` | Data no formato brasileiro |
| `45678` numa coluna de data | **Data serial do Excel**, não um número |
| `7891234567890` convertido em notação científica | Código de barras que o Excel estragou |
| `Ma\xE7\xE3` | CSV salvo em Windows-1252, não UTF-8 |

Os dois últimos são os que mais causam dor: o Excel **altera os dados sozinho** ao abrir o arquivo, e o resultado chega ao sistema já corrompido.

## Reconhecimento automático de colunas

Os cabeçalhos variam entre planilhas. Duas abordagens usadas:

- **Mercadinho:** reconhecimento por sinônimos conhecidos (`EAN`, `VLR VENDA`, `QTDE`, `VENCIMENTO`)
- **Projeto W:** tentativa automática e, quando falha, **etapa de mapeamento manual** onde o usuário liga cada campo esperado à coluna real

Vale ter as duas: automático para o caso comum, manual como saída sempre disponível.

## As cinco proteções obrigatórias

| Proteção | O que evita |
|---|---|
| **Na dúvida, recuse a linha** | Adivinhar e sobrescrever o registro errado — [[../Problemas-Resolvidos/20-Importacao-Renomeia-Produto-Errado|caso real]] |
| **Identificador duplicado no próprio arquivo é barrado** | Duas linhas disputando o mesmo registro |
| **Uma transação por linha** | Uma linha ruim descartar as boas |
| **Tudo entra no extrato de movimentações** | A importação burlar a auditoria |
| **Limite no tamanho descomprimido** | [[../Problemas-Resolvidos/22-Decompression-Bomb-em-XLSX|Decompression bomb]] |

> [!dados] A regra que resume todas
> **Importação em massa é escrita destrutiva.** Trate com o mesmo cuidado de um `UPDATE` sem `WHERE`: pré-visualização antes, auditoria depois, e recusa explícita em vez de palpite.

## Links relacionados

- Projetos: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho]] · [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]]
- Mapa: [[../Mapas/02-Mapa-Dados|Mapa de Dados]]

## Perguntas de revisão

Qual o princípio de uma importação segura de planilhas? :: Nada é gravado antes da confirmação.

Quais os quatro passos de uma boa importação? :: Escolher o arquivo, conferir as colunas, conferir linha a linha o que será feito e confirmar.

Como interpretar R$ 1.234,56 numa importação brasileira? :: Como 1234.56: o ponto é separador de milhar e a vírgula é decimal.

O que é um número como 45678 numa coluna de data do Excel? :: Uma data serial do Excel, não um número comum.

Por que o Excel pode estragar códigos de barras? :: Porque converte números longos em notação científica ao abrir o arquivo.

Como tratar uma importação em massa? :: Como escrita destrutiva, igual a um UPDATE sem WHERE: pré-visualização antes, auditoria depois e recusa em vez de palpite.
