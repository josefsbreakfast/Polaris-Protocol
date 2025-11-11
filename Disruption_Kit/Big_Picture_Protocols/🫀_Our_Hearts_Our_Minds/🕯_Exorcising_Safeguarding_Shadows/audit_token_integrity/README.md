---
title: "🪙 Token Integrity Audit — Subfolder Overview"
created: 2025-11-10
last_updated: 2025-11-10
authors:
  - Polaris Systems & Governance Working Group
cluster: "🧩 System Governance / ⚖️ Legal & State Governance"
purpose: >
  To maintain accuracy and role directionality across pseudonymised datasets that
  include both offender and victim records.  
  This folder contains the templates, checklists, and plain-language resources required
  to perform a Token Switching & Relationship Integrity Audit.
status: "Active — shared for internal and partner use"
---

# 🪙 Token Integrity Audit  
*Preventing cross-system contamination through token switching and role inversion.*

---

## 🧭 Purpose

Justice and safeguarding datasets often rely on pseudonymised identifiers (“tokens”)
to protect individuals’ identities while allowing data linkage.
When those tokens are re-issued or mis-mapped, **token switching** can occur.
If relationship fields (`victim_of`, `offender_of`, `related_to`) are not tightly defined,
records can invert roles, creating **data twins** and contaminating analytic outputs.

This audit framework ensures that:
- Tokens remain unique and traceable through their lifecycle.  
- Relationship direction is maintained across all exports and mirrors.  
- Corrections propagate to secondary systems within defined timeframes.  

---

## 📁 Folder Contents

| File | Description |
|------|--------------|
| **🪙_token_switching_audit_overview.md** | Executive-summary node for readers who want a conceptual explanation without YAML. |
| **🧾_token_integrity_audit_template.yaml** | Full technical checklist and scoring matrix for auditors or information-governance teams. |
| **📊_sample_reporting_table.md** | Example of how audit results can be summarised and visualised. |
| **📚_references.md** | Supporting frameworks and external standards (GDPR, ICO, ISO, NIST). |

---

## 🧮 Expected Outputs

| Deliverable | Description |
|--------------|-------------|
| **Token Collision Report** | Quantifies duplicate pseudonym IDs across systems. |
| **Directionality Matrix** | Confirms that victim/offender roles are preserved. |
| **Propagation Timeline** | Measures delay between corrections and mirrored datasets. |
| **Recommendations Log** | Prioritised fixes for system owners and data controllers. |

---

## ⚙️ Implementation Notes

- Run this audit **after any major system migration, schema change, or data-sharing renewal.**  
- Each participating organisation should maintain its own copy of the YAML template,
  signed off by the Data Protection Officer.  
- Non-technical reviewers can read the Markdown overview and completed reporting tables.  
- Results should feed into annual **Data Accuracy Statements** under Article 5(1)(d) UK GDPR.

---

## 🧠 Related Polaris Nodes

| Node | Function |
|------|-----------|
| `💾_token_switching.md` | Mechanism of pseudonym rotation errors. |
| `🧬_data_twinning.md` | Downstream effect of token and role fusion. |
| `🧮_data_error_decay_table.md` | Typical lifespan of data anomalies. |
| `🧾_data_lineage_review.md` | How to request or conduct provenance tracing. |

---

## 📚 References
- UK GDPR Art. 5(1)(d) — Accuracy  
- Data Protection Act 2018 s. 171 — Compliance Orders  
- ICO Data-Sharing Code of Practice (2021)  
- ISO/IEC 27701 § 7.4 — Pseudonymisation Integrity  
- NIST SP 800-188 — De-Identification Risk Metrics  

---

*Maintained within the Polaris Protocol repository.  
Contact: Systems & Governance Cluster Leads*
