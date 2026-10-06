---
tags: [ia, gans, texto, experimento, pytorch, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
verificado_em: 2026-10-06
---

# Experimento: uma GAN treinada nas notas do cofre

O script `GANs/exemplos/gan_das_notas.py` treina uma GAN de texto com a prosa deste cofre: lê as notas, limpa o Markdown e ensina o gerador a imitar **trechos de 32 caracteres**. O objetivo não é produzir notas úteis, porque para isso RAG e fine-tuning são muito melhores ([[IA-Aplicada/04-RAG-Busca-Mais-Geracao|RAG]], [[IA-Aplicada/05-Fine-Tuning|fine-tuning]]). O objetivo é **ver na prática** o que uma GAN consegue aprender de texto, e onde ela trava ([[09-GANs-para-Texto|GANs para texto]]).

> [!summary] Resultado em uma frase
> Em 28 minutos de CPU, a GAN aprendeu a **forma** do português escrito nas notas (tamanho das palavras, espaços, sílabas, palavras curtas como "que", "com", "uma") e passou por um colapso de modos no começo, mas quase não aprendeu **vocabulário**: só 6% das palavras de 3 letras ou mais que ela escreve existem. Nada foi copiado das notas.

## Os dados: o que entra e o que fica de fora

O script segue a mesma política da exportação para IA ([[Cerebro/Guias/08-Cofre-para-IA-e-Lembretes|cofre para IA]]):

- **entra:** as notas `.md` de todas as trilhas e do `Cerebro/`;
- **fica de fora:** `Diario/` e `Inbox/` (pessoais), `Templates/`, cópias de código de terceiros (`*/Fontes/*`), pastas ocultas como `.obsidian/` e `.imports/`, e os próprios exemplos.

A limpeza tira tudo que não é prosa: frontmatter, blocos de código, links (fica só o texto visível), tabelas, callouts e URLs. Depois passa tudo para minúsculas e mantém um vocabulário fixo de 63 caracteres (letras com acento, dígitos, espaço e pontuação básica). Os trechos de treino começam sempre no início de uma palavra.

Em 06/10/2026, depois de criada esta trilha, o corpus tinha **301 notas** e cerca de **940 mil caracteres** de texto limpo. O treino leu as notas quando a trilha ainda estava sendo escrita, com um pouco menos que isso. O corpus muda a cada nota editada: rode `python gan_das_notas.py --dados` para ver o atual. O `--treinar` também mostra o tamanho na primeira linha.

## O modelo

A arquitetura é a do modelo de linguagem do artigo do **WGAN-GP** (Gulrajani et al., 2017), conferida no código original dos autores:

- **gerador:** 128 números de ruído → camada linear → blocos residuais de convolução 1D → para cada uma das 32 posições, uma **distribuição de probabilidade** sobre os 63 caracteres (softmax);
- **crítico:** recebe 32 posições × 63 caracteres (texto real em **one-hot**, ou as distribuições do gerador) → blocos residuais → uma nota;
- **treino:** perda do [[05-WGAN-e-Estabilizacao|WGAN-GP]] com λ = 10, Adam com taxa 0,0001 e betas (0,5; 0,9), lotes de 64.

O gerador **nunca escolhe** um caractere durante o treino: entrega distribuições, e o crítico as compara com o one-hot real. Só na hora de mostrar o texto o script pega o caractere mais provável de cada posição.

| | Artigo original | Padrão do cofre |
|---|---|---|
| Canais (dim) | 512 | 64 |
| Blocos residuais por rede | 5 | 3 |
| Passos do crítico por passo do gerador | 10 | 5 |
| Iterações | 200.000 | 6.000 |
| Hardware | GPU | CPU de 6 núcleos, cerca de 0,3 s por iteração |

O custo das convoluções cresce com o **quadrado** do número de canais. Cada iteração do cofre custa cerca de **1/200** de uma iteração original, e são 33 vezes menos iterações. No total, o experimento usa umas **7 mil vezes menos computação** que o artigo. É o que cabe em meia hora de CPU.

## Como medir o que ela aprendeu

A cada 250 iterações, o gerador escreve 200 trechos a partir de um **ruído fixo**, e o script mede ([[07-Avaliar-GANs|avaliar GANs]]):

| Métrica | O que mede | Texto real | Letras ao acaso | Colapso ("o o o…") |
|---|---|---|---|---|
| **Palavras que existem** | fração das palavras de 3+ letras que aparecem nas notas | 100% | 0,8% | 0% |
| **Variedade** (distinct-4) | fração de sequências de 4 caracteres diferentes | 59% | 94% | 0% |
| **Copiados** | fração dos trechos que aparecem idênticos nas notas | — | — | — |

A variedade **depende do número de trechos**: com 2.000 em vez de 200, o texto real cai para 23%. Só compare valores medidos com a mesma quantidade. O script também imprime a **distância W** estimada pelo crítico, que deve cair à medida que o texto falso se aproxima do real.

## O que aconteceu no treino

Rodada de 06/10/2026, com as configurações padrão e semente 0 (28 minutos):

| Iteração | Distância W | Palavras que existem | Variedade | Exemplo de trecho gerado |
|---|---|---|---|---|
| 250 | 5,16 | 1,8% | 3,3% | `esessssseesssssessssessssesss  o` |
| 1.000 | 2,48 | 0,5% | 14,5% | `esda roscrsda ros eudosdoudoudo ` |
| 2.000 | 2,33 | 7,8% | 33,6% | `os emc cor de cnemo de  erfaide ` |
| 3.000 | 2,24 | 5,2% | 49,4% | `var vaa territendo dento prse e ` |
| 4.000 | 2,08 | 6,4% | 59,5% | `qur sua mecinmonto mostomtpio e ` |
| 5.000 | 2,16 | 7,4% | 64,8% | `qis qua mariifente tertom aio o ` |
| 6.000 | 2,48 | 7,0% | 61,8% | `a to esraa do que ancon er irdo ` |

Nenhum trecho, em nenhuma etapa, foi copiado das notas.

### 1. Começou em colapso de modos

Na iteração 250, o gerador só escrevia "s", "e" e espaços: a variedade estava em 3%, contra 59% do texto real. É o [[04-Problemas-do-Treino|colapso de modos]] visto em texto. Achou poucas saídas que enganavam o crítico e repetiu só elas. O WGAN-GP o tirou de lá: a variedade foi subindo, com pequenas quedas, até se igualar à do texto real perto da iteração 4.000. Depois passou um pouco dela, oscilando entre 62% e 69%, sinal de letras um pouco mais soltas que no texto de verdade.

### 2. Aprendeu a forma antes do conteúdo

Numa avaliação maior, com 2.000 trechos do modelo final:

| | Gerado | Real |
|---|---|---|
| Tamanho médio das palavras | 4,7 letras | 4,6 letras |
| Fração de espaços | 15% | 16% |
| Palavras mais frequentes, na ordem | o, a, e, no, de, co, do, u | de, o, e, a, que, em, é, do |
| Palavras de 3+ letras que existem | 6,2% | 100% |

A GAN acertou a **estatística** do texto: palavras do tamanho certo, separadas na frequência certa, com sílabas que alternam consoante e vogal e terminações como "-ado", "-ante", "-ar". Entre as palavras mais frequentes, as curtas e comuns aparecem quase na mesma ordem do texto real, misturadas com pedaços que não são palavras ("co", "u"). As palavras de 3+ letras que ela mais acerta são "que", "cor", "com", "das", "dos", "sua" e "uma"; a mais longa foi "cortando". O **vocabulário** quase não veio: 6% de palavras existentes é 8 vezes mais que letras ao acaso, mas muito longe do texto real.

### 3. O mesmo ruído guarda a mesma "forma de frase"

Compare o mesmo vetor de ruído nas iterações 5.000 e 6.000:

```text
5.000:  por lrarostdnemerla cor recar di
6.000:  sor liicar dlamerta sol resar da
```

Os espaços ficam quase nas mesmas posições, e só as letras mudam. Cada ponto do [[02-Gerador-e-Discriminador|espaço latente]] virou um "esqueleto" de frase, e o treino refina o que vai dentro dele.

### 4. A distância W parou de cair antes da qualidade parar de subir

A estimativa caiu de 5,2 para cerca de 2,3 até a iteração 2.000 e depois ficou oscilando entre 1,9 e 2,5. A variedade, porém, continuou subindo até a iteração 4.500. O número impresso vem de **um único lote de 64 trechos**, então tem muito ruído. É útil para ver a tendência, mas não substitui as métricas.

## Por que ela não aprendeu mais

- **Computação:** 7 mil vezes menos que o artigo, cujo modelo também só chegou a soletrar palavras frequentes.
- **Dados:** menos de 1 milhão de caracteres. Modelos de linguagem usam bilhões.
- **O problema de fundo:** o crítico compara distribuições com one-hot, e o gerador aprende a deixar o caractere certo "mais provável", não a escolher palavras ([[09-GANs-para-Texto|GANs para texto]]).
- **Janela curta:** 32 caracteres cabem em 5 ou 6 palavras. Não há espaço para frases com sentido.

## E se o objetivo fosse gerar texto útil a partir das notas?

| Objetivo | Caminho certo |
|---|---|
| Responder perguntas com base nas notas, citando a fonte | [[IA-Aplicada/04-RAG-Busca-Mais-Geracao\|RAG]] |
| Escrever no estilo das notas | [[IA-Aplicada/05-Fine-Tuning\|fine-tuning]] de um modelo de linguagem pronto |
| Treinar um modelo pequeno do zero, para estudar | modelo de linguagem de caracteres que prevê o próximo caractere (o tradicional, que ganhou das GANs) |
| Entender treino adversarial | este experimento |

## Rodar

Com o ambiente da nota [[08-GAN-em-PyTorch|GAN em PyTorch]] ativado:

```bat
cd GANs\exemplos
python gan_das_notas.py --dados
python gan_das_notas.py --treinar
python gan_das_notas.py --gerar 20
```

A primeira linha mostra o corpus e as referências. A segunda treina por 6.000 iterações (cerca de meia hora) e salva o modelo em `saida/`. A terceira gera 20 trechos com o modelo salvo. Rodar `--treinar` de novo **continua** de onde parou; `--do-zero` recomeça. O histórico das métricas fica em `saida/historico.csv`.

### Experimentos para fazer

- `--treinar --iteracoes 20000`: continua o treino. A fração de palavras que existem passa de 10%?
- `--do-zero --dim 128 --blocos 5`: rede maior, cerca de 4 vezes mais lenta por iteração (1,15 s contra 0,30 s, medido em 06/10/2026). Aprende mais palavras no mesmo número de iterações? Atenção: `--do-zero` substitui o modelo salvo.
- `--do-zero --passos-critico 1`: o crítico treina tanto quanto o gerador. O colapso do começo dura mais?
- Compare com um modelo que prevê o próximo caractere, treinado no mesmo corpus pelo mesmo tempo.

## Perguntas de revisão

Qual a ideia do experimento de GAN com as notas do cofre? :: Treinar uma GAN de texto nos trechos de 32 caracteres das notas para ver o que ela aprende de texto e onde trava.

Que pastas ficam fora do corpus da GAN de texto do cofre? :: Diario e Inbox, por serem pessoais, Templates, cópias de código de terceiros e pastas ocultas como .obsidian e .imports.

Como o gerador da GAN de texto do cofre evita escolher caracteres no treino? :: Entrega uma distribuição de probabilidade por posição, que o crítico compara com o texto real em one-hot.

Como o colapso de modos apareceu na GAN de texto do cofre? :: Na iteração 250, o gerador só escrevia "s", "e" e espaços, com variedade de 3% contra 59% do texto real.

O que a GAN de texto do cofre aprendeu bem? :: A forma do texto: tamanho das palavras, frequência de espaços, sílabas e palavras curtas e frequentes como "que" e "com".

O que a GAN de texto do cofre não aprendeu? :: Vocabulário: só cerca de 6% das palavras de 3 letras ou mais que ela escreve existem nas notas (conferido em 06/10/2026).

A GAN de texto do cofre copiou trechos das notas? :: Não; nenhum trecho gerado apareceu idêntico nas notas em nenhuma etapa do treino.

Por que a métrica distinct-4 só é comparável com a mesma quantidade de amostras? :: Porque, com mais trechos, mais sequências se repetem; o texto real dá 59% com 200 trechos e 23% com 2.000.

Por que a distância W impressa no treino oscila tanto? :: Porque é estimada a partir de um único lote de 64 trechos, o que a torna ruidosa.

Quanta computação o experimento do cofre usa em relação ao artigo do WGAN-GP? :: Cerca de 7 mil vezes menos: cada iteração custa uns 1/200 da original, e são 33 vezes menos iterações.

Qual o caminho certo para responder perguntas com base nas notas do cofre? :: RAG, que busca os trechos relevantes e responde citando a fonte, e não uma GAN.

---
Anterior: [[09-GANs-para-Texto|GANs para texto]] · Próxima: [[11-GANs-Difusao-e-Outros-Geradores|GANs, difusão e outros geradores]] · Trilha: [[GANs/00-Indice|GANs]]
