# scripts/maintenance/governance_pass.ps1
param(
  [string]$Date = "",
  [string]$Branch = "governance-pass-2025-08-11",
  [string]$BaselineTag = "baseline-pre-clean-2025-08-11",
  [switch]$NoPush # use -NoPush if you want to skip git push
)

# Helper: safe date default (YYYY-MM-DD)
function Get-TodayISO {
  return (Get-Date).ToString('yyyy-MM-dd')
}

if (-not $Date -or $Date.Trim() -eq "") { $Date = Get-TodayISO }

# Paths (repo root)
Set-Location (Join-Path $PSScriptRoot "..\..")
$dailyLogPath = Join-Path "scans" ("harm_scan_{0}.txt" -f $Date)
$masterPath   = Join-Path "scans" "master_harm_ledger.md"

# 1) Create today's harm log (no overwrite if exists)
& "scripts\maintenance\new_harm_log.ps1" -Date $Date -Branch $Branch -BaselineTag $BaselineTag

Write-Host "`n---" -ForegroundColor DarkGray
Write-Host ">>> Update the harm scan log at: $dailyLogPath" -ForegroundColor Yellow
Write-Host ">>> Press Enter here when you're ready to MERGE into the master ledger." -ForegroundColor Yellow
Read-Host | Out-Null

# 2) Merge daily log into master ledger
& "scripts\maintenance\merge_harm_log.ps1" -DailyLog "" -Branch $Branch -BaselineTag $BaselineTag

# 3) Auto-commit and push (only if there are changes)
try {
  $currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
  if ($currentBranch -ne $Branch) {
    Write-Host "Switching to branch $Branch (currently $currentBranch)..." -ForegroundColor Yellow
    git checkout $Branch | Out-Null
  }

  git add "scans\harm_scan_*.txt" "scans\master_harm_ledger.md" 2>$null

  $changes = git diff --cached --name-only
  if ([string]::IsNullOrWhiteSpace($changes)) {
    Write-Host "No changes to commit (daily log may be unchanged)." -ForegroundColor Cyan
  } else {
    $commitDate = (Get-Date).ToString('yyyy-MM-dd')
    git commit -m "governance: merge harm scan into master ledger ($commitDate)" | Out-Null
    Write-Host "Committed changes." -ForegroundColor Green

    if (-not $NoPush) {
      $hasUpstream = (git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>$null)
      if ([string]::IsNullOrWhiteSpace($hasUpstream)) {
        git push --set-upstream origin $Branch
      } else {
        git push
      }
      Write-Host "Pushed to origin/$Branch." -ForegroundColor Green
    } else {
      Write-Host "Skipping push (NoPush set). Run 'git push' when ready." -ForegroundColor Yellow
    }
  }
}
catch {
  Write-Host "Git step failed: $($_.Exception.Message)" -ForegroundColor Red
  Write-Host "Manual fallback:  git add scans\*.txt scans\master_harm_ledger.md; git commit -m 'msg'; git push"
}

# 4) Post-commit summary (L1/L2/L3 counts + unique file count)
function Show-HarmSummary {
  param([string]$Path)

  if (-not (Test-Path $Path)) {
    Write-Host "`nSummary: No daily harm log found at $Path" -ForegroundColor Yellow
    return
  }

  $content = Get-Content -Path $Path -Raw -Encoding UTF8
  if ([string]::IsNullOrWhiteSpace($content)) {
    Write-Host "`nSummary: Daily harm log is empty." -ForegroundColor Yellow
    return
  }

  $L1 = ([regex]::Matches($content, '^\[L1\]', 'Multiline')).Count
  $L2 = ([regex]::Matches($content, '^\[L2\]', 'Multiline')).Count
  $L3 = ([regex]::Matches($content, '^\[L3\]', 'Multiline')).Count

  $fileMatches = [regex]::Matches($content, '^\[L[123]\]\s+File:\s+(.+)$', 'Multiline')
  $files = @{}
  foreach ($m in $fileMatches) {
    $f = $m.Groups[1].Value.Trim()
    if (-not $files.ContainsKey($f)) { $files[$f] = $true }
  }
  $uniqueFiles = $files.Keys.Count

  Write-Host "`n=== Governance Pass Summary ($Date) ===" -ForegroundColor White
  Write-Host ("Log: {0}" -f $Path) -ForegroundColor DarkGray
  Write-Host ("Files touched: {0}" -f $uniqueFiles) -ForegroundColor White
  Write-Host ("L3 (Critical): {0}" -f $L3) -ForegroundColor Red
  Write-Host ("L2 (Material): {0}" -f $L2) -ForegroundColor Yellow
  Write-Host ("L1 (Minor)   : {0}" -f $L1) -ForegroundColor Green

  if (($L3 + $L2 + $L1) -eq 0) {
    Write-Host "No entries yet — remember to log findings as you sweep." -ForegroundColor Cyan
  }
}

Show-HarmSummary -Path $dailyLogPath

# 5) Friendly nudge
Write-Host "`nDone. Keep skimming in small batches; commit often. 🧭" -ForegroundColor DarkGray
