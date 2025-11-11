---
title: "📊 Token Integrity Audit — Sample Reporting Table"
created: 2025-11-10
last_updated: 2025-11-10
authors:
  - Polaris Systems & Governance Working Group
purpose: >
  Example summary format for completed Token Switching & Relationship Integrity Audits.
  Provides a concise, human-readable snapshot of results for governance boards
  and external reviewers.
status: "Template — duplicate and populate after each audit cycle."
---

# 📊 Token Integrity Audit — Reporting Summary

---

## 🧭 Audit Metadata

| Field | Value |
|--------|--------|
| **Organisation** | e.g., Nottingham City Council / University Partner |
| **Audit Lead** | Name, Role |
| **Date Range Audited** | YYYY-MM-DD → YYYY-MM-DD |
| **Systems in Scope** | SystmOne, Mosaic, nDelius, ADR UK SRS Mirror |
| **Next Scheduled Audit** | YYYY-MM-DD |
| **Overall Risk Rating** | 🔴 High / 🟠 Moderate / 🟢 Low |

---

## 🧩 Core Findings

| Metric | Description | Result | Target | Status |
|---------|--------------|---------|---------|---------|
| **Token Collision Rate** | % of pseudonym tokens attached to multiple demographic profiles | 0.8 % | ≤ 1 % | 🟢 |
| **Token Rotation without Lookup** | % of re-issued tokens missing mapping table | 3 % | ≤ 1 % | 🟠 |
| **Null Role Field Rate** | % of records missing victim/offender designation | 2 % | ≤ 0.5 % | 🔴 |
| **Role Inversion Count** | Instances where same ID logged as victim & offender | 4 | 0 | 🔴 |
| **Case-Level Joins Detected** | Joins using `case_id` instead of `person_id` | 12 | 0 | 🟠 |
| **Propagation Lag (days)** | Mean delay from correction → mirror dataset | 21 days | ≤ 7 days | 🔴 |

---

## ⚙️ System-Specific Notes

| System | Key Issue | Corrective Action | Owner | Due Date |
|---------|------------|------------------|--------|-----------|
| Mosaic | Directional fields missing in MARAC export | Update schema; add `role_type` validation rule | LA Data Team | 2026-01-31 |
| nDelius | Legacy tokens from 2019 not reconciled | Run token-collision script; re-seed offender namespace | HMPPS ICT | 2025-12-15 |
| SystmOne | Role inversion detected on two cases | Verify through patient safeguarding review | NHS IG Lead | 2025-11-30 |
| ADR UK Mirror | Propagation lag of 21 days | Accelerate nightly ETL refresh to weekly | ADR Ops | 2026-02-01 |

---

## 🧮 Summary Statistics

| Category | Value |
|-----------|-------|
| **Total Records Audited** | 42 ,500 |
| **Tokens with Errors** | 386 |
| **Records Affected by Role Inversion** | 4 |
| **Unique Systems Audited** | 4 |
| **Average Correction Propagation Time** | 21 days |

---

## 🧾 Recommendations

1. Introduce **separate token namespaces** for victims and offenders.  
2. Implement **automated directionality checks** before every data export.  
3. Require **quarterly reconciliation** of token mapping tables.  
4. Add **propagation dashboards** for DPO oversight.  
5. Include **cross-system training** on pseudonym integrity for data-entry staff.

---

## 🪞 Lessons Learned

> *Token integrity depends on both technology and attention.*  
> Even minor schema drift or lazy join logic can collapse distinctions that legal and ethical frameworks rely on.  
> Future audits should track whether the fixes above reduce the inversion and propagation metrics.

---

*Template maintained under the Polaris Protocol — Systems & Governance Cluster.*  
