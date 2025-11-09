# 📚 Resource Guides Schema
**First created:** 2025-11-09 | **Last updated:** 2025-11-09  
*Template for encoding expectation-calibrated resource lists within Polaris*

---

## 🧭 Orientation  
Resource Guides allow Polaris nodes to link out to books, podcasts, and articles **without implying endorsement**.  
Each resource is tagged for *quadrant position*, *tone*, and *use value*, helping readers anticipate worldview and register before engaging.  

The schema is designed to be simple, transparent, and machine-readable for later visualisation.

---

## 🧩 YAML Schema  

```yaml
- title: "string"                      # Resource title
  type: "book | podcast | article | website | report"
  author: "string"                     # Author or creator
  year: YYYY                           # Optional
  quadrant: [authority|autonomous, collective|individual]
  strength: "what it does well"
  bias: "declared or evident worldview"
  tone: "tone register — analytical, conversational, provocative, etc."
  polaris_use: "how it fits into the wider project"
  link: "url"
```

---

## 🗺️ Quadrant Legend  

| Quadrant | Meaning |
|-----------|----------|
| **Authority–Collective (AC)** | State, institutional, structural — often technocratic or policy-focused. |
| **Authority–Individual (AI)** | Authoritarian or moralising individual focus — hierarchy justified by “order”. |
| **Autonomous–Collective (aC)** | Mutual-aid, abolitionist, or commons-based; often decentralised civic organisation. |
| **Autonomous–Individual (aI)** | Libertarian, anti-statist, personal liberty orientation. |

Each resource may sit between two poles, e.g. `[autonomous, collective]` → 🕊️🐝.  

---

## 🧭 Usage  

1. Add new entries to your `.yaml` guide files using this schema.  
2. Reference them inside nodes using short code blocks or excerpts.  
3. Optional: add an “Expectation” line like:  
   > *Expectation: liberal-institutional frame, dense but data-rich.*  
4. In future, these can be visualised as quadrant maps.

---

## 🌌 Constellations  

📚 🧿 🛰️ 🔮 — literacy, nuance, expectation management, epistemic transparency  

---

## ✨ Stardust  

resource guides, metadata schema, expectation management, epistemic mapping, civic literacy  

---

## 🏮 Footer  

*📚 Resource Guides Schema* is a scaffolding node of the Polaris Protocol.  
It standardises how external readings, podcasts, and media are annotated to maintain clarity across ideological spectra.

> 📡 Cross-references:  
> - [🧿 SASSI as Counter-Surveillance Accountability](../🧿_sassi_as_counter_surveillance_accountability.md)  
> - [⚖️ United Fronts as Democratic Defence](../⚖️_united_fronts_democratic_defence.md)  
> - [🐝 All In Commons](../../🦆_Digital_Disruption/🐝_All_In_Commons)

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2025-11-09_
