---
tags: [python, setup]
cssclasses: [cerebro-nota, cerebro-python]
---

# Instalando e Preparando o Ambiente

## Por que essa etapa existe

Seu computador não vem com o interpretador Python pronto para uso sério por padrão (no Windows, geralmente nem vem). Antes de escrever qualquer código, você precisa de duas coisas:

1. O **interpretador Python** instalado.
2. Um lugar confortável para **escrever código** — um editor de texto voltado para programação.

## 1. Instalar o Python (Windows)

1. Acesse o site oficial: `python.org/downloads` e baixe a versão mais recente.
2. Ao rodar o instalador, marque a opção **"Add python.exe to PATH"** antes de clicar em instalar. Isso é importante: é o que permite digitar `python` no terminal de qualquer pasta e o sistema saber onde encontrá-lo.
3. Depois de instalar, abra um terminal (PowerShell) e confirme:

```bash
python --version
```

Se aparecer algo como `Python 3.12.x`, deu certo.

> **Por que isso importa**: "PATH" é uma lista de pastas que o sistema operacional verifica quando você digita um comando. Se o Python não estiver nela, o terminal responde algo como "python não é reconhecido como comando".

## 2. Editor de código

Você pode escrever Python em qualquer editor de texto puro, mas um editor voltado para código ajuda bastante porque destaca erros, colore a sintaxe e sugere código. Recomendação para iniciantes: **VS Code** (gratuito, leve, com extensão oficial de Python).

Depois de instalar o VS Code, instale a extensão "Python" (da Microsoft) dentro dele — ela habilita autocompletar, execução e depuração.

## 3. O terminal

Você vai usar o terminal (linha de comando) o tempo todo para rodar seus programas. Não precisa dominá-lo agora, só o essencial:

- `cd caminho\da\pasta` — entra em uma pasta.
- `dir` (Windows) — lista arquivos da pasta atual.
- `python nome_do_arquivo.py` — executa um arquivo Python.

## 4. Verificando que está tudo pronto

Crie uma pasta para seus estudos, por exemplo `Python\exemplos` (ela já existe neste cofre — veja [[00-Indice]]). Dentro dela, você vai criar arquivos terminados em `.py`. Esse é o formato de arquivo que o interpretador Python reconhece como código-fonte.

## Erros comuns nesta etapa

- Esquecer de marcar "Add to PATH" na instalação → comando `python` não é reconhecido. Solução: reinstalar marcando a opção, ou adicionar manualmente ao PATH.
- Ter mais de uma versão de Python instalada e não saber qual está rodando → use sempre `python --version` para conferir.

## Exercício

Abra o terminal, rode `python --version` e depois digite apenas `python` (sem mais nada) e pressione Enter. Você vai entrar no **modo interativo** do Python (um `>>>` vai aparecer). Digite `2 + 2` e pressione Enter. Depois digite `exit()` para sair. Isso é o interpretador rodando código, um comando por vez, em tempo real.

---
Próxima nota: [[03-Primeiro-Programa]]
