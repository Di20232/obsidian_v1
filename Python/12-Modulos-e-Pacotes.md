---
tags: [python, basico, flashcards]
cssclasses: [cerebro-nota, cerebro-python]
---

# Módulos e Pacotes

## O problema que isso resolve

Ninguém precisa reinventar tudo do zero. Python já vem com uma "caixa de ferramentas" enorme embutida (a **biblioteca padrão**), e existe um repositório mundial de código pronto feito por outras pessoas (o **PyPI**). Módulos e pacotes são o mecanismo para **usar** código que não está no seu arquivo atual — seja da biblioteca padrão, de terceiros, ou escrito por você mesmo em outro arquivo.

## O que é um módulo

Um módulo é, na prática, **um arquivo `.py`** com código (funções, variáveis) que pode ser importado em outro arquivo. A biblioteca padrão do Python já vem com dezenas de módulos prontos.

```python
import math

print(math.sqrt(16))    # 4.0 -> raiz quadrada
print(math.pi)            # 3.141592653589793
```

`import math` diz ao Python "carregue o módulo `math` e disponibilize seu conteúdo através do nome `math`". Depois, `math.sqrt(...)` acessa a função `sqrt` que pertence a esse módulo (mesma lógica de `.` que você viu em métodos de string, [[10-Strings]]).

## Importando partes específicas

```python
from math import sqrt, pi

print(sqrt(16))   # não precisa mais escrever math.sqrt
print(pi)
```

Use isso quando for usar poucas coisas de um módulo grande e quiser um código mais curto. Cuidado: importar tudo com `from math import *` é considerado má prática, porque some a clareza de "de onde veio essa função".

## Módulos úteis da biblioteca padrão (para conhecer)

```python
import random
print(random.randint(1, 10))    # número aleatório entre 1 e 10

import datetime
hoje = datetime.date.today()
print(hoje)

import os
print(os.getcwd())    # pasta atual onde o programa está rodando
```

## Criando seu próprio módulo

Se você criar um arquivo `utilidades.py` com:

```python
# utilidades.py
def dobro(numero):
    return numero * 2
```

Pode usá-lo de outro arquivo **na mesma pasta**:

```python
# programa.py
import utilidades

print(utilidades.dobro(5))   # 10
```

Isso é o começo de organizar um projeto maior em vários arquivos, em vez de um único arquivo gigante.

## Pacotes e `pip`

Um **pacote** é uma coleção de módulos, geralmente publicada por terceiros, que você instala com a ferramenta `pip` (que já vem junto com o Python):

```bash
pip install requests
```

Depois de instalado, você importa normalmente:

```python
import requests

resposta = requests.get("https://exemplo.com")
print(resposta.status_code)
```

Pacotes de terceiros populares: `requests` (fazer requisições web), `pandas` (análise de dados em tabelas), `flask`/`django` (desenvolvimento web).

## Por que isso importa desde já

Você não precisa decorar módulos agora, mas precisa entender o **conceito**: sempre que precisar de uma funcionalidade que parece "básica demais para eu ter que escrever do zero" (datas, números aleatórios, requisições à internet), provavelmente já existe um módulo pronto para isso. Parte da habilidade de programar é saber procurar antes de reinventar.

## Exercício

Use o módulo `random` para simular o lançamento de um dado (número aleatório entre 1 e 6), rodando isso 5 vezes dentro de um `for` (de [[08-Lacos-de-Repeticao]]).

## Perguntas de revisão

O que é um módulo em Python? :: Um arquivo .py com funções e variáveis que pode ser importado em outro arquivo.

Qual a diferença entre import math e from math import sqrt? :: import math exige escrever math.sqrt; from math import sqrt permite usar sqrt direto.

Por que evitar from modulo import *? :: Porque some a clareza de onde cada função veio.

Como instalar um pacote de terceiros em Python? :: Com pip install nome_do_pacote, que baixa do repositório PyPI.

O que é a biblioteca padrão do Python? :: O conjunto de módulos que já vem com o Python, como math, random, datetime e os.

---
Veja o exemplo em `Python/exemplos/12_modulos.py`. Próxima nota: [[13-Tratamento-de-Erros]]
