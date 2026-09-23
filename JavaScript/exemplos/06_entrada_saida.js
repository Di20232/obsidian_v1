// Saída com template string
let nome = process.argv[2] || "Diego";
let idade = Number(process.argv[3] || 25);

console.log(`Olá, ${nome}!`);
console.log(`Você tem ${idade} anos.`);

const ANO_ATUAL = 2026;
let anoDos100 = ANO_ATUAL + (100 - idade);
console.log(`Você completa 100 anos em ${anoDos100}.`);

// Rode assim para testar com seus próprios dados:
// node 06_entrada_saida.js Diego 25
