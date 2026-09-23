# Listas
frutas = ["maçã", "banana", "uva"]
print(frutas[0])
print(frutas[-1])
frutas.append("pera")
frutas.remove("banana")
print(frutas)

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# Tuplas
coordenada = (10, 20)
print(coordenada[0])

# Dicionários
pessoa = {
    "nome": "Diego",
    "idade": 25,
    "cidade": "São Paulo",
}
print(pessoa["nome"])
pessoa["idade"] = 26
pessoa["profissao"] = "Dev"

for chave, valor in pessoa.items():
    print(chave, "->", valor)

# Exercício resolvido: lista de dicionários
produtos = [
    {"nome": "Caderno", "preco": 15.90},
    {"nome": "Caneta", "preco": 3.50},
    {"nome": "Mochila", "preco": 120.00},
]

total = 0
for produto in produtos:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")
    total += produto["preco"]

print(f"Total: R$ {total:.2f}")
