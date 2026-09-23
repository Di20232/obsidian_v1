USE biblioteca;

CREATE TABLE IF NOT EXISTS contas (
    id INT PRIMARY KEY,
    titular VARCHAR(100),
    saldo DECIMAL(10,2)
);

INSERT INTO contas VALUES (1, 'Diego', 500.00), (2, 'Ana', 200.00);

-- Transação: transferência atômica
START TRANSACTION;
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;

SELECT * FROM contas;

-- Exemplo de rollback (desfazendo uma mudança de teste)
START TRANSACTION;
UPDATE contas SET saldo = 0 WHERE id = 1;
SELECT * FROM contas; -- mostraria saldo 0 aqui dentro da transação
ROLLBACK;
SELECT * FROM contas; -- saldo volta ao valor anterior

-- Usuário com permissões restritas
CREATE USER IF NOT EXISTS 'app_biblioteca'@'localhost' IDENTIFIED BY 'senha_forte_aqui';
GRANT SELECT, INSERT ON biblioteca.* TO 'app_biblioteca'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'app_biblioteca'@'localhost';
