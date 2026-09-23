USE biblioteca;

INSERT INTO livros (titulo, autor, ano_publicacao) VALUES
    ('Dom Casmurro', 'Machado de Assis', 1899),
    ('O Cortiço', 'Aluísio Azevedo', 1890),
    ('Grande Sertão: Veredas', 'Guimarães Rosa', 1956),
    ('Capitães da Areia', 'Jorge Amado', 1937);

SELECT * FROM livros;

UPDATE livros SET ano_publicacao = 1900 WHERE titulo = 'Dom Casmurro';

SELECT * FROM livros WHERE titulo = 'Dom Casmurro';

-- Sempre confira antes de apagar
SELECT * FROM livros WHERE titulo = 'O Cortiço';
DELETE FROM livros WHERE titulo = 'O Cortiço';

SELECT * FROM livros;
