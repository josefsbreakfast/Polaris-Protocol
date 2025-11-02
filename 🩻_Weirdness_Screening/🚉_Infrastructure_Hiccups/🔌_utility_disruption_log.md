# 🔌 Utility Disruption Log
**First created:** 2025-11-02 | **Last updated:** 2025-11-02  
*Power grid, telecoms, data centre, CDN, and backbone events.*

---

## 🧭 Orientation
Log **utility-layer** outages: electricity, fibre cuts, CDN edges gone dark, DNS misroutes, cloud region wobble.

---

## 🌱 Purpose
- Tie utility drops to **geographies and critical venues**.  
- Distinguish maintenance windows from **coincidental mass inconvenience**.

---

## 🧪 Minimal Record (YAML front-matter)
```yaml
when: 2025-11-02T14:22:00Z
utility: "Power / ISP / Cloud Region / CDN"
area: "Borough / City / Data centre code"
symptom: "Packet loss 80% / brownout / total loss"
duration: "30m"
scope: "X exchanges / Y postcodes"
artifacts: [ping_plot.png, ops_status.png]
notes: "Coincided with court injunction drop"
tags: [utility_outage, comms_brownout]
```

---

## 🧾 Log Table
| when (UTC) | utility | area | scope | symptom | duration | artifacts | notes |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

> If applicable, capture **ASNs, traceroutes**, and **incident IDs** from providers.

---

## 🔗 Cross-references
- [📬 Comms Breaks](../📬_Comms_Breaks/)  
- [📈 Infrastructure Sync Chart](./📈_infrastructure_sync_chart.md)

---

## ✨ Stardust
power cut, isp outage, dns failure, backbone event, data centre incident

---

## 🏮 Footer
Part of **🚉 Infrastructure Hiccups**. Utilities make the world hum; note when the hum drops.
