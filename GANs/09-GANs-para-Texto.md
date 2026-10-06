---
tags: [ia, gans, texto, nlp, modelos-de-linguagem, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# GANs para texto

GANs funcionam muito bem para **imagens e áudio**, mas quase nunca para **texto**. O motivo é um detalhe matemático com consequências enormes: texto é feito de **escolhas discretas** (esta palavra *ou* aquela), e o gradiente, que é o que ensina o gerador, não atravessa uma escolha. Esta nota explica o problema, as tentativas de contorná-lo e por que os modelos de linguagem atuais seguiram outro caminho.

## Por que imagem funciona e texto não

Numa imagem, o gerador produz **números contínuos** (a intensidade de cada pixel). Se o discriminador diz "esta imagem pareceria mais real com este pixel um pouco mais claro", o gerador consegue mudar o pixel **um pouco**, e o gradiente diz exatamente quanto.

No texto, o gerador precisa **escolher um caractere ou palavra** em cada posição. Escolher (sortear ou pegar o mais provável) é um **salto**: não existe "um pouco mais perto da palavra *casa*". A derivada de uma escolha é zero em quase todo lugar, e o sinal do discriminador **morre ali**.

```text
imagem:  ruído → gerador → 0,73  0,12  0,98 …  → discriminador     (o gradiente volta por tudo)
texto:   ruído → gerador → probabilidades → ESCOLHA → "casa" → discriminador
                                              ↑ o gradiente para aqui
```

## As tentativas

### 1. Não escolher: comparar distribuições

Em vez de escolher, o gerador entrega **a distribuição inteira** em cada posição (por exemplo, 70% "a", 20% "o", 10% "e"). O discriminador compara isso com o texto real codificado em **one-hot** (100% na letra certa). Tudo fica contínuo e o gradiente passa.

O problema: com a perda original, o discriminador vence de forma **trivial**. Basta perceber que o texto real é sempre 100% numa letra e o falso nunca é. O artigo do **WGAN-GP** (Gulrajani et al., 2017) mostrou que, com a penalidade de gradiente, essa abordagem **funciona razoavelmente** para trechos curtos de caracteres. A penalidade obriga o crítico a ser "suave" e o impede de explorar esse atalho com tanta força. O modelo aprendeu a soletrar palavras curtas e frequentes, mas as frases não faziam sentido. **É a abordagem do [[10-Experimento-GAN-com-as-Notas|experimento com as notas do cofre]].**

### 2. Escolher de forma "amaciada": Gumbel-softmax

O truque de **Gumbel-softmax** (Jang et al. e Maddison et al., 2016) imita um sorteio com uma função contínua controlada por uma **temperatura**. Com temperatura alta, a saída é uma mistura suave. Com temperatura perto de zero, ela se aproxima de uma escolha de verdade. Treina-se baixando a temperatura aos poucos. Funciona, mas é delicado de ajustar.

### 3. Tratar como jogo de recompensa: aprendizado por reforço

O **SeqGAN** (Yu et al., 2016) trata o gerador como um **jogador** que escolhe uma palavra por vez, e a nota do discriminador ao fim da frase vira uma **recompensa**. O gerador aprende com o algoritmo REINFORCE, sem precisar de gradiente através da escolha. Para dar recompensa a frases ainda incompletas, completa a frase várias vezes por sorteio e tira a média.

Funciona, mas o sinal é **muito ruidoso**. Na prática, exige treinar o gerador antes pelo método tradicional (prever a próxima palavra), e a parte adversarial só ajusta no fim. Vieram dezenas de variações (LeakGAN, MaliGAN, RankGAN…).

### 4. Fazer a GAN num espaço contínuo

Outra saída é treinar primeiro um **autoencoder**, que transforma frases em vetores contínuos e vetores de volta em frases, e usar a GAN para gerar **vetores**, não palavras. A ARAE (Zhao et al., 2017) segue essa linha.

## O veredito

O artigo *Language GANs Falling Short* (Caccia et al., 2018) comparou essas GANs com o modelo tradicional, treinado só para **prever o próximo token**, ajustando a **temperatura** na hora de gerar. O tradicional ganhou em todo o equilíbrio entre qualidade e diversidade.

Logo depois, os **Transformers** treinados para prever o próximo token em quantidades enormes de texto (a família GPT e seus sucessores) dominaram de vez. É assim que funcionam os modelos de linguagem atuais ([[IA-Aplicada/01-Como-Funcionam-os-Modelos-de-Linguagem|como funcionam os modelos de linguagem]]). Prever o próximo token tem treino estável, aproveita qualquer texto sem rótulo e não tem colapso de modos no treino.

## Onde a ideia adversarial sobrou no texto

- **ELECTRA** (Clark et al., 2020): um gerador pequeno troca algumas palavras de uma frase, e um discriminador aprende a apontar quais foram trocadas. O discriminador vira um ótimo modelo para entender texto. Mas o gerador é treinado do jeito tradicional, **não** de forma adversarial: os autores relatam que a versão adversarial funcionou pior.
- **Detectores de texto gerado por IA** são discriminadores, mas treinados separadamente, sem jogo com o gerador. São pouco confiáveis contra modelos novos.

## Perguntas de revisão

Por que GANs funcionam bem com imagens e mal com texto? :: Porque pixels são contínuos e o gradiente passa por eles, enquanto texto exige escolher tokens discretos, e o gradiente não atravessa uma escolha.

Qual é a derivada de escolher um token e qual a consequência para a GAN? :: É zero em quase todo lugar, então o sinal do discriminador não chega ao gerador.

Como o WGAN-GP treinou uma GAN de texto sem escolher caracteres? :: O gerador entrega uma distribuição de probabilidade por posição, e o crítico a compara com o texto real em one-hot.

Por que comparar distribuições com one-hot falha na GAN original? :: Porque o discriminador vence trivialmente ao perceber que o texto real é sempre 100% numa letra e o falso nunca é.

O que é o truque de Gumbel-softmax? :: Uma aproximação contínua de um sorteio controlada por uma temperatura; perto de zero, ela se aproxima de uma escolha discreta.

Como o SeqGAN contorna o problema do gradiente no texto? :: Trata o gerador como um agente de aprendizado por reforço e usa a nota do discriminador como recompensa no algoritmo REINFORCE.

Qual foi a conclusão do artigo Language GANs Falling Short? :: Que modelos tradicionais de prever o próximo token, com a temperatura ajustada, superam as GANs de texto no equilíbrio entre qualidade e diversidade.

O ELECTRA é uma GAN? :: Não exatamente: tem gerador e discriminador, mas o gerador é treinado pelo método tradicional, não de forma adversarial.

Como os modelos de linguagem atuais geram texto? :: Prevendo o próximo token, com Transformers treinados em grandes quantidades de texto, e não com GANs.

---
Anterior: [[08-GAN-em-PyTorch|GAN em PyTorch]] · Próxima: [[10-Experimento-GAN-com-as-Notas|Experimento com as notas]] · Trilha: [[GANs/00-Indice|GANs]]
