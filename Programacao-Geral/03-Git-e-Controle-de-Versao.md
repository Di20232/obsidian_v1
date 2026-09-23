---
tags: [programacao, git, fundamentos]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Git e Controle de Versão

## O problema que isso resolve

Sem uma ferramenta de controle de versão, times (ou até uma pessoa sozinha) acabam com pastas chamadas `projeto_final`, `projeto_final_v2`, `projeto_final_v2_CORRIGIDO`. Isso não escala e não permite saber **quem mudou o quê, quando, e por quê**, nem voltar com segurança para uma versão anterior se algo quebrar. **Git** é a ferramenta padrão da indústria para resolver exatamente isso: ele guarda o histórico completo de mudanças de um projeto de código.

## Conceitos-chave

- **Repositório**: uma pasta cujo histórico de mudanças o Git está rastreando.
- **Commit**: uma "fotografia" do estado do código em um momento, com uma mensagem explicando o que mudou e por quê.
- **Branch (ramo)**: uma linha independente de desenvolvimento — permite experimentar ou desenvolver uma funcionalidade sem afetar o código principal até que esteja pronto.
- **Remoto (remote)**: uma cópia do repositório hospedada em outro lugar (geralmente no GitHub), usada para backup e colaboração entre pessoas.

## Fluxo básico

```bash
git init                          # transforma a pasta atual em um repositório Git
git status                        # mostra o que mudou desde o último commit
git add arquivo.py                # marca um arquivo para entrar no próximo commit ("staging")
git add .                         # marca todos os arquivos modificados
git commit -m "Adiciona validação de idade"   # grava um commit com uma mensagem
git log                           # mostra o histórico de commits
```

**Por que existe a etapa de `add` separada do `commit`**: isso permite escolher exatamente quais mudanças entram em cada "fotografia", em vez de ser tudo-ou-nada — útil quando você mudou várias coisas não relacionadas e quer separá-las em commits distintos e organizados.

## Branches

```bash
git branch nova-funcionalidade     # cria um novo branch
git checkout nova-funcionalidade   # muda para esse branch
git checkout -b outra-funcionalidade  # cria e já muda, em um comando só

git checkout main                  # volta para o branch principal
git merge nova-funcionalidade      # traz as mudanças do branch de volta para main
```

**Por que branches importam**: em um time, cada pessoa trabalha em seu próprio branch, sem interferir no código dos outros até que sua parte esteja pronta e revisada. Mesmo sozinho, é útil para testar uma ideia arriscada sem comprometer o código que já funciona.

## Trabalhando com um remoto (GitHub)

**GitHub** é um serviço que hospeda repositórios Git na internet — não é o Git em si, é uma plataforma construída em torno dele (existem alternativas: GitLab, Bitbucket).

```bash
git clone https://github.com/usuario/repositorio.git   # baixa um repositório existente
git push                           # envia seus commits locais para o remoto
git pull                           # baixa commits novos que outras pessoas enviaram
```

## Pull Request (PR)

Em times, a forma padrão de integrar código não é dar `push` direto no branch principal — é abrir um **Pull Request**: uma proposta formal de "aqui está o que eu mudei no meu branch, revisem antes de aceitar no principal". Isso permite revisão de código (outra pessoa lê e comenta antes de aprovar) e é uma das práticas mais centrais do desenvolvimento profissional colaborativo.

## `.gitignore`

Um arquivo especial que lista o que o Git **não** deve rastrear — por exemplo, ambientes virtuais (`venv/`, visto em [[../Python/16-Boas-Praticas-e-Proximos-Passos]]), arquivos temporários, ou segredos como senhas e chaves de API. Isso evita que dados sensíveis ou volumosos demais acabem no histórico compartilhado.

```
# .gitignore
venv/
__pycache__/
*.pyc
.env
```

## Erros comuns de quem está começando

- Fazer commits gigantes com dezenas de mudanças não relacionadas, misturando tudo — dificulta entender o histórico depois.
- Mensagens de commit vagas como "ajustes" ou "fix" — prefira mensagens que expliquem o "porquê" da mudança.
- Colocar senhas/chaves direto no código e dar commit — uma vez no histórico do Git, é difícil remover completamente, mesmo apagando depois.

## Exercício

Instale o Git (`git-scm.com`), configure seu nome e e-mail (`git config --global user.name "Seu Nome"` e `git config --global user.email "seu@email.com"`), crie uma pasta de teste, rode `git init`, crie um arquivo, e faça seu primeiro commit.

---
Próxima nota: [[04-Estruturas-de-Dados]]
