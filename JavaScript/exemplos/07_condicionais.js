let numero = Number(process.argv[2] || -4);

if (numero > 0) {
    console.log("Positivo");
} else if (numero < 0) {
    console.log("Negativo");
} else {
    console.log("É zero");
}

console.log(numero % 2 === 0 ? "Par" : "Ímpar");

// switch
let diaDaSemana = 3;
switch (diaDaSemana) {
    case 1:
        console.log("Segunda");
        break;
    case 2:
        console.log("Terça");
        break;
    case 3:
        console.log("Quarta");
        break;
    default:
        console.log("Dia inválido");
}

// Rode assim para testar: node 07_condicionais.js 7
