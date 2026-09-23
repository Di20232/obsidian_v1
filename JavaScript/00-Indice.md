---
tags: [javascript, indice]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Curso de JavaScript do Zero

Esta trilha segue o mesmo formato do [[../Python/00-Indice|curso de Python]]: cada nota explica um conceito, o **porquê** ele existe, e a **sintaxe correta** com exemplos comentados. Se você já fez a trilha de Python, vai reconhecer a lógica por trás de quase tudo aqui — o que muda principalmente é a sintaxe e alguns conceitos específicos de JavaScript (assincronismo, DOM). Ver a mesma ideia em duas linguagens diferentes é, inclusive, uma das formas mais rápidas de fixar o que é "lógica de programação" e o que é "sintaxe de uma linguagem específica" — ponto já adiantado em [[../Programacao-Geral/06-Paradigmas-e-Panorama-de-Linguagens]].

## Trilha

1. [[01-O-que-e-JavaScript]] — o que é, onde roda, por que existe
2. [[02-Preparando-o-Ambiente]] — instalar o Node.js e preparar o editor
3. [[03-Primeiro-Programa]] — "Olá, mundo" e como o JavaScript é executado
4. [[04-Variaveis-e-Tipos]] — `let`, `const`, `var` e os tipos de dado
5. [[05-Operadores]] — contas, comparações e a pegadinha do `==` vs `===`
6. [[06-Entrada-e-Saida]] — receber dados e mostrar resultados
7. [[07-Condicionais]] — tomar decisões (`if`)
8. [[08-Lacos-de-Repeticao]] — repetir tarefas (`for`, `while`)
9. [[09-Arrays-e-Objetos]] — guardar várias informações juntas
10. [[10-Strings]] — manipular texto de verdade
11. [[11-Funcoes]] — organizar código em blocos reutilizáveis
12. [[12-Modulos-e-NPM]] — dividir código em arquivos e usar pacotes de terceiros
13. [[13-Tratamento-de-Erros]] — lidar com o que dá errado
14. [[14-Assincronismo]] — código que espera algo terminar sem travar tudo
15. [[15-Classes-e-POO]] — modelar problemas com classes e objetos
16. [[16-DOM-e-Eventos]] — fazer uma página web reagir a cliques e ações
17. [[17-Boas-Praticas-e-Proximos-Passos]] — como continuar depois deste curso

## Exemplos executáveis

Cada nota (a partir da 03) tem um arquivo correspondente em `JavaScript/exemplos/`. Rode com o Node.js instalado (nota 02):

```bash
node 03_ola_mundo.js
```

A nota 16 é a exceção — DOM só existe dentro de um navegador, então o exemplo dela é um `.html` para abrir diretamente no navegador.

## Onde isto se conecta com o resto do cofre

- [[../Python/00-Indice]] — a outra linguagem que você já aprendeu; compare a sintaxe lado a lado sempre que possível.
- [[../Programacao-Geral/08-JavaScript-Basico]] — o resumo que já existia sobre JS; esta trilha aprofunda cada ponto daquela nota.
- [[../Programacao-Geral/07-HTML-e-CSS]] e [[../Programacao-Geral/10-Como-a-Web-Funciona]] — contexto necessário para a nota 16 (DOM) fazer sentido.
