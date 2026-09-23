---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/admin/AdminCategories.tsx
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# frontend/src/pages/admin/AdminCategories.tsx

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/admin/AdminCategories.tsx). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```tsx
import { useEffect, useState } from 'react'
import { api } from '../../api/client'
import type { Category } from '../../types'
import { getErrorMessage } from '../../utils/errors'

export default function AdminCategories() {
  const [categories, setCategories] = useState<Category[]>([])
  const [name, setName] = useState('')
  const [error, setError] = useState('')
  const [creating, setCreating] = useState(false)

  function load() {
    api.get<Category[]>('/categories').then((res) => setCategories(res.data))
  }

  useEffect(load, [])

  async function handleCreate(e: React.FormEvent) {
    e.preventDefault()
    setError('')
    setCreating(true)
    try {
      await api.post('/admin/categories', { name })
      setName('')
      load()
    } catch (err) {
      setError(getErrorMessage(err, 'Não foi possível criar a categoria.'))
    } finally {
      setCreating(false)
    }
  }

  async function handleDelete(id: number, name: string) {
    if (!confirm(`Excluir categoria "${name}"?`)) return
    setError('')
    try {
      await api.delete(`/admin/categories/${id}`)
      load()
    } catch (err) {
      setError(getErrorMessage(err, 'Não foi possível excluir a categoria.'))
    }
  }

  return (
    <div>
      <h2 className="mb-4 text-lg font-bold text-gray-900">Categorias</h2>

      <form onSubmit={handleCreate} className="mb-6 flex max-w-md gap-2">
        <input
          required
          maxLength={80}
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Nome da nova categoria"
          className="flex-1 rounded border border-gray-300 px-3 py-2"
        />
        <button
          type="submit"
          disabled={creating}
          className="rounded bg-brand px-4 py-2 font-semibold text-white hover:bg-brand-dark disabled:opacity-60"
        >
          Adicionar
        </button>
      </form>

      {error && <p className="mb-3 text-sm text-red-600">{error}</p>}

      <div className="max-w-md overflow-hidden rounded-lg border border-gray-200 bg-white">
        {categories.map((c) => (
          <div key={c.id} className="flex items-center justify-between border-b border-gray-100 px-4 py-3 last:border-0">
            <span className="text-gray-900">{c.name}</span>
            <button onClick={() => handleDelete(c.id, c.name)} className="text-sm text-red-600 hover:underline">
              Excluir
            </button>
          </div>
        ))}
      </div>
    </div>
  )
}

```
