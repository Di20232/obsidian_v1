---
tags: [seguranca, web, senhas, hash, criptografia, flashcards]
cssclasses: [cerebro-nota, cerebro-seguranca]
verificado_em: 2026-09-23
fonte: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
---

# Armazenamento de senhas

A pergunta não é *se* o banco vai vazar, e sim **o que o atacante consegue fazer quando ele vazar**. Senha guardada do jeito certo continua inútil para quem roubou a tabela. Guardada do jeito errado, vira acesso à conta — e, como as pessoas repetem senha, à conta delas em outros sites.

## Hash, não criptografia

| | Criptografia | Hash |
|---|---|---|
| Direção | duas vias: quem tem a chave decifra | uma via: não existe "desfazer" |
| Uso certo | dado que precisa ser lido de novo (endereço, CPF para nota fiscal) | senha, que só precisa ser **comparada** |
| Se a chave vazar | todas as senhas saem em texto | não há chave para vazar |

Para conferir a senha no login, calcula-se o hash do que a pessoa digitou e compara-se com o hash guardado. Ninguém — nem o administrador — precisa saber a senha original. Se um sistema consegue **enviar sua senha por e-mail**, ele a guarda errado.

## Por que SHA-256 puro não serve

SHA-256, SHA-1 e MD5 são **rápidos** de propósito. Uma placa de vídeo calcula bilhões deles por segundo, o que torna viável testar listas enormes de senhas vazadas contra cada hash. Para senha, a velocidade é o defeito.

Um hash de senha precisa de três coisas:

1. **Ser lento e configurável** (fator de trabalho), para cada tentativa custar caro.
2. **Salt:** um valor aleatório, único por usuário, guardado junto com o hash. Assim, duas pessoas com a mesma senha têm hashes diferentes, e tabelas pré-calculadas (*rainbow tables*) não funcionam.
3. **Usar memória** (nos algoritmos modernos), o que dificulta ataque com hardware especializado.

## O que a OWASP recomenda (conferido em 23/09/2026)

| Ordem de preferência | Algoritmo | Configuração mínima |
|---|---|---|
| 1º | **Argon2id** | 19 MiB de memória, 2 iterações, paralelismo 1 |
| 2º (sem Argon2id) | **scrypt** | custo N = 2¹⁷, bloco r = 8, paralelismo p = 1 |
| Sistemas legados | **bcrypt** | fator de trabalho 10 ou mais; senha limitada a **72 bytes** |
| Exigência FIPS-140 | **PBKDF2** com HMAC-SHA-256 | 600.000 iterações ou mais |

Os valores são **mínimos**. Aumente enquanto o login continuar rápido o bastante no seu servidor (algo como até meio segundo é aceitável para a maioria dos sistemas).

> [!warning] O limite de 72 bytes do bcrypt
> O bcrypt ignora o que passar de 72 bytes. Em UTF-8, um caractere acentuado ocupa 2 bytes. Frases-senha longas podem ser truncadas sem aviso. É um dos motivos para preferir Argon2id em projeto novo.

## Na prática

### Python (Argon2id)

```python
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()                     # confira os parâmetros contra o mínimo da OWASP

def cadastrar(senha: str) -> str:
    return ph.hash(senha)                 # o salt é gerado e embutido no resultado

def conferir(hash_guardado: str, senha: str) -> bool:
    try:
        ph.verify(hash_guardado, senha)
        return True
    except VerifyMismatchError:
        return False
```

O resultado é uma string só, com algoritmo, parâmetros, salt e hash — algo como `$argon2id$v=19$m=...,t=...,p=...$<salt>$<hash>`. Guarde numa coluna de texto.

**No Flask**, `werkzeug.security.generate_password_hash` e `check_password_hash` já aplicam um algoritmo lento com salt; é aceitável quando não há Argon2 disponível.

### Node.js (bcrypt)

```js
import bcrypt from 'bcrypt';

const hash = await bcrypt.hash(senha, 12);        // 12 = fator de trabalho
const ok = await bcrypt.compare(senhaDigitada, hash);
```

## Atualizar hashes antigos sem pedir nova senha

Se o sistema guarda MD5 ou SHA-1:

1. No próximo login bem-sucedido, a senha digitada está disponível em texto — calcule o hash novo e substitua.
2. Para quem não entra há muito tempo, a OWASP sugere **envolver o hash antigo** no novo (`argon2(md5_antigo)`) e marcar a linha, ou forçar redefinição de senha.
3. Bibliotecas como o `argon2-cffi` têm `check_needs_rehash` para saber quando os parâmetros ficaram abaixo do atual.

## Pepper

Um **pepper** é um segredo único para todo o sistema, guardado **fora do banco** (variável de ambiente, cofre de segredos), combinado com a senha antes do hash. Se só o banco vazar, o atacante não consegue nem começar a testar senhas. É uma camada extra — nunca substitui o salt e o algoritmo lento.

## O que nunca fazer

- Guardar senha em texto puro, "criptografada" com chave reversível ou em Base64 (Base64 não é criptografia).
- Usar MD5, SHA-1 ou SHA-256 sem fator de trabalho.
- Inventar o próprio esquema ("SHA-256 duas vezes com o nome do usuário").
- Escrever a senha em **log**, em mensagem de erro ou em ferramenta de monitoramento. → [[17-Logs-Monitoramento-e-Incidentes|logs]]
- Limitar a senha a 12 ou 16 caracteres "porque a coluna é pequena": a coluna guarda o hash, que tem tamanho fixo.

## Perguntas de revisão

Por que senhas devem ser guardadas com hash e não com criptografia? :: Porque o hash é de uma via e só precisa ser comparado; a criptografia é reversível e, se a chave vazar, todas as senhas aparecem.

Por que SHA-256 puro não serve para senhas? :: Porque é rápido demais: uma placa de vídeo testa bilhões de palpites por segundo contra cada hash.

O que é salt e para que serve? :: Um valor aleatório único por usuário, guardado com o hash, que faz senhas iguais terem hashes diferentes e inutiliza tabelas pré-calculadas.

Qual algoritmo a OWASP recomenda em primeiro lugar para senhas e com qual configuração mínima? :: Argon2id com 19 MiB de memória, 2 iterações e paralelismo 1.

Qual o fator de trabalho mínimo do bcrypt segundo a OWASP? :: 10 ou mais.

Qual a limitação do bcrypt com senhas longas? :: Ele só considera os primeiros 72 bytes; o resto é ignorado sem aviso.

Quantas iterações de PBKDF2-HMAC-SHA-256 a OWASP recomenda? :: 600.000 ou mais, e só quando há exigência de conformidade FIPS-140.

O que é pepper? :: Um segredo único do sistema, guardado fora do banco, combinado com a senha antes do hash; é camada extra e não substitui o salt.

Como migrar hashes antigos sem pedir senha nova a todos? :: Recalcular com o algoritmo novo no próximo login bem-sucedido; para contas inativas, envolver o hash antigo no novo ou forçar redefinição.

Um sistema que envia sua senha atual por e-mail está guardando certo? :: Não; se ele consegue recuperar a senha original, ela não está com hash.

---
Anterior: [[03-HTTPS-e-TLS|HTTPS e TLS]] · Próxima: [[05-Autenticacao-Sessoes-e-MFA|Autenticação, sessões e MFA]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
