# 🪙 Token Switching & Relationship Integrity Audit — Executive Overview  
**First created:** 2025-11-10 | **Last updated:** 2025-11-11  
*Operational guide for identifying and correcting pseudonym and role-direction errors across justice and safeguarding data systems.*  

---

## 🧭 Purpose  

To ensure that pseudonymisation (“tokenisation”) and relational fields (`victim_of`, `offender_of`, `related_to`) remain stable across system migrations, exports, and research datasets.  

The audit detects:  
- Token duplication or “token switching”  
- Role inversion or data-twinning  
- Gaps in propagation of data corrections  

---

## 🧩 Why It Matters  

Even anonymised data can contaminate downstream systems if two people share a token or if relational fields lose directionality.  
This audit protects:  
- Victim confidentiality  
- Offender-management accuracy  
- Institutional credibility and legal compliance (UK GDPR, Data Protection Act 2018, Section 170 offences)  

---

## 🧮 Key Questions Auditors Ask  

1. Have pseudonym tokens ever been re-issued or rotated?  
2. Are lookup tables between token generations encrypted and reconciled?  
3. Are role fields (`victim_of`, `offender_of`, `related_to`) always populated and non-symmetric?  
4. Do API joins use **person-level** rather than **case-level** keys?  
5. How quickly do data corrections propagate to mirror systems?  

---

## 🧱 How to Read the YAML Template  

The companion file `🧾_token_integrity_audit_template.yaml` defines:  
- **Audit scope** — systems and date range  
- **Checks** — token lineage, mapping tables, role directionality, joins, audit trails  
- **Metrics** — collision rate, reversal rate, propagation lag  

Non-technical reviewers can skip YAML details and read the *Summary findings* section once populated.  

---

## 🕊️ Deliverables  

| Output | Description |
|--------|-------------|
| **Token-collision report** | Flags duplicate pseudonym IDs across systems |
| **Directionality matrix** | Confirms victim/offender roles preserved |
| **Propagation timeline** | Shows time from correction → mirror update |
| **Recommendations log** | Prioritised fixes and policy updates |

---

## ⚙️ Governance Reference  

- **UK GDPR Art. 5(1)(d)** — Accuracy  
- **Data Protection Act 2018 s. 171** — Enforced subject rights  
- **ICO Data-Sharing Code of Practice (2021)**  
- **ISO 27701 § 7.4** — Pseudonymisation Integrity  

---

## 💡 Implementation Tip  

Run this audit after:  
- Any **system migration or vendor change**  
- Any **data-sharing agreement renewal**  
- Any **incident where role inversion or duplicate records** are suspected  

---

## 📚 Related Polaris Nodes  

- `🧬_data_twinning.md` — downstream effect of token and role fusion  
- `💾_token_switching.md` — mechanism of pseudonym rotation errors  
- `🧮_data_error_decay_table.md` — lifespan of data anomalies  
- `🧾_data_lineage_review.md` — provenance tracing and record review  

---

## 🌌 Constellations  

🧠 ⚖️ 🪙 🕯 🫀 — governance, legality, ethics, integrity, and care through data truth.  

---

## ✨ Stardust  

token switching, pseudonymisation, relationship integrity, data audit, safeguarding systems, justice datasets, role inversion, victim confidentiality, governance ethics, GDPR compliance  

---

## 🏮 Footer  

*🪙 Token Switching & Relationship Integrity Audit — Executive Overview* is a living node of the Polaris Protocol.  
It functions as the **conceptual overview** for the Token Integrity Audit process within  
*🕯 Exorcising Safeguarding Shadows → 🫀 Our Hearts Our Minds → Big Picture Protocols → Disruption Kit*.  

> 📡 Cross-references:
> 
> - [🪙 Token Integrity Audit — Subfolder Overview](./README.md) — index and templates  
> - [🕯 Exorcising Safeguarding Shadows](../) — audit cluster and case re-alignment  
> - [🫀 Our Hearts Our Minds](../../) — humane governance and trauma ethics  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-11-11_
