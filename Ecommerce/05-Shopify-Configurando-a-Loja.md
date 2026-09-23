---
tags: [ecommerce, shopify, configuracao, passo-a-passo, flashcards]
cssclasses: [cerebro-nota, cerebro-ecommerce]
---

# Shopify: configurando a loja

A ordem importa: primeiro as **regras** da loja (Configurações), depois o **catálogo**, por último a **aparência**. Quem começa pelo tema costuma passar dias escolhendo cores e descobre na véspera que não consegue receber Pix ou calcular frete.

Os nomes dos menus abaixo são os do painel em português. Eles mudam de vez em quando; se não encontrar um item, use a busca do topo do painel.

## Etapa 1 — Conta e dados da loja

**Configurações → Geral (Detalhes da loja)**
- nome da loja, e-mail de contato e e-mail de remetente;
- **endereço e CNPJ/razão social** — aparecem em notificações e são exigidos por lei na loja (ver [[11-Fiscal-e-Legal|fiscal e legal]]);
- moeda da loja: **Real (BRL)**;
- fuso horário: Brasília; unidade de peso: kg.

> [!warning] Moeda
> Defina a moeda **antes** de cadastrar produtos e receber pedidos. Trocar depois é trabalhoso e pode ficar bloqueado quando já houver transações.

**Configurações → Idiomas:** português como idioma principal da loja.

## Etapa 2 — Plano e cobrança

**Configurações → Plano:** escolha o plano (ver [[04-Shopify-Visao-Geral|visão geral]]). O pagamento anual reduz o valor mensal. Cadastre o cartão da empresa para as faturas.

## Etapa 3 — Pagamentos

**Configurações → Pagamentos**
- ative um **provedor de pagamento de terceiros** que aceite cartão, Pix e boleto no Brasil;
- configure parcelamento: número máximo de parcelas e a partir de que parcela há juros;
- opcional: **formas de pagamento manuais** (ex.: Pix com confirmação manual), útil no começo, mas trabalhoso em volume;
- faça um **pedido de teste** com o modo de teste do provedor antes de abrir a loja.

Detalhes e armadilhas em [[07-Pagamentos-no-Brasil|pagamentos no Brasil]].

## Etapa 4 — Checkout e contas de cliente

**Configurações → Checkout**
- dados de contato: e-mail ou telefone;
- campos obrigatórios: nome completo, endereço, telefone e **CPF/CNPJ** (normalmente exigido pelo provedor de pagamento e necessário para a nota fiscal);
- consentimento para marketing por e-mail e SMS (desmarcado por padrão, por causa da LGPD);
- página de agradecimento e rastreamento de pedido.

## Etapa 5 — Frete e entrega

**Configurações → Frete e entrega**
- endereço de origem (de onde os pacotes saem);
- **perfis de frete** e zonas (Brasil; por região, se o preço mudar);
- tarifas: fixa, por peso, por valor do pedido, **frete grátis acima de X**, ou cálculo por app de frete integrado aos Correios e transportadoras;
- retirada no local, se houver ponto físico;
- peso e dimensões corretos em cada produto — sem isso, o cálculo erra.

Estratégias em [[08-Frete-e-Logistica|frete e logística]].

## Etapa 6 — Impostos

**Configurações → Impostos e tributos:** no Brasil, o preço exibido normalmente **já inclui** os tributos. Em geral não se configura cobrança de imposto separada no checkout. A emissão de nota é feita por app ou ERP. Confirme o enquadramento com o contador.

## Etapa 7 — Políticas

**Configurações → Políticas**
- **Troca e devolução** (incluindo o direito de arrependimento de 7 dias);
- **Privacidade** (LGPD);
- **Termos de serviço**;
- **Frete e prazos**;
- **Informações de contato**.

A Shopify oferece modelos, mas eles são genéricos e não seguem a lei brasileira. Adapte à [[11-Fiscal-e-Legal|legislação brasileira]] e ao seu negócio.

## Etapa 8 — Notificações

**Configurações → Notificações:** revise os e-mails de confirmação de pedido, envio (com rastreio), entrega e reembolso. Traduza o que estiver genérico e coloque sua marca. É o canal que o cliente mais lê.

## Etapa 9 — Domínio

**Configurações → Domínios:** compre um domínio pela Shopify ou conecte um que você já tem (registro.br para `.com.br`). Defina-o como **principal**, para que o endereço `.myshopify.com` redirecione.

## Etapa 10 — Equipe e permissões

**Configurações → Usuários e permissões:** cada pessoa com login próprio e só as permissões necessárias. Ative **verificação em duas etapas** na conta do dono.

## Etapa 11 — Catálogo

Cadastre produtos e coleções: [[06-Shopify-Produtos-e-Colecoes|produtos e coleções]].

## Etapa 12 — Aparência

**Loja virtual → Temas → Personalizar**
- escolha um tema gratuito oficial;
- página inicial: proposta de valor clara em uma frase, coleções principais, prova social, e frete e trocas explicados;
- **Navegação:** menu principal (coleções) e rodapé (políticas, contato, sobre, rastreio);
- **Páginas:** Sobre, Contato, Perguntas frequentes, Como comprar;
- **Preferências:** título e descrição da página inicial para buscadores ([[14-SEO-e-Conteudo|SEO]]), imagem para redes sociais, pixels de anúncio;
- teste **no celular**: a maior parte das visitas vem de lá.

## Etapa 13 — Antes de abrir

Siga o [[18-Checklist-de-Lancamento|checklist de lançamento]] e remova a senha da loja (**Loja virtual → Preferências → Acesso restrito**).

## Perguntas de revisão

Em que ordem configurar uma loja Shopify? :: Primeiro as regras da loja em Configurações, depois o catálogo, e por último a aparência do tema.

Por que definir a moeda antes de cadastrar produtos? :: Porque trocar a moeda depois é trabalhoso e pode ficar bloqueado quando já existem transações.

Quais políticas uma loja brasileira precisa publicar? :: Troca e devolução com o direito de arrependimento de 7 dias, privacidade (LGPD), termos de serviço, frete e prazos, e informações de contato.

Por que o checkout deve pedir CPF ou CNPJ? :: Porque o provedor de pagamento normalmente exige e a nota fiscal precisa do documento do comprador.

Qual teste é obrigatório antes de abrir a loja? :: Um pedido de teste completo, pago e reembolsado, feito pelo celular.

---
Anterior: [[04-Shopify-Visao-Geral|Visão geral]] · Próxima: [[06-Shopify-Produtos-e-Colecoes|Produtos e coleções]] · Trilha: [[Ecommerce/00-Indice|E-commerce]]
