# 🛒 Service Blockages  
**First created:** 2025-09-16 | **Last updated:** 2026-05-19  
*Consumer-facing anomalies (shopping carts empty, items always “out of stock”).*  

---

## 🌱 Purpose  

Track **consumer-facing anomalies** that block access to goods or services — online shopping carts that clear themselves, items perpetually “out of stock,” payment authorisations that fail without cause.  
When denial of access clusters around certain categories or times, it may indicate **economic containment** disguised as logistics.  

---

## 🧩 Why These Blockages Matter  

Commerce is often mistaken for a neutral arena — a realm of choice, efficiency, and personal control.  
But in practice, shopping interfaces are also **permission systems**, deciding who may transact, what may circulate, and when scarcity appears.  

Repeated service failures — disappearing stock, broken checkout, cancelled orders — can signal:  

- **Targeted throttling** of items linked to activism, survival, or protest (e.g. SIMs, tents, books).  
- **Algorithmic invisibility**, where search ranking hides key products.  
- **Credit or payment filtering**, where approval systems flag “risk” based on metadata, postcode, or association.  
- **Psychological conditioning**, teaching resignation through inconvenience: “it’s just out of stock.”  

What looks like a consumer glitch may in fact be a controlled variable in a social experiment on access.  

---

## 🔍 Frequency  

Isolated incidents are routine — servers fail, stock runs out.  
But across survivor logs, **patterns of denial** emerge:  
- Whole product lines disappearing across multiple vendors.  
- Specific SKUs unpurchasable only from certain regions.  
- Cart resets that coincide with media or policy flashpoints.  

Mapping these interruptions exposes a **soft economic perimeter** — the invisible walls of who is allowed to buy, move, and equip.  

---

## 🧭 Representation  

| Type | Signature | Typical Cover Story | Possible Logic |
|------|------------|---------------------|----------------|
| **Phantom Stock** | Item shows “available,” checkout fails | Supply chain delay | Flagged product category or region |
| **Cart Reset** | Basket empties on refresh | Session timeout | Intentional clearance on keyword or metadata |
| **Checkout Stall** | Payment page hangs indefinitely | Payment processor lag | Behavioural throttling or user flag |
| **Selective Unavailability** | Same item in stock elsewhere | Regional demand | Targeted retail geofencing |
| **Authorization Denial** | Payment rejected for valid card | Bank risk model | Vendor-side profiling or identity suppression |

These are not always malicious — but the *timing* and *topic clustering* can reveal strategic scarcity.  

---

## 📝 What to Collect  

- **Site / app**, SKU / URL, inventory region, account status  
- **Flow step where it breaks** (add-to-cart, checkout, payment auth)  
- **Error text / codes**, request or correlation IDs  
- **Alternative SKUs / retailers tested**  
- **Timestamp** and **device / network** used  
- **Screenshots** of listing, cart, and error message  
- **Correlated context:** what was being bought, and what was happening that day?  

---

## 🧾 Minimal Record Schema (YAML front-matter)  

```yaml
when: 2025-10-05T11:32:00Z
site: "RetailerX.com"
sku: "9780141991443"
symptom: "Book shows in stock, checkout returns generic error"
error: "ERR_PAYMENT_GATEWAY_TIMEOUT"
artifacts: [screenshot_cart.png, error_page.png]
repro: {vpn: true, mobile: false}
notes: "Title is banned in several regions; alternate ISBN works"
```

---

## 🗂 Planned Nodes  

| Node | Scope | Notes |
|------|-------|-------|
| `🧾_phantom_stock_registry.md` | Inventory anomalies | Logs of items falsely marked unavailable or out of stock. |
| `💳_payment_auth_failure_log.md` | Transaction layer | Records of inexplicable declines or reversals. |
| `📦_cart_reset_patterns.md` | UX behaviour | Tracks disappearing carts or interrupted sessions. |
| `🪞_retail_shadowban_index.md` | Platform bias | Catalogues of suppressed or delisted products. |
| `📈_service_blockage_timeline.md` | Correlation chart | Overlay of outages with political or social events. |
| `🧰_consumer_countermeasure_kit.md` | Survivor tools | Guidance for alternate purchasing routes and documentation. |

Together, these nodes make the economic layer of containment visible — showing how control hides in queues, baskets, and broken buy buttons.  

---

## 🌌 Constellations  

🩻 🛒 💳 🔮 — This node sits in the consumer-infrastructure constellation, tracing how economic systems simulate scarcity as a form of suppression.  

---

## ✨ Stardust  

consumer access, shopping glitch, payment denial, digital scarcity, checkout failure, supply manipulation, service anomaly, economic containment  

---

## 🏮 Footer  

*🛒 Service Blockages* is a living node of the Polaris Protocol.  
It tracks denial of consumer access as a suppression vector — revealing how friction and scarcity can be engineered into obedience.  

> 📡 Cross-references:  
> - [🚉 Infrastructure Hiccups](../🚉_Infrastructure_Hiccups/) — large-scale public service disruptions  
> - [🔑 Access Barriers](../🔑_Access_Barriers/) — authentication and lock-out mechanisms  
> - [🎛 Systematic Patterns](../🎛_Systematic_Patterns/) — recurring or scheduled interference  
> - [Field Logs](../../Disruption_Kit/Field_Logs/) — corroborating timeline evidence  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-05-19_
