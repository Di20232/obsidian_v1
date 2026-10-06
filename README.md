# Cérebro de Conhecimento

Cofre do Obsidian em português do Brasil. Junta **o que estudo** (14 trilhas, de Python a GANs) com **o que já construí** (projetos reais, bugs resolvidos, decisões). A tabela de trilhas do [Cérebro](Cerebro/00-Cerebro.md) mostra onde cada assunto já apareceu num projeto real.

O cofre tem 809 notas visíveis no Obsidian, sem contar este README: 307 escritas à mão e 502 geradas a partir do código importado do GitHub. As 90 notas de `.imports/` não aparecem, porque o Obsidian ignora pastas que começam com ponto. Cerca de 1.440 perguntas de revisão (`pergunta :: resposta`) ficam no fim de 263 notas.

## Como abrir

1. Clone o repositório:
   ```bash
   git clone https://github.com/Di20232/obsidian_v1.git
   ```
2. No Obsidian, escolha **Abrir pasta como cofre** e selecione a pasta `obsidian_v1`.
3. Abra [Cerebro/00-Cerebro.md](Cerebro/00-Cerebro.md).

No GitHub as notas também abrem, mas os links `[[...]]` entre elas só funcionam dentro do Obsidian.

A configuração vem no repositório, em `.obsidian/`. O cofre abre pronto:

| O quê | Como vem |
|---|---|
| Plugins | só os nativos (canvas, bases, notas diárias, modelos, propriedades, recuperação de arquivos e outros). **Nenhum plugin da comunidade.** |
| Nota nova (`Ctrl+N`) | cai em `Cerebro/Inbox` |
| Anexos | `Cerebro/Anexos` |
| Notas diárias | `Cerebro/Diario`, nome `AAAA-MM-DD`, com o modelo `Template-Diario` |
| Modelos (`Ctrl+P` → *Modelos: Inserir modelo*) | `Cerebro/Templates` |
| Links ao renomear | atualizados sempre, sem perguntar |
| Excluir nota | **sem pedir confirmação** (`promptDelete: false`) |
| Fora da busca e do grafo | `Cerebro/GitHub/Second-Brain/Fontes/` (código de terceiros com links de exemplo) |
| Cores por assunto | snippet `cerebro-todas-as-notas` já ativo; grafo com 20 grupos de cor |

Nada precisa ser ligado à mão. Três observações:

- O plugin nativo **Sync** está ligado, mas só faz algo com assinatura do Obsidian Sync.
- As perguntas de revisão seguem o formato do plugin da comunidade **Spaced Repetition**. Ele não vem instalado. Instalar é opcional.
- O outro snippet, `cerebro-cores`, é uma paleta antiga e fica desligado. Tem só 16 classes, sem E-commerce, Finanças, Bootstrap, Tailwind, MySQL, SQLite nem GitHub. Não precisa ligar.

## Por onde começar

- [Cérebro](Cerebro/00-Cerebro.md): porta de entrada. Mostra as áreas, as trilhas e os cinco aprendizados que mais custaram caro.
- [Painel de Estudo](Cerebro/01-Painel-de-Estudo.md): como escolher uma trilha e montar uma sessão de 45 a 90 minutos.
- [Como usar](Cerebro/02-Como-Usar.md): os três tipos de nota (captura, conhecimento, experiência), o fluxo e as convenções.

| Se você quer... | Vá para |
|---|---|
| Aprender a programar do zero | [Curso de Python do Zero](Python/00-Indice.md) |
| Escolher o que estudar agora | [Painel de Estudo](Cerebro/01-Painel-de-Estudo.md) |
| Resolver um problema parecido com um já enfrentado | [Problemas Resolvidos](Cerebro/Problemas-Resolvidos/00-Indice.md) |
| Retomar um projeto | [Projetos](Cerebro/Projetos/00-Indice.md) |
| Ver como os assuntos se ligam | [Mapas](Cerebro/Mapas/00-Mapa-Programacao.md) ou o [mapa visual](Cerebro/Mapa-do-Cerebro.canvas) (abre no Obsidian) |
| Anotar algo agora, sem organizar | [Caixa de Captura](Cerebro/Inbox/00-Capturar.md) ou a nota do dia no [Diário](Cerebro/Diario/00-Diario.md) |
| Fazer a revisão da semana, salvar ou desfazer | [Rotina do cofre](Cerebro/Guias/07-Rotina-do-Cofre.md) |
| Entender as cores | [Legenda de Cores](Cerebro/Guias/00-Legenda-de-Cores.md) |
| Usar o cofre com IA ou revisar com perguntas | [Cofre para IA e lembretes](Cerebro/Guias/08-Cofre-para-IA-e-Lembretes.md) |
| Saber o que aconteceu e quando | [Linha do Tempo](Cerebro/Linha-do-Tempo.md) |
| Conferir um termo | [Glossário](Cerebro/03-Glossario.md) |

