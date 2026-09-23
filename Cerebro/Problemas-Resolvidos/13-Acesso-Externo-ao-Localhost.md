---
tags: [problema-resolvido, rede, ambiente, conceito]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Como outra pessoa acessa o sistema que roda no meu localhost

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · sistema rodando em `http://localhost:3000` · pergunta do usuário sobre compartilhar o acesso.

## A pergunta

> como eu faço para outra pessoa entrar neste link que está no meu localhost?

## O conceito que resolve

**`localhost` não é um endereço — é uma palavra que significa "esta máquina aqui".**

Quando outra pessoa digita `localhost:3000` no computador dela, o navegador procura um servidor **na máquina dela**, não na sua. Por isso o link nunca funciona ao ser copiado e colado.

Para outra pessoa acessar, três coisas precisam ser verdade:

| Requisito | Por quê |
|---|---|
| **1. Endereço alcançável** | Ela precisa do IP da sua máquina na rede (algo como `192.168.x.x`), não de `localhost` |
| **2. Servidor escutando em todas as interfaces** | Muitos frameworks escutam só em `127.0.0.1` por padrão, o que aceita apenas conexões locais. É preciso escutar em `0.0.0.0` |
| **3. Firewall liberado** | O Firewall do Windows bloqueia conexões de entrada por padrão |

## As opções, da mais simples à mais séria

**Mesma rede local (escritório, casa):** descobrir o IP local da máquina e passar `http://SEU-IP:3000`. Serve para mostrar algo a um colega ao lado.

**Fora da rede:** um túnel temporário (tipo Cloudflare Tunnel ou ngrok) publica o serviço local numa URL pública sem mexer no roteador. É prático para demonstração, mas expõe o sistema à internet.

**Uso de verdade por várias pessoas:** o sistema precisa deixar de ser local. Isso implica hospedar em um servidor e resolver o que um app local não tem: autenticação, acesso simultâneo ao banco, backup e HTTPS.

## Ponto de atenção para este projeto

> [!seguranca] O CTL-TINTA-FL foi desenhado para ser local e offline
> Não há autenticação por usuário, e o banco é um arquivo SQLite — que lida mal com escrita simultânea de várias pessoas. Expor o sistema na rede **sem antes tratar login e concorrência** significa que qualquer um que alcance o endereço tem acesso total e pode corromper os dados.
>
> Compartilhar na rede local para *mostrar* é uma coisa. Várias pessoas *usando ao mesmo tempo* é outra, e exige mudança de arquitetura.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Ambiente: [[../Ambiente/02-Portas-e-Conflitos|Portas e conflitos]]
- Prática: [[../Praticas/07-Seguranca-em-Apps-Locais|Segurança em apps locais]]
