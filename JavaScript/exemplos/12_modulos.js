const { dobro, quadrado } = require("./utilidades.js");

console.log(dobro(5));   // 10

// Exercício resolvido: quadrado dos números de 1 a 5
for (let numero = 1; numero <= 5; numero++) {
    console.log(`${numero}^2 = ${quadrado(numero)}`);
}
