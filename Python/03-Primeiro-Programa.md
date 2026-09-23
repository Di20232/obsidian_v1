---
tags: [python, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Primeiro Programa

## O ritual do "Olá, mundo"

Tradicionalmente, o primeiro programa em qualquer linguagem apenas exibe uma mensagem na tela. Isso confirma que: o interpretador está instalado, você sabe criar e rodar um arquivo, e o ambiente está funcionando ponta a ponta. Não é sobre o código em si — é sobre validar o processo.

## Criando o arquivo

Crie um arquivo chamado `ola_mundo.py` (a extensão `.py` é obrigatória — é como o sistema e o interpretador identificam "isto é código Python") com este conteúdo:

```python
print("Olá, mundo!")
```

Veja o exemplo completo em `Python/exemplos/03_ola_mundo.py`.

## Executando

No terminal, navegue até a pasta do arquivo e rode:

```bash
python 03_ola_mundo.py
```

O terminal deve mostrar:

```
Olá, mundo!
```

## Desmontando essa única linha

- `print(...)` é uma **função**: um bloco de código pronto, que já vem embutido no Python, que faz uma tarefa específica — nesse caso, exibir algo na tela. Vamos estudar funções a fundo em [[11-Funcoes]], mas já dá pra usar uma sem entender tudo por trás.
- `(...)` — os parênteses indicam que você está **chamando** (executando) a função `print`, e o que está dentro deles é o que você está entregando para ela usar, chamado de **argumento**.
- `"Olá, mundo!"` — texto entre aspas é chamado de **string** (cadeia de caracteres). Aspas dizem ao Python "isto é texto literal, não é um comando".

## Por que a indentação importa em Python

Diferente de outras linguagens que usam chaves `{ }` para marcar blocos de código, **Python usa espaços no início da linha (indentação)** para isso. Ainda não vimos blocos (isso aparece em [[07-Condicionais]]), mas já vale gravar a regra: **em Python, espaços no começo da linha têm significado**. Um espaço a mais ou a menos onde não deveria gera erro. O padrão da comunidade é usar **4 espaços** por nível — a maioria dos editores já faz isso automaticamente ao apertar Tab.

## Comentários

Qualquer texto depois de `#` na mesma linha é ignorado pelo interpretador. Serve para você (ou outra pessoa) explicar o "porquê" de um trecho de código:

```python
# Isto é um comentário: o Python não executa esta linha.
print("Isto sim é executado.")  # comentário no fim da linha também funciona
```

## Erros comuns

- Esquecer as aspas em volta do texto → `print(Olá, mundo!)` dá erro, porque o Python tenta interpretar `Olá` como um comando/nome, não como texto.
- Esquecer de fechar um parêntese ou aspas.
- Salvar o arquivo sem a extensão `.py`.

Quando algo dá erro, o Python mostra um **traceback**: um texto (às vezes assustador à primeira vista) que aponta a linha exata do problema e o tipo de erro. Leia sempre de baixo para cima — a última linha costuma dizer o essencial.

## Exercício

Altere `03_ola_mundo.py` para imprimir seu próprio nome em uma linha e uma frase sobre por que você está aprendendo Python em outra linha (duas chamadas de `print`).

## Perguntas de revisão

O que faz print("Olá, mundo!")? :: Chama a função print para exibir o texto entre aspas na tela.

O que é um argumento de função? :: O valor entregue entre os parênteses na chamada da função, para ela usar.

Por que a indentação importa em Python? :: Porque Python usa os espaços no início da linha para marcar blocos de código; o padrão é 4 espaços por nível.

Como escrever um comentário em Python? :: Com # antes do texto; tudo depois de # na linha é ignorado pelo interpretador.

Como ler um traceback do Python? :: De baixo para cima: a última linha diz o tipo do erro e o essencial, e acima aparece a linha exata do problema.

---
Próxima nota: [[04-Variaveis-e-Tipos]]
