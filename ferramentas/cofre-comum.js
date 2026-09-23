// Funções compartilhadas pelas ferramentas do cofre: ler notas, frontmatter e perguntas de revisão.
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const PULAR = new Set(['.obsidian', '.git', '.trash', '.imports', 'node_modules', 'exportacao', 'ferramentas']);

function listarNotas() {
  const notas = [];
  (function varrer(dir) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      if (PULAR.has(e.name)) continue;
      const p = path.join(dir, e.name);
      if (e.isDirectory()) varrer(p);
      else if (e.name.endsWith('.md')) notas.push(path.relative(root, p).split(path.sep).join('/'));
    }
  })(root);
  return notas.sort();
}

// Frontmatter simples do cofre: chave: valor, e listas no formato [a, b].
function lerNota(caminho) {
  const bruto = fs.readFileSync(path.join(root, caminho), 'utf8').replace(/\r\n/g, '\n');
  const meta = {};
  let corpo = bruto;
  const m = bruto.match(/^---\n([\s\S]*?)\n---\n?/);
  if (m) {
    corpo = bruto.slice(m[0].length);
    for (const linha of m[1].split('\n')) {
      const kv = linha.match(/^([\w-]+):\s*(.*)$/);
      if (!kv) continue;
      const valor = kv[2].trim();
      meta[kv[1]] = /^\[.*\]$/.test(valor)
        ? valor.slice(1, -1).split(',').map(s => s.trim()).filter(Boolean)
        : valor.replace(/^["']|["']$/g, '');
    }
  }
  const titulo = (corpo.match(/^#\s+(.+)$/m) || [, path.posix.basename(caminho, '.md')])[1].trim();
  return { caminho, meta, corpo, titulo };
}

// "Pergunta :: Resposta" em linha própria, só dentro da seção "## Perguntas de revisão"
// (assim `std::cout` e outros "::" de código nunca viram pergunta).
function extrairPerguntas(corpo) {
  const semCodigo = corpo.replace(/```[\s\S]*?```/g, '');
  const pares = [];
  let naSecao = false;
  for (const linha of semCodigo.split('\n')) {
    if (/^##\s/.test(linha)) { naSecao = /^##\s+Perguntas de revisão/i.test(linha); continue; }
    if (!naSecao) continue;
    const m = linha.match(/^\s*(?:[-*]\s+)?(.+?)\s*::\s*(.+?)\s*$/);
    if (m) pares.push({ pergunta: limparMarkdown(m[1]), resposta: limparMarkdown(m[2]) });
  }
  return pares;
}

// Troca [[alvo|apelido]] pelo apelido e [[alvo]] pelo nome da nota; remove ênfase.
function limparMarkdown(texto) {
  return texto
    .replace(/!?\[\[([^\]|]+)\\?\|([^\]]+)\]\]/g, '$2')
    .replace(/!?\[\[([^\]]+)\]\]/g, (_, alvo) => path.posix.basename(alvo.split('#')[0]).replace(/^\d+-/, '').replace(/-/g, ' '))
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/\\\|/g, '|')
    .trim();
}

module.exports = { root, listarNotas, lerNota, extrairPerguntas, limparMarkdown };
