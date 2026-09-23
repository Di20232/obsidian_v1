// Arrays
let frutas = ["maçã", "banana", "uva"];
console.log(frutas[0]);
console.log(frutas.at(-1));
frutas.push("pera");
console.log(frutas);

frutas.forEach((fruta, indice) => {
    console.log(indice, fruta);
});

// map, filter, reduce
let numeros = [1, 2, 3, 4, 5];
console.log(numeros.map(n => n * 2));
console.log(numeros.filter(n => n % 2 === 0));
console.log(numeros.reduce((total, n) => total + n, 0));

// Objetos
const pessoa = {
    nome: "Diego",
    idade: 25,
    cidade: "São Paulo",
};
console.log(pessoa.nome);
pessoa.idade = 26;
pessoa.profissao = "Dev";

for (const chave in pessoa) {
    console.log(chave, "->", pessoa[chave]);
}

// Exercício resolvido: array de objetos
const produtos = [
    { nome: "Caderno", preco: 15.9 },
    { nome: "Caneta", preco: 3.5 },
    { nome: "Mochila", preco: 120.0 },
];

produtos.forEach(produto => {
    console.log(`${produto.nome}: R$ ${produto.preco.toFixed(2)}`);
});

let total = produtos.reduce((soma, produto) => soma + produto.preco, 0);
console.log(`Total: R$ ${total.toFixed(2)}`);
