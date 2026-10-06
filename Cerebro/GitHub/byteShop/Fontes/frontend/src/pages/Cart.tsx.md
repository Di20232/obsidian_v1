---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/Cart.tsx
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# frontend/src/pages/Cart.tsx

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/Cart.tsx). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] · [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```tsx
import { Link, useNavigate } from 'react-router-dom'
import { useCart } from '../context/CartContext'
import { useAuth } from '../context/AuthContext'
import { formatPrice } from '../utils/format'

export default function Cart() {
  const { items, updateQuantity, removeItem, totalPrice } = useCart()
  const { user } = useAuth()
  const navigate = useNavigate()

  if (items.length === 0) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-16 text-center">
        <h1 className="text-xl font-bold text-gray-900">Seu carrinho está vazio</h1>
        <Link to="/produtos" className="mt-4 inline-block text-brand hover:underline">
          Ver produtos
        </Link>
      </div>
    )
  }

  return (
    <div className="mx-auto max-w-4xl px-4 py-8">
      <h1 className="mb-6 text-2xl font-bold text-gray-900">Meu Carrinho</h1>

      <div className="space-y-4">
        {items.map(({ product, quantity }) => (
          <div
            key={product.id}
            className="flex flex-col gap-4 rounded-lg border border-gray-200 bg-white p-4 sm:flex-row sm:items-center"
          >
            <div className="flex items-center gap-4">
              <img
                src={product.image_url}
                alt={product.name}
                className="h-20 w-20 shrink-0 rounded object-cover"
              />
              <div className="min-w-0 flex-1">
                <Link to={`/produtos/${product.slug}`} className="font-medium text-gray-900 hover:text-brand">
                  {product.name}
                </Link>
                <p className="text-sm text-gray-500">{formatPrice(product.price)} / unidade</p>
              </div>
            </div>
            <div className="flex items-center justify-between gap-4 sm:justify-end">
              <input
                type="number"
                min={1}
                max={product.stock}
                value={quantity}
                onChange={(e) => updateQuantity(product.id, Number(e.target.value))}
                className="w-16 shrink-0 rounded border border-gray-300 px-2 py-1.5"
              />
              <span className="shrink-0 text-right font-semibold text-gray-900 sm:w-24">
                {formatPrice(Number(product.price) * quantity)}
              </span>
              <button
                onClick={() => removeItem(product.id)}
                className="shrink-0 text-sm text-red-600 hover:underline"
              >
                Remover
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-8 flex items-center justify-between border-t border-gray-200 pt-6">
        <span className="text-lg font-bold text-gray-900">Total: {formatPrice(totalPrice)}</span>
        <button
          onClick={() => navigate(user ? '/checkout' : '/login?redirect=/checkout')}
          className="rounded bg-brand px-6 py-3 font-semibold text-white hover:bg-brand-dark"
        >
          Finalizar compra
        </button>
      </div>
    </div>
  )
}

```
