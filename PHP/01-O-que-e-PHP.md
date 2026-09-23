---
tags: [php, conceitos]
cssclasses: [cerebro-nota, cerebro-php]
---

# O que é PHP

## Uma linguagem feita para gerar páginas web no servidor

Lembre do modelo cliente-servidor visto em [[../Programacao-Geral/10-Como-a-Web-Funciona]]: o navegador (cliente) pede uma página, um servidor responde. JavaScript ([[../JavaScript/01-O-que-e-JavaScript]]) roda **no navegador**, depois que a página já chegou. PHP roda **no servidor**, **antes** de a página ser enviada — ele monta o HTML dinamicamente (por exemplo, buscando dados de um banco, ver [[14-PHP-com-Banco-de-Dados]]) e só então entrega o resultado final ao navegador, que nunca vê o código PHP em si, só o HTML pronto.

```
Navegador pede a página
        ↓
Servidor roda o código PHP
        ↓
PHP gera HTML (às vezes buscando dados em um banco)
        ↓
Servidor devolve o HTML pronto ao navegador
```

## Por que PHP continua relevante

PHP nasceu em 1995 e alimenta uma fatia enorme da web até hoje — WordPress (o sistema por trás de uma parcela gigante de sites do mundo), Wikipedia e Facebook (nas origens) foram construídos com ele. É frequentemente a porta de entrada mais direta para "back-end web" por ser simples de colocar no ar e ter suporte quase universal em provedores de hospedagem baratos.

## Misturando PHP com HTML: a característica mais marcante da linguagem

Diferente de Python ou JavaScript, que geram texto/HTML através de comandos (`print`, `console.log`, manipulação do DOM), PHP foi desenhado para ser **embutido diretamente dentro de HTML**:

```php
<!DOCTYPE html>
<html>
<body>
    <h1>Bem-vindo!</h1>
    <p>Hoje é <?php echo date("d/m/Y"); ?></p>
</body>
</html>
```

Tudo entre `<?php` e `?>` é código PHP, executado no servidor; tudo fora disso é HTML comum, enviado como está. O servidor processa o arquivo inteiro e substitui os blocos `<?php ?>` pelo resultado antes de mandar a página para o navegador — o visitante nunca vê `<?php echo date(...) ?>`, só vê a data já calculada no HTML final.

## Comparando com o que você já sabe

| Conceito | Python | JavaScript | PHP |
|---|---|---|---|
| Onde roda | em qualquer lugar (script, servidor) | navegador ou Node.js | servidor, gerando HTML |
| Exibir algo | `print(...)` | `console.log(...)` | `echo ...;` |
| Fim de instrução | quebra de linha | `;` (opcional) | `;` (obrigatório) |
| Comentário | `# comentário` | `// comentário` | `// comentário` ou `# comentário` |
| Variável | `nome` | `nome` | `$nome` (sempre com `$`) |

## Interpretado, como Python e JavaScript

Mesmo conceito de [[../Python/01-O-que-e-Programacao]]: não existe uma etapa de compilação manual — o servidor executa o arquivo `.php` diretamente através de um interpretador, a cada requisição.

## Vocabulário específico de PHP

- **Tag PHP**: `<?php` e `?>`, delimitam onde o código PHP começa e termina dentro de um arquivo.
- **`echo`**: a forma mais comum de gerar saída (texto/HTML) a partir do PHP.
- **Servidor web**: o programa que recebe as requisições HTTP e aciona o interpretador PHP para gerar a resposta — Apache e Nginx são os mais comuns em produção; para aprender, o próprio PHP tem um servidor embutido simples (visto em [[02-Preparando-o-Ambiente]]).
- **Superglobais**: variáveis especiais (`$_GET`, `$_POST`, `$_SESSION`) sempre disponíveis, que carregam dados vindos da requisição — aprofundado em [[11-Formularios-e-Superglobais]].

## Exercício

Sem escrever código ainda: pense em uma página que você usa e que claramente busca dados diferentes a cada visita (um feed de notícias, um painel de pedidos, o preço atualizado de um produto). Essa é exatamente a categoria de problema que PHP (ou qualquer linguagem de back-end equivalente) resolve — gerar HTML diferente, sob demanda, com base em dados que mudam.

---
Próxima nota: [[02-Preparando-o-Ambiente]]
