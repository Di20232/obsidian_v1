---
tags: [ia, dados, treino, dataset, lgpd, flashcards]
cssclasses: [cerebro-nota, cerebro-ia]
---

# Preparar dados para treinar IA

Um modelo aprende exatamente o que os dados mostram, inclusive os erros. Preparar dados é a parte mais trabalhosa e mais importante de qualquer projeto de IA. Esta nota usa **este cofre** como exemplo.

## O que já existe no cofre

```bash
node ferramentas/exportar-para-ia.js
```

Gera três arquivos em `exportacao/` (fora do git, recriáveis a qualquer momento):

| Arquivo | Conteúdo | Serve para |
|---|---|---|
| `notas.jsonl` | uma nota por linha: id, título, trilha, tags, `verificado_em`, `fonte`, texto limpo | indexar num [[04-RAG-Busca-Mais-Geracao\|RAG]]; pré-treino |
| `perguntas.jsonl` | pares das seções "Perguntas de revisão", com a nota de origem | conjunto de avaliação; flashcards |
| `perguntas-chat.jsonl` | os mesmos pares no formato de conversa | [[05-Fine-Tuning\|fine-tuning]] |

Ficam de fora, por padrão:
- **cópias de código de terceiros** (`*/Fontes/*`): têm licença própria (o repositório Second Brain é MIT, que exige manter o aviso de copyright);
- **modelos** de nota (`Templates/`), que são esqueletos vazios;
- **Diário** e **Inbox**, que são rascunhos pessoais. Só entram com `--incluir-pessoal`, depois de revisar.

O `README.md` da raiz também fica de fora, sempre: ele descreve o repositório e não é nota.

## Checklist antes de treinar

### Direito de usar
- [ ] O texto é seu, ou a licença permite o uso? Conteúdo copiado de sites, cursos e livros **não** entra.
- [ ] Repositórios importados: licença conferida e aviso de copyright preservado quando exigido.

### Privacidade (LGPD)
- [ ] Sem nomes de clientes, CPF, telefone, e-mail, endereço.
- [ ] Sem senhas, tokens, chaves de API, caminhos internos sensíveis.
- [ ] Prints e registros de conversas com terceiros revisados ou removidos.

Veja [[09-Riscos-Seguranca-e-LGPD-na-IA|riscos e LGPD]].

### Qualidade
- [ ] **Sem duplicatas:** a mesma pergunta com respostas diferentes ensina contradição.
- [ ] **Sem dados vencidos:** notas com `verificado_em` antigo reconferidas, ou tiradas do fine-tuning.
- [ ] **Respostas autocontidas:** "Sim, como dito acima" não serve; a resposta precisa fazer sentido sozinha.
- [ ] **Formato consistente:** mesmo estilo de resposta em todos os exemplos.
- [ ] **Sem instruções escondidas:** texto do tipo "ignore as instruções anteriores" colado numa nota vira instrução aprendida. O cofre já teve um caso assim, num arquivo importado.

### Separação
- [ ] Conjunto de **teste** separado antes de qualquer treino ([[07-Avaliar-Sistemas-de-IA|avaliação]]).

## Como escrever notas que viram bons dados

As convenções do cofre já são boas práticas de dados:

| Convenção do cofre | Por que ajuda a IA |
|---|---|
| uma ideia por seção, com título descritivo | trechos de busca limpos; cada seção é um bom *chunk* |
| frontmatter com `tags`, `verificado_em`, `fonte` | filtrar por assunto e por idade do dado |
| definição no início ("X é…") | o modelo aprende a definição correta |
| exemplos numéricos conferidos | ensina o raciocínio, não só a regra |
| "Perguntas de revisão" com respostas completas | pares prontos de treino e de avaliação |
| links entre notas | contexto e relações entre conceitos |
| uma nota por assunto, atualizada em vez de duplicada | sem versões contraditórias |

A regra de ouro para as perguntas: **a resposta deve estar correta, completa numa frase e fazer sentido sem a pergunta ao lado**.

## Quanto dado é preciso

- **RAG:** funciona com o que houver. Mais notas bem organizadas = mais perguntas respondidas.
- **Fine-tuning de formato ou tom:** algumas centenas de exemplos bons costumam bastar para ver efeito.
- **Ensinar um domínio inteiro por fine-tuning:** raramente é o caminho certo para um cofre pessoal. Use RAG.

## Perguntas de revisão

O que o exportador do cofre gera? :: Três arquivos JSONL em exportacao/: notas completas com metadados, pares de pergunta e resposta, e os mesmos pares no formato de conversa.

Por que as cópias de código de terceiros ficam fora da exportação? :: Porque têm licença própria; o uso exige respeitar os termos, como manter o aviso de copyright.

Por que o Diário e a Inbox ficam fora por padrão? :: Porque são rascunhos pessoais que podem ter dados privados e informação não revisada.

Que dados pessoais precisam sair antes de treinar? :: Nomes de clientes, CPF, telefone, e-mail, endereço, além de senhas, tokens e chaves.

Por que duplicatas atrapalham o treino? :: A mesma pergunta com respostas diferentes ensina contradição ao modelo.

Qual a regra de ouro para escrever pares de pergunta e resposta? :: A resposta deve estar correta, completa numa frase e fazer sentido sem a pergunta ao lado.

Por que texto de instrução escondido numa nota é perigoso para o treino? :: Porque o modelo aprende a seguir aquela instrução como se fosse comportamento desejado.

---
Anterior: [[05-Fine-Tuning|Fine-tuning]] · Próxima: [[07-Avaliar-Sistemas-de-IA|Avaliar sistemas de IA]] · Trilha: [[IA-Aplicada/00-Indice|IA Aplicada]]
