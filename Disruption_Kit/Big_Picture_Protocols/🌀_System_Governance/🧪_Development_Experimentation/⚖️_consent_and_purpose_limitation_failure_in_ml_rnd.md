# ⚖️ Consent and Purpose Limitation Failure in ML R&D  
**First created:** 2025-12-14 | **Last updated:** 2025-12-14  
*When machine-learning research reuses personal data beyond consented scope or lawful purpose*

---

## What this node is about

Consent and purpose limitation failure occurs when personal data — or derived representations of it — is used in machine-learning research or development **outside the scope for which it was originally collected or consented**.

In ML contexts, this failure is often obscured by technical abstraction:
embeddings, features, proxies, or “models” are treated as separate from data subjects.

They are not.

This node documents how ML R&D routinely exceeds lawful boundaries without recognising that it has done so.

---

## Purpose limitation: the core legal constraint

Under GDPR and aligned frameworks, personal data must be:

- collected for **specified, explicit purposes**
- processed only in ways **compatible with those purposes**
- not repurposed without a new lawful basis

This principle applies equally to:

- raw data  
- derived features  
- embeddings  
- inferred attributes  
- behavioural summaries  

Reformatting data does not reset its legal status.

---

## Why ML R&D routinely violates purpose limitation

ML R&D environments tend to:

- treat data reuse as technically neutral  
- prioritise experimentation speed  
- collapse research and production pipelines  
- rely on “legitimate interest” without assessment  
- assume internal use is exempt  
- ignore downstream effects  

As a result, data collected for:
- service delivery  
- account operation  
- security  
- support  

is quietly reused for:
- behavioural modelling  
- clustering  
- inference testing  
- prototype training  
- feature exploration  

This is a **purpose shift**, even when intentions are benign.

---

## Consent failure in R&D contexts

Consent failure occurs when:

- individuals were not informed their data would be used for ML research  
- consent was bundled, coerced, or implicit  
- employee or tester data was repurposed  
- inference exceeded reasonable expectation  
- withdrawal mechanisms were absent or ineffective  

In many ML R&D cases, **no meaningful consent was obtained at all** — only assumed.

---

## Why “research exemption” is often misapplied

Organisations frequently invoke a vague notion of “research” to justify reuse.

This is usually incorrect.

Research exemptions typically require:
- public interest  
- ethical oversight  
- minimisation  
- anonymisation that is genuine  
- safeguards against re-identification  
- non-deployment against individuals  

Private, product-driven ML R&D rarely meets these criteria.

Calling it “research” does not make it exempt.

---

## Derived data is still personal data

A common misconception is that:

> “Once data becomes an embedding or feature, it is no longer personal.”

This is false.

If a representation:
- relates to an identifiable person  
- is linkable back to them  
- influences how they are treated  

…it remains personal data.

Derived data inherits the consent and purpose constraints of its source.

---

## Interaction with proxy-based inference

Purpose limitation failures are amplified when:

- behavioural proxies are used to infer sensitive traits  
- those inferences were never disclosed  
- consent never covered such processing  
- outputs affect users indirectly  

In these cases, the system is not only repurposing data —
it is **creating new regulated data** without lawful basis.

---

## Why these failures persist

Consent and purpose limitation failures persist because:

- governance frameworks lag ML practice  
- responsibility is diffused across teams  
- legal review is siloed  
- artefacts are framed as technical  
- users lack visibility  
- harms are indirect and delayed  

The absence of immediate failure is mistaken for compliance.

---

## When this becomes a breach

A consent and purpose limitation failure becomes a regulatory breach when:

- processing exceeds original scope  
- no alternative lawful basis applies  
- sensitive inference occurs  
- individuals are affected materially  
- transparency obligations are unmet  

In ML R&D contexts, these conditions are frequently satisfied.

---

## What lawful ML R&D requires

Lawful ML research and development requires:

- explicit articulation of research purpose  
- compatibility assessment against original purpose  
- fresh consent where required  
- genuine anonymisation or strong safeguards  
- separation of research and production data  
- documentation of lawful basis  
- respect for withdrawal and objection rights  

Absent these measures, R&D activity is not lawful experimentation — it is unauthorised processing.

---

## Key takeaway

> **ML research does not exist outside data protection law.**

If a model can affect a person, the data that shaped it remains subject to consent, purpose limitation, and accountability.

---

## 🌌 Constellations  
⚖️ 🚨 🧪 🐶 🧠 — lawful basis · purpose creep · consent failure · research misuse

---

## ✨ Stardust  
consent failure, purpose limitation, ML research governance, GDPR compliance, derived data, lawful basis, unauthorised processing

---

## 🏮 Footer  

*Consent and Purpose Limitation Failure in ML R&D* is a living node of the **Polaris Protocol**, documenting how machine-learning research frequently exceeds the lawful scope of data use and why technical abstraction does not neutralise legal obligation.

This node situates ML R&D within **data protection law**, not outside it.

> 📡 Cross-references:
> 
> - **🚨 Proxy-Based Special Category Inference** — where consent failure becomes a rights violation  
> - **🧪 R&D Artefact Leakage into Production** — how research outputs gain operational power  
> - **🐶 Internal Dogfooding as a Risk Vector** — consent complications in employee data use  
> - **🧯 Governance Gap: Explanation vs Acceptability** — why explanation does not excuse breach  

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2025-12-14_
