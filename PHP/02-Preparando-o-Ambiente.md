---
tags: [php, setup, flashcards]
cssclasses: [cerebro-nota, cerebro-php]
---

# Preparando o Ambiente

## O que você precisa

1. O **interpretador PHP** instalado.
2. Um **servidor web** para receber requisições HTTP e acionar o PHP — para aprender, o próprio PHP já traz um servidor embutido, sem precisar instalar Apache/Nginx.

## Instalando o PHP no Windows

1. Baixe o PHP em `windows.php.net/download` (escolha a versão "Thread Safe" mais recente, em ZIP).
2. Extraia o conteúdo, por exemplo, em `C:\php`.
3. Adicione `C:\php` ao **PATH** do sistema (mesmo conceito visto em [[../Python/02-Instalando-Python]] — a lista de pastas que o terminal verifica ao procurar um comando).
4. Confirme no terminal:

```bash
php --version
```

**Alternativa mais simples para iniciantes**: instalar um pacote tudo-em-um como **XAMPP** ou **Laragon**, que já vem com PHP, MySQL (ver [[../MySQL/00-Indice]]) e um servidor Apache configurados juntos, com interface gráfica para ligar/desligar tudo. Para focar em aprender a linguagem, o PHP puro (passo acima) já é suficiente.

## Rodando o servidor embutido do PHP

Dentro da pasta do seu projeto, no terminal:

```bash
php -S localhost:8000
```

Isso inicia um servidor local na porta 8000. Abra `http://localhost:8000` no navegador para ver os arquivos `.php` daquela pasta sendo processados e exibidos como páginas web de verdade. Pare o servidor com `Ctrl+C`.

**Por que isso é necessário, diferente de Python e JavaScript**: em [[../Python/03-Primeiro-Programa]] e [[../JavaScript/03-Primeiro-Programa]], você rodava o arquivo diretamente (`python arquivo.py`, `node arquivo.js`) e via o resultado no terminal. PHP foi desenhado para ser **servido** por um servidor web e visto no **navegador** — mesmo aprendendo sozinho, você precisa desse servidor local para ver o resultado do jeito real.

Também é possível rodar um arquivo PHP puramente pelo terminal, sem servidor, útil para scripts sem HTML (vamos usar isso nas primeiras notas para simplificar):

```bash
php arquivo.php
```

## Editor de código

O mesmo **VS Code** já configurado em [[../Python/02-Instalando-Python]] funciona bem para PHP; vale instalar a extensão "PHP Intelephense" para autocompletar e checagem de sintaxe.

## Verificando que está tudo pronto

```bash
php --version
php -S localhost:8000
```

## Erros comuns nesta etapa

- Esquecer de adicionar o PHP ao PATH → `php` não é reconhecido como comando.
- Rodar `php -S localhost:8000` de dentro da pasta errada, e não achar os arquivos esperados no navegador — confira sempre em qual pasta o terminal está ([[../Programacao-Geral/02-Terminal-e-Linha-de-Comando]]).
- Confundir a porta usada (`8000`, `8080`...) e tentar abrir uma porta diferente da que o comando usou.

## Exercício

Instale o PHP, rode `php --version` para confirmar, crie uma pasta com um arquivo `teste.php` contendo `<?php echo "Funcionou!"; ?>`, rode `php -S localhost:8000` dentro dela, e abra `http://localhost:8000/teste.php` no navegador.

## Perguntas de revisão

Como iniciar o servidor embutido do PHP? :: Com php -S localhost:8000 dentro da pasta do projeto, e abrir http://localhost:8000 no navegador.

Por que PHP precisa de um servidor para ver o resultado? :: Porque foi desenhado para ser servido por um servidor web e visto no navegador.

Qual a alternativa tudo-em-um para instalar PHP no Windows? :: Pacotes como XAMPP ou Laragon, que trazem PHP, MySQL e Apache configurados.

Como rodar um arquivo PHP sem servidor? :: Pelo terminal, com php arquivo.php, útil para scripts sem HTML.

Que extensão do VS Code ajuda com PHP? :: PHP Intelephense, para autocompletar e checar sintaxe.

---
Próxima nota: [[03-Primeiro-Programa]]
