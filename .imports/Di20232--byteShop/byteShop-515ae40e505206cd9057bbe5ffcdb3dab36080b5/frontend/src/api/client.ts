import axios from 'axios'

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Se um token que enviamos for rejeitado (expirado/inválido/revogado), a
// sessão local fica "presa" — o usuário continua vendo a UI de logado, mas
// toda ação falha silenciosamente. Aqui limpamos o token e mandamos para o
// login, exceto quando o próprio 401 veio do login/cadastro (credenciais
// erradas), que deve ser tratado localmente pela tela.
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const status = error?.response?.status
    const sentToken = Boolean(error?.config?.headers?.Authorization)
    const url: string = error?.config?.url || ''
    const isAuthEndpoint = url.includes('/auth/login') || url.includes('/auth/register')

    if (status === 401 && sentToken && !isAuthEndpoint) {
      localStorage.removeItem('token')
      if (!window.location.pathname.startsWith('/login')) {
        window.location.href = '/login'
      }
    }
    return Promise.reject(error)
  },
)
