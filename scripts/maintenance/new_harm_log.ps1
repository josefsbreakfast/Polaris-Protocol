param(
  [string]$Date = "",
  [string]$Branch = "governance-pass-2025-08-11",
  [string]$BaselineTag = "baseline-pre-clean-2025-08-11"
)

if (-not $Date -or $Date.Trim() -eq "") {
  $Date = (Get-Date).ToString('yyyy-MM-dd')
}

$scansDir = Join-Path $PSScriptRoot "..\..\scans" | Resolve-Path
$logPath  = Join-Path $scansDir ("harm_scan_$Date.txt")

if (Test-Path $logPath) {
  Write-Host "Harm scan for $Date already exists: $logPath" -ForegroundColor Yellow
  exit 1
}

New-Item -ItemType Directory -Force -Path $scansDir | Out-Null

@"
# Polaris Protocol — Governance Pass Harm Scan Log
# Date: $Date
# Branch: $Branch
# Baseline Tag: $BaselineTag
# Purpose: Track all files flagged for tone skew / sexualisation / credibility undermining during manual sweep.

------------------------------------------------------------
[HEADER]
- Sweep type: Manual tone audit
- Trigger criteria: see tone deviation checklist
- Quarantine folder: /Quarantine/$Date_manual/
- Severity scale:
    L1 = Minor stylistic issue (fix later)
    L2 = Material tone shift (neutralise now)
    L3 = Critical contamination (quarantine immediately)
------------------------------------------------------------

[ENTRY TEMPLATE]
[Ln] File: <relative/path/from/repo/root>
Severity: L1 | L2 | L3
Section: <brief description — e.g., Paragraph 3, metadata section, closing note>
Finding: <short note on skew/tone issue>
Action: <Quarantined | Neutralised | Trimmed | Rewritten>
Notes: <optional — e.g., suspected fork injection, matched pattern X>

------------------------------------------------------------
[ENTRIES]

"@ | Out-File -FilePath $logPath -Encoding UTF8 -NoNewline

Write-Host "Created harm scan log: $logPath" -ForegroundColor Green
