---
tags: [seguranca, web, checklist, flashcards]
aliases: [Checklist de Segurança]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# Checklist de segurança web

Tudo da trilha num lugar, na ordem em que aparece num projeto. Não é preciso cumprir 100% antes de publicar um protótipo, mas cada item deixado de fora deve ser uma **decisão consciente**, registrada.

## Antes de codar

- [ ] Desenhei o fluxo e respondi às [[01-Principios-e-Modelo-de-Ameacas|quatro perguntas]] da modelagem de ameaças.
- [ ] Sei quais dados pessoais o sistema guarda e por quê (minimização).
- [ ] Defini os papéis e quem pode ver e fazer o quê.
- [ ] Escolhi framework e bibliotecas maduras para login, sessão e acesso ao banco.

## Ao codar

**Identidade**
- [ ] Senhas com [[04-Armazenamento-de-Senhas|Argon2id ou bcrypt]], nunca hash rápido.
- [ ] Senha mínima de 15 caracteres (ou 8 com MFA), sem regras de composição, com lista de bloqueio. → [[05-Autenticacao-Sessoes-e-MFA|NIST]]
- [ ] Limite de tentativas de login e mensagem única de erro.
- [ ] Recuperação de senha com token aleatório, guardado como hash, curto e de uso único.
- [ ] Novo ID de sessão após o login; logout invalida no servidor.
- [ ] MFA disponível, e obrigatório para administradores.
- [ ] Se usar JWT: algoritmo fixo, `exp` curto, `aud` e `iss` conferidos. → [[06-JWT-e-Tokens|JWT]]
- [ ] Se usar login social: authorization code + PKCE, `state`, ID token validado. → [[07-OAuth-e-OpenID-Connect|OAuth]]

**Acesso**
- [ ] Toda rota nega por padrão; checagem no servidor.
- [ ] Toda consulta de dado de usuário filtra pelo dono (sem IDOR). → [[08-Controle-de-Acesso|controle de acesso]]
- [ ] Lista de campos permitidos em cada formulário/API (sem mass assignment).
- [ ] Preço, desconto e papel vêm do servidor.

**Entrada e saída**
- [ ] Todas as consultas SQL parametrizadas; nomes de tabela/coluna por allowlist. → [[09-Injecao-SQL-e-Comandos|injeção]]
- [ ] Nenhum `shell=True`, `exec`, `eval` ou `render_template_string` com dado do usuário.
- [ ] Nenhum `|safe`, `innerHTML`, `dangerouslySetInnerHTML` ou `unsafe_allow_html` com dado do usuário sem sanitização. → [[10-XSS-e-CSP|XSS]]
- [ ] Token CSRF em formulários; nenhum GET muda estado. → [[11-CSRF-e-Cookies|CSRF]]
- [ ] Uploads com limite de tamanho, tipo conferido pelo conteúdo, nome gerado, fora da pasta pública. → [[13-SSRF-Uploads-e-Caminhos|uploads]]
- [ ] URLs buscadas pelo servidor passam por allowlist ou checagem de IP (SSRF).
- [ ] Exportação de CSV/XLSX protegida contra injeção de fórmula.

**Erros**
- [ ] Mensagens genéricas ao usuário, detalhes só no log.
- [ ] Checagens de segurança falham fechado.
- [ ] Operações que precisam acontecer juntas usam transação.

## Antes de publicar

- [ ] HTTPS com renovação automática, redirecionamento de HTTP e HSTS. → [[03-HTTPS-e-TLS|HTTPS]]
- [ ] Cookies com `Secure`, `HttpOnly` e `SameSite`.
- [ ] Cabeçalhos: CSP, `nosniff`, `Referrer-Policy`, `frame-ancestors`. → [[14-Cabecalhos-de-Seguranca|cabeçalhos]]
- [ ] CORS com lista fechada de origens, se houver. → [[12-CORS|CORS]]
- [ ] Modo debug **desligado**; sem senhas padrão; sem rotas de teste. → [[15-Segredos-e-Configuracao-Segura|configuração]]
- [ ] Nenhum segredo no repositório nem no frontend; `.env` no `.gitignore`; secret scanning ativo.
- [ ] Banco, Redis e painéis não acessíveis pela internet.
- [ ] Usuário do banco com menor privilégio.
- [ ] `npm audit` / `pip-audit` sem pendências críticas; lockfile versionado. → [[16-Dependencias-e-Cadeia-de-Suprimentos|dependências]]
- [ ] Logs de segurança ligados, sem dados sensíveis, e pelo menos um alerta configurado. → [[17-Logs-Monitoramento-e-Incidentes|logs]]
- [ ] Backup automático **com restauração testada**.
- [ ] Política de privacidade coerente com os dados que o sistema realmente coleta.

## Depois de publicar (rotina)

| Frequência | Tarefa |
|---|---|
| Semanal | olhar alertas e picos nos logs; aplicar atualizações de segurança do Dependabot |
| Mensal | auditar dependências; revisar usuários administradores e chaves de API ativas; testar um backup |
| A cada funcionalidade nova | repetir a modelagem de ameaças; testes de acesso com dois usuários |
| Anual | revisar esta checklist inteira; trocar segredos antigos; ensaiar a resposta a incidente |

## Como testar o próprio sistema

- **Testes automatizados de segurança** junto com os outros: usuário A tentando acessar dados de B, rota de admin com usuário comum, entrada com `'`, `<script>` e `../`.
- **Revisão de código** com esta checklist ao lado.
- **Scanner automático** (o OWASP ZAP é gratuito) contra um ambiente de teste — **só em sistemas seus ou com autorização por escrito**.
- **Análise estática** no CI: Bandit (Python), ESLint com regras de segurança, CodeQL no GitHub.

## Perguntas de revisão

Quais são os três itens mais importantes de identidade antes de publicar? :: Senhas com hash lento (Argon2id ou bcrypt), limite de tentativas de login e sessão renovada após o login e invalidada no logout.

Qual a checagem mais importante de controle de acesso? :: Filtrar toda consulta pelo dono do dado no servidor, evitando IDOR.

Que itens de configuração conferir antes de publicar? :: HTTPS com HSTS, cookies seguros, cabeçalhos de segurança, debug desligado, sem senhas padrão, sem segredos no repositório e banco fora da internet.

O que revisar todo mês num sistema publicado? :: Auditoria de dependências, lista de administradores e chaves de API ativas, e um teste de restauração de backup.

Que entradas simples usar em testes automatizados de segurança? :: Aspas simples, script HTML e ../ nos campos, além de tentar acessar dados de outro usuário e rotas de admin com usuário comum.

Em quais sistemas é permitido rodar um scanner como o OWASP ZAP? :: Só nos seus próprios sistemas ou com autorização por escrito do dono.

Um item da checklist pode ficar de fora de um protótipo? :: Pode, desde que seja uma decisão consciente e registrada, não um esquecimento.

---
Anterior: [[17-Logs-Monitoramento-e-Incidentes|Logs e incidentes]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
