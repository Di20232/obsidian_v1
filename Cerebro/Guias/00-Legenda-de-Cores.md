---
tags: [guia, obsidian, organizacao]
cssclasses: [cerebro-nota, cerebro-geral]
---

# 🎨 Legenda de Cores

As cores tornam o cofre mais rápido de ler. Elas indicam o **assunto**, não a importância da nota.

| Cor | Assunto |
|---|---|
| Roxo | central do cérebro, organização e repositórios do GitHub |
| Azul | fundamentos e programação geral |
| Verde | Python |
| Amarelo | JavaScript |
| Púrpura | PHP |
| Ciano | CSS |
| Verde-água | Tailwind e dados |
| Azul-royal | MySQL |
| Verde-esmeralda | SQLite |
| Laranja-escuro | Web e ByteShop |
| Índigo | engenharia de software |
| Laranja | projetos e produto |
| Rosa | problemas resolvidos |
| Vermelho | segurança |
| Magenta | IA, automação e Bootstrap |
| Verde-limão | práticas de trabalho |
| Cinza | ambiente e infraestrutura |
| Rosa-choque | e-commerce, Shopify e divulgação |
| Dourado | finanças do pequeno negócio |

## Como funciona

O snippet ativo é `cerebro-todas-as-notas`. Ele aplica títulos, links, faixa lateral e fundo sutil por assunto, tanto na leitura quanto na edição. Os tons são ajustados para temas claro e escuro. As pastas das notas também recebem cores no explorador de arquivos.

No grafo, cada uma das 22 classes de assunto tem um grupo de cor em `.obsidian/graph.json`, com o tom do tema escuro. Central e GitHub, IA e Bootstrap usam a mesma cor em todo lugar. Tailwind e dados, Web e projetos têm tons diferentes no tema claro e ficam iguais no grafo e no tema escuro.

O outro snippet, `cerebro-cores`, é a paleta antiga: fica desligado e não precisa ser ativado.

Todas as notas de estudo e do Cérebro, inclusive as importadas, recebem uma classe base e uma classe de assunto. Para manter o padrão em uma nota nova:

```yaml
cssclasses: [cerebro-nota, cerebro-projetos]
```

Classes de assunto: `cerebro-geral`, `cerebro-programacao`, `cerebro-python`, `cerebro-javascript`, `cerebro-php`, `cerebro-css`, `cerebro-bootstrap`, `cerebro-tailwind`, `cerebro-mysql`, `cerebro-sqlite`, `cerebro-web`, `cerebro-dados`, `cerebro-engenharia`, `cerebro-seguranca`, `cerebro-ia`, `cerebro-projetos`, `cerebro-problemas`, `cerebro-praticas`, `cerebro-ambiente`, `cerebro-github`, `cerebro-ecommerce` e `cerebro-financas`.

As cores foram configuradas usando [CSS snippets](https://help.obsidian.md/Extending+Obsidian/CSS+snippets) e [cssclasses](https://help.obsidian.md/Editing+and+formatting/Properties), recursos documentados do Obsidian. A verificação foi feita nos arquivos; a aparência não foi inspecionada na janela do aplicativo nesta etapa.

Os modelos de nota de projeto e de decisão já trazem `cerebro-projetos`, e o de problema traz `cerebro-problemas`. Os de diário e de revisão semanal trazem `cerebro-geral`. Os de conceito e de tecnologia também trazem `cerebro-geral`: troque pela classe do assunto, como fazem as notas de [[Tecnologias/00-Indice|Tecnologias]] (por exemplo, `cerebro-python`).

Veja também: [[00-Indice|Guias]] · [[Templates/00-Modelos|Modelos de nota]].