## Estrutura do repositório

| Caminho | Notas `.md` | Outros arquivos | O que tem |
|---|---:|---:|---|
| `Cerebro/` | 606 | 8 | O núcleo: projetos, problemas resolvidos, tecnologias, práticas, ambiente, mapas, guias, modelos e a importação do GitHub (515 das notas). |
| 14 pastas de trilha | 203 | 84 | Uma pasta por assunto na raiz, de `Programacao-Geral/` a `Seguranca-Web/`. Os outros arquivos são os exemplos de código e seus dados, incluindo 13 `.pyc` de cache (veja "O que fica fora do git"). |
| `.obsidian/` | 0 | 8 | Configuração do cofre: 6 `.json` e 2 snippets CSS (`cerebro-todas-as-notas`, ativo; `cerebro-cores`, paleta antiga, desligado). |
| `.imports/` | 90 | 411 | Scripts PowerShell da importação do GitHub, a lista de repositórios, o manifesto com SHA-256 e as 4 árvores de código extraídas. Não aparece no Obsidian. |
| `.gitignore`, `.gitattributes` | — | 2 | O que fica fora do git; guardar byte a byte (`* -text`), com uma exceção (veja "O que fica fora do git"). |
| [Quero desenvolver um sistema web si.txt](Quero%20desenvolver%20um%20sistema%20web%20si.txt) | — | 1 | Briefing original do Projeto W. |

## Trilhas de estudo

Cada trilha tem um `00-Indice.md` e notas numeradas para ler em ordem. As notas de conteúdo terminam com perguntas de revisão; nas trilhas de programação, interface e banco de dados, também com um exercício. A contagem inclui o índice.

