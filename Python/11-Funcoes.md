---
tags: [python, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Funções

## O problema que isso resolve

Repare que você já usou `print()`, `int()`, `len()`, `range()` — todas são **funções prontas** do Python. Uma função é um bloco de código nomeado, que faz uma tarefa específica, e que você pode **chamar quantas vezes quiser** sem reescrever a lógica toda vez. Isso evita repetição de código (se um dia precisar mudar como algo funciona, muda em um lugar só) e organiza o programa em partes com responsabilidades claras.

## Criando sua própria função

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Diego")   # chama a função -> "Olá, Diego!"
saudacao("Ana")      # chama de novo, com outro valor
```

Desmontando:
- `def` inicia a definição de uma função.
- `saudacao` é o nome escolhido (mesmas regras de nomes de variáveis, [[04-Variaveis-e-Tipos]]).
- `(nome)` é o **parâmetro** — um "espaço reservado" para um valor que será informado em cada chamada.
- `:` e o bloco indentado abaixo — igual à sintaxe de `if`/`for` que você já conhece.
- **Definir** a função (`def ...`) não a executa. Ela só roda quando você **chama** (`saudacao("Diego")`).

`"Diego"` na chamada é chamado de **argumento** — o valor real que preenche o parâmetro `nome` daquela vez.

## `return`: devolvendo um valor

`print()` dentro da função só mostra algo na tela — não devolve nada para ser usado depois. Para uma função **calcular e devolver** um valor, usa-se `return`:

```python
def somar(a, b):
    return a + b

resultado = somar(3, 4)
print(resultado)          # 7
print(somar(10, 5) * 2)   # 30 -> o retorno pode ser usado em outra expressão
```

Assim que o Python executa um `return`, a função **termina imediatamente** — nada depois dele, na mesma função, é executado.

## Parâmetros com valor padrão

```python
def saudacao(nome, saudacao_inicial="Olá"):
    print(f"{saudacao_inicial}, {nome}!")

saudacao("Diego")               # "Olá, Diego!" -> usa o padrão
saudacao("Diego", "Bom dia")    # "Bom dia, Diego!" -> sobrescreve o padrão
```

Isso torna a função flexível sem obrigar quem a usa a sempre informar todos os detalhes.

## Argumentos nomeados (keyword arguments)

```python
def apresentar(nome, idade, cidade):
    print(f"{nome}, {idade} anos, de {cidade}")

apresentar(nome="Diego", cidade="São Paulo", idade=25)  # ordem não importa quando nomeado
```

Útil quando a função tem muitos parâmetros — deixa a chamada mais legível e evita erro de trocar a ordem.

## Escopo: onde uma variável "existe"

```python
def calcular():
    resultado = 10  # existe só dentro desta função
    return resultado

print(calcular())
print(resultado)   # ERRO: NameError -> "resultado" não existe fora da função
```

**Por que isso importa**: variáveis criadas dentro de uma função são locais a ela — isso evita que funções diferentes acidentalmente interfiram nos dados umas das outras. É uma proteção, não uma limitação.

## Por que quebrar código em funções

Sem funções, um programa vira um único bloco enorme e repetitivo. Com funções, cada pedaço tem um nome que já explica o que faz, pode ser testado isoladamente, e pode ser reaproveitado. Regra prática: se você percebe que copiou e colou o mesmo trecho de código duas vezes, é sinal de que ele deveria virar uma função.

## Exercício

Escreva uma função `eh_par(numero)` que recebe um número e **retorna** `True` se for par e `False` se for ímpar (não use `print` dentro dela). Depois, use um `for` (de [[08-Lacos-de-Repeticao]]) para testar a função com os números de 1 a 10, imprimindo o número e o resultado.

## Perguntas de revisão

O que é uma função? :: Um bloco de código nomeado que faz uma tarefa e pode ser chamado várias vezes sem reescrever a lógica.

Qual a diferença entre parâmetro e argumento? :: Parâmetro é o nome reservado na definição da função; argumento é o valor real passado na chamada.

Qual a diferença entre print e return numa função? :: print só mostra na tela; return devolve o valor para ser usado em outra parte do código e encerra a função.

O que é escopo local? :: Variáveis criadas dentro de uma função existem só dentro dela, o que evita interferência entre funções.

Quando transformar um trecho de código em função? :: Quando o mesmo trecho foi copiado e colado mais de uma vez.

Definir uma função com def a executa? :: Não; ela só roda quando é chamada.

---
Veja o exemplo em `Python/exemplos/11_funcoes.py`. Próxima nota: [[12-Modulos-e-Pacotes]]
