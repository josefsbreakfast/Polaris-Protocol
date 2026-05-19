# 🏧 ATM Freeze Patterns
**First created:** 2025-11-02 | **Last updated:** 2026-05-19  
*Machine-level errors and timing motifs.*

---

## 🧭 Orientation
Catalogue **repeating ATM faults**: host timeouts, card capture events, partial cash dispenses, receipt printer failures.

---

## 🌱 Purpose
- Map **error-code families** (e.g., 093, 114, 116) to timing and location.  
- Detect **postcode or venue clustering** (near courts, stations, protest sites).

---

## 🧪 Minimal Record (YAML front-matter)
```yaml
when: 2025-11-02T18:05:00Z
network: "LINK / Visa Plus / Bank ATM"
location: "Street, City"
symptom: "HOST UNAVAILABLE"
duration: "10m"
cash_dispensed: false
error_code: "091"
artifacts: [atm_screen.jpg, receipt.jpg]
notes: "Multiple users queued; contactless withdrawal also failed"
tags: [atm_freeze, host_timeout]
```

---

## 🧾 Pattern Table
| when (UTC) | network | location | error code | cash dispensed | duration | artifacts | notes |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

> Photograph **error screens** and retain receipts; code strings are crucial.

---

## 🔗 Cross-references
- [💳 Payment System Outage Registry](./💳_payment_system_outage_registry.md)  
- [📈 Infrastructure Sync Chart](./📈_infrastructure_sync_chart.md)

---

## ✨ Stardust
atm host timeout, card capture, receipt error, cash dispense fault

---

## 🏮 Footer
Part of **🚉 Infrastructure Hiccups**. Cash points are canaries; watch their song.

2026-05-19
