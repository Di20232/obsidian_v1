let nome = "Diego";
console.log(nome[0]);
console.log(nome.length);
console.log(nome.slice(0, 3));

let texto = "  Olá, Mundo!  ";
texto = texto.trim();
console.log(texto);
console.log(texto.toLowerCase());
console.log(texto.toUpperCase());
console.log(texto.replace("Olá", "Oi"));

let preco = 19.9;
console.log(`R$ ${preco.toFixed(2)}`);

let frase = "o rato roeu a roupa";
let palavras = frase.split(" ");
console.log(palavras);
console.log(palavras.join(" "));

// Exercício resolvido: validar e-mail
let email = process.argv[2] || "diego@exemplo.com";
if (email.includes("@") && email.endsWith(".com")) {
    console.log("e-mail válido");
} else {
    console.log("e-mail inválido");
}

// Exercício resolvido: contar palavras
let fraseUsuario = process.argv[3] || "o rato roeu a roupa do rei";
console.log(`A frase tem ${fraseUsuario.split(" ").length} palavras`);
