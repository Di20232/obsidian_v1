---
tags: [php, boas-praticas, flashcards]
cssclasses: [cerebro-nota, cerebro-php]
---

# Boas Práticas e Próximos Passos

## Você terminou o essencial de PHP

Com Python, JavaScript e agora PHP, você já viu a mesma lógica de programação através de três sintaxes e três contextos de execução diferentes (script geral, navegador, servidor web) — isso é uma base muito mais sólida do que "saber uma linguagem", é entender o que é universal e o que é específico de cada ferramenta (ver [[../Programacao-Geral/06-Paradigmas-e-Panorama-de-Linguagens]]).

## PSR: o "PEP 8" do PHP

Assim como Python tem a PEP 8 ([[../Python/16-Boas-Praticas-e-Proximos-Passos]]), a comunidade PHP tem os **PSRs** (PHP Standard Recommendations), mantidos pela PHP-FIG. Os mais relevantes no dia a dia:
- **PSR-1/PSR-12**: estilo de código — indentação, nomes, chaves.
- **PSR-4**: como organizar arquivos e namespaces para autoload automático (abaixo).

## Ferramentas de estilo automático

```bash
composer require --dev friendsofphp/php-cs-fixer
```

Equivalente ao `black`/`ruff` de Python ([[../Python/16-Boas-Praticas-e-Proximos-Passos]]) e ao Prettier/ESLint de JavaScript ([[../JavaScript/17-Boas-Praticas-e-Proximos-Passos]]).

## Composer: o `pip`/`npm` do PHP

```bash
composer init                 # cria o composer.json, descrevendo o projeto
composer require monolog/monolog   # instala um pacote de terceiros
```

Mesmo papel do `pip` ([[../Python/12-Modulos-e-Pacotes]]) e do `npm` ([[../JavaScript/12-Modulos-e-NPM]]): gerencia dependências, criando uma pasta `vendor/` (equivalente a `node_modules/`) que **nunca** deve ir para o Git ([[../Programacao-Geral/03-Git-e-Controle-de-Versao]]):

```
# .gitignore
vendor/
```

## Namespaces: organizando classes em projetos maiores

```php
namespace App\Modelos;

class Usuario {
    // ...
}
```

```php
use App\Modelos\Usuario;

$usuario = new Usuario();
```

Cumpre papel parecido com módulos de Python ([[../Python/12-Modulos-e-Pacotes]]) e `import`/`export` de JavaScript ([[../JavaScript/12-Modulos-e-NPM]]): evita conflito de nomes entre classes de partes diferentes de um projeto grande (ou entre seu código e o de uma biblioteca de terceiros).

## Frameworks: o próximo passo natural

PHP puro (o que você aprendeu aqui) é suficiente para scripts e sites pequenos. Projetos maiores quase sempre usam um **framework**, que já resolve roteamento de URLs, conexão a banco, templates de página, e segurança, de forma padronizada:
- **Laravel**: o mais popular atualmente, com muitos recursos prontos.
- **Symfony**: mais modular, usado como base de outros frameworks (inclusive parte do próprio Laravel).

## Segurança: pontos que valem menção extra em PHP

Retomando [[../Programacao-Geral/13-Boas-Praticas-de-Codigo]], com foco no que é mais específico de aplicações PHP:
- **SQL injection**: sempre prepared statements com PDO, nunca concatenação (já visto em [[14-PHP-com-Banco-de-Dados]]).
- **XSS** (injeção de código malicioso em HTML gerado a partir de dados do usuário): use `htmlspecialchars($dado)` sempre que exibir dado vindo de `$_GET`/`$_POST`/banco dentro de HTML.
- **Senhas**: nunca guarde senha em texto puro — use `password_hash()` ao salvar e `password_verify()` ao checar login.

## Testando seu código

```php
function somar($a, $b) {
    return $a + $b;
}

assert(somar(2, 3) === 5);
assert(somar(-1, 1) === 0);
echo "Testes passaram!\n";
```

Mesmo `assert` simples visto em [[../Python/16-Boas-Praticas-e-Proximos-Passos]]. Para projetos reais, a ferramenta padrão é **PHPUnit** (`composer require --dev phpunit/phpunit`), com sintaxe orientada a objetos parecida com a organização de testes vista em [[../Programacao-Geral/12-Debugging-e-Testes]].

## Para onde ir a partir daqui

- **Pratique com um projeto completo**: um sistema de cadastro simples (formulário → PDO → listagem), juntando [[11-Formularios-e-Superglobais]] e [[14-PHP-com-Banco-de-Dados]].
- **Aprofunde o banco de dados**: [[../MySQL/00-Indice]] para o banco mais usado junto com PHP em produção, ou [[../SQLite/00-Indice]] para continuar sem precisar de servidor.
- **Explore um framework** (Laravel é o ponto de partida mais comum) depois de estar confortável com PHP puro.
- Volte para [[../Programacao-Geral/00-Indice]] para reforçar Git, testes e boas práticas gerais, aplicando-as a projetos PHP.

## Perguntas de revisão

O que são os PSRs? :: As recomendações de padrão da comunidade PHP, como PSR-12 para estilo e PSR-4 para autoload.

Qual o gerenciador de pacotes do PHP? :: O Composer, que instala dependências na pasta vendor/.

Como proteger contra XSS em PHP? :: Usando htmlspecialchars ao exibir dados do usuário ou do banco dentro de HTML.

Como guardar senhas em PHP? :: Com password_hash ao salvar e password_verify ao checar o login, nunca em texto puro.

Quais são os frameworks PHP mais usados? :: Laravel e Symfony.

Qual a ferramenta padrão de testes em PHP? :: O PHPUnit.

---
Fim da trilha de PHP. Volte ao [[00-Indice|índice deste curso]], ao [[../Python/00-Indice|curso de Python]], ao [[../JavaScript/00-Indice|curso de JavaScript]] ou ao [[../Programacao-Geral/00-Indice|conhecimento geral de programação]] a qualquer momento.
