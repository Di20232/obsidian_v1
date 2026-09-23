---
tags: [problema-resolvido, docker, banco-de-dados, ambiente, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Login retorna 500 porque o Docker foi encerrado

## Contexto

[[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]] · sistema que funcionava normalmente algumas horas antes.

## Sintoma e impacto

A tela carregava, mas o login respondia **HTTP 500**. Nos logs:

```
Can not reach database server at localhost:5433
```

## Causa-raiz

O **Docker Desktop havia sido encerrado** cerca de três horas antes, levando junto o container do PostgreSQL. O app Node continuava rodando no host, servindo as páginas normalmente — mas sem banco por trás.

Daí o formato do sintoma: a interface aparece (é arquivo estático), e só quebra quando alguma rota precisa de dados.

> **500 significa que o servidor está vivo e falhou ao processar.** É o oposto de [[12-Conexao-Recusada-no-Localhost|ERR_CONNECTION_REFUSED]], onde não há ninguém para atender. Saber diferenciar economiza metade do diagnóstico.

## Correção aplicada

```bash
docker compose up -d
```

**Os dados estavam intactos** — estavam em um volume nomeado do Docker, que sobrevive ao container ser parado ou removido. Só o processo havia morrido.

## Prevenção

> [!problema] Se a tela abre mas as ações falham, suspeite das dependências
> Aplicação no ar + erro 500 = alguma coisa **atrás** do app está fora. Banco, cache, fila, API externa. Comece pelo banco.
>
> Depois de reiniciar a máquina ou fechar o Docker Desktop, o comando é sempre o mesmo:
> ```bash
> docker compose up -d
> ```

Vale também confirmar que o volume é **nomeado** e não anônimo — é isso que garante que os dados sobrevivam.

## Links relacionados

- Projeto: [[../Projetos/06-Mercadinho-Seu-Joao|Mercadinho Seu João]]
- Tecnologia: [[../Tecnologias/04-Docker|Docker]]
- Relacionado: [[12-Conexao-Recusada-no-Localhost|Conexão recusada: o outro erro]]

## Perguntas de revisão

Por que a tela carrega mas o login dá erro 500? :: O app está no ar, mas uma dependência por trás, geralmente o banco, está fora.

O que fazer depois de reiniciar a máquina ou fechar o Docker Desktop? :: Rodar docker compose up -d.

Por que os dados sobreviveram ao container parado? :: Porque estavam num volume nomeado do Docker, que persiste mesmo sem o container.
