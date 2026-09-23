---
tags: [seguranca, web, indice, moc]
aliases: [Segurança Web, Segurança de Aplicações Web]
cssclasses: [cerebro-nota, cerebro-seguranca]
verificado_em: 2026-09-23
---

# 🛡️ Segurança web

Quase todo ataque a um sistema web explora um descuido simples: uma consulta que não confere o dono do dado, uma senha guardada do jeito errado, uma chave esquecida no repositório, um campo que aceita HTML. Esta trilha cobre o que um desenvolvedor precisa saber para não cometer esses erros — com exemplos em Python (Flask), JavaScript (Node/Express) e SQL, as pilhas usadas nos projetos do cofre.

> [!warning] Teste só o que é seu
> As técnicas descritas aqui servem para **proteger** os próprios sistemas. Testar sistemas de terceiros sem autorização por escrito é crime no Brasil (Lei 12.737/2012) e em quase todo lugar.

> [!info] Fontes principais
> Onde uma nota cita um padrão, ele foi conferido em 23/09/2026: [OWASP Top 10:2025](https://owasp.org/Top10/2025/), [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/), [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html), [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) e a Resolução CD/ANPD nº 15/2024.

## Trilha

### Fundamentos
1. [[01-Principios-e-Modelo-de-Ameacas|Princípios e modelo de ameaças]] — CIA, menor privilégio, defesa em profundidade, STRIDE
2. [[02-OWASP-Top-10|OWASP Top 10:2025]] — os dez riscos mais críticos e onde cada um é tratado
3. [[03-HTTPS-e-TLS|HTTPS e TLS]] — o que o cadeado garante e o que não garante

### Identidade
4. [[04-Armazenamento-de-Senhas|Armazenamento de senhas]] — hash lento, salt, Argon2id e bcrypt
5. [[05-Autenticacao-Sessoes-e-MFA|Autenticação, sessões e MFA]] — regras do NIST, login, recuperação, passkeys
6. [[06-JWT-e-Tokens|JWT e tokens]] — como validar, onde guardar, quando não usar
7. [[07-OAuth-e-OpenID-Connect|OAuth e OpenID Connect]] — "Entrar com Google" sem furos, PKCE
8. [[08-Controle-de-Acesso|Controle de acesso]] — o risco número 1: IDOR, papéis, multiempresa

### Ataques clássicos
9. [[09-Injecao-SQL-e-Comandos|Injeção de SQL e de comandos]] — parâmetros, allowlist, subprocess
10. [[10-XSS-e-CSP|XSS e CSP]] — escapar a saída e limitar o que o navegador executa
11. [[11-CSRF-e-Cookies|CSRF e cookies]] — tokens, SameSite, HttpOnly, Secure
12. [[12-CORS|CORS]] — o que é, por que o erro aparece, como não abrir demais
13. [[13-SSRF-Uploads-e-Caminhos|SSRF, uploads e caminhos]] — quando o servidor busca, grava ou lê o que o usuário mandou

### Operação
14. [[14-Cabecalhos-de-Seguranca|Cabeçalhos de segurança]] — HSTS, CSP, nosniff e companhia
15. [[15-Segredos-e-Configuracao-Segura|Segredos e configuração segura]] — .env, vazamento, modo debug
16. [[16-Dependencias-e-Cadeia-de-Suprimentos|Dependências e cadeia de suprimentos]] — auditoria, lockfile, pacotes falsos
17. [[17-Logs-Monitoramento-e-Incidentes|Logs, monitoramento e incidentes]] — o que registrar, alertar e comunicar à ANPD
18. [[18-Checklist-de-Seguranca-Web|Checklist de segurança web]] — tudo junto, por fase do projeto

## As três ideias que atravessam a trilha

1. **Nunca confie no cliente.** Tudo que vem do navegador — formulário, URL, cabeçalho, cookie, JSON, arquivo — pode ter sido forjado. A validação que importa é a do servidor. → [[08-Controle-de-Acesso|controle de acesso]] · [[09-Injecao-SQL-e-Comandos|injeção]]
2. **Dado e código não se misturam.** SQL injection, XSS e injeção de comandos são o mesmo erro: texto do usuário virando instrução. A defesa é sempre separar os dois (parâmetros, escape, lista de argumentos). → [[10-XSS-e-CSP|XSS]]
3. **Camadas, não muralha.** Nenhuma defesa é perfeita; o que protege é ter várias, de modo que uma falha não seja suficiente. → [[01-Principios-e-Modelo-de-Ameacas|defesa em profundidade]]

## Onde isso encontra o resto do cofre

- [[Cerebro/Mapas/04-Mapa-Seguranca|Mapa de Segurança]] — visão geral e checklist curto
- [[Cerebro/Praticas/07-Seguranca-em-Apps-Locais|Segurança em apps locais]] — as regras que saíram das auditorias dos projetos
- Casos reais: [[Cerebro/Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL|SQL injection por token de URL]], [[Cerebro/Problemas-Resolvidos/09-Nome-de-Tabela-em-F-String-no-SQL|nome de tabela em f-string]], [[Cerebro/Problemas-Resolvidos/22-Decompression-Bomb-em-XLSX|bomba de descompressão em XLSX]], [[Cerebro/Problemas-Resolvidos/13-Acesso-Externo-ao-Localhost|acesso externo ao localhost]]
- [[IA-Aplicada/09-Riscos-Seguranca-e-LGPD-na-IA|Riscos e segurança na IA]] — injeção de prompt é o mesmo erro de misturar dado e instrução
- [[Ecommerce/07-Pagamentos-no-Brasil|Pagamentos]] e [[Ecommerce/11-Fiscal-e-Legal|LGPD na loja]] — onde uma falha vira prejuízo e processo
- [[Programacao-Geral/10-Como-a-Web-Funciona|Como a web funciona]] — HTTP, cookies e navegador, a base desta trilha
