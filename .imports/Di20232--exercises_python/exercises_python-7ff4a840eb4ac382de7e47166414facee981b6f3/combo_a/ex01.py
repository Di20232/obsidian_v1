"""Exercicio 01 - variaveis, precedencia de operadores e f-strings.

Variacao A (orientada a dados): cada linha da saida vira um item de uma
tupla e a impressao acontece de uma vez so, unindo os itens com quebras
de linha.
"""

NOME = "Python"
SAUDACAO = "Olá, Diego!"
EXPRESSAO = "2 + 3 * 4"


def montar_linhas():
    """Devolve, na ordem certa, as linhas que o programa deve imprimir."""
    # A multiplicacao tem precedencia sobre a soma: 2 + (3 * 4) = 14.
    resultado = 2 + 3 * 4

    return (
        NOME,
        str(resultado),
        SAUDACAO,
        EXPRESSAO,
        f"{EXPRESSAO} = {resultado}",
    )


def main():
    print("\n".join(montar_linhas()))


if __name__ == "__main__":
    main()
