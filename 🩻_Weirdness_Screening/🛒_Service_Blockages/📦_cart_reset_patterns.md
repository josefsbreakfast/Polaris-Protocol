# 📦 Cart Reset Patterns
**First created:** 2025-11-02 | **Last updated:** 2025-11-02  
*Disappearing baskets, session purges, and interrupted flows.*

---

## 🧭 Orientation
When carts empty themselves on refresh or step transitions, record the *where* and *when* to isolate feature flags vs containment flags.

---

## 🌱 Purpose
- Identify UX‑layer manipulations that discourage completion.  
- Correlate cart resets with product categories and news cycles.

---

## 🧪 Minimal Record (YAML front‑matter)
```yaml
when: 2025-11-02T12:00:00Z
site: "RetailerZ.com"
session_id: "abc123"
symptom: "Cart empties on shipping step"
error: "SESSION_EXPIRED"
artifacts: [cart_full.png, cart_empty.png]
repro: {"incognito": true, "vpn": false, "mobile": false}
notes: "Only SKUs tagged camping; electronics persist"
tags: [cart_reset, shipping_step]
```

---

## 🧾 Log Template
| when (UTC) | site | session | step | retained items? | error text | artifacts | repro notes |
|---|---|---|---|---|---|---|---|
|  |  |  | add‑to‑cart / shipping / payment |  |  |  |  |

---

## 🛰️ Pattern Hooks
- Reset only when flagged keywords present in basket (e.g., tents, SIMs).  
- Resets begin/stop around policy events; persists across browsers.

---

## 🔗 Cross‑references
- [🪞 Retail Shadowban Index](./🪞_retail_shadowban_index.md)  
- [📈 Service Blockage Timeline](./📈_service_blockage_timeline.md)

---

## ✨ Stardust
cart emptying, session manipulation, UX throttling, soft lockout

---

## 🏮 Footer
Part of **🛒 Service Blockages**. Carts are memory; forced forgetting is a signature.
