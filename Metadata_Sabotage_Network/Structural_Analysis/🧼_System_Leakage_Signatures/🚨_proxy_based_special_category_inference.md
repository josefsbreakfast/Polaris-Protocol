# 🚨 Proxy-Based Special Category Inference  
**First created:** 2025-12-14 | **Last updated:** 2025-12-14  
*When indirect behavioural signals are used to infer protected or sensitive attributes without consent*

---

## What this node is about

Proxy-based special category inference occurs when systems infer **protected or sensitive attributes** about a person using indirect signals rather than explicit data.

These inferences are often framed as:
- probabilistic  
- non-identifying  
- “just metadata”  
- or merely contextual  

In reality, they constitute **regulated data processing** under most modern data-protection frameworks.

This node documents how proxy inference crosses a legal and ethical boundary — even when the inference is inaccurate.

---

## What counts as special category data

Under GDPR, UK GDPR, and aligned regimes, special category data includes inferences relating to:

- health or mental health  
- sexual life or orientation  
- political opinions  
- religious or philosophical beliefs  
- trade union membership  
- racial or ethnic origin  
- biometric or genetic traits  
- intimate relationships or relational status  

Crucially:

> **Inference counts as processing.  
Accuracy is irrelevant to classification.**

If a system attempts to infer these attributes — even incorrectly — it is processing special category data.

---

## How proxies are used to infer sensitive attributes

Systems frequently infer sensitive attributes using proxies such as:

- time-of-day activity → mental health or distress  
- content themes → political or religious beliefs  
- language style → emotional or psychological state  
- interaction patterns → relational or sexual interest  
- network proximity → ideological alignment  
- persistence or intensity → fixation or dependency  

These proxies are attractive because:
- they are readily available  
- they avoid collecting explicit disclosures  
- they appear “safer” than direct data  

They are not safer.
They are **less transparent**.

---

## Why proxy inference is treated as acceptable (incorrectly)

Organisations often justify proxy inference by claiming:

- the data is anonymised  
- the inference is probabilistic  
- no explicit labels are stored  
- the system does not “know for sure”  
- outputs are not user-facing  

None of these arguments remove regulatory obligation.

The relevant test is not certainty.
It is **purpose and effect**.

---

## The core failure

The core failure can be summarised as:

> **Avoiding explicit collection does not avoid responsibility.**

Proxy inference is often used to:
- sidestep consent requirements  
- avoid triggering internal review  
- preserve modelling flexibility  
- claim plausible deniability  

This does not change the nature of the processing.

It only obscures it.

---

## Interaction with behavioural modelling failures

Proxy-based special category inference rarely occurs in isolation.

It is amplified by:

- behavioural proxy misinterpretation  
- sparse clustering  
- embedding inertia  
- R&D artefact leakage  
- dogfooding bias  

When these failures combine, systems may:
- infer sensitive traits from very little data  
- generalise cluster-level attributes to individuals  
- persist inferences long after conditions change  

This creates a **durable shadow profile** that users cannot see or contest.

---

## Why inaccuracy does not mitigate harm

A common misconception is that incorrect inference is harmless.

In fact, inaccurate proxy inference can be worse because it:

- cannot be corrected through disclosure  
- cannot be disproven by the user  
- still shapes system behaviour  
- still influences moderation, steering, or reputation  
- still creates chilling effects  

From a rights perspective, **being wrongly inferred is still being processed**.

---

## When proxy inference becomes unlawful

Proxy-based special category inference is unlawful when:

- there is no explicit, informed consent  
- no clear statutory exemption applies  
- inference exceeds original purpose  
- safeguards are absent or inadequate  
- users are not informed  
- inference affects individuals materially  

In most consumer and platform contexts, these conditions are not met.

The result is silent non-compliance.

---

## Why this is difficult to detect or audit

Proxy inference is difficult to detect because:

- inferences are embedded, not labelled  
- attributes are represented as weights or vectors  
- no single field contains the sensitive category  
- documentation avoids explicit naming  
- systems treat inference as “feature engineering”  

This allows organisations to sincerely claim ignorance while continuing the practice.

---

## Impact on individuals

For individuals, proxy-based special category inference can result in:

- intrusive personalisation  
- inappropriate content or intervention  
- reputational distortion  
- safety misclassification  
- emotional harm  
- loss of trust  
- inability to contest or correct  

The harm occurs **even if no one ever “looks at” the inference**.

---

## What lawful handling requires

Lawful handling of special category inference requires:

- explicit, informed, freely given consent  
- clear articulation of inference purpose  
- strict necessity and proportionality  
- enhanced safeguards  
- transparency to the data subject  
- meaningful opt-out and redress  

Absent these conditions, the inference should not occur.

---

## Key takeaway

> **You cannot infer your way around consent.**

When systems use proxies to guess protected attributes, they are not avoiding regulation — they are violating it quietly.

---

## 🌌 Constellations  
🚨 🧠 🧪 🐶 👻 — sensitive inference · proxy misuse · governance breach · hidden processing

---

## ✨ Stardust  
special category data, proxy inference, sensitive attributes, behavioural profiling, GDPR Article 9, inferred traits, rights violation

---

## 🏮 Footer  

*Proxy-Based Special Category Inference* is a living node of the **Polaris Protocol**, documenting how behavioural systems infer protected attributes through indirect signals and why this practice constitutes regulated data processing regardless of intent or accuracy.

This node frames proxy inference as a **rights issue**, not a modelling shortcut.

> 📡 Cross-references:
> 
> - **🧠 Behavioural Proxy Misinterpretation** — how weak signals gain meaning  
> - **🧪 R&D Artefact Leakage into Production** — how experimental inference escapes governance  
> - **🐶 Internal Dogfooding as a Risk Vector** — how internal norms shape sensitive inference  
> - **⚖️ Consent and Purpose Limitation Failure in ML R&D** — the legal boundary this crosses  

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2025-12-14_
