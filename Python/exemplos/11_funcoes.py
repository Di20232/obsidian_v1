def saudacao(nome, saudacao_inicial="Olá"):
    print(f"{saudacao_inicial}, {nome}!")

saudacao("Diego")
saudacao("Diego", "Bom dia")


def somar(a, b):
    return a + b

resultado = somar(3, 4)
print(resultado)


def apresentar(nome, idade, cidade):
    print(f"{nome}, {idade} anos, de {cidade}")

apresentar(nome="Diego", cidade="São Paulo", idade=25)


# Exercício resolvido
def eh_par(numero):
    return numero % 2 == 0

for numero in range(1, 11):
    print(numero, eh_par(numero))
