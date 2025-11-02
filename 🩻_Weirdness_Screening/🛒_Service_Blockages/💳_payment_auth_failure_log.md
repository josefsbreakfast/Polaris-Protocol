# 💳 Payment Auth Failure Log
**First created:** 2025-11-02 | **Last updated:** 2025-11-02  
*Transaction denials and inexplicable reversals across processors.*

---

## 🧭 Orientation
Capture payment‑layer behavior: approvals, soft/hard declines, 3‑DS loops, and reversals that lack a valid cause code.

---

## 🌱 Purpose
- Differentiate bank‑side vs merchant‑side denials.  
- Spot metadata‑driven filtering (postcode, device fingerprint, commodity class).

---

## 🧪 Minimal Record (YAML front‑matter)
```yaml
when: 2025-11-02T12:00:00Z
site: "RetailerY.app"
amount: 29.99
currency: "GBP"
method: "Visa Credit"
symptom: "3‑DS loop then hard decline"
error: "DO_NOT_HONOUR"
processor: "Adyen"
artifacts: [3ds_prompt.png, decline_msg.png]
device: "iOS 18.6.2 Safari"
network: "Home ISP"
notes: "Same card succeeded on other retailer within 5 min"
tags: [auth_denial, 3ds_loop]
```

---

## 🧾 Log Template
| when (UTC) | site | amount | currency | method | processor | result | code/text | step | artifacts |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | soft decline / hard decline / reversal |  | pre‑auth / 3‑DS / capture |  |

> Where possible request **auth/correlation IDs** and note them verbatim.

---

## 🧩 Differentiators
- Same card succeeds for small basket but fails for survival/activism SKUs.  
- Declines by postcode/VPN, passes on mobile data.  
- Repeated *"do not honor"* without issuer explanation.

---

## 🔗 Cross‑references
- [🧾 Phantom Stock Registry](./🧾_phantom_stock_registry.md)  
- [📦 Cart Reset Patterns](./📦_cart_reset_patterns.md)  
- [🧰 Consumer Countermeasure Kit](./🧰_consumer_countermeasure_kit.md)

---

## ✨ Stardust
payment denial, processor filtering, risk scoring, 3‑DS loop, correlation ID

---

## 🏮 Footer
Part of **🛒 Service Blockages**. Payment layers are permission systems; log them like evidence.
