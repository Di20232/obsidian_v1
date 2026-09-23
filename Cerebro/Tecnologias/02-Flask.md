---
tags: [tecnologia, python, flask, web]
cssclasses: [cerebro-nota, cerebro-python]
---

# Flask — a fase web intermediária do CTL-TINTA-FL

Micro-framework web em Python. Foi a **segunda das três vidas** do [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]: substituiu o Tkinter e depois cedeu lugar ao [[01-Reflex|Reflex]].

## O que foi construído nessa fase

| Peça | Papel |
|---|---|
| `app.py` | Servidor com cerca de 60 rotas e a lógica de negócio |
| `db.py` | Camada de banco — **extraída do Tkinter e reaproveitada** |
| `templates/` | 7 páginas Jinja2: base, dashboard, entrada, despacho, estoque, relatórios, cadastros |
| `iniciar.bat` | Localiza o Python, instala o Flask se faltar, abre o navegador |

Embora a fase tenha sido substituída, **o aprendizado ficou** — e o `db.py` sobreviveu intacto para o Reflex.

## O que valeu a pena e continua valendo

**CSRF em formulários.** Implementado com `hmac`, e não com hash caseiro. O detalhe que importa: a `secret_key` precisa ser **persistida em disco**. Se ela for gerada a cada boot, toda sessão é invalidada no restart — usuários deslogados e tokens CSRF quebrados.

**Endpoint de consulta em tempo real.** Uma rota `/api/saldo/<id>` alimentava o saldo do item na tela de despacho enquanto o usuário escolhia — sem recarregar a página.

**Validação por rota testável via curl.** Todas as rotas verificadas antes da entrega:

```bash
for r in / /entrada /despacho /estoque /relatorios /cadastros; do
  echo "$r -> $(curl -s -o /dev/null -w "%{http_code}" "http://localhost:5000$r")"
done
```

## A lição estrutural

> [!programacao] Separar banco de interface pagou-se sozinho
> O `db.py` atravessou **três interfaces completamente diferentes** — Tkinter, Flask e Reflex — sem reescrita. Quando a camada de dados não sabe quem a chama, trocar de framework deixa de ser reescrita e vira substituição.

## Links relacionados

- Projeto: [[../Projetos/05-CTL-TINTA-FL|CTL-TINTA-FL]]
- Tecnologia: [[01-Reflex|Reflex — a fase seguinte]]
- Trilha: [[../../Python/00-Indice|Python]]
