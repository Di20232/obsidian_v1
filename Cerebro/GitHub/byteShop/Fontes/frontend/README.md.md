---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/README.md
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# frontend/README.md

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/README.md). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend enabling type-aware lint rules by installing `oxlint-tsgolint` and editing `.oxlintrc.json`:

```json
{
  "$schema": "./node_modules/oxlint/configuration_schema.json",
  "plugins": ["react", "typescript", "oxc"],
  "options": {
    "typeAware": true
  },
  "rules": {
    "react/rules-of-hooks": "error",
    "react/only-export-components": ["warn", { "allowConstantExport": true }]
  }
}
```

See the [Oxlint rules documentation](https://oxc.rs/docs/guide/usage/linter/rules) for the full list of rules and categories.
