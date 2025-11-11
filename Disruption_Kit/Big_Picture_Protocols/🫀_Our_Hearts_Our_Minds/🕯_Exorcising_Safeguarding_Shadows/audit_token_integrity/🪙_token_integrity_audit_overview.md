# 🪙 Token Switching & Relationship Integrity Audit — Executive Overview
**First created:** 2025-11-10 | **Last updated:** 2025-11-10  
*Operational guide for identifying and correcting pseudonym and role-direction errors across justice and safeguarding data systems.*

---

## 🧭 Purpose
To ensure that pseudonymisation (“tokenisation”) and relational fields (victim/offender/related) remain stable across system migrations, exports, and research datasets.  
The audit detects:
- Token duplication or “token switching”
- Role inversion or data-twinning
- Gaps in propagation of data corrections

---

## 🧩 Why it matters
Even anonymised data can contaminate downstream systems if two people share a token or if relational fields lose directionality.  
This audit protects:
- Victim confidentiality  
- Offender-management accuracy  
- Institutional credibility and legal compliance (UK GDPR, Data Protection Act 2018, Section 170 offences)

---

## 🧮 Key questions auditors ask
1. Have pseudonym tokens ever been re-issued or rotated?  
2. Are lookup tables between token generations encrypted and reconciled?  
3. Are role fields (`victim_of`, `offender_of`, `related_to`) always populated and non-symmetric?  
4. Do API joins use **person-level** rather than **case-level** keys?  
5. How quickly do data corrections propagate to mirror systems?

---

## 🧱 How to read the YAML template
The companion file `🧾_token_integrity_audit_template.yaml` defines:
- **Audit scope** (systems, date range)  
- **Checks** (token lineage, mapping tables, role directionality, joins, audit trails)  
- **Metrics** (collision rate, reversal rate, propagation lag)

Non-technical reviewers can skip YAML details and read the “Summary findings” section once populated.

---

## 🕊️ Deliverables
| Output | Description |
|--------|--------------|
| **Token-collision report** | Flags duplicate pseudonym IDs across systems |
| **Directionality matrix** | Confirms victim/offender roles preserved |
| **Propagation timeline** | Shows time from correction → mirror update |
| **Recommendations log** | Prioritised fixes and policy updates |

---

## ⚙️ Governance reference
- UK GDPR Art. 5(1)(d) (Accuracy)  
- Data Protection Act 2018 s. 171 (Enforced subject rights)  
- ICO Data-Sharing Code of Practice (2021)  
- ISO 27701 § 7.4 (Pseudonymisation integrity)

---

## 💡 Implementation tip
Run this audit after:
- Any **system migration or vendor change**
- Any **data-sharing agreement renewal**
- Any **incident where role inversion or duplicate records** are suspected

---

## 📚 Related Polaris nodes
- `🧬_data_twinning.md`  
- `💾_token_switching.md`  
- `🧮_data_error_decay_table.md`  
- `🧾_data_lineage_review.md`

---

*Prepared for shared deployment within Polaris Protocol under the Systems & Governance cluster.*
