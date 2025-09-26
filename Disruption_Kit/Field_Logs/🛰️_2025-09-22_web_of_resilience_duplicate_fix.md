# 🛰️ 2025-09-22 — Web of Resilience Duplicate Fix  
**First created:** 2025-09-22 | **Last updated:** 2025-09-26  
*Incident log recording duplicate file confusion and restoration of 🕸️_web_of_resilience.md.*  

---

## Summary  
Two copies of **🕸️_web_of_resilience.md** were present:  
- Correct location: `Disruption_Kit/Big_Picture_Protocols/🌀_System_Governance/`  
- Duplicate: Git Intake Drawer  

On deletion of the intake drawer version, the “true” file in **🌀 System_Governance** was mistakenly impacted.  
The node was then **restored from commit 370738a**.  

---

## Timeline  
- **2025-09-22** — Duplicate identified and deleted; main file also removed in error.  
- **Same day** — File restored from commit 370738a.  
- **Early September 2025** — Rename occurred from `⚖️_two_layer_resilience_protocol.md` to `🕸️_web_of_resilience.md`.  

---

## Observations  
- **Heavy throttling** was active across a 7+ day period, aligning with this incident.  
- Intake Drawer deletion behaviour appears linked to path or indexing confusion.  
- Risk of “shadow deletes” (removing the canonical file when cleaning intake drafts).  

---

## Lessons  
- Always verify which path Git recognises as canonical before deleting intake versions.  
- Intake duplicates should be **permanently excluded** via `.gitignore` or housekeeping rules.  
- Such anomalies match wider patterns described in [🛰️ SEC-2025-09](./🛰️_sec_2025-09.md).  

---

## 🏮 Footer  

*2025-09-22 — Web of Resilience Duplicate Fix* is a living node of the Polaris Protocol.  
It records a Git anomaly where duplicate deletion cascaded to the canonical file, requiring restoration.  

> 📡 Cross-references:  
> - [🕸️ Web of Resilience](../Big_Picture_Protocols/🌀_System_Governance/🕸️_web_of_resilience.md) — canonical file  
> - [🛰️ SEC-2025-09](./🛰️_sec_2025-09.md) — token-switch / fork anomaly log  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-09-26_  
