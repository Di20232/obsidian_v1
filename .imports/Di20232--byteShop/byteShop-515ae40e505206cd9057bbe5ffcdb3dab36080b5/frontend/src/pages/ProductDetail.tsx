import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { api } from '../api/client'
import type { Product } from '../types'
import { formatPrice } from '../utils/format'
import { useCart } from '../context/CartContext'

export default function ProductDetail() {
  const { slug } = useParams()
  const [product, setProduct] = useState<Product | null>(null)
  const [quantity, setQuantity] = useState(1)
  const [notFound, setNotFound] = useState(false)
  const { addItem } = useCart()
  const [added, setAdded] = useState(false)

  useEffect(() => {
    setProduct(null)
    setNotFound(false)
    api
      .get<Product>(`/products/${slug}`)
      .then((res) => setProduct(res.data))
      .catch(() => setNotFound(true))
  }, [slug])

  if (notFound) {
    return (
      <div className="mx-auto max-w-7xl px-4 py-16 text-center">
        <p className="text-gray-600">Produto não encontrado.</p>
        <Link to="/produtos" className="mt-4 inline-block text-brand hover:underline">
          Voltar ao catálogo
        </Link>
      </div>
    )
  }

  if (!product) {
    return <div className="mx-auto max-w-7xl px-4 py-16 text-center text-gray-500">Carregando...</div>
  }

  return (
    <div className="mx-auto max-w-7xl px-4 py-8">
      <nav className="mb-4 text-sm text-gray-500">
        <Link to="/produtos" className="hover:text-brand">Produtos</Link>
        {' / '}
        <Link to={`/produtos?categoria=${product.category.slug}`} className="hover:text-brand">
          {product.category.name}
        </Link>
      </nav>

      <div className="grid grid-cols-1 gap-8 md:grid-cols-2">
        <img src={product.image_url} alt={product.name} className="w-full rounded-lg border border-gray-200" />

        <div>
          <span className="text-sm font-semibold uppercase text-brand">{product.brand}</span>
          <h1 className="mt-1 text-2xl font-bold text-gray-900">{product.name}</h1>
          <p className="mt-4 text-3xl font-extrabold text-gray-900">{formatPrice(product.price)}</p>
          <p className="mt-1 text-sm text-gray-500">
            {product.stock > 0 ? `${product.stock} unidades em estoque` : 'Produto esgotado'}
          </p>

          <p className="mt-4 text-gray-700">{product.description}</p>

          {Object.keys(product.specs).length > 0 && (
            <div className="mt-6">
              <h2 className="mb-2 font-semibold text-gray-900">Especificações</h2>
              <table className="w-full text-sm">
                <tbody>
                  {Object.entries(product.specs).map(([key, value]) => (
                    <tr key={key} className="border-b border-gray-100">
                      <td className="py-1.5 pr-4 font-medium capitalize text-gray-600">
                        {key.replace(/_/g, ' ')}
                      </td>
                      <td className="py-1.5 text-gray-900">{String(value)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          <div className="mt-6 flex items-center gap-3">
            <input
              type="number"
              min={1}
              max={product.stock}
              value={quantity}
              onChange={(e) => setQuantity(Math.min(product.stock, Math.max(1, Number(e.target.value) || 1)))}
              className="w-20 rounded border border-gray-300 px-3 py-2"
            />
            <button
              onClick={() => {
                addItem(product, quantity)
                setAdded(true)
                setTimeout(() => setAdded(false), 2000)
              }}
              disabled={product.stock === 0}
              className="rounded bg-brand px-6 py-2 font-semibold text-white hover:bg-brand-dark disabled:cursor-not-allowed disabled:bg-gray-300"
            >
              {added ? 'Adicionado!' : 'Adicionar ao carrinho'}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
