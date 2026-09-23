$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$vaultRoot = Split-Path -Parent $PSScriptRoot
$archiveRoot = Join-Path $vaultRoot 'Cerebro\GitHub\Arquivos'
New-Item -ItemType Directory -Force -Path $archiveRoot | Out-Null
$repos = Get-Content -Raw -Encoding UTF8 (Join-Path $PSScriptRoot 'repositorios.json') | ConvertFrom-Json
foreach ($repo in $repos) {
    if (-not $repo.sha) { continue }
    $slug = $repo.name.Replace('/', '--')
    $archive = Join-Path $archiveRoot ($slug + '--' + $repo.sha.Substring(0,12) + '.zip')
    if (-not (Test-Path -LiteralPath $archive)) {
        Invoke-WebRequest -UseBasicParsing -Uri ('https://codeload.github.com/' + $repo.name + '/zip/' + $repo.sha) -OutFile $archive -TimeoutSec 180
    }
    $extracted = Join-Path $PSScriptRoot $slug
    if (-not (Test-Path -LiteralPath $extracted)) { Expand-Archive -LiteralPath $archive -DestinationPath $extracted }
    $root = Get-ChildItem -Directory -LiteralPath $extracted | Select-Object -First 1
    $count = @(Get-ChildItem -Recurse -File -Force -LiteralPath $root.FullName).Count
    if ($count -ne @($repo.files).Count) { throw ('Contagem divergente: ' + $repo.name + ' ' + $count) }
    [pscustomobject]@{repo=$repo.name;arquivos=$count;bytes=(Get-Item -LiteralPath $archive).Length;sha256=(Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash}
}
