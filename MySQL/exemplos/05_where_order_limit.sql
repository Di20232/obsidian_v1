USE biblioteca;

-- Livros publicados depois de 1900, mais recente primeiro, top 2
SELECT titulo, autor, ano_publicacao
FROM livros
WHERE ano_publicacao > 1900
ORDER BY ano_publicacao DESC
LIMIT 2;

-- Busca por padrão de texto no título
SELECT * FROM livros WHERE titulo LIKE '%Sertão%';

-- Intervalo de anos
SELECT * FROM livros WHERE ano_publicacao BETWEEN 1930 AND 1960;

-- Cidades distintas (exemplo hipotético, requer coluna cidade em clientes)
-- SELECT DISTINCT cidade FROM clientes;
