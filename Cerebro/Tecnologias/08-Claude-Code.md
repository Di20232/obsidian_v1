---
tags: [tecnologia, ferramentas, claude-code, automacao]
cssclasses: [cerebro-nota, cerebro-engenharia]
---

# Claude Code — configuração e plugins

Ferramenta usada para conduzir as sessões de desenvolvimento registradas neste cérebro.

## Arquivos de configuração do projeto

| Arquivo | Papel |
|---|---|
| `CLAUDE.md` | Contexto do projeto: stack, convenções, decisões |
| `.claude/settings.json` | Permissões e configuração |
| `.claude/launch.json` | Como subir o servidor de desenvolvimento |

**Convenção adotada nos projetos deste cofre:** commits escritos em português.

## Plugin e marketplace não são a mesma coisa

Erro encontrado ao tentar instalar um plugin: *repositório selecionado não é um marketplace*. → [[../Problemas-Resolvidos/02-Repositorio-nao-e-Marketplace|nota do caso]]

A distinção:

| Arquivo presente | O que o repositório é |
|---|---|
| `.claude-plugin/plugin.json` | Um **plugin** individual |
| `.claude-plugin/marketplace.json` | Um **marketplace** que lista vários plugins |

Tentar adicionar um plugin como se fosse marketplace produz exatamente aquele erro.

**Solução que funcionou:** criar um marketplace local mínimo apontando para o plugin já clonado, registrá-lo e instalar a partir dele — tudo pelo terminal, sem precisar de sessão interativa:

```bash
claude plugin marketplace add <caminho-do-marketplace-local>
```
```bash
claude plugin install <nome>@local-plugins
```
```bash
claude plugin list
```

## Sobre chaves de API de provedores

Plugins que consultam vários modelos precisam de chaves de API configuradas como variável de ambiente.

> [!seguranca] Nunca guarde a chave aqui
> Registre neste cofre apenas o **nome da variável** (por exemplo `OPENROUTER_API_KEY`) e onde obtê-la. O valor vai em variável de ambiente do usuário, nunca em nota, commit ou conversa.

## Configuração de `launch.json` que evitou um problema recorrente

```json
{ "autoPort": true }
```

Com isso, se a porta preferida estiver ocupada, o servidor escolhe outra em vez de falhar. Resolveu o caso da [[../Problemas-Resolvidos/18-Porta-3000-Presa-por-Processo-Orfao|porta 3000 presa por processo órfão]].

## Links relacionados

- Prática: [[../Praticas/09-Como-Trabalhamos|Como trabalhamos]]
- Problema: [[../Problemas-Resolvidos/02-Repositorio-nao-e-Marketplace|Repositório não é marketplace]]
