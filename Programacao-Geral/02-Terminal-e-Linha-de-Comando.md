---
tags: [programacao, fundamentos, terminal, flashcards]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Terminal e Linha de Comando

## Por que isso é essencial, não opcional

Interfaces gráficas (clicar em ícones) escondem detalhes para facilitar o uso casual. Programadores usam o **terminal** (também chamado de linha de comando, shell, console) porque ele é mais rápido, mais preciso, e é a única forma de operar muitas ferramentas (git, servidores, instaladores de pacotes). Você já usou isso em [[../Python/02-Instalando-Python]] para rodar `python`.

## O que é, de fato

O terminal é um programa que aceita **comandos de texto** e devolve texto como resposta — sem menus, sem cliques. No Windows, os principais são **PowerShell** e o **Prompt de Comando (cmd)**; no Linux/macOS, é o **Bash** (ou variantes como zsh).

## Comandos essenciais (PowerShell/Windows)

```powershell
pwd                     # mostra a pasta atual (print working directory)
cd Documents             # entra na pasta "Documents"
cd ..                    # sobe um nível de pasta
ls                       # lista arquivos e pastas da pasta atual (Get-ChildItem)
mkdir novo_projeto        # cria uma nova pasta
New-Item arquivo.py       # cria um arquivo vazio
Remove-Item arquivo.py    # apaga um arquivo (cuidado: não vai para a lixeira)
Copy-Item origem.py destino.py   # copia um arquivo
```

Equivalentes no Bash/Linux/macOS (bom saber, pois muita documentação assume Bash):

```bash
pwd
cd Documents
cd ..
ls
mkdir novo_projeto
touch arquivo.py
rm arquivo.py
cp origem.py destino.py
```

## Conceitos-chave

- **Diretório atual**: toda sessão de terminal está "dentro" de alguma pasta; comandos relativos (como `python arquivo.py`) dependem de onde você está.
- **Caminho relativo vs. absoluto**: já visto em [[../Python/14-Arquivos]] — `pasta\arquivo.py` (relativo à pasta atual) vs. `C:\Users\Diego\pasta\arquivo.py` (endereço completo, sempre o mesmo não importa de onde você rode).
- **Argumentos de comando**: a maioria dos comandos aceita opções depois do nome, geralmente começando com `-` ou `--`. Ex.: `python --version` (visto em [[../Python/02-Instalando-Python]]) — `--version` é um argumento que muda o comportamento do comando `python`.
- **Autocompletar**: pressionar Tab enquanto digita um nome de arquivo/pasta geralmente completa automaticamente — evita erros de digitação e economiza tempo.
- **Histórico**: a seta para cima repete o último comando digitado — útil para reexecutar ou ajustar algo que você acabou de rodar.

## Por que isso importa além de rodar `.py`

Praticamente toda ferramenta de desenvolvimento profissional (Git, visto em [[03-Git-e-Controle-de-Versao]]; gerenciadores de pacotes; servidores locais) é operada via terminal. Interfaces gráficas para essas ferramentas existem, mas o terminal continua sendo a forma mais universal e documentada de usá-las — todo tutorial na internet assume que você sabe o básico de terminal.

## Erros comuns

- Rodar um comando de dentro da pasta errada (esquecer de `cd` até a pasta certa antes).
- Confundir sintaxe do PowerShell com a do Bash (comandos como `rm -rf`, comuns em tutoriais de Linux/macOS, não funcionam direto no PowerShell).
- Apagar um arquivo pelo terminal sem perceber que **não existe lixeira** por padrão nesse caminho — é definitivo.

## Exercício

Abra o terminal, crie uma pasta chamada `teste_terminal`, entre nela, crie um arquivo `nota.txt` dentro, liste o conteúdo da pasta para confirmar que o arquivo existe, e depois apague o arquivo e a pasta.

## Perguntas de revisão

Por que programadores usam o terminal? :: Porque é mais rápido e preciso, e muitas ferramentas como git e gerenciadores de pacotes só funcionam ou são documentadas por ele.

O que fazem pwd, cd .. e ls? :: pwd mostra a pasta atual, cd .. sobe um nível e ls lista o conteúdo da pasta.

Para que serve a tecla Tab no terminal? :: Para autocompletar nomes de arquivos e pastas.

Arquivos apagados pelo terminal vão para a lixeira? :: Não; a exclusão pelo terminal é definitiva.

Comandos do Bash funcionam direto no PowerShell? :: Nem sempre; comandos como rm -rf, comuns em tutoriais Linux, não funcionam direto no PowerShell.

---
Próxima nota: [[03-Git-e-Controle-de-Versao]]
