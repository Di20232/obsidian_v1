---
tags: [moc, dados, banco-de-dados, sql]
aliases: [Mapa de Dados]
cssclasses: [cerebro-nota, cerebro-dados]
---

# 🗃️ Mapa de Dados e Bancos de Dados

Dados confiáveis sustentam quase todo software. O caminho saudável é entender a pergunta de negócio antes de criar tabelas ou consultas.

```text
Pergunta → entidades → relações → restrições → consultas → relatórios/decisões
```

## Conceitos centrais

- **Entidade:** algo sobre o qual guardamos dados, como Cliente ou Pedido.
- **Atributo:** característica de uma entidade, como nome ou data.
- **Chave primária:** identificador único de cada registro.
- **Chave estrangeira:** ligação entre duas entidades.
- **Restrição:** regra que evita dados inválidos ou inconsistentes.
- **Índice:** estrutura que acelera buscas, com custo de escrita e espaço.
- **Transação:** grupo de alterações que deve ocorrer por inteiro ou não ocorrer.

## Trilhas do cofre

- [[../../Programacao-Geral/09-SQL-e-Bancos-de-Dados|SQL e Bancos de Dados]]
- [[../../SQLite/00-Indice|SQLite]] — banco simples, local e embutido
- [[../../MySQL/00-Indice|MySQL]] — banco servidor para aplicações multiusuário

## Antes de mudar dados importantes

1. Qual é a regra de negócio e qual registro ela afeta?
2. Há backup ou uma forma de testar em dados de exemplo?
3. A alteração pode rodar duas vezes sem duplicar ou estragar dados?
4. Há validação no servidor, além da tela?
5. Como conferir o resultado e como reverter se necessário?

## Conexões

Dados atravessam [[01-Mapa-Web|Web]], [[03-Mapa-Engenharia|Engenharia]], [[04-Mapa-Seguranca|Segurança]] e [[05-Mapa-IA|IA]].
