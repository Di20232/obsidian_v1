---
tags: [problema-resolvido, docker, windows, ferramentas]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# docker exec quebra caminhos no Git Bash do Windows

## Contexto

[[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]] · Git Bash (MSYS) no Windows · comandos `docker compose exec` com caminhos absolutos.

## Sintoma e impacto

Comandos que funcionam em qualquer Linux falhavam:

```bash
docker compose exec app python /tmp/teste_stress.py
```

O container reclamava de um caminho que ninguém escreveu — algo como `C:/Program Files/Git/tmp/teste_stress.py`.

## Causa-raiz

O **Git Bash no Windows converte automaticamente caminhos ao estilo Unix** em caminhos do Windows antes de passá-los ao programa. É um recurso do MSYS, e normalmente ajuda.

Aqui atrapalha: o caminho `/tmp/teste_stress.py` é **para dentro do container Linux**, não para o Windows. A conversão acontece antes de o Docker receber o argumento, então o container recebe um caminho do Windows que não existe nele.

## Correção aplicada

Desativar a conversão apenas naquele comando:

```bash
MSYS_NO_PATHCONV=1 docker compose exec app python /tmp/teste_stress.py
```

## Prevenção

> [!problema] Sinal para reconhecer na hora
> Se um caminho que você escreveu como `/algo` aparece no erro como `C:/Program Files/Git/algo`, é conversão do MSYS. A correção é sempre `MSYS_NO_PATHCONV=1` na frente do comando.
>
> Acontece com `docker exec`, `docker run -v`, `kubectl exec` e qualquer ferramenta que receba caminhos destinados a um sistema Linux remoto ou containerizado.

Para copiar arquivos para dentro do container, `docker cp` funciona sem esse problema:

```bash
docker cp arquivo.py nome-do-container:/tmp/arquivo.py
```

## Links relacionados

- Projeto: [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]]
- Tecnologia: [[../Tecnologias/04-Docker|Docker]]
- Ambiente: [[../Ambiente/01-Maquina-Windows|Máquina Windows]]
