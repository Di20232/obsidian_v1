# Operadores aritméticos
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)    # divisão comum -> float
print(10 // 3)   # divisão inteira
print(10 % 3)    # resto da divisão
print(10 ** 2)   # potência

# Operadores de comparação
idade = 20
print(idade == 20)
print(idade != 18)
print(idade >= 18)

# Operadores lógicos
tem_cnh = True
pode_dirigir = idade >= 18 and tem_cnh
print(pode_dirigir)

# Atribuição composta
contador = 0
contador += 1
contador += 1
print(contador)  # 2

# Exercício resolvido: semanas e dias em 100 dias
dias = 100
semanas = dias // 7
dias_restantes = dias % 7
print(f"{semanas} semanas completas e {dias_restantes} dias restantes")
