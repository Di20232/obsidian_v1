numero = int(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("É zero")

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# Condição composta (equivalente a if aninhado, mas mais legível)
idade = 20
tem_ingresso = True
if idade >= 18 and tem_ingresso:
    print("Entrada liberada")
else:
    print("Entrada negada")
