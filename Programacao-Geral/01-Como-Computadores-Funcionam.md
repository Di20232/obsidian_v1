---
tags: [programacao, fundamentos]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Como Computadores Funcionam

## Por que aprender isso antes de ir mais fundo

Todo conceito de programação — variável, função, arquivo — é, no fundo, uma abstração sobre como o hardware realmente funciona. Entender essa base ajuda a entender **por que** as linguagens de programação são como são, e por que certas operações são rápidas e outras lentas.

## As peças principais

- **CPU (processador)**: executa instruções, uma de cada vez, extremamente rápido (bilhões por segundo). É a "força de trabalho" do computador — ele não entende Python, só entende um conjunto pequeno e fixo de instruções muito básicas (somar, comparar, mover dados).
- **RAM (memória)**: um espaço de armazenamento temporário e rápido, onde ficam os dados e o código que estão sendo usados **agora**. É apagada quando o computador desliga — por isso variáveis somem quando o programa termina, como mencionado em [[../Python/14-Arquivos]].
- **Disco (SSD/HD)**: armazenamento permanente, mais lento que a RAM, mas que mantém os dados mesmo sem energia. É onde seus arquivos `.py`, fotos e documentos vivem.
- **Sistema Operacional (Windows, Linux, macOS)**: o programa que gerencia todos os outros — decide qual programa usa a CPU em cada instante, organiza arquivos em disco, controla acesso a teclado, tela, rede. Todo programa que você roda, incluindo o interpretador Python, roda **em cima** do sistema operacional, através dele.

## Do código-fonte à execução

1. Você escreve código-fonte (texto legível por humanos), como visto em [[../Python/01-O-que-e-Programacao]].
2. Esse texto precisa virar **instruções de máquina** (código binário) para a CPU executar. Isso acontece de duas formas:
   - **Compilação**: um programa (compilador) traduz todo o código de uma vez, gerando um arquivo executável separado, antes de rodar (típico de C, visto em [[11-C-e-Memoria]]).
   - **Interpretação**: um programa (interpretador) lê e traduz o código enquanto executa, linha a linha ou por um bytecode intermediário (é o caso do Python).

## Binário: a linguagem real da máquina

No fim, tudo — números, texto, imagens, o próprio código — é armazenado e processado como sequências de **bits** (0 e 1). Um caractere de texto, por exemplo, é internamente um número (existe uma tabela, chamada Unicode/ASCII, que mapeia cada caractere para um número). Você nunca vai precisar manipular binário diretamente na maior parte do trabalho do dia a dia, mas é útil saber que, por baixo de tudo, é sempre isso.

## Por que isso afeta decisões reais de programação

- Ler/escrever em disco (arquivos, bancos de dados) é **ordens de magnitude mais lento** que operar na RAM — por isso programas evitam acessar disco repetidamente dentro de um loop crítico.
- A CPU processa uma instrução de cada vez por núcleo — "paralelismo" (fazer várias coisas ao mesmo tempo de verdade) depende de ter múltiplos núcleos e código escrito para aproveitá-los.
- Memória RAM é limitada — carregar um arquivo de 50 GB inteiro de uma vez pode esgotar a memória disponível; por isso [[../Python/14-Arquivos]] mostrou como ler um arquivo linha por linha em vez de tudo de uma vez.

## Exercício mental

Pense no comando que você já rodou, `python meu_arquivo.py` (visto em [[../Python/03-Primeiro-Programa]]). Liste, em ordem, o que acontece: o sistema operacional localiza o programa `python`, carrega esse programa na RAM, a CPU começa a executar suas instruções, o interpretador lê seu arquivo `.py` do disco, traduz e executa cada linha. Visualizar essa cadeia ajuda a entender onde cada tipo de lentidão ou erro pode aparecer.

---
Próxima nota: [[02-Terminal-e-Linha-de-Comando]]
