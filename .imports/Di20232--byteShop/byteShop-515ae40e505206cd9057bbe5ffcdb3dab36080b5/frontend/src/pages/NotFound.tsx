import { Link } from 'react-router-dom'

export default function NotFound() {
  return (
    <div className="mx-auto max-w-3xl px-4 py-24 text-center">
      <h1 className="text-4xl font-extrabold text-gray-900">404</h1>
      <p className="mt-2 text-gray-600">Página não encontrada.</p>
      <Link to="/" className="mt-4 inline-block text-brand hover:underline">
        Voltar à página inicial
      </Link>
    </div>
  )
}
