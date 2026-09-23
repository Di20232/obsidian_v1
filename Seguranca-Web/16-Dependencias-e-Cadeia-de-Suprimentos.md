---
tags: [seguranca, web, dependencias, supply-chain, npm, pip, flashcards]
aliases: [Cadeia de Suprimentos de Software, Supply Chain]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# Dependências e cadeia de suprimentos

Um projeto Node pequeno instala centenas de pacotes; um projeto Python, dezenas. **Cada um roda com as mesmas permissões do seu código.** A categoria A03 do [[02-OWASP-Top-10|OWASP Top 10:2025]] trata disso: tem poucas ocorrências nos dados, mas o maior impacto médio entre as dez.

## Os três tipos de problema

| Tipo | Exemplo | Defesa |
|---|---|---|
| **Vulnerabilidade conhecida** numa dependência | versão antiga de uma biblioteca com falha publicada (CVE) | auditoria e atualização frequente |
| **Pacote malicioso** | nome parecido com um popular (*typosquatting*: `reqeusts`), mantenedor com conta invadida publicando versão com código que rouba variáveis de ambiente | conferir antes de instalar, lockfile, bloquear scripts de instalação quando possível |
| **Build ou distribuição comprometidos** | ação do GitHub Actions alterada, script de CDN trocado | fixar versões por hash, verificar integridade |

> [!warning] Pacotes que a IA inventa
> Assistentes de código às vezes sugerem pacotes **que não existem**. Atacantes registram esses nomes com código malicioso (*slopsquatting*). Antes de instalar um pacote sugerido, confira se ele existe, quem mantém e há quanto tempo. → [[IA-Aplicada/09-Riscos-Seguranca-e-LGPD-na-IA|riscos na IA]]

## Antes de adicionar uma dependência

- **Preciso mesmo?** Uma função de 10 linhas não justifica um pacote.
- **É o pacote certo?** Confira o nome letra por letra, o repositório oficial e o link da documentação.
- **Está vivo?** Última versão, frequência de commits, issues respondidas, número de mantenedores.
- **É popular?** Downloads semanais e projetos que dependem dele.
- **O que ele puxa junto?** Uma dependência que traz 80 outras aumenta a superfície.

## Lockfile: instalar sempre a mesma coisa

| Ecossistema | Arquivo | Instalação reprodutível |
|---|---|---|
| npm | `package-lock.json` (versionar!) | `npm ci` |
| pnpm / yarn | `pnpm-lock.yaml` / `yarn.lock` | `pnpm install --frozen-lockfile` / `yarn install --immutable` |
| pip | `requirements.txt` com versões fixas (`==`) e, idealmente, hashes | `pip install --require-hashes -r requirements.txt` |
| uv / Poetry | `uv.lock` / `poetry.lock` | `uv sync --locked` / `poetry install` |

Sem lockfile, dois `npm install` em dias diferentes podem instalar versões diferentes — inclusive uma recém-comprometida.

## Auditar e atualizar

```bash
npm audit                     # vulnerabilidades conhecidas nas dependências
npm outdated                  # o que está desatualizado
pip-audit                     # equivalente para Python (pip install pip-audit)
```

- Ative o **Dependabot** (ou Renovate) no GitHub: ele abre pull requests com as atualizações e alertas de segurança.
- **Atualize com frequência e em passos pequenos.** Pular dois anos de versões transforma uma atualização de rotina num projeto.
- Nem todo alerta é urgente: veja se a parte vulnerável é usada pelo seu código e se a dependência é só de desenvolvimento.
- `npm audit fix --force` pode instalar versões com mudanças incompatíveis. Rode os testes depois.

## Scripts de instalação

Pacotes npm podem rodar código no `install` (`postinstall`). É o caminho mais usado por pacotes maliciosos. Opções:

- `npm install --ignore-scripts` (ou `ignore-scripts=true` no `.npmrc`) e liberar só os pacotes que precisam compilar algo.
- pnpm e Bun já bloqueiam scripts de dependências por padrão e pedem liberação explícita.

## Integridade de scripts de CDN

Ao carregar um script de outro domínio, inclua o hash esperado (**Subresource Integrity**). Se o arquivo no CDN for alterado, o navegador se recusa a executar:

```html
<script src="https://cdn.jsdelivr.net/npm/biblioteca@1.2.3/dist/lib.min.js"
        integrity="sha384-<hash do arquivo>"
        crossorigin="anonymous"></script>
```

Fixe a **versão exata** na URL; `@latest` torna o hash inútil.

## CI/CD

- Fixar ações do GitHub Actions por **hash do commit**, não só por tag (`uses: actions/checkout@<sha>`), porque tags podem ser movidas.
- Dar ao token do CI só as permissões necessárias (`permissions: contents: read`).
- Segredos do CI não ficam disponíveis para pull requests vindos de forks.

## Imagens Docker

- Imagem base oficial e com versão fixa (`python:3.12-slim`, não `latest`).
- Reconstruir periodicamente para receber correções do sistema.
- Não rodar como root dentro do container (`USER app`). → [[Cerebro/Tecnologias/04-Docker|Docker]]

## Perguntas de revisão

Por que dependências são um risco de segurança? :: Porque cada pacote roda com as mesmas permissões do seu código, e um projeto instala dezenas ou centenas deles.

O que é typosquatting? :: Publicar um pacote malicioso com nome parecido com um popular, esperando erro de digitação, como reqeusts no lugar de requests.

O que é slopsquatting? :: Registrar com código malicioso nomes de pacotes inexistentes que assistentes de IA costumam sugerir.

Para que serve o lockfile? :: Para instalar sempre exatamente as mesmas versões das dependências, em qualquer máquina e dia.

Qual a diferença entre npm install e npm ci? :: O npm ci instala exatamente o que está no package-lock.json e falha se houver divergência; o npm install pode atualizar o lockfile.

Quais comandos auditam dependências no npm e no Python? :: npm audit no Node e pip-audit no Python.

Por que atualizar dependências com frequência e em passos pequenos? :: Porque atualizações pequenas são fáceis de testar; acumular anos de versões transforma a correção de segurança num projeto grande.

Por que scripts postinstall são perigosos? :: Porque executam código de qualquer pacote na instalação, e são o caminho mais usado por pacotes maliciosos.

O que é Subresource Integrity? :: Um atributo integrity com o hash esperado de um script externo; se o arquivo mudar, o navegador não executa.

Por que fixar ações do GitHub Actions por hash do commit? :: Porque tags podem ser movidas para outro código; o hash garante que a ação executada é a que foi revisada.

---
Anterior: [[15-Segredos-e-Configuracao-Segura|Segredos e configuração]] · Próxima: [[17-Logs-Monitoramento-e-Incidentes|Logs e incidentes]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
