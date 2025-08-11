param(
  [string]$DailyLog = "",
  [string]$Branch = "governance-pass-2025-08-11",
  [string]$BaselineTag = "baseline-pre-clean-2025-08-11"
)

$scansDir   = Join-Path $PSScriptRoot "..\..\scans" | Resolve-Path
$masterPath = Join-Path $scansDir "master_harm_ledger.md"

if (-not $DailyLog -or $DailyLog.Trim() -eq "") {
  $candidate = Get-ChildItem -Path $scansDir -Filter "harm_scan_*.txt" |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if (-not $candidate) {
    Write-Host "No harm_scan_*.txt found in $scansDir" -ForegroundColor Yellow
    exit 1
  }
  $DailyLog = $candidate.FullName
} else {
  if (-not (Test-Path $DailyLog)) {
    $DailyLog = Join-Path (Get-Location) $DailyLog
  }
}

if (-not (Test-Path $DailyLog)) {
  Write-Host "Daily log not found: $DailyLog" -ForegroundColor Red
  exit 1
}

if (-not (Test-Path $masterPath)) {
  @"
# Polaris Protocol — Master Harm Ledger

This ledger records governance-pass harm scans appended daily.

"@ | Out-File -FilePath $masterPath -Encoding UTF8 -NoNewline
}

$dailyContent = Get-Content -Path $DailyLog -Raw -Encoding UTF8
$hash = [System.BitConverter]::ToString(
  (New-Object -TypeName System.Security.Cryptography.SHA256Managed).ComputeHash(
    [System.Text.Encoding]::UTF8.GetBytes($dailyContent)
  )
).Replace("-", "").ToLower()

$masterRaw = Get-Content -Path $masterPath -Raw -Encoding UTF8
if ($masterRaw -match [regex]::Escape("digest:$hash")) {
  Write-Host "Already merged (digest exists): $DailyLog" -ForegroundColor Cyan
  exit 0
}

$filename = [System.IO.Path]::GetFileName($DailyLog)
$match = [regex]::Match($filename, 'harm_scan_(\d{4}-\d{2}-\d{2})\.txt')
$date = $match.Success ? $match.Groups[1].Value : (Get-Date).ToString('yyyy-MM-dd')

$relPath = Resolve-Path -Relative $DailyLog 2>$null
if (-not $relPath) { $relPath = $DailyLog }

$entry = @"
---
<!-- digest:$hash -->
## $date — Governance Pass

**Branch:** $Branch  
**Baseline Tag:** $BaselineTag  
**Source file:** $relPath

<details>
<summary>Harm scan contents</summary>

