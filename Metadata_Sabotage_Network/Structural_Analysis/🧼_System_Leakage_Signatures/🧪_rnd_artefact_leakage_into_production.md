# 🧪 R&D Artefact Leakage into Production  
**First created:** 2025-12-14 | **Last updated:** 2025-12-14  
*How experimental models, datasets, and assumptions escape research contexts and shape live systems*

---

## What this node is about

R&D artefact leakage describes a systemic failure mode in which **experimental models, datasets, embeddings, or assumptions developed for research purposes are reused — intentionally or accidentally — in production systems** without adequate revalidation, governance, or consent review.

This is not a rare oversight.
It is a structural outcome of how modern ML systems are built, iterated, and shipped.

The result is that **exploratory artefacts gain real-world power**, often long after their original context has been forgotten.

---

## What counts as an R&D artefact

R&D artefacts include, but are not limited to:

- prototype models  
- pilot embeddings  
- experimental clustering geometry  
- internal evaluation datasets  
- proof-of-concept pipelines  
- feature engineering assumptions  
- heuristic labels used “temporarily”  
- synthetic or semi-synthetic data  
- early-stage safety or risk classifiers  

These artefacts are legitimate *inside* R&D.
They become problematic when treated as production-grade.

---

## How leakage happens

R&D artefact leakage usually occurs through ordinary workflows:

- a prototype model “works well enough” and is reused  
- an embedding space becomes a dependency for another service  
- a research classifier is wrapped by a product feature  
- a pilot dataset is reused to bootstrap training  
- a temporary heuristic becomes permanent by inertia  
- documentation is lost as teams change  
- ownership of the artefact becomes unclear  

No malice is required.
Only momentum.

---

## Why R&D artefacts are especially risky

R&D artefacts differ from production assets in critical ways.

They are often:

- trained on small or biased samples  
- overfitted to niche behaviours  
- optimised for insight, not fairness  
- unconcerned with consent scope  
- loosely documented  
- weakly audited  
- intentionally sensitive to edge cases  

When these artefacts leak into production, their **exploratory sensitivity is mistaken for reliability**.

---

## Interaction with sparse clusters and ghost geometry

R&D artefact leakage is a primary source of:

- micro-clusters  
- frozen centroids  
- exaggerated similarity  
- legacy embedding spaces  

If an R&D dataset contained:
- only a handful of users  
- a narrow behavioural slice  
- internal staff or testers  

…the resulting geometry may encode clusters of size 1–3.

When that geometry persists downstream, it creates the illusion of meaningful grouping where none exists.

---

## Why this leakage often goes unnoticed

Organisations rarely notice R&D artefact leakage because:

- the system appears to function  
- metrics do not immediately degrade  
- artefacts are abstracted behind APIs  
- no one remembers the original context  
- responsibility is diffuse  
- users cannot see the source of inference  

From the outside, the behaviour looks intentional.
From the inside, it looks like legacy code.

---

## Interaction with consent and purpose limitation

A critical governance failure occurs when:

- data collected for research is reused operationally  
- experimental inference becomes user-facing  
- consent boundaries are exceeded silently  
- special category inference is inherited by downstream systems  

Even if the original R&D use was lawful or internal,
**reuse without renewed legal basis is not**.

R&D artefact leakage often bypasses consent review entirely because the artefact is treated as “technical,” not as data processing.

---

## Why “it was just a prototype” is not a defence

Once an artefact influences:

- user experience  
- classification  
- moderation  
- reputation  
- risk assessment  
- behavioural steering  

…it is no longer a prototype.

Intent does not determine impact.
Deployment does.

Treating research artefacts as harmless because they were never meant for production obscures the real issue: **they are now operating on people.**

---

## When R&D leakage becomes harmful

R&D artefact leakage becomes harmful when it:

- embeds unvalidated assumptions into live systems  
- amplifies sparse cluster effects  
- sustains outdated interpretations  
- enables proxy-based sensitive inference  
- affects individuals without transparency or recourse  

At this point, the problem is not technical debt.
It is **unauthorised inference at scale**.

---

## What proper containment requires

Preventing R&D artefact leakage requires:

- strict separation between research and production pipelines  
- explicit artefact lifecycle management  
- consent and purpose revalidation before reuse  
- sunset clauses for experimental models  
- documentation of provenance and assumptions  
- auditability of embedding origins  
- governance review before promotion to production  

Absent these controls, leakage is the default outcome.

---

## Key takeaway

> **Research artefacts are hypotheses.  
Production systems treat them as facts.**

Without deliberate containment, exploratory tools quietly become instruments of power.

---

## 🌌 Constellations  
🧪 👻 🧮 🧠 — experimental artefacts · legacy geometry · sparsity amplification · inference drift

---

## ✨ Stardust  
R&D leakage, prototype reuse, experimental models, embedding inheritance, technical debt, governance failure, artefact persistence

---

## 🏮 Footer  

*R&D Artefact Leakage into Production* is a living node of the **Polaris Protocol**, documenting how experimental ML artefacts escape their intended context and shape real-world systems without adequate validation, consent, or governance.

This node situates leakage as an **organisational failure**, not an accident — and a primary source of downstream harm in behavioural modelling.

> 📡 Cross-references:
> 
> - **👻 Embedding Inertia and Ghost Geometry** — why leaked artefacts persist  
> - **🧮 Sparse Cluster Pathology (Micro-clusters)** — how small R&D datasets distort grouping  
> - **🐶 Internal Dogfooding as a Risk Vector** — a common source of R&D artefacts  

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2025-12-14_
