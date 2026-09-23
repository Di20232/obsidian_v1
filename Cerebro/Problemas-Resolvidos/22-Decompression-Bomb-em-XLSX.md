---
tags: [problema-resolvido, seguranca, python, dados, upload, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Decompression bomb em upload de planilha

## Contexto

[[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]] · `app/core/loaders.py` · upload de arquivos `.xlsx` · encontrado na mesma auditoria de segurança.

## Sintoma e impacto

Nenhum em uso. Risco de **negação de serviço**: um arquivo pequeno o suficiente para passar em qualquer validação poderia derrubar o processo por consumo de memória.

## Causa-raiz

A validação olhava para a coisa errada. Havia um limite de **500 MB no arquivo comprimido** — mas nenhum limite de linhas ou de tamanho **descomprimido** ao ler o Excel.

O detalhe que torna isso explorável: um `.xlsx` é um ZIP de XML. XML repetitivo comprime extraordinariamente bem. Um arquivo de poucos megabytes pode se expandir para gigabytes na memória ao ser lido pelo pandas ou openpyxl.

> A validação media o tamanho **antes** da expansão — exatamente onde o ataque não aparece.

## Correção aplicada

Verificação de tamanho seguro na leitura, limitando o volume **descomprimido**: número de linhas e bytes expandidos, com recusa antes de carregar tudo na memória.

Severidade: **baixa/média**, por ser negação de serviço em uma aplicação local.

## Prevenção

> [!seguranca] Valide o dado expandido, não o arquivo
> Qualquer formato comprimido — `.xlsx`, `.docx`, `.zip`, imagens, JSON comprimido — precisa de limite **depois** da descompressão. Tamanho de arquivo é uma métrica enganosa nesses casos.
>
> Para planilhas, limites concretos e úteis: número máximo de linhas, de colunas e de bytes descomprimidos — verificados durante a leitura, em fluxo, não depois de carregar.

## Links relacionados

- Projeto: [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]]
- Prática: [[../Praticas/07-Seguranca-em-Apps-Locais|Segurança em apps locais]] · [[../Praticas/05-Importacao-de-Planilhas|Importação de planilhas]]
- Trilha: [[../../Seguranca-Web/13-SSRF-Uploads-e-Caminhos|SSRF, uploads e caminhos]]

## Perguntas de revisão

O que é uma decompression bomb? :: Um arquivo pequeno comprimido que se expande para gigabytes ao ser lido, derrubando o processo por falta de memória.

Por que um .xlsx pode ser uma decompression bomb? :: Porque é um ZIP de XML, e XML repetitivo comprime extremamente bem.

O que validar num upload de arquivo comprimido? :: O tamanho depois de descomprimir, como linhas, colunas e bytes, e não só o tamanho do arquivo.
