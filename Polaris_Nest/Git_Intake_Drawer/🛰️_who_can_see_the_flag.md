# 🛰️ Who Can See the Flag  
**First created:** 2025-11-12 | **Last updated:** 2025-11-12  
*Visibility layers for OSA-style or “Restricted” metadata flags across civilian and defence-adjacent systems.*

---

## 🧭 Orientation  
When a record carries a protective-marking string — “OSA,” “Restricted,” or “Official-Sensitive” — multiple tiers of staff may see that label even if they cannot access the underlying content.  
This node maps *who* can see *what* within local government, NHS, and defence-partner contexts, clarifying why a single mistaken tag can spread through networks for years.

---

## 🪞 Visibility Layers  

```mermaid
graph TD
    A[Metadata Tag Created<br>(e.g., "OSA / Restricted")] --> B1[Local Security / SIRO / DSO]
    A --> B2[DPO / IG Manager]
    A --> B3[Legal / Monitoring Officer]
    A --> B4[System Administrators]
    B1 --> C1[MOD or Vetting Oversight<br>(if linked dataset)]
    B3 --> C2[Corporate Leadership / Audit & Risk]
    B4 --> C3[Downstream Partner Systems<br>(NHS, Police, MoJ)]
```

---

### 🧩 Layer Summary  

| Tier | Role | Typical Access | Comment |
|------|------|----------------|----------|
| **1** | **Originating Officer / Record Owner** | Sees and sets the tag | May mis-apply OSA due to risk aversion or legacy forms. |
| **2** | **DSO / SIRO / Caldicott Guardian** | Sees full metadata, limited content | Approves or removes markings in protective-security systems. |
| **3** | **DPO / Information Governance Lead** | Sees all data for compliance | Must verify that any national-security claim has a lawful basis. |
| **4** | **Monitoring Officer / Head of Legal** | Sees both tag and underlying file | Final sign-off for exemptions; single-point containment risk. |
| **5** | **System Administrators / ICT** | See tag label only, no content | Replicate restrictions automatically; rarely verify meaning. |
| **6** | **External Partners (NHS / MoJ / MOD)** | May see inherited “restricted” markers | Often treat them as genuine; source rarely questioned. |

---

## 🔍 Key Insight  
A false flag can live for years because each layer assumes the one above had authority.  
The fix requires both **protective-security review (SIRO/DSO)** *and* **data-protection rectification (DPO/Monitoring Officer)** to act jointly.

---

## 🌌 Constellations  
🛰️ 🧱 🔮 ⚖️ 🧠 — visibility, metadata architecture, governance, and procedural integrity.

---

## ✨ Stardust  
osa metadata, protective marking, visibility layers, siro, dpo, monitoring officer, containment mapping, structural analysis, governance hygiene, data rectification  

---

## 🏮 Footer  

*🛰️ Who Can See the Flag* is a living node of the **Polaris Protocol**.  
It maps how mis-applied protective markings propagate through civilian infrastructures, showing where containment hardens and where it can be undone.

> 📡 Cross-references:  
> – [📮 OSA Flag Clarification Request](../Disruption_Kit/Survivor_Tools/📮_osa_flag_clarification_request.md)  
> – [☔️ Protocol Integrity SOP](../🏮_Polaris_Nest/☔️_protocol_integrity_sop.md)  
> – [🧟‍♀️ Residual Shadows](../Metadata_Sabotage_Network/🔥_Data_Risks/🧟‍♀️_Residual_Shadows/)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-11-12_
