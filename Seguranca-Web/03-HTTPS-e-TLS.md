---
tags: [seguranca, web, https, tls, criptografia, flashcards]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# HTTPS e TLS

HTTPS é HTTP dentro de um canal protegido pelo **TLS** (Transport Layer Security). É a primeira camada de qualquer sistema publicado: sem ela, qualquer um no caminho — o Wi-Fi do café, o provedor, um roteador comprometido — lê e altera o que passa, inclusive senhas e cookies de sessão.

## O que o TLS garante

| Garantia | Como |
|---|---|
| **Confidencialidade** | o conteúdo é criptografado entre o navegador e o servidor |
| **Integridade** | qualquer alteração no caminho é detectada |
| **Autenticidade do servidor** | o certificado prova que o navegador está falando com o domínio certo |

## O que o TLS **não** garante

- **Que o site é honesto.** Site de golpe também tem cadeado. O cadeado diz "a conversa é privada", não "o site é confiável".
- **Que o servidor é seguro.** Os dados chegam protegidos e podem vazar de um banco mal configurado.
- **Que quem está do outro lado é quem diz ser** — o TLS comum autentica o servidor, não o usuário. Isso é trabalho do [[05-Autenticacao-Sessoes-e-MFA|login]].

## Como funciona, em alto nível

1. O navegador se conecta e diz quais versões e algoritmos aceita.
2. O servidor responde com o **certificado**: a chave pública dele, assinada por uma **autoridade certificadora (CA)** em que o navegador confia.
3. O navegador confere a assinatura, a validade e se o nome do domínio bate.
4. Os dois combinam uma **chave de sessão** temporária (troca de chaves com Diffie-Hellman efêmero, que dá *forward secrecy*: roubar a chave do servidor depois não decifra conversas antigas).
5. O resto da conversa usa criptografia simétrica rápida com essa chave.

## Configuração mínima de um site publicado

- **TLS 1.2 como mínimo, TLS 1.3 preferido.** SSL 3.0, TLS 1.0 e 1.1 estão obsoletos.
- **Certificado de uma CA pública**, renovado automaticamente. O Let's Encrypt emite de graça, e a maioria das hospedagens (Vercel, Netlify, Render, Cloudflare) já faz isso sozinha.
- **Redirecionar HTTP para HTTPS** (porta 80 → 443).
- **HSTS** para o navegador nunca mais tentar HTTP naquele domínio:

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

  Sem HSTS, o primeiro acesso por `http://` pode ser interceptado antes do redirecionamento. Detalhes em [[14-Cabecalhos-de-Seguranca|cabeçalhos de segurança]].
- **Cookies de sessão com `Secure`**, para nunca viajarem sem criptografia. → [[11-CSRF-e-Cookies|cookies]]
- **Sem conteúdo misto:** uma página HTTPS que carrega script por `http://` abre um buraco. Os navegadores bloqueiam a maioria dos casos, mas imagens e links quebrados aparecem.

> [!info] Validade dos certificados está diminuindo
> O CA/Browser Forum, que define as regras das autoridades certificadoras, aprovou a redução gradual da validade máxima dos certificados públicos ao longo dos próximos anos. Na prática: **renovação manual deixou de ser opção**. Automatize (ACME/Let's Encrypt ou a hospedagem).

## Erros comuns de desenvolvedor

**Desligar a verificação do certificado** para "resolver" um erro:

```python
requests.get(url, verify=False)          # ERRADO: aceita qualquer certificado, até falso
```

```js
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'   // ERRADO: desliga para o processo inteiro
```

Isso anula a autenticidade: qualquer intermediário se passa pelo servidor. Se o certificado é de uma CA interna, **aponte para ela** (`verify='/caminho/ca.pem'`) em vez de desligar.

**Achar que dentro da rede interna não precisa.** Tráfego interno também é interceptado; o princípio de "confiança zero" trata a rede interna como hostil.

**Guardar dado sensível "porque está em HTTPS".** O TLS protege **em trânsito**. Em repouso (banco, backup, disco) é outro problema: criptografia no banco ou no disco, controle de acesso e [[04-Armazenamento-de-Senhas|hash para senhas]].

## Desenvolvimento local

- `http://localhost` é tratado pelos navegadores como contexto seguro, então a maior parte das APIs funciona sem HTTPS.
- Para testar HTTPS local de verdade (cookies `Secure`, service workers em outro host), ferramentas como o **mkcert** criam uma CA local confiável só na sua máquina.
- Expor o `localhost` para outra pessoa acessar é outro assunto → [[Cerebro/Problemas-Resolvidos/13-Acesso-Externo-ao-Localhost|caso real]].

## Perguntas de revisão

Quais são as três garantias do TLS? :: Confidencialidade do conteúdo, integridade (alteração é detectada) e autenticidade do servidor por meio do certificado.

O cadeado do HTTPS significa que o site é confiável? :: Não; significa só que a conversa é privada e que o domínio é aquele. Sites de golpe também têm certificado.

O que é uma autoridade certificadora? :: Uma entidade em que o navegador confia e que assina certificados atestando que uma chave pública pertence a um domínio.

O que é forward secrecy? :: A propriedade de que roubar a chave privada do servidor no futuro não permite decifrar conversas gravadas no passado, porque cada sessão usou uma chave temporária.

Qual a versão mínima de TLS recomendada hoje? :: TLS 1.2 como mínimo e TLS 1.3 como preferido; SSL, TLS 1.0 e TLS 1.1 estão obsoletos.

Para que serve o cabeçalho HSTS? :: Para o navegador passar a usar só HTTPS naquele domínio, evitando que o primeiro acesso por HTTP seja interceptado.

Por que nunca usar verify=False no requests? :: Porque desliga a checagem do certificado e qualquer intermediário pode se passar pelo servidor; para CA interna, aponte o caminho do certificado dela.

O HTTPS protege os dados guardados no banco? :: Não; protege só em trânsito. Dados em repouso precisam de controle de acesso, criptografia no armazenamento e hash para senhas.

Por que automatizar a renovação de certificados? :: Porque a validade máxima dos certificados públicos está sendo reduzida e a renovação manual vira fonte de sites fora do ar.

---
Anterior: [[02-OWASP-Top-10|OWASP Top 10]] · Próxima: [[04-Armazenamento-de-Senhas|Armazenamento de senhas]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