| Trilha | Notas | Temas | Onde aparece na prática |
|---|---:|---|---|
| [Programação Geral](Programacao-Geral/00-Indice.md) | 15 | computador, terminal, Git, estruturas de dados, algoritmos, HTML/CSS, SQL, web e HTTP, C e memória, testes | base de tudo |
| [Python](Python/00-Indice.md) | 17 | curso do zero: de "o que é programar" a classes e boas práticas | [CTL-TINTA-FL](Cerebro/Projetos/05-CTL-TINTA-FL.md), [Projeto W](Cerebro/Projetos/07-Projeto-W-Analise-de-Vendas.md) |
| [JavaScript](JavaScript/00-Indice.md) | 18 | o mesmo formato do Python, mais assincronismo e DOM | [Mercadinho Seu João](Cerebro/Projetos/06-Mercadinho-Seu-Joao.md) |
| [PHP](PHP/00-Indice.md) | 16 | formulários, superglobais, POO, PDO com MySQL e SQLite | — |
| [CSS](CSS/00-Indice.md) | 10 | seletores, box model, flexbox, grid, responsividade, animações | interfaces do Mercadinho (HTML, CSS e JavaScript servidos pelo backend) e do CTL-TINTA-FL |
| [TailwindCSS](TailwindCSS/00-Indice.md) | 7 | utility-first, layout, estados, dark mode (Tailwind 3) | CTL-TINTA-FL: classes Tailwind no Reflex ([Problema 08](Cerebro/Problemas-Resolvidos/08-Toast-Invisivel-com-Classes-Tailwind.md)) |
| [Bootstrap](Bootstrap/00-Indice.md) | 7 | Bootstrap 5: grid, componentes, utilitários | — |
| [SQLite](SQLite/00-Indice.md) | 8 | banco sem servidor, tipos dinâmicos, CRUD, uso com Python e PHP | CTL-TINTA-FL ([SQLite na prática](Cerebro/Tecnologias/03-SQLite-na-Pratica.md)) |
| [MySQL](MySQL/00-Indice.md) | 12 | tabelas, CRUD, joins, agregação, índices, transações, usuários | conceitos aplicados no PostgreSQL do Mercadinho |
| [IA Aplicada](IA-Aplicada/00-Indice.md) | 11 | modelos de linguagem, prompts, embeddings, RAG, fine-tuning, avaliação, agentes, LGPD | [Claude Code](Cerebro/Tecnologias/08-Claude-Code.md), o cofre como dado de treino |
| [GANs](GANs/00-Indice.md) | 13 | gerador e discriminador, treino, WGAN-GP, arquiteturas, avaliação, deepfakes e lei | [uma GAN treinada nas notas do cofre](GANs/10-Experimento-GAN-com-as-Notas.md) |
| [Finanças](Financas/00-Indice.md) | 15 | caixa, DRE, margem, preço, capital de giro, impostos (MEI, Simples, reforma), crédito | [Sistema de Vendas e Estoque](Cerebro/Projetos/02-Sistema-de-Vendas-e-Estoque.md), Mercadinho |
| [E-commerce](Ecommerce/00-Indice.md) | 35 | Shopify, pagamentos, frete, fiscal, marketplaces, tráfego pago | [Planejamento de E-commerce](Cerebro/Projetos/04-Planejamento-de-E-commerce.md), [Loja de Infoprodutos](Cerebro/Projetos/03-Loja-de-Infoprodutos-sobre-IA.md), [byteShop](Cerebro/GitHub/byteShop/01-Arquitetura-e-Aprendizados.md) |
| [Segurança Web](Seguranca-Web/00-Indice.md) | 19 | OWASP Top 10, senhas, sessões, JWT, OAuth, injeção, XSS, CSRF, incidentes | [Segurança em apps locais](Cerebro/Praticas/07-Seguranca-em-Apps-Locais.md), [SQL injection no Projeto W](Cerebro/Problemas-Resolvidos/21-SQL-Injection-por-Token-de-URL.md) |

A ordem que as próprias notas pressupõem:

- **Programação:** Python (não exige saber nada) → Programação Geral → JavaScript → PHP. O Painel de Estudo sugere estudar a base junto com uma linguagem.
- **Interface:** CSS antes de Bootstrap ou Tailwind.
- **Banco:** [SQL e bancos de dados](Programacao-Geral/09-SQL-e-Bancos-de-Dados.md) → MySQL → SQLite. O índice do SQLite parte do MySQL. Para praticar sem instalar nada, o índice do MySQL indica o SQLite.
- **Negócio:** Finanças antes de E-commerce.
- **IA:** GANs pede Python básico. A nota 10 de GANs usa RAG, fine-tuning e preparação de dados, da IA Aplicada.

## O Cérebro

A parte que vem da experiência fica em `Cerebro/`, com entrada pelo [Cérebro](Cerebro/00-Cerebro.md). Quase toda pasta de notas tem um índice com prefixo `00-`. As exceções são `GitHub/Conhecimento/` e as subpastas `Fontes/` geradas. Em `Mapas/`, o `00-` é o Mapa de Programação.

