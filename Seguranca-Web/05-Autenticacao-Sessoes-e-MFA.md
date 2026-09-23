---
tags: [seguranca, web, autenticacao, sessoes, mfa, flashcards]
cssclasses: [cerebro-nota, cerebro-seguranca]
verificado_em: 2026-09-23
fonte: https://pages.nist.gov/800-63-4/sp800-63b.html
---

# Autenticação, sessões e MFA

**Autenticação** responde "quem é você?". **Sessão** é como o sistema lembra a resposta nas requisições seguintes. As duas precisam estar certas: um login perfeito não adianta se o identificador da sessão pode ser adivinhado ou roubado.

## Regras de senha do NIST (SP 800-63B-4, agosto de 2025)

O NIST é o instituto de padrões dos Estados Unidos; as regras dele viraram referência mundial e **contrariam vários hábitos antigos**:

| Regra | O que diz |
|---|---|
| Tamanho mínimo | **15 caracteres** quando a senha é o único fator; **8** quando faz parte de autenticação multifator |
| Tamanho máximo | aceitar **pelo menos 64** caracteres |
| Caracteres | aceitar todos os ASCII imprimíveis, espaço e Unicode |
| Regras de composição | **proibido** exigir "maiúscula, número e símbolo" |
| Troca periódica | **proibido** obrigar a trocar de tempos em tempos; troca só com indício de vazamento |
| Lista de bloqueio | **obrigatório** recusar senhas comuns, vazadas, palavras de dicionário e derivadas do nome do serviço ou do usuário, explicando o motivo |
| Dicas e perguntas secretas | **proibido** ("nome do primeiro animal") |
| Gerenciador de senhas | **obrigatório** permitir preenchimento automático; recomendado permitir colar |
| Limite de tentativas | **obrigatório**: no máximo 100 falhas seguidas por conta, com atraso crescente, desafio antirrobô ou análise de risco antes disso |

A lógica: senha longa e fora de listas de vazamento vale mais que `Senha@2026`, que cumpre todas as regras antigas e está em qualquer lista de ataque.

## O fluxo de login

- **Mensagem única para falha:** "usuário ou senha inválidos". Dizer "este e-mail não existe" permite descobrir quem tem conta (**enumeração de usuários**).
- O mesmo vale para **cadastro** e **"esqueci minha senha"**: responda "se o e-mail existir, enviaremos um link".
- **Tempo de resposta parecido** nos dois casos: se o sistema só calcula o hash quando o usuário existe, a diferença de tempo denuncia.
- **Limite de tentativas por conta e por IP**, com atraso progressivo. Isso freia o **credential stuffing** — robôs testando pares de e-mail e senha vazados de outros sites.

## Recuperação de senha

É o caminho mais atacado, porque dá acesso à conta sem saber a senha.

1. Gerar um **token aleatório longo** (ex.: `secrets.token_urlsafe(32)` em Python, `crypto.randomBytes(32)` em Node). Nunca sequencial, nunca derivado de e-mail ou data.
2. Guardar **o hash do token** no banco, não o token.
3. **Validade curta** (minutos a poucas horas) e **uso único**.
4. Ao redefinir: invalidar o token, **encerrar as outras sessões** e avisar por e-mail que a senha mudou.
5. Montar o link com o domínio configurado no servidor, **nunca** com o cabeçalho `Host` da requisição (senão o atacante faz o sistema mandar um link para o domínio dele).

## Sessões

| Cuidado | Por quê |
|---|---|
| ID de sessão aleatório e longo, gerado pelo framework | não pode ser adivinhado |
| **Gerar um novo ID após o login** | evita *session fixation*: o atacante planta um ID conhecido e espera a vítima logar com ele |
| Expirar por inatividade e por tempo máximo | sessão eterna é sessão roubável para sempre |
| Logout invalida a sessão **no servidor** | apagar só o cookie no navegador não basta |
| Cookie com `HttpOnly`, `Secure` e `SameSite` | protege contra roubo por script, envio sem HTTPS e CSRF → [[11-CSRF-e-Cookies\|cookies]] |
| Pedir a senha de novo para ações críticas | trocar e-mail, senha, dados de pagamento |

> [!tip] Sessão no servidor ou token?
> Para um sistema web tradicional (Flask, Express com páginas), **sessão no servidor com cookie** é o mais simples e seguro. [[06-JWT-e-Tokens|JWT]] resolve outros problemas — e cria alguns.

## MFA: mais de um fator

Fatores são de três tipos: **algo que você sabe** (senha), **algo que você tem** (celular, chave física) e **algo que você é** (biometria, que desbloqueia um dispositivo — sozinha, o NIST não a reconhece como autenticador).

| Método | Força | Observação |
|---|---|---|
| **Passkey / WebAuthn / chave física** | a mais alta | **resistente a phishing**: a credencial é presa ao domínio verdadeiro, então um site falso não consegue usá-la |
| **App autenticador (TOTP)** | boa | código de 6 dígitos que muda a cada 30 s; um site falso ainda pode pedir e repassar o código em tempo real |
| **SMS** | a mais fraca | o NIST classifica como autenticador **restrito**, por causa de troca de chip, portabilidade e interceptação |

Onde exigir MFA primeiro: **contas de administrador**, painel da loja, e-mail e hospedagem. Ofereça **códigos de recuperação** para quem perder o dispositivo — guardados com hash, como senhas.

## Perguntas de revisão

Qual a diferença entre autenticação e sessão? :: Autenticação confirma quem é o usuário; a sessão é o mecanismo que lembra essa identidade nas requisições seguintes.

Qual o tamanho mínimo de senha segundo o NIST SP 800-63B-4? :: 15 caracteres quando a senha é o único fator; 8 quando faz parte de autenticação multifator.

O NIST recomenda exigir maiúscula, número e símbolo na senha? :: Não; proíbe regras de composição e exige, em vez disso, comparar a senha com uma lista de senhas comuns e vazadas.

O NIST recomenda obrigar a troca periódica de senha? :: Não; a troca só deve ser exigida quando há indício de que a senha foi comprometida.

Qual o limite de tentativas de login definido pelo NIST? :: No máximo 100 falhas consecutivas por conta, com atraso crescente ou outras defesas antes disso.

O que é enumeração de usuários e como evitar? :: Descobrir quais e-mails têm conta pelas respostas do login, cadastro ou recuperação; evita-se com mensagem única e tempo de resposta parecido.

O que é credential stuffing? :: Robôs testando pares de e-mail e senha vazados de outros sites, aproveitando que as pessoas repetem senhas.

Como deve ser o token de recuperação de senha? :: Aleatório e longo, guardado como hash, com validade curta e uso único; ao usar, encerrar as outras sessões.

O que é session fixation e como evitar? :: O atacante faz a vítima logar com um ID de sessão que ele já conhece; evita-se gerando um ID novo logo após o login.

Por que passkeys são resistentes a phishing? :: Porque a credencial fica presa ao domínio verdadeiro e o navegador não a entrega a um site falso.

Por que o SMS é o fator mais fraco de MFA? :: Porque está sujeito a troca de chip, portabilidade indevida e interceptação; o NIST o classifica como autenticador restrito.

---
Anterior: [[04-Armazenamento-de-Senhas|Armazenamento de senhas]] · Próxima: [[06-JWT-e-Tokens|JWT e tokens]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
