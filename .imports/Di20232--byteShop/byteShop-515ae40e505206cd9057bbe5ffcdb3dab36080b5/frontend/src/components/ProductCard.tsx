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
