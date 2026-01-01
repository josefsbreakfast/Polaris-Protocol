# 🧰 Upstream Compromise — Remote Middleware Checklist  
**First created:** 2025-10-13 | **Last updated:** 2026-01-01  
*Triage and detection playbook for suspected remote or supply‑chain compromises.*  

---

## 🧭 Orientation  
Compact SOP for when middleware or provider infrastructure has been tampered with upstream.

---

## 🔧 Triage Checklist (preserve first)  
- Snapshot instances, container images, router configs; hash artifacts.  
- Export cloud audit, CI/CD, API gateway, webhook logs (WORM store).  
- Disable non‑essential tools/plugins/webhooks; block egress for middleware.  
- Revoke or shorten service‑account keys; rotate secrets.  
- Diff prompts + tool manifests; record human‑readable diffs.  
- Notify provider & IR; avoid in‑place edits—prefer signed rollback.

---

## 📡 Detection Dashboard — minimal spec  
**Telemetry:** Cloud audit, CI logs, tool router logs, artifact registry, API gateway, job scheduler, vector‑DB writes, error/retry metrics, session preamble sampling.  
**Alerts:** new privileged service account (critical); tool invoked without user intent (high); system/meta prompt changed off‑window (critical); >5 identical preamble changes/24h (medium); outbound to unknown domains spike (high).  
**Widgets:** tool‑invocation time series; region×service‑account heatmap; prompt diff viewer; scheduled‑jobs table.

---

## 🛡️ Containment Playbook  
1) Fail closed → 2) Roll back to signed build → 3) Rotate secrets → 4) Quarantine memory stores → 5) Canary redeploy with behaviour diff → 6) Multi‑party approval before re‑enabling tools.

---

## 🗂 Filing Guidance  
Create Field Log: title, timeline, evidence hashes, actions, owners, next steps. Cross‑link to Protocol Integrity SOP.

---

## 🌌 Constellations  
- 📡 Protocol Integrity SOP  
- ⚙️ System Governance  
- 🧠 Survivor Voice Fidelity  

## ✨ Stardust  
upstream compromise, supply‑chain, signed artifacts, forensic telemetry, credential rotation  

*Upstream Compromise Checklist | Part of Polaris Protocol Field Ops Stack.*  

*Last updated 2026-01-01*
