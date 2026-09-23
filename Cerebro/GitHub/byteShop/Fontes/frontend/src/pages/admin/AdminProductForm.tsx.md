---
tags: [github, fonte-importada]
cssclasses: [cerebro-nota, cerebro-web]
source: https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/admin/AdminProductForm.tsx
source_commit: 515ae40e505206cd9057bbe5ffcdb3dab36080b5
importado_em: 2026-09-15
status: fonte-do-repositorio
---

# frontend/src/pages/admin/AdminProductForm.tsx

Origem: [Di20232/byteShop](https://github.com/Di20232/byteShop/blob/515ae40e505206cd9057bbe5ffcdb3dab36080b5/frontend/src/pages/admin/AdminProductForm.tsx). Versao consultada: 515ae40e5052.

[[Cerebro/GitHub/byteShop/00-Indice|Indice deste repositorio]] Â· [[Cerebro/GitHub/Arquivos/Di20232--byteShop--515ae40e5052.zip|Arquivo completo ZIP]]

> [!info] Documento de referencia importado
> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.

```tsx
import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { api } from '../../api/client'
import type { Category } from '../../types'
import { getErrorMessage } from '../../utils/errors'

export default function AdminProductForm() {
  const { id } = useParams()
  const isEdit = Boolean(id)
  const navigate = useNavigate()

  const [categories, setCategories] = useState<Category[]>([])
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [brand, setBrand] = useState('')
  const [price, setPrice] = useState('')
  const [stock, setStock] = useState('')
  const [imageUrl, setImageUrl] = useState('')
  const [categoryId, setCategoryId] = useState('')
  const [specsText, setSpecsText] = useState('{}')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(isEdit)
  const [saving, setSaving] = useState(false)

  useEffect(() => {
    api.get<Category[]>('/categories').then((res) => {
      setCategories(res.data)
      if (!isEdit && res.data.length > 0) setCategoryId(String(res.data[0].id))
    })
  }, [isEdit])

  useEffect(() => {
    if (!isEdit) return
    setLoading(true)
    api
      .get(`/admin/products/${id}`)
      .then((res) => {
        const product = res.data
        setName(product.name)
        setDescription(product.description)
        setBrand(product.brand)
        setPrice(String(product.price))
        setStock(String(product.stock))
        setImageUrl(product.image_url)
        setCategoryId(String(product.category.id))
        setSpecsText(JSON.stringify(product.specs, null, 2))
      })
      .finally(() => setLoading(false))
  }, [id, isEdit])

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError('')

    let specs: Record<string, unknown>
    try {
      specs = JSON.parse(specsText || '{}')
    } catch {
      setError('Especificações inválidas: use um JSON válido, ex: {"nucleos": 6}')
      return
    }

    const payload = {
      name,
      description,
      brand,
      price: Number(price),
      stock: Number(stock),
      image_url: imageUrl,
      specs,
      category_id: Number(categoryId),
    }

    setSaving(true)
    try {
      if (isEdit) {
        await api.put(`/admin/products/${id}`, payload)
      } else {
        await api.post('/admin/products', payload)
      }
      navigate('/admin/produtos')
    } catch (err) {
      setError(getErrorMessage(err, 'Não foi possível salvar o produto.'))
    } finally {
      setSaving(false)
    }
  }

  if (loading) return <p className="text-gray-500">Carregando...</p>

  return (
    <div>
      <h2 className="mb-4 text-lg font-bold text-gray-900">{isEdit ? 'Editar produto' : 'Novo produto'}</h2>
      <form onSubmit={handleSubmit} className="max-w-xl space-y-4">
        <div>
          <label className="mb-1 block text-sm font-medium text-gray-700">Nome</label>
          <input
            required
            maxLength={200}
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full rounded border border-gray-300 px-3 py-2"
          />
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">Marca</label>
            <input
              value={brand}
              maxLength={80}
              onChange={(e) => setBrand(e.target.value)}
              className="w-full rounded border border-gray-300 px-3 py-2"
            />
          </div>
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">Categoria</label>
            <select
              required
              value={categoryId}
              onChange={(e) => setCategoryId(e.target.value)}
              className="w-full rounded border border-gray-300 px-3 py-2"
            >
              {categories.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.name}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium text-gray-700">Descrição</label>
          <textarea
            value={description}
            maxLength={2000}
            onChange={(e) => setDescription(e.target.value)}
            rows={3}
            className="w-full rounded border border-gray-300 px-3 py-2"
          />
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">Preço (R$)</label>
            <input
              required
              type="number"
              step="0.01"
              min="0.01"
              max="99999999.99"
              value={price}
              onChange={(e) => setPrice(e.target.value)}
              className="w-full rounded border border-gray-300 px-3 py-2"
            />
          </div>
          <div>
            <label className="mb-1 block text-sm font-medium text-gray-700">Estoque</label>
            <input
              required
              type="number"
              min="0"
              max="1000000"
              value={stock}
              onChange={(e) => setStock(e.target.value)}
              className="w-full rounded border border-gray-300 px-3 py-2"
            />
          </div>
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium text-gray-700">URL da imagem</label>
          <input
            value={imageUrl}
            maxLength={500}
            onChange={(e) => setImageUrl(e.target.value)}
            placeholder="https://..."
            className="w-full rounded border border-gray-300 px-3 py-2"
          />
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium text-gray-700">
            Especificações (JSON)
          </label>
          <textarea
            value={specsText}
            onChange={(e) => setSpecsText(e.target.value)}
            rows={6}
            spellCheck={false}
            className="w-full rounded border border-gray-300 px-3 py-2 font-mono text-sm"
          />
          <p className="mt-1 text-xs text-gray-500">
            Ex: {'{'}"nucleos": 6, "threads": 12, "socket": "AM4"{'}'}
          </p>
        </div>

        {error && <p className="text-sm text-red-600">{error}</p>}

        <div className="flex gap-3">
          <button
            type="submit"
            disabled={saving}
            className="rounded bg-brand px-6 py-2 font-semibold text-white hover:bg-brand-dark disabled:opacity-60"
          >
            {saving ? 'Salvando...' : 'Salvar'}
          </button>
          <button
            type="button"
            onClick={() => navigate('/admin/produtos')}
            className="rounded border border-gray-300 px-6 py-2 font-semibold text-gray-700 hover:bg-gray-50"
          >
            Cancelar
          </button>
        </div>
      </form>
    </div>
  )
}

```
