USE biblioteca;

INSERT INTO emprestimos (livro_id, nome_leitor) VALUES
    (1, 'Carla'),
    (3, 'Pedro');

-- INNER JOIN: só livros que já foram emprestados
SELECT l.titulo, e.nome_leitor
FROM emprestimos e
JOIN livros l ON e.livro_id = l.id;

-- LEFT JOIN: todos os livros, emprestados ou não
SELECT l.titulo, e.nome_leitor
FROM livros l
LEFT JOIN emprestimos e ON l.id = e.livro_id;

-- Livros que nunca foram emprestados
SELECT l.titulo
FROM livros l
LEFT JOIN emprestimos e ON l.id = e.livro_id
WHERE e.id IS NULL;
