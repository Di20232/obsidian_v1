---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/Catalog.tsx
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# frontend/src/pages/Catalog.tsx

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/Catalog.tsx). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```tsx
import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { api } from '../api/client'
import type { Category, Product } from '../types'
import ProductCard from '../components/ProductCard'

export default function Catalog() {
  const [searchParams, setSearchParams] = useSearchParams()
  const [categories, setCategories] = useState<Category[]>([])
  const [products, setProducts] = useState<Product[]>([])
  const [pages, setPages] = useState(1)
  const [loading, setLoading] = useState(true)

  const categorySlug = searchParams.get('categoria') || ''
  const query = searchParams.get('q') || ''
  const sort = searchParams.get('sort') || 'relevance'
  const rawPage = Number(searchParams.get('page'))
  const page = Number.isInteger(rawPage) && rawPage > 0 ? rawPage : 1

  useEffect(() => {
    api
      .get<Category[]>('/categories')
      .then((res) => setCategories(res.data))
      .catch(() => setCategories([]))
  }, [])

  useEffect(() => {
    setLoading(true)
    api
      .get('/products', {
        params: {
          category: categorySlug || undefined,
          q: query || undefined,
          sort,
          page,
          page_size: 12,
        },
      })
      .then((res) => {
        setProducts(res.data.items)
        setPages(res.data.pages)
      })
      .catch(() => {
        setProducts([])
        setPages(1)
      })
      .finally(() => setLoading(false))
  }, [categorySlug, query, sort, page])

  function updateParam(key: string, value: string) {
    const next = new URLSearchParams(searchParams)
    if (value) next.set(key, value)
    else next.delete(key)
    next.set('page', '1')
    setSearchParams(next)
  }

  function goToPage(p: number) {
    const next = new URLSearchParams(searchParams)
    next.set('page', String(p))
    setSearchParams(next)
  }

  return (
    <div className="mx-auto max-w-7xl px-4 py-8">
      <div className="flex flex-col gap-6 md:flex-row">
        <aside className="w-full shrink-0 md:w-56">
          <h3 className="mb-2 font-bold text-gray-900">Categorias</h3>
          <ul className="space-y-1 text-sm">
            <li>
              <button
                onClick={() => updateParam('categoria', '')}
                className={`w-full rounded px-2 py-1.5 text-left hover:bg-gray-100 ${
                  !categorySlug ? 'bg-brand/10 font-semibold text-brand' : 'text-gray-700'
                }`}
              >
                Todas
              </button>
            </li>
            {categories.map((cat) => (
              <li key={cat.id}>
                <button
                  onClick={() => updateParam('categoria', cat.slug)}
                  className={`w-full rounded px-2 py-1.5 text-left hover:bg-gray-100 ${
                    categorySlug === cat.slug ? 'bg-brand/10 font-semibold text-brand' : 'text-gray-700'
                  }`}
                >
                  {cat.name}
                </button>
              </li>
            ))}
          </ul>
        </aside>

        <div className="flex-1">
          <div className="mb-4 flex items-center justify-between">
            <h1 className="text-xl font-bold text-gray-900">
              {query ? `Resultados para "${query}"` : 'Produtos'}
            </h1>
            <select
              value={sort}
              onChange={(e) => updateParam('sort', e.target.value)}
              className="rounded border border-gray-300 px-3 py-1.5 text-sm"
            >
              <option value="relevance">Relevância</option>
              <option value="price_asc">Menor preço</option>
              <option value="price_desc">Maior preço</option>
              <option value="newest">Novidades</option>
            </select>
          </div>

          {loading ? (
            <p className="text-gray-500">Carregando...</p>
          ) : products.length === 0 ? (
            <p className="text-gray-500">Nenhum produto encontrado.</p>
          ) : (
            <>
              <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-4">
                {products.map((product) => (
                  <ProductCard key={product.id} product={product} />
                ))}
              </div>

              {pages > 1 && (
                <div className="mt-8 flex justify-center gap-2">
                  {Array.from({ length: pages }, (_, i) => i + 1).map((p) => (
                    <button
                      key={p}
                      onClick={() => goToPage(p)}
                      className={`h-9 w-9 rounded ${
                        p === page ? 'bg-brand text-white' : 'bg-white text-gray-700 hover:bg-gray-100'
                      } border border-gray-300`}
                    >
                      {p}
                    </button>
                  ))}
                </div>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  )
}

```
