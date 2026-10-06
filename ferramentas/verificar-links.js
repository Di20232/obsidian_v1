// Verifica wikilinks, links markdown e canvas do cofre.
// Uso: node ferramentas/verificar-links.js [--tudo]
//   sem --tudo, ignora as cópias de código em */Fontes/*, onde links de exemplo
//   ("people/Sam Patel", "[[X]]") são texto do repositório original, não notas.
// Sai com código 1 quando encontra link quebrado nas notas.
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

const exatos = new Set(arquivos.map(f => f.toLowerCase()));
const porNome = new Set(arquivos.map(f => path.posix.basename(f).toLowerCase()));

function existe(origem, alvo) {
  let t = alvo.trim();
  if (!t) return true; // [[#titulo]] aponta para a própria nota
  if (!EXT.test(t)) t += '.md';
  const pasta = path.posix.dirname(origem);
  for (const c of [path.posix.join(pasta, t), path.posix.normalize(t)]) {
    if (exatos.has(c.replace(/^\.\//, '').toLowerCase())) return true;
  }
  const semSubida = t.toLowerCase().replace(/^(\.\.\/)+/, '');
  if (!t.includes('/')) return porNome.has(semSubida);
  return arquivos.some(f => f.toLowerCase() === semSubida || f.toLowerCase().endsWith('/' + semSubida));
}

const quebrados = [];
let total = 0;
const notas = arquivos.filter(f => /\.(md|canvas)$/.test(f) && (tudo || !/\/Fontes\//.test(f)));
for (const f of notas) {
  let texto = fs.readFileSync(path.join(root, f), 'utf8');
  if (f.endsWith('.canvas')) {
    let c;
    try { c = JSON.parse(texto || '{}'); } catch { quebrados.push([f, '(canvas com JSON inválido)']); continue; }
    for (const n of c.nodes || []) {
      if (n.type === 'file') { total++; if (!exatos.has(n.file.toLowerCase())) quebrados.push([f, n.file]); }
    }
    texto = (c.nodes || []).filter(n => n.type === 'text').map(n => n.text).join('\n');
  }
  texto = texto.replace(/```[\s\S]*?```/g, '').replace(/`[^`\n]*`/g, '');
  for (const m of texto.matchAll(/!?\[\[([^\]]+?)\]\]/g)) {
    total++;
    const alvo = m[1].split(/\\?\|/)[0].split('#')[0].replace(/\\$/, '');
    if (!existe(f, alvo)) quebrados.push([f, m[1]]);
  }
  for (const m of texto.matchAll(/\[[^\]]*\]\(([^)\s]+)\)/g)) {
    const href = m[1];
    if (/^[a-z]+:/i.test(href) || href.startsWith('#')) continue;
    total++;
    let alvo; try { alvo = decodeURIComponent(href.split('#')[0]); } catch { alvo = href; }
    if (!existe(f, alvo)) quebrados.push([f, href]);
  }
}

console.log(`${notas.length} notas verificadas, ${total} links, ${quebrados.length} quebrados`);
for (const [de, para] of quebrados) console.log(`  ${de}  ->  ${para}`);
process.exitCode = quebrados.length ? 1 : 0;
