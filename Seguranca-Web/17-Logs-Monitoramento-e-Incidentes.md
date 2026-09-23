---
tags: [seguranca, web, logs, monitoramento, incidentes, lgpd, flashcards]
aliases: [Resposta a Incidentes, Comunicação de Incidente ANPD]
cssclasses: [cerebro-nota, cerebro-seguranca]
verificado_em: 2026-09-23
fonte: Resolução CD/ANPD nº 15/2024 (Regulamento de Comunicação de Incidente de Segurança)
---

# Logs, monitoramento e incidentes

Nenhuma defesa é perfeita. A diferença entre um incidente pequeno e um desastre costuma ser **quanto tempo** levou para alguém perceber. O A09 do [[02-OWASP-Top-10|OWASP Top 10:2025]] mudou de nome justamente para destacar o **alerta**: log que ninguém olha vale pouco.

## O que registrar

| Evento | Por quê |
|---|---|
| Login com sucesso e com falha, logout | detectar tentativas em massa e acessos estranhos |
| Bloqueio por excesso de tentativas | sinal de ataque em andamento |
| Acesso negado (403/404 em recurso de outro usuário) | alguém testando [[08-Controle-de-Acesso\|IDs de outros]] |
| Troca de senha, e-mail, MFA; recuperação de senha | caminhos de tomada de conta |
| Ações administrativas: criar usuário, mudar papel, apagar dados, mudar preço | rastrear quem fez o quê (não repúdio) |
| Falhas de validação em volume incomum | varredura automatizada |
| Erros 500 | bugs e tentativas de exploração |
| Uso de chaves de API e webhooks recebidos | detectar chave vazada |

Cada registro com: **data e hora (UTC ou com fuso)**, usuário, IP, rota/ação, resultado e um identificador de requisição.

## O que **nunca** registrar

- Senhas (inclusive as **erradas** — muitas vezes é a senha certa com um erro de digitação, ou a senha de outro site).
- Tokens, cookies de sessão, chaves de API, códigos de MFA, links de recuperação.
- Número de cartão, CVV.
- Dados pessoais além do necessário (CPF completo, endereço, dados de saúde). Se precisar, mascare: `***.456.789-**`.

Cuidado com logs automáticos: registrar "o corpo inteiro da requisição" leva a senha junto.

## Log bom é estruturado e centralizado

```python
logger.warning("login_falhou", extra={"usuario": email_mascarado, "ip": ip, "req": req_id})
```

- **Estruturado** (JSON ou chave=valor) para dar para filtrar e contar.
- **Centralizado** fora do servidor da aplicação — quem invade o servidor não pode apagar o próprio rastro.
- **Retenção definida**: guardar o bastante para investigar, e não para sempre (dado pessoal no log também está sujeito à LGPD).
- **Relógios sincronizados** entre os servidores, senão a linha do tempo não fecha.

## Alertas que valem a pena

Poucos e acionáveis, para ninguém se acostumar a ignorar:

- Pico de logins com falha (por conta ou por IP).
- Login de administrador de país ou horário incomum.
- Muitas respostas 403/404 do mesmo usuário em sequência.
- Pico de erros 500 depois de um deploy.
- Uso de uma chave de API a partir de um IP novo.
- Mudança de papel para administrador.

## Resposta a incidentes

As fases clássicas:

1. **Preparação** — saber antes quem decide, quem comunica, onde estão os backups e os contatos (hospedagem, provedor de pagamento, contador, advogado).
2. **Detecção e análise** — confirmar o que aconteceu, desde quando, quais dados e quantas pessoas.
3. **Contenção** — tirar do ar a parte afetada, revogar chaves, encerrar sessões, trocar senhas.
4. **Erradicação** — corrigir a causa (a falha, a conta invadida, a dependência maliciosa).
5. **Recuperação** — voltar ao normal, se preciso a partir de backup, e vigiar de perto.
6. **Lições aprendidas** — registrar o que houve e o que muda, no formato de [[Cerebro/Problemas-Resolvidos/00-Indice|problema resolvido]].

**Preserve as evidências** (logs, cópia do servidor) antes de apagar e reinstalar tudo.

## LGPD: comunicar à ANPD e aos titulares

Conferido em 23/09/2026 na Resolução CD/ANPD nº 15/2024:

- O controlador deve comunicar **à ANPD** e **aos titulares** o incidente que possa causar **risco ou dano relevante** em até **3 dias úteis**, contados de quando soube que o incidente afetou dados pessoais (salvo prazo diferente em lei específica).
- É considerado relevante quando pode afetar significativamente direitos dos titulares **e** envolve pelo menos um destes: dados sensíveis; dados de crianças, adolescentes ou idosos; **dados financeiros**; **dados de autenticação em sistemas**; dados protegidos por sigilo; ou dados em larga escala.
- **Todo incidente**, comunicado ou não, precisa ser **registrado** e o registro guardado por **no mínimo 5 anos**, com data, circunstâncias, dados afetados, número de titulares, avaliação de risco, medidas e o motivo de não ter comunicado, se for o caso.

Para uma loja virtual, um vazamento da tabela de clientes com senhas ou dados de pagamento entra quase sempre no critério. Decida com apoio jurídico. → [[Ecommerce/11-Fiscal-e-Legal|LGPD na loja]]

## Backups: a última linha de defesa

- **Regra 3-2-1:** três cópias, em dois tipos de armazenamento, uma fora do local (e de preferência uma que não possa ser apagada pela mesma credencial — contra ransomware).
- **Teste a restauração.** Backup que nunca foi restaurado é uma hipótese.
- Backups contêm os mesmos dados pessoais do sistema: criptografe e restrinja o acesso.

## Perguntas de revisão

Que eventos de segurança uma aplicação deve registrar? :: Logins com sucesso e falha, bloqueios, acessos negados, trocas de senha, e-mail e MFA, ações administrativas, picos de validação falha, erros 500 e uso de chaves de API.

O que nunca deve aparecer em logs? :: Senhas (inclusive erradas), tokens, cookies de sessão, chaves de API, códigos de MFA, links de recuperação, dados de cartão e dados pessoais além do necessário.

Por que centralizar logs fora do servidor da aplicação? :: Para que quem invadir o servidor não consiga apagar o próprio rastro, e para permitir busca e alerta.

Por que o A09 do Top 10:2025 destaca o alerta? :: Porque log sem ninguém avisado não permite reagir a tempo; o valor está em perceber o incidente cedo.

Quais são as fases da resposta a incidentes? :: Preparação, detecção e análise, contenção, erradicação, recuperação e lições aprendidas.

Qual o prazo para comunicar um incidente relevante à ANPD e aos titulares? :: Três dias úteis, contados de quando o controlador soube que o incidente afetou dados pessoais.

Quando um incidente é considerado de risco ou dano relevante pela ANPD? :: Quando pode afetar significativamente direitos dos titulares e envolve dados sensíveis, de crianças, adolescentes ou idosos, financeiros, de autenticação, sigilosos ou em larga escala.

Por quanto tempo guardar o registro de incidentes de segurança? :: No mínimo cinco anos, inclusive dos incidentes que não foram comunicados.

O que é a regra 3-2-1 de backup? :: Três cópias, em dois tipos de armazenamento, com uma fora do local.

Por que preservar evidências antes de reinstalar um servidor invadido? :: Porque os logs e a cópia do servidor mostram como o ataque aconteceu e quais dados foram afetados, o que é necessário para corrigir e comunicar.

---
Anterior: [[16-Dependencias-e-Cadeia-de-Suprimentos|Dependências]] · Próxima: [[18-Checklist-de-Seguranca-Web|Checklist]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
