class Pessoa {
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }

    seApresentar() {
        console.log(`Oi, eu sou ${this.nome} e tenho ${this.idade} anos`);
    }
}

const pessoa1 = new Pessoa("Diego", 25);
const pessoa2 = new Pessoa("Ana", 30);
pessoa1.seApresentar();
pessoa2.seApresentar();

class ContaBancaria {
    constructor(titular, saldo = 0) {
        this.titular = titular;
        this.saldo = saldo;
    }

    depositar(valor) {
        this.saldo += valor;
    }

    sacar(valor) {
        if (valor > this.saldo) {
            console.log("Saldo insuficiente");
        } else {
            this.saldo -= valor;
        }
    }
}

const conta = new ContaBancaria("Diego");
conta.depositar(100);
conta.sacar(30);
console.log(conta.saldo);

class Animal {
    constructor(nome) {
        this.nome = nome;
    }

    emitirSom() {
        console.log("Som genérico de animal");
    }
}

class Cachorro extends Animal {
    emitirSom() {
        console.log(`${this.nome} diz: Au au!`);
    }
}

class Gato extends Animal {
    emitirSom() {
        console.log(`${this.nome} diz: Miau!`);
    }
}

const animais = [new Cachorro("Rex"), new Gato("Mimi")];
for (const animal of animais) {
    animal.emitirSom();
}

class Funcionario extends Pessoa {
    constructor(nome, idade, cargo) {
        super(nome, idade);
        this.cargo = cargo;
    }

    seApresentar() {
        super.seApresentar();
        console.log(`Trabalho como ${this.cargo}`);
    }
}

const funcionario = new Funcionario("Diego", 25, "Desenvolvedor");
funcionario.seApresentar();

// Exercício resolvido
class Produto {
    constructor(nome, preco) {
        this.nome = nome;
        this.preco = preco;
    }

    aplicarDesconto(percentual) {
        this.preco -= this.preco * (percentual / 100);
    }
}

const produtos = [
    new Produto("Caderno", 15.9),
    new Produto("Caneta", 3.5),
    new Produto("Mochila", 120.0),
];
const descontos = [10, 5, 20];

produtos.forEach((produto, i) => {
    produto.aplicarDesconto(descontos[i]);
    console.log(`${produto.nome}: R$ ${produto.preco.toFixed(2)}`);
});
