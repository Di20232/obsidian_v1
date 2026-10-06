---
tags: [ia, gans, wgan, treino, estabilizacao, flashcards]
aliases: [WGAN, WGAN-GP, Wasserstein GAN]
cssclasses: [cerebro-nota, cerebro-ia]
---

# WGAN e estabilização

A **WGAN** (*Wasserstein GAN*, Arjovsky, Chintala e Bottou, 2017) troca a pergunta do discriminador. Em vez de "real ou falso?", ele dá uma **nota** que estima **quanto trabalho** seria preciso para transformar a distribuição falsa na real. Essa medida, a **distância de Wasserstein**, continua informando a direção certa mesmo quando as duas distribuições não se tocam, que é justamente onde a GAN original fica sem gradiente ([[04-Problemas-do-Treino|problemas do treino]]).

## A distância do "carregador de terra"

Imagine as duas distribuições como **montes de terra**. A distância de Wasserstein-1, também chamada *Earth Mover's Distance*, é o **menor custo** para mover a terra de um monte até ficar com a forma do outro: quantidade de terra × distância percorrida.

Compare com a divergência de Jensen-Shannon, usada pela GAN original:

| Situação | Jensen-Shannon | Wasserstein |
|---|---|---|
| Montes iguais | 0 | 0 |
| Montes separados por 10 metros | log 2 | 10 |
| Montes separados por 1 metro | log 2 (igual!) | 1 |

Para Jensen-Shannon, montes a 10 metros e a 1 metro são **igualmente diferentes**, e o gerador não sabe se está chegando perto. Para Wasserstein, aproximar é sempre melhor, e é isso que gera um gradiente útil.

## O crítico

Calcular essa distância diretamente é inviável, mas existe uma forma equivalente: é o **maior valor possível** de média da nota nos reais − média da nota nos falsos, entre todas as funções de nota "suaves" (**1-Lipschitz**: a nota não pode variar mais rápido que a distância entre os exemplos).

Na prática:

- o discriminador vira **crítico**: sem sigmoide na saída, devolve uma nota livre;
- **perda do crítico** = média(nota dos falsos) − média(nota dos reais), ou seja, ele quer separar ao máximo;
- **perda do gerador** = − média(nota dos falsos), ou seja, ele quer subir a nota que recebe;
- o crítico treina **mais vezes** que o gerador (5 passos para 1 é o padrão), para a nota ser uma boa estimativa da distância.

Um bônus: a estimativa da distância **acompanha a qualidade das amostras**. Pela primeira vez, uma curva do treino de GAN passou a significar alguma coisa. O script de texto do cofre imprime essa estimativa como "distância W".

## Como manter o crítico "suave"

### Corte de pesos (WGAN original)

Depois de cada passo, todos os pesos do crítico são cortados para o intervalo [−0,01; 0,01]. Funciona, mas os próprios autores chamaram de solução ruim: limita o que o crítico consegue aprender e deixa os gradientes explodindo ou sumindo, conforme o valor do corte.

### Penalidade de gradiente (WGAN-GP)

O **WGAN-GP** (Gulrajani et al., 2017) troca o corte por uma **penalidade**. Uma função é 1-Lipschitz quando a inclinação (norma do gradiente) não passa de 1. Então:

1. sorteia pontos **entre** um exemplo real e um falso (interpolação com peso aleatório);
2. calcula a norma do gradiente do crítico nesses pontos;
3. soma à perda do crítico **λ × (norma − 1)²**, com λ = 10.

```python
def penalidade_de_gradiente(critico, reais, falsas):
    alfa = torch.rand(reais.size(0), 1)
    meio = (alfa * reais + (1 - alfa) * falsas).requires_grad_(True)
    gradiente, = torch.autograd.grad(critico(meio).sum(), meio, create_graph=True)
    return ((gradiente.norm(dim=1) - 1) ** 2).mean()
```

O `create_graph=True` permite derivar a própria penalidade no `backward()`, o que se chama derivada de segunda ordem. O artigo sugere Adam com taxa 0,0001, β1 = 0 e β2 = 0,9 (o código de texto dos autores usa β1 = 0,5). Também recomenda **não usar normalização de lote no crítico**, porque a penalidade é calculada exemplo a exemplo; se precisar, use normalização de camada.

