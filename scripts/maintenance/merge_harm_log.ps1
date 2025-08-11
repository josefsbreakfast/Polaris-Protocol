param(
  [string]$DailyLog = "",
  [string]$Branch = "governance-pass-2025-08-11",
  [string]$BaselineTag = "baseline-pre-clean-2025-08-11"
)

# repo-root relative paths
$scansDir   = Join-Path $PSScriptRoot "..\..\scans" | Resolve-Path
$masterPath = Join-Path $scansDir "master_harm_ledger.md"

# If no daily log provided, pick the most recent harm_scan_*.txt in /scans
if (-not $DailyLog -or $DailyLog.Trim() -eq "") {
  $candidate = Get-ChildItem -Path $scansDir -Filter "harm_scan_*.txt" |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if (-not $candidate) {
    Write-Host "No harm_scan_*.txt found in $scansDir" -ForegroundColor Yellow
    exit 1
  }
  $DailyLog = $candidate.FullName
} else {
  # allow relative path
  if (-not (Test-Path $DailyLog)) {
    $DailyLog = Join-Path (Get-Location) $DailyLog
  }
}

if (-not (Test-Path $DailyLog)) {
  Write-Host "Daily log not found: $DailyLog" -ForegroundColor Red
  exit 1
}

# Ensure master exists with header
if (-not (Test-Path $masterPath)) {
  @"
# Polaris Protocol — Master Harm Ledger

This ledger records governance-pass harm scans appended daily.

"@ | Out-File -FilePath $masterPath -Encoding UTF8 -NoNewline
}

# Compute a content hash to avoid duplicate ingestion
$dailyContent = Get-Content -Path $DailyLog -Raw -Encoding UTF8
$hash = [System.BitConverter]::ToString(
  (New-Object -TypeName System.Security.Cryptography.SHA256Managed).ComputeHash(
    [System.Text.Encoding]::UTF8.GetBytes($dailyContent)
  )
).Replace("-", "").ToLower()

# If hash already present in master, bail out
$masterRaw = Get-Content -Path $masterPath -Raw -Encoding UTF8
if ($masterRaw -match [regex]::Escape("digest:$hash")) {
  Write-Host "Already merged (digest exists): $DailyLog" -ForegroundColor Cyan
  exit 0
}

# Derive date from filename if present; else use today
# looks for harm_scan_YYYY-MM-DD.txt
$filename = [System.IO.Path]::GetFileName($DailyLog)
$match = [regex]::Match($filename, 'harm_scan_(\d{4}-\d{2}-\d{2})\.txt')
if ($match.Success) {
  $date = $match.Groups[1].Value
} else {
  $date = (Get-Date).ToString('yyyy-MM-dd')
}

# Build the entry to append (include hidden digest)
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

