# 🛰️ AI Targeting & “Risk Management” — Unit 8200 Stack (LLM + Lavender/Gospel)  
**First created:** 2025-10-17 | **Last updated:** 2025-10-17  
*Open-source picture of how Israel’s Unit 8200–linked systems are reported to work: an LLM for intel triage plus ML targeters (Lavender / Gospel / “Where’s Daddy?”), and the policy “risk knobs” that shape harm.*
<!--Firstly:  
It's Day 2 of my period and even I can look at grown men naming a new toy, "Where's Daddy?" and think, "awww... they miss their dads, how sweet".  
How old are we?! 🤣🤣🤣  -->
---

## 🧭 Orientation  
Two layers recur across reporting:  
1. **Targeting / triage ML** (e.g., *Lavender* for people, *Gospel / Habsora* for places, timing via *“Where’s Daddy?”*), and  
2. a **ChatGPT-like LLM** reportedly trained on mass-intercepts to answer analysts’ questions over surveillance corpora.  
Together they accelerate candidate generation and briefing, while internal “risk-management” thresholds determine what gets hit and when.

---

## 🗺️ Systems at a Glance

| System | Reported role | Inputs (reported / inferred) | Outputs to | Notes |
|--------|---------------|------------------------------|-------------|-------|
| **Lavender** | People-ranking for strikes (confidence-scored candidates) | Telecom metadata / content, social graph, device IDs, geolocation, prior intel logs | Target Administration Directorate; operational units | Flagged very large cohorts; rapid human checks at tempo. |
| **Gospel / Habsora** | Infrastructure / places targeting | Multi-INT fusion incl. imagery + comms patterns | Target lists (buildings / structures) | Described as scaling target throughput (“factory”). |
| **“Where’s Daddy?”** | Timing / locational layer (when target is at home) | Movement / routine telemetry fused to person record | Strike-timing recommendations | Cited alongside Lavender. |
| **8200 LLM (ChatGPT-like)** | Analyst assistant over intercept troves (RAG-style Q&A, summaries, link maps) | Large intercept corpus (Arabic / Hebrew comms), case files; vector search | Briefs, entity / link summaries; hypothesis prompts | Reported in training / roll-out c. 2024–25. |

---

## ⚙️ How the Pipeline Is Proposed to Work  
1. **Ingest & index** multi-source data (SIGINT transcripts, device graphs, imagery)  
2. **Model scoring** of people / places  
3. **Policy thresholds** (who / what qualifies; permitted collateral)  
4. **Human sign-off** under tempo  
5. **Tasking to units**  
6. **Post-strike logging**  
High tempo + permissive thresholds can shift practical control toward model outputs.

---

## 🧮 “Risk Management” Knobs (Policy Dials)  
- **Score thresholds:** what model confidence triggers surfacing / action.  
- **Collateral tolerance:** internally set ceilings per target class (policy encoded into workflow).  
- **Tempo vs. scrutiny:** higher tempo → smaller review budget per target.  
- **Data scope:** breadth / depth of intercepts included (affects bias + reach).

---

## 🧨 Known / Expected Failure Modes  
- **Bias & label leakage:** historic suspicion labels become “ground truth,” reinforcing errors.  
- **Goal mis-specification:** optimise for target throughput rather than civilian-harm minimisation.  
- **LLM over-trust:** fluent but wrong link summaries propagate into briefs.  
- **Accountability diffusion:** builders vs. policy setters vs. operators vs. legal sign-off blur responsibility.

---

## 🧰 Stack / Infrastructure Context (public reporting)  
Large-scale cloud use (e.g., hyperscale storage / indexing) has been described in recent investigations; corporate governance decisions have affected access in some periods, indicating external checks on state AI stacks.

---

## 🧭 Oversight / Critiques (open record)  
- UN experts and NGOs have criticised AI-assisted high-throughput targeting and urged scrutiny.  
- Legal debates frame these as decision-support tools, but **human-in-the-loop quality** remains the legality hinge.  
- Policy syntheses warn of systematic misidentification at scale under permissive thresholds.

---

## 🌌 Constellations  
🛰️ SIGINT • 🧠 LLMs • 🪪 metadata • 🕸️ link-analysis • 🎛️ thresholds • ⚖️ proportionality • 📡 cloud stack

---

## ✨ Stardust  
lavender • habsora / gospel • “where’s daddy?” • intercept corpora • decision-support vs. autonomy • collateral policy dials

---

## 🏮 Footer  
*AI Targeting & “Risk Management” — Unit 8200 Stack* is a living node of the Polaris Protocol.  
It collates reputable open sources on reported systems and highlights where policy choices (“risk knobs”) drive outcomes as much as code.

> 📡 Cross-references: consider linking to **Genocide Denialism**, **Narrative Management**, and **Metadata Sabotage Network** clusters.

---

**Suggested filename:**  
`Disruption_Kit/Big_Picture_Protocols/🛰️_AI_Targeting_Risk_Management/🛰️_unit_8200_llm_lavender_pipeline.md`
