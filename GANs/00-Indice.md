---
tags: [ia, gans, aprendizado-profundo, indice, moc]
aliases: [GANs, Redes Adversariais Generativas, Generative Adversarial Networks]
cssclasses: [cerebro-nota, cerebro-ia]
verificado_em: 2026-10-06
---

# 🎭 GANs: redes adversariais generativas

Uma GAN coloca duas redes neurais para competir: um **gerador** que inventa exemplos e um **discriminador** que tenta desmascará-los. Dessa disputa saíram os rostos de pessoas que não existem, a tradução de esboços em fotos e uma ideia que vive até hoje dentro dos geradores de imagem e de voz. Esta trilha vai da intuição ao código: como o treino funciona, por que ele quebra, como estabilizar, como medir e onde as GANs ainda são a melhor escolha.

> [!example] Dois experimentos que rodam numa CPU comum
> A pasta `GANs/exemplos/` tem dois scripts em PyTorch, testados neste cofre em 06/10/2026:
> - `gan_2d.py`: uma GAN que aprende a desenhar 8 grupos de pontos em menos de um minuto. Serve para **ver** o colapso de modos e o efeito do WGAN-GP ([[08-GAN-em-PyTorch|GAN em PyTorch]]).
> - `gan_das_notas.py`: uma GAN de texto treinada nas **próprias notas do cofre** ([[10-Experimento-GAN-com-as-Notas|experimento com as notas]]).

## Trilha

### Fundamentos
1. [[01-O-Que-Sao-GANs|O que são GANs]]: gerador × discriminador, o falsificador e a polícia, uma perda que aprende
2. [[02-Gerador-e-Discriminador|Gerador e discriminador]]: o caminho dos dados, espaço latente, GAN condicional
3. [[03-Como-o-Treino-Funciona|Como o treino funciona]]: o jogo minimax, o laço alternado, a perda não saturante

### Fazer funcionar
4. [[04-Problemas-do-Treino|Problemas do treino]]: colapso de modos, oscilação, gradiente que some; sintomas e remédios
5. [[05-WGAN-e-Estabilizacao|WGAN e estabilização]]: distância de Wasserstein, penalidade de gradiente, normalização espectral
6. [[06-Arquiteturas-Importantes|Arquiteturas importantes]]: DCGAN, Pix2Pix, CycleGAN, StyleGAN, BigGAN
7. [[07-Avaliar-GANs|Avaliar GANs]]: qualidade × diversidade, FID, precisão e cobertura, memorização

### Na prática
8. [[08-GAN-em-PyTorch|GAN em PyTorch]]: o exemplo 2D, passo a passo, com resultados de 5 sementes
9. [[09-GANs-para-Texto|GANs para texto]]: por que texto é difícil e o que já foi tentado
10. [[10-Experimento-GAN-com-as-Notas|Experimento com as notas]]: uma GAN treinada neste cofre, e o que ela aprendeu

### Contexto
11. [[11-GANs-Difusao-e-Outros-Geradores|GANs, difusão e outros geradores]]: onde cada família ganha, e onde as GANs sobrevivem
12. [[12-Riscos-Deepfakes-e-Lei|Riscos, deepfakes e lei]]: fraude, eleição, LGPD e como se defender

## As três ideias que atravessam a trilha

1. **O discriminador é uma perda que aprende.** Em vez de uma regra escrita à mão, uma rede julga o que "parece real", e isso produz saídas nítidas. → [[01-O-Que-Sao-GANs|o que são GANs]]
2. **Equilíbrio, não mínimo.** O treino é um jogo entre duas redes que mudam juntas. A perda não mede qualidade, o colapso de modos é a falha típica, e a estabilidade vem de limitar o discriminador. → [[04-Problemas-do-Treino|problemas]] · [[05-WGAN-e-Estabilizacao|WGAN]]
3. **Contínuo sim, discreto não.** GANs brilham com imagem e áudio e tropeçam em texto, porque o gradiente não atravessa uma escolha. Para texto, os modelos de linguagem venceram. → [[09-GANs-para-Texto|GANs para texto]]

## Onde isso encontra o resto do cofre

- [[IA-Aplicada/00-Indice|IA Aplicada]]: modelos de linguagem, RAG e fine-tuning, que são o caminho certo para gerar **texto** a partir das notas
- [[IA-Aplicada/06-Preparar-Dados-para-Treinar-IA|Preparar dados para treinar IA]]: as mesmas regras de limpeza e privacidade valem para o corpus da GAN de texto
- [[IA-Aplicada/09-Riscos-Seguranca-e-LGPD-na-IA|Riscos e LGPD na IA]]: o lado jurídico do treino com dados de pessoas
- [[Cerebro/Mapas/05-Mapa-IA|Mapa de IA]]: a visão geral
- [[Python/00-Indice|Python]]: a base para ler os exemplos
