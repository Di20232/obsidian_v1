---
tags: [moc, seguranca, privacidade]
aliases: [Mapa de Segurança]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# 🛡️ Mapa de Segurança

Segurança não é uma etapa final; é um hábito de reduzir riscos desde a primeira tela e a primeira tabela.

## Áreas essenciais

| Área | Cuidados iniciais |
|---|---|
| Identidade | senhas fortes, autenticação apropriada e recuperação segura |
| Autorização | cada pessoa acessa apenas as ações e os dados necessários |
| Dados | validar entrada, criptografar onde necessário e evitar coleta excessiva |
| Código | atualizar dependências, revisar bibliotecas e tratar erros sem vazar detalhes |
| Infraestrutura | backups testados, menor privilégio e registros de eventos relevantes |
| Pessoas | desconfiar de pedidos urgentes, links suspeitos e compartilhamento de segredos |

## Checklist antes de publicar

- [ ] Senhas, chaves e tokens não estão no repositório ou em capturas de tela.
- [ ] Entradas de formulário e API são validadas no servidor.
- [ ] Permissões são verificadas em toda ação sensível.
- [ ] Erros não mostram dados internos para quem usa o sistema.
- [ ] Backups e restauração foram pensados para os dados importantes.
- [ ] Dependências e ambiente têm um processo de atualização.

Segurança se cruza com [[01-Mapa-Web|Web]], [[02-Mapa-Dados|Dados]] e [[03-Mapa-Engenharia|Engenharia]]. Para aprofundar, registre exemplos reais e recomendações de fontes confiáveis em [[../Referencias/00-Referencias-Confiaveis|Referências]].
