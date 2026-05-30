# 🛰️ STASI-Style Email & Mirroring Concerns — Field Log  
**First created:** 2025-09-20 | **Last updated:** 2025-12-29  
*Field log recording observations about email mirroring, DNS-level stalling, eSIM cloning, mailbox mirroring, and the operational implications for UK surveillance visibility and attribution.*  

---

## 🌐 Factual Summary (events & observations)  
- **Event date:** 2025-09-20.  
- **Context:** User reports recurring incidents of interference, deletions, and unusual content visibility patterns.  
- **Hypotheses observed:**  
  - Self-addressed emails that avoid UK servers due to DNS routing or local MX configuration.  
  - Mailbox mirroring or unauthorised mailbox access (server-side or via backups) enabling remote reading without device compromise.  
  - eSIM or SIM cloning enabling interception or redirection of communications and recovery/verification messages.  
  - DNS-level throttling or blocking so certain messages never appear in UK monitoring pipelines.  
  - Combinations of local physical access and remote cyber intrusion (hybrid vectors).

---

## 📝 Non-Evidentiary Context (user reflection)  
- These patterns make it plausible that UK surveillance/authorities might not see all communications if those messages never hit UK-controlled infrastructure. This complicates attribution and detection for domestic agencies.  
- Multiple actors (state, organised crime, local operators) could implement similar methods; the priority is identifying and patching systemic vulnerabilities rather than premature attribution.

---

## 🔒 Investigatory Leads / Immediate Preservation Steps  
1. **Preserve affected messages and metadata** — capture raw headers, full message source, timestamps, and routing metadata. Screenshot header view as backup.  
2. **Collect device and account logs** — sign-in history, IP addresses, OAuth tokens, mailbox forwarding rules, connected apps, and admin logs.  
3. **Check MX/DNS records and routing** — capture current DNS/MX records for affected domains (use `dig` or online DNS lookup tools).  
4. **Contact telecoms / mobile provider** — ask about eSIM activity, SIM swaps, or unusual provisioning events.  
5. **Investigate mailbox backups / mirroring** — check server-side rules and third-party backups replicating mailboxes outside expected jurisdictions.  
6. **Preserve sync/backup logs** — LastSync times and activity for cloud storage/mail clients.  
7. **Create a chained timeline** — document each observed deletion, disappearance, unusual amplification, or suspicious access.  
8. **Consider a forensic image** — if legal action or formal investigation is planned, create forensic disk images of affected devices.  
9. **Legal / regulatory steps** — SARs to email providers, FOIs to public bodies, and letters to ISPs requesting logs; preserve correspondence and receipts.

---

## 🛡️ Practical Mitigations (short-term)  
- Change passwords on affected accounts from a secure device; enable hardware-backed 2FA (security keys).  
- Consider moving sensitive drafting to an air-gapped device or an encrypted offline document until preserved.  
- Avoid re-uploading or republishing sensitive material until copies and hashes are secured.  
- Use a different communications channel (Signal, ProtonMail) for coordination with trusted contacts.  
- Ask your mobile provider to freeze SIM changes until anomalies are resolved.

---

## ⚠️ Attribution Caution  
These observations and hypotheses are **not** evidence of a specific actor. They are investigatory leads reflecting plausible technical mechanisms. For attribution you will need forensic traces (server logs, carrier records, device images) and corroborating intelligence.

---

## 📍 Suggested Next Steps (research & escalation)  
1. **Preserve artefacts now** — time-sensitive logs may be overwritten by normal rotation.  
2. **Engage a digital forensic specialist** if you suspect serious compromise.  
3. **Make SAR/FOI requests** for communications metadata held by providers or public bodies.  
4. **Coordinate with trusted legal counsel** before pursuing public allegations or releases that reference named individuals or organisations.

---

## 📡 Cross-References  
> - [🛰️ Codename Table Loss (2025-09-20)] `../Field_Logs/🛰️_codename_table_loss_2025-09-20.md`  
> - [💸 Russian Overlap Patterns] `../Big_Picture_Protocols/💸_russian_overlap_patterns.md`  
---

## 🏮 Footer  

> 📡 Cross-references:
> 
> - [1up](./README.md)  
> - [2up](../README.md)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-12-29_
