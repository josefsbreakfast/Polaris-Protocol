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
& "scripts\mainten
