---
tags: [ia, gans, arquiteturas, visao-computacional, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Arquiteturas importantes de GANs

Desde 2014, as GANs ganharam centenas de variações. Algumas viraram marcos, porque resolveram um problema que travava todo mundo: treinar com imagens, escolher o que gerar, traduzir uma imagem em outra, chegar a alta resolução. Conhecer essas poucas ajuda a entender qualquer artigo novo, que quase sempre combina ideias delas.

> [!info] Sobre os anos
> O ano é o da primeira versão pública do artigo (arXiv). Vários foram publicados em conferência no ano seguinte.

## Linha do tempo

| Ano | Arquitetura | Ideia principal | Serve para |
|---|---|---|---|
| 2014 | **GAN** (Goodfellow et al.) | gerador × discriminador | a base de tudo ([[01-O-Que-Sao-GANs\|o que são]]) |
| 2014 | **cGAN** (Mirza e Osindero) | rótulo entra nas duas redes | escolher o que gerar |
| 2015 | **DCGAN** (Radford, Metz e Chintala) | regras para usar convoluções de forma estável | imagens; virou o ponto de partida padrão |
| 2016 | **Pix2Pix** (Isola et al.) | tradução com pares de imagens | esboço → foto, mapa → satélite |
| 2016 | **SRGAN** (Ledig et al.) | perda adversarial + perda perceptual | aumentar a resolução |
| 2017 | **CycleGAN** (Zhu et al.) | tradução **sem** pares, com consistência de ciclo | cavalo ↔ zebra, verão ↔ inverno |
| 2017 | **WGAN / WGAN-GP** | trocar a divergência e limitar o crítico | estabilidade ([[05-WGAN-e-Estabilizacao\|WGAN]]) |
| 2017 | **ProGAN** (Karras et al.) | crescer a resolução aos poucos | rostos em 1024×1024 |
| 2018 | **SAGAN** (Zhang et al.) | autoatenção + normalização espectral | imagens com estrutura global coerente |
| 2018 | **BigGAN** (Brock et al.) | escala: lotes enormes e muitas classes | ImageNet com alta fidelidade |
| 2018 | **StyleGAN** (Karras et al.) | estilo injetado em cada camada | rostos realistas com controle de atributos |
| 2019 | **StyleGAN2** | corrige artefatos do StyleGAN | a referência em rostos por anos |
| 2020 | **HiFi-GAN** (Kong et al.) | GAN para áudio | transformar espectrograma em voz |
| 2021 | **StyleGAN3** | geração sem *aliasing* | animação sem textura "grudada" na tela |
| 2023 | **GigaGAN** (Kang et al.) | GAN de texto para imagem em grande escala | mostrar que GANs ainda competem em velocidade |

## DCGAN: as regras que tornaram imagens possíveis

Antes do DCGAN, usar convoluções em GANs costumava divergir. O artigo propôs um conjunto de regras que virou receita:

- trocar *pooling* por convoluções com passo (no discriminador) e convoluções transpostas (no gerador);
- usar **normalização de lote** (*batch norm*) nas duas redes, menos na saída do gerador e na entrada do discriminador;
- **ReLU** no gerador com **tanh** na saída; **LeakyReLU** no discriminador;
- nada de camadas totalmente conectadas no meio da rede;
- Adam com taxa 0,0002 e β1 = 0,5 ([[03-Como-o-Treino-Funciona|configuração]]).

## Pix2Pix e CycleGAN: transformar uma imagem em outra

O **Pix2Pix** é uma GAN condicional em que a condição é **uma imagem inteira**. Recebe o esboço e gera a foto. Tem três ingredientes:

- gerador em formato **U-Net**, que passa os detalhes da entrada direto para a saída;
- discriminador **PatchGAN**, que julga pedaços pequenos da imagem em vez dela inteira, o que favorece textura nítida;
- perda **L1** (fidelidade à imagem esperada) somada à perda adversarial (realismo).

O limite do Pix2Pix é precisar de **pares**: a mesma cena como esboço e como foto. O **CycleGAN** dispensa os pares com **duas** GANs (A→B e B→A) e uma regra: transformar de A para B e voltar para A deve devolver a imagem original. Essa **consistência de ciclo** impede o gerador de trocar o conteúdo da cena enquanto troca o estilo.

## ProGAN e StyleGAN: alta resolução com controle

O **ProGAN** treina primeiro em 4×4 pixels e vai **acrescentando camadas** (8×8, 16×16… até 1024×1024). Cada etapa só precisa aprender detalhes da sua escala, o que estabiliza o treino.

O **StyleGAN** muda o gerador:

1. uma **rede de mapeamento** transforma o ruído *z* num vetor intermediário *w*, mais organizado;
2. *w* é injetado em **cada camada** como um "estilo";
3. as camadas iniciais controlam atributos grossos (pose, formato do rosto) e as finais, detalhes (textura da pele, cor do cabelo).

Por isso dá para **misturar estilos**: pose de um rosto com textura de outro. Foi o StyleGAN que popularizou os sites de "pessoa que não existe", e é por isso que rostos sintéticos hoje são indistinguíveis a olho nu ([[12-Riscos-Deepfakes-e-Lei|riscos e deepfakes]]).

## BigGAN e o truque do truncamento

O **BigGAN** mostrou que GANs melhoram muito com **escala**: lotes de até 2.048 imagens, redes largas e as 1.000 classes do ImageNet. Também popularizou o **truque do truncamento**: sortear o ruído só perto do centro da distribuição. As amostras ficam **mais caprichadas e menos variadas**. É um botão explícito entre qualidade e diversidade ([[07-Avaliar-GANs|avaliação]]).

## Perguntas de revisão

O que o DCGAN trouxe para as GANs? :: Um conjunto de regras para usar convoluções de forma estável, como normalização de lote, ReLU no gerador, LeakyReLU no discriminador e nada de pooling.

Qual a diferença entre Pix2Pix e CycleGAN? :: O Pix2Pix precisa de pares de imagens correspondentes; o CycleGAN aprende sem pares, usando consistência de ciclo.

O que é consistência de ciclo no CycleGAN? :: A regra de que transformar uma imagem de A para B e de volta para A deve devolver a imagem original.

O que é um discriminador PatchGAN? :: Um discriminador que julga pedaços pequenos da imagem em vez da imagem inteira, favorecendo texturas nítidas.

Por que o Pix2Pix soma a perda L1 à adversarial? :: A L1 mantém a saída fiel à imagem esperada e a adversarial garante que ela pareça real.

Como o ProGAN chega a alta resolução? :: Treina primeiro em resolução baixa e vai acrescentando camadas para resoluções maiores.

O que a rede de mapeamento do StyleGAN faz? :: Transforma o ruído z num vetor intermediário w, que é injetado como estilo em cada camada do gerador.

No StyleGAN, o que controlam as camadas iniciais e as finais? :: As iniciais controlam atributos grossos como pose e formato; as finais, detalhes como textura e cor.

O que é o truque do truncamento do BigGAN? :: Sortear o ruído só perto do centro da distribuição, trocando variedade por qualidade das amostras.

Para que serve a HiFi-GAN? :: Para transformar espectrogramas em áudio de voz, como etapa final da síntese de fala.

---
Anterior: [[05-WGAN-e-Estabilizacao|WGAN e estabilização]] · Próxima: [[07-Avaliar-GANs|Avaliar GANs]] · Trilha: [[GANs/00-Indice|GANs]]
