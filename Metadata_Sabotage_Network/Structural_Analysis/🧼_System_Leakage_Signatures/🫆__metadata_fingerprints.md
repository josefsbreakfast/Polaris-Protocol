# 🫆 Metadata Fingerprints — Hidden Fields and Author Traces
**First created:** 2025-10-10 | **Last updated:** 2025-10-16  
*Forensic signatures buried inside digital residue.*

---

## 🧭 Orientation  

Every digital object carries a ghost of its creation.  
Even when text, image, or code is sanitised, residual metadata — timestamps, EXIF coordinates, UUIDs, revision histories, author fields — remains as a forensic signature.  
These hidden traces reveal the invisible architectures behind documents, exposing lineage, authorship, and the routes of containment.  
This node treats metadata as institutional DNA: an evidentiary trail linking artefacts to origin systems.

---

## 📑 Key Sections  

### 1. File-Format Forensics  
Different formats preserve different residues:  
| Format | Common Residue | Forensic Value |
|---------|----------------|----------------|
| **JPEG / PNG** | EXIF camera ID, GPS, device serial | Location & hardware origin |
| **DOCX / ODT** | Author, editing software, revision timestamps | Authorship verification |
| **PDF** | Producer, creation date, embedded font paths | Workflow reconstruction |
| **CSV / XLSX** | Hidden sheets, cell comments, change-tracking | Data manipulation evidence |
| **ZIP / TAR** | Compression tool version, directory order | Build-pipeline attribution |

Metadata survives redaction if files are merely exported or renamed rather than scrubbed.

---

### 2. Hidden Author Fields  
Office suites and CMS platforms embed author names, user IDs, and organisational paths in file headers.  
Example:  
```
<w:author>jsmith@agency.gov.uk</w:author>
<w:lastModifiedBy>contractor.name@vendor.co.uk</w:lastModifiedBy>
```
These fields reveal subcontractor relationships, working environments, and internal usernames.  
Automated redaction tools often miss them because they reside in XML namespaces or binary header blocks.  
For auditors, they function as **containment fingerprints** — evidence of shared infrastructure even when branding differs.

---

### 3. Revision Chains and UUIDs  
Most collaborative systems (SharePoint, Google Docs, Drive, OneNote, Confluence) assign immutable **document IDs** and revision chains.  
Even if a file is duplicated or renamed, its underlying UUID may persist across exports.  
By comparing these identifiers, investigators can:  
- trace unauthorised copies,  
- connect leaks to specific environments,  
- confirm whether “independent” versions share ancestry.  

Revision diffs expose narrative evolution — a micro-history of institutional editing.

---

### 4. Ethical Scrubbing vs Erasure  
Removing metadata can protect survivors’ privacy, but full erasure also deletes provenance vital for accountability.  
The ethical stance: **scrub for safety, preserve for justice.**  

Best practice:  
- **Create two derivatives:** a redacted public copy and a preserved forensic copy.  
- **Log all scrub operations** with timestamp and hash.  
- **Never alter the original hash chain**; use containerised archiving (e.g., WORM or append-only storage).  
- **Train staff** in metadata awareness — many exposures occur through default export behaviour.

Metadata ethics sit at the intersection of care and evidence: invisibility must be a choice, not a default.

---

## 🌌 Constellations  

🫆 🧩 🧼 🧿 ⚙️ — Forensic-containment constellation; bridges *System Leakage Signatures*, *Leak Archive Protocol*, and *Contradictory Updates.*

---

## ✨ Stardust  

metadata, forensics, EXIF, revision history, author trace, digital residue, forensic transparency, document lineage, ethical scrubbing  

---

## 🏮 Footer  

*Metadata Fingerprints — Hidden Fields and Author Traces* is a living node of the Polaris Protocol.  
It converts file residue into institutional fingerprint, demonstrating how containment leaves its own trail of evidence.  

> 📡 Cross-references:  
> - [🧼 System Leakage Signatures README](./README.md) — catalogue of systemic leak indicators  
> - [🧾 Leak Archive Protocol — Secure Collection and Annotation Method](./🧾_leak_archive_protocol_secure_collection_and_annotation_method.md) — preservation workflow  
> - [🔥 Contradictory Updates — When Policy Versions Argue](../Disruption_Kit/Big_Picture_Protocols/🔥_contradictory_updates_when_policy_versions_argue.md) — textual drift comparison  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-16_
