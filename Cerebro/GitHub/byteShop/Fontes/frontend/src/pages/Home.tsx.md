---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/Home.tsx
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# frontend/src/pages/Home.tsx

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/Home.tsx). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```tsx
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import type { Category, Product } from '../types'
import ProductCard from '../components/ProductCard'

export default function Home() {
  const [categories, setCategories] = useState<Category[]>([])
  const [featured, setFeatured] = useState<Product[]>([])

  useEffect(() => {
    api
      .get<Category[]>('/categories')
      .then((res) => setCategories(res.data))
      .catch(() => setCategories([]))
    api
      .get('/products', { params: { sort: 'newest', page_size: 8 } })
      .then((res) => setFeatured(res.data.items))
      .catch(() => setFeatured([]))
  }, [])

  return (
    <div>
      <section className="bg-ink py-14 text-center text-white">
        <h1 className="text-3xl font-extrabold sm:text-5xl">
          Monte seu PC com quem <span className="text-brand">entende</span> de hardware
        </h1>
        <p className="mx-auto mt-4 max-w-xl text-gray-300">
          Processadores, placas de vídeo, periféricos e muito mais com o melhor custo-benefício.
        </p>
        <Link
          to="/produtos"
          className="mt-6 inline-block rounded-md bg-brand px-6 py-3 font-semibold hover:bg-brand-dark"
        >
          Ver todos os produtos
        </Link>
      </section>

      <section className="mx-auto max-w-7xl px-4 py-10">
        <h2 className="mb-4 text-xl font-bold text-gray-900">Categorias</h2>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-6">
          {categories.map((cat) => (
            <Link
              key={cat.id}
              to={`/produtos?categoria=${cat.slug}`}
              className="rounded-lg border border-gray-200 bg-white p-4 text-center text-sm font-medium text-gray-700 shadow-sm hover:border-brand hover:text-brand"
            >
              {cat.name}
            </Link>
          ))}
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-4 pb-14">
        <h2 className="mb-4 text-xl font-bold text-gray-900">Lançamentos</h2>
        <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-4">
          {featured.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </section>
    </div>
  )
}

```
