---
tags: [problema-resolvido, impressao, windows, suporte, flashcards]
status: roteiro-validado
cssclasses: [cerebro-nota, cerebro-problemas]
---

# Falha de impressão: Word, página de teste e Spooler

> [!problema] Sintoma
> O Word não imprime ou a página de teste falha; em alguns casos o serviço Spooler de Impressão não está em execução.

## Diagnóstico

Se a página de teste também falha, o problema não é específico do Word. Ele está em conexão, fila, serviço, driver ou configuração da impressora.

## Solução por etapas

1. **Isole o escopo:** tente imprimir um PDF ou texto simples e a página de teste.
2. **Verifique o básico:** energia, cabo USB ou conexão Wi-Fi/rede e impressora correta como padrão.
3. **Confira a fila:** identifique trabalhos parados antes de remover qualquer um.
4. **Reinicie o Spooler:** confirme que o serviço está em execução e configurado para inicialização automática, quando adequado ao ambiente.
5. **Se houver fila corrompida:** pare o serviço, remova apenas os trabalhos presos e inicie o serviço novamente. Isso cancela impressões pendentes, então avise quem enviou documentos antes.
6. **Reinstale o driver:** use o driver atual do fabricante, reinicie e teste novamente.
7. **Só se o restante funcionar:** investigue opções ou reparo do Office.

## Prevenção

- manter driver homologado e atualizado;
- documentar modelo, tipo de conexão e computador/servidor que compartilha a impressora;
- não limpar a fila sem confirmar que os trabalhos podem ser cancelados;
- testar uma página de teste após mudanças de driver ou rede.

## Links relacionados

- [[../Ambiente/00-Indice|Ambiente]]
- [[../Guias/02-Resolver-Problemas|Resolver Problemas]]

## Perguntas de revisão

Se a página de teste da impressora também falha, onde está o problema? :: Não é do Word: está na conexão, fila, serviço Spooler, driver ou configuração da impressora.

Qual o primeiro passo diante de uma falha de impressão? :: Isolar o escopo, tentando imprimir um PDF ou texto simples e a página de teste.

Qual o cuidado antes de limpar a fila de impressão? :: Avisar quem enviou documentos, porque limpar a fila cancela as impressões pendentes.

Quando investigar o Office numa falha de impressão? :: Só depois de confirmar que o resto (conexão, fila, Spooler e driver) funciona.
