---
tags: [tecnologia, python, streamlit, dados]
cssclasses: [cerebro-nota, cerebro-python]
---

# Streamlit — dashboard em Python puro

Framework para transformar script Python em aplicação web de dados, sem front-end. Usado no [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]] junto com Pandas e Plotly.

## Por que foi a escolha certa ali

O requisito era explícito: *sistema simples, leve, rodando localmente por Docker, evitando arquitetura complexa*. Streamlit entrega upload de arquivo, tabela, gráfico e filtro com poucas linhas — e o custo de manutenção é baixo porque não há camada de front separada.

## A armadilha de segurança que ele introduz

**Parâmetros de URL são entrada do usuário.**

```python
token = st.query_params.get("s")     # vem da URL, é entrada hostil
```

No Projeto W esse token era usado para montar o nome de uma tabela SQL, o que criou uma injeção latente. → [[../Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL|caso real]]

> [!seguranca] Fácil de esquecer
> Como Streamlit parece um script local, é natural tratar `query_params` como configuração. Ele é tão externo quanto um campo de formulário.

## Upload de arquivo pede limite depois da descompressão

Limitar o tamanho do arquivo enviado não protege contra um `.xlsx` pequeno que se expande para gigabytes ao ser lido. → [[../Problemas-Resolvidos/22-Decompression-Bomb-em-XLSX|caso real]]

## Padrão de arquitetura que funcionou

```
app/
├── main.py, state.py, config.py
├── core/     loaders · cleaning · mapping · schema · pipeline
│             sales · inventory · purchasing · forecast · exporters
├── data/     repository.py
└── ui/       components · theme · pages
```

Manter o **cálculo em `core/`** e o Streamlit apenas em `ui/` permitiu testar a lógica sem subir a interface — inclusive rodando testes de estresse direto nas funções.

## Detalhe de produto que vale copiar

O app **declara que os números são estimativas, não garantias**, e recomenda validação humana. Em qualquer sistema que faz previsão, dizer isso na tela evita que o usuário tome a saída como certeza.

## Links relacionados

- Projeto: [[../Projetos/07-Projeto-W-Analise-de-Vendas|Projeto W]]
- Tecnologia: [[04-Docker|Docker]]
- Mapa: [[../Mapas/02-Mapa-Dados|Mapa de Dados]]
