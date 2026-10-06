// Verifica os links e grava um ponto de restauração do cofre no git.
// Uso: clique duas vezes em salvar-cofre.bat, ou rode no terminal:
//   node ferramentas/salvar-cofre.js "o que mudou"
const { spawnSync } = require('child_process');
const path = require('path');

const root = path.resolve(__dirname, '..');
const rodar = (cmd, args, mostrar = true) =>
  spawnSync(cmd, args, { cwd: root, encoding: 'utf8', stdio: mostrar ? 'inherit' : 'pipe' });

console.log('\n== Links ==');
if (rodar('node', [path.join(__dirname, 'verificar-links.js')]).status !== 0) {
  console.log('Há links quebrados (lista acima). O ponto de restauração será gravado mesmo assim.');
}

console.log('\n== Mudanças ==');
const mudancas = rodar('git', ['status', '--porcelain'], false).stdout.split('\n').filter(Boolean);
if (!mudancas.length) {
  console.log('Nada mudou desde o último ponto de restauração.');
  process.exit(0);
}
rodar('git', ['status', '--short']);

const agora = new Date();
const dois = n => String(n).padStart(2, '0');
const quando = `${agora.getFullYear()}-${dois(agora.getMonth() + 1)}-${dois(agora.getDate())} ${dois(agora.getHours())}:${dois(agora.getMinutes())}`;
const mensagem = process.argv[2] || `Cofre em ${quando} (${mudancas.length} arquivos)`;

rodar('git', ['add', '-A']);
if (rodar('git', ['commit', '-q', '-m', mensagem]).status !== 0) process.exit(1);
console.log('\nPonto de restauração gravado:');
rodar('git', ['log', '-1', '--format=  %h  %s']);
