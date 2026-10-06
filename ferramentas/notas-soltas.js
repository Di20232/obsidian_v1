// Encontra notas sem ligação no cofre.
// Uso: node ferramentas/notas-soltas.js [--tudo]
//   isoladas:     nenhum link sai e nenhum link chega
//   sem entrada:  ninguém aponta para a nota (só se chega por busca)
//   sem saída:    a nota não aponta para nada
// Sem --tudo, ignora as cópias de código em */Fontes/*.
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const tudo = process.argv.includes('--tudo');
const PULAR = new Set(['.obsidian', '.git', '.trash', '.imports', 'node_modules']);
const EXT = /\.(md|canvas|base|png|jpe?g|gif|svg|webp|pdf|zip|css|json|ps1|bat|txt)$/i;

const arquivos = [];
(function varrer(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (PULAR.has(e.name)) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) varrer(p);
    else arquivos.push(path.relative(root, p).split(path.sep).join('/'));
  }
})(root);

const porCaminho = new Map(arquivos.map(f => [f.toLowerCase(), f]));

// Resolve como o Obsidian: caminho relativo ou a partir da raiz; senão pelo nome,
// preferindo a mesma pasta e depois o caminho mais curto.
function resolver(origem, alvo) {
  let t = alvo.trim();
  if (!t) return origem;
  if (!EXT.test(t)) t += '.md';
  const pasta = path.posix.dirname(origem);
  for (const c of [path.posix.join(pasta, t), path.posix.normalize(t)]) {
    const achado = porCaminho.get(c.replace(/^\.\//, '').toLowerCase());
    if (achado) return achado;
  }
  const fim = t.toLowerCase().replace(/^(\.\.\/)+/, '');
  const cands = arquivos.filter(f => {
    const l = f.toLowerCase();
    return l === fim || l.endsWith('/' + fim);
  });
  if (!cands.length) return null;
  return cands.find(f => path.posix.dirname(f) === pasta) || cands.sort((a, b) => a.length - b.length)[0];
}

const ehNota = f => /\.(md|canvas)$/.test(f) && (tudo || !/\/Fontes\//.test(f));
const notas = arquivos.filter(ehNota);
const saidas = new Map(notas.map(n => [n, new Set()]));
const entradas = new Map(notas.map(n => [n, new Set()]));

for (const f of notas) {
  let texto = fs.readFileSync(path.join(root, f), 'utf8');
  const alvos = [];
  if (f.endsWith('.canvas')) {
    let c = {};
    try { c = JSON.parse(texto || '{}'); } catch {}
    for (const n of c.nodes || []) if (n.type === 'file') alvos.push(n.file);
    texto = (c.nodes || []).filter(n => n.type === 'text').map(n => n.text).join('\n');
  }
  texto = texto.replace(/```[\s\S]*?```/g, '').replace(/`[^`\n]*`/g, '');
  for (const m of texto.matchAll(/!?\[\[([^\]]+?)\]\]/g)) alvos.push(m[1].split(/\\?\|/)[0].split('#')[0].replace(/\\$/, ''));
  for (const m of texto.matchAll(/\[[^\]]*\]\(([^)\s]+)\)/g)) {
    if (/^[a-z]+:/i.test(m[1]) || m[1].startsWith('#')) continue;
    try { alvos.push(decodeURIComponent(m[1].split('#')[0])); } catch { alvos.push(m[1]); }
  }
  for (const a of alvos) {
    const destino = f.endsWith('.canvas') && porCaminho.has(a.toLowerCase()) ? porCaminho.get(a.toLowerCase()) : resolver(f, a);
    if (!destino || destino === f) continue;
    saidas.get(f).add(destino);
    if (entradas.has(destino)) entradas.get(destino).add(f);
  }
}

const isoladas = notas.filter(n => !saidas.get(n).size && !entradas.get(n).size);
const semEntrada = notas.filter(n => saidas.get(n).size && !entradas.get(n).size);
const semSaida = notas.filter(n => !saidas.get(n).size && entradas.get(n).size);

const listar = (titulo, lista) => {
  console.log(`\n${titulo}: ${lista.length}`);
  for (const n of lista) console.log('  ' + n);
};
console.log(`${notas.length} notas analisadas`);
listar('Isoladas (nenhuma ligação)', isoladas);
listar('Sem entrada (ninguém aponta para elas)', semEntrada);
listar('Sem saída (não apontam para nada)', semSaida);
