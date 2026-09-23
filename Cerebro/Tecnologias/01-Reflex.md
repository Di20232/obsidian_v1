---
tags: [tecnologia, python, reflex, interface, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Reflex — Python que vira React

Framework em que se escreve **Python** e o resultado compila para uma aplicação **React**. Usado no [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]].

## Por que foi escolhido

Permitiu construir uma interface web moderna **sem escrever JavaScript**, reaproveitando integralmente a camada de banco (`db.py`) que já existia desde a versão Tkinter.

## O conceito que explica todos os erros: Var

Dentro de um componente, os valores **não são dados Python** — são **`Var`**: referências que só viram valor de verdade no navegador.

Quase todo erro de Reflex vem de tratar um `Var` como se fosse um valor comum.

| O que você escreve | Funciona? | O que acontece |
|---|---|---|
| `str(var)` | ❌ | Converte a **referência** em texto, não o dado → [[../Problemas-Resolvidos/06-Selects-Reflex-Nao-Enviam-Valor|caso real]] |
| `var1 and var2` | ❌ | `and` é palavra-chave, não pode ser sobrecarregada → [[../Problemas-Resolvidos/07-Operadores-Python-em-Var-do-Reflex|caso real]] |
| `var1 & var2` | ✅ | Operador bitwise, o Reflex intercepta |
| `var > 0` | ✅ | Comparações são sobrecarregadas |
| `if var: ...` | ❌ | Avalia ao montar a página, não no navegador |
| `rx.cond(var, a, b)` | ✅ | A forma correta de condicional reativa |

> [!programacao] A regra que evita a família inteira
> **Calcule no estado, apresente no template.** Se você precisa de lógica sobre um valor da tela, faça no *event handler* — lá os dados são dicionários Python de verdade.

## Outras armadilhas que custaram tempo

**Link não é botão.** `rx.link` sem `href` válido compila para uma âncora; o clique navega e **cancela o evento WebSocket** antes de ele chegar ao servidor. Use `rx.button(type="button")` para qualquer coisa que **age**. → [[../Problemas-Resolvidos/05-Exclusao-Nao-Funciona-em-Cadastros|caso real]]

**Estilo recebe valor CSS, não classe.** `background="bg-red-50"` é nome de classe do Tailwind, não cor. O navegador descarta em silêncio e o elemento fica invisível. → [[../Problemas-Resolvidos/08-Toast-Invisivel-com-Classes-Tailwind|caso real]]

**Editar não basta — precisa recompilar.** Uma alteração que "não apareceu" muitas vezes só não foi compilada.

## Como executar

```bash
py -m reflex run --loglevel error
```

Sobe em `http://localhost:3000`. Depende de Node instalado (o Reflex gera e empacota o front). O bundle compilado fica em `.web/` — e **inspecioná-lo é a forma mais confiável de confirmar** o que um componente virou de fato.

## Organização que funcionou

```
app_reflex/
├── estados/       lógica Python (um arquivo por tela)
├── paginas/       composição visual
└── componentes/   reutilizáveis (selects, toast, cartões, badges)
```

Separar **estados** de **páginas** foi o que tornou possível mover a lógica para fora do template — a correção que resolveu a família de bugs de `Var`.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Trilha: [[../../Python/00-Indice|Python]]
- Mapa: [[../Mapas/01-Mapa-Web|Mapa Web]]

## Perguntas de revisão

O que é o Reflex? :: Um framework em que se escreve Python e o resultado compila para uma aplicação React.

O que é um Var no Reflex? :: Uma referência a um valor que só vira dado real no navegador; tratá-la como valor Python comum causa a maioria dos erros.

Qual a regra que evita os erros com Var no Reflex? :: Calcular no estado, no event handler, e só apresentar no template.

Onde fica o bundle compilado do Reflex? :: Na pasta .web; inspecioná-lo confirma o que cada componente virou.

Como organizar um app Reflex? :: Separar estados (lógica), páginas (composição visual) e componentes reutilizáveis.
