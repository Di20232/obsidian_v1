---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/Login.tsx
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# frontend/src/pages/Login.tsx

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/Login.tsx). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```tsx
import { useState } from 'react'
import { Link, useNavigate, useSearchParams } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { getSafeRedirect } from '../utils/safeRedirect'

export default function Login() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      await login(email, password)
      navigate(getSafeRedirect(searchParams.get('redirect')))
    } catch {
      setError('E-mail ou senha inválidos.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mx-auto max-w-sm px-4 py-16">
      <h1 className="mb-6 text-2xl font-bold text-gray-900">Entrar</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="mb-1 block text-sm font-medium text-gray-700">E-mail</label>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full rounded border border-gray-300 px-3 py-2"
          />
        </div>
        <div>
          <label className="mb-1 block text-sm font-medium text-gray-700">Senha</label>
          <input
            type="password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full rounded border border-gray-300 px-3 py-2"
          />
        </div>
        {error && <p className="text-sm text-red-600">{error}</p>}
        <button
          type="submit"
          disabled={loading}
          className="w-full rounded bg-brand py-2.5 font-semibold text-white hover:bg-brand-dark disabled:opacity-60"
        >
          {loading ? 'Entrando...' : 'Entrar'}
        </button>
      </form>
      <p className="mt-4 text-sm text-gray-600">
        Não tem conta?{' '}
        <Link to="/cadastro" className="font-medium text-brand hover:underline">
          Cadastre-se
        </Link>
      </p>
    </div>
  )
}

```
