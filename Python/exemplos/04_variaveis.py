# Criando variáveis de tipos diferentes
nome = "Diego"
idade = 25
altura = 1.78
esta_estudando = True

print(nome)
print(idade)
print(altura)
print(esta_estudando)

# Verificando o tipo de cada valor
print(type(nome))
print(type(idade))
print(type(altura))
print(type(esta_estudando))

# Convertendo tipos (casting)
idade_texto = str(idade)
print("Tenho " + idade_texto + " anos")

numero_em_texto = "42"
numero = int(numero_em_texto)
print(numero + 8)
