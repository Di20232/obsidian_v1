---
tags: [projeto, python, streamlit, dados, docker, seguranca, flashcards]
status: em-uso
cssclasses: [cerebro-nota, cerebro-projetos]
---

# Projeto W — Análise de Vendas e Planejamento de Estoque

> [!projeto] Origem
> Registro extraído das sessões de trabalho no Claude Code. Volta para [[00-Indice|📦 Projetos]].

## O que é

Sistema web **local, simples e leve** para análise de vendas e planejamento de estoque. Você anexa planilhas de vendas/estoque (Excel ou CSV) e ele processa automaticamente, gerando dashboard e análise de estoque.

- **Pasta:** `C:\Users\Perim\Documents\proejto\projeto_w`
- **Stack:** Python · Streamlit · Pandas · Plotly · Docker
- **URL:** `http://localhost:8501`
- **Container:** `analise-vendas-estoque`

> 📄 O briefing original está guardado no cofre, na raiz: `Quero desenvolver um sistema web si.txt`

## As perguntas que o sistema responde

- Quanto estou vendendo? Quais lojas vendem mais? Quais CDs movimentam mais?
- Quais produtos vendem mais? Qual a média de venda dos produtos?
- Quanto estoque eu deveria manter? Quantas unidades devo comprar?
- Em quantos dias precisarei de novo pedido? Quais produtos vão faltar? Quais estão em excesso?

## Ideia central: mapeamento de colunas

Os nomes das colunas variam de planilha para planilha. Então o sistema:
1. tenta identificar sozinho (`Data`, `Loja`, `CD`, `SKU`, `Produto`, `Quantidade`, `Valor`, `Estoque`, `Lead time`…)
2. e, quando não consegue, abre uma **etapa de mapeamento manual** — DATA → [Data da Venda], LOJA → [Filial], e assim por diante

## Telas

| Tela | O que mostra |
|---|---|
| **Dashboard** | Evolução de vendas, média/dia, melhor dia, Top 10 lojas e CDs |
| **Estoque** | SKUs analisados, em risco de ruptura, em atenção, em excesso, cobertura mediana |
| **Alertas** | Faixas de urgência (7 dias / 15 dias / excesso / adequado), com export CSV e Excel |
| **Sugestão de Compras** | Venda média diária, cobertura, lead time, ponto de reposição, sugestão de compra com risco |

Com os dados de exemplo (11.540 linhas, 20 SKUs) o sistema mostrou: 5 SKUs precisando de compra, 2.906 unidades sugeridas, R$ 67,2 mil estimados, cobertura mediana de 22,7 dias.

> 💡 O sistema avisa explicitamente que são **estimativas, não garantias**, e recomenda validação humana. Bom padrão a manter em qualquer previsão.

## Arquitetura

```
app/
├── main.py, state.py, config.py
├── core/     loaders · cleaning · mapping · schema · pipeline
│             sales · inventory · purchasing · forecast · filters · exporters
├── data/     repository.py
└── ui/       components · theme · pages
```

## Auditoria de segurança

O usuário pediu para agir como um atacante e simular ataques ao próprio sistema. Rodamos uma auditoria completa que encontrou **dois achados reais**:

- [[../Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL|SQL injection latente via token de URL]] — severidade média, latente
- [[../Problemas-Resolvidos/22-Decompression-Bomb-em-XLSX|Decompression bomb em upload .xlsx]] — baixa/média, negação de serviço

Ambos corrigidos e commitados. → método em [[../Praticas/06-Caca-de-Bugs|Caça de Bugs]].

Depois disso, teste de estresse com volume absurdo para confirmar que o site não trava.

## Problemas que este projeto gerou

- [[../Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL|SQL injection latente via token de URL]]
- [[../Problemas-Resolvidos/22-Decompression-Bomb-em-XLSX|Decompression bomb em .xlsx]]
- [[../Problemas-Resolvidos/23-Docker-Exec-no-Git-Bash-do-Windows|docker exec quebrando no Git Bash do Windows]]

## Estado

✅ Rodando via Docker · dados de exemplo carregados · auditado e corrigido · correções commitadas e enviadas.

## Perguntas de revisão

O que é o Projeto W? :: Um sistema web local que processa planilhas de vendas e estoque e gera dashboard, alertas e sugestão de compras.

Qual a stack do Projeto W? :: Python, Streamlit, Pandas, Plotly e Docker.

Como o Projeto W lida com nomes de colunas diferentes? :: Tenta identificar sozinho e, se falhar, abre uma etapa de mapeamento manual.

Quais achados de segurança a auditoria do Projeto W encontrou? :: Uma SQL injection latente via token de URL e uma decompression bomb em upload de .xlsx.
