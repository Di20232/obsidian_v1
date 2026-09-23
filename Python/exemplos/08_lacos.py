# for + range
for numero in range(5):
    print(numero)

# for percorrendo uma lista
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break e continue
for numero in range(10):
    if numero == 5:
        break
    print(numero)

for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)

# Exercício resolvido: tabuada
numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Exercício resolvido: soma até digitar 0
soma = 0
while True:
    valor = int(input("Digite um número (0 para parar): "))
    if valor == 0:
        break
    soma += valor
print(f"Soma total: {soma}")
