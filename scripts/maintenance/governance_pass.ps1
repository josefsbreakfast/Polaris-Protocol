param(
  [string]$Date = "",
  [string]$Branch = "governance-pass-2025-08-11",
  [string]$BaselineTag = "baseline-pre-clean-2025-08-11"
)

# Step 1 — create today's harm log
& "$PSScriptRoot\new_harm_log.ps1" -Date $Date -Branch $Branch -BaselineTag $BaselineTag

Write-Host "`n---" -ForegroundColor DarkGray
Write-Host ">>> Now update the harm scan log with today's sweep findings." -ForegroundColor Yellow
Write-Host ">>> Press Enter when ready to merge into the master ledger." -ForegroundColor Yellow
Read-Host

# Step 2 — merge into master ledger
& "$PSScriptRoot\merge_harm_log.ps1" -DailyLog "" -Branch $Branch -BaselineTag $BaselineTag
