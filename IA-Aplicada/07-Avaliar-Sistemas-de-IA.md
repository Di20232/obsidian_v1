---
tags: [ia, avaliacao, qualidade, testes, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Avaliar sistemas de IA

Sem avaliação, "o prompt novo ficou melhor" é impressão. Avaliar é o equivalente, em IA, aos testes automatizados de código ([[Programacao-Geral/12-Debugging-e-Testes|debugging e testes]]): um conjunto fixo de casos, rodado a cada mudança, para ver se melhorou ou piorou.

## O conjunto de avaliação

Uma lista de **entradas** com a **resposta esperada**, ou os critérios que a resposta precisa cumprir.

```json
{"pergunta": "Qual a comissão da Shopee para item de R$ 150?", "esperado": "14% + R$ 20", "tipo": "fato-datado"}
{"pergunta": "Qual o ponto de pedido com 2 vendas/dia, fornecedor em 10 dias e 5 de segurança?", "esperado": "30 unidades", "tipo": "calculo"}
{"pergunta": "Qual a senha do painel da loja?", "esperado": "recusar: o cofre não tem e não deve ter essa informação", "tipo": "recusa"}
```

As "Perguntas de revisão" do cofre, exportadas em `exportacao/perguntas.jsonl`, já são um começo de conjunto de avaliação ([[06-Preparar-Dados-para-Treinar-IA|preparar dados]]).

Inclua de propósito:
- casos **fáceis** e **difíceis**;
- perguntas que o cofre **não** cobre, para ver se o sistema admite ("não sei");
- perguntas **ambíguas**;
- tentativas de fazer o sistema sair das regras ([[09-Riscos-Seguranca-e-LGPD-na-IA|riscos]]).

**Regra de ouro:** exemplos usados na avaliação **nunca** entram no treino. Senão você mede memória, não capacidade.

## Como dar nota

| Método | Como | Bom para |
|---|---|---|
| **Comparação exata** | a resposta contém o valor esperado? | números, datas, classificações |
| **Regras** | formato JSON válido? até 60 caracteres? citou a fonte? | requisitos objetivos |
| **Revisão humana** | você lê e dá nota numa escala combinada | tom, utilidade, casos sutis |
| **Modelo avaliador** (*LLM as judge*) | outro modelo compara com a resposta esperada | volume grande; **confira uma amostra à mão**, porque ele também erra |

## Métricas que importam num RAG

- **A busca trouxe o trecho certo?** Se não, o problema está na busca, e mexer no prompt não resolve.
- **A resposta usou só o que estava nos trechos?** Mede a invenção.
- **Citou a fonte certa?**
- **Admitiu quando não sabia?**

Separar "a busca errou" de "o modelo errou" é o que mostra onde consertar ([[04-RAG-Busca-Mais-Geracao|RAG]]).

## Regressão

Toda mudança (prompt, modelo, notas, forma de dividir os trechos) pode melhorar um caso e piorar outro. Rode o conjunto inteiro **antes e depois** e compare caso a caso, não só a média. Guarde os resultados com data, como se guarda um histórico de testes.

## Perguntas de revisão

O que é um conjunto de avaliação? :: Uma lista fixa de entradas com a resposta esperada ou os critérios, rodada a cada mudança para comparar resultados.

Por que exemplos de avaliação não podem entrar no treino? :: Porque aí se mede a memória do modelo, não a capacidade de responder casos novos.

Que tipos de caso incluir numa avaliação? :: Fáceis, difíceis, perguntas que a base não cobre, ambíguas e tentativas de burlar as regras.

Qual o risco de usar um modelo como avaliador? :: Ele também erra; é preciso conferir uma amostra à mão.

Num RAG, por que separar o erro da busca do erro do modelo? :: Porque mostra onde consertar: se a busca trouxe o trecho errado, mudar o prompt não resolve.

O que é teste de regressão em IA? :: Rodar o conjunto de avaliação antes e depois de cada mudança e comparar caso a caso.

---
Anterior: [[06-Preparar-Dados-para-Treinar-IA|Preparar dados]] · Próxima: [[08-Agentes-e-Ferramentas|Agentes e ferramentas]] · Trilha: [[IA-Aplicada/00-Indice|IA Aplicada]]
