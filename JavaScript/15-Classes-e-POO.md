---
tags: [javascript, poo, flashcards]
cssclasses: [cerebro-nota, cerebro-javascript]
---

# Classes e Programação Orientada a Objetos

## Mesmo conceito de [[../Python/15-Programacao-Orientada-a-Objetos]]

Agrupar dados e comportamento em um molde (classe), e criar instâncias (objetos) a partir dele. A sintaxe de JavaScript moderno (desde 2015) é bem próxima da de Python.

```javascript
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

pessoa1.seApresentar();   // "Oi, eu sou Diego e tenho 25 anos"
pessoa2.seApresentar();

console.log(pessoa1.nome); // "Diego"
```

Comparando direto com [[../Python/15-Programacao-Orientada-a-Objetos]]:

| Python | JavaScript |
|---|---|
| `class Pessoa:` | `class Pessoa {` |
| `def __init__(self, nome, idade):` | `constructor(nome, idade) {` |
| `self.nome = nome` | `this.nome = nome` |
| `def se_apresentar(self):` | `seApresentar() {` |
| `pessoa1 = Pessoa("Diego", 25)` | `const pessoa1 = new Pessoa("Diego", 25)` — repare no `new` obrigatório |
| `self` | `this` — mesmo conceito, nome diferente |

**Diferença de sintaxe que chama atenção**: JavaScript exige a palavra-chave `new` ao criar uma instância; Python não usa nada equivalente (`Pessoa(...)` já basta).

## Métodos que alteram o próprio objeto

```javascript
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
console.log(conta.saldo);   // 70
```

## Herança: `extends` no lugar de `(NomeDaClasse)`

```javascript
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
```

Comparando com [[../Python/15-Programacao-Orientada-a-Objetos]]: `class Cachorro(Animal):` em Python vira `class Cachorro extends Animal {` em JavaScript — mesma ideia de herança, palavra-chave diferente (`extends` em vez de simplesmente colocar o nome entre parênteses).

## `super()`: chamando o construtor da classe-pai

Quando uma subclasse precisa de parâmetros extras além dos que a classe-pai já pede:

```javascript
class Funcionario extends Pessoa {
    constructor(nome, idade, cargo) {
        super(nome, idade);   // chama o constructor de Pessoa primeiro
        this.cargo = cargo;
    }

    seApresentar() {
        super.seApresentar();  // reaproveita o comportamento da classe-pai
        console.log(`Trabalho como ${this.cargo}`);
    }
}

const funcionario = new Funcionario("Diego", 25, "Desenvolvedor");
funcionario.seApresentar();
```

`super(...)` chama o `constructor` da classe-pai; `super.metodo()` chama um método específico da classe-pai. Isso não tem exigência sintática direta equivalente em Python (que resolve isso de forma um pouco diferente, com `super().__init__(...)`), mas o **conceito** — reaproveitar o comportamento do "pai" antes de adicionar o que é específico do "filho" — é o mesmo.

## Objetos sem classe: uma diferença real em relação a Python

Em Python, para agrupar dados você quase sempre usa dicionário **ou** classe, dependendo se precisa de comportamento junto. Em JavaScript, é comum usar **objetos literais** (vistos em [[09-Arrays-e-Objetos]]) até para coisas que, em outra linguagem, você criaria uma classe pequena para representar — classes só entram quando o "molde" vai ser reaproveitado várias vezes com comportamento próprio.

## Exercício

Crie uma classe `Produto` com `nome` e `preco`, e um método `aplicarDesconto(percentual)` que reduz `this.preco` proporcionalmente (mesmo exercício de [[../Python/15-Programacao-Orientada-a-Objetos]], agora em JS). Crie 3 produtos, aplique descontos diferentes, e exiba o preço final de cada um.

## Perguntas de revisão

Qual o equivalente de __init__ e self em JavaScript? :: constructor e this.

O que JavaScript exige ao criar uma instância e Python não? :: A palavra new, como new Pessoa("Diego", 25).

Como declarar herança em JavaScript? :: Com extends, como class Cachorro extends Animal.

Para que serve super() numa classe JavaScript? :: super(...) chama o construtor da classe-pai e super.metodo() chama um método dela.

Quando JavaScript prefere objeto literal em vez de classe? :: Quando só se agrupam dados; a classe entra quando o molde se repete com comportamento próprio.

---
Veja o exemplo em `JavaScript/exemplos/15_classes.js`. Próxima nota: [[16-DOM-e-Eventos]]
