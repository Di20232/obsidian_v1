// Três formas de escrever função
function saudacao(nome) {
    console.log(`Olá, ${nome}!`);
}
saudacao("Diego");

const saudacao2 = function (nome) {
    console.log(`Olá (expressão), ${nome}!`);
};
saudacao2("Diego");

const saudacao3 = (nome) => {
    console.log(`Olá (arrow), ${nome}!`);
};
saudacao3("Diego");

const dobro = (numero) => numero * 2;
console.log(dobro(5));

// return
function somar(a, b) {
    return a + b;
}
console.log(somar(3, 4));

// Valor padrão
function saudacao4(nome, saudacaoInicial = "Olá") {
    console.log(`${saudacaoInicial}, ${nome}!`);
}
saudacao4("Diego");
saudacao4("Diego", "Bom dia");

// Desestruturação de objeto como substituto de argumento nomeado
function apresentar({ nome, idade, cidade }) {
    console.log(`${nome}, ${idade} anos, de ${cidade}`);
}
apresentar({ cidade: "São Paulo", nome: "Diego", idade: 25 });

// Exercício resolvido
const ehPar = (numero) => numero % 2 === 0;

for (let numero = 1; numero <= 10; numero++) {
    console.log(numero, ehPar(numero));
}
