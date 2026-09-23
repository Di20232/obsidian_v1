import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { api } from '../api/client'
import type { Order } from '../types'
import { formatPrice } from '../utils/format'

export default function OrderDetail() {
  const { id } = useParams()
  const [order, setOrder] = useState<Order | null>(null)
  const [notFound, setNotFound] = useState(false)

  useEffect(() => {
    api
      .get<Order>(`/orders/${id}`)
      .then((res) => setOrder(res.data))
      .catch(() => setNotFound(true))
  }, [id])

  if (notFound) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-16 text-center text-gray-500">Pedido não encontrado.</div>
    )
  }

  if (!order) {
    return <div className="mx-auto max-w-3xl px-4 py-16 text-center text-gray-500">Carregando...</div>
  }

  return (
    <div className="mx-auto max-w-3xl px-4 py-8">
      <Link to="/pedidos" className="text-sm text-brand hover:underline">
        ← Voltar aos pedidos
      </Link>
      <h1 className="mt-2 mb-1 text-2xl font-bold text-gray-900">Pedido #{order.id}</h1>
      <p className="mb-6 text-sm text-gray-500">
        Realizado em {new Date(order.created_at).toLocaleString('pt-BR')} ·{' '}
        <span className="font-medium text-green-700">{order.status}</span>
      </p>

      <div className="rounded-lg border border-gray-200 bg-white p-4">
        {order.items.map((item) => (
          <div key={item.id} className="flex justify-between border-b border-gray-100 py-2 last:border-0">
            <span className="text-gray-700">
              {item.product_name} x{item.quantity}
            </span>
            <span className="font-medium text-gray-900">
              {formatPrice(Number(item.unit_price) * item.quantity)}
            </span>
          </div>
        ))}
        <div className="mt-3 flex justify-between pt-3 font-bold text-gray-900">
          <span>Total</span>
          <span>{formatPrice(order.total)}</span>
        </div>
      </div>

      <div className="mt-4 rounded-lg border border-gray-200 bg-white p-4">
        <h2 className="mb-1 font-semibold text-gray-900">Endereço de entrega</h2>
        <p className="text-sm text-gray-700">{order.shipping_address}</p>
      </div>
    </div>
  )
}
