export interface Category {
  id: number
  name: string
  slug: string
}

export interface Product {
  id: number
  name: string
  slug: string
  description: string
  brand: string
  price: string
  stock: number
  image_url: string
  specs: Record<string, unknown>
  category: Category
}

export interface User {
  id: number
  name: string
  email: string
  is_admin: boolean
  created_at: string
}

export interface CartItem {
  product: Product
  quantity: number
}

export interface OrderItem {
  id: number
  product_id: number
  product_name: string
  quantity: number
  unit_price: string
}

export interface Order {
  id: number
  status: string
  total: string
  shipping_address: string
  created_at: string
  items: OrderItem[]
}
