# 📂 Data Shifts  
**First created:** 2025-09-16 | **Last updated:** 2026-05-19  
*Records missing, timestamps mismatched, attachments stripped.*  

---

## 🌱 Purpose  

Document **integrity anomalies** across systems — especially where data appears to move, vanish, or rewrite itself without clear cause.  
These are not only technical issues but *metadata signals* that something — or someone — has intervened in recordkeeping.  

---

## 🧩 Why These Shifts Matter  

Information systems are designed to appear neutral.  
When data changes quietly — edits with no version history, attachments disappearing, timestamps that rewrite the past — the silence itself becomes a record.  

These shifts often occur:  
- During **containment escalations**, where inconvenient evidence is quietly re-indexed or rewritten.  
- As part of **automated clean-up routines**, masking selective erasure behind routine maintenance.  
- Through **cross-system propagation**, where synced databases overwrite one another’s “truth.”  

Tracking data shifts reveals the **soft architecture of suppression**:  
not brute deletion, but version drift — *truth rewritten as metadata error.*  

### Frequency  

Such anomalies are common in environments where multiple data custodians interact (e.g., healthcare, education, legal, or NGO ecosystems).  
They are often dismissed as clerical error or sync lag, yet across survivors’ logs they form recognisable fingerprints of control — subtle, deniable, systemic.  

### Representation  

A *data shift* is not one event but a gradient:  

| Type | Signature | Likely Mechanism | Example |
|------|------------|------------------|----------|
| **Displacement** | File moved / renamed / re-linked | Path rewrite, cloud sync | A folder reference changes but file hash remains identical. |
| **Attrition** | Content or attachment stripped | API filter, upload limit, moderation script | A report exports without its images or PDFs. |
| **Timestamp Drift** | Modified / creation dates rewritten | System clock offset, forced re-save | A record’s “last updated” matches an event it should predate. |
| **Version Reversal** | Newer record replaced by older | Rollback, permission reset | A witness statement reverts to an earlier draft. |

Each case can be small — but together they show **intentional entropy**: the slow erasure of memory through procedural means.  

---

## 📝 What to Collect  

- **Source system + record IDs / URLs**  
- **Expected vs. observed data** (include small diff/table if possible)  
- **Time window** when change likely occurred  
- **Who / what last touched the record** (user, bot, API, service account)  
- **Export of raw record / version history** if available  
- **Correlated suppression event** (e.g., media takedown, access lockout)  
- **Hash / checksum comparisons** if you can produce them safely  

---

## 🗂 Planned Nodes  

| Node | Scope | Notes |
|------|-------|-------|
| `📊_version_drift_index.md` | Audit ledger | Tracks recurring timestamp or version mismatches across cases. |
| `🧮_checksum_registry.md` | Integrity proofs | Library of cryptographic hashes for evidence preservation. |
| `🪞_phantom_versions_casebook.md` | Narrative | Case studies of records reverting or “splitting” between systems. |
| `🧾_record_mirroring_experiments.md` | Countermeasure | Controlled duplication tests to confirm live overwrites. |
| `🔍_diff_visualisation_templates.md` | Data viz | Markdown + code snippets for comparing revisions. |
| `📜_chain_of_custody_audit.md` | Legal | Simple checklist to assert record continuity for investigations. |

Together, these nodes turn *Data Shifts* into both a **forensic workspace** and a **counter-erasure archive** — where disappearance itself is evidence.  

---

## 🌌 Constellations  

🩻 📂 🧮 🕯️ — This node sits within the evidentiary core of Weirdness Screening, illuminating how silence, drift, and duplication reveal systems in motion.

---

## ✨ Stardust  

data integrity, metadata drift, silent rewriting, timestamp anomalies, evidence preservation, record loss, forensic verification, suppression infrastructure  

---

## 🏮 Footer  

*📂 Data Shifts* is a living node of the Polaris Protocol.  
It captures manipulation, corruption, and quiet rewriting of records — turning each “missing file” into a traceable event within suppression ecosystems.  

> 📡 Cross-references:  
> - [👾 Weirdness Screening](../) — triage of system behaviour  
> - [🎛 Systematic Patterns](../🎛_Systematic_Patterns/) — scheduled or repeating anomalies  
> - [🧬 Structural Mapping](../../../Metadata_Sabotage_Network/Structural_Analysis/🧬_Structural_Mapping/) — schema and pathway tracking  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-05-19_
