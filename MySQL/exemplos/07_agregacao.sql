USE biblioteca;

SELECT COUNT(*) AS total_livros FROM livros;
SELECT MIN(ano_publicacao) AS mais_antigo, MAX(ano_publicacao) AS mais_recente FROM livros;

-- Empréstimos por leitor
SELECT nome_leitor, COUNT(*) AS total_emprestimos
FROM emprestimos
GROUP BY nome_leitor
ORDER BY total_emprestimos DESC;

-- Só leitores com mais de 1 empréstimo
SELECT nome_leitor, COUNT(*) AS total_emprestimos
FROM emprestimos
GROUP BY nome_leitor
HAVING total_emprestimos > 1;

-- Todos os livros com a contagem de empréstimos (0 para os nunca emprestados)
SELECT l.titulo, COUNT(e.id) AS vezes_emprestado
FROM livros l
LEFT JOIN emprestimos e ON l.id = e.livro_id
GROUP BY l.id, l.titulo
ORDER BY vezes_emprestado DESC;
