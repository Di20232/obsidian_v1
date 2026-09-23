---
tags: [guia, obsidian, organizacao]
cssclasses: [cerebro-nota, cerebro-geral]
---

# 🎨 Legenda de Cores

As cores tornam o cofre mais rápido de ler. Elas indicam o **assunto**, não a importância da nota.

| Cor | Assunto |
|---|---|
| Roxo | central do cérebro e organização |
| Azul | fundamentos e programação geral |
| Verde | Python |
| Amarelo | JavaScript |
| Ciano | CSS |
| Verde-água | Tailwind e dados |
| Azul-royal | MySQL |
| Verde-esmeralda | SQLite |
| Âmbar | Web e ByteShop |
| Índigo | engenharia de software |
| Laranja | projetos e produto |
| Rosa | problemas resolvidos |
| Vermelho | segurança |
| Magenta | IA e automação |
| Verde-limão | práticas de trabalho |
| Cinza | ambiente e infraestrutura |
| Rosa-choque | e-commerce, Shopify e divulgação |

## Como funciona

O snippet ativo é `cerebro-todas-as-notas`. Ele aplica títulos, links, faixa lateral e fundo sutil por assunto, tanto na leitura quanto na edição. Os tons são ajustados para temas claro e escuro. As pastas e o grafo também recebem cores.

Todas as notas existentes e importadas recebem uma classe base e uma classe de assunto. Para manter o padrão em uma nota nova:

```yaml
cssclasses: [cerebro-nota, cerebro-projetos]
```

Classes de assunto: `cerebro-geral`, `cerebro-programacao`, `cerebro-python`, `cerebro-javascript`, `cerebro-php`, `cerebro-css`, `cerebro-bootstrap`, `cerebro-tailwind`, `cerebro-mysql`, `cerebro-sqlite`, `cerebro-web`, `cerebro-dados`, `cerebro-engenharia`, `cerebro-seguranca`, `cerebro-ia`, `cerebro-projetos`, `cerebro-problemas`, `cerebro-praticas`, `cerebro-ambiente`, `cerebro-github` e `cerebro-ecommerce`.

As cores foram configuradas usando [CSS snippets](https://help.obsidian.md/Extending+Obsidian/CSS+snippets) e [cssclasses](https://help.obsidian.md/Editing+and+formatting/Properties), recursos documentados do Obsidian. A verificação foi feita nos arquivos; a aparência não foi inspecionada na janela do aplicativo nesta etapa.

Veja também: [[00-Indice|Guias]] · [[Templates/00-Modelos|Modelos de nota]], que já trazem a classe de cor certa.
