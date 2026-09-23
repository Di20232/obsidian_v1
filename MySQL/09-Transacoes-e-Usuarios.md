---
tags: [mysql, sql, flashcards]
cssclasses: [cerebro-nota, cerebro-mysql]
---

# Transações e Usuários

## O problema que transações resolvem

Imagine uma transferência bancária: **retirar** de uma conta e **depositar** em outra são dois comandos `UPDATE` separados. Se o programa travar (ou a conexão cair) **entre** os dois comandos, o dinheiro simplesmente desaparece — saiu de uma conta e nunca chegou na outra. Uma **transação** garante que um grupo de comandos rode **como se fosse um único comando indivisível**: ou todos são aplicados, ou nenhum é.

## `BEGIN`, `COMMIT`, `ROLLBACK`

```sql
START TRANSACTION;

UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;

COMMIT;   -- confirma as duas mudanças, tornando-as permanentes
```

Se algo der errado no meio do caminho (um erro de validação na aplicação, por exemplo), você desfaz **tudo** que foi feito desde o `START TRANSACTION`:

```sql
START TRANSACTION;

UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
-- algo deu errado aqui...
ROLLBACK;   -- desfaz TUDO desde o START TRANSACTION, como se nada tivesse acontecido
```

## As garantias ACID (o porquê, resumido)

Transações existem para garantir quatro propriedades, conhecidas pela sigla **ACID**:
- **Atomicidade**: tudo ou nada (o exemplo acima).
- **Consistência**: o banco nunca fica em um estado inválido, mesmo com falhas no meio do processo.
- **Isolamento**: transações simultâneas de usuários diferentes não interferem umas nas outras de forma inesperada.
- **Durabilidade**: depois de um `COMMIT`, o dado está salvo de verdade, mesmo que o servidor caia logo em seguida.

Você não precisa decorar a sigla — o que importa é reconhecer **quando** usar transação: sempre que uma operação de negócio envolve **mais de um comando** que precisam ser tratados como uma unidade só.

## Usando transação a partir do código (PHP/PDO)

```php
$pdo->beginTransaction();
try {
    $pdo->exec("UPDATE contas SET saldo = saldo - 100 WHERE id = 1");
    $pdo->exec("UPDATE contas SET saldo = saldo + 100 WHERE id = 2");
    $pdo->commit();
} catch (Exception $erro) {
    $pdo->rollBack();
    echo "Transferência falhou: " . $erro->getMessage();
}
```

Conecta diretamente com `try`/`catch` visto em [[../PHP/12-Tratamento-de-Erros]] — o padrão comum é: tentar, e se der erro, desfazer tudo com `rollBack()`.

## Usuários e permissões

Até aqui você usou `root`, que tem acesso total. Em produção, cada aplicação deve ter um usuário **próprio**, com **só as permissões que ela realmente precisa** — princípio chamado de **menor privilégio**, o mesmo espírito de segurança discutido em [[../Programacao-Geral/13-Boas-Praticas-de-Codigo]].

```sql
CREATE USER 'app_loja'@'localhost' IDENTIFIED BY 'senha_forte_aqui';

GRANT SELECT, INSERT, UPDATE, DELETE ON loja.* TO 'app_loja'@'localhost';

FLUSH PRIVILEGES;   -- aplica as mudanças de permissão imediatamente
```

`GRANT SELECT, INSERT, UPDATE, DELETE ON loja.*` dá acesso de CRUD (visto em [[04-CRUD-Insert-Select-Update-Delete]]) só ao banco `loja`, sem permitir apagar tabelas (`DROP`) ou criar outros usuários — se esse usuário vazar ou for comprometido, o estrago possível é bem menor do que se fosse o `root`.

```sql
SHOW GRANTS FOR 'app_loja'@'localhost';   -- confere as permissões concedidas
REVOKE DELETE ON loja.* FROM 'app_loja'@'localhost';   -- remove uma permissão específica
```

## Exercício

Crie um usuário `app_biblioteca` com permissão apenas de `SELECT` e `INSERT` no banco `biblioteca` (sem `UPDATE`/`DELETE`). Depois, pense: por que um sistema que só cadastra empréstimos (nunca edita ou apaga) se beneficiaria de um usuário com permissões tão restritas?

## Perguntas de revisão

Para que serve uma transação? :: Para que um grupo de comandos seja aplicado por inteiro ou não seja aplicado, como numa transferência bancária.

O que fazem COMMIT e ROLLBACK? :: COMMIT confirma as mudanças da transação; ROLLBACK desfaz tudo desde o início dela.

O que significa ACID? :: Atomicidade, Consistência, Isolamento e Durabilidade, as garantias das transações.

Quando usar transação? :: Sempre que uma operação de negócio envolve mais de um comando que precisam ser tratados como unidade.

O que é o princípio do menor privilégio no banco? :: Cada aplicação usa um usuário próprio só com as permissões de que precisa, nunca o root.

Como dar permissão de CRUD a um usuário num banco? :: GRANT SELECT, INSERT, UPDATE, DELETE ON banco.* TO 'usuario'@'localhost'.

---
Veja o exemplo em `MySQL/exemplos/09_transacoes_usuarios.sql`. Próxima nota: [[10-MySQL-com-PHP-e-Python]]
