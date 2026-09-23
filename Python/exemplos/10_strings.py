nome = "Diego"
print(nome[0])
print(nome[-1])
print(nome[0:3])
print(len(nome))

texto = "  Olá, Mundo!  "
texto = texto.strip()
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.replace("Olá", "Oi"))

preco = 19.9
print(f"R$ {preco:.2f}")

frase = "o rato roeu a roupa"
palavras = frase.split()
print(palavras)
print(" ".join(palavras))

# Exercício resolvido: validar e-mail simples
email = input("Digite seu e-mail: ")
if "@" in email and email.endswith(".com"):
    print("e-mail válido")
else:
    print("e-mail inválido")

# Exercício resolvido: contar palavras
frase_usuario = input("Digite uma frase: ")
quantidade_palavras = len(frase_usuario.split())
print(f"A frase tem {quantidade_palavras} palavras")
