---
tags: [ia, gans, treino, colapso-de-modos, depuracao, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Problemas do treino de GANs

Treinar uma GAN é procurar o **equilíbrio** entre duas redes que mudam ao mesmo tempo, e não o mínimo de uma única perda. Esse equilíbrio é frágil. Os problemas clássicos são o **colapso de modos**, a **oscilação** sem convergência e o **gradiente que desaparece** quando o discriminador vence. Esta nota mostra como reconhecer cada um e o que costuma resolver.

## Colapso de modos

Um **modo** é um "tipo" de exemplo nos dados: cada dígito de 0 a 9, cada raça de cachorro, cada grupo de pontos. Há **colapso de modos** (*mode collapse*) quando o gerador produz **pouca variedade**: ele acha algumas saídas que enganam o discriminador e passa a repetir só elas.

- **Colapso total:** a mesma saída para qualquer ruído. O tutorial de GANs do Goodfellow (2016) chama isso de "cenário Helvetica".
- **Colapso parcial** (*mode dropping*): o gerador cobre alguns modos e ignora outros. É o caso mais comum, e o mais traiçoeiro, porque cada amostra isolada parece boa.

**Por que acontece:** o gerador é recompensado por enganar o discriminador **agora**, não por cobrir os dados inteiros. Se uma saída engana, concentrar tudo nela é o caminho mais curto. O discriminador aprende a rejeitá-la, o gerador pula para outra, e o ciclo se repete.

> [!example] No exemplo do cofre
> A [[08-GAN-em-PyTorch|GAN 2D]] tenta imitar 8 grupos de pontos num círculo. Com a perda original e 5 sementes diferentes, ela cobriu **6, 7, 3, 7 e 7** dos 8 grupos: colapso parcial em todas as rodadas. Na semente 2, o discriminador venceu (a perda dele caiu para 0,83) e só 3 grupos sobraram. Na [[10-Experimento-GAN-com-as-Notas|GAN de texto]], o colapso aparece como **trechos repetidos**, e por isso o script mede a "variedade".

## Oscilação e não convergência

Como cada rede muda o alvo da outra, o treino pode **girar em círculos**: o gerador migra de um modo para outro, o discriminador corre atrás, e as amostras melhoram e pioram em ondas. As perdas sobem e descem sem tendência. Aqui não há um "fundo do vale" para onde descer.

## O discriminador vence e o gradiente some

Se o discriminador fica bom demais, ele rejeita todos os falsos com certeza total. Na perda original, isso **satura** o gradiente do gerador ([[03-Como-o-Treino-Funciona|perda não saturante]]).

Há um motivo mais profundo, mostrado por Arjovsky e Bottou (2017): imagens reais ocupam uma "fatia" muito fina de todos os arranjos de pixels possíveis, e as do gerador ocupam outra. Quando essas fatias **não se tocam**, a divergência de Jensen-Shannon fica constante (log 2), não importa o quanto o gerador se aproxime. Sem variação, não há gradiente para dizer para onde ir. Esse é o ponto de partida do [[05-WGAN-e-Estabilizacao|WGAN]].

## Sensibilidade a hiperparâmetros

Pequenas mudanças na taxa de aprendizado, nos betas do Adam, no tamanho do lote ou na normalização podem separar um treino bom de um que diverge. No exemplo 2D do cofre, a mesma WGAN-GP com taxa 0,0001 ainda estava longe de convergir em 3.000 passos, e com 0,001 chegou perto. Mude **uma coisa por vez** e anote o resultado.

## Sintoma, causa provável e o que tentar

| Sintoma | Causa provável | O que tentar |
|---|---|---|
| Amostras quase iguais entre si | colapso de modos | [[05-WGAN-e-Estabilizacao\|WGAN-GP]]; lote maior; camada de desvio-padrão do lote no discriminador (ProGAN) |
| Perda do discriminador perto de 0 e gerador parado | discriminador forte demais | taxa menor para o discriminador; suavizar rótulos reais (0,9 em vez de 1); normalização espectral |
| Perdas oscilando e amostras piorando em ondas | instabilidade do jogo | taxa de aprendizado menor; β1 = 0,5 ou 0; média móvel (EMA) dos pesos do gerador |
| Valores `NaN` na perda | gradiente explodindo | penalidade de gradiente; taxa menor; conferir a normalização dos dados |
| Padrão de "tabuleiro de xadrez" nas imagens | convolução transposta com passo que não divide o tamanho do filtro | ampliar a imagem (*upsample*) e depois aplicar convolução comum |
| Amostras idênticas a exemplos de treino | memorização | menos épocas; mais dados; conferir vizinho mais próximo ([[07-Avaliar-GANs\|avaliação]]) |

## Hábitos que evitam dor de cabeça

1. **Ruído fixo para acompanhar:** sorteie um conjunto de vetores *z* no início e gere a partir deles a cada relatório. Assim a comparação entre etapas é justa. Os dois scripts do cofre fazem isso.
2. **Salvar o modelo de tempos em tempos:** o melhor gerador muitas vezes **não é o último**. O treino pode piorar depois de um bom momento.
3. **Medir, não só olhar:** a vista humana não percebe falta de variedade numa grade de 16 imagens. Use uma métrica de cobertura ([[07-Avaliar-GANs|avaliar GANs]]).
4. **Começar pequeno:** teste a ideia num problema de brinquedo (como os pontos 2D) antes de gastar horas de GPU.

## Perguntas de revisão

O que é colapso de modos numa GAN? :: Quando o gerador produz pouca variedade, repetindo poucas saídas que enganam o discriminador.

Qual a diferença entre colapso total e colapso parcial de modos? :: No total, o gerador produz a mesma saída para qualquer ruído; no parcial, cobre só alguns tipos de exemplo e ignora os outros.

Por que o gerador tende ao colapso de modos? :: Porque é recompensado por enganar o discriminador no momento, não por cobrir toda a variedade dos dados.

Por que o gradiente do gerador some quando o discriminador é perfeito? :: Porque a perda satura e, com distribuições que não se sobrepõem, a divergência de Jensen-Shannon fica constante, sem indicar direção.

Por que o treino de uma GAN pode oscilar sem convergir? :: Porque cada rede muda o alvo da outra, e o gerador pode migrar de modo em modo enquanto o discriminador corre atrás.

O que fazer quando a perda do discriminador vai a zero e o gerador para de melhorar? :: Enfraquecer o discriminador: taxa de aprendizado menor, rótulos reais suavizados para 0,9 ou normalização espectral.

O que causa o padrão de tabuleiro de xadrez em imagens geradas? :: Convolução transposta cujo passo não divide o tamanho do filtro; ampliar a imagem e depois aplicar convolução comum resolve.

Por que usar ruído fixo para acompanhar o treino de uma GAN? :: Para comparar as etapas sempre com as mesmas entradas, sem que a avaliação mude os sorteios do treino.

Por que salvar o modelo durante o treino de uma GAN? :: Porque o treino pode piorar depois de um bom momento, e o melhor gerador muitas vezes não é o último.

Quantos dos 8 grupos a GAN original cobriu no exemplo 2D do cofre? :: Entre 3 e 7, conforme a semente; colapso parcial em todas as 5 rodadas (conferido em 06/10/2026).

---
Anterior: [[03-Como-o-Treino-Funciona|Como o treino funciona]] · Próxima: [[05-WGAN-e-Estabilizacao|WGAN e estabilização]] · Trilha: [[GANs/00-Indice|GANs]]
