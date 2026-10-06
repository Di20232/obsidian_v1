---
tags: [ia, gans, difusao, vae, modelos-generativos, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
verificado_em: 2026-10-06
---

# GANs, difusão e outros geradores

GANs são uma de várias **famílias de modelos gerativos**. Entre 2015 e 2020 elas dominaram a geração de imagens. Depois, os **modelos de difusão** assumiram a liderança em qualidade e diversidade, e os **modelos autoregressivos** (os LLMs) dominaram o texto. Mesmo assim, a ideia adversarial continua presente dentro de muitos desses sistemas. Esta nota compara as famílias e mostra onde cada uma é usada.

## As famílias

| Família | Como gera | Gerar é… | Treino | Ponto forte | Ponto fraco |
|---|---|---|---|---|---|
| **GAN** | uma passada do gerador transforma ruído em exemplo | muito rápido | instável, jogo entre duas redes | nitidez e velocidade | colapso de modos; não dá a probabilidade |
| **VAE** | codificador comprime em vetores; decodificador reconstrói | rápido | estável | espaço latente organizado; estima probabilidade | amostras mais borradas |
| **Difusão** | parte de puro ruído e remove ruído aos poucos | lento (dezenas de passos) | estável, só prever o ruído | qualidade e diversidade | custo de geração |
| **Autoregressivo** | um pedaço por vez, prevendo o próximo | lento em sequências longas | estável, prever o próximo token | texto e código; aproveita dados sem rótulo | erro se acumula; um passo por token |
| **Fluxo normalizador** | transformações inversíveis do ruído | rápido | estável | probabilidade exata | restrições na arquitetura limitam a qualidade |

Os marcos de cada família: VAE (Kingma e Welling, 2013), PixelCNN para imagens autoregressivas (van den Oord et al., 2016), RealNVP e Glow para fluxos (2016 e 2018), DDPM para difusão (Ho et al., 2020).

## Por que a difusão passou as GANs em imagens

- **Treino estável:** a tarefa de um modelo de difusão é só prever o ruído adicionado a uma imagem. É uma regressão comum, sem adversário e sem equilíbrio para manter ([[04-Problemas-do-Treino|problemas do treino de GANs]]).
- **Cobertura:** como aprende a reconstruir **todos** os exemplos, não sofre colapso de modos. O artigo *Diffusion Models Beat GANs on Image Synthesis* (Dhariwal e Nichol, 2021) mostrou FID melhor que o BigGAN no ImageNet.
- **Condicionamento por texto** se encaixou bem, e daí vieram os geradores de imagem a partir de descrição.

O preço é a **velocidade**: gerar exige dezenas a centenas de passos, contra uma passada da GAN.

## Onde GANs e a ideia adversarial continuam em uso

1. **Dentro dos próprios modelos de difusão.** O Stable Diffusion trabalha num espaço comprimido por um autoencoder, e esse autoencoder foi treinado com **perda perceptual + perda adversarial** (herança do VQGAN, Esser et al., 2020). Sem o discriminador, as imagens decodificadas sairiam borradas, pelo mesmo motivo de [[01-O-Que-Sao-GANs|uma perda pixel a pixel]].
2. **Difusão em poucos passos.** A **destilação adversarial** (*Adversarial Diffusion Distillation*, Sauer et al., 2023, usada no SDXL Turbo) usa um discriminador para ensinar um modelo de difusão a gerar em **1 a 4 passos**.
3. **Áudio:** vocoders como HiFi-GAN e MelGAN, e sistemas de síntese de voz como o VITS, usam treino adversarial para transformar representações intermediárias em voz natural, em tempo real.
4. **Restauração e super-resolução:** Real-ESRGAN (ampliar imagens) e GFPGAN (restaurar rostos em fotos antigas) são GANs muito usadas em ferramentas de edição.
5. **Edição interativa:** o DragGAN (2023) permite arrastar pontos de uma imagem (abrir uma boca, virar um rosto) usando o espaço latente de um StyleGAN, em tempo real.

## Qual usar

| Objetivo | Escolha atual |
|---|---|
| Gerar texto ou código | modelo de linguagem autoregressivo ([[IA-Aplicada/00-Indice\|IA Aplicada]]) |
| Gerar imagem a partir de descrição, com qualidade | difusão, ou versões destiladas para rapidez |
| Gerar em tempo real, numa área estreita (rostos, um tipo de textura) | GAN |
| Converter espectrograma em áudio | vocoder GAN |
| Entender como treino adversarial funciona | GAN pequena ([[08-GAN-em-PyTorch\|exemplo 2D]]) |

## Perguntas de revisão

Quais as principais famílias de modelos gerativos? :: GANs, autoencoders variacionais (VAEs), modelos de difusão, modelos autoregressivos e fluxos normalizadores.

Como um modelo de difusão gera uma imagem? :: Parte de puro ruído e remove ruído aos poucos, em dezenas de passos, até chegar à imagem.

Por que o treino de um modelo de difusão é mais estável que o de uma GAN? :: Porque a tarefa é só prever o ruído adicionado, uma regressão comum, sem adversário nem equilíbrio para manter.

Qual a principal vantagem das GANs sobre os modelos de difusão? :: Velocidade: a GAN gera em uma única passada, enquanto a difusão precisa de dezenas de passos.

Qual a principal desvantagem dos VAEs em relação às GANs? :: Amostras mais borradas.

Que artigo mostrou modelos de difusão superando GANs em imagens? :: Diffusion Models Beat GANs on Image Synthesis, de Dhariwal e Nichol, 2021.

Onde a perda adversarial aparece dentro do Stable Diffusion? :: No treino do autoencoder que comprime e reconstrói as imagens, que usa perda perceptual mais perda adversarial.

O que é destilação adversarial de difusão? :: Usar um discriminador para ensinar um modelo de difusão a gerar imagens em 1 a 4 passos, como no SDXL Turbo.

Em que área de áudio as GANs continuam muito usadas? :: Em vocoders, como a HiFi-GAN, que transformam espectrogramas em voz em tempo real.

---
Anterior: [[10-Experimento-GAN-com-as-Notas|Experimento com as notas]] · Próxima: [[12-Riscos-Deepfakes-e-Lei|Riscos, deepfakes e lei]] · Trilha: [[GANs/00-Indice|GANs]]
