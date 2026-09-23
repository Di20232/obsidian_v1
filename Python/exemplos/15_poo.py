class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def se_apresentar(self):
        print(f"Oi, eu sou {self.nome} e tenho {self.idade} anos")


pessoa1 = Pessoa("Diego", 25)
pessoa2 = Pessoa("Ana", 30)
pessoa1.se_apresentar()
pessoa2.se_apresentar()


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor


conta = ContaBancaria("Diego")
conta.depositar(100)
conta.sacar(30)
print(conta.saldo)


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico de animal")


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Au au!")


class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")


animais = [Cachorro("Rex"), Gato("Mimi")]
for animal in animais:
    animal.emitir_som()


# Exercício resolvido
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)


produtos = [
    Produto("Caderno", 15.90),
    Produto("Caneta", 3.50),
    Produto("Mochila", 120.00),
]

descontos = [10, 5, 20]
for produto, desconto in zip(produtos, descontos):
    produto.aplicar_desconto(desconto)
    print(f"{produto.nome}: R$ {produto.preco:.2f}")
