"""Exercicio 05 - sistema escolar com estruturas de selecao.

Variacao A (orientada a dados): os limites de nota, as situacoes do aluno e
os menus ficam em tabelas; uma unica funcao generica sabe rodar qualquer
menu a partir dessas tabelas.
"""

LARGURA = 50

# (nota minima, rotulo) - vence o primeiro limite alcancado.
CLASSIFICACOES = (
    (9.0, "EXCELENTE"),
    (7.0, "BOM"),
    (5.0, "REGULAR"),
    (3.0, "RUIM"),
)
CLASSIFICACAO_PADRAO = "PESSIMO"

# (condicao, modelo do texto) - vence a primeira condicao verdadeira.
SITUACOES = (
    (lambda nota, faltas: nota >= 9.0, "ALUNO DESTAQUE - Nota {nota}"),
    (lambda nota, faltas: nota >= 7.0 and faltas <= 10, "APROVADO - Nota {nota}, Faltas {faltas}"),
    (lambda nota, faltas: nota >= 5.0 and faltas <= 10, "EM RECUPERACAO - Nota {nota}, Faltas {faltas}"),
    (lambda nota, faltas: True, "REPROVADO - Nota {nota}, Faltas {faltas}"),
)

OPCOES_PROCESSADOR = {
    "1": "OPCAO 1: Listar alunos",
    "2": "OPCAO 2: Cadastrar aluno",
    "3": "OPCAO 3: Calcular media",
    "4": "OPCAO 4: Sair do sistema",
    "sair": "OPCAO 4: Sair do sistema",
}


# ---------------------------------------------------------------- entradas


def ler_float(mensagem, minimo=0, maximo=10):
    """Insiste ate receber um numero real dentro do intervalo."""
    while True:
        try:
            valor = float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            continue

        if minimo <= valor <= maximo:
            return valor

        print(f"Valor fora do intervalo permitido ({minimo} a {maximo}).")


def ler_inteiro(mensagem, minimo=0):
    """Insiste ate receber um inteiro maior ou igual ao minimo."""
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue

        if valor >= minimo:
            return valor

        print(f"Digite um valor maior ou igual a {minimo}.")


# ------------------------------------------------------------------ regras


def classificar(nota):
    """Traduz a nota em um rotulo, consultando a tabela CLASSIFICACOES."""
    for limite, rotulo in CLASSIFICACOES:
        if nota >= limite:
            return rotulo
    return CLASSIFICACAO_PADRAO


def situacao_do_aluno(nome, nota, faltas):
    """Monta a linha de situacao consultando a tabela SITUACOES."""
    for condicao, modelo in SITUACOES:
        if condicao(nota, faltas):
            return f"{nome}: " + modelo.format(nota=nota, faltas=faltas)

    raise AssertionError("a tabela SITUACOES precisa terminar com uma condicao sempre verdadeira")


def resultado_aprovacao(nota, frequencia):
    """Texto do resultado combinando nota e frequencia."""
    if frequencia >= 75 and nota >= 7.0:
        return "RESULTADO: APROVADO - Nota e frequencia suficientes"
    if frequencia >= 75:
        return f"RESULTADO: REPROVADO - Frequencia OK, mas nota {nota} abaixo de 7.0"
    return f"RESULTADO: REPROVADO - Frequencia {frequencia}% abaixo de 75%"


# ------------------------------------------------------------------- acoes


def verificar_aprovacao():
    print("\n=== VERIFICACAO DE APROVACAO ===")

    nota = ler_float("Digite a nota do aluno (0 a 10): ", 0, 10)
    frequencia = ler_float("Digite a frequencia do aluno (0 a 100): ", 0, 100)

    print(f"Nota: {nota} - Frequencia: {frequencia}%")
    print(resultado_aprovacao(nota, frequencia))


def classificar_nota():
    print("\n=== CLASSIFICACAO DE NOTA ===")

    nota = ler_float("Digite a nota para classificar (0 a 10): ", 0, 10)

    print(f"Nota: {nota}")
    print(f"CLASSIFICACAO: {classificar(nota)}")


def processar_menu():
    print("\n=== PROCESSADOR DE MENU ===")
    print("1 - Listar alunos")
    print("2 - Cadastrar aluno")
    print("3 - Calcular media")
    print("4 - Sair do sistema")

    opcao = input("Digite a opcao desejada: ")

    print(OPCOES_PROCESSADOR.get(opcao, f"OPCAO INVALIDA: {opcao}"))


def avaliar_aluno():
    print("\n=== AVALIACAO DO ALUNO ===")

    nome = input("Digite o nome do aluno: ")
    nota = ler_float("Digite a nota do aluno (0 a 10): ", 0, 10)
    faltas = ler_inteiro("Digite o numero de faltas: ", 0)

    print(f"Aluno: {nome} - Nota: {nota} - Faltas: {faltas}")
    print(situacao_do_aluno(nome, nota, faltas))


def repetir(acao, pergunta):
    """Roda a acao em laco enquanto o usuario responder 's'."""
    while True:
        acao()
        if input(pergunta).strip().lower() != "s":
            break


