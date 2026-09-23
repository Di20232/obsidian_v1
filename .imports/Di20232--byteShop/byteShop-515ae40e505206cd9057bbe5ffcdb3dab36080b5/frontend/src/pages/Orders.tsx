import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../api/client'
import type { Order } from '../types'
import { formatPrice } from '../utils/format'

export default function Orders() {
  const [orders, setOrders] = useState<Order[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api
      .get<Order[]>('/orders')
      .then((res) => setOrders(res.data))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <div className="mx-auto max-w-4xl px-4 py-16 text-center text-gray-500">Carregando...</div>

  return (
    <div className="mx-auto max-w-4xl px-4 py-8">
      <h1 className="mb-6 text-2xl font-bold text-gray-900">Meus Pedidos</h1>
      {orders.length === 0 ? (
        <p className="text-gray-500">Você ainda não fez nenhum pedido.</p>
      ) : (
        <div className="space-y-3">
          {orders.map((order) => (
            <Link
              key={order.id}
              to={`/pedidos/${order.id}`}
              className="flex items-center justify-between rounded-lg border border-gray-200 bg-white p-4 hover:border-brand"
            >
              <div>
                <p className="font-medium text-gray-900">Pedido #{order.id}</p>
                <p className="text-sm text-gray-500">
                  {new Date(order.created_at).toLocaleDateString('pt-BR')} · {order.items.length} item(ns)
                </p>
              </div>
              <div className="text-right">
                <p className="font-bold text-gray-900">{formatPrice(order.total)}</p>
                <span className="inline-block rounded-full bg-green-100 px-2 py-0.5 text-xs font-medium text-green-700">
                  {order.status}
                </span>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  )
}
