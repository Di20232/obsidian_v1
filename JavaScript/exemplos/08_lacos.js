// for clássico
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// for...of (percorre valores)
let frutas = ["maçã", "banana", "uva"];
for (const fruta of frutas) {
    console.log(fruta);
}

// for...in (percorre chaves)
let pessoa = { nome: "Diego", idade: 25 };
for (const chave in pessoa) {
    console.log(chave, "->", pessoa[chave]);
}

// while
let contador = 0;
while (contador < 5) {
    console.log(contador);
    contador++;
}

// break e continue
for (let i = 0; i < 10; i++) {
    if (i === 5) break;
    console.log(i);
}
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) continue;
    console.log(i);
}

// Exercício resolvido: tabuada
let numero = Number(process.argv[2] || 5);
for (let i = 1; i <= 10; i++) {
    console.log(`${numero} x ${i} = ${numero * i}`);
}

// Exercício resolvido: cumprimentar nomes
let nomes = ["Diego", "Ana", "Bruno"];
for (const nome of nomes) {
    console.log(`Olá, ${nome}!`);
}
