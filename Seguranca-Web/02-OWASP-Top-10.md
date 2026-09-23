---
tags: [seguranca, web, owasp, flashcards]
aliases: [OWASP Top 10, Top 10 OWASP]
cssclasses: [cerebro-nota, cerebro-seguranca]
verificado_em: 2026-09-23
fonte: https://owasp.org/Top10/2025/
---

# OWASP Top 10:2025

A **OWASP** (Open Worldwide Application Security Project) é uma fundação sem fins lucrativos que publica guias abertos de segurança de software. O **Top 10** é o documento de conscientização mais conhecido da área: a lista dos riscos mais críticos em aplicações web, montada com dados de testes em milhares de aplicações e com uma pesquisa com profissionais.

A edição atual é a **2025**, a oitava da série (conferido em 23/09/2026).

## A lista

| # | Categoria | Em uma frase | Onde a trilha trata |
|---|---|---|---|
| A01 | **Broken Access Control** — controle de acesso quebrado | o usuário consegue ver ou mudar o que não é dele | [[08-Controle-de-Acesso\|controle de acesso]], [[13-SSRF-Uploads-e-Caminhos\|SSRF]] |
| A02 | **Security Misconfiguration** — configuração insegura | debug ligado, senha padrão, porta aberta, erro detalhado | [[15-Segredos-e-Configuracao-Segura\|configuração]], [[14-Cabecalhos-de-Seguranca\|cabeçalhos]] |
| A03 | **Software Supply Chain Failures** — falhas na cadeia de suprimentos | dependência vulnerável ou maliciosa, build comprometido | [[16-Dependencias-e-Cadeia-de-Suprimentos\|dependências]] |
| A04 | **Cryptographic Failures** — falhas de criptografia | dado sensível sem criptografia, algoritmo fraco, senha com hash rápido | [[03-HTTPS-e-TLS\|HTTPS]], [[04-Armazenamento-de-Senhas\|senhas]] |
| A05 | **Injection** — injeção | dado do usuário vira comando: SQL, shell, XSS | [[09-Injecao-SQL-e-Comandos\|injeção]], [[10-XSS-e-CSP\|XSS]] |
| A06 | **Insecure Design** — design inseguro | a falha está na regra, não no código: não havia defesa prevista | [[01-Principios-e-Modelo-de-Ameacas\|modelo de ameaças]] |
| A07 | **Authentication Failures** — falhas de autenticação | senha fraca aceita, sem limite de tentativas, sessão que não expira | [[05-Autenticacao-Sessoes-e-MFA\|autenticação]], [[06-JWT-e-Tokens\|tokens]] |
| A08 | **Software or Data Integrity Failures** — falhas de integridade | confiar em código ou dado sem verificar a origem | [[16-Dependencias-e-Cadeia-de-Suprimentos\|integridade]], [[13-SSRF-Uploads-e-Caminhos\|desserialização]] |
| A09 | **Security Logging and Alerting Failures** — falhas de log e alerta | ninguém percebe o ataque, ou percebe tarde | [[17-Logs-Monitoramento-e-Incidentes\|logs e incidentes]] |
| A10 | **Mishandling of Exceptional Conditions** — tratamento ruim de exceções | erro que vaza detalhes, falha que libera acesso, estado inconsistente | [[17-Logs-Monitoramento-e-Incidentes\|erros]] |

## O que mudou em relação a 2021

- **Controle de acesso continua em 1º.** Segundo a OWASP, em média 3,73% das aplicações testadas tinham pelo menos uma das 40 fraquezas da categoria.
- **SSRF foi incorporado ao A01.** Em 2021 era uma categoria própria (A10).
- **Configuração insegura subiu do 5º para o 2º lugar**, porque cada vez mais comportamento depende de configuração.
- **A03 é novo no formato:** amplia o antigo "componentes vulneráveis e desatualizados" para toda a cadeia (dependências, sistema de build, distribuição). Tem poucas ocorrências nos dados, mas o maior impacto médio.
- **Criptografia caiu do 2º para o 4º** e **injeção do 3º para o 5º**. XSS continua dentro de injeção.
- **A10 é nova:** erros mal tratados, lógica que "falha aberta" e condições anormais.
- **A09 mudou de nome** para destacar o **alerta**: log sem alguém avisado vale pouco.

## Como usar o Top 10

- **Como lista de estudo e de revisão de código**, não como checklist completo. O próprio documento se define como material de conscientização.
- **Para verificação formal**, a OWASP mantém o **ASVS** (Application Security Verification Standard), com requisitos testáveis por nível.
- **Para "como fazer"**, os [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) têm receitas curtas por assunto (senhas, sessões, XSS, CSRF...). Várias notas desta trilha seguem esses guias.

## Leitura rápida por tipo de sistema

| Sistema | Riscos que mais aparecem |
|---|---|
| Sistema interno com login (estoque, vendas) | A01, A07, A02 (debug ligado), A05 (SQL montado com texto) |
| Loja virtual | A01 (pedido de outro cliente), A04, A07, A03 (plugins e apps) |
| API para app mobile | A01 (IDOR), A07 (tokens), A02 (CORS aberto) |
| Painel com upload de planilha | A05, A01 (SSRF, caminhos), A10 (arquivo malformado) |

## Perguntas de revisão

O que é o OWASP Top 10? :: Um documento de conscientização da OWASP com os dez riscos mais críticos em aplicações web, baseado em dados de testes e em pesquisa com profissionais.

Qual é o risco número 1 do OWASP Top 10:2025? :: A01 Broken Access Control, controle de acesso quebrado: o usuário consegue ver ou alterar o que não deveria.

Quais são as duas categorias novas do Top 10:2025? :: A03 Software Supply Chain Failures (falhas na cadeia de suprimentos) e A10 Mishandling of Exceptional Conditions (tratamento ruim de condições excepcionais).

Para onde foi o SSRF no Top 10:2025? :: Foi incorporado ao A01, controle de acesso quebrado.

Qual categoria mais subiu no Top 10:2025? :: Security Misconfiguration, configuração insegura, que foi do 5º para o 2º lugar.

Em qual categoria do Top 10 está o XSS? :: Em A05 Injection, junto com SQL injection e injeção de comandos.

O Top 10 serve como checklist completo de segurança? :: Não; é material de conscientização. Para verificação formal existe o OWASP ASVS, e para receitas práticas os OWASP Cheat Sheets.

Qual a diferença entre Insecure Design e um bug de implementação? :: No design inseguro a defesa nem foi prevista na regra do sistema; no bug de implementação a defesa foi prevista mas foi codificada errado.

---
Anterior: [[01-Principios-e-Modelo-de-Ameacas|Princípios]] · Próxima: [[03-HTTPS-e-TLS|HTTPS e TLS]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
