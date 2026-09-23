# Escrevendo tarefas em um arquivo
tarefas = []
for i in range(3):
    tarefa = input(f"Digite a tarefa {i + 1}: ")
    tarefas.append(tarefa)

with open("tarefas.txt", "w") as arquivo:
    for tarefa in tarefas:
        arquivo.write(tarefa + "\n")

# Lendo e exibindo as tarefas numeradas
with open("tarefas.txt", "r") as arquivo:
    for numero, linha in enumerate(arquivo, start=1):
        print(f"{numero}. {linha.strip()}")

# Adicionando uma tarefa extra sem apagar as anteriores
with open("tarefas.txt", "a") as arquivo:
    arquivo.write("Revisar anotações de Python\n")

# Lidando com arquivo inexistente
try:
    with open("nao_existe.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Esse arquivo não existe.")
