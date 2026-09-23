---
tags: [php, indice]
cssclasses: [cerebro-nota, cerebro-php]
---

# Curso de PHP do Zero

Mesmo formato do [[../Python/00-Indice|curso de Python]] e do [[../JavaScript/00-Indice|curso de JavaScript]]: cada nota explica o **porquê** do conceito e a **sintaxe correta**, com exemplos comentados. PHP é a terceira linguagem desta sequência — se você já fez as outras duas, vai reconhecer quase toda a lógica, só a sintaxe muda de novo (ver o panorama comparativo em [[../Programacao-Geral/06-Paradigmas-e-Panorama-de-Linguagens]]).

> **Nota sobre os exemplos**: diferente das trilhas de Python e JavaScript, este ambiente não tem o PHP instalado para testar ao vivo — os exemplos foram escritos com cuidado extra na sintaxe, mas rode-os você mesmo depois de instalar (nota 02) para confirmar.

## Por que aprender PHP depois de Python e JavaScript

Você já sabe como o **navegador** processa JavaScript ([[../JavaScript/16-DOM-e-Eventos]]) e como um **servidor genérico** funciona ([[../Programacao-Geral/10-Como-a-Web-Funciona]]). PHP é uma linguagem **desenhada especificamente para rodar no servidor**, gerando páginas web dinamicamente — é a peça que faltava para fechar o ciclo completo de "como um site de verdade funciona", da requisição do navegador até a resposta montada com dados de um banco.

## Trilha

1. [[01-O-que-e-PHP]] — o que é, onde roda, por que ainda é tão usado
2. [[02-Preparando-o-Ambiente]] — instalar PHP e um servidor local
3. [[03-Primeiro-Programa]] — misturando PHP com HTML pela primeira vez
4. [[04-Variaveis-e-Tipos]] — `$variavel` e os tipos de dado
5. [[05-Operadores]] — contas, comparações e a diferença entre `==` e `===`
6. [[06-Condicionais]] — tomar decisões (`if`)
7. [[07-Lacos-de-Repeticao]] — repetir tarefas (`for`, `while`, `foreach`)
8. [[08-Arrays]] — listas e dicionários, no mesmo tipo
9. [[09-Strings]] — manipular texto de verdade
10. [[10-Funcoes]] — organizar código em blocos reutilizáveis
11. [[11-Formularios-e-Superglobais]] — receber dados do navegador (`$_GET`, `$_POST`)
12. [[12-Tratamento-de-Erros]] — lidar com o que dá errado
13. [[13-POO]] — modelar problemas com classes e objetos
14. [[14-PHP-com-Banco-de-Dados]] — conectar PHP a MySQL/SQLite com PDO
15. [[15-Boas-Praticas-e-Proximos-Passos]] — como continuar depois deste curso

## Onde isto se conecta

- [[../Python/00-Indice]] e [[../JavaScript/00-Indice]] — as outras duas linguagens desta sequência; compare a sintaxe sempre que possível.
- [[../MySQL/00-Indice]] — o banco de dados mais comum usado junto com PHP, aprofundado em sua própria trilha.
- [[../Programacao-Geral/10-Como-a-Web-Funciona]] — contexto de HTTP/cliente-servidor necessário para entender por que PHP existe.
