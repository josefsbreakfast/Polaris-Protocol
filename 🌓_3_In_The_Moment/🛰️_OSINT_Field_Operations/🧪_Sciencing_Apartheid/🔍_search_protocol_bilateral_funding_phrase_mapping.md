# 🔍 Search Protocol — Bilateral Funding Phrase Mapping  
**First created:** 2025-11-07 | **Last updated:** 2026-05-21  
*A field procedure for identifying institutional links through public funding acknowledgements and project metadata.*  

---

## 🧭 Purpose  

To map **institution-level networks** in bilateral research or diplomatic programmes using only open, published data.  
This protocol focuses on the phrase-search method — tracking standard acknowledgements such as *“supported by the UK–Israel Science Council.”*  

---

## 🧩 1. Define the Search Strings  

Use multiple variants to capture formatting differences:  

```
"supported by the UK-Israel Science Council"  
"funded by the UK Israel Science Council"  
"UK–Israel Science Council project"  
"UK Israel Science Council support"  
```

Optional wideners:  

```
"UK-Israel Science" + "Council"  
"UK Israel" + "bilateral research"  
```

---

## 🧮 2. Target Databases (Open Access)  

| Source | URL / Access | Key Fields |
|---------|--------------|------------|
| **UKRI Gateway to Research** | [gtr.ukri.org](https://gtr.ukri.org) | project title, abstract, organisation name |
| **University Repositories** | institutional websites / Pure systems | funding acknowledgement, sponsor |
| **ResearchFish** | institutional login only | outcomes → funding acknowledgement |
| **Google Scholar / Semantic Scholar** | free text search | acknowledgements in papers |
| **Press releases / Embassy sites** | open web | event announcements, project names |

---

## 🧾 3. Procedure  

1. Run each query and collect *project-level records*.  
2. Extract and normalise:  
   - **Institution name**  
   - **Department / Centre**  
   - **Year / Funding call**  
   - **Project title**  
   - **URL or DOI**  
3. De-duplicate by institution.  
4. Aggregate counts → *number of projects per institution*.  
5. Optional: plot network diagram where nodes = institutions, edges = joint projects.  

Keep all data at the **organisational level**; avoid personal identifiers.  

---

## 🗂️ 4. Recommended CSV Schema  

| institution | department | project_title | year | funding_phrase | url | notes |
|--------------|-------------|----------------|------|----------------|-----|-------|
| Example University | Dept of Physics | Nano-Sensors for Medical Imaging | 2023 | "supported by the UK–Israel Science Council" | https://gtr.ukri.org/... |  |  

---

## 🧠 5. Analytical Checks  

- **Temporal:** do funding years cluster around particular diplomatic events?  
- **Disciplinary:** which research areas dominate?  
- **Geographical:** are collaborations spread across regions or concentrated in specific universities?  
- **Narrative:** does project language mirror policy rhetoric from embassy or council statements?  

---

## 🧭 6. Ethical Boundaries  

- Use only **published** or **officially archived** material.  
- Do **not** compile personal datasets on individual researchers.  
- Treat institutional names as public entities, not private persons.  

---

## 🌌 Constellations  

🪩 Public Faces, Hidden Files — visible figures as network anchors  
🌐 Academic Partnership Architecture — structural map of bilateral collaboration  
🧾 Filling the Transparency Gap — missing data categories in partnerships  
🕵️‍♀️ OSINT Guide — general open-source investigation methods  

---

## ✨ Stardust  

open-source investigation, bilateral research, funding acknowledgement, academic networks, transparency, UKRI, metadata analysis, ethical OSINT  

---

## 🏮 Footer  

*Search Protocol — Bilateral Funding Phrase Mapping* provides a replicable, low-risk method for uncovering institutional connections in international research ecosystems using nothing but publicly available metadata.  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-05-21_
