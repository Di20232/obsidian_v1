---
tags: [ia, gans, pytorch, python, pratica, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
verificado_em: 2026-10-06
---

# GAN em PyTorch: o exemplo 2D

O script `GANs/exemplos/gan_2d.py` é uma GAN completa em cerca de 170 linhas, que treina em **menos de um minuto numa CPU comum**. Ela aprende a desenhar **8 grupos de pontos dispostos num círculo**. É pequena o bastante para ler inteira e visual o bastante para **ver** os problemas das notas anteriores: colapso de modos, a troca entre qualidade e diversidade e o efeito do WGAN-GP.

## Preparar o ambiente (uma vez)

O exemplo precisa só do **PyTorch**. Num ambiente virtual fora do cofre, para não pesar no Obsidian nem no git ([[Python/16-Boas-Praticas-e-Proximos-Passos|ambientes virtuais]]), no Prompt de Comando do Windows:

```bat
python -m venv %USERPROFILE%\.venvs\gan-cofre
%USERPROFILE%\.venvs\gan-cofre\Scripts\activate
pip install torch
```

O `pip install torch` baixa a versão para CPU, com cerca de 124 MB (versão 2.14.1, conferido em 06/10/2026). Não precisa de placa de vídeo.

## Rodar

```bat
%USERPROFILE%\.venvs\gan-cofre\Scripts\activate
cd GANs\exemplos
python gan_2d.py
python gan_2d.py --perda wgan-gp
python gan_2d.py --semente 2
```

A primeira linha de `python` treina a GAN original (cerca de 20 s numa CPU de 6 núcleos), a segunda treina a WGAN-GP (cerca de 1 min) e a terceira repete a GAN original com outra semente, que dá outro resultado. Os desenhos ficam em `GANs/exemplos/saida/`, pasta fora do git porque é recriável.

## O que o script faz

### Os dados

```python
# CENTROS: 8 pontos (x, y) num círculo de raio 2
def amostras_reais(n):
    escolhidos = CENTROS[torch.randint(0, 8, (n,))]   # sorteia um dos 8 grupos
    return escolhidos + 0.05 * torch.randn(n, 2)      # e espalha um pouco em volta
```

Dados de brinquedo têm uma vantagem enorme para aprender: **sabemos a resposta certa**. Dá para medir exatamente quantos grupos o gerador cobre, o que é impossível com fotos.

### As duas redes

Duas redes iguais na forma, com duas camadas ocultas de 128 neurônios:

- **gerador:** 8 números de ruído → ponto (x, y);
- **discriminador:** ponto (x, y) → um número (*logit* na GAN original, nota do crítico na WGAN-GP).

### O laço de treino

Exatamente o de [[03-Como-o-Treino-Funciona|como o treino funciona]]: um passo do discriminador (com `.detach()` nos falsos), depois um passo do gerador. Com `--perda wgan-gp`, o script troca três coisas: perdas do [[05-WGAN-e-Estabilizacao|WGAN]], penalidade de gradiente e 5 passos do crítico por passo do gerador.

### A avaliação

A cada 500 passos, o gerador desenha 2.000 pontos a partir de um **ruído fixo** ([[04-Problemas-do-Treino|hábitos]]), e o script mede:

- **grupos cobertos:** quantos dos 8 grupos receberam pelo menos 2% dos pontos. É a **cobertura** ([[07-Avaliar-GANs|avaliação]]);
- **pontos no alvo:** que fração dos pontos caiu perto de algum grupo. É a **precisão**.

No fim, mostra um mapa de densidade no próprio terminal e salva um SVG com os pontos reais (cinza) e os gerados (magenta).

## O que acontece numa rodada

Saída real da GAN original, semente 0:

```text
passo   500 | perda D   1.061 | perda G   0.986 | grupos cobertos 8/8 | pontos no alvo 34.6%
passo  1000 | perda D   1.069 | perda G   1.423 | grupos cobertos 6/8 | pontos no alvo 71.1%
passo  1500 | perda D   1.189 | perda G   1.249 | grupos cobertos 6/8 | pontos no alvo 81.5%
passo  2000 | perda D   1.226 | perda G   1.123 | grupos cobertos 6/8 | pontos no alvo 87.7%
passo  2500 | perda D   1.233 | perda G   0.958 | grupos cobertos 6/8 | pontos no alvo 90.4%
passo  3000 | perda D   1.253 | perda G   0.951 | grupos cobertos 6/8 | pontos no alvo 91.8%
```

Leia de cima para baixo:

1. No passo 500, o gerador **cobre os 8 grupos**, mas de forma grosseira: só 35% dos pontos acertam algum grupo.
2. No passo 1000, ficou mais preciso (71%) e **largou dois grupos**. Esse é o colapso parcial acontecendo ao vivo: concentrar-se no que engana o discriminador rende mais que cobrir tudo.
3. Daí em diante, a precisão sobe até 92%, mas os dois grupos perdidos **nunca voltam**.
4. A perda do discriminador sobe em direção a 1,386, o valor de quem chuta 1/2 para tudo. Ainda assim, faltam dois grupos: **perda boa não garante cobertura**.

![[gans-2d-gan-semente0.svg|360]]

## Cinco sementes, duas perdas

| Perda | Grupos cobertos (sementes 0 a 4) | Pontos no alvo |
|---|---|---|
| GAN original | 6, 7, 3, 7, 7 | 65% a 92% |
| WGAN-GP | 7, 8, 8, 8, 8 | 66% a 84% |

A semente 2 da GAN original mostra o pior caso: o discriminador venceu (a perda dele caiu para 0,83) e só 3 grupos sobraram, ligados por "trilhas" de pontos que não pertencem a nenhum.

![[gans-2d-gan-semente2-colapso.svg|360]]

As **trilhas** aparecem em todas as rodadas, e têm uma causa matemática: o gerador é uma **função contínua** do ruído, e ruídos vizinhos dão pontos vizinhos. Para levar uma parte do ruído a um grupo e outra parte a outro grupo, ele precisa passar pelo caminho entre os dois. O melhor que pode fazer é **encurtar** esse caminho, mandando para lá poucas entradas. É também por isso que imagens geradas às vezes saem como uma "mistura" de dois tipos.

A WGAN-GP cobre os 8 grupos quase sempre, mas espalha mais pontos entre eles: menos precisão, mais diversidade. A imagem dela está na nota de [[05-WGAN-e-Estabilizacao|WGAN]].

> [!tip] O resultado muda de máquina para máquina
> Com a mesma semente, o script repete o resultado na mesma máquina. Em outro processador ou outra versão do PyTorch, pequenas diferenças de arredondamento crescem ao longo do treino, e os números podem mudar. Por isso a tabela usa 5 sementes, e não uma.

## Experimentos para fazer

- `--ruido 1`: com um único número de ruído, o gerador só consegue desenhar uma **linha** passando pelos grupos. Quantos ele cobre, e quantos pontos ficam na linha entre eles?
- `--passos 10000`: os grupos perdidos voltam com mais treino?
- `--perda wgan-gp --taxa 0.0001`: a taxa do artigo do WGAN-GP. Com 3.000 passos, ela ainda fica longe de convergir (7 grupos, só 25% dos pontos no alvo na semente 0). Quantos passos ela precisa?
- Mude `DESVIO` no código de 0,05 para 0,2. Os grupos ficam mais largos, mas continuam separados, porque os centros vizinhos estão a 1,53 de distância. O colapso diminui?

## Perguntas de revisão

Por que dados de brinquedo em 2D são bons para estudar GANs? :: Porque se conhece a resposta certa e dá para medir exatamente quantos modos o gerador cobre, o que é impossível com fotos.

O que mede "grupos cobertos" no exemplo 2D do cofre? :: A cobertura: quantos dos 8 grupos receberam pelo menos 2% dos pontos gerados.

O que mede "pontos no alvo" no exemplo 2D do cofre? :: A precisão: que fração dos pontos gerados caiu perto de algum grupo real.

O que mostra a GAN 2D cobrir 8 grupos no passo 500 e só 6 no passo 1000? :: Colapso parcial de modos acontecendo durante o treino: ao ganhar precisão, o gerador largou grupos.

A perda do discriminador perto de 1,386 garante que a GAN cobre todos os dados? :: Não; no exemplo 2D, ela chegou perto desse valor e mesmo assim faltavam dois dos oito grupos.

Qual a diferença de comportamento entre a GAN original e a WGAN-GP no exemplo 2D? :: A WGAN-GP cobre os 8 grupos quase sempre, mas com menos pontos no alvo; a GAN original é mais precisa e perde grupos.

Por que o resultado de uma GAN pode mudar entre máquinas com a mesma semente? :: Porque pequenas diferenças de arredondamento entre processadores e versões crescem ao longo do treino.

Que pacote o exemplo de GAN do cofre precisa e onde instalá-lo? :: Só o PyTorch, num ambiente virtual fora do cofre, com pip install torch.

---
Anterior: [[07-Avaliar-GANs|Avaliar GANs]] · Próxima: [[09-GANs-para-Texto|GANs para texto]] · Trilha: [[GANs/00-Indice|GANs]]
