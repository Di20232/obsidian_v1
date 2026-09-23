import { Component, type ErrorInfo, type ReactNode } from 'react'

interface Props {
  children: ReactNode
}

interface State {
  hasError: boolean
}

export default class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false }

  static getDerivedStateFromError(): State {
    return { hasError: true }
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error('Erro não tratado na interface:', error, info)
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="mx-auto max-w-md px-4 py-24 text-center">
          <h1 className="text-xl font-bold text-gray-900">Ops, algo deu errado</h1>
          <p className="mt-2 text-gray-600">
            Ocorreu um erro inesperado nesta página. Tente recarregar.
          </p>
          <button
            onClick={() => window.location.reload()}
            className="mt-6 rounded bg-brand px-6 py-2 font-semibold text-white hover:bg-brand-dark"
          >
            Recarregar página
          </button>
        </div>
      )
    }
    return this.props.children
  }
}
