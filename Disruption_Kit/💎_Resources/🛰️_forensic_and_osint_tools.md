# 🛰️ Forensic & OSINT Tools  
**First created:** 2025-08-17  |  **Last updated:** 2025-10-04  
*A shared toolkit for digital and analogue evidence collection, verification, and counter-containment analysis.*

---

## Purpose
To equip investigators, journalists, and survivors with practical, lawful techniques for documenting harm and tracing systemic interference.  
The emphasis is on **verifiable, reproducible, and chain-of-custody-safe** practice — bridging open-source intelligence with survivor-centred forensics.

---

## Tool Families
| Folder | Focus |
|---------|--------|
| **`metadata_analysis/`** | Checkers, EXIF readers, and integrity verifiers for images, PDFs, and video. |
| **`osint_methods/`** | Step-by-step search guides: domain lookups, company filings, satellite and archive tools. |
| **`record_requests/`** | FOI / Subject-Access templates and escalation scripts. |
| **`harm_scan/`** | Polaris-specific forensic analytics (harm scan logs, suppression metrics, delta inversion curves). |
| **`verification_lab/`** | Cross-checking protocols, hashing utilities, and evidence packaging standards. |
| **`field_logs/`** | Annotated examples of real investigations (sanitised for safety). |

---

## Workflow Overview
1. **Acquire** – preserve the source intact (use write-blockers or read-only mounts).  
2. **Verify** – generate SHA256 or MD5 hashes immediately; record time in UTC.  
3. **Analyse** – extract metadata, check for manipulation, and compare against known baselines.  
4. **Correlate** – cross-reference with open data, public filings, or independent witnesses.  
5. **Report** – create redacted and unredacted bundles; log all software used and versions.  
6. **Store Securely** – offline encrypted archive + checksum manifest in separate location.

---

## OSINT Ethics
- Work only with data that is lawfully and publicly accessible.  
- Never expose private individuals without clear public-interest grounds.  
- Blur or redact identifying information in training materials.  
- Always log search dates, tools, and query strings for reproducibility.  
- Respect fatigue and trauma thresholds: rotate analysts, debrief often.

---

## Polaris-Specific Adaptations
- **Harm Scan Logs:** quantify suppression events per actor or platform.  
- **Suppression Metrics:** weighted indicators combining reach, removal, and redaction velocity.  
- **Delta Inversion Curves:** timeline models showing how edits propagate and reverse.  
- **Signal Leak Mapping:** overlay of metadata residue from deleted or altered records.  

Each analytic routine should have:
- plain-text documentation,  
- input/output examples, and  
- checksum-verified scripts in `/harm_scan/` or `/analysis_scripts/`.

---

## Reporting Format
Every investigation should include:
1. **Summary Narrative** – what was examined, why, and under what authority.  
2. **Evidence Table** – filename, hash, source, and chain-of-custody note.  
3. **Findings** – facts only, separated from interpretation.  
4. **Interpretive Appendix** – context, hypotheses, and links to related Polaris nodes.  

---

## 🌌 Constellations
🛰️ 🧿 ⚖️ — forensics, observation, accountability.

---

## ✨ Stardust
osint, digital forensics, metadata analysis, harm scan, suppression metrics, evidence preservation, delta inversion

---

## 🏮 Footer
Forensics is storytelling under oath.  
OSINT is what happens when the story tells you back.

*Survivor authorship is sovereign. Containment is never neutral.*  
_Last updated: 2025-10-04_