> [!example] No exemplo do cofre
> A mesma rede 2D, treinada nos mesmos 3.000 passos ([[08-GAN-em-PyTorch|GAN em PyTorch]]):
>
> | Perda | Grupos cobertos (5 sementes) | Pontos no alvo |
> |---|---|---|
> | GAN original | 6, 7, 3, 7, 7 | 65% a 92% |
> | WGAN-GP | 7, 8, 8, 8, 8 | 66% a 84% |
>
> A WGAN-GP cobriu **todos os grupos em 4 de 5 rodadas**. Em troca, espalhou um pouco mais de pontos pelo caminho entre eles. É a troca entre qualidade e diversidade de que trata a [[07-Avaliar-GANs|avaliação]].

![[gans-2d-wgan-gp-semente1.svg|360]]

## Outras técnicas de estabilização

| Técnica | O que faz | Onde aparece |
|---|---|---|
| **Normalização espectral** (Miyato et al., 2018) | divide os pesos de cada camada do discriminador pelo seu maior valor singular, limitando a inclinação de forma barata | SAGAN, BigGAN; em PyTorch, `torch.nn.utils.parametrizations.spectral_norm` |
| **TTUR** (Heusel et al., 2017) | taxas de aprendizado diferentes, com o discriminador mais rápido (ex.: 0,0004 contra 0,0001) | SAGAN |
| **Perda *hinge*** | o discriminador só é punido quando erra ou acerta "por pouco" | SAGAN, BigGAN |
| **Regularização R1** (Mescheder et al., 2018) | penaliza o gradiente do discriminador só nos dados **reais** | StyleGAN |
| **Suavizar rótulos reais** (Salimans et al., 2016) | usar 0,9 em vez de 1 para os reais, e só para eles | GANs clássicas |
| **Média móvel dos pesos do gerador** (EMA) | usar, para gerar, a média dos pesos ao longo do treino | ProGAN, StyleGAN |
| **Ruído nas entradas do discriminador** | sobrepõe as distribuições, que deixam de ser disjuntas | GANs clássicas |

## Perguntas de revisão

O que a WGAN muda em relação à GAN original? :: Troca a classificação real ou falso por uma nota que estima a distância de Wasserstein entre a distribuição real e a gerada.

O que é a distância de Wasserstein-1? :: O menor custo para transformar uma distribuição na outra, como mover terra: quantidade movida vezes distância percorrida.

Por que a distância de Wasserstein dá gradiente útil quando a de Jensen-Shannon não dá? :: Porque continua diminuindo à medida que as distribuições se aproximam, mesmo sem sobreposição, enquanto Jensen-Shannon fica constante em log 2.

Como se chama o discriminador numa WGAN e o que ele devolve? :: Crítico; devolve uma nota sem limite, sem sigmoide, em que maior significa mais parecido com o real.

Qual a perda do crítico numa WGAN? :: A média das notas dos falsos menos a média das notas dos reais.

Que restrição o crítico da WGAN precisa respeitar? :: Ser 1-Lipschitz, isto é, a nota não pode variar mais rápido que a distância entre os exemplos.

Como a WGAN original mantinha o crítico 1-Lipschitz e qual o problema? :: Cortando os pesos para um intervalo pequeno, o que limita o crítico e faz os gradientes explodirem ou sumirem.

Como funciona a penalidade de gradiente do WGAN-GP? :: Sorteia pontos entre exemplos reais e falsos e soma à perda λ vezes o quadrado da diferença entre a norma do gradiente do crítico e 1, com λ = 10.

Por que não usar normalização de lote no crítico do WGAN-GP? :: Porque a penalidade é calculada exemplo a exemplo, e a normalização de lote mistura os exemplos do lote.

Quantos passos do crítico costumam ser dados para cada passo do gerador numa WGAN? :: Cinco.

O que é normalização espectral? :: Dividir os pesos de cada camada do discriminador pelo seu maior valor singular, o que limita a inclinação da rede de forma barata.

O que é TTUR no treino de GANs? :: Usar taxas de aprendizado diferentes para o discriminador e o gerador, com o discriminador mais rápido.

No exemplo 2D do cofre, quantos grupos a WGAN-GP cobriu? :: Todos os 8 em 4 de 5 sementes, contra no máximo 7 da GAN original (conferido em 06/10/2026).

---
Anterior: [[04-Problemas-do-Treino|Problemas do treino]] · Próxima: [[06-Arquiteturas-Importantes|Arquiteturas importantes]] · Trilha: [[GANs/00-Indice|GANs]]
