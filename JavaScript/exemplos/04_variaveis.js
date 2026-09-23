// let, const
let idade = 25;
const nome = "Diego";
let cidade = "São Paulo";

console.log(nome, idade, cidade);

// Tipos primitivos e typeof
console.log(typeof idade);
console.log(typeof nome);
console.log(typeof true);
console.log(typeof undefined);

// Conversão de tipos
let idadeTexto = "25";
let idadeNumero = Number(idadeTexto);
console.log(idadeNumero + 1);

let numero = 10;
let numeroTexto = String(numero);
console.log("Tenho " + numeroTexto + " anos");

// Type coercion (a pegadinha)
console.log("5" + 3);   // "53"
console.log("5" - 3);   // 2
console.log("5" * "2"); // 10
