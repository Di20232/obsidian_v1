---
tags: [python, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Arquivos (leitura e escrita)

## O problema que isso resolve

Tudo que você guardou em variáveis, listas ou dicionários até agora **desaparece quando o programa termina** — isso é memória temporária (RAM). Para que um dado sobreviva depois que o programa fecha, ele precisa ser salvo em **disco**, em um arquivo. Ler e escrever arquivos é como um programa persiste (guarda de verdade) informação.

## Escrevendo em um arquivo

```python
arquivo = open("notas.txt", "w")   # "w" = write (escrever)
arquivo.write("Primeira linha\n")
arquivo.write("Segunda linha\n")
arquivo.close()
```

- `open("notas.txt", "w")` abre (ou cria, se não existir) o arquivo para escrita.
- `\n` dentro da string é um **caractere de quebra de linha** — sem ele, tudo ficaria numa linha só.
- `"w"` **apaga o conteúdo anterior** do arquivo, se ele já existir. Cuidado com isso.
- `.close()` fecha o arquivo, liberando-o. Esquecer de fechar pode causar dados não salvos corretamente ou o arquivo ficar bloqueado para outros programas.

## A forma recomendada: `with`

```python
with open("notas.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
# o arquivo é fechado automaticamente ao sair deste bloco, mesmo se der erro
```

`with` garante o fechamento automático do arquivo, mesmo que aconteça um erro no meio do processo (conectando com [[13-Tratamento-de-Erros]]: é uma forma de "finally" embutida especificamente para arquivos). Por isso é a forma preferida por praticamente todo código Python profissional.

## Modos de abertura

| Modo | Significado |
|---|---|
| `"w"` | escrever — apaga o conteúdo existente |
| `"a"` | append — adiciona ao final, sem apagar o que já existe |
| `"r"` | ler — modo padrão se você não especificar nada |

## Lendo um arquivo

```python
with open("notas.txt", "r") as arquivo:
    conteudo = arquivo.read()   # lê tudo de uma vez, como uma única string
print(conteudo)
```

Lendo linha por linha (útil para arquivos grandes, ou quando você quer processar cada linha separadamente):

```python
with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())   # .strip() remove o \n do final de cada linha
```

## Adicionando sem apagar (`"a"`)

```python
with open("notas.txt", "a") as arquivo:
    arquivo.write("Terceira linha, adicionada depois\n")
```

## Lidando com arquivo que não existe

```python
try:
    with open("nao_existe.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Esse arquivo não existe.")
```

Isso conecta diretamente com [[13-Tratamento-de-Erros]]: tentar ler um arquivo inexistente é um erro esperado e recorrente, então deve ser tratado, não deixado quebrar o programa.

## Caminho de arquivo: relativo vs. absoluto

`"notas.txt"` é um **caminho relativo** — o Python procura esse arquivo na pasta em que o programa está sendo executado. Você também pode usar um **caminho absoluto**, apontando o local exato no computador:

```python
with open(r"C:\Users\Diego\Documents\notas.txt", "r") as arquivo:
    print(arquivo.read())
```

O `r` antes das aspas cria uma **raw string**, que trata `\` literalmente em vez de tentar interpretá-lo como início de um caractere especial (como o `\n` que você viu acima) — importante porque caminhos do Windows usam `\`.

## Exercício

Escreva um programa que peça 3 tarefas via `input()` (um `for` de [[08-Lacos-de-Repeticao]] rodando 3 vezes) e salve cada uma em uma linha de um arquivo `tarefas.txt`. Depois, em outra parte do mesmo programa, abra esse arquivo em modo leitura e imprima todas as tarefas numeradas.

## Perguntas de revisão

Qual a diferença entre os modos w, a e r ao abrir arquivo? :: w escreve apagando o conteúdo anterior, a adiciona ao final e r lê, sendo o padrão.

Por que abrir arquivos com with? :: Porque o arquivo é fechado automaticamente ao sair do bloco, mesmo se ocorrer erro.

Que erro ocorre ao abrir para leitura um arquivo que não existe? :: FileNotFoundError.

Para que serve o r antes de um caminho do Windows, como r"C:\pasta"? :: Cria uma raw string, que trata a barra invertida literalmente em vez de como caractere especial.

Por que salvar dados em arquivo? :: Porque variáveis ficam na memória temporária e somem quando o programa termina; o arquivo em disco persiste.

---
Veja o exemplo em `Python/exemplos/14_arquivos.py`. Próxima nota: [[15-Programacao-Orientada-a-Objetos]]
