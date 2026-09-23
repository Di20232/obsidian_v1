---
tags: [programacao, debugging, testes]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Debugging e Testes

## Debugging não é um sinal de fracasso, é parte do trabalho

Todo programa que você escreve, em qualquer linguagem, vai ter comportamento inesperado em algum momento — isso não é exceção, é a regra. **Debugging** é o processo sistemático de descobrir **por que** o código não faz o que deveria. A diferença entre alguém iniciante e alguém experiente não é a ausência de bugs, é a velocidade e o método para encontrá-los.

## Nível 1: leitura do erro

Você já viu isso em [[../Python/13-Tratamento-de-Erros]] — um traceback do Python mostra o tipo do erro e a linha exata onde ele aconteceu. **Sempre leia a última linha primeiro** — ela costuma dizer exatamente o tipo de problema (`ValueError`, `TypeError`, etc.) e uma descrição.

## Nível 2: print debugging

A técnica mais simples e ainda extremamente usada: inserir `print()` em pontos estratégicos do código para ver o valor real das variáveis em cada etapa:

```python
def calcular_media(notas):
    print(f"notas recebidas: {notas}")   # print de depuração
    soma = sum(notas)
    print(f"soma: {soma}")                # print de depuração
    media = soma / len(notas)
    return media
```

Depois de resolver o problema, remova esses prints — eles são temporários, não parte do código final.

## Nível 3: o debugger de verdade

Um **debugger** (como o integrado no VS Code, mencionado em [[../Python/02-Instalando-Python]]) permite:
- Colocar um **breakpoint**: um ponto onde a execução **pausa**.
- Inspecionar o valor de **todas** as variáveis naquele momento exato, sem precisar adivinhar onde colocar `print`.
- Avançar **uma linha por vez** (step), observando exatamente como o estado do programa muda.

Isso é mais poderoso que `print()` porque você não precisa saber de antemão o que quer observar — pode explorar livremente uma vez pausado.

## Isolando o problema

Uma técnica geral, independente de ferramenta: quando algo não funciona, **reduza o problema ao menor caso possível** que ainda reproduz o erro. Se um programa de 200 linhas falha, tente isolar as 5-10 linhas relevantes em um script separado — isso remove ruído e frequentemente já revela a causa.

## Testes automatizados: prevenir em vez de caçar

Debugging conserta um problema já encontrado. **Testes automatizados** existem para pegar problemas **antes** de virarem bugs em produção, e para garantir que uma mudança nova não quebrou algo que já funcionava (chamado de **regressão**).

```python
def somar(a, b):
    return a + b

def test_somar_positivos():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-1, -1) == -2

def test_somar_com_zero():
    assert somar(0, 5) == 5
```

Com a biblioteca `pytest` (a mais usada em projetos Python; `pip install pytest`), basta rodar `pytest` no terminal ([[02-Terminal-e-Linha-de-Comando]]) e ela encontra e roda automaticamente todas as funções que começam com `test_`, reportando quais passaram e quais falharam.

## O que testar

- **Caso normal**: a entrada esperada, o "caminho feliz".
- **Casos de borda (edge cases)**: valores extremos ou incomuns — lista vazia, número zero, número negativo, texto vazio.
- **Casos de erro**: entradas que devem falhar de propósito (conectando com [[../Python/13-Tratamento-de-Erros]]) — confirmar que o erro certo é levantado.

```python
import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

def test_dividir_por_zero_levanta_erro():
    with pytest.raises(ValueError):
        dividir(10, 0)
```

## Por que isso compensa o tempo investido

Escrever testes parece "trabalho extra" no começo. O retorno aparece quando o projeto cresce: você pode mudar uma função no meio de um sistema grande e, rodando os testes, saber **em segundos** se quebrou algo em outra parte — em vez de descobrir isso meses depois, com um usuário real reportando o problema.

## Exercício

Pegue a função `eh_par` que você escreveu no exercício de [[../Python/11-Funcoes]] e escreva 3 testes para ela usando `assert`: um número par, um número ímpar, e o caso de borda `0` (que é par).

---
Próxima nota: [[13-Boas-Praticas-de-Codigo]]
