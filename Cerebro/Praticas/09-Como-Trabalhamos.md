---
tags: [pratica, processo, colaboracao]
cssclasses: [cerebro-nota, cerebro-praticas]
---

# Como trabalhamos — o método observado

Padrões que se repetiram nas 19 sessões e produziram bons resultados. Não é teoria: é o que de fato aconteceu.

## O ciclo que funcionou

```
usar o sistema de verdade
   → encontrar o problema real
      → investigar até a causa-raiz
         → corrigir
            → confirmar com evidência
               → registrar
```

O primeiro passo é o mais subestimado. **Quase todos os bugs deste cofre foram encontrados usando o sistema, não lendo o código.** Os selects cinza, o texto invisível, o saldo sem sentido, o botão que não exclui — nenhum apareceria em revisão de código.

## O que caracteriza uma boa investigação aqui

**Confirmar antes de concluir.** O caso da [[../Problemas-Resolvidos/05-Exclusao-Nao-Funciona-em-Cadastros|exclusão que não funcionava]] teve três causas sucessivas. Cada uma parecia definitiva. Só a checagem no banco encerrou o assunto.

**Evidência executada, não suposta.** Contar quantas linhas estão travadas por chave estrangeira leva trinta segundos e substitui uma hora de teoria.

**Verificar o resultado compilado, não o fonte.** No Reflex, inspecionar o bundle foi o que provou que os botões haviam de fato deixado de ser links.

**Dizer o que ficou de fora.** Quando os workflows falharam nos arquivos grandes, isso foi registrado como pendência aberta em vez de ser dissolvido num resumo otimista.

## Convenções adotadas

- **Commits em português**, descrevendo o que mudou e por quê
- `CLAUDE.md` em cada projeto com stack e convenções
- `.env` sempre fora do Git
- Confirmar antes de ações destrutivas — parar containers, apagar pasta, encerrar processo
- Antes de encerrar um processo, **ver a linha de comando dele** ([[../Problemas-Resolvidos/18-Porta-3000-Presa-por-Processo-Orfao|por quê]])

## Sinais de que a investigação está no caminho errado

- A correção é aplicada mas o sintoma volta → a causa-raiz não foi encontrada, só um sintoma intermediário
- Não há como demonstrar que funcionou → falta evidência
- A explicação exige "deve ser" ou "provavelmente" → ainda é suposição

## Registrar é parte do trabalho

Uma investigação bem-feita que não vira nota precisa ser refeita inteira da próxima vez. O registro custa cinco minutos e é o que separa este cofre de uma pasta de código.

Use [[../Templates/Template-Problema|Template de Problema]] logo após confirmar a correção — não semanas depois, quando o detalhe já se perdeu.

## Links relacionados

- Práticas: [[01-Feedback-Rapido|Feedback rápido]] · [[02-Definicao-de-Pronto|Definição de pronto]] · [[03-Documentacao-Que-Ajuda|Documentação que ajuda]] · [[06-Caca-de-Bugs|Caça de bugs]]
- Tecnologia: [[../Tecnologias/08-Claude-Code|Claude Code]]
