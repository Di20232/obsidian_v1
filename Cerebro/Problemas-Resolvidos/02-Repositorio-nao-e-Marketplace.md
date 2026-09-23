---
tags: [problema-resolvido, git, plugins, configuracao, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Repositório selecionado não é um marketplace de plugins

> [!problema] Sintoma
> Uma ferramenta informa que o repositório não é marketplace porque não encontra o manifesto esperado.

## Causa-raiz

Foi selecionada uma pasta vazia, um plugin individual ou outro repositório que não contém a estrutura de marketplace exigida.

## Correção

1. Abra a raiz do repositório pretendido.
2. Confirme que existe o manifesto obrigatório no caminho esperado pela ferramenta.
3. Se houver somente arquivos de um plugin, procure o repositório que agrega o marketplace.
4. Se a pasta atual tiver apenas diretórios de trabalho/saída, volte para a URL ou pasta correta antes de tentar adicionar novamente.

## Prevenção

Antes de cadastrar qualquer repositório, valide a estrutura e leia o README do projeto. “Repositório de plugin” e “repositório de marketplace” são papéis diferentes.

## Links relacionados

- [[../../Programacao-Geral/03-Git-e-Controle-de-Versao|Git e Controle de Versão]]
- [[../Tecnologias/00-Indice|Tecnologias]]

## Perguntas de revisão

Por que uma ferramenta diz que o repositório não é marketplace de plugins? :: Porque não encontra o manifesto esperado: foi escolhida uma pasta vazia, um plugin individual ou outro repositório.

Qual a diferença entre repositório de plugin e de marketplace? :: São papéis diferentes: o de marketplace agrega plugins e tem o manifesto próprio; o de plugin contém um plugin só.

O que fazer antes de cadastrar um repositório numa ferramenta? :: Validar a estrutura e ler o README do projeto.
