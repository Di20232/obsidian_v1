try:
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    resultado = numero_1 / numero_2
except ValueError:
    print("Digite apenas números.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Fim do programa.")

# Padrão: repetir até o usuário digitar algo válido
while True:
    try:
        idade = int(input("Sua idade: "))
        break
    except ValueError:
        print("Digite um número válido.")

print(f"Idade registrada: {idade}")
