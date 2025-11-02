# 🪞 Retail Shadowban Index
**First created:** 2025-11-02 | **Last updated:** 2025-11-02  
*Catalogues of suppressed, delisted, or unsearchable products.*

---

## 🧭 Orientation
A rolling index of products that vanish from search, appear only via direct URL, or rank far below expectation despite availability.

---

## 🌱 Purpose
- Detect algorithmic invisibility at the discovery layer.  
- Compare site search vs external search for the same SKU/ISBN.

---

## 🧪 Minimal Record (YAML front‑matter)
```yaml
when: 2025-11-02T12:00:00Z
site: "Bookseller.example"
sku: "9780141991443"
query: "book title exact"
symptom: "No result in site search; direct URL loads"
artifacts: [site_search.png, direct_url.png]
alt_retailers: ["RetailerA", "RetailerB"]
notes: "Variant ISBN ranks normally"
tags: [shadowban, ranking_suppression]
```

---

## 🧾 Index Table
| when (UTC) | site | sku | query | rank / visibility | direct URL loads? | alt retailers | artifacts |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

---

## 🧬 Tests
- Exact match vs fuzzy match queries.  
- Signed‑in vs signed‑out.  
- Regional VPNs and language toggles.

---

## 🔗 Cross‑references
- [🧾 Phantom Stock Registry](./🧾_phantom_stock_registry.md)  
- [📈 Service Blockage Timeline](./📈_service_blockage_timeline.md)

---

## ✨ Stardust
search suppression, delisting, ranking bias, algorithmic invisibility

---

## 🏮 Footer
Part of **🛒 Service Blockages**. If you can only buy what you can find, search is policy.
