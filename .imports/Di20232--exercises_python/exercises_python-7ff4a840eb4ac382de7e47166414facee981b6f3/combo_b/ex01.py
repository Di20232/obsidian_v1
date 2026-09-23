"""Exercicio 01 - variaveis, precedencia de operadores e f-strings.

Variacao B (orientada a objetos): os valores ficam guardados dentro de um
objeto e a impressao acontece linha a linha, dentro de um metodo.
"""


class Demonstracao:
    """Guarda os valores do exercicio e sabe exibi-los na tela."""

    def __init__(self, nome, saudacao, expressao):
        self.nome = nome
        self.saudacao = saudacao
        self.expressao = expressao

    @property
    def resultado(self):
        """A multiplicacao vem antes da soma: 2 + (3 * 4) = 14."""
        return 2 + 3 * 4

    def exibir(self):
        print(self.nome)
        print(self.resultado)
        print(self.saudacao)
        print(self.expressao)
        print(f"{self.expressao} = {self.resultado}")


def main():
    demonstracao = Demonstracao(
        nome="Python",
        saudacao="Olá, Diego!",
        expressao="2 + 3 * 4",
    )
    demonstracao.exibir()


if __name__ == "__main__":
    main()