| Área | O que tem |
|---|---|
| [Projetos](Cerebro/Projetos/00-Indice.md) | 9 projetos: o que resolvem, como rodar, decisões, pendências. Os três sistemas implementados são CTL-TINTA-FL (Python, Reflex, SQLite), Mercadinho Seu João (Node, Express, Prisma, PostgreSQL, Docker) e Projeto W (Streamlit, Pandas, Plotly, Docker). |
| [Problemas Resolvidos](Cerebro/Problemas-Resolvidos/00-Indice.md) | 24 casos de depuração em 6 categorias; 21 deles ligados ao projeto que os gerou. O formato padrão é sintoma → causa-raiz → correção → prevenção. Olhe aqui antes de investigar do zero. |
| [Tecnologias](Cerebro/Tecnologias/00-Indice.md) | 8 ferramentas usadas de verdade: Reflex, Flask, SQLite, Docker, Prisma e PostgreSQL, Git e GitHub, Streamlit, Claude Code. Cada uma com a sua armadilha principal. |
| [Práticas](Cerebro/Praticas/00-Indice.md) | 4 práticas de base e 5 tiradas dos projetos: importação de planilhas, caça de bugs, segurança em apps locais, unidades de medida, como trabalhamos. |
| [Ambiente](Cerebro/Ambiente/00-Indice.md) | Máquina Windows, mapa de portas, as duas contas Git. Regra: nada de senha, token ou `.env` real no cofre. |
| [Mapas](Cerebro/Mapas/00-Mapa-Programacao.md) | 7 mapas de conteúdo: Programação, Web, Dados, Engenharia, Segurança, IA e Complementar. |
| [Guias](Cerebro/Guias/00-Indice.md) | Aprender um assunto, resolver problemas, criar projeto, transformar experiência em conhecimento, Git e VS Code, servidor local para HTML, rotina do cofre, cofre para IA, legenda de cores. |
| [Modelos](Cerebro/Templates/00-Modelos.md) | 7 modelos: Conceito, Decisão, Diário, Problema, Projeto, Revisão Semanal, Tecnologia. |
| [GitHub](Cerebro/GitHub/00-Indice.md) | Retrato de 15/09/2026 dos repositórios públicos de Di20232 e de uma biblioteca externa. Detalhes abaixo. |
| [Inbox](Cerebro/Inbox/00-Capturar.md) e [Diário](Cerebro/Diario/00-Diario.md) | Só os índices. Nenhuma captura ou nota diária foi publicada. |
| [Referências](Cerebro/Referencias/00-Referencias-Confiaveis.md) | Critérios de fonte confiável. |
| Anexos (`Cerebro/Anexos/`) | 3 gráficos SVG dos experimentos de GAN. |

Na raiz de `Cerebro/` ficam ainda o [Glossário](Cerebro/03-Glossario.md) (12 termos), a [Linha do Tempo](Cerebro/Linha-do-Tempo.md) (11 marcos, de 03/09 a 06/10/2026) e o [Mapa do Cérebro](Cerebro/Mapa-do-Cerebro.canvas), um canvas com 11 nós.

### Repositórios importados

| Repositório | Arquivos | Comece por |
|---|---:|---|
| byteShop (React/TypeScript + FastAPI) | 88 | [Arquitetura e aprendizados](Cerebro/GitHub/byteShop/01-Arquitetura-e-Aprendizados.md) |
| contro-vend-public (Node/Express + Prisma) | 43 | [Arquitetura e aprendizados](Cerebro/GitHub/contro-vend-public/01-Arquitetura-e-Aprendizados.md) |
| exercises_python | 13 | [Guia de estudo](Cerebro/GitHub/exercises_python/01-Guia-de-Estudo.md) |
| eugeniughelbur/obsidian-second-brain (licença MIT) | 354 | [Guia em português](Cerebro/GitHub/Second-Brain/01-Guia-em-Portugues.md) |

- Cada arquivo de origem virou uma nota em `<repositório>/Fontes/` (498 no total), com `source` e `source_commit` no frontmatter.
- A cópia íntegra de cada repositório está num ZIP em `Cerebro/GitHub/Arquivos/`. Os SHA-256 estão no [registro da importação](Cerebro/GitHub/04-Registro-da-Importacao.md).
- O CTL-TINTA estava vazio no GitHub e tem só [uma nota escrita à mão](Cerebro/GitHub/CTL-TINTA/00-Indice.md).
- `Cerebro/GitHub/Conhecimento/` reúne 4 notas tiradas do código, sem índice próprio: [estoque concorrente](Cerebro/GitHub/Conhecimento/01-Estoque-Concorrente.md), [sessão e permissões](Cerebro/GitHub/Conhecimento/02-Sessao-e-Permissoes.md), [testes](Cerebro/GitHub/Conhecimento/03-Testar-Comportamento.md) e [previsão de reposição](Cerebro/GitHub/Conhecimento/04-Previsao-de-Reposicao.md).
- As `Fontes/` e o `00-Indice.md` de cada repositório são **gerados** por `.imports/converter-fontes.ps1`, depois de `.imports/baixar-fontes.ps1`.

