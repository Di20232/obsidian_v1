---
tags: [seguranca, web, principios, modelagem-de-ameacas, flashcards]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# Princípios e modelo de ameaças

Antes de qualquer técnica, segurança é um jeito de pensar: **o que eu preciso proteger, de quem, e o que acontece se falhar?** Sem essa pergunta, a equipe gasta energia em defesas bonitas e deixa a porta dos fundos aberta.

## O que se protege: a tríade CIA

| Propriedade | Significado | Exemplo de falha |
|---|---|---|
| **Confidencialidade** | só quem deve vê o dado | lista de clientes exposta numa URL sem login |
| **Integridade** | o dado não é alterado sem autorização | cliente muda o preço do produto no JSON do carrinho |
| **Disponibilidade** | o sistema funciona quando precisa | login derrubado por excesso de tentativas automáticas |

Duas propriedades costumam completar a lista:

- **Autenticidade** — ter certeza de quem fez a ação.
- **Não repúdio** — a pessoa não consegue negar depois que fez. Depende de registro confiável (→ [[17-Logs-Monitoramento-e-Incidentes|logs]]).

## Os princípios que evitam a maioria dos erros

| Princípio | Na prática |
|---|---|
| **Menor privilégio** | o usuário do banco da aplicação não pode apagar tabelas; o token da API só lê o que precisa; o funcionário do caixa não vê o financeiro |
| **Defesa em profundidade** | consulta parametrizada **e** usuário de banco restrito **e** validação de entrada **e** log. Uma camada falha, as outras seguram |
| **Negar por padrão** | toda rota exige login, a não ser as que foram liberadas de propósito — nunca o contrário |
| **Falhar fechado** | se a checagem de permissão der erro, a resposta é "acesso negado", não "deixa passar" |
| **Seguro por padrão** | a configuração que vem de fábrica é a segura; o inseguro exige mudança consciente |
| **Minimização** | não coletar, não guardar e não mostrar dado que não é necessário. Dado que não existe não vaza |
| **Não confiar no cliente** | preço, desconto, papel do usuário e ID do dono vêm do servidor, nunca do formulário |
| **Simplicidade** | cada caminho extra (rota esquecida, painel de teste, flag de debug) é uma superfície de ataque |

## Superfície de ataque e fronteira de confiança

- **Superfície de ataque** é tudo por onde um dado externo entra: rotas HTTP, formulários, parâmetros de URL, cabeçalhos, cookies, uploads, webhooks, filas, e-mails processados, arquivos importados.
- **Fronteira de confiança** é o ponto em que o dado passa de "não confiável" para "confiável". Toda checagem precisa acontecer **ali**, no servidor.

> [!example] O caso real
> No [[Cerebro/Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL|Projeto W]], um parâmetro de URL era tratado como se fosse interno. A fronteira de confiança estava no lugar errado.

## Modelagem de ameaças em quatro perguntas

Não precisa de ferramenta nem de reunião longa. Para cada funcionalidade nova, responda:

1. **O que estamos construindo?** Desenhe o fluxo: quem envia o quê, para onde, e onde o dado fica guardado.
2. **O que pode dar errado?** Use o STRIDE abaixo como lista de lembrete.
3. **O que vamos fazer a respeito?** Para cada ameaça: corrigir, reduzir, aceitar (com registro) ou transferir.
4. **Fizemos um bom trabalho?** Revise depois de pronto: as defesas foram implementadas e testadas?

### STRIDE: seis tipos de ameaça

| Letra | Ameaça | Propriedade violada | Exemplo |
|---|---|---|---|
| **S** — Spoofing | se passar por outro | autenticidade | login com senha vazada de outro site |
| **T** — Tampering | adulterar dado | integridade | alterar `preco` no corpo da requisição |
| **R** — Repudiation | negar que fez | não repúdio | administrador apaga pedido e não há log |
| **I** — Information disclosure | vazar informação | confidencialidade | mensagem de erro mostra o SQL e o caminho do servidor |
| **D** — Denial of service | derrubar o serviço | disponibilidade | upload de 2 GB trava o servidor |
| **E** — Elevation of privilege | ganhar poder indevido | autorização | usuário comum envia `"papel": "admin"` no cadastro |

### Exemplo: tela de login do Mercadinho

| Ameaça | Resposta |
|---|---|
| S: tentativas automáticas com senhas vazadas | limite de tentativas, bloqueio de senhas comuns, MFA para administrador |
| I: a mensagem diz "usuário não existe" | mensagem única: "usuário ou senha inválidos" |
| I: senhas legíveis se o banco vazar | hash lento com salt ([[04-Armazenamento-de-Senhas|Argon2id]]) |
| R: ninguém sabe quem entrou | log de login com data, usuário e IP |
| D: robô faz milhares de requisições | limite por IP e atraso progressivo |

## Risco = probabilidade × impacto

Não dá para corrigir tudo de uma vez. Priorize pelo que é **provável** e **caro**:

- Alta probabilidade, alto impacto (rota de pedidos sem checagem de dono): corrigir já.
- Baixa probabilidade, alto impacto (vazamento do backup): reduzir (criptografar, restringir acesso).
- Alta probabilidade, baixo impacto (spam no formulário de contato): tratar quando der.
- Baixa e baixo: registrar e aceitar conscientemente.

## Perguntas de revisão

O que é a tríade CIA? :: Confidencialidade (só quem deve vê), integridade (o dado não é alterado sem autorização) e disponibilidade (o sistema funciona quando precisa).

O que é o princípio do menor privilégio? :: Cada usuário, serviço ou chave recebe só as permissões mínimas necessárias para a sua função.

O que é defesa em profundidade? :: Ter várias camadas de proteção independentes, de modo que a falha de uma não baste para o ataque dar certo.

O que significa falhar fechado? :: Se uma checagem de segurança der erro, o sistema nega o acesso em vez de liberar.

O que é superfície de ataque? :: Todos os pontos por onde dados externos entram no sistema: rotas, formulários, URL, cabeçalhos, cookies, uploads, webhooks e arquivos importados.

Quais são as quatro perguntas da modelagem de ameaças? :: O que estamos construindo? O que pode dar errado? O que vamos fazer a respeito? Fizemos um bom trabalho?

O que significa cada letra do STRIDE? :: Spoofing (se passar por outro), Tampering (adulterar), Repudiation (negar a ação), Information disclosure (vazar), Denial of service (derrubar) e Elevation of privilege (ganhar poder indevido).

Por que a minimização de dados é uma defesa? :: Porque dado que não é coletado nem guardado não pode vazar.

Como priorizar riscos de segurança? :: Por probabilidade vezes impacto: corrigir primeiro o que é provável e caro, e aceitar conscientemente o que é improvável e barato.

---
Próxima: [[02-OWASP-Top-10|OWASP Top 10:2025]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
