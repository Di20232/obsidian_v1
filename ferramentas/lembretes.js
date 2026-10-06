// Sorteia perguntas de revisão do cofre para relembrar.
// Uso: node ferramentas/lembretes.js [quantidade] [trilha]
//   node ferramentas/lembretes.js            10 perguntas de qualquer trilha
//   node ferramentas/lembretes.js 5 Ecommerce
// Mostra as perguntas primeiro; as respostas aparecem depois de apertar Enter.
const readline = require('readline');
const { listarNotas, lerNota, extrairPerguntas } = require('./cofre-comum');

const quantidade = parseInt(process.argv[2], 10) || 10;
const filtro = (process.argv[3] || '').toLowerCase();

const todas = [];
for (const caminho of listarNotas()) {
  if (/\/Fontes\//.test(caminho) || caminho.startsWith('Cerebro/Templates/')) continue;
  if (filtro && !caminho.toLowerCase().includes(filtro)) continue;
  const { corpo, titulo } = lerNota(caminho);
  for (const par of extrairPerguntas(corpo)) todas.push({ ...par, titulo });
}

if (!todas.length) {
  console.log('Nenhuma pergunta encontrada' + (filtro ? ` na trilha "${filtro}"` : '') + '.');
  process.exit(0);
}

for (let i = todas.length - 1; i > 0; i--) {
  const j = Math.floor(Math.random() * (i + 1));
  [todas[i], todas[j]] = [todas[j], todas[i]];
}
const sorteadas = todas.slice(0, quantidade);

console.log(`\n== ${sorteadas.length} lembretes (de ${todas.length} perguntas no cofre) ==\n`);
sorteadas.forEach((p, i) => console.log(`${i + 1}. ${p.pergunta}\n   (${p.titulo})\n`));

const mostrarRespostas = () => {
  console.log('== Respostas ==\n');
  sorteadas.forEach((p, i) => console.log(`${i + 1}. ${p.resposta}\n`));
};

if (process.stdin.isTTY) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  rl.question('Tente responder de cabeça. Enter para ver as respostas...', () => { rl.close(); mostrarRespostas(); });
} else {
  mostrarRespostas();
}
