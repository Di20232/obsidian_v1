---
tags: [ecommerce, shopify, catalogo, produtos]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Shopify: produtos e coleções

## Anatomia de um produto

| Campo | O que colocar | Por que importa |
|---|---|---|
| **Título** | o que é + atributo principal: "Garrafa térmica inox 500 ml" | é o que o cliente e o Google leem primeiro |
| **Descrição** | benefício, uso, medidas, material, cuidados, o que vem na caixa | responde as perguntas que viriam no atendimento |
| **Mídia** | fotos em fundo limpo, foto de uso, detalhe, escala (na mão, no ambiente); vídeo curto | no digital, a foto substitui pegar o produto na mão |
| **Preço** e **preço comparativo** | o preço comparativo (o "de") só se for real | preço "de/por" inventado é propaganda enganosa |
| **Custo por item** | quanto você paga pelo produto | a Shopify calcula margem e lucro nos relatórios |
| **SKU** | código interno único por variante | sem SKU, estoque e nota fiscal viram confusão |
| **Código de barras** (GTIN/EAN) | se o produto tiver | exigido por marketplaces e pelo Google Shopping |
| **Estoque** | quantidade por local; "rastrear quantidade" ligado | evita vender o que não tem |
| **Peso** e dimensões | do produto **embalado** | o frete é calculado com eles |
| **Tipo**, **fornecedor**, **tags** | categorias internas | alimentam coleções automáticas e filtros |
| **SEO** (listagem em buscadores) | título e descrição próprios para o Google | ver [[14-SEO-e-Conteudo\|SEO]] |
| **Status** | Ativo / Rascunho | rascunho não aparece na loja |

## Variantes

Produto com opções (tamanho, cor, voltagem) é **um produto com variantes**, não vários produtos. Cada variante tem preço, SKU, estoque, peso e foto próprios.

```text
Camiseta Básica
├── P / Preta   SKU CAM-BAS-P-PRE   estoque 12
├── M / Preta   SKU CAM-BAS-M-PRE   estoque 20
└── M / Branca  SKU CAM-BAS-M-BRA   estoque 0
```

> [!tip] SKU legível
> Um padrão como `CATEGORIA-MODELO-TAMANHO-COR` permite entender o item só pelo código na etiqueta, na nota e na planilha. É o mesmo princípio de [[Cerebro/Praticas/08-Unidades-de-Medida|tratar unidade como regra de negócio]]: um identificador ambíguo corrompe estoque e relatório.

## Coleções

Coleções agrupam produtos para navegação (menu, página inicial, filtros).

| Tipo | Como funciona | Use para |
|---|---|---|
| **Manual** | você escolhe produto por produto | vitrines curadas: "Presentes até R$ 100", "Mais vendidos" |
| **Automatizada** | entram os produtos que obedecem a condições (tag, tipo, preço, estoque) | categorias estáveis: "Camisetas" = tipo igual a Camiseta |

Coleções automáticas se mantêm sozinhas: cadastrou um produto com o tipo certo, ele aparece na coleção. Por isso vale definir **tipo** e **tags** com disciplina desde o primeiro produto.

## Cadastro em lote

**Produtos → Importar** aceita planilha CSV. Baixe o modelo da própria Shopify, preencha e importe. Antes de importar centenas de itens, **teste com 3 linhas**. A lição do [[Cerebro/Praticas/05-Importacao-de-Planilhas|cofre sobre importação de planilhas]] vale aqui: confira como a importação trata produtos já existentes, para não sobrescrever o item errado.

## Boas práticas de catálogo

- Cada foto com **texto alternativo** (acessibilidade e SEO).
- Imagens com a mesma proporção em todo o catálogo, para a grade não ficar desalinhada.
- Produto esgotado: esconder, ou manter visível com "avise-me quando chegar" (bom para produto que volta).
- Revise o catálogo inteiro no celular.

---
Anterior: [[05-Shopify-Configurando-a-Loja|Configurando a loja]] · Próxima: [[07-Pagamentos-no-Brasil|Pagamentos no Brasil]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
