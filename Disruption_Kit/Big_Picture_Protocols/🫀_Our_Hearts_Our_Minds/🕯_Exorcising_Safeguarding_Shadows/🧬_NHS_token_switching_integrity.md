# 🧬 NHS Token Switching Integrity  
**First created:** 2025-10-04 | **Last updated:** 2025-10-15  
*Audit protocol for summary-care vs local EHR token switching and evidence preservation.*  

---

## Why this matters
Token switching between the NHS Spine Summary Care Record and local EHRs can silently alter who “holds” authority over a patient narrative at write-time and read-time. This node sets immediate preservation steps and a simple field audit so current patients are protected and retrospective review is possible.

## Immediate actions (preserve now)
- Issue legal holds to trusts, ICSs, and vendors covering: access logs, auth tokens, API gateway logs, consent flags, break-glass events.  
- Freeze rotation schedules for relevant keys for 90 days.  
- Export + checksum daily deltas from SCR↔EHR sync jobs.

## 10-minute spot check
- Compare SCR consent state vs local EHR consent state on 5 live records.  
- Diff timeline: who wrote, who read, which token, which role.  
- Flag mismatches; route to senior IG.

## Risks & harms to watch
- False consent inheritance, silent role escalation, retroactive timeline edits.  

## 📡 Cross-references
- See *Death Review Integrity Audit* (../Field_Logs/🛰️_death_review_integrity_audit.md)

## 🌌 Constellations
🧿 🛠️ 📜 — oversight, fix-first, statutory alignment.

## ✨ Stardust
summary care record, spine, token switching, consent flags, audit, data integrity, legal hold

## 🏮 Footer
This is a living node of the Polaris Protocol. It defines minimum viable controls to stop narrative tampering during active investigations.

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-15_
