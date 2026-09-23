---
tags: [pratica, debugging, seguranca, processo, flashcards]
cssclasses: [cerebro-nota, cerebro-praticas]
---

# Caça de bugs — o método que funcionou

Pedido recorrente nos três projetos: *caça intensa de bugs, quebras de código e brechas, corrigindo todas.* Esta nota registra o que funcionou e o que não funcionou.

Complementa [[04-Auditoria-de-Projetos|Auditoria de projetos]].

## O princípio central

> [!problema] Auditoria empírica vence análise estática
> Ler o código produz **suspeitas**. Rodar o código produz **fatos**.
>
> A diferença prática: uma suspeita gera discussão sobre severidade; um fato vem com o input usado, o traceback e a linha exata. Só o segundo permite corrigir com confiança.

No [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]], a sondagem em Python confirmou em segundos três coisas que a leitura só sugeria: que `sqlite3.Row` gerava chaves duplicadas, que a f-string de tabela aceitava entrada arbitrária, e que a exclusão batia em `IntegrityError`.

## Vetores que vale atacar de verdade

Usados na auditoria do CTL-TINTA-FL e do [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]]:

| Vetor | O que testa |
|---|---|
| **Injeção SQL** | Queries dinâmicas e tentativa de furar a lista de permissão |
| **Path traversal** | Escrita arbitrária em exportação de CSV e screenshots |
| **Confusão de tipo** | `None`, string vazia, 10^18, NaN, infinito, vírgula vs ponto, unicode |
| **Entrada extrema na interface** | Strings enormes, XSS, valores fora de faixa |
| **Concorrência** | Escrita simultânea no SQLite — travamento e corrupção |
| **Upload** | Arquivo comprimido que explode na memória |

## A escala de severidade que evita drama

Nem todo achado merece a mesma urgência. A classificação usada:

- **Real e explorável hoje** → corrigir agora
- **Real e latente** → a falha está escrita, falta alguém ativar o caminho. Corrigir mesmo assim, porque a ativação costuma ser uma linha de configuração ([[../Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL|exemplo]])
- **Ponto de atenção** → não é falha, mas é padrão frágil que convida a uma

Dizer explicitamente "não é explorável hoje, e mesmo assim deve ser corrigido porque X" é mais útil que inflar ou minimizar a severidade.

## O que não funcionou

Refatoração automática em lote com vários agentes paralelos **travou justamente nos dois maiores arquivos** — os que mais precisavam. → [[../Problemas-Resolvidos/14-Workflows-Massivos-Falham-em-Arquivos-Grandes|caso completo]]

> [!problema] Onde dividir
> Lote resolve **muitos arquivos pequenos e parecidos**. Os dois ou três arquivos grandes do projeto precisam de tratamento individual, com revisão a cada passo. Planejar isso desde o início evita descobrir no fim que o trabalho principal não foi feito.

## Fechamento de uma caçada

1. Confirmar cada achado com evidência executada, não com leitura
2. Classificar por severidade real
3. Corrigir, começando por quebras e segurança
4. **Reverificar** — rodar de novo o que produziu o achado
5. Registrar cada correção em [[../Problemas-Resolvidos/00-Indice|Problemas Resolvidos]] com causa-raiz, não só com o conserto

O passo 5 é o que transforma horas de investigação em minutos da próxima vez.

## Links relacionados

- Prática: [[04-Auditoria-de-Projetos|Auditoria de projetos]] · [[07-Seguranca-em-Apps-Locais|Segurança em apps locais]]
- Mapa: [[../Mapas/04-Mapa-Seguranca|Mapa de Segurança]]

## Perguntas de revisão

Por que auditoria empírica vence análise estática? :: Porque ler o código gera suspeitas e rodar o código gera fatos, com a entrada, o erro e a linha exata.

Quais vetores atacar numa caça de bugs? :: Injeção SQL, path traversal, confusão de tipos, entradas extremas, concorrência e upload de arquivos.

Quais os três níveis de severidade de um achado? :: Real e explorável hoje, real e latente, e ponto de atenção.

Quais os passos para fechar uma caçada de bugs? :: Confirmar com evidência executada, classificar a severidade, corrigir, reverificar e registrar com a causa-raiz.
