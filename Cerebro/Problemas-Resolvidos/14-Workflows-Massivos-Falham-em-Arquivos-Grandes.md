---
tags: [problema-resolvido, processo, automacao, ferramentas, flashcards]
status: resolvido
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Workflows automáticos falham nos arquivos maiores

## Contexto

[[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]] · dois workflows paralelos de refatoração e auditoria, disparados a partir do pedido de caça intensa a bugs.

## Sintoma e impacto

Ambos os workflows terminaram com **falha por esgotamento de tentativas** em múltiplos agentes. O que travou não foi aleatório: foram justamente **`controle_suprimentos.py` e `db.py`** — os dois maiores arquivos do projeto.

Impacto: os arquivos que mais precisavam da refatoração de exceções e logging foram os únicos que **não a receberam**. Essa pendência continua aberta.

## Causa-raiz

Refatoração automática em lote, com vários agentes em paralelo, degrada quando o arquivo é grande e tem muitas camadas de tratamento de exceção repetido. Cada tentativa precisa carregar o arquivo inteiro, entender o padrão e reescrever — e o custo cresce mais rápido que o tamanho do arquivo.

Os arquivos **pequenos** passaram sem problema: os estados do Reflex e os utilitários foram refatorados e validados com sucesso.

## O que sobreviveu à falha

Vale registrar, porque não foi perda total. As fases de **mapeamento** concluíram e entregaram:

- diffs e recomendações de logging para todos os módulos de interface;
- avaliação do `.gitignore`, settings, requirements e caminhos sensíveis;
- confirmação de que **não há segredos ou tokens escritos no código**;
- confirmação de que a injeção de SQL está mitigada pela lista de permissão — com a f-string ainda como ponto de atenção ([[09-Nome-de-Tabela-em-F-String-no-SQL|ver]]).

## Correção aplicada

Aplicar manualmente o que os workflows já haviam mapeado: `.gitignore` endurecido e refatoração dos módulos de interface.

**Pendente:** `controle_suprimentos.py` e `db.py` precisam ser tratados de forma assistida, arquivo por arquivo, em vez de em lote.

## Prevenção

> [!problema] Quando automatizar e quando não
> Automação em lote é excelente para **muitos arquivos pequenos e parecidos**. Ela degrada exatamente onde o trabalho é mais difícil: arquivo grande, lógica entrelaçada, padrão irregular.
>
> A escolha certa é dividir: deixe o lote cuidar da massa, e trate os dois ou três arquivos grandes individualmente, com revisão a cada passo.

Ver o método que funcionou em [[../Praticas/06-Caca-de-Bugs|Caça de bugs]].

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Prática: [[../Praticas/06-Caca-de-Bugs|Caça de bugs]] · [[../Praticas/04-Auditoria-de-Projetos|Auditoria de projetos]]

## Perguntas de revisão

Onde a refatoração automática em lote costuma falhar? :: Nos arquivos grandes, com lógica entrelaçada e padrões irregulares.

Onde a automação em lote funciona bem? :: Em muitos arquivos pequenos e parecidos.

Como dividir o trabalho entre automação e revisão manual? :: Deixar o lote cuidar da massa e tratar os poucos arquivos grandes individualmente, com revisão a cada passo.
