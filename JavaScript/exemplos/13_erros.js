// NaN: conversão inválida não lança erro sozinha
let idade1 = Number("abc");
console.log(idade1);          // NaN
console.log(Number.isNaN(idade1)); // true

// try/catch/finally
try {
    console.log("Tentando...");
    JSON.parse("{ isso não é json válido }");
} catch (erro) {
    console.log("Capturado:", erro.message);
} finally {
    console.log("Isto roda sempre.");
}

// throw + try/catch
function dividir(a, b) {
    if (b === 0) {
        throw new Error("Não é possível dividir por zero");
    }
    return a / b;
}

try {
    console.log(dividir(10, 2));
    console.log(dividir(10, 0));
} catch (erro) {
    console.log("Erro:", erro.message);
}

// Validando entrada do usuário
let idadeTexto = process.argv[2] || "25";
let idade = Number(idadeTexto);
if (Number.isNaN(idade)) {
    console.log("Isso não é um número válido!");
} else {
    console.log(`Idade registrada: ${idade}`);
}
