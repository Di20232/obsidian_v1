---
tags: [css, layout, posicionamento, flashcards]
cssclasses: [cerebro-nota, cerebro-css]
---

# Posicionamento

## `position`: tirando um elemento do fluxo normal

Por padrão, elementos HTML seguem o **fluxo normal**: aparecem na página na ordem em que foram escritos, um depois do outro (ou lado a lado, se `inline`/`flex`/`grid`). A propriedade `position` permite alterar esse comportamento.

## `static`: o padrão, nada de especial

```css
.normal {
    position: static;   /* valor padrão de todo elemento — segue o fluxo normal */
}
```

## `relative`: desloca o elemento, mas mantém o espaço original reservado

```css
.deslocado {
    position: relative;
    top: 10px;      /* desloca 10px para BAIXO da posição original */
    left: 20px;      /* desloca 20px para a DIREITA da posição original */
}
```

O elemento se move visualmente, mas o espaço que ele **ocupava originalmente** no fluxo continua reservado — outros elementos não se movem para preencher esse espaço. `position: relative` também tem um segundo papel importante: cria um **ponto de referência** para elementos filhos com `position: absolute` (veja abaixo).

## `absolute`: sai completamente do fluxo, posiciona em relação a um ancestral

```css
.container {
    position: relative;   /* vira o "ponto zero" para o filho absoluto */
}

.selo {
    position: absolute;
    top: 10px;
    right: 10px;    /* posiciona no canto superior direito DO CONTAINER, não da página inteira */
}
```

`position: absolute` remove o elemento do fluxo normal (outros elementos passam a ignorá-lo completamente, como se ele não ocupasse espaço) e o posiciona em relação ao **ancestral mais próximo que tenha `position` diferente de `static`** — por isso é tão comum ver `position: relative` no container pai, só para servir de referência ao filho `absolute`. Se nenhum ancestral tiver isso, o elemento se posiciona em relação à página inteira.

**Uso mais comum**: um selo/badge no canto de um card, um ícone de fechar no canto de um modal, um menu suspenso (dropdown).

## `fixed`: gruda na tela, ignora rolagem

```css
.barra-fixa {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
}
```

Posicionado em relação à **janela do navegador** (viewport), não à página — permanece visível no mesmo lugar mesmo enquanto o usuário rola a página. Uso clássico: barra de navegação que fica sempre visível no topo, botão de "voltar ao topo".

## `sticky`: um meio-termo entre `relative` e `fixed`

```css
.cabecalho-secao {
    position: sticky;
    top: 0;    /* obrigatório: define o "limite" onde ele gruda */
}
```

Comporta-se como `relative` (segue o fluxo normal) **até** que a rolagem da página alcance o valor de `top` definido — a partir daí, "gruda" na tela como `fixed`, até que o elemento **pai** termine de rolar. Muito usado para cabeçalhos de seção (por exemplo, letras de um índice alfabético que grudam no topo enquanto você rola aquela seção).

## `z-index`: quem fica por cima de quem

```css
.atras { position: relative; z-index: 1; }
.frente { position: relative; z-index: 2; }
```

Quando elementos posicionados (`relative`, `absolute`, `fixed`, `sticky`) se sobrepõem visualmente, `z-index` decide a ordem de empilhamento — números maiores ficam **por cima** de números menores. Elementos sem `position` definida (ou `static`) ignoram `z-index` completamente.

## Resumo de quando usar cada `position`

| Valor | Uso típico |
|---|---|
| `static` | comportamento padrão, não precisa declarar |
| `relative` | pequenos ajustes finos, ou criar referência para um filho `absolute` |
| `absolute` | elemento posicionado dentro de um container específico (badge, dropdown) |
| `fixed` | elemento grudado na janela inteira (barra de navegação, botão flutuante) |
| `sticky` | elemento que gruda só enquanto está dentro do seu container (cabeçalho de seção) |

## Exercício

Abra `CSS/exemplos/06_posicionamento.html`. Crie um card com um selo "Novo" posicionado no canto superior direito usando `position: relative` no card e `position: absolute` no selo. Depois, crie uma barra de navegação com `position: sticky; top: 0;` no topo de uma página com bastante conteúdo, e role a página para ver o comportamento.

## Perguntas de revisão

O que faz position: relative? :: Desloca o elemento mantendo o espaço original, e serve de referência para filhos absolute.

Em relação a quê um elemento absolute se posiciona? :: Ao ancestral mais próximo com position diferente de static; sem nenhum, à página.

Qual a diferença entre fixed e sticky? :: fixed fica sempre na mesma posição da janela; sticky segue o fluxo até atingir o limite de top e então gruda dentro do container pai.

O que decide o z-index? :: Qual elemento posicionado fica por cima; números maiores ficam na frente.

O z-index funciona em elementos static? :: Não; só em elementos com position relative, absolute, fixed ou sticky.

---
Veja o exemplo em `CSS/exemplos/06_posicionamento.html`. Próxima nota: [[07-Responsividade]]
