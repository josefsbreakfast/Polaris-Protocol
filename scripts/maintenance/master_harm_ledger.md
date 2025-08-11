# scripts/maintenance/merge_harm_log.ps1
param(
  [string]$DailyLog = "",
  [string]$Branch = "governance-pass-2025-08-11",
  [string]$BaselineTag = "baseline-pre-clean-2025-08-11"
)

$scansDir   = Join-Path $PSScriptRoot "..\..\scans" | Resolve-Path
$masterPath = Join-Path $scansDir "master_harm_ledger.md"

# Pick most recent daily log if none provided
if (-not $DailyLog -or $DailyLog.Trim() -eq "") {
  $candidate = Get-ChildItem -Path $scansDir -Filter "harm_scan_*.txt" |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if (-not $candidate) { Write-Host "No harm_scan_*.txt found in $scansDir" -ForegroundColor Yellow; exit 1 }
  $DailyLog = $candidate.FullName
} elseif (-not (Test-Path $DailyLog)) {
  $DailyLog = Join-Path (Get-Location) $DailyLog
}

if (-not (Test-Path $DailyLog)) { Write-Host "Daily log not found: $DailyLog" -ForegroundColor Red; exit 1 }

# Ensure master exists
if (-not (Test-Path $masterPath)) {
@"
# Polaris Protocol — Master Harm Ledger

This ledger records governance-pass harm scans appended daily.

"@ | Out-File -FilePath $masterPath -Encoding UTF8 -NoNewline
}

# Read daily content + hash for de-dupe
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

# Derive date
$filename = [System.IO.Path]::GetFileName($DailyLog)
$match = [regex]::Match($filename, 'harm_scan_(\d{4}-\d{2}-\d{2})\.txt')
$date = $match.Success ? $match.Groups[1].Value : (Get-Date).ToString('yyyy-MM-dd')

# --- NEW: compute stats from dailyContent ---
$L1 = ([regex]::Matches($dailyContent, '^\[L1\]', 'Multiline')).Count
$L2 = ([regex]::Matches($dailyContent, '^\[L2\]', 'Multiline')).Count
$L3 = ([regex]::Matches($dailyContent, '^\[L3\]', 'Multiline')).Count

$fileMatches = [regex]::Matches($dailyContent, '^\[L[123]\]\s+File:\s+(.+)$', 'Multiline')
$files = @{}
foreach ($m in $fileMatches) { $f = $m.Groups[1].Value.Trim(); if (-not $files.ContainsKey($f)) { $files[$f] = $true } }
$uniqueFiles = $files.Keys.Count

$stats = @"
**Stats:**  
- Files touched: $uniqueFiles  
- L3 (Critical): $L3  
- L2 (Material): $L2  
- L1 (Minor): $L1
"@

# Build entry (include stats + details with raw log)
$relPath = Resolve-Path -Relative $DailyLog 2>$null; if (-not $relPath) { $relPath = $DailyLog }

$entry = @"
---
<!-- digest:$hash -->
## $date — Governance Pass

**Branch:** $Branch  
**Baseline Tag:** $BaselineTag  
**Source file:** $relPath

$stats

<details>
<summary>Harm scan contents</summary>

</details>

"@

Add-Content -Path $masterPath -Value "`r`n$entry"
Write-Host "Merged: $DailyLog → $($masterPath)" -ForegroundColor Green