**Rodar os scripts da importação.** No Windows, a política de execução padrão bloqueia arquivos `.ps1`. Da raiz do cofre, com o PowerShell 7:

```powershell
pwsh -ExecutionPolicy Bypass -File .imports\baixar-fontes.ps1
pwsh -ExecutionPolicy Bypass -File .imports\converter-fontes.ps1
```

- **Use o PowerShell 7 (`pwsh`).** O `converter-fontes.ps1` está em UTF-8 sem BOM e tem o caractere `·` nos cabeçalhos. O Windows PowerShell 5.1 (`powershell`) lê esse arquivo como ANSI e grava `Â·` no lugar de `·`, o erro que aparece hoje nas notas geradas. Se só tiver o 5.1, salve antes o script em UTF-8 com BOM.
- **O conversor não grava por cima.** Com as `Fontes/` presentes, ele para no primeiro arquivo que já existe (erro `Destino ja existe`). Para regenerar, apague as quatro pastas `Cerebro/GitHub/*/Fontes/`. Isso recria as notas e o `00-Indice.md` de cada repositório e regrava `.imports/importacao-verificada.json`. Edições à mão nesses arquivos se perdem.

## Código de exemplo

Os exemplos ficam em `<Trilha>/exemplos/` e levam o número da nota que os explica (`04_crud.py` ↔ nota 04). As exceções são os dois scripts de GANs (`gan_2d.py`, da nota 08, e `gan_das_notas.py`, da nota 10) e o `JavaScript/exemplos/utilidades.js`, usado pelo 12. Os comandos rodam a partir da raiz. As notas foram escritas no Windows e usam `python`; no Linux e no macOS costuma ser `python3`.

| Exemplos | Como rodar | Precisa de |
|---|---|---|
| Python 03–15 | `python3 Python/exemplos/03_ola_mundo.py` | Python 3. Os de 06, 07, 08, 10, 13 e 14 pedem dados no teclado. |
| JavaScript 03–15 | `node JavaScript/exemplos/03_ola_mundo.js` | Node.js. O 06, 07, 08, 10 e 13 aceitam argumentos e têm valores padrão (ex.: `node JavaScript/exemplos/06_entrada_saida.js Ana 30`). O 14 usa `fetch` (Node 18+) e internet para consultar a API do GitHub; sem rede, essa parte mostra um aviso ou `undefined`. |
| JavaScript 16 | abrir `JavaScript/exemplos/16_dom.html` no navegador | navegador |
| PHP 03–14 | `php PHP/exemplos/03_ola_mundo.php` | PHP 8+; o 14 usa a extensão `pdo_sqlite` |
| PHP 11 (formulário) | `cd PHP/exemplos && php -S localhost:8000` e abrir `http://localhost:8000/11_formulario.html` | PHP e navegador |
| CSS 01–08 | abrir o `.html` no navegador | nada. O 03 busca a fonte Roboto no Google Fonts; sem internet, usa sans-serif. |
| TailwindCSS 02–05, Bootstrap 02–05 | abrir o `.html` no navegador | internet (Play CDN do Tailwind 3; Bootstrap 5.3.3 pelo jsDelivr) |
| SQLite 03–05 | `python3 SQLite/exemplos/04_crud.py` | só Python; o módulo `sqlite3` já vem junto |
| MySQL 03–09 | veja abaixo | servidor MySQL ou MariaDB e usuário administrador |

Os exemplos de Python, JavaScript, PHP e SQLite foram rodados (Python 3.13, Node 22, PHP 8.3) e terminam sem erro. Três deles gravam arquivos que o `.gitignore` não cobre:

- `Python/exemplos/14_arquivos.py` cria `tarefas.txt` na pasta atual.
- `PHP/exemplos/14_banco_dados.php` cria `PHP/exemplos/banco.db`.
- `SQLite/exemplos/05_persistencia.py` sobrescreve `SQLite/exemplos/tarefas.db`, que está versionado. Rode numa cópia ou desfaça com `git restore SQLite/exemplos/tarefas.db`.

