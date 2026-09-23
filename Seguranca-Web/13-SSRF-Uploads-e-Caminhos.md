---
tags: [seguranca, web, ssrf, upload, path-traversal, flashcards]
aliases: [SSRF, Path Traversal, Upload Seguro]
cssclasses: [cerebro-nota, cerebro-seguranca]
---

# SSRF, uploads e caminhos

Três problemas com a mesma raiz: o servidor **busca, grava ou lê** alguma coisa usando um endereço, nome ou arquivo que veio do usuário.

## SSRF: o servidor busca o que o usuário manda

**SSRF** (Server-Side Request Forgery) acontece em funções como "importar imagem por URL", "gerar prévia de link", "testar webhook" ou "baixar planilha do link". O atacante manda uma URL que o **servidor** consegue alcançar e ele não:

| URL maliciosa | O que expõe |
|---|---|
| `http://localhost:8080/admin` | painel que só escuta na máquina |
| `http://192.168.0.10/` | serviços da rede interna |
| `http://169.254.169.254/...` | serviço de metadados da nuvem, que pode entregar credenciais da máquina |
| `file:///etc/passwd` | arquivos do servidor, se a biblioteca aceitar o esquema |

No [[02-OWASP-Top-10|OWASP Top 10:2025]], o SSRF passou a fazer parte do A01, controle de acesso quebrado.

### Defesas

1. **Allowlist de destinos** sempre que possível: "só imagens do nosso CDN", "só a API do parceiro".
2. Aceitar só `https:` (e `http:` se preciso). Recusar `file:`, `gopher:`, `ftp:`.
3. **Resolver o nome e conferir o IP** antes de conectar: bloquear loopback (`127.0.0.0/8`, `::1`), redes privadas (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), link-local (`169.254.0.0/16`) e similares.
4. **Conectar no IP que foi conferido**, não resolver de novo — senão um DNS que muda de resposta (*DNS rebinding*) troca o destino entre a checagem e a conexão.
5. **Desligar redirecionamentos** automáticos (ou conferir cada salto): uma URL externa inofensiva pode redirecionar para `localhost`.
6. Limitar tempo e tamanho da resposta; **não devolver a resposta bruta** ao usuário.
7. Na infraestrutura: o servidor da aplicação não precisa alcançar toda a rede interna.

## Path traversal: ler ou gravar fora da pasta

```python
# ERRADO
return send_file(f"uploads/{request.args['arquivo']}")
# arquivo = "../../app/config.py"  → entrega o código com as senhas
```

```python
# CERTO (Flask): send_from_directory recusa caminhos que saem da pasta
from flask import send_from_directory
return send_from_directory("uploads", nome_guardado_no_banco)
```

Regras:

- **Não usar o nome enviado pelo usuário como caminho.** Gere um nome (`uuid4().hex + ".png"`) e guarde o nome original só como texto no banco.
- Se precisar montar caminho, normalize e confira que ele continua dentro da pasta base:

```python
from pathlib import Path
base = Path("uploads").resolve()
alvo = (base / nome).resolve()
if not alvo.is_relative_to(base):
    abort(400)
```

- `werkzeug.utils.secure_filename` limpa o nome, mas gerar um nome novo é mais seguro.
- Ao extrair ZIP, faça a mesma checagem para cada entrada (*zip slip*: um arquivo chamado `../../app.py` dentro do ZIP).

## Upload de arquivos

| Risco | Defesa |
|---|---|
| Arquivo gigante derruba o servidor | limite de tamanho no servidor web e na aplicação (`MAX_CONTENT_LENGTH` no Flask, `limits` no multer) |
| Arquivo comprimido que explode ao abrir | limitar o tamanho **depois** de descomprimir e o número de linhas → [[Cerebro/Problemas-Resolvidos/22-Decompression-Bomb-em-XLSX\|caso real com XLSX]] |
| Extensão mentirosa (`foto.jpg` que é HTML) | conferir o tipo pelo **conteúdo** (assinatura do arquivo, abrir com a biblioteca de imagem), não pela extensão nem pelo `Content-Type` enviado |
| HTML ou SVG com script servido pelo seu domínio | servir uploads de outro domínio ou com `Content-Disposition: attachment` e `X-Content-Type-Options: nosniff`; SVG pode conter `<script>` |
| Arquivo executável na pasta pública | guardar **fora** da raiz do site e sem permissão de execução |
| Nome de arquivo com caminho | gerar nome novo (acima) |
| Imagem com metadados pessoais (GPS) | reprocessar a imagem, o que remove os metadados |

## Planilhas: injeção de fórmula

Ao **exportar** CSV ou XLSX com dados digitados por usuários, um campo que começa com `=`, `+`, `-`, `@` (ou tabulação e retorno de carro) pode ser executado como fórmula quando alguém abrir no Excel. Prefixe esses valores com um apóstrofo (`'`) ou exporte como texto. Relevante para os sistemas do cofre que [[Cerebro/Praticas/05-Importacao-de-Planilhas|trabalham com planilhas]].

## Arquivos que viram código: desserialização

Alguns formatos executam código ao serem carregados:

- **`pickle`** (Python): nunca carregar pickle vindo de fora. Use JSON.
- **YAML:** `yaml.load` pode criar objetos arbitrários; use **`yaml.safe_load`**.
- Modelos de IA em formato pickle (`.pkl`, alguns `.pt` antigos) também executam código; prefira `safetensors`.

Isso entra em A08 (falhas de integridade de software e dados) no Top 10.

## Perguntas de revisão

O que é SSRF? :: Server-Side Request Forgery: o atacante faz o servidor buscar uma URL que só o servidor alcança, como localhost, a rede interna ou os metadados da nuvem.

Em quais funcionalidades o SSRF costuma aparecer? :: Importar imagem por URL, gerar prévia de link, testar webhook e baixar arquivo a partir de um link.

Quais as principais defesas contra SSRF? :: Allowlist de destinos, só esquemas http e https, conferir o IP resolvido contra faixas privadas e locais, conectar no IP conferido, desligar redirecionamentos e não devolver a resposta bruta.

O que é DNS rebinding no contexto de SSRF? :: O nome resolve para um IP permitido na checagem e para um IP interno na conexão; evita-se conectando no IP que já foi conferido.

O que é path traversal? :: Usar sequências como ../ num nome de arquivo para ler ou gravar fora da pasta prevista.

Qual a forma mais segura de nomear arquivos enviados? :: Gerar um nome novo no servidor, como um UUID, e guardar o nome original só como texto no banco.

Como conferir o tipo real de um arquivo enviado? :: Pelo conteúdo, com a assinatura do arquivo ou abrindo com a biblioteca adequada, e não pela extensão nem pelo Content-Type enviado.

Por que SVG enviado por usuário é perigoso? :: Porque SVG pode conter script; servido pelo próprio domínio, vira XSS.

O que é injeção de fórmula em planilhas exportadas? :: Um campo que começa com =, +, - ou @ é executado como fórmula ao abrir no Excel; evita-se prefixando com apóstrofo.

Por que nunca carregar pickle de fonte externa? :: Porque carregar um pickle pode executar código arbitrário; para dados externos use JSON, e para YAML use yaml.safe_load.

O que é zip slip? :: Um arquivo dentro do ZIP com nome como ../../app.py que, ao extrair sem checagem, é gravado fora da pasta de destino.

---
Anterior: [[12-CORS|CORS]] · Próxima: [[14-Cabecalhos-de-Seguranca|Cabeçalhos de segurança]] · Trilha: [[Seguranca-Web/00-Indice|Segurança Web]]
