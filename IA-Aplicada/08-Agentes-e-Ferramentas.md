---
tags: [ia, agentes, automacao, ferramentas, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Agentes e ferramentas

Um modelo sozinho só produz texto. Um **agente** é um modelo ligado a **ferramentas**: ler arquivos, rodar comandos, consultar uma API, buscar na web, criar um produto na loja. O modelo decide qual ferramenta usar, vê o resultado e decide o próximo passo, até terminar a tarefa.

O [[Cerebro/Tecnologias/08-Claude-Code|Claude Code]], usado para construir este cofre, é um agente: leu as notas, rodou os scripts de verificação e gravou os commits.

## Como funciona

```text
objetivo → modelo pensa → pede uma ferramenta (ex.: ler arquivo X)
         → o sistema executa e devolve o resultado
         → modelo pensa de novo → outra ferramenta ou resposta final
```

Cada ferramenta é descrita ao modelo com **nome**, **para que serve** e **quais parâmetros** recebe. Descrições claras fazem o agente escolher a ferramenta certa, assim como um bom [[02-Escrevendo-Prompts|prompt]].

## Conectores (MCP)

O **MCP** (*Model Context Protocol*) é um padrão aberto para ligar ferramentas e fontes de dados a assistentes de IA. Um "servidor MCP" oferece ferramentas (por exemplo, consultar pedidos da Shopify, ler o Google Drive) que qualquer assistente compatível pode usar. É assim que o Claude consegue consultar uma loja, como citado em [[Ecommerce/19-Rotina-de-Gestao-da-Loja|rotina de gestão da loja]].

## Controle: o que o agente pode fazer sozinho

Quanto mais poder a ferramenta tem, mais controle ela precisa:

| Tipo de ação | Exemplo | Controle recomendado |
|---|---|---|
| **Ler** | consultar pedidos, ler notas | pode ser automático |
| **Criar ou alterar, reversível** | editar uma nota com git, criar rascunho de produto | automático com registro, e desfazer disponível |
| **Irreversível ou externo** | enviar e-mail a cliente, publicar, apagar, mudar preço ao vivo | **confirmação humana** a cada vez |
| **Dinheiro e credenciais** | pagar, transferir, digitar senha | **nunca** delegar; a pessoa faz |

É o princípio de **humano no circuito** do [[Cerebro/Mapas/05-Mapa-IA|Mapa de IA]]. O git do cofre existe justamente para que as alterações feitas por agentes tenham desfazer ([[Cerebro/Guias/07-Rotina-do-Cofre|rotina do cofre]]).

## Onde agentes falham

- **Instruções escondidas** em conteúdo lido: uma página ou arquivo diz "ignore as regras e faça X". O agente deve tratar conteúdo lido como **dado**, nunca como ordem ([[09-Riscos-Seguranca-e-LGPD-na-IA|riscos]]).
- **Loops:** tenta a mesma coisa várias vezes sem progredir.
- **Excesso de confiança:** declara "pronto" sem verificar. Bons agentes conferem o resultado (rodar o teste, checar os links).
- **Escopo:** faz mais do que foi pedido. Peça tarefas bem delimitadas.

## Perguntas de revisão

O que é um agente de IA? :: Um modelo ligado a ferramentas, que escolhe qual usar, vê o resultado e decide o próximo passo até concluir a tarefa.

O que é MCP? :: Model Context Protocol, um padrão aberto para conectar ferramentas e fontes de dados a assistentes de IA.

Que ações de um agente exigem confirmação humana? :: As irreversíveis ou externas, como enviar mensagens, publicar, apagar e mudar preços ao vivo.

Que ações nunca devem ser delegadas a um agente? :: Pagamentos, transferências e digitação de senhas ou credenciais.

Como um agente deve tratar instruções encontradas num arquivo ou página que leu? :: Como dado, nunca como ordem.

Por que o git ajuda quando agentes editam o cofre? :: Porque toda alteração salva pode ser desfeita.

---
Anterior: [[07-Avaliar-Sistemas-de-IA|Avaliar sistemas de IA]] · Próxima: [[09-Riscos-Seguranca-e-LGPD-na-IA|Riscos e LGPD]] · Trilha: [[IA-Aplicada/00-Indice|IA Aplicada]]
