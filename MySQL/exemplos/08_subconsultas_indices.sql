USE biblioteca;

-- Subconsulta: livros nunca emprestados
SELECT titulo FROM livros
WHERE id NOT IN (SELECT livro_id FROM emprestimos);

-- Subconsulta correlacionada com EXISTS
SELECT titulo FROM livros l
WHERE EXISTS (SELECT 1 FROM emprestimos e WHERE e.livro_id = l.id);

-- Índices
CREATE INDEX idx_emprestimos_livro ON emprestimos(livro_id);
CREATE INDEX idx_livros_titulo ON livros(titulo);

-- Verificando o plano de execução
EXPLAIN SELECT * FROM emprestimos WHERE livro_id = 1;