def verificar_multiplos_alunos():
    print("\n=== VERIFICAR MULTIPLOS ALUNOS ===")
    repetir(verificar_aprovacao, "\nVerificar outro aluno? (s/n): ")


def classificar_multiplas_notas():
    print("\n=== CLASSIFICAR MULTIPLAS NOTAS ===")
    repetir(classificar_nota, "\nClassificar outra nota? (s/n): ")


def processar_lista_alunos():
    print("\n=== PROCESSAR LISTA DE ALUNOS ===")

    alunos = []
    while True:
        nome = input("Nome do aluno: ")
        nota = ler_float("Nota (0 a 10): ", 0, 10)
        faltas = ler_inteiro("Faltas: ", 0)

        alunos.append({"nome": nome, "nota": nota, "faltas": faltas})

        if input("Adicionar outro aluno? (s/n): ").strip().lower() != "s":
            break

    if alunos:
        print("\n" + "-" * 30)
        print("RESULTADOS:")
        print("-" * 30)

        for aluno in alunos:
            print(situacao_do_aluno(aluno["nome"], aluno["nota"], aluno["faltas"]))


# ------------------------------------------------------------------- menus


def executar_menu(cabecalho, subtitulo, opcoes, prompt, saidas_extras=()):
    """Roda um menu descrito por dados.

    opcoes: dicionario {tecla: (rotulo, funcao)}; funcao None encerra o menu.
    """
    for linha in cabecalho:
        print(linha)

    while True:
        print("\n" + "-" * LARGURA)
        print(subtitulo)
        print("-" * LARGURA)
        for tecla, (rotulo, _) in opcoes.items():
            print(f"{tecla} - {rotulo}")

        escolha = input(prompt)
        item = opcoes.get(escolha)

        if escolha in saidas_extras or (item is not None and item[1] is None):
            print("\nSaindo do sistema...")
            return

        if item is None:
            print("\nOPCAO INVALIDA! Tente novamente.")
        else:
            item[1]()

        input("\nPressione Enter para continuar...")


def main():
    executar_menu(
        cabecalho=(
            "=" * LARGURA,
            "SISTEMA ESCOLAR SIMPLES",
            "Demonstracao de estruturas de selecao",
            "=" * LARGURA,
        ),
        subtitulo="MENU PRINCIPAL",
        opcoes={
            "1": ("Verificar Aprovacao", verificar_aprovacao),
            "2": ("Classificar Nota", classificar_nota),
            "3": ("Processar Menu", processar_menu),
            "4": ("Avaliar Aluno", avaliar_aluno),
            "5": ("Sair", None),
        },
        prompt="\nEscolha uma opcao (1-5): ",
    )


def menu_avancado():
    executar_menu(
        cabecalho=(
            "=" * LARGURA,
            "SISTEMA ESCOLAR - MENU AVANCADO",
            "=" * LARGURA,
        ),
        subtitulo="OPCOES:",
        opcoes={
            "1": ("Verificar Aprovacao", verificar_aprovacao),
            "2": ("Classificar Nota", classificar_nota),
            "3": ("Processar Menu", processar_menu),
            "4": ("Avaliar Aluno", avaliar_aluno),
            "5": ("Verificar Multiplos Alunos", verificar_multiplos_alunos),
            "6": ("Classificar Multiplas Notas", classificar_multiplas_notas),
            "7": ("Processar Lista de Alunos", processar_lista_alunos),
            "8": ("Sair", None),
        },
        prompt="\nEscolha uma opcao: ",
        saidas_extras=("sair",),
    )


def testar_rapido():
    testes = {
        "1": ("Testar Aprovacao", verificar_aprovacao),
        "2": ("Testar Classificacao", classificar_nota),
        "3": ("Testar Match Case", processar_menu),
        "4": ("Testar Guarda", avaliar_aluno),
    }

    print("\n=== TESTE RAPIDO ===")
    for tecla, (rotulo, _) in testes.items():
        print(f"{tecla} - {rotulo}")

    escolha = input("Escolha um teste (1-4): ")
    teste = testes.get(escolha)

    if teste is None:
        print("Opcao invalida!")
    else:
        teste[1]()


def escolher_versao():
    versoes = {
        "1": ("Menu Interativo", main),
        "2": ("Menu Avancado", menu_avancado),
        "3": ("Teste Rapido", testar_rapido),
        "4": ("Sair", None),
    }

    print("=" * LARGURA)
    print("SISTEMA ESCOLAR - VERSOES DISPONIVEIS")
    print("=" * LARGURA)
    for tecla, (rotulo, _) in versoes.items():
        print(f"{tecla} - {rotulo}")

    escolha = input("\nEscolha uma versao (1-4): ")
    versao = versoes.get(escolha)

    if versao is None:
        print("Opcao invalida!")
    elif versao[1] is None:
        print("Saindo...")
    else:
        versao[1]()


if __name__ == "__main__":
    escolher_versao()
