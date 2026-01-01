# 🛰️ Exchange Authentication Anomaly — Pre-FOIA Deadline  
**First created:** 2025-10-27 | **Last updated:** 2026-01-01  
*Spike in Exchange-level sign-in failures two weeks before statutory FOIA/SAR deadlines.*  

---

## 🧭 Orientation  

With two weeks remaining before the statutory deadline for both a **Freedom of Information Act (FOIA)** request and a **Subject Access Request (SAR)** lodged with the university, an **increase in failed Microsoft Exchange sign-in attempts** has appeared across devices.  

The failures are being logged at the **Exchange / Entra ID authentication layer**, not at device level — meaning they are reaching the **university’s Azure Active Directory tenant**, which Microsoft hosts as data processor but the university owns and controls.  

This pattern raises concern that:  
- there is either **malicious or accidental access activity** occurring within the university’s identity infrastructure, or  
- there is a **broader systemic compromise** of the institution’s authentication perimeter (e.g. credential stuffing, insider access, or sync error).

---

## 🧩 Sequence Summary  

| Timestamp Context | Observed Event | Probable Layer | Interpretation |
|--------------------|----------------|----------------|----------------|
| T-14 days (pre-deadline) | Multiple repeated sign-in failures on Exchange accounts (same devices, same credentials). | Microsoft Entra ID (Azure AD) — University tenant | Reached university-level authentication endpoint; rejected there. |
| Ongoing | No new MFA prompts; device health normal. | Device / local client layer | Local credentials stable — failure not local. |
| Prior FOIA + SAR submitted | Two weeks from legal response deadline. | Administrative governance layer | Correlation may indicate defensive infrastructure change or increased monitoring. |

---

## 🧮 Control & Ownership Table  

| Layer | Entity | Legal Role | Notes |
|-------|---------|-------------|-------|
| **Exchange Online / Entra ID Tenant** | University IT Services Division | **Data Controller** | Holds and enforces all identity, MFA, and access policies. |
| **Microsoft Cloud Infrastructure** | Microsoft Ireland Operations Ltd. | **Data Processor** | Provides hosting; logs events but does not own identities. |
| **Jisc UK Access Management Federation** | Jisc Services Ltd. | **Federation Operator** | Maintains metadata and signing keys; no visibility into user sign-ins. |
| **End-User Devices** | Researcher / survivor | **Data Subject** | Holds session tokens; receives failure notifications. |

---



## 🔁 Pattern Recurrence Analysis  

Pattern recurrence functions as the primary differentiator between an **isolated technical error** and a **systemic or targeted access pattern**.  
It is therefore crucial to record and visualise recurrence frequency, timing, and network origin.

### 🧩 Diagnostic Considerations  

1. **Temporal clustering** — If failures cluster around specific times or administrative events (e.g. FOIA/SAR milestones), this suggests intentional or procedural triggers rather than random noise.  
2. **Origin signature** — Recurrent attempts from internal subnets or VPN endpoints imply misconfiguration or insider probing; repeated external IPs indicate sustained targeting.  
3. **Policy resonance** — Alignment with password rotations, MFA rollouts, or access-policy refreshes suggests system activity; alignment with legal deadlines suggests governance-layer interference or audit response.  
4. **GDPR implication** — Under UK GDPR Articles 33–34, recurrence elevates an incident into a potential **notifiable breach** if it reflects continuing unauthorised access risk.

### 🧮 Recurrence Tracking Routine  

| Step | Purpose | Evidence | Responsible |
|------|----------|-----------|-------------|
| **Log recurrence intervals** | Identify periodicity (daily, weekly, event-linked). | Extract timestamps from Entra ID sign-in logs (group by day/hour). | Researcher / Analyst |
| **Correlate with institutional calendar** | Check overlap with FOIA/SAR deadlines, policy pushes, maintenance windows. | Overlay chart of anomalies vs key admin events. | Researcher |
| **Compare IP source categories** | Determine internal vs external origin. | GeoIP lookup + university network ranges. | IT Security (on DPO request) |
| **Escalate if recurrence > 3 cycles** | Trigger formal security incident review. | Updated log attached to DPO report. | Researcher → DPO |

---

## 🧾 Next Actions (Merged and Updated)

| Action | Purpose | Evidence to Capture | Responsible |
|--------|----------|--------------------|--------------|
| 1. Export Entra ID sign-in logs | Verify exact timestamps, IPs, and user agents for failed attempts. | CSV export from Entra → Monitoring → Sign-in Logs (last 14 days). | Researcher (request from university IT if access restricted). |
| 2. Cross-reference event IDs | Match Entra ID event IDs to device timestamps to confirm correlation. | Device event viewer logs + Entra ID CSV export. | Researcher / Technical Analyst. |
| 3. Notify Data Protection Officer | Record potential security incident under UK GDPR Articles 33–34. | Summary report referencing this log + timestamps of anomaly. | University DPO / Researcher. |
| 4. Note FOIA/SAR timelines | Maintain chronological table linking requests to authentication anomaly dates. | Table or chart correlating submission/response timeline. | Researcher. |
| 5. Retain export metadata | Store export checksum and file hash for evidence integrity. | SHA-256 checksum of CSV export + timestamped hash file. | Researcher. |
| 6. Assess pattern recurrence | Schedule follow-up review at T‑7 days to determine if failures persist. | Add reminder in Field Logs index or calendar. | Researcher. |
| 7. Document ongoing anomalies | Maintain forensic continuity if further sign-in failures appear. | Append entries to Field Log daily if anomalies persist. | Researcher. |

---

## 🌌 Constellations  

🛰️ 🧿 ⚖️ — Field anomaly in authentication governance; linked to system-governance oversight and accountability tracking.

---

## ✨ Stardust  

azure ad, exchange online, authentication failure, university tenant, data controller, jisc federation, microsoft ireland ops, foia timing, sar deadline, security anomaly, dpo notification

---

## 🏮 Footer  

> 📡 Cross-references:
> 
> - [1up](./README.md)  
> - [2up](../README.md)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-01-01_
