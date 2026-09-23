---
tags: [sqlite, mysql, comparacao]
cssclasses: [cerebro-nota, cerebro-sqlite]
---

# SQLite vs. MySQL: Quando Usar Cada Um

## Não existe "o melhor" — existe o adequado ao problema

Depois de aprender os dois ([[../MySQL/00-Indice]] e esta trilha), a pergunta certa não é "qual é melhor", é "qual se encaixa neste projeto específico". Esta nota resume os critérios de decisão.

## Tabela de decisão

| Critério | SQLite | MySQL |
|---|---|---|
| Configuração | zero — é um arquivo | precisa instalar e configurar um servidor |
| Múltiplos usuários escrevendo ao mesmo tempo | limitado | feito para isso |
| Site/app com muitos usuários simultâneos | não recomendado | recomendado |
| App mobile ou desktop com dados locais | ideal | exagero |
| Protótipos e aprendizado | ideal | também funciona, mais fricção para começar |
| Múltiplos servidores acessando o mesmo banco | não é possível (é um arquivo local) | sim, natural |
| Controle de usuários e permissões granulares | não existe | sim ([[../MySQL/09-Transacoes-e-Usuarios]]) |
| Volume de dados muito grande, com necessidade de escalar | limitado | melhor preparado |

## Sinais de que SQLite é suficiente

- O banco é usado por **um único programa** por vez (um app, um script).
- Você está prototipando ou aprendendo, e não quer a fricção de configurar um servidor.
- Os dados são **locais** ao dispositivo/usuário, não compartilhados entre várias pessoas.
- O volume de escrita simultânea é baixo.

## Sinais de que você precisa de MySQL (ou PostgreSQL)

- Um site com **vários usuários acessando e alterando dados ao mesmo tempo** — o cenário mais comum de aplicações web reais.
- Você precisa de **usuários e permissões** distintos por aplicação ou por pessoa ([[../MySQL/09-Transacoes-e-Usuarios]]).
- O sistema vai **crescer** e eventualmente rodar em mais de um servidor acessando o mesmo banco.
- Você precisa de recursos avançados de administração, replicação, ou monitoramento em escala.

## Um caminho comum na prática

Muitos projetos começam com SQLite durante o desenvolvimento (mais simples, sem depender de infraestrutura) e migram para MySQL/PostgreSQL ao ir para produção, quando a concorrência de usuários reais passa a importar. Frameworks como Django (Python) e Laravel (PHP, [[../PHP/15-Boas-Praticas-e-Proximos-Passos]]) facilitam essa troca, porque o código de aplicação (via ORM, mencionado em [[../MySQL/10-MySQL-com-PHP-e-Python]]) muda pouco ou nada entre os dois — só a configuração de conexão muda.

## Ambos falam o mesmo SQL, na prática

Como você viu ao longo desta trilha, o SQL que você aprendeu em [[../MySQL/00-Indice]] funcionou quase sem alteração aqui — isso não é coincidência, é o valor de aprender o **padrão SQL**, discutido desde [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]], em vez de decorar comandos de um banco específico.

## Exercício

Para cada cenário abaixo, decida SQLite ou MySQL e justifique em uma frase: (1) um aplicativo de anotações para celular, sem sincronização online; (2) um site de e-commerce com milhares de pedidos por dia; (3) um script pessoal que organiza seus arquivos de música localmente; (4) uma rede social com posts e comentários de múltiplos usuários.

---
Próxima nota: [[07-Boas-Praticas-e-Proximos-Passos]]
