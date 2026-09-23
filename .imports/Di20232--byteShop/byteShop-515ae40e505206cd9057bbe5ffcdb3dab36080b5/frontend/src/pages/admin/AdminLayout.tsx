import { NavLink, Outlet } from 'react-router-dom'

export default function AdminLayout() {
  const linkClass = ({ isActive }: { isActive: boolean }) =>
    `block rounded px-3 py-2 text-sm font-medium ${
      isActive ? 'bg-brand/10 text-brand' : 'text-gray-700 hover:bg-gray-100'
    }`

  return (
    <div className="mx-auto max-w-7xl px-4 py-8">
      <h1 className="mb-6 text-2xl font-bold text-gray-900">Painel Administrativo</h1>
      <div className="flex flex-col gap-6 md:flex-row">
        <aside className="w-full shrink-0 md:w-56">
          <nav className="space-y-1">
            <NavLink to="/admin/produtos" className={linkClass} end>
              Produtos
            </NavLink>
            <NavLink to="/admin/categorias" className={linkClass}>
              Categorias
            </NavLink>
          </nav>
        </aside>
        <div className="flex-1">
          <Outlet />
        </div>
      </div>
    </div>
  )
}
