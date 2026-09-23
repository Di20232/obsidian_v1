---
tags: [programacao, boas-praticas]
cssclasses: [cerebro-nota, cerebro-programacao]
---

# Boas Práticas de Código

## O que separa "funciona" de "está bom"

Um código pode dar a resposta certa e ainda assim ser problemático — difícil de entender, difícil de mudar sem quebrar algo, difícil de revisar. Boas práticas existem porque **código é lido muito mais vezes do que é escrito**, seja por outra pessoa, seja por você mesmo daqui a seis meses.

## KISS: Keep It Simple

Prefira sempre a solução mais simples que resolve o problema. Código "esperto" demais (usando truques obscuros de linguagem para economizar uma linha) geralmente custa mais tempo de leitura do que economiza de escrita.

```python
# desnecessariamente denso
resultado = [x**2 for x in range(10) if x % 2 == 0 and x > 2]

# mais simples de acompanhar, mesmo com mais linhas
resultado = []
for x in range(10):
    if x % 2 == 0 and x > 2:
        resultado.append(x ** 2)
```

Nenhuma das duas está "errada" — a primeira (list comprehension) é idiomática em Python e vale aprender depois; o ponto é: **priorize clareza sobre compactação** enquanto você não tem certeza de que a versão compacta é realmente mais legível para quem vai ler.

## DRY: Don't Repeat Yourself

Já mencionado em [[../Python/16-Boas-Praticas-e-Proximos-Passos]] — código duplicado é código que precisa ser lembrado e corrigido em vários lugares ao mesmo tempo. Extraia para uma função (visto em [[../Python/11-Funcoes]]) assim que perceber repetição.

## YAGNI: You Aren't Gonna Need It

Não construa flexibilidade ou funcionalidade "para o caso de precisar no futuro". Código extra não usado ainda é código para manter, testar e entender — sem trazer benefício nenhum enquanto não é usado. Resolva o problema que existe **agora**.

## Nomes revelam intenção

```python
# ruim
def calc(x, y, z):
    return x * y * (1 - z)

# bom: os nomes já explicam o cálculo, sem precisar de comentário
def calcular_preco_com_desconto(preco, quantidade, percentual_desconto):
    return preco * quantidade * (1 - percentual_desconto)
```

Um bom nome de função descreve **o que ela faz**; um bom nome de variável descreve **o que ela representa** — não o tipo (`lista_nomes` é melhor que `lista1`).

## Funções pequenas, com uma responsabilidade

Se uma função exige um parágrafo de comentário só para explicar tudo que ela faz, provavelmente ela está fazendo **coisas demais** e deveria ser dividida em funções menores, cada uma com um propósito único e nomeável. Isso também facilita testar cada parte isoladamente (ver [[12-Debugging-e-Testes]]).

## Tratamento de erros no lugar certo

Conectando com [[../Python/13-Tratamento-de-Erros]]: capture exceções onde você **sabe o que fazer** com o erro (mostrar uma mensagem, tentar de novo, usar um valor padrão). Capturar um erro só para silenciá-lo (`except: pass`) esconde problemas em vez de resolvê-los, e torna bugs futuros muito mais difíceis de rastrear.

## Revisão de código (code review)

Em times, é padrão que outra pessoa leia seu código antes de ele ser integrado (conectando com o conceito de Pull Request em [[03-Git-e-Controle-de-Versao]]). O objetivo não é só achar bugs — é compartilhar conhecimento do sistema entre o time e manter um padrão de qualidade consistente. Receber uma crítica no código não é uma crítica pessoal — é parte normal e saudável do processo.

## Documentação mínima que vale a pena

- Um `README.md` no projeto explicando o que ele faz e como rodar.
- **Docstrings** em funções não óbvias:

```python
def calcular_media(notas):
    """Recebe uma lista de notas e retorna a média aritmética."""
    return sum(notas) / len(notas)
```

Reserve comentários para explicar **decisões não óbvias** ("por que fizemos assim", "isso contorna um bug da biblioteca X") — não para narrar o que o código já deixa claro sozinho.

## Segurança básica que todo programador deveria saber de cor

- Nunca deixe senhas, chaves de API ou tokens direto no código-fonte — use variáveis de ambiente ou arquivos ignorados pelo Git (`.gitignore`, visto em [[03-Git-e-Controle-de-Versao]]).
- Nunca confie cegamente em dados vindos de fora (formulários, APIs, arquivos enviados por usuários) — sempre valide antes de usar.
- Ao usar SQL, sempre use parâmetros em vez de concatenar strings diretamente (visto em [[09-SQL-e-Bancos-de-Dados]]), para evitar SQL injection.

## Exercício

Pegue um dos exercícios que você já resolveu no [[../Python/00-Indice|curso de Python]] (por exemplo, o de [[../Python/09-Listas-Tuplas-Dicionarios]]) e revise: os nomes de variáveis explicam bem o que representam? Existe alguma repetição que poderia virar função? Reescreva se encontrar algo para melhorar.

---
Próxima nota: [[14-Proximos-Passos-Trilhas]]
