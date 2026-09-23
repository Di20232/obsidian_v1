"""Exercicio 03 - sistema de compras com recibo.

Variacao A (orientada a dados): o calculo devolve um dicionario e o recibo
e montado como uma lista de linhas ja formatadas, impressa em seguida.
"""

LARGURA = 50


def formatar_real(valor):
    """Formata no padrao brasileiro: 1234.5 -> '1.234,50'."""
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_compra(preco, quantidade, percentual_desconto):
    """Devolve subtotal, desconto, total e valor medio por unidade."""
    subtotal = preco * quantidade
    valor_desconto = subtotal * (percentual_desconto / 100)
    total_final = subtotal - valor_desconto
    valor_medio = total_final / quantidade if quantidade else 0

    return {
        "subtotal": subtotal,
        "valor_desconto": valor_desconto,
        "total_final": total_final,
        "valor_medio": valor_medio,
    }


def montar_recibo(nome_cliente, produto, preco, quantidade, percentual_desconto, dados):
    """Devolve a lista de linhas do recibo, na ordem de impressao."""
    return [
        "",
        "=" * LARGURA,
        "         RECIBO DA COMPRA",
        "=" * LARGURA,
        f"Cliente:          {nome_cliente}",
        f"Produto:          {produto}",
        f"Quantidade:       {quantidade} unidade(s)",
        f"Preco unitario:   R$ {formatar_real(preco)}",
        "-" * LARGURA,
        f"Subtotal:         R$ {formatar_real(dados['subtotal'])}",
        f"Desconto:         {percentual_desconto:.0f}%"
        f" (R$ {formatar_real(dados['valor_desconto'])})",
        "-" * LARGURA,
        f"TOTAL A PAGAR:    R$ {formatar_real(dados['total_final'])}",
        "",
        f"Valor medio por unidade: R$ {formatar_real(dados['valor_medio'])}",
        "",
        "=" * LARGURA,
        "          OBRIGADO PELA COMPRA!",
        "=" * LARGURA,
    ]


def main():
    print("=" * LARGURA)
    print("         SISTEMA DE COMPRAS")
    print("=" * LARGURA)

    nome_cliente = input("Nome do cliente: ")
    produto = input("Nome do produto: ")
    preco = float(input("Preco unitario (R$): "))
    quantidade = int(input("Quantidade: "))
    percentual_desconto = float(input("Percentual de desconto (%): "))

    dados = calcular_compra(preco, quantidade, percentual_desconto)
    linhas = montar_recibo(
        nome_cliente, produto, preco, quantidade, percentual_desconto, dados
    )

    for linha in linhas:
        print(linha)

    print("Processando dados", end="... ")
    print("Finalizado!", end="\n\n")


if __name__ == "__main__":
    main()
