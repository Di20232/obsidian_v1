const fs = require("fs").promises;

// setTimeout: prova de que o código não espera parado
console.log("1");
setTimeout(() => {
    console.log("2 (depois de um tempinho)");
}, 200);
console.log("3");

// Promise encadeada com .then()
fs.readFile(__dirname + "/dados.txt", "utf-8")
    .then((conteudo) => {
        console.log("Lido via .then():", conteudo.trim());
    })
    .catch((erro) => console.log("Erro:", erro.message));

// async/await (forma recomendada)
async function processarArquivo() {
    try {
        const conteudo = await fs.readFile(__dirname + "/dados.txt", "utf-8");
        console.log("Lido via await:", conteudo.trim().toUpperCase());
    } catch (erro) {
        console.log("Erro:", erro.message);
    }
}
processarArquivo();

// fetch: buscando dados de uma API real (requer internet)
async function buscarUsuario() {
    try {
        const resposta = await fetch("https://api.github.com/users/octocat");
        const dados = await resposta.json();
        console.log(`Usuário: ${dados.name}, repositórios públicos: ${dados.public_repos}`);
    } catch (erro) {
        console.log("Não foi possível buscar dados da API (sem internet?):", erro.message);
    }
}
buscarUsuario();
