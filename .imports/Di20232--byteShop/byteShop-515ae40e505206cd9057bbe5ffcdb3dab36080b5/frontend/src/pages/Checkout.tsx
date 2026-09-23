import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { api } from '../api/client'
import { useCart } from '../context/CartContext'
import { formatPrice } from '../utils/format'
import { getErrorMessage } from '../utils/errors'

export default function Checkout() {
  const { items, totalPrice, clear } = useCart()
  const navigate = useNavigate()
  const [address, setAddress] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      const res = await api.post('/orders', {
        shipping_address: address,
        items: items.map((i) => ({ product_id: i.product.id, quantity: i.quantity })),
      })
      clear()
      navigate(`/pedidos/${res.data.id}`)
    } catch (err) {
      setError(getErrorMessage(err, 'Não foi possível concluir o pedido.'))
    } finally {
      setLoading(false)
    }
  }

  if (items.length === 0) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-16 text-center text-gray-500">
        Seu carrinho está vazio.
      </div>
    )
  }

  return (
    <div className="mx-auto max-w-3xl px-4 py-8">
      <h1 className="mb-6 text-2xl font-bold text-gray-900">Finalizar Compra</h1>

      <div className="mb-6 rounded-lg border border-gray-200 bg-white p-4">
        <h2 className="mb-3 font-semibold text-gray-900">Resumo do pedido</h2>
        {items.map(({ product, quantity }) => (
          <div key={product.id} className="flex justify-between py-1 text-sm text-gray-700">
            <span>
              {product.name} x{quantity}
            </span>
            <span>{formatPrice(Number(product.price) * quantity)}</span>
          </div>
        ))}
        <div className="mt-3 flex justify-between border-t border-gray-200 pt-3 font-bold text-gray-900">
          <span>Total</span>
          <span>{formatPrice(totalPrice)}</span>
        </div>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="mb-1 block text-sm font-medium text-gray-700">Endereço de entrega</label>
          <textarea
            required
            minLength={5}
            maxLength={500}
            value={address}
            onChange={(e) => setAddress(e.target.value)}
            placeholder="Rua, número, bairro, cidade, CEP"
            className="w-full rounded border border-gray-300 px-3 py-2"
            rows={3}
          />
        </div>

        <div className="rounded-lg border border-dashed border-gray-300 bg-gray-50 p-4 text-sm text-gray-600">
          Pagamento simulado: ao confirmar, seu pedido será registrado como <strong>pago</strong> automaticamente
          (sem cobrança real).
        </div>

        {error && <p className="text-sm text-red-600">{error}</p>}

        <button
          type="submit"
          disabled={loading}
          className="w-full rounded bg-brand py-3 font-semibold text-white hover:bg-brand-dark disabled:opacity-60"
        >
          {loading ? 'Processando...' : `Confirmar pedido — ${formatPrice(totalPrice)}`}
        </button>
      </form>
    </div>
  )
}
