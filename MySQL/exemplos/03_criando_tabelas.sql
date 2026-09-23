CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

DROP TABLE IF EXISTS emprestimos;
DROP TABLE IF EXISTS livros;

CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100),
    ano_publicacao INT
);

CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    nome_leitor VARCHAR(100) NOT NULL,
    data_emprestimo DATE DEFAULT (CURRENT_DATE),
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);

DESCRIBE livros;
DESCRIBE emprestimos;
