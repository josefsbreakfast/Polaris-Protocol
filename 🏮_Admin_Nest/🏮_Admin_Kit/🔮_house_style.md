# 🔮 House Style  
**Version:** 1.8  
**First created:** 2025-08-08 | **Last updated:** 2026-05-25  
*Standard Formatting & Style Guide for Polaris Protocol*  

---

## 1. **File Naming Conventions**  

All filenames must follow the pattern:

```text
EMOJI_snake_case.md
```

### Rules  
- Begin with an **emoji prefix** for category.  
- Use a short descriptive title in **snake_case**.  
- Use lowercase only.  
- End with the `.md` extension.  

### Restrictions  
- No spaces.  
- No extra punctuation other than underscores.  
- No random capitals.  
- No decorative symbols beyond the emoji prefix.  

### Dates  
Do not include dates in filenames unless:

- the file is a Field Log tied to a specific date, or  
- the filename itself denotes a dated evidence sequence.

### Examples  

```text
🧬_cloneproof.md
🛰️_metadata_ghosts_2025-08-12.md
⚖️_containment_contract_trace.md
```

---

## 2. **Folder Structure**  

### Core Routing Logic  

- **Big_Picture_Protocols/**  
  Structural / systemic analysis, diagnostics, governance theory, pattern mapping.

- **Survivor_Tools/**  
  Practical guidance, countermeasures, navigation aids, resilience tooling.

- **Field_Logs/**  
  Dated evidence logs, forensic documentation, screenshots, CSVs, plots.

- **Containment_Scripts/**  
  Platform suppression patterns, visibility manipulation methods, behavioural governance.

- **SCP-VoiceX_Casefiles/**  
  Personal testimony, filings, chronology, archive material.

- **Admin_Kit/**  
  House style, templates, trackers, routing logic, scaffolding infrastructure.

---

## 3. **Document Structure**  

Polaris nodes are modular documents.  
Files are expected to use multiple H2 sections to organise material clearly.

---

### Title Block  

Each file begins with:

- an H1 title,
- metadata,
- and a one-line italic summary.

### Rules  

- H1 must contain:
  - emoji prefix,
  - title in Sentence Case.

- Metadata line format:

```markdown
**First created:** YYYY-MM-DD | **Last updated:** YYYY-MM-DD
```

- Follow with:
  - a single italic one-line scope summary.

### Example  

```markdown
# 🧬 Cloneproof  
**First created:** 2025-07-14 | **Last updated:** 2025-08-12  
*Practical countermeasures for voice and behavioural cloning*
```

---

### Body Structure  

After the title block, nodes may contain as many H2 sections as required.

Multiple H2 sections are standard Polaris formatting.

### Common H2 Patterns  

```markdown
## 🛰️ Orientation
## ✨ Key Features
## 🧿 Analysis
## ⚖️ Failure Modes
## 🛠️ Diagnostic Tools
## 📚 Case Studies
## 🌌 Constellations
## ✨ Stardust
## 🏮 Footer
```

### Heading Hierarchy Rules  

- H1 is reserved for the document title only.  
- Main sections use H2 (`##`).  
- Subsections use H3 (`###`).  
- Avoid excessive nesting depth.  
- Break large text walls into readable sections.

### Structural Expectations  

Most nodes will contain:

- orientation or framing,
- one or more analytical sections,
- optional tools/examples/case sections,
- a Constellations block,
- a Stardust block,
- and a Footer block.

Exact section names may vary by node type.

---

## 4. **Cross-Linking**  

### Link Rules  

- Use relative paths only.  
- Never use absolute GitHub URLs.  
- Never leave raw filenames floating in body prose without context.

### Link Style  

Cross-links should describe:
- purpose,
- relationship,
- or function.

Not merely filename repetition.

### Example  

```markdown
See [📩 Ghost vs Haunting Chart](../Disruption_Kit/Big_Picture_Protocols/📩_ghost_vs_haunting_chart_2025-08-12.csv)
```

---

## 5. **Versioning & Updates**  

### Metadata Requirements  

Every file must contain:

- `First created`
- `Last updated`

### Version Rules  

- Increment House Style version when rules materially change.  
- Sync dates across linked infrastructure nodes where appropriate.  
- Major revisions should be reflected in changelog or governance notes if applicable.

---

## 6. **Constellations Block**  

Every file includes a **Constellations** section before the Footer.

### Purpose  

The Constellations block:

- maps the node into the wider Polaris semantic ecosystem,
- acts as conceptual routing infrastructure,
- and visually situates the node within thematic clusters.

Optional media references may appear here.

---

### Required Structure  

```markdown
## 🌌 Constellations
```

### Format  

- 2–5 emojis from the Visual Palette.  
- One short explanatory line.

### Example  

```markdown
## 🌌 Constellations  
🪞 ✂️ 🧩 🧠 🧿 — diagnostic register; narrative fracture mapping; containment visibility analysis.
```

---

## 7. **Stardust Block**  

Every file includes a Stardust block immediately before the Footer.

### Purpose  

The Stardust block functions as:

- keyword indexing,
- semantic tagging,
- search support,
- and navigation infrastructure.

---

### Required Structure  

```markdown
## ✨ Stardust
```

### Format Rules  

- Plain lowercase words or short phrases.  
- No emojis.  
- Comma-separated only.  
- Usually 5–10 entries.  
- Ordered from broad thematic → specific technical.

### Example  

```markdown
## ✨ Stardust  
containment, narrative governance, visibility management, british systems culture, institutional pacing
```

---

## 8. **Footer Block**  

Every Polaris node must end with a dedicated Footer section.

The Footer is structurally mandatory — not decorative.

It functions as:

- archive routing infrastructure,
- contextual framing,
- cross-cluster navigation,
- and sovereignty anchoring.

---

### Required Footer Structure  

```markdown
---

## 🏮 Footer  

*Node Title* is a living node of the **Polaris Protocol**.  
1–3 sentences situating the node’s purpose, function, or analytical role.  
Written in documentary or archival voice.  

> 📡 Cross-references:
>
> - [Related Node or Folder](../path/) — *short functional description*  
> - [Related Node or Folder](../path/) — *short functional description*  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: YYYY-MM-DD_
```

---

### Footer Rules  

- Footer must always be the final section in the file.  
- Footer heading must always use H2 format:
  - `## 🏮 Footer`
- Footer must contain at least one cross-reference block.  
- Cross-references should explain function — not merely repeat filenames.  
- The sovereignty line should remain unchanged unless a project explicitly defines an alternative.  
- `_Last updated:_` line must appear at the absolute end of the file.

### Footer Tone  

Footer language should:

- sound archival or documentary rather than promotional,
- situate the node within the wider Polaris ecosystem,
- clarify why the node exists,
- and reinforce continuity between clusters.

---

## 9. **Voice & Tone Fidelity**  

Polaris writing preserves survivor voice fidelity by default.

### Core Principles  

- Do not over-neutralise tone unless explicitly requested.  
- Documentary voice may coexist with irony, grief, humour, or sharpness.  
- Precision matters more than false institutional blandness.  
- Nodes should remain readable without flattening emotional reality.

### Drafting Expectations  

Writing should aim for:

- structural clarity,
- semantic precision,
- readable modularity,
- and recognisable Polaris undertone.

See:

```text
🎛️_polaris_drafting_rules_survivor_voice_fidelity.md
```

for extended drafting guidance.

---

## 10. **Protocol Integrity Expectations**  

All major uploads, edits, and routing passes should undergo integrity review.

### Minimum Checks  

- Filename compliance  
- Metadata correctness  
- Heading hierarchy consistency  
- Footer presence  
- Cross-link validity  
- Constellations presence  
- Stardust presence  
- Sovereignty line preservation

### Governance Reminder  

Structural consistency is not cosmetic.

Formatting coherence is part of:
- archive survivability,
- routing clarity,
- and long-term protocol integrity.

---

## 🏮 Footer  

*🔮 House Style* is a living node of the **Polaris Protocol**.  
It defines the structural, stylistic, and routing conventions used across the Polaris archive ecosystem.  
This document functions as the canonical formatting and organisational reference for maintaining interoperability between nodes, clusters, and governance layers.

> 📡 Cross-references:
>
> - [🎛️ Polaris Drafting Rules — Survivor Voice Fidelity](./🎛️_polaris_drafting_rules_survivor_voice_fidelity.md) — *tone, undertone, and drafting fidelity rules*  
> - [☔️ Protocol Integrity SOP](./☔️_protocol_integrity_sop.md) — *consistency and governance checking procedures*  
> - [🐝 Template Node](./🐝_template_node.md) — *base structural template for new nodes*
>  
> 🏮 Return To:  
>
> - [🏮 Admin Kit](./) - *1up*  
> - [🏮 Admin Nest](../README.md) - *2up*  
> - [🌌 Polaris Protocol - Root](../../README.md) - *root*  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-05-25_