**MySQL.** Os scripts formam uma sequência sobre o banco `biblioteca`, criado pelo 03. Rode em ordem, sem nome de banco no comando. Os comandos abaixo são para bash ou Git Bash:

```bash
mysql -u root -p -t < MySQL/exemplos/03_criando_tabelas.sql
# ... um por um até o 09, ou de uma vez:
cat MySQL/exemplos/0*.sql | mysql -u root -p -t
```

No PowerShell, o `<` não funciona. Use `Get-Content MySQL\exemplos\03_criando_tabelas.sql | mysql -u root -p -t`.

Não dá para repetir sem limpar. Na segunda vez, o 09 falha por chave duplicada, porque o 03 não apaga a tabela `contas`. O 08 rodado de novo sozinho falha porque os índices já existem. Para recomeçar, `DROP DATABASE biblioteca;`. O 09 cria o usuário `app_biblioteca@localhost` com a senha de exemplo `senha_forte_aqui`; remova depois com `DROP USER 'app_biblioteca'@'localhost';`. Esses scripts nunca rodaram num MySQL real (veja o aviso em [MySQL](MySQL/00-Indice.md)).

### Experimentos de GAN

Os dois scripts em `GANs/exemplos/` só precisam de PyTorch. Rodam na CPU e não acessam a rede. Instale o torch num ambiente virtual fora do cofre.

Linux e macOS (bash):

```bash
python3 -m venv ~/.venvs/gan-cofre
source ~/.venvs/gan-cofre/bin/activate
pip install torch --index-url https://download.pytorch.org/whl/cpu   # no macOS, basta: pip install torch
```

No Linux, o `pip install torch` sem `--index-url` instala a versão com CUDA, que traz vários GB de pacotes `nvidia-*` que estes scripts não usam.

Windows, no Prompt de Comando (cmd), como em [GAN em PyTorch](GANs/08-GAN-em-PyTorch.md). No PowerShell, `%USERPROFILE%` não funciona.

```bat
python -m venv %USERPROFILE%\.venvs\gan-cofre
%USERPROFILE%\.venvs\gan-cofre\Scripts\activate
pip install torch
```

| Comando | O que faz | Tempo |
|---|---|---|
| `python3 GANs/exemplos/gan_2d.py` | GAN que aprende 8 grupos de pontos num círculo. Mostra quantos grupos cobriu e o colapso de modos. | 15 a 20 s |
| `python3 GANs/exemplos/gan_2d.py --perda wgan-gp` | o mesmo com WGAN-GP | cerca de 1 min |
| `python3 GANs/exemplos/gan_das_notas.py --dados` | mostra o corpus: a prosa das notas do cofre | segundos |
| `python3 GANs/exemplos/gan_das_notas.py --treinar` | treina uma GAN de texto nas notas: mais 6000 iterações a partir do último ponto salvo (salva a cada 500). Rodar de novo soma outras 6000; para recomeçar, use `--do-zero`. | cerca de 30 min |
| `python3 GANs/exemplos/gan_das_notas.py --gerar 20` | gera 20 trechos com o modelo salvo | segundos |

A saída vai para `GANs/exemplos/saida/`, fora do git. Os resultados mudam de máquina para máquina, então os números das notas não são garantidos. As explicações estão em [GAN em PyTorch](GANs/08-GAN-em-PyTorch.md) e [Experimento com as notas](GANs/10-Experimento-GAN-com-as-Notas.md).

## Convenções

