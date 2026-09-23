import { Link, useNavigate } from 'react-router-dom'
import { useState } from 'react'
import { useAuth } from '../context/AuthContext'
import { useCart } from '../context/CartContext'

export default function Navbar() {
  const { user, logout } = useAuth()
  const { totalItems } = useCart()
  const navigate = useNavigate()
  const [search, setSearch] = useState('')

  function handleSearch(e: React.FormEvent) {
    e.preventDefault()
    navigate(search.trim() ? `/produtos?q=${encodeURIComponent(search.trim())}` : '/produtos')
  }

  return (
    <header className="sticky top-0 z-50 bg-ink text-white shadow-md">
      <div className="mx-auto flex max-w-7xl items-center gap-4 px-4 py-3">
        <Link to="/" className="shrink-0 text-2xl font-extrabold tracking-tight">
          Byte<span className="text-brand">Shop</span>
        </Link>

        <form onSubmit={handleSearch} className="hidden flex-1 md:flex">
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            type="text"
            placeholder="Buscar processadores, placas de vídeo, periféricos..."
            className="w-full rounded-l-md border-0 bg-white px-4 py-2 text-gray-900 focus:outline-none focus:ring-2 focus:ring-brand"
          />
          <button
            type="submit"
            className="rounded-r-md bg-brand px-4 py-2 font-semibold text-white hover:bg-brand-dark"
          >
            Buscar
          </button>
        </form>

        <nav className="ml-auto flex items-center gap-4 text-sm font-medium">
          <Link to="/produtos" className="hover:text-brand">
            Produtos
          </Link>
          {user ? (
            <div className="flex items-center gap-3">
              <Link to="/pedidos" className="hover:text-brand">
                Meus Pedidos
              </Link>
              {user.is_admin && (
                <Link to="/admin" className="hover:text-brand">
                  Painel Admin
                </Link>
              )}
              <span className="hidden text-gray-300 sm:inline">Olá, {user.name.split(' ')[0]}</span>
              <button onClick={logout} className="rounded bg-gray-700 px-3 py-1.5 hover:bg-gray-600">
                Sair
              </button>
            </div>
          ) : (
            <Link to="/login" className="rounded bg-gray-700 px-3 py-1.5 hover:bg-gray-600">
              Entrar
            </Link>
          )}
          <Link
            to="/carrinho"
            className="relative rounded bg-brand px-3 py-1.5 font-semibold hover:bg-brand-dark"
          >
            Carrinho
            {totalItems > 0 && (
              <span className="absolute -right-2 -top-2 flex h-5 w-5 items-center justify-center rounded-full bg-white text-xs font-bold text-ink">
                {totalItems}
              </span>
            )}
          </Link>
        </nav>
      </div>
      <form onSubmit={handleSearch} className="flex px-4 pb-3 md:hidden">
        <input
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          type="text"
          placeholder="Buscar produtos..."
          className="w-full rounded-l-md border-0 bg-white px-4 py-2 text-gray-900 focus:outline-none"
        />
        <button type="submit" className="rounded-r-md bg-brand px-4 py-2 font-semibold text-white">
          Buscar
        </button>
      </form>
    </header>
  )
}
