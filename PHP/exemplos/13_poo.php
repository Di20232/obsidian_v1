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
$pessoa1->seApresentar();

class ContaBancaria {
    private $saldo;
    public $titular;

    public function __construct($titular, $saldo = 0) {
        $this->titular = $titular;
        $this->saldo = $saldo;
    }

    public function depositar($valor) {
        $this->saldo += $valor;
    }

    public function getSaldo() {
        return $this->saldo;
    }
}

$conta = new ContaBancaria("Diego");
$conta->depositar(100);
echo $conta->getSaldo() . "\n";

class Animal {
    protected $nome;

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

class Funcionario extends Pessoa {
    public $cargo;

    public function __construct($nome, $idade, $cargo) {
        parent::__construct($nome, $idade);
        $this->cargo = $cargo;
    }

    public function seApresentar() {
        parent::seApresentar();
        echo "Trabalho como {$this->cargo}\n";
    }
}

$funcionario = new Funcionario("Diego", 25, "Desenvolvedor");
$funcionario->seApresentar();

// Interface + construtor curto
interface Formatavel {
    public function formatar(): string;
}

class ProdutoFormatavel implements Formatavel {
    public function __construct(public $nome, public $preco) {}

    public function formatar(): string {
        return "{$this->nome}: R$ " . number_format($this->preco, 2, ",", ".");
    }
}

$produto = new ProdutoFormatavel("Caderno", 15.90);
echo $produto->formatar() . "\n";

// Exercício resolvido
class Produto {
    private $nome;
    private $preco;

    public function __construct($nome, $preco) {
        $this->nome = $nome;
        $this->preco = $preco;
    }

    public function getPreco() {
        return $this->preco;
    }

    public function aplicarDesconto($percentual) {
        $this->preco -= $this->preco * ($percentual / 100);
    }
}

$p = new Produto("Mochila", 120.00);
$p->aplicarDesconto(20);
echo number_format($p->getPreco(), 2, ",", ".") . "\n";
