// Aritméticos
console.log(10 + 3);
console.log(10 - 3);
console.log(10 * 3);
console.log(10 / 3);
console.log(10 % 3);
console.log(10 ** 2);
console.log(Math.floor(10 / 3)); // divisão "inteira"

// Comparação: == vs ===
console.log(5 == "5");   // true
console.log(5 === "5");  // false
console.log(5 !== "5");  // true

// Lógicos
let idade = 20;
let temCarteira = true;
console.log(idade >= 18 && temCarteira);

// Atribuição composta e incremento
let contador = 0;
contador += 1;
contador++;
console.log(contador); // 2

// Exercício resolvido: semanas e dias em 100 dias
let dias = 100;
let semanas = Math.floor(dias / 7);
let diasRestantes = dias % 7;
console.log(`${semanas} semanas completas e ${diasRestantes} dias restantes`);

// Exercício resolvido: === vs ==
let nota = "10";
console.log(nota === 10); // false: tipos diferentes
console.log(nota == 10);  // true: coerção converte "10" para 10
