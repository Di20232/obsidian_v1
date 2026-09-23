---
tags: [programacao, web, fundamentos, flashcards]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Como a Web Funciona

## O modelo cliente-servidor

Quando você digita um endereço no navegador, dois programas diferentes conversam:

- **Cliente**: o navegador (ou um app, ou outro programa) que **pede** informação.
- **Servidor**: um programa, rodando em outro computador (às vezes do outro lado do mundo), que **responde** a esses pedidos.

Essa conversa segue um protocolo (um conjunto de regras combinadas) chamado **HTTP**.

## Requisição e resposta HTTP

Toda interação segue o mesmo padrão: o cliente envia uma **requisição**, o servidor devolve uma **resposta**.

Uma requisição tem, entre outras coisas:
- Um **método**: o que está sendo pedido.
  - `GET` — buscar/ler dados (abrir uma página, buscar uma lista de produtos).
  - `POST` — enviar/criar dados (submeter um formulário, criar um usuário).
  - `PUT`/`PATCH` — atualizar dados existentes.
  - `DELETE` — remover dados.
- Uma **URL**: o endereço do recurso pedido (`https://exemplo.com/usuarios/5`).
- Às vezes, um **corpo** (body): dados enviados junto, como os campos de um formulário.

Uma resposta tem:
- Um **código de status**: um número que resume o resultado.
  - `200` — sucesso.
  - `201` — criado com sucesso (comum após um `POST`).
  - `301`/`302` — redirecionamento.
  - `400` — requisição malformada (erro do cliente).
  - `401`/`403` — não autenticado / sem permissão.
  - `404` — não encontrado.
  - `500` — erro interno do servidor.
- Um **corpo**: o conteúdo da resposta em si (o HTML de uma página, ou dados).

## APIs: servidores que respondem dados, não páginas

Uma página HTML é feita para humanos lerem no navegador. Uma **API** (Application Programming Interface) é um servidor feito para **programas** conversarem entre si — em vez de devolver HTML, devolve dados estruturados, geralmente em **JSON**.

## JSON: o formato universal de troca de dados

```json
{
    "nome": "Diego",
    "idade": 25,
    "cidade": "São Paulo",
    "hobbies": ["programação", "leitura"]
}
```

Repare a semelhança direta com um dicionário Python (visto em [[../Python/09-Listas-Tuplas-Dicionarios]]) — não é coincidência: JSON foi inspirado na sintaxe de objetos do JavaScript, e mapeia quase 1:1 para dicionários e listas em Python.

```python
import json

dados = {"nome": "Diego", "idade": 25}
texto_json = json.dumps(dados)      # dicionário -> texto JSON
print(texto_json)

dados_de_volta = json.loads(texto_json)  # texto JSON -> dicionário
print(dados_de_volta["nome"])
```

## Consumindo uma API a partir do Python

```python
import requests

resposta = requests.get("https://api.exemplo.com/usuarios/5")
print(resposta.status_code)   # 200, por exemplo
dados = resposta.json()        # converte a resposta JSON direto em dicionário/lista
print(dados["nome"])
```

`requests` é um pacote de terceiros (visto o conceito em [[../Python/12-Modulos-e-Pacotes]]), instalado com `pip install requests`, e é a forma mais comum de um script Python conversar com serviços na internet.

## REST: um padrão de organizar APIs

**REST** é um estilo (não uma tecnologia específica) de organizar APIs em torno de **recursos**, usando os métodos HTTP de forma consistente:

```
GET    /usuarios         -> lista todos os usuários
GET    /usuarios/5        -> busca o usuário de id 5
POST   /usuarios          -> cria um novo usuário
PUT    /usuarios/5        -> atualiza o usuário de id 5
DELETE /usuarios/5        -> remove o usuário de id 5
```

A maioria das APIs que você vai consumir ou construir na carreira segue (ao menos parcialmente) esse padrão — reconhecer essa estrutura acelera muito entender uma API nova.

## Autenticação, rapidamente

Como um servidor sabe quem está fazendo a requisição? Formas comuns:
- **API key**: uma chave secreta enviada junto de cada requisição.
- **Token (ex.: JWT)**: um código gerado no login, enviado nas requisições seguintes para provar "eu já me autentiquei antes".

## Front-end vs. back-end, juntando tudo

- **Front-end**: o que roda no navegador do usuário — HTML ([[07-HTML-e-CSS]]), CSS, JavaScript ([[08-JavaScript-Basico]]).
- **Back-end**: o que roda no servidor — recebe requisições, consulta o banco de dados ([[09-SQL-e-Bancos-de-Dados]]), aplica regras de negócio, devolve respostas. Pode ser escrito em Python (com frameworks como Flask ou Django), JavaScript/Node.js, Java, Go, entre outros.

Quando você abre uma rede social, o front-end pede dados ao back-end via API (HTTP + JSON), e o back-end busca esses dados no banco de dados — esse ciclo completo é o que "fazer um site" realmente envolve por trás.

## Exercício

Use `requests` em Python para buscar dados de uma API pública gratuita (por exemplo, `https://api.github.com/users/octocat`), imprima o código de status da resposta e alguns campos do JSON retornado.

## Perguntas de revisão

O que é o modelo cliente-servidor? :: O cliente, como o navegador, pede informação e o servidor responde, seguindo o protocolo HTTP.

Para que servem GET, POST, PUT/PATCH e DELETE? :: GET busca, POST cria, PUT e PATCH atualizam e DELETE remove dados.

O que significam os códigos 200, 201, 404 e 500? :: 200 sucesso, 201 criado, 404 não encontrado e 500 erro interno do servidor.

Qual a diferença entre 401 e 403? :: 401 é não autenticado; 403 é autenticado mas sem permissão.

O que é uma API? :: Um servidor feito para programas conversarem, devolvendo dados estruturados, geralmente em JSON.

O que é REST? :: Um estilo de organizar APIs em torno de recursos, usando os métodos HTTP de forma consistente, como GET /usuarios/5.

Qual a diferença entre front-end e back-end? :: Front-end roda no navegador (HTML, CSS, JavaScript); back-end roda no servidor, com regras de negócio e banco de dados.

---
Próxima nota: [[11-C-e-Memoria]]
