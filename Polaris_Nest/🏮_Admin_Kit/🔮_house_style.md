# 🔮 House Style  
**Version:** 1.7  
**First created:** 2025-08-08 | **Last updated:** 2025-11-09  
*Standard Formatting & Style Guide for Polaris Protocol*  

---

## 1. **File Naming Conventions**  
- All filenames must follow the pattern: **EMOJI_snake_case.md**  
  - Begin with an **emoji prefix** for category.  
  - Then use a short descriptive title in **snake_case** (all lowercase with underscores).  
  - Always end with the `.md` extension.  

- **No spaces**.  
- **No extra punctuation** other than underscores.  
- **No dates** in filenames unless:  
  - The file is a Field Log tied to a specific day (`🛰️_metadata_ghosts_2025-08-12.md`).  
  - Or the filename itself denotes a sequence of dated evidence.  

**Examples:**  
- `Survivor_Tools/🧬_cloneproof.md`  
- `Field_Logs/🛰️_icc_tag_thread_containment.md`  
- `Big_Picture_Protocols/⚖️_containment_contract_trace.md`  

---

## 2. **Folder Structure**  
- **Big_Picture_Protocols/** → Structural / systemic analysis (diagnostics, typologies, inversion theory).  
- **Survivor_Tools/** → Practical strategies, survivor-led guides, countermeasures.  
- **Field_Logs/** → Dated forensic documentation, evidence files, CSVs, plots.  
- **Containment_Scripts/** → Platform suppression and visibility manipulation methods.  
- **SCP-VoiceX Casefiles/** → Personal case records, testimony, legal filings.  
- **Admin_Kit/** → Planning notes, trackers, house style docs, operational scaffolding.  

---

## 3. **Document Structure**  

### Title Block  
- **H1 title**: Emoji prefix + **Capitalised Title in Sentence Case**.  
- Metadata line beneath:  
  - **First created:** `YYYY-MM-DD` | **Last updated:** `YYYY-MM-DD`  
  - *Italic one-line summary of scope*  

**Example:**  

```markdown
# 🧬 Cloneproof  
**First created:** 2025-07-14 | **Last updated:** 2025-08-12  
*Practical countermeasures for voice and behavioural cloning*
```

---

## 4. **Cross-Linking**  

Use relative paths only (never absolute GitHub URLs).  

Always wrap with a clear description (not raw filename).  

**Example (display only):**  

```markdown
See [📩 Ghost vs Haunting Chart (2025-08-12)](../Disruption_Kit/Big_Picture_Protocols/📩_ghost_vs_haunting_chart_2025-08-12.csv)
```

---

## 5. **Versioning & Updates**  

Each file shows creation + last update date.  

Increment House Style version when rules are added or changed.  

Version history tracked at top of this file.  

---

## 6. **Constellations Block**  

Every file includes a **Constellations** section *before the Footer*.  

**Purpose:**  
- To map each node into the wider Polaris constellation.  
- Works like a “semantic compass” for where the file belongs in the visual + conceptual palette.
- Optionally: this may include media references which relate to the node, at writer's discretion.  

**Format:**  
- **H2 heading**: `## 🌌 Constellations`  
- 2–5 emoji drawn from the [Visual Palette](../Admin_Kit/_visual_palette.md.txt)  
- A short line explaining why those constellations apply.  

**Example:**  

```markdown
## 🌌 Constellations  
🪞 ✂️ 🧩 🧠 🧿 — short 1-line semantic tag defining node’s function (e.g., diagnostic register; civic reconstruction register; forensic ledger).  
```

---

## 7. **Stardust Block**  

Every file includes a **Stardust** section *just before the Footer*.  

**Purpose:**  
- SEO + tags for navigation and indexing.  
- Plain word/phrase list (no emojis).  

**Format:**  
- **H2 heading**: `## ✨ Stardust`  
- 5–10 keywords or short phrases separated by commas.  

**Example:**  

```markdown
## ✨ Stardust  
comma-separated conceptual and keyword list — always lowercase, no caps; ordered from thematic to specific.  

```

 ---

## 8. **Footer Block**  

Every file ends with a **🏮 Footer** section.  

**Required elements:**  
- **H2 heading**: `## 🏮 Footer`  
- A short paragraph situating the file as a *living node of the Polaris Protocol* (purpose + scope).  
- One or more **📡 cross-references** to related directories or nodes (using relative paths).  
- **Closing sovereignty line**:  
  *Survivor authorship is sovereign. Containment is never neutral.*  
- Final `_Last updated: YYYY-MM-DD_` line.  

**Example:**  

```markdown
---

## 🏮 Footer  

*Node Title* is a living node of the **Polaris Protocol**.  
1-2 sentences stating its purpose, phrased in documentary voice.  

> 📡 Cross-references:
> 
> - [Node or Folder 1](../path/) — *one-line function descriptor*  
> - [Node or Folder 2](../path/) — *one-line function descriptor*  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: YYYY-MM-DD_

```

