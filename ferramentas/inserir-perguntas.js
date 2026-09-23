// Insere uma seção "## Perguntas de revisão" em notas, a partir de um JSON
// { "arquivo.md": [["pergunta", "resposta"], ...] }, e marca a nota com a tag flashcards.
// Uso: node ferramentas/inserir-perguntas.js <pasta-das-notas> <perguntas.json>
// Não mexe em notas que já têm a seção (rodar de novo é seguro).
const fs = require('fs');
const path = require('path');

const [pasta, arquivoJson] = process.argv.slice(2);
if (!pasta || !arquivoJson) {
  console.error('Uso: node ferramentas/inserir-perguntas.js <pasta-das-notas> <perguntas.json>');
  process.exit(1);
}
const dados = JSON.parse(fs.readFileSync(arquivoJson, 'utf8'));
let feitas = 0, puladas = 0;

for (const [nome, pares] of Object.entries(dados)) {
  const alvo = path.join(pasta, nome);
  if (!fs.existsSync(alvo)) { console.log(`  não existe: ${nome}`); puladas++; continue; }
  let texto = fs.readFileSync(alvo, 'utf8');
  if (/^##\s+Perguntas de revisão/m.test(texto)) { console.log(`  já tem perguntas: ${nome}`); puladas++; continue; }

  const bloco = '## Perguntas de revisão\n\n' + pares.map(([p, r]) => `${p} :: ${r}`).join('\n\n') + '\n\n';
  // Antes do rodapé de navegação ("---" seguido de Anterior/Próxima/Trilha); senão, no fim.
  const rodape = texto.search(/\n---\n(?:Anterior|Próxima|Trilha)/);
  texto = rodape >= 0
    ? texto.slice(0, rodape).replace(/\s*$/, '\n\n') + bloco + texto.slice(rodape + 1)
    : texto.replace(/\s*$/, '\n\n') + bloco.trimEnd() + '\n';

  // Tag flashcards no frontmatter (usada pelo plugin Spaced Repetition, se instalado).
  texto = texto.replace(/^(---\n[\s\S]*?^tags:\s*\[)([^\]]*)\]/m, (m, ini, tags) =>
    /\bflashcards\b/.test(tags) ? m : `${ini}${tags}, flashcards]`);

  fs.writeFileSync(alvo, texto, 'utf8');
  feitas++;
}
console.log(`${feitas} notas com perguntas inseridas, ${puladas} puladas.`);
