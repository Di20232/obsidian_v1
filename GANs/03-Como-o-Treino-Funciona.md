---
tags: [ia, gans, treino, otimizacao, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Como o treino de uma GAN funciona

O treino de uma GAN é um **jogo entre duas redes**: o discriminador ganha pontos quando acerta o que é real e o que é falso, o gerador ganha pontos quando o engana. As duas são treinadas **em turnos alternados**, cada uma com sua perda, até que o discriminador não consiga mais separar as duas coisas.

## O jogo em uma fórmula

O artigo original escreve o jogo assim:

$$
\min_G \max_D \; V(D,G) = \mathbb{E}_{x \sim \text{dados}}[\log D(x)] + \mathbb{E}_{z \sim \text{ruído}}[\log(1 - D(G(z)))]
$$

Em palavras:

- **D(x)** é a probabilidade, segundo o discriminador, de *x* ser real.
- O **discriminador quer aumentar** V: dar nota perto de 1 aos reais (o primeiro termo vai a log 1 = 0) e perto de 0 aos falsos (o segundo também vai a 0).
- O **gerador quer diminuir** V: fazer D(G(z)) chegar perto de 1, o que joga o segundo termo para menos infinito.

É um jogo de **soma zero**: o que um ganha, o outro perde.

## O laço de treino

Cada iteração tem dois passos:

1. **Passo do discriminador:** pegar um lote de dados reais e gerar um lote falso. Calcular a perda dizendo "estes são reais (1)" e "estes são falsos (0)". Atualizar **só o discriminador**: o gerador fica parado.
2. **Passo do gerador:** gerar um lote novo e passar pelo discriminador. Calcular a perda dizendo "quero que estes sejam vistos como reais (1)". Atualizar **só o gerador**: o discriminador fica parado.

```python
# 1) discriminador: o .detach() impede que este passo mexa no gerador
falsas = gerador(torch.randn(lote, 8)).detach()
perda_d = bce(discriminador(reais), um) + bce(discriminador(falsas), zero)
opt_d.zero_grad(); perda_d.backward(); opt_d.step()

# 2) gerador: o gradiente atravessa o discriminador, mas só opt_g dá o passo
falsas = gerador(torch.randn(lote, 8))
perda_g = bce(discriminador(falsas), um)
opt_g.zero_grad(); perda_g.backward(); opt_g.step()
```

O código completo, que roda em um minuto na CPU, está em [[08-GAN-em-PyTorch|GAN em PyTorch]].

## A perda "não saturante"

No começo do treino, os falsos são tão ruins que o discriminador os rejeita com facilidade: D(G(z)) fica perto de 0. Nesse ponto, a curva de log(1 − D(G(z))) é quase **plana**, e o gerador recebe um gradiente minúsculo justamente quando mais precisa aprender. Isso se chama **saturação**.

O próprio artigo de 2014 propõe o conserto: em vez de **minimizar** log(1 − D(G(z))), o gerador **maximiza** log D(G(z)). O objetivo final é o mesmo (enganar o discriminador), mas o gradiente é forte justamente quando os falsos são ruins. No código, isso é só dar ao gerador o rótulo "real" (1) na perda, como no passo 2 acima. **Quase toda implementação usa essa versão.**

## Onde o jogo termina, na teoria

Para um gerador fixo, o melhor discriminador possível responde:

$$
D^*(x) = \frac{p_\text{dados}(x)}{p_\text{dados}(x) + p_\text{gerador}(x)}
$$

Se o gerador reproduz perfeitamente a distribuição dos dados, as duas densidades são iguais e **D\* = 1/2 em todo lugar**: o discriminador só pode chutar. O artigo mostra que, com o discriminador ótimo, minimizar o jogo equivale a minimizar a **divergência de Jensen-Shannon** entre a distribuição dos dados e a do gerador, e o valor do jogo no equilíbrio é −log 4.

Na prática, esse equilíbrio **raramente é atingido de forma estável** ([[04-Problemas-do-Treino|problemas do treino]]).

## Como ler as perdas

Num classificador comum, a perda cai e isso indica progresso. **Numa GAN, não.** As perdas medem quem está ganhando o jogo, não a qualidade das amostras.

| Valor observado | Leitura |
|---|---|
| Perda do discriminador perto de 1,386 (ln 2 + ln 2) | ele está chutando 1/2 para tudo: equilíbrio ou discriminador fraco |
| Perda do discriminador caindo para perto de 0 | ele venceu; o gerador vai parar de receber sinal útil |
| Perda do gerador perto de 0,693 (ln 2) | o discriminador dá cerca de 1/2 aos falsos |
| Perdas oscilando muito, amostras piorando | instabilidade; veja [[05-WGAN-e-Estabilizacao|estabilização]] |

No exemplo 2D do cofre, a perda do discriminador sobe aos poucos, de 1,06 no passo 500 para 1,25 no passo 3.000, chegando perto do ponto de chute. Mesmo assim, o gerador estava ignorando 2 dos 8 grupos de dados ([[08-GAN-em-PyTorch|o exemplo]]). Por isso é preciso **olhar as amostras e medir** ([[07-Avaliar-GANs|avaliar GANs]]).

## Configuração que costuma funcionar

Do artigo do DCGAN (2015), muito copiada até hoje:

- otimizador **Adam** com taxa de aprendizado **0,0002**;
- **β1 = 0,5** em vez do padrão 0,9: com menos "inércia", o otimizador acompanha melhor um alvo que muda a cada passo, porque o adversário também está aprendendo;
- lotes de **128** exemplos;
- ruído *z* sorteado de uma distribuição normal ou uniforme.

## Perguntas de revisão

Como é treinada uma GAN? :: Em turnos alternados: primeiro o discriminador aprende a separar reais de falsos, depois o gerador aprende a enganá-lo, cada um com sua perda.

No passo do discriminador, por que se usa detach na saída do gerador? :: Para que o gradiente daquele passo não altere os pesos do gerador.

O que o discriminador quer no jogo da GAN original? :: Dar nota perto de 1 aos exemplos reais e perto de 0 aos falsos.

O que o gerador quer no jogo da GAN original? :: Que o discriminador dê nota perto de 1 aos exemplos falsos.

O que é a saturação do gerador no começo do treino? :: Com falsos muito ruins, D(G(z)) fica perto de 0 e log(1 − D(G(z))) fica quase plano, então o gradiente do gerador quase some.

O que é a perda não saturante do gerador? :: Maximizar log D(G(z)) em vez de minimizar log(1 − D(G(z))), o que dá gradiente forte quando os falsos ainda são ruins.

Qual a saída do discriminador ótimo quando o gerador reproduz perfeitamente os dados? :: 1/2 para qualquer exemplo, porque ele só pode chutar.

Que divergência a GAN original minimiza quando o discriminador é ótimo? :: A divergência de Jensen-Shannon entre a distribuição dos dados e a do gerador.

Por que a perda de uma GAN não indica a qualidade das amostras? :: Porque ela mede quem está ganhando o jogo entre as duas redes, não o quanto as amostras se parecem com os dados.

Qual o valor da perda do discriminador com entropia cruzada quando ele responde 1/2 para tudo? :: Cerca de 1,386, que é ln 2 do lote real mais ln 2 do lote falso.

Qual configuração de Adam o DCGAN popularizou para GANs? :: Taxa de aprendizado 0,0002 e β1 = 0,5.

---
Anterior: [[02-Gerador-e-Discriminador|Gerador e discriminador]] · Próxima: [[04-Problemas-do-Treino|Problemas do treino]] · Trilha: [[GANs/00-Indice|GANs]]
