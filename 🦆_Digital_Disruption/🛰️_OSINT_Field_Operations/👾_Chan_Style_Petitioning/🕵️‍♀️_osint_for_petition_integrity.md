# 🕵️‍♀️ OSINT for Petition Integrity  

**First created:** 2025-11-02  
*Open-source methods for checking whether an online petition or mobilisation campaign is real, amplified, or manufactured.*

---

## 🧭 Orientation  

Digital petitions create the illusion of mass consensus at very low cost.  
Before citing or sharing one, trace its **velocity**, **geography**, and **amplifiers**.  
This node gives a reproducible workflow that any researcher or journalist can follow using only open data.

---

## ⚙️ 1 · Locate the Source Data  

Official UK petitions expose their data through a public JSON API:  

```
https://petition.parliament.uk/petitions/<petition-id>.json
```

Example:  
`https://petition.parliament.uk/petitions/700143.json`

Download the JSON and save it with timestamped filename:  
`petition_700143_2025-11-02T21-00Z.json`

---

## ⚙️ 2 · Check Growth Velocity  

Plot signatures over time.  
A normal, organic petition shows **gradual adoption** with small bursts after press coverage.  
Synthetic or botted campaigns show **vertical jumps** — thousands of signatures within minutes.

```bash
jq '.data.attributes.signature_count_by_day' petition_700143.json > sigs.csv
```

Visualise with any charting tool.  
> ⚠️  Velocity > 5 % of total within a single minute = probable automation.

---

## ⚙️ 3 · Inspect Geography  

Every signature includes an optional country / constituency field.  
Compute ratios:

| Field | Organic Range | Red-flag |
|--------|----------------|----------|
| UK Constituency coverage | 70–90 % | < 60 % |
| “Unknown” or foreign country codes | < 10 % | > 20 % |
| Concentration | bell-curve | spikes in tiny areas |

```bash
jq '.data.attributes.signatures_by_country' petition_700143.json
```

---

## ⚙️ 4 · Trace Amplification  

1. Use open-source search tools to find who first shared the petition link.  
2. Log top 10 accounts by engagement.  
3. Check account age + follower ratio.  
4. Look for identical text strings or hashtags → copy-paste network.  
5. Archive screenshots of the posts.

**Red-flags:**  
- Same caption repeated > 5 × within one hour.  
- Accounts with creation dates within 7 days of the campaign.  
- Cross-posting from meme or crypto-promo networks.

---

## ⚙️ 5 · Correlate with External Events  

Match spikes to specific broadcasts or influencer posts.  

| Time (UTC) | Event | Signature Jump |
|-------------|--------|----------------|
| 20:00 | Tweet by influencer | +300 000 |
| 20:07 | Petition site lag | +200 000 |
| 21:00 | Server throttling | plateau |

---

## ⚙️ 6 · Archive and Report  

- Save all JSON dumps, screenshots, and charts under `archives/petitions/`.  
- Compute SHA-256 hashes for integrity.  
- Mirror to at least two independent repositories (`cross_mirroring_sop.md`).  
- Publish a short transparency note:  
  > “Signature data verified DD-MM-YYYY; anomalies observed XYZ % non-UK origins.”

---

## 🧩 Optional : Quick Verification Script  

```bash
#!/usr/bin/env bash
id=$1
curl -s "https://petition.parliament.uk/petitions/$id.json" | jq '{title: .data.attributes.action,
      signature_count: .data.attributes.signature_count,
      countries: .data.attributes.signatures_by_country}'
```

---

## 🌌 Constellations  

🕵️‍♀️ 📡 ⚖️ 🧾 — verification · transparency · civic hygiene  

---

## ✨ Stardust  

petition integrity, OSINT, digital forensics, velocity analysis, bot detection, transparency, civic literacy  

---

## 🏮 Footer  

*🕵️‍♀️ OSINT for Petition Integrity* is a practical node of the Polaris Protocol.  
It teaches open-source verification of mass-signature campaigns and protects civic discourse from synthetic mobilisation.  

> 📡 Cross-references:  
> - [🕵️‍♀️ Synthetic Mobilisation and Petition Farms](🕵️‍♀️_synthetic_mobilisation_and_petition_farms.md) — analytic background  
> - [📡 Language as Attack Surface](../../../Disruption_Kit/Big_Picture_Protocols/📡_language_as_attack_surface.md) — information-warfare context  
> - [🧾 Archive Capture Template](../../../Disruption_Kit/Big_Picture_Protocols/templates/archive_capture_template.md) — data preservation  
> - [🪞 Cross-Mirroring SOP](../../../Operational_Kits/archives/cross_mirroring_sop.md) — redundancy  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated 2025-11-02_
