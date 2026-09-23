nome = input("Digite seu nome: ")
idade_texto = input("Digite sua idade: ")
idade = int(idade_texto)  # input() sempre devolve str; convertemos para int

ano_atual = int(input("Digite o ano atual: "))
ano_dos_100 = ano_atual + (100 - idade)

print(f"Olá, {nome}!")
print(f"Você tem {idade} anos.")
print(f"Você completa 100 anos em {ano_dos_100}.")
