---
tags: [sqlite, sql, conceitos]
cssclasses: [cerebro-nota, cerebro-sqlite]
---

# O que é SQLite

## Um banco de dados sem servidor

Em [[../MySQL/01-O-que-e-MySQL]], você viu que o MySQL roda como um **servidor** separado, esperando conexões de rede. **SQLite é radicalmente diferente**: o banco de dados inteiro é **um único arquivo** no disco (algo como `banco.db`), e não existe processo de servidor rodando em segundo plano — o programa que usa o banco **é** quem lê e escreve nesse arquivo diretamente, através de uma biblioteca embutida.

```
MySQL:   Aplicação  --- rede --->  Servidor MySQL (processo separado)  --->  Arquivos em disco
SQLite:  Aplicação  ---  lê/escreve diretamente  --->  Um único arquivo .db
```

## Por que isso é útil

- **Zero configuração**: não existe "instalar servidor", "criar usuário", "configurar porta" (comparar com [[../MySQL/02-Instalando-e-Configurando]]) — é só um arquivo.
- **Portátil**: copiar o banco inteiro é literalmente copiar um arquivo — útil para backups simples, testes, ou mover dados entre máquinas.
- **Embutido**: várias linguagens (incluindo Python, [[../Python/09-Listas-Tuplas-Dicionarios]]) já trazem suporte a SQLite embutido, sem precisar instalar nada extra.

## Onde SQLite é usado no mundo real

Não é "só para aprender" — SQLite é, provavelmente, **o banco de dados mais implantado do mundo**, em número de instalações:
- Todo aplicativo de celular (Android e iOS) que guarda dados localmente costuma usar SQLite por trás.
- Navegadores (Chrome, Firefox) usam SQLite para guardar histórico, favoritos, cookies.
- Ferramentas de desktop que precisam de um banco leve, sem depender de infraestrutura externa.

## Onde SQLite **não** é a escolha certa

- **Múltiplos programas escrevendo ao mesmo tempo, com muita concorrência**: como não há um servidor central coordenando o acesso, muitas escritas simultâneas de fontes diferentes competem por travar o arquivo — um servidor como MySQL lida melhor com isso.
- **Aplicações web com muitos usuários simultâneos**: sites com tráfego significativo geralmente precisam de um banco com servidor (MySQL, PostgreSQL), justamente pela concorrência de acesso.
- Esse trade-off é aprofundado em [[06-SQLite-vs-MySQL]].

## SQL, o mesmo padrão, com dialeto próprio

SQLite implementa o mesmo padrão SQL que você já viu em [[../Programacao-Geral/09-SQL-e-Bancos-de-Dados]] e [[../MySQL/00-Indice]] — `SELECT`, `WHERE`, `JOIN`, `GROUP BY` funcionam praticamente do mesmo jeito. As diferenças aparecem principalmente em **tipos de dado** (aprofundado em [[03-Tipos-Dinamicos-e-Tabelas]]) e em alguns comandos de administração, que nem fazem sentido em um banco sem servidor (não existe `CREATE USER`, por exemplo — não há conceito de usuário de banco separado, quem tem acesso ao arquivo tem acesso ao banco inteiro).

## Exercício

Sem escrever código ainda: pense em um aplicativo de celular que você usa offline (sem internet) e ainda assim guarda seus dados (notas, tarefas, mensagens salvas). É bem provável que ele use SQLite por trás — reflita sobre por que "sem servidor" faz sentido nesse cenário específico, comparado a um site que várias pessoas acessam ao mesmo tempo.

---
Próxima nota: [[02-Usando-SQLite]]
