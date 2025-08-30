<#  Sync-To-Aegis.ps1
    Private → Public 공개용 동기화 스크립트
    사용 예:
      cd "C:\Users\JUN\Desktop\Auto-CVS-Project"
      .\scripts\tools\Sync-To-Aegis.ps1 `
          -PrivateRoot "C:\Users\JUN\Desktop\Auto-CVS-Project" `
          -PublicRoot  "C:\Users\JUN\Desktop\Project-Aegis"
#>

[CmdletBinding()]
param(
    # 원본(Private) 루트를 명시적으로 지정 (기본값: 스크립트 위치의 2단계 상위 = 프로젝트 루트)
    [string]$PrivateRoot = (Split-Path -Parent (Split-Path -Parent $PSScriptRoot)),
    [Parameter(Mandatory=$true)]
    [string]$PublicRoot,
    [switch]$WhatIfOnly
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Resolve-Dir([string]$path) {
  if (-not (Test-Path -LiteralPath $path)) {
    New-Item -ItemType Directory -Path $path -Force | Out-Null
  }
  return (Resolve-Path -LiteralPath $path).Path
}

function To-Rel([string]$root, [string]$full) {
  $rel = $full.Substring($root.Length).TrimStart('\','/')
  # 패턴 비교는 백슬래시 기준으로 할 것
  return $rel -replace '/', '\'
}

function Test-GlobMatch([string]$relPath, [string[]]$patterns) {
  foreach ($p in $patterns) {
    if ([string]::IsNullOrWhiteSpace($p)) { continue }
    $pp = ($p.Trim() -replace '/', '\')
    # 폴더 패턴이 들어오면 내부 전체를 의미하도록 보정
    if ($pp.EndsWith('\**')) {
      if ($relPath -like $pp) { return $true }
    } elseif ($pp.EndsWith('\*')) {
      if ($relPath -like $pp) { return $true }
    } else {
      # 정확/와일드카드 모두 -like로 처리
      if ($relPath -like $pp) { return $true }
    }
  }
  return $false
}

# 1) 경로 정리
$PrivateRoot = Resolve-Dir $PrivateRoot
$PublicRoot  = Resolve-Dir $PublicRoot

Write-Host "PrivateRoot : $PrivateRoot"
Write-Host "PublicRoot  : $PublicRoot"

# 2) 기본 포함/제외 규칙
$defaultIncludes = @(
  'src\learning\**',
  'src\dynamo_demo\**',
  'docs\showcase\**',
  'scripts\tools\**',
  'README.aegis.md'     # → Public 에서는 README.md 로 배치
)

$defaultExcludes = @(
  'docs\strategy\**',
  'data\private\**',
  'families\private\**',
  '**\*.rvt', '**\*.rfa', '**\*.rte', '**\*.rft', # Revit 바이너리 금지
  '.git\**', '.gitignore', '.gitattributes',      # git 메타 제외(필요시 허용)
  '.public-exclude', '.public-include'
)

# 3) 루트의 include/exclude 파일 병합
$incFile = Join-Path $PrivateRoot '.public-include'
$excFile = Join-Path $PrivateRoot '.public-exclude'

$includes = @($defaultIncludes)
$excludes = @($defaultExcludes)

if (Test-Path -LiteralPath $incFile) {
  $includes += (Get-Content -LiteralPath $incFile | Where-Object { $_ -and -not $_.Trim().StartsWith('#') })
}
if (Test-Path -LiteralPath $excFile) {
  $excludes += (Get-Content -LiteralPath $excFile | Where-Object { $_ -and -not $_.Trim().StartsWith('#') })
}

Write-Host "`n== Include rules ==" -ForegroundColor Cyan
$includes | ForEach-Object { Write-Host "  + $_" }
Write-Host "== Exclude rules ==" -ForegroundColor Magenta
$excludes | ForEach-Object { Write-Host "  - $_" }

# 4) 파일 스캔
$allFiles = Get-ChildItem -LiteralPath $PrivateRoot -Recurse -File
$willCopy = New-Object System.Collections.Generic.List[string]
$skipped  = New-Object System.Collections.Generic.List[string]

foreach ($f in $allFiles) {
  $rel = To-Rel $PrivateRoot $f.FullName

  # 제외 우선
  if (Test-GlobMatch $rel $excludes) {
    $skipped.Add($rel) | Out-Null
    continue
  }

  # 포함 규칙에 하나라도 걸리면 복사
  if (Test-GlobMatch $rel $includes) {
    $willCopy.Add($rel) | Out-Null
  } else {
    $skipped.Add($rel) | Out-Null
  }
}

Write-Host "`n=== Preview ===" -ForegroundColor Yellow
Write-Host ("Copy   : {0}" -f $willCopy.Count)
Write-Host ("Skip   : {0}" -f $skipped.Count)

if ($WhatIfOnly) {
  Write-Host "`n(미리보기 모드) 복사를 수행하지 않습니다." -ForegroundColor Yellow
  return
}

# 5) 실제 복사
foreach ($rel in $willCopy) {
  $src = Join-Path $PrivateRoot $rel
  $dst = Join-Path $PublicRoot  $rel

  $dstDir = Split-Path -Parent $dst
  if (-not (Test-Path -LiteralPath $dstDir)) {
    New-Item -ItemType Directory -Path $dstDir -Force | Out-Null
  }
  Copy-Item -LiteralPath $src -Destination $dst -Force
  Write-Host ("COPIED  {0}" -f $rel)
}

# 6) README 변환: README.aegis.md → Public/README.md
$aegisReadme = Join-Path $PrivateRoot 'README.aegis.md'
if (Test-Path -LiteralPath $aegisReadme) {
  Copy-Item -LiteralPath $aegisReadme -Destination (Join-Path $PublicRoot 'README.md') -Force
  Write-Host "UPDATED README.md from README.aegis.md" -ForegroundColor Green
}

Write-Host ""
Write-Host "Done. Review changes and commit/push in:`n  $PublicRoot" -ForegroundColor Green
