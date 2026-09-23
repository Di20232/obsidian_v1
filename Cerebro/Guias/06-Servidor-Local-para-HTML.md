---
tags: [guia, html, localhost, web, flashcards]
cssclasses: [cerebro-nota, cerebro-web]
---

# Servidor local para HTML

Abrir um arquivo HTML pelo explorador usa o endereço `file://`. Para testar recursos que dependem de HTTP, como `fetch`, módulos JavaScript e algumas APIs do navegador, use um servidor local.

## Opções simples

| Ferramenta | Como usar | Quando escolher |
|---|---|---|
| VS Code + Live Server | abrir o `index.html` com a extensão | início rápido e visual |
| Python | `python -m http.server 8080` na pasta do projeto | já tem Python e quer evitar extensão |
| Node | um servidor do projeto ou ferramenta de desenvolvimento | o projeto já usa Node e scripts próprios |

Depois, abra o endereço mostrado, normalmente `http://localhost:porta`.

## Cuidados

- pare o servidor quando terminar se ele não for necessário;
- não trate um servidor local como se fosse publicado na internet;
- se uma porta estiver ocupada, escolha outra em vez de encerrar processos desconhecidos;
- o servidor local não substitui testes no ambiente real de publicação.

## Links relacionados

- [[../Mapas/01-Mapa-Web|Mapa Web]]
- [[../../Programacao-Geral/10-Como-a-Web-Funciona|Como a Web Funciona]]

## Perguntas de revisão

Por que usar um servidor local em vez de abrir o HTML direto? :: Porque recursos como fetch e módulos JavaScript não funcionam pelo endereço file://.

Como subir um servidor local com Python? :: Com python -m http.server 8080 na pasta do projeto.

O que fazer se a porta do servidor local estiver ocupada? :: Escolher outra porta em vez de encerrar processos desconhecidos.
