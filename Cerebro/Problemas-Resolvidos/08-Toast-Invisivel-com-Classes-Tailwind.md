---
tags: [problema-resolvido, reflex, css, interface, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Toast invisível: classe do Tailwind usada como valor de CSS

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · Reflex · componente `app_reflex/componentes/toast.py` e os badges de status.

## Sintoma e impacto

Mensagens de erro e aviso **não apareciam**. O usuário clicava em excluir, a operação era recusada pelo banco, o sistema gerava a mensagem — e a tela não mostrava nada.

Impacto real: transformou uma recusa legítima do banco em um bug aparente de interface, e custou duas rodadas de investigação. Ver [[05-Exclusao-Nao-Funciona-em-Cadastros|o caso completo]].

## Causa-raiz

Confusão entre dois mundos que se parecem:

```python
background="bg-red-50"    # ERRADO — isso é um NOME DE CLASSE do Tailwind
background="#fef2f2"      # CERTO  — isso é um VALOR de cor CSS
```

No Tailwind, `bg-red-50` é o nome de uma **classe** que você aplica em `class=`. Aqui ela foi passada como **valor** da propriedade CSS `background`. O navegador recebe `background: bg-red-50`, não entende, e **descarta a declaração em silêncio** — sem erro no console, sem aviso.

O elemento existia no DOM, com tamanho e texto. Só não tinha cor de fundo nem contraste, e ficava invisível sobre o fundo da página.

## Correção aplicada

Todas as cores do toast e dos badges reescritas em **hex literal**.

## Prevenção

> [!problema] Regra
> **Classe do Tailwind vai em `class`. Valor de cor vai em propriedade CSS.** Em componentes que recebem estilo como dicionário Python (Reflex, styled-components, estilos inline), só valores CSS válidos funcionam.

Sinal de alerta para reconhecer isso rápido: **o elemento existe no DOM mas não se vê**. Inspecione o elemento — se a propriedade aparece riscada nas ferramentas do navegador, o valor é inválido.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Tecnologia: [[../Tecnologias/01-Reflex|Reflex]] · [[../../TailwindCSS/00-Indice|Trilha Tailwind CSS]]
- Relacionado: [[05-Exclusao-Nao-Funciona-em-Cadastros|Exclusão que não funciona]]

## Perguntas de revisão

Por que background="bg-red-50" deixa o elemento invisível? :: Porque bg-red-50 é nome de classe do Tailwind, não valor de cor CSS; o navegador descarta a declaração em silêncio.

Qual a regra entre classe do Tailwind e valor CSS? :: Classe do Tailwind vai em class; valor de cor, como #fef2f2, vai na propriedade CSS.

Qual o sinal de alerta de um valor CSS inválido? :: O elemento existe no DOM mas não aparece, e a propriedade surge riscada nas ferramentas do navegador.
