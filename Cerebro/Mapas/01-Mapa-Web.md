---
tags: [moc, web, frontend, backend]
aliases: [Mapa Web]
cssclasses: [cerebro-nota, cerebro-web]
---

# 🌐 Mapa de Desenvolvimento Web

Uma aplicação web é uma conversa entre quem usa o produto, o navegador, o servidor e os dados.

```text
Pessoa → navegador → HTML/CSS/JavaScript → HTTP/API → servidor → banco de dados
```

## Interface (front-end)

- [[../../Programacao-Geral/07-HTML-e-CSS|HTML e CSS]] — estrutura e apresentação
- [[../../CSS/00-Indice|CSS]] — layout, responsividade e acessibilidade visual
- [[../../JavaScript/00-Indice|JavaScript]] — comportamento e interação
- [[../../Bootstrap/00-Indice|Bootstrap]] — componentes prontos
- [[../../TailwindCSS/00-Indice|Tailwind CSS]] — estilização por utilitários

**Critérios de qualidade:** semântica, acesso por teclado, contraste, carregamento rápido, feedback claro e boa experiência em telas pequenas.

## Servidor (back-end)

- recebe requisições, valida dados e aplica regras de negócio;
- conversa com bancos de dados e serviços externos;
- devolve páginas ou dados em formatos como JSON;
- autentica pessoas e autoriza ações.

Veja: [[../../PHP/00-Indice|PHP]], [[../../Programacao-Geral/10-Como-a-Web-Funciona|Como a web funciona]] e [[02-Mapa-Dados|Dados]].

## APIs e HTTP

| Ideia | Pergunta útil |
|---|---|
| rota/endpoint | qual endereço representa este recurso? |
| método HTTP | estou lendo, criando, alterando ou removendo? |
| status | a resposta explica se deu certo e por quê? |
| validação | dados inválidos são recusados antes de alterar algo? |
| contrato | outra aplicação consegue integrar sem adivinhar? |

## Publicação

Antes de publicar, confirme ambiente, variáveis secretas, migrações, backups, logs e uma forma simples de desfazer uma versão ruim. Veja [[03-Mapa-Engenharia|Engenharia de Software]].

Para testar uma página localmente com `fetch` e módulos JavaScript, veja [[../Guias/06-Servidor-Local-para-HTML|Servidor local para HTML]].
