---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-python]
source: https://github.com/Di20232/exercises_python/blob/7ff4a840eb4ac382de7e47166414facee981b6f3/comparar_saidas.py
source_commit: 7ff4a840eb4ac382de7e47166414facee981b6f3
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# comparar_saidas.py

Origem: [Di20232/exercises_python](https://github.com/Di20232/exercises_python/blob/7ff4a840eb4ac382de7e47166414facee981b6f3/comparar_saidas.py). Versao consultada: 7ff4a840eb4a.

[[Cerebro/GitHub/exercises_python/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--exercises_python--7ff4a840eb4a.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```python
"""Roda os dois combos com as mesmas entradas e compara as saidas.

As duas variacoes de cada exercicio sao escritas de formas diferentes, mas
devem imprimir exatamente a mesma coisa. Este script alimenta os dois
programas com o mesmo texto no teclado e mostra a diferenca, se houver.

Uso:
    python comparar_saidas.py

Termina com codigo 0 quando tudo bate e 1 quando alguma saida diverge.
"""

import difflib
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
COMBOS = ("combo_a", "combo_b")

# {exercicio: [(descricao do caso, o que sera digitado)]}
CASOS = {
    "ex01": [
        ("sem entrada", ""),
    ],
    "ex02": [
        ("sem entrada", ""),
    ],
    "ex03": [
        ("compra com desconto", "Maria\nCaderno\n35\n3\n10\n"),
        ("compra sem desconto", "João\nCaneta\n2.5\n10\n0\n"),
        ("valor quebrado e milhar", "Ana\nMochila\n1999.9\n2\n15\n"),
    ],
    "ex04": [
        ("adulto com ingresso", "20\nsim\n"),
        ("adulto sem ingresso", "20\nnao\n"),
        ("menor de idade", "12\nsim\n"),
        ("idade no limite", "16\ns\n"),
        ("entradas invalidas antes das validas", "abc\n-5\n17\ntalvez\nn\n"),
    ],
    "ex05": [
        ("versao 1, verificar aprovacao", "1\n1\n8\n80\n\n5\n"),
        ("versao 1, classificar nota e opcao invalida", "1\n2\n9.5\n\n9\n\n5\n"),
        ("versao 1, nota invalida e fora do intervalo", "1\n1\nxyz\n11\n8\n60\n\n5\n"),
        ("versao 1, processar menu com opcao desconhecida", "1\n3\n7\n\n5\n"),
        ("versao 2, lista de alunos", "2\n7\nAna\n9\n2\ns\nBruno\n6\n3\nn\n\n8\n"),
        ("versao 2, multiplas notas", "2\n6\n4\ns\n2\nn\n\nsair\n"),
        ("versao 2, faltas invalidas", "2\n4\nDaniel\n7\n-1\nabc\n12\n\n8\n"),
        ("versao 3, avaliar aluno", "3\n4\nCarlos\n7.5\n4\n"),
        ("versao 3, teste invalido", "3\n9\n"),
        ("versao 4, sair", "4\n"),
        ("versao invalida", "9\n"),
    ],
}


def rodar(combo, exercicio, entrada):
    """Executa um exercicio com a entrada dada e devolve (saida, codigo)."""
    processo = subprocess.run(
        [sys.executable, str(RAIZ / combo / f"{exercicio}.py")],
        input=entrada,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return processo.stdout, processo.returncode


def comparar(exercicio, descricao, entrada):
    """Compara as duas variacoes. Devolve True quando batem."""
    saida_a, codigo_a = rodar(COMBOS[0], exercicio, entrada)
    saida_b, codigo_b = rodar(COMBOS[1], exercicio, entrada)

    if saida_a == saida_b and codigo_a == codigo_b:
        print(f"  ok     {exercicio}  [{descricao}]")
        return True

    print(f"  FALHOU {exercicio}  [{descricao}]")

    if codigo_a != codigo_b:
        print(f"    codigo de saida: {COMBOS[0]}={codigo_a}  {COMBOS[1]}={codigo_b}")

    diferenca = difflib.unified_diff(
        saida_a.splitlines(),
        saida_b.splitlines(),
        fromfile=f"{COMBOS[0]}/{exercicio}.py",
        tofile=f"{COMBOS[1]}/{exercicio}.py",
        lineterm="",
    )
    for linha in diferenca:
        print(f"    {linha}")

    return False


def main():
    print(f"Comparando {COMBOS[0]} x {COMBOS[1]}\n")

    total = 0
    falhas = 0

    for exercicio in sorted(CASOS):
        for descricao, entrada in CASOS[exercicio]:
            total += 1
            if not comparar(exercicio, descricao, entrada):
                falhas += 1

    print()
    if falhas:
        print(f"{falhas} de {total} casos divergiram.")
        return 1

    print(f"Todos os {total} casos produziram saidas identicas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

```
