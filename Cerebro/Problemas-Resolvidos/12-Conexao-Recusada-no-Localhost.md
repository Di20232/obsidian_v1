---
tags: [problema-resolvido, ambiente, servidor, reflex, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# ERR_CONNECTION_REFUSED ao abrir o localhost

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · navegador em `http://localhost:3000/despacho`.

## Sintoma e impacto

```
Failed to Load Page
ERR_CONNECTION_REFUSED (-102)
URL: http://localhost:3000/despacho
```

## Causa-raiz

Conexão recusada significa uma coisa bem específica: **não há nada escutando naquela porta**. Não é erro de rota, de permissão nem de código — o servidor não está no ar.

No caso, o processo do Reflex havia sido encerrado (ou nunca subiu depois de uma edição), e o navegador continuava apontando para a URL antiga.

Vale distinguir os três cenários que se confundem:

| O que aparece | O que significa |
|---|---|
| **ERR_CONNECTION_REFUSED** | Nada escutando na porta — servidor caído |
| **404** | Servidor no ar, rota inexistente |
| **500** | Servidor no ar, erro na aplicação — como em [[19-Docker-Parado-Causa-Erro-500|banco fora do ar]] |

## Correção aplicada

Subir o servidor de novo:

```bash
py -m reflex run --loglevel error
```

Ou duplo clique em `iniciar.bat`. Aguardar a mensagem indicando que o app está rodando antes de abrir o navegador.

## Prevenção

> [!problema] Diagnóstico em ordem
> 1. O processo está rodando? (`Get-NetTCPConnection -LocalPort 3000 -State Listen`)
> 2. Está na porta que você está acessando?
> 3. Só então investigue a aplicação.
>
> No Reflex há uma armadilha extra: **editar o arquivo não basta** — é preciso recompilar. Uma alteração que "não apareceu" pode simplesmente não ter sido compilada.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Ambiente: [[../Ambiente/02-Portas-e-Conflitos|Portas e conflitos]]
- Relacionados: [[18-Porta-3000-Presa-por-Processo-Orfao|Porta presa por processo órfão]] · [[19-Docker-Parado-Causa-Erro-500|Erro 500 por banco fora do ar]]

## Perguntas de revisão

O que significa ERR_CONNECTION_REFUSED? :: Que nada está escutando naquela porta: o servidor não está no ar.

Qual a diferença entre conexão recusada, 404 e 500? :: Recusada: servidor fora; 404: servidor no ar e rota inexistente; 500: servidor no ar com erro na aplicação.

Como verificar se algo escuta na porta 3000 no Windows? :: Com Get-NetTCPConnection -LocalPort 3000 -State Listen.

Qual armadilha extra do Reflex quando uma alteração não aparece? :: Editar o arquivo não basta; é preciso recompilar.
