---
tags: [ia, gans, avaliacao, metricas, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Avaliar GANs

Avaliar uma GAN é responder a **duas perguntas separadas**: as amostras são **boas** (parecem dados reais)? E são **variadas** (cobrem tudo que existe nos dados)? Um gerador pode acertar uma e errar a outra. Como a perda do treino não responde a nenhuma das duas ([[03-Como-o-Treino-Funciona|como ler as perdas]]), é preciso medir à parte.

## Qualidade e diversidade são coisas diferentes

| Situação | Qualidade | Diversidade | Exemplo |
|---|---|---|---|
| O ideal | alta | alta | rostos nítidos de todas as idades, etnias e expressões |
| Colapso de modos | alta | baixa | rostos perfeitos, mas todos parecidos ([[04-Problemas-do-Treino\|colapso]]) |
| Gerador "espalhado" | baixa | alta | todo tipo de rosto, mas borrados ou deformados |
| Memorização | alta | aparente | cópias quase exatas das fotos de treino |

A **comparação humana** ainda é usada, mas tem dois pontos cegos: ninguém percebe falta de variedade olhando 16 imagens, e ninguém percebe uma cópia sem conhecer o conjunto de treino.

## Inception Score (IS)

Proposto por Salimans et al. (2016). Passa as imagens geradas por um classificador pronto (Inception, treinado no ImageNet) e mede duas coisas:

- cada imagem deve ser classificada **com confiança** (sinal de qualidade);
- o conjunto inteiro deve espalhar-se **por muitas classes** (sinal de diversidade).

**Quanto maior, melhor.** Os limites são sérios: ele **nunca olha os dados reais**, só faz sentido para imagens parecidas com as classes do ImageNet e não percebe colapso **dentro** de uma classe.

## FID: a métrica padrão

A **Fréchet Inception Distance** (Heusel et al., 2017) compara **reais com geradas**:

1. passa os dois conjuntos pela rede Inception-v3 e guarda, de cada imagem, um vetor de 2.048 características;
2. resume cada conjunto pela **média** e pela **covariância** desses vetores;
3. calcula a distância entre os dois resumos:

$$
\text{FID} = \lVert \mu_r - \mu_g \rVert^2 + \operatorname{Tr}\!\left(\Sigma_r + \Sigma_g - 2(\Sigma_r \Sigma_g)^{1/2}\right)
$$

**Quanto menor, melhor**; 0 significa estatísticas idênticas. O FID piora tanto com amostras ruins (a média se desloca) quanto com falta de variedade (a covariância encolhe).

> [!warning] Só compare FID com FID medido do mesmo jeito
> O valor muda com o **número de amostras** (com poucas, sai mais alto; o comum é usar 50 mil), com a **resolução**, com a **implementação** e até com o **método de redimensionar** as imagens. Um FID de artigo e um FID seu só são comparáveis se tudo isso for igual. Em PyTorch, a `torchmetrics` tem `FrechetInceptionDistance`.

## Precisão e cobertura

O FID mistura qualidade e diversidade num número só. As métricas de **precisão e cobertura** (*precision and recall*, Sajjadi et al., 2018; versão melhorada de Kynkäänniemi et al., 2019) separam as duas:

- **precisão:** que fração das amostras geradas cai **perto de algum dado real**? Mede qualidade.
- **cobertura** (*recall*): que fração dos dados reais tem **alguma amostra gerada por perto**? Mede diversidade.

O exemplo 2D do cofre usa exatamente essas duas ideias, em versão simples: **"pontos no alvo"** é a precisão, e **"grupos cobertos"** é a cobertura ([[08-GAN-em-PyTorch|GAN em PyTorch]]).

## Conferir memorização

Uma GAN com poucos dados pode **decorar** exemplos de treino. Isso engana as métricas, porque a cópia é perfeita e variada, e é um risco real quando os dados são fotos de pessoas ou material licenciado.

O teste mais simples: para cada amostra gerada, achar o **vizinho mais próximo** no conjunto de treino e olhar os pares lado a lado. Distâncias quase zero são cópias. O script de texto do cofre faz a versão mais direta: conta quantos trechos gerados aparecem **idênticos** nas notas ([[10-Experimento-GAN-com-as-Notas|experimento com as notas]]).

## E para texto?

Métricas de imagem não servem para texto. Para frases geradas, usa-se:

- **qualidade:** fração de palavras que existem; **BLEU** contra textos reais; **perplexidade** medida por um modelo de linguagem;
- **diversidade:** **distinct-n**, a fração de sequências de *n* palavras ou caracteres diferentes entre todas as geradas; **self-BLEU**, que mede o quanto as amostras se parecem entre si (menor é mais variado).

O experimento do cofre mede "palavras que existem" (com 3 letras ou mais, para "a", "o" e "e" não contarem por acaso), "variedade" (distinct-4, por caracteres) e "copiados". Cada métrica precisa de uma **referência** para ser lida:

| 200 trechos de 32 caracteres | Palavras que existem | Variedade |
|---|---|---|
| Texto real das notas | 100% | 59% |
| Letras sorteadas pela frequência | 0,8% | 94% |
| Colapso total ("o o o o…") | 0% | 0% |

A variedade **não** é "quanto maior, melhor": texto real fica perto de 59%, e valores bem acima disso indicam letras soltas sem estrutura.

> [!warning] Uma métrica mal escolhida engana
> A primeira versão do script media variedade como "fração de trechos idênticos". Ela marcou 100% num gerador que só escrevia "oooo oo ooooo", porque nenhum trecho era **exatamente** igual a outro. Antes de confiar numa métrica, teste-a contra casos em que você sabe a resposta, como na tabela acima.

## Perguntas de revisão

Quais as duas perguntas que a avaliação de uma GAN precisa responder? :: Se as amostras são boas, isto é, parecidas com dados reais, e se são variadas, cobrindo toda a diversidade dos dados.

Por que olhar uma grade de imagens geradas não basta para avaliar uma GAN? :: Porque o olho humano não percebe falta de variedade em poucas amostras nem cópias de exemplos de treino.

O que o Inception Score mede e qual a sua principal limitação? :: Mede se cada imagem é classificada com confiança e se o conjunto cobre muitas classes; a limitação é nunca comparar com os dados reais.

O que é o FID? :: A distância de Fréchet entre a média e a covariância das características da rede Inception-v3 extraídas de imagens reais e geradas; menor é melhor.

Por que FIDs de experimentos diferentes podem não ser comparáveis? :: Porque o valor muda com o número de amostras, a resolução, a implementação e o método de redimensionar as imagens.

O que medem precisão e cobertura em modelos gerativos? :: Precisão é a fração das amostras geradas perto de dados reais (qualidade); cobertura é a fração dos dados reais com amostras geradas por perto (diversidade).

Como verificar se uma GAN decorou exemplos de treino? :: Buscando, para cada amostra gerada, o vizinho mais próximo no conjunto de treino e conferindo se há cópias quase exatas.

Que métricas avaliam diversidade em texto gerado? :: O distinct-n, fração de sequências de n palavras ou caracteres diferentes entre as geradas, e o self-BLEU, que mede o quanto as amostras se parecem entre si.

Por que contar trechos idênticos não detecta colapso de modos em texto? :: Porque trechos quase iguais, como variações de "oooo oo ooo", contam como diferentes; é preciso medir sequências curtas repetidas, como no distinct-n.

Como testar se uma métrica de avaliação é confiável? :: Aplicando-a a casos com resposta conhecida, como texto real, letras sorteadas e um colapso total, e conferindo se ela os separa.

---
Anterior: [[06-Arquiteturas-Importantes|Arquiteturas importantes]] · Próxima: [[08-GAN-em-PyTorch|GAN em PyTorch]] · Trilha: [[GANs/00-Indice|GANs]]
