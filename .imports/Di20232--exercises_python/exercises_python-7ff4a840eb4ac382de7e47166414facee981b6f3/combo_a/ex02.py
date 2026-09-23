"""Exercicio 02 - carrinho de compras com valores fixos.

Variacao A (orientada a dados): os textos e os numeros ficam num unico
dicionario e a saida sai de um template preenchido com format_map.
"""

COMPRA = {
    "titulo": "Cálculo no carrinho de compras",
    "descricao": "Um cliente comprou dois livros, cada um por: ",
    "conectivo": " e recebeu um desconto de: ",
    "pergunta": "Quanto ele gastou?",
    "resposta": "Ele gastou: ",
    "preco_unitario": 35.00,
    "quantidade": 2,
    "desconto": 10.00,
}

TEMPLATE = (
    "{titulo}\n"
    "{descricao}R$ {preco_unitario:.2f}{conectivo}R$ {desconto:.2f}\n"
    "{pergunta}\n"
    "{resposta}R$ {valor_final:.2f}"
)


def calcular_valor_final(dados):
    """Subtotal (preco x quantidade) menos o desconto em reais."""
    subtotal = dados["preco_unitario"] * dados["quantidade"]
    return subtotal - dados["desconto"]


def main():
    dados = dict(COMPRA, valor_final=calcular_valor_final(COMPRA))
    print(TEMPLATE.format_map(dados))


if __name__ == "__main__":
    main()
