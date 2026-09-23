/**
 * A FastAPI retorna `detail` como string em erros que nós lançamos manualmente
 * (400/401/403/404/409), mas como uma LISTA de objetos em erros de validação
 * automática (422 do Pydantic). Renderizar essa lista direto no JSX quebra o
 * React ("Objects are not valid as a React child" — tela branca). Esta função
 * normaliza os dois formatos para uma string segura de exibir.
 */
export function getErrorMessage(err: unknown, fallback: string): string {
  const detail = (err as { response?: { data?: { detail?: unknown } } })?.response?.data?.detail

  if (typeof detail === "string") {
    return detail
  }

  if (Array.isArray(detail)) {
    const messages = detail
      .map((item) => (item && typeof item === "object" && "msg" in item ? String((item as { msg: unknown }).msg) : null))
      .filter((msg): msg is string => Boolean(msg))
    if (messages.length > 0) {
      return messages.join("; ")
    }
  }

  return fallback
}