- **Nomes:** `NN-Titulo-Com-Hifens.md`, sem acento e sem espaço. O índice da pasta, quando existe, começa com `00-`. Dentro da nota, o título tem acento e diz o assunto, não a ação.
- **Frontmatter:** `tags` curtas e `cssclasses: [cerebro-nota, cerebro-<assunto>]`. Conteúdo que envelhece (lei, preço, taxa, versão) leva `verificado_em` e `fonte`.
- **Perguntas de revisão:** seção `## Perguntas de revisão` no fim da nota, antes do rodapé. Uma pergunta por linha, no formato `Pergunta? :: Resposta`, com uma linha em branco entre elas. A resposta é correta, completa numa frase e faz sentido sem a pergunta. Uma pergunta por fato. Dado que muda leva a data na resposta, por exemplo "(conferido em 23/09/2026)". Notas com perguntas levam a tag `flashcards`. A referência do formato é o guia [Cofre para IA e lembretes](Cerebro/Guias/08-Cofre-para-IA-e-Lembretes.md).
- **Links:** wikilinks com caminho, muitas vezes relativo (`[[../Python/11-Funcoes]]`). Toda nota liga ao assunto maior e a algo relacionado.
- **Cores:** cada assunto tem uma cor (18 na [legenda](Cerebro/Guias/00-Legenda-de-Cores.md)). A classe em `cssclasses` escolhe a cor, por exemplo `cerebro-projetos` para projeto.

## Rotina

| Quando | O quê |
|---|---|
| Todo dia | Abrir a nota do dia, que nasce em `Cerebro/Diario` com o modelo. Jogar ideias em **Capturas**. Ao terminar, uma linha em **Próximo passo**. |
| Ao criar uma nota | Escrever 3 a 6 perguntas de revisão na hora, enquanto o assunto está fresco. |
| Ao resolver um bug | Registrar na hora com o [modelo de problema](Cerebro/Templates/Template-Problema.md). |
| Toda semana, 20 a 30 min | Criar uma nota em `Diario/` com o [modelo de revisão](Cerebro/Templates/Template-Revisao-Semanal.md): esvaziar capturas, atualizar projetos, registrar problemas e decisões, conferir se as notas novas da semana ganharam perguntas, marcar marcos na Linha do Tempo, salvar. |

Uma ideia vira nota assim: captura no Inbox → título que dê para achar depois → explicação, exemplo e quando **não** usar → pelo menos dois links. Se já existe nota sobre o assunto, melhore essa nota em vez de criar uma duplicata.

### Salvar e desfazer com git

O cofre é um repositório git para que nada se perca. Em 15/09/2026 uma sessão sobrescreveu o índice de projetos e não houve como recuperar. Salve antes e depois de pedir a um agente que mexa no cofre.

Os comandos abaixo são para bash ou Git Bash:

```bash
git status                                                       # o que mudou
git add -A                                                       # preparar tudo o que mudou
git commit -m "Revisão da semana"                                # salvar um ponto de restauração
git log --oneline -- "Cerebro/Projetos/00-Indice.md"             # histórico de uma nota
git show <hash>:"Cerebro/Projetos/00-Indice.md"                  # ver uma versão antiga
git restore --source <hash> -- "Cerebro/Projetos/00-Indice.md"   # voltar a nota para essa versão
```

Troque `<hash>` pelo código que o `git log` mostrar. Antes de gravar, leia a lista do `git status`: o `git add -A` leva tudo o que não está no `.gitignore`. O guia manda salvar com `ferramentas/salvar-cofre.bat`, que saiu do repositório (veja os avisos). O `git add -A` e o `git commit` fazem o mesmo, sem a verificação de links.

Esses comandos gravam o ponto de restauração só na sua máquina. Para guardar também no GitHub, use `git push`. Antes, confira com que conta o Git vai enviar: veja [Contas Git](Cerebro/Ambiente/03-Contas-Git.md) e [Problemas Resolvidos 24](Cerebro/Problemas-Resolvidos/24-Push-403-com-Conta-Git-Errada.md).

## O que fica fora do git

| Entrada no `.gitignore` | Por quê |
|---|---|
| `.obsidian/workspace.json`, `.obsidian/workspace-mobile.json`, `.obsidian/cache` | estado da janela do Obsidian: muda a cada clique, não é conhecimento |
| `exportacao/` | exportação para IA (`notas.jsonl`, `perguntas.jsonl`, `perguntas-chat.jsonl`), gerada por `ferramentas/exportar-para-ia.js`, que não está na versão atual (veja os avisos). Deixa de fora as `Fontes/`, os modelos e, sem `--incluir-pessoal`, o Diário e o Inbox. |
| `GANs/exemplos/saida/` | modelos treinados, desenhos e histórico dos experimentos, recriáveis rodando os scripts |
| `__pycache__/` | cache do Python |
| `.trash/` | lixeira interna do Obsidian |
| `.DS_Store`, `Thumbs.db`, `desktop.ini` | arquivos de sistema |

