<?php

// Usa SQLite: não precisa de servidor, só do arquivo banco.db (criado automaticamente)
$pdo = new PDO("sqlite:" . __DIR__ . "/banco.db");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$pdo->exec("DROP TABLE IF EXISTS tarefas");
$pdo->exec("CREATE TABLE tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT,
    concluida INTEGER DEFAULT 0
)");

$stmt = $pdo->prepare("INSERT INTO tarefas (descricao, concluida) VALUES (?, ?)");
$stmt->execute(["Estudar PHP", 1]);
$stmt->execute(["Estudar SQLite", 0]);
$stmt->execute(["Revisar anotações", 0]);

$stmt = $pdo->prepare("SELECT * FROM tarefas WHERE concluida = ?");
$stmt->execute([0]);
$pendentes = $stmt->fetchAll(PDO::FETCH_ASSOC);

echo "Tarefas pendentes:\n";
foreach ($pendentes as $tarefa) {
    echo "- {$tarefa['descricao']}\n";
}
