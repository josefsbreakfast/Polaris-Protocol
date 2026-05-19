# 🧾 Phantom Stock Registry
**First created:** 2025-11-02 | **Last updated:** 2026-05-19  
*Inventory anomalies where items appear available but cannot be purchased.*

---

## 🧭 Orientation
A lightweight log for SKU-level anomalies that look like stock but behave like mirage. Use this registry to record, compare, and cluster incidents across vendors and time.

---

## 🌱 Purpose
- Track items that present as "in stock" yet fail at checkout or vanish on refresh.  
- Surface vendor- or category-level patterns suggestive of selective denial or controlled scarcity.

---

## 🧪 Minimal Record (YAML front‑matter)
```yaml
when: 2025-11-02T12:00:00Z
site: "RetailerX.com"
sku: "PRODUCTCODE-123"
symptom: "Shows in stock; checkout returns generic error"
error: "ERR_CHECKOUT_GENERIC"
artifacts: [listing.png, cart.png, error.png]
repro: {"vpn": true, "mobile": false}
notes: "Alternate color variant succeeds; EU region only fails"
tags: [phantom_stock, selective_unavailability]
```

---

## 🧾 Log Template (append rows below)
| when (UTC) | site | sku | region | symptom | error/code | step | artifacts | repro notes |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | add-to-cart / checkout / payment |  |  |

> Tip: keep original URLs and note exact variant/size. Vendor A/B will often diverge by a single option.

---

## 🔬 Signals to Watch
- Same SKU purchasable in one region/account but not another.  
- Variant swap (size/color/ISBN) suddenly succeeds.  
- Denials that align with events (policy votes, protests, strikes).

---

## 🔗 Cross‑references
- [💳 Payment Auth Failure Log](./💳_payment_auth_failure_log.md)  
- [🪞 Retail Shadowban Index](./🪞_retail_shadowban_index.md)  
- [📈 Service Blockage Timeline](./📈_service_blockage_timeline.md)

---

## ✨ Stardust
phantom stock, inventory mirage, selective unavailability, retail geofencing, scarcity signal

---

## 🏮 Footer
Part of **🛒 Service Blockages** (Weirdness Screening). Survivor authorship is sovereign; document precisely and early.
2026-05-19
