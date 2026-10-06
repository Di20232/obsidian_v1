---
tags: [ia, inteligencia-artificial, indice, moc]
aliases: [IA Aplicada, Inteligência Artificial]
cssclasses: [cerebro-nota, cerebro-ia]
---

# 🤖 IA Aplicada

Esta trilha explica como os modelos de linguagem funcionam e como usá-los de verdade: escrever instruções, buscar nas próprias anotações, treinar com dados próprios, medir se deu certo e evitar os riscos. O [[Cerebro/Mapas/05-Mapa-IA|Mapa de IA]] tem a visão geral; aqui está a prática.

Ela também explica **o próprio cofre como dado de treino**. A nota [[06-Preparar-Dados-para-Treinar-IA|Preparar dados para treinar IA]] mostra como as notas e as perguntas de revisão viram arquivos de treino.

## Trilha

### Como funciona
1. [[01-Como-Funcionam-os-Modelos-de-Linguagem|Como funcionam os modelos de linguagem]] — tokens, contexto, probabilidade, alucinação
2. [[02-Escrevendo-Prompts|Escrevendo prompts]] — instrução, contexto, exemplos, formato de saída

### Usar o próprio conhecimento
3. [[03-Embeddings-e-Busca-Semantica|Embeddings e busca semântica]] — buscar por significado, não por palavra
4. [[04-RAG-Busca-Mais-Geracao|RAG: busca + geração]] — responder com base nas suas notas, citando a fonte
5. [[05-Fine-Tuning|Fine-tuning]] — quando treinar um modelo vale a pena, e quando não
6. [[06-Preparar-Dados-para-Treinar-IA|Preparar dados para treinar IA]] — limpeza, formato JSONL, licença, privacidade

### Fazer direito
7. [[07-Avaliar-Sistemas-de-IA|Avaliar sistemas de IA]] — conjunto de teste, métricas, regressão
8. [[08-Agentes-e-Ferramentas|Agentes e ferramentas]] — IA que executa ações, e como controlar
9. [[09-Riscos-Seguranca-e-LGPD-na-IA|Riscos, segurança e LGPD]] — injeção de instruções, vazamento, dados pessoais

### Na prática
10. [[10-IA-no-Pequeno-Negocio|IA no pequeno negócio]] — atendimento, catálogo, análise, com os limites de cada uso

## As três ideias que atravessam a trilha

1. **O modelo prevê texto provável, não verifica fatos.** Tudo que importa precisa de fonte ou conferência. → [[01-Como-Funcionam-os-Modelos-de-Linguagem|como funciona]]
2. **Conhecimento que muda vai na busca (RAG); comportamento vai no treino (fine-tuning).** → [[05-Fine-Tuning|quando treinar]]
3. **Sem avaliação, "melhorou" é opinião.** Um conjunto de perguntas com respostas esperadas é o que permite comparar. → [[07-Avaliar-Sistemas-de-IA|avaliação]]

## Onde isso encontra o resto do cofre

- [[Cerebro/Tecnologias/08-Claude-Code|Claude Code]] — um agente de IA usado no dia a dia deste cofre
- [[Cerebro/Guias/08-Cofre-para-IA-e-Lembretes|Cofre para IA e lembretes]] — as convenções e ferramentas de exportação
- [[GANs/00-Indice|GANs]] — redes adversariais generativas, outra família de modelos gerativos, com um experimento que treina uma GAN nas notas do cofre
- [[Ecommerce/00-Indice|E-commerce]] — onde a IA entra na operação de uma loja