O `.gitattributes` da raiz tem `* -text`: cada arquivo é guardado byte a byte, sem converter quebras de linha. Exceção: `.imports/eugeniughelbur--obsidian-second-brain/` traz um `.gitattributes` próprio (`* text=auto`, com `eol=lf` para `.py` e `.sh`), que vale dentro dessa pasta. No Windows com `core.autocrlf=true`, os arquivos dela saem com as quebras de linha convertidas.

Uma exceção à regra do cache: `Python/exemplos/__pycache__/` (13 arquivos `.pyc`) está versionado. Para tirar: `git rm -r --cached Python/exemplos/__pycache__`.

## Avisos

- **A pasta `ferramentas/` saiu do repositório** no commit `760d2aa` (29/09/2026). A [rotina do cofre](Cerebro/Guias/07-Rotina-do-Cofre.md), o guia [Cofre para IA](Cerebro/Guias/08-Cofre-para-IA-e-Lembretes.md), o modelo de revisão semanal e as notas [04](IA-Aplicada/04-RAG-Busca-Mais-Geracao.md) e [06](IA-Aplicada/06-Preparar-Dados-para-Treinar-IA.md) de IA Aplicada ainda citam `salvar-cofre.bat`, `verificar-links.js`, `lembretes.bat`/`.js`, `exportar-para-ia.js`, `notas-soltas.js` e `inserir-perguntas.js`. Na versão atual, esses comandos falham. Os scripts continuam no histórico; para trazê-los de volta: `git restore --source 9da104f -- ferramentas`.
- **Informação com data.** Leis, tributos, tarifas e padrões de segurança foram conferidos em 23/09/2026 (Finanças, E-commerce, Segurança Web). A lei sobre deepfakes, em [GANs/12](GANs/12-Riscos-Deepfakes-e-Lei.md), em 06/10/2026. A reforma tributária está em transição até 2033. Parte das tarifas não foi conferida ([23](Ecommerce/23-Outros-Marketplaces.md) e [34](Ecommerce/34-TikTok-Shop-Ads-e-GMV-Max.md) de E-commerce), nem os recursos GMV Max e Proteção de ROAS da Shopee ([29](Ecommerce/29-Shopee-Ads.md)), como as próprias notas dizem. Confira na fonte antes de decidir. Finanças é educação financeira, não assessoria.
- **Partes geradas.** As 498 notas de `Cerebro/GitHub/*/Fontes/` e os 4 índices gerados mostram `Â·` no lugar de `·`. A causa é a codificação do `converter-fontes.ps1` lido pelo Windows PowerShell 5.1 (veja "Rodar os scripts da importação"). Num clone novo, `.imports/baixar-fontes.ps1` para com "Contagem divergente" no obsidian-second-brain: o arquivo `scripts/eval/retrieval_cases.example.jsonl` ficou fora do git por causa do `.gitignore` do próprio projeto importado. Apague `.imports/eugeniughelbur--obsidian-second-brain` antes de rodar o script.
- **Instruções de terceiros.** `.imports/` traz o obsidian-second-brain inteiro, com `CLAUDE.md`, `SKILL.md` e `.claude-plugin/`. As mesmas instruções estão como notas dentro do cofre, em `Cerebro/GitHub/Second-Brain/Fontes/` (`CLAUDE.md.md`, `SKILL.md.md` e `_claude-plugin/`). Essa pasta fica fora da busca do Obsidian, mas não de um agente que leia os arquivos. Um agente que trabalhe no cofre pode tomar essas instruções como se fossem do cofre.
- **Este README é um `.md` na raiz do cofre.** O Obsidian o mostra como nota (com ele, são 810). Ele também entra no corpus da GAN de texto: `gan_das_notas.py` lê todo `.md` do cofre, menos as pastas que começam com ponto (`.imports`, `.obsidian`) e as chamadas `Templates`, `Diario`, `Inbox`, `Fontes`, `exportacao` e `exemplos`. As 301 notas citadas em GANs/10 passam a 302.
