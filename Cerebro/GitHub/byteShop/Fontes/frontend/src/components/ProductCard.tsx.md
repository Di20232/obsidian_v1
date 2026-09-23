---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/components/ProductCard.tsx
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# frontend/src/components/ProductCard.tsx

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/components/ProductCard.tsx). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```tsx
import { Link } from 'react-router-dom'
import type { Product } from '../types'
import { formatPrice } from '../utils/format'
import { useCart } from '../context/CartContext'

export default function ProductCard({ product }: { product: Product }) {
  const { addItem } = useCart()

  return (
    <div className="flex flex-col overflow-hidden rounded-lg border border-gray-200 bg-white shadow-sm transition hover:shadow-lg">
      <Link to={`/produtos/${product.slug}`}>
        <img src={product.image_url} alt={product.name} className="h-48 w-full object-cover" />
      </Link>
      <div className="flex flex-1 flex-col gap-2 p-4">
        <span className="text-xs font-semibold uppercase text-brand">{product.brand}</span>
        <Link to={`/produtos/${product.slug}`} className="line-clamp-2 font-medium text-gray-900 hover:text-brand">
          {product.name}
        </Link>
        <div className="mt-auto flex items-center justify-between pt-2">
          <span className="text-lg font-bold text-gray-900">{formatPrice(product.price)}</span>
          <button
            onClick={() => addItem(product)}
            disabled={product.stock === 0}
            className="rounded bg-brand px-3 py-1.5 text-sm font-semibold text-white hover:bg-brand-dark disabled:cursor-not-allowed disabled:bg-gray-300"
          >
            {product.stock === 0 ? 'Esgotado' : 'Adicionar'}
          </button>
        </div>
      </div>
    </div>
  )
}

```
