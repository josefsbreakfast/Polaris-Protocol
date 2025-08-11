param(
  [string]$Date = "",
  [string]$Branch = "governance-pass-2025-08-11",
  [string]$BaselineTag = "baseline-pre-clean-2025-08-11",
  [switch]$NoPush # use -NoPush if you want to skip git push
)

# 0) Ensure we're at repo root (script is in scripts/maintenance/)
Set-Location (Join-Path $PSScriptRoot "..\..")

# 1) Create today's harm log
& "scripts\maintenance\new_harm_log.ps1" -Date $Date -Branch $Branch -BaselineTag $BaselineTag

Write-Host "`n---" -ForegroundColor DarkGray
Write-Host ">>> Update the harm scan log with today's sweep findings." -ForegroundColor Yellow
Write-Host ">>> Press Enter here when you're ready to merge into the master ledger." -ForegroundColor Yellow
Read-Host | Out-Null

# 2) Merge daily log into master ledger
& "scripts\maintenance\merge_harm_log.ps1" -DailyLog "" -Branch $Branch -BaselineTag $BaselineTag

# 3) Auto-commit and push
#    - Adds today's harm_scan_YYYY-MM-DD.txt and scans/master_harm_ledger.md
#    - Commits only if there are changes
#    - Pushes to origin/$Branch unless -NoPush is set
try {
  # Ensure we're on the intended branch (won't switch if already there)
  git rev-parse --abbrev-ref HEAD | Out-Null
  $currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
  if ($currentBranch -ne $Branch) {
    Write-Host "Switching to branch $Branch (currently $currentBranch)..." -ForegroundColor Yellow
    git checkout $Branch | Out-Null
  }

  # Stage the scan files
  git add "scans\harm_scan_*.txt" "scans\master_harm_ledger.md" 2>$null

  # Only commit if there are staged changes
  $changes = git diff --cached --name-only
  if ([string]::IsNullOrWhiteSpace($changes)) {
    Write-Host "No changes to commit (daily log may be unchanged)." -ForegroundColor Cyan
  } else {
    $commitDate = (Get-Date).ToString('yyyy-MM-dd')
    git commit -m "governance: merge harm scan into master ledger ($commitDate)" | Out-Null
    Write-Host "Committed changes." -ForegroundColor Green

    if (-not $NoPush) {
      # Ensure upstream is set (first push only)
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
  Write-Host "You can manually run: git add scans\\*.txt scans\\master_harm_ledger.md; git commit -m 'msg'; git push"
}
