---
tags: [guia, cerebro, ia, dados, flashcards]
aliases: [Cofre para IA, Lembretes]
cssclasses: [cerebro-nota, cerebro-geral]
---

# Cofre para IA e lembretes

Este cofre tem dois usos além da consulta:
1. **dado de treino** para uma IA: busca com RAG, avaliação e, quando fizer sentido, fine-tuning;
2. **lembretes** para você: perguntas de revisão sorteadas para fixar o que foi estudado.

Os dois dependem das mesmas convenções. O porquê de cada uma está em [[IA-Aplicada/06-Preparar-Dados-para-Treinar-IA|Preparar dados para treinar IA]].

## Convenções de toda nota nova

- [ ] **Frontmatter** com `tags` e `cssclasses`; e `verificado_em` + `fonte` quando o conteúdo envelhece (preço, taxa, lei, versão).
- [ ] **Definição logo no início:** "X é…".
- [ ] **Uma ideia por seção**, com título `##` descritivo.
- [ ] **Exemplo** concreto, com números conferidos.
- [ ] **Links** para o assunto maior e para notas relacionadas.
- [ ] Seção **`## Perguntas de revisão`** no fim, antes do rodapé.
- [ ] Sem dados pessoais, senhas ou textos copiados de terceiros.

## Formato das perguntas de revisão

Uma por linha, com linha em branco entre elas:

```text
## Perguntas de revisão

O que é margem de contribuição? :: É o que sobra de cada venda depois de pagar todos os custos variáveis.

Qual a fórmula do ponto de pedido? :: Média diária de vendas × (prazo do fornecedor + margem de segurança).
```

Regras:
- a resposta está **correta**, é **completa numa frase** e faz sentido **sem a pergunta**;
- uma pergunta por fato; nada de "explique tudo sobre…";
- dados que mudam levam a data na resposta: "(conferido em 23/09/2026)";
- o separador `::` só é lido dentro da seção "Perguntas de revisão". Fora dela, `std::cout` e afins não viram pergunta.

Esse é o mesmo formato do plugin **Spaced Repetition** do Obsidian (repetição espaçada). As notas com perguntas levam a tag `flashcards`, que o plugin usa. Instalá-lo é opcional: por ser plugin de terceiros, é decisão sua.

## As ferramentas

| Comando | O que faz |
|---|---|
| `ferramentas/lembretes.bat` (duplo clique) ou `node ferramentas/lembretes.js 10` | sorteia 10 perguntas; as respostas aparecem depois do Enter |
| `node ferramentas/lembretes.js 5 Ecommerce` | só perguntas de uma trilha (qualquer trecho do caminho serve: `ia-aplicada`, `shopee`) |
| `node ferramentas/exportar-para-ia.js` | gera `exportacao/notas.jsonl`, `perguntas.jsonl` e `perguntas-chat.jsonl` |
| `node ferramentas/inserir-perguntas.js <pasta> <arquivo.json>` | insere perguntas em lote a partir de um JSON `{ "nota.md": [["pergunta", "resposta"]] }` |

A pasta `exportacao/` fica fora do git: é gerada a partir das notas e pode ser recriada a qualquer momento.

## O que fica fora da exportação

- cópias de código de terceiros (`*/Fontes/*`), por causa da licença;
- `Templates/`, que são esqueletos;
- `Diario/` e `Inbox/`, que são pessoais, a menos que você rode com `--incluir-pessoal`.

## Rotina sugerida

- **Todo dia (5 min):** `lembretes.bat` com 5 perguntas.
- **Ao criar uma nota:** escrever 3 a 6 perguntas de revisão na hora, enquanto o assunto está fresco.
- **Na revisão semanal:** notas novas da semana ganharam perguntas? ([[07-Rotina-do-Cofre|rotina do cofre]])
- **Antes de treinar ou indexar:** rodar o exportador e conferir notas com `verificado_em` antigo.

## Perguntas de revisão

Qual o formato de uma pergunta de revisão no cofre? :: Uma linha com a pergunta, dois-pontos duplos e a resposta, dentro da seção "Perguntas de revisão".

Como sortear lembretes do cofre? :: Clicar duas vezes em ferramentas/lembretes.bat ou rodar node ferramentas/lembretes.js com a quantidade e, opcionalmente, a trilha.

Como gerar os arquivos para treinar ou alimentar uma IA? :: Rodar node ferramentas/exportar-para-ia.js, que cria os arquivos JSONL em exportacao/.

Quando escrever as perguntas de revisão de uma nota? :: Ao criar a nota, enquanto o assunto está fresco.

Por que dados que mudam levam a data na resposta? :: Para o lembrete e o treino não passarem um valor antigo como se fosse atual.

---
Veja também: [[00-Indice|Guias]] · [[IA-Aplicada/00-Indice|IA Aplicada]]
