// Exporta o cofre em JSONL para treinar ou alimentar uma IA.
// Uso: node ferramentas/exportar-para-ia.js [--incluir-pessoal]
// Gera em exportacao/:
//   notas.jsonl           uma nota por linha, com metadados e texto limpo (para RAG ou pré-treino)
//   perguntas.jsonl       pares pergunta/resposta das seções "Perguntas de revisão"
//   perguntas-chat.jsonl  os mesmos pares no formato de conversa (messages: user/assistant)
// Fica de fora por padrão: cópias de código de terceiros (*/Fontes/*), modelos, Diário e Inbox.
const fs = require('fs');
const path = require('path');
const { root, listarNotas, lerNota, extrairPerguntas, limparMarkdown } = require('./cofre-comum');

const pessoal = process.argv.includes('--incluir-pessoal');
const excluir = c =>
  /\/Fontes\//.test(c) ||
  c.startsWith('Cerebro/Templates/') ||
  (!pessoal && (c.startsWith('Cerebro/Diario/') || c.startsWith('Cerebro/Inbox/')));

const saida = path.join(root, 'exportacao');
fs.mkdirSync(saida, { recursive: true });
const notas = [], perguntas = [], chat = [];
let puladas = 0;

for (const caminho of listarNotas()) {
  if (excluir(caminho)) { puladas++; continue; }
  const { meta, corpo, titulo } = lerNota(caminho);
  const texto = limparMarkdown(corpo.replace(/\n{3,}/g, '\n\n'));
  if (texto.length < 80) { puladas++; continue; }
  const partes = caminho.split('/');
  const trilha = partes[0] === 'Cerebro' && partes.length > 2 ? partes[1] : partes[0];
  notas.push({
    id: caminho,
    titulo,
    trilha,
    tags: meta.tags || [],
    verificado_em: meta.verificado_em || null,
    fonte: meta.fonte || null,
    texto,
  });
  for (const par of extrairPerguntas(corpo)) {
    perguntas.push({ ...par, nota: caminho, titulo, trilha, verificado_em: meta.verificado_em || null });
    chat.push({ messages: [{ role: 'user', content: par.pergunta }, { role: 'assistant', content: par.resposta }] });
  }
}

const gravar = (nome, linhas) => fs.writeFileSync(path.join(saida, nome), linhas.map(l => JSON.stringify(l)).join('\n') + '\n', 'utf8');
gravar('notas.jsonl', notas);
gravar('perguntas.jsonl', perguntas);
gravar('perguntas-chat.jsonl', chat);

const porTrilha = {};
for (const n of notas) porTrilha[n.trilha] = (porTrilha[n.trilha] || 0) + 1;
console.log(`Exportado em exportacao/: ${notas.length} notas, ${perguntas.length} perguntas (${puladas} arquivos deixados de fora)`);
console.log('Notas por trilha:', Object.entries(porTrilha).map(([t, n]) => `${t} ${n}`).join(' · '));
const datados = notas.filter(n => n.verificado_em).length;
console.log(`${datados} notas têm verificado_em: dados que envelhecem, reconfira antes de treinar.`);
