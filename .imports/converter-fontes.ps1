$ErrorActionPreference = 'Stop'
$vaultRoot = Split-Path -Parent $PSScriptRoot
$encoding = New-Object System.Text.UTF8Encoding($false)
$repos = Get-Content -Raw -Encoding UTF8 (Join-Path $PSScriptRoot 'repositorios.json') | ConvertFrom-Json
$report = @()
foreach ($repo in $repos) {
    if (-not $repo.sha) { continue }
    $slug = $repo.name.Replace('/', '--')
    $sourceRoot = (Get-ChildItem -Directory (Join-Path $PSScriptRoot $slug) | Select-Object -First 1).FullName
    $label = ($repo.name -split '/')[1]
    $section = if ($label -eq 'obsidian-second-brain') { 'Second-Brain' } else { $label }
    $category = switch ($label) { 'byteShop' {'web'} 'contro-vend-public' {'dados'} 'exercises_python' {'python'} default {'ia'} }
    $baseNote = 'Cerebro/GitHub/' + $section
    $archive = 'Cerebro/GitHub/Arquivos/' + $slug + '--' + $repo.sha.Substring(0,12) + '.zip'
    $rows = @()
    foreach ($file in $repo.files) {
        $sourcePath = Join-Path $sourceRoot $file.path
        $safePath = (($file.path -split '/') | ForEach-Object { if ($_.StartsWith('.')) {'_'+$_.Substring(1)} else {$_} }) -join '/'
        # Every imported file is a Markdown reference; executable names gain .md.
        $notePath = $baseNote + '/Fontes/' + $safePath + '.md'
        $destination = Join-Path $vaultRoot $notePath
        if (Test-Path -LiteralPath $destination) { throw ('Destino ja existe: ' + $notePath) }
        $url = 'https://github.com/' + $repo.name + '/blob/' + $repo.sha + '/' + (($file.path -split '/' | ForEach-Object {[uri]::EscapeDataString($_)}) -join '/')
        $extension = [IO.Path]::GetExtension($file.path).ToLowerInvariant()
        $binary = $extension -in @('.png','.jpg','.jpeg','.gif','.ico','.webp','.pdf','.woff','.woff2','.zip')
        $header = "---`ntags: [github, fonte-importada]`ncssclasses: [cerebro-nota, cerebro-$category]`nsource: $url`nsource_commit: $($repo.sha)`nimportado_em: 2026-09-15`nstatus: fonte-do-repositorio`n---`n`n# $($file.path)`n`nOrigem: [$($repo.name)]($url). Versao consultada: $($repo.sha.Substring(0,12)).`n`n[[${baseNote}/00-Indice|Indice deste repositorio]] · [[${archive}|Arquivo completo ZIP]]`n`n> [!info] Documento de referencia importado`n> Conteudo do autor, preservado para consulta. Comandos e instrucoes descrevem o projeto de origem; sua importacao nao os instala nem executa. Exemplos de pessoas e projetos do segundo cerebro sao ficticios.`n`n"
        if ($binary) {
            $body = "Arquivo binario de $($file.size) bytes, preservado integralmente no ZIP. Caminho original: $($file.path).`n"
        } else {
            $content = [IO.File]::ReadAllText($sourcePath).Replace("`r`n","`n")
            if ($extension -eq '.md') {
                # Source metadata stays visible as an example rather than controlling the vault.
                $match = [regex]::Match($content,'\A---\n[\s\S]*?\n---\n?')
                $metadata = ''
                if ($match.Success) {
                    $metadata = "`n## Metadados originais`n`n``````yaml`n" + $match.Value + "`n```````n"
                    $content = $content.Substring($match.Length)
                }
                # Resolve relative Markdown URLs against the pinned source page.
                $content = [regex]::Replace($content,'(!?\[[^\]\r\n]*\]\()([^\s\)]+)(\))', {
                    param($m)
                    $target = $m.Groups[2].Value
                    if ($target -match '^(https?:|mailto:|#|data:)') { return $m.Value }
                    try { $resolved = ([uri]::new([uri]$url,$target)).AbsoluteUri; return $m.Groups[1].Value + $resolved + $m.Groups[3].Value } catch { return $m.Value }
                })
                # Vault-specific wikilinks in examples are kept literal, not linked to the user's notes.
                $content = [regex]::Replace($content,'!?\[\[[^\]\r\n]+\]\]', {param($m) '<code>' + [Net.WebUtility]::HtmlEncode($m.Value) + '</code>'})
                $body = $content + $metadata
            } else {
                $lang = switch ($extension) { '.py' {'python'} '.js' {'javascript'} '.mjs' {'javascript'} '.ts' {'typescript'} '.tsx' {'tsx'} '.json' {'json'} '.yml' {'yaml'} '.yaml' {'yaml'} '.sql' {'sql'} '.css' {'css'} '.html' {'html'} '.sh' {'bash'} default {'text'} }
                $longest = 3
                foreach ($m in [regex]::Matches($content,'`+')) { if ($m.Length -ge $longest) { $longest=$m.Length+1 } }
                $fence = [string]::new([char]96,$longest)
                $body = $fence + $lang + "`n" + $content + "`n" + $fence + "`n"
            }
        }
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
        [IO.File]::WriteAllText($destination,$header+$body,$encoding)
        $rows += [pscustomobject]@{source=$file.path;note=$notePath;bytes=$file.size;binary=$binary;sha256=(Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash}
    }
    $repoIndex = "---`ntags: [moc, github]`ncssclasses: [cerebro-nota, cerebro-$category]`nsource_commit: $($repo.sha)`nimportado_em: 2026-09-15`n---`n`n# $($repo.name) - fontes completas`n`n[[Cerebro/GitHub/00-Indice|Central GitHub]] · [[${archive}|Baixar copia integral ZIP]]`n`nSnapshot da branch $($repo.branch), commit $($repo.sha). Todos os $($rows.Count) arquivos da arvore publica estao catalogados abaixo. Os arquivos de texto estao legiveis nas notas; binarios ficam preservados no ZIP. O historico completo de commits, issues e pull requests nao faz parte deste snapshot.`n`n## Arquivos`n`n"
    foreach ($row in $rows) { $repoIndex += '- [[' + $row.note + '|' + $row.source + ']]' + "`n" }
    [IO.File]::WriteAllText((Join-Path $vaultRoot ($baseNote+'/00-Indice.md')),$repoIndex,$encoding)
    $report += [pscustomobject]@{repo=$repo.name;sha=$repo.sha;notes=$rows.Count;markdown=@($rows|Where-Object source -like '*.md').Count;binary=@($rows|Where-Object binary).Count;archive=$archive;files=$rows}
}
[IO.File]::WriteAllText((Join-Path $PSScriptRoot 'importacao-verificada.json'),($report|ConvertTo-Json -Depth 8),$encoding)
$report | Select-Object repo,notes,markdown,binary,archive | ConvertTo-Json -Depth 4
