---
tags: [php, poo, flashcards]
cssclasses: [cerebro-nota, cerebro-php]
---

# Programação Orientada a Objetos

## Mesmo conceito de [[../Python/15-Programacao-Orientada-a-Objetos]] e [[../JavaScript/15-Classes-e-POO]]

PHP tem suporte completo a classes, e a sintaxe fica no meio do caminho entre Python e JavaScript.

```php
<?php
class Pessoa {
    public $nome;
    public $idade;

    public function __construct($nome, $idade) {
        $this->nome = $nome;
        $this->idade = $idade;
    }

    public function seApresentar() {
        echo "Oi, eu sou {$this->nome} e tenho {$this->idade} anos\n";
    }
}

$pessoa1 = new Pessoa("Diego", 25);
$pessoa2 = new Pessoa("Ana", 30);

$pessoa1->seApresentar();
$pessoa2->seApresentar();

echo $pessoa1->nome . "\n";
```

Comparando com o que você já sabe:

| Python | JavaScript | PHP |
|---|---|---|
| `def __init__(self, ...)` | `constructor(...)` | `public function __construct(...)` |
| `self` | `this` | `$this` |
| `pessoa1 = Pessoa(...)` | `new Pessoa(...)` | `new Pessoa(...)` |
| `pessoa1.nome` | `pessoa1.nome` | `$pessoa1->nome` (seta, não ponto!) |

**Diferença de sintaxe que mais chama atenção**: PHP usa `->` (seta) para acessar propriedades e métodos de um objeto, não `.` como Python e JavaScript. Isso porque `.` já é o operador de concatenação de string em PHP ([[09-Strings]]) — usar `.` também para objetos criaria ambiguidade.

## Visibilidade: `public`, `private`, `protected`

Diferente de Python (que usa só convenção, como `_nome` para sinalizar "privado", sem travar de verdade) e JavaScript (que tem `#nome` para privado de verdade, mas é recente na linguagem), PHP sempre teve controle de visibilidade explícito e obrigatório em cada propriedade/método:

```php
class ContaBancaria {
    private $saldo;   // só acessível de dentro da própria classe
    public $titular;   // acessível de qualquer lugar

    public function __construct($titular, $saldo = 0) {
        $this->titular = $titular;
        $this->saldo = $saldo;
    }

    public function depositar($valor) {
        $this->saldo += $valor;
    }

    public function getSaldo() {   // "getter": forma controlada de ler um dado privado
        return $this->saldo;
    }
}

$conta = new ContaBancaria("Diego");
$conta->depositar(100);
echo $conta->getSaldo() . "\n";   // 100
echo $conta->saldo;                 // ERRO: não é possível acessar propriedade privada
```

**Por que isso importa**: `private` impede que código de fora da classe altere `$saldo` diretamente, forçando que qualquer mudança passe pelos métodos da própria classe (como `depositar`), que podem validar a operação. Isso é chamado de **encapsulamento** — proteger o estado interno de um objeto contra alterações descontroladas de fora.

## Herança: `extends`, igual JavaScript

```php
class Animal {
    protected $nome;   // protected: acessível na própria classe E em subclasses (mas não de fora)

    public function __construct($nome) {
        $this->nome = $nome;
    }

    public function emitirSom() {
        echo "Som genérico de animal\n";
    }
}

class Cachorro extends Animal {
    public function emitirSom() {
        echo "{$this->nome} diz: Au au!\n";
    }
}

class Gato extends Animal {
    public function emitirSom() {
        echo "{$this->nome} diz: Miau!\n";
    }
}

$animais = [new Cachorro("Rex"), new Gato("Mimi")];
foreach ($animais as $animal) {
    $animal->emitirSom();
}
```

Sintaxe quase idêntica a [[../JavaScript/15-Classes-e-POO]] — `extends`, sobrescrita de método, mesma lógica.

## `parent::`, o equivalente ao `super` de JavaScript

```php
class Funcionario extends Pessoa {
    public $cargo;

    public function __construct($nome, $idade, $cargo) {
        parent::__construct($nome, $idade);   // chama o construtor da classe-pai
        $this->cargo = $cargo;
    }

    public function seApresentar() {
        parent::seApresentar();                 // reaproveita o comportamento do pai
        echo "Trabalho como {$this->cargo}\n";
    }
}

$funcionario = new Funcionario("Diego", 25, "Desenvolvedor");
$funcionario->seApresentar();
```

## Interfaces: um contrato que classes prometem cumprir

Conceito que nem Python nem JavaScript têm de forma nativa e explícita: uma **interface** define quais métodos uma classe **deve** ter, sem implementá-los — é um "contrato":

```php
interface Formatavel {
    public function formatar(): string;
}

class Produto implements Formatavel {
    public function __construct(public $nome, public $preco) {}   // sintaxe curta: propriedades direto no construtor

    public function formatar(): string {
        return "{$this->nome}: R$ " . number_format($this->preco, 2, ",", ".");
    }
}

$produto = new Produto("Caderno", 15.90);
echo $produto->formatar() . "\n";
```

`public function __construct(public $nome, public $preco) {}` é um atalho do PHP moderno (8+): declarar `public` diretamente nos parâmetros do construtor já cria e preenche a propriedade automaticamente, sem precisar escrever `$this->nome = $nome;` manualmente.

## Exercício

Crie uma classe `Produto` com `nome` e `preco` (propriedades `private`), um `getPreco()`, e um método `aplicarDesconto($percentual)` que reduz o preço proporcionalmente (mesmo exercício de [[../Python/15-Programacao-Orientada-a-Objetos]] e [[../JavaScript/15-Classes-e-POO]], agora em PHP).

## Perguntas de revisão

Como acessar propriedades e métodos de objeto em PHP? :: Com a seta ->, porque o ponto já é o operador de concatenação.

Qual a diferença entre public, private e protected? :: public é acessível de qualquer lugar, private só dentro da classe e protected na classe e nas subclasses.

O que é encapsulamento? :: Proteger o estado interno do objeto, obrigando que mudanças passem pelos métodos da própria classe.

Qual o equivalente do super de JavaScript em PHP? :: parent::, como parent::__construct(...).

O que é uma interface em PHP? :: Um contrato que define quais métodos uma classe deve ter, sem implementá-los.

O que faz public no parâmetro do construtor em PHP 8? :: Cria e preenche a propriedade automaticamente, sem escrever $this->nome = $nome.

---
Veja o exemplo em `PHP/exemplos/13_poo.php`. Próxima nota: [[14-PHP-com-Banco-de-Dados]]
