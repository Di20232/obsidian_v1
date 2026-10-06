---
tags: [ia, gans, deepfake, seguranca, lgpd, legislacao, flashcards]
aliases: [Deepfakes]
cssclasses: [cerebro-nota, cerebro-ia]
verificado_em: 2026-10-06
fonte: https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-610-de-18-de-dezembro-de-2019
---

# Riscos, deepfakes e lei

Um **deepfake** é um vídeo, áudio ou imagem **sintético** que imita uma pessoa real: o rosto, a voz, os gestos. As GANs tornaram rostos falsos indistinguíveis a olho nu ([[06-Arquiteturas-Importantes|StyleGAN]]), mas não são a única técnica. A troca de rostos em vídeo costuma usar **autoencoders**, e hoje a clonagem de voz e os modelos de difusão fazem boa parte do trabalho. O risco é o mesmo, qualquer que seja a técnica.

> [!warning] Isto não é parecer jurídico
> A nota resume regras em vigor para orientar o estudo e o uso responsável (conferido em 06/10/2026). Em um caso concreto, procure um advogado.

> [!info] Fontes conferidas em 06/10/2026
> [Resolução TSE nº 23.610/2019, texto compilado](https://www.tse.jus.br/legislacao/compilada/res/2019/resolucao-no-23-610-de-18-de-dezembro-de-2019) (com as alterações das Resoluções 23.732/2024 e 23.755/2026), [Lei nº 15.123/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15123.htm) e [LGPD, Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm). Regras eleitorais mudam a cada eleição: confira a versão em vigor antes de usar.

## Os riscos

- **Fraude:** voz clonada de um parente ou de um chefe pedindo um Pix urgente; vídeo falso de uma celebridade anunciando investimento.
- **Desinformação:** candidato "dizendo" o que nunca disse, às vésperas da eleição.
- **Conteúdo íntimo falso:** montagens sexuais de pessoas reais sem consentimento, usadas para humilhar, chantagear ou perseguir.
- **Difamação e assédio:** colocar alguém em situação que nunca aconteceu.
- **Prova falsa e o "dividendo do mentiroso":** quando qualquer vídeo pode ser falso, quem foi flagrado de verdade passa a alegar que o vídeo é montagem.

## O que diz a lei no Brasil

### Propaganda eleitoral

A Resolução TSE nº 23.610/2019, que regula a propaganda eleitoral, ganhou regras sobre IA com a **Resolução nº 23.732/2024**, depois ampliadas pela **Resolução nº 23.755/2026**.

- **Rotular (art. 9º-B):** conteúdo sintético feito com IA "ou tecnologia equivalente" para criar, substituir, omitir, mesclar ou alterar imagens ou sons obriga o responsável a **avisar de modo explícito, destacado e acessível** que o conteúdo foi fabricado ou manipulado, e com qual tecnologia. O aviso vai no início dos áudios; como rótulo (marca d'água) e na audiodescrição das imagens; nas duas formas nos vídeos; e em cada página de material impresso. Ajustes de qualidade de imagem e som, vinhetas, logomarcas e montagens costumeiras de campanha estão fora da regra.
- **Sem simular conversa (art. 9º-B, § 3º):** chatbots e avatares de campanha seguem a mesma regra e não podem simular conversa com o candidato ou com outra pessoa real.
- **Silêncio sintético na eleição (art. 9º-B, § 3º-A, de 2026):** é proibido publicar, republicar ou impulsionar conteúdo sintético **novo** com imagem, voz ou manifestação de candidato ou pessoa pública, **mesmo rotulado**, das 72 horas antes até as 24 horas depois do fim da votação.
- **Proibir o deepfake (art. 9º-C, § 1º):** é **proibido** usar, para prejudicar ou favorecer candidatura, áudio ou vídeo sintético que crie, substitua ou altere a imagem ou a voz de pessoa viva, falecida ou fictícia (*deep fake*), **mesmo com autorização** da pessoa.
- **Consequências:** o conteúdo irregular deve ser removido de imediato, por iniciativa da plataforma ou por ordem judicial (art. 9º-B, § 4º). O deepfake configura abuso de poder e uso indevido dos meios de comunicação, e pode levar à **cassação do registro ou do mandato** (art. 9º-C, § 2º).

### Violência psicológica contra a mulher

A **Lei nº 15.123/2025** acrescentou um parágrafo ao art. 147-B do Código Penal: a pena do crime de violência psicológica contra a mulher é **aumentada de metade** quando ele é cometido com **inteligência artificial** ou outro recurso tecnológico que **altere imagem ou som da vítima**.

### Imagem, voz e dados pessoais

- A **Constituição** (art. 5º, X) protege a intimidade, a vida privada, a honra e a **imagem** das pessoas e garante indenização por dano material ou moral.
- O **Código Civil** (art. 20) permite proibir o uso não autorizado da imagem de alguém e pedir indenização, quando o uso atinge a honra ou tem fins comerciais.
- A **LGPD** (Lei 13.709/2018) trata imagem e voz de pessoa identificável como **dado pessoal**. Quando usados para identificar a pessoa (reconhecimento facial ou de voz), viram **dado biométrico**, classificado como **dado pessoal sensível** (art. 5º, II), que só pode ser tratado nas hipóteses restritas do art. 11. Treinar um gerador com fotos de pessoas reais exige base legal e cuidado ([[IA-Aplicada/09-Riscos-Seguranca-e-LGPD-na-IA|riscos e LGPD na IA]]).

## Boas práticas para quem cria

1. **Consentimento por escrito** de quem aparece ou tem a voz usada, com a finalidade descrita.
2. **Rotular** todo conteúdo sintético que alguém possa tomar por real, mesmo fora de eleição.
3. **Procedência:** quando a ferramenta oferece, mantenha as credenciais de conteúdo (padrão **C2PA**, da coalizão criada em 2021 por empresas como Adobe, Microsoft e BBC), que registram como o arquivo foi criado e editado.
4. **Dados de treino** próprios, licenciados ou com base legal; nunca fotos de terceiros "achadas" na internet.
5. **Nunca** gerar conteúdo sexual, difamatório ou eleitoral envolvendo pessoas reais.

Os experimentos deste cofre seguem essa linha: a GAN 2D usa pontos sintéticos, e a [[10-Experimento-GAN-com-as-Notas|GAN de texto]] usa só as próprias notas, sem as pastas pessoais.

## Como se defender

- **Golpe por voz ou vídeo:** desligue e **ligue de volta** para o número que você já conhece. Combine com a família uma **pergunta ou palavra-chave** que só vocês saibam. Urgência + pedido de dinheiro é o sinal de alerta.
- **Conteúdo suspeito:** procure a **origem** (quem publicou primeiro?), faça busca reversa da imagem e consulte agências de checagem antes de compartilhar.
- **Detectores automáticos:** servem como pista, não como prova. Erram com geradores novos e dão falsos positivos. Nunca acuse alguém só com base neles.
- **Sinais visuais** (mãos, dentes, brincos diferentes, fundo distorcido, reflexo nos olhos) já ajudaram muito, mas ficam menos confiáveis a cada geração de modelos.

## Perguntas de revisão

O que é um deepfake? :: Um vídeo, áudio ou imagem sintético que imita o rosto, a voz ou os gestos de uma pessoa real.

Todo deepfake é feito com GAN? :: Não; troca de rostos costuma usar autoencoders, e clonagem de voz e modelos de difusão também são usados.

O que é o dividendo do mentiroso? :: Quando qualquer vídeo pode ser falso, quem foi flagrado de verdade passa a alegar que a prova é montagem.

O que o art. 9º-B da Resolução TSE 23.610/2019 exige na propaganda eleitoral? :: Que conteúdo sintético feito com IA ou tecnologia equivalente traga aviso explícito, destacado e acessível de que foi fabricado ou manipulado e de qual tecnologia foi usada (conferido em 06/10/2026).

Um candidato pode usar deepfake na propaganda se a pessoa retratada autorizar? :: Não; o art. 9º-C da Resolução TSE 23.610/2019 proíbe o deepfake para prejudicar ou favorecer candidatura mesmo com autorização (conferido em 06/10/2026).

Qual a consequência de usar deepfake na propaganda eleitoral? :: Configura abuso de poder e uso indevido dos meios de comunicação e pode levar à cassação do registro ou do mandato (conferido em 06/10/2026).

O que a Resolução TSE 23.755/2026 proibiu perto do dia da eleição? :: Publicar, republicar ou impulsionar conteúdo sintético novo com imagem, voz ou manifestação de candidato ou pessoa pública, mesmo rotulado, das 72 horas antes às 24 horas depois do fim da votação (conferido em 06/10/2026).

Um chatbot de campanha pode simular conversa com o candidato? :: Não; a Resolução TSE 23.610/2019 proíbe chatbots e avatares de simular conversa com o candidato ou outra pessoa real (conferido em 06/10/2026).

O que mudou com a Lei 15.123/2025? :: A pena da violência psicológica contra a mulher passou a ser aumentada de metade quando o crime usa IA ou recurso que altere imagem ou som da vítima.

Como a LGPD classifica dado biométrico? :: Como dado pessoal sensível, quando vinculado a uma pessoa natural (art. 5º, II), tratável só nas hipóteses do art. 11.

O que é o padrão C2PA? :: Um padrão de credenciais de conteúdo que registra como um arquivo foi criado e editado, para indicar sua procedência.

Qual a melhor defesa contra golpe de voz clonada pedindo dinheiro? :: Desligar e ligar de volta para o número já conhecido, e combinar com a família uma palavra-chave.

Detectores de deepfake servem como prova? :: Não; erram com geradores novos e dão falsos positivos, então servem só como pista.

---
Anterior: [[11-GANs-Difusao-e-Outros-Geradores|GANs, difusão e outros geradores]] · Trilha: [[GANs/00-Indice|GANs]]
