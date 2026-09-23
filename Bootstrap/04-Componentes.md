---
tags: [bootstrap, componentes]
cssclasses: [cerebro-nota, cerebro-bootstrap]
---

# Componentes

## O catálogo de peças prontas

Além do grid ([[03-Grid-System]]), o valor central do Bootstrap é seu catálogo de **componentes de interface** já estilizados e testados. Esta nota cobre os mais usados no dia a dia.

## Botões

```html
<button class="btn btn-primary">Primário</button>
<button class="btn btn-secondary">Secundário</button>
<button class="btn btn-success">Sucesso</button>
<button class="btn btn-danger">Perigo</button>
<button class="btn btn-outline-primary">Contornado</button>
<button class="btn btn-primary btn-lg">Grande</button>
<button class="btn btn-primary btn-sm">Pequeno</button>
```

O padrão `btn btn-<variante>` se repete em vários componentes do Bootstrap — `<variante>` (primary, secondary, success, danger, warning, info) é o vocabulário de cores semânticas do framework, reaproveitado em alertas, badges, textos.

## Cards

```html
<div class="card" style="width: 18rem;">
    <div class="card-body">
        <h5 class="card-title">Título do Card</h5>
        <p class="card-text">Algum texto descritivo dentro do card.</p>
        <a href="#" class="btn btn-primary">Ação</a>
    </div>
</div>
```

`card` é o container; `card-body` dá o espaçamento interno; `card-title`/`card-text` ajustam a tipografia — a mesma estrutura de card que você já construiu manualmente em [[../CSS/02-Box-Model]] e [[../CSS/08-Transicoes-e-Animacoes]], agora pronta.

## Navbar

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">MeuSite</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="menu">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item"><a class="nav-link" href="#">Início</a></li>
                <li class="nav-item"><a class="nav-link" href="#">Sobre</a></li>
            </ul>
        </div>
    </div>
</nav>
```

`navbar-expand-lg` diz "vire menu hambúrguer **abaixo** do breakpoint `lg`, e mostre os links normalmente **a partir** dele" — o mesmo padrão responsivo mobile/desktop discutido em [[../CSS/07-Responsividade]], já resolvido. Os atributos `data-bs-toggle`/`data-bs-target` são o que aciona o **JavaScript do Bootstrap** (mencionado em [[02-Instalando-e-Configurando]]) para abrir/fechar o menu, sem você escrever nenhum `addEventListener` manual (comparar com [[../JavaScript/16-DOM-e-Eventos]]).

## Formulários

```html
<form>
    <div class="mb-3">
        <label for="nome" class="form-label">Nome</label>
        <input type="text" class="form-control" id="nome" placeholder="Seu nome">
    </div>
    <div class="mb-3">
        <label for="email" class="form-label">E-mail</label>
        <input type="email" class="form-control" id="email">
    </div>
    <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

`form-control` estiliza campos de entrada de forma consistente; `form-label` estiliza os rótulos; `mb-3` (margin-bottom, ver [[05-Utilitarios-e-Responsividade]]) espaça cada grupo de campo.

## Alertas

```html
<div class="alert alert-success">Operação realizada com sucesso!</div>
<div class="alert alert-danger">Algo deu errado.</div>
```

## Modal: interatividade sem escrever JavaScript

```html
<button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#meuModal">Abrir Modal</button>

<div class="modal fade" id="meuModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Título do Modal</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">Conteúdo do modal aqui.</div>
        </div>
    </div>
</div>
```

Um modal (janela sobreposta) exigiria, em JavaScript puro, controlar visibilidade, foco, fechamento ao clicar fora, tudo manualmente (conceitos vistos em [[../JavaScript/16-DOM-e-Eventos]]). Com Bootstrap, `data-bs-toggle="modal"` + `data-bs-target="#id"` já resolve tudo isso — **desde que o `<script>` do Bootstrap JS esteja carregado**, como visto em [[02-Instalando-e-Configurando]].

## Exercício

Abra `Bootstrap/exemplos/04_componentes.html`. Monte uma página com uma navbar, 3 cards em um grid responsivo (combinando com [[03-Grid-System]]), e um botão que abre um modal.

---
Veja o exemplo em `Bootstrap/exemplos/04_componentes.html`. Próxima nota: [[05-Utilitarios-e-Responsividade]]
