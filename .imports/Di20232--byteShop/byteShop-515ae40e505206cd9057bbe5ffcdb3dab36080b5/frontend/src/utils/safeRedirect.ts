/**
 * O parâmetro `?redirect=` vem da URL (controlada pelo atacante em um link
 * malicioso). Só aceitamos caminhos relativos internos ("/algo"); qualquer
 * outra coisa (URL absoluta "https://...", ou "//evil.com" que o navegador
 * trata como protocolo-relativo) cai no fallback seguro.
 */
export function getSafeRedirect(value: string | null, fallback = '/'): string {
  if (!value) return fallback
  if (!value.startsWith('/') || value.startsWith('//')) return fallback
  return value
}
