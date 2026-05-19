# 💳 Payment System Outage Registry
**First created:** 2025-11-02 | **Last updated:** 2026-05-19  
*Financial rails: cards, ATMs, bank networks, merchant acquirers.*

---

## 🧭 Orientation
A ledger of **payment rail disruptions**: card terminals down, PSP API faults, Faster Payments delays, ATM host timeouts.

---

## 🌱 Purpose
- Differentiate issuer, scheme, acquirer, and merchant failures.  
- Detect **geographic or temporal clustering** around civic flashpoints.  
- Build an evidence base with **auth IDs / RRN / STAN** where available.

---

## 🧪 Minimal Record (YAML front-matter)
```yaml
when: 2025-11-02T12:00:00Z
provider: "PSP/Acquirer e.g., Worldpay"
surface: "Retail terminals / eCom"
symptom: "Widespread 'unable to connect to host'"
duration: "20m"
scope: "Multiple cities"
codes: ["05 DO NOT HONOUR", "91 ISSUER UNAVAILABLE"]
artifacts: [terminal_screen.jpg, status_page.png]
notes: "Charities reporting donation failures during vigil"
tags: [payment_stall, rails_outage]
```

---

## 🧾 Registry Table
| when (UTC) | provider | surface | scope | symptom | codes | duration | artifacts | notes |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

> Capture **RRN/STAN** if a slip prints. Ask merchants which PSP they use.

---

## 🔗 Cross-references
- [🏧 ATM Freeze Patterns](./🏧_atm_freeze_patterns.md)  
- [📈 Infrastructure Sync Chart](./📈_infrastructure_sync_chart.md)  
- [🧰 Field Kit — Infrastructure Logs](./🧰_field_kit_infrastructure_logs.md)

---

## ✨ Stardust
psp outage, scheme decline, rails disruption, faster payments delay, settlement fault

---

## 🏮 Footer
Part of **🚉 Infrastructure Hiccups** (Weirdness Screening). Payment rails are civic plumbing; log with precision.
2026-05-19
