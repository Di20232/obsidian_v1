---
tags: [ia, gans, aprendizado-profundo, modelos-generativos, flashcards]
aliases: [GAN, Rede Adversarial Generativa]
cssclasses: [cerebro-nota, cerebro-ia]
---

# O que são GANs

Uma **GAN** (*Generative Adversarial Network*, rede adversarial generativa) é um par de redes neurais treinadas **uma contra a outra**: o **gerador** cria exemplos falsos a partir de números aleatórios, e o **discriminador** tenta separar os falsos dos reais. Cada uma melhora tentando vencer a outra, e no fim o gerador produz dados parecidos com os de treino — rostos, paisagens, vozes — que não existiam antes.

## A analogia do falsificador

O artigo que criou a ideia (Ian Goodfellow e colegas, *Generative Adversarial Nets*, 2014) usa uma comparação simples:

- o **gerador** é um falsificador de dinheiro, que começa fazendo notas grosseiras;
- o **discriminador** é a polícia, que aprende a reconhecer notas falsas;
- cada vez que a polícia descobre um defeito, o falsificador corrige aquele defeito;
- a competição só para quando as notas falsas ficam indistinguíveis das verdadeiras.

O falsificador **nunca vê uma nota verdadeira de perto**. Ele aprende só com o retorno da polícia. É exatamente assim no código: o gerador não recebe os dados reais, só o gradiente que vem do discriminador ([[02-Gerador-e-Discriminador|gerador e discriminador]]).

## Gerativo × discriminativo

| | Modelo discriminativo | Modelo gerativo |
|---|---|---|
| Pergunta que responde | "este e-mail é spam?" | "como é um e-mail típico?" |
| O que aprende | a fronteira entre classes | a distribuição dos próprios dados |
| Saída | um rótulo ou probabilidade | um exemplo novo |
| Exemplos | classificador de imagens, detector de fraude | GANs, modelos de difusão, LLMs |

A GAN junta os dois: um modelo gerativo (o gerador) treinado por um discriminativo (o discriminador).

## A ideia central: uma perda que aprende

Para treinar uma rede que gera imagens, é preciso uma **perda**: um número que diga quão ruim está a saída. A escolha óbvia, comparar pixel a pixel com uma imagem real (erro quadrático), dá imagens **borradas**: quando há várias respostas possíveis, a média delas é o que minimiza o erro, e a média de vários rostos é um borrão.

Na GAN, quem julga é o **discriminador**, uma rede que aprende sozinha o que faz uma imagem "parecer real". Ele pune o borrão, porque borrão não existe nos dados reais, e o gerador é empurrado para saídas **nítidas**. Essa troca de uma regra escrita à mão por um juiz que aprende é a grande contribuição das GANs, e aparece hoje dentro de outros modelos ([[11-GANs-Difusao-e-Outros-Geradores|GANs, difusão e outros geradores]]).

## Para que servem

- **Gerar imagens realistas:** rostos de pessoas que não existem (StyleGAN), produtos, texturas.
- **Transformar imagens:** esboço em foto, dia em noite, cavalo em zebra ([[06-Arquiteturas-Importantes|arquiteturas]]).
- **Aumentar resolução e restaurar** fotos antigas.
- **Áudio:** transformar espectrogramas em voz na síntese de fala.
- **Dados sintéticos** para treinar outros modelos, com cuidado: a GAN pode copiar exemplos de treino ([[07-Avaliar-GANs|avaliação]]).
- **Acelerar modelos de difusão**, usando um discriminador para ensinar o modelo a gerar em poucos passos.

## O que GANs não fazem bem

- **Texto:** palavras são escolhas discretas, e o gradiente não atravessa uma escolha. Os grandes modelos de linguagem usam outra abordagem ([[09-GANs-para-Texto|GANs para texto]]).
- **Dizer quão provável é um exemplo:** a GAN gera, mas não calcula a probabilidade de um dado. Por isso não serve, sozinha, para detectar anomalias por probabilidade.
- **Treino previsível:** o equilíbrio entre as duas redes é frágil ([[04-Problemas-do-Treino|problemas do treino]]).

## Perguntas de revisão

O que é uma GAN? :: Um par de redes neurais treinadas uma contra a outra: o gerador cria exemplos falsos a partir de ruído e o discriminador tenta separá-los dos reais.

Quem criou as GANs e quando? :: Ian Goodfellow e colegas, no artigo Generative Adversarial Nets, de 2014.

O gerador de uma GAN vê os dados reais durante o treino? :: Não; ele aprende só pelo gradiente que recebe do discriminador.

Qual a diferença entre um modelo discriminativo e um gerativo? :: O discriminativo aprende a separar classes e devolve um rótulo; o gerativo aprende a distribuição dos dados e cria exemplos novos.

Por que treinar um gerador de imagens com erro pixel a pixel produz imagens borradas? :: Porque, quando há várias respostas possíveis, a média delas minimiza o erro, e a média de várias imagens é um borrão.

Qual a principal ideia das GANs em relação à função de perda? :: Trocar uma perda escrita à mão por um discriminador que aprende sozinho o que faz um exemplo parecer real.

Por que GANs não são boas para gerar texto? :: Porque palavras são escolhas discretas, e o gradiente do discriminador não atravessa a escolha de um token.

Uma GAN calcula a probabilidade de um exemplo? :: Não; ela gera exemplos, mas não fornece a probabilidade de um dado específico.

---
Próxima: [[02-Gerador-e-Discriminador|Gerador e discriminador]] · Trilha: [[GANs/00-Indice|GANs]]
