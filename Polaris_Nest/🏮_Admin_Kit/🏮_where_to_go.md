# 🏮 Where to Go  
**First created:** 2025-09-12 | **Last updated:** 2025-09-28  
*Decision tree for filing new nodes into the Polaris Protocol repository*  

---

## 🌱 Scope  

This document is the **filing compass** for Polaris.  
Whenever a new file arrives, follow the flowchart below to decide its correct home.  
Each branch points to an exact folder and subfolder, with scope notes built in.  

**Routing note for banned/muted media:** narrative or case-study nodes go to **🎶 Banned_Broadcasts_Cooperative**; datasets/CSVs/scripts route to **🎶 Banned_Broadcasts_Cooperative/data/**.

---

## 🗺 Filing Flowchart  

```mermaid
flowchart TD
  A[📂 New file arrives] --> B{Repo-level meta or style?}
  B -->|Yes| B1[Polaris_Nest / 🏮 Admin_Kit — House Style, Branding Guide]
  B -->|No| C{Defines systemic rules / protocol structure?}

  %% Big Picture Protocols narrowed routing (REFRESHED)
  C -->|Yes| Cpick{Which systemic axis?}
  C -->|No| D{Practical survivor tool / countermeasure?}

  Cpick -->|Governance logics, authorisation chains| C1[🌀 System_Governance]
  Cpick -->|Human dignity, ethics frames| C1b[🌱 Human_Principles]
  Cpick -->|University compliance & discipline| C1c[🎓 British_University_Compliance_Service]
  Cpick -->|Media / broadcast bans & circulation| C7[🎶 Banned_Broadcasts_Cooperative]
  Cpick -->|Trauma, psychology & medical misuse| C2[🐦‍🔥 Trauma_Psychology_Medical_Misuse]
  Cpick -->|Forensic witness histories reshaped / suppressed| C3[👁️‍🗨️ Witness_Historical_Casefiles]
  Cpick -->|Memory, narrative suppression, politicised identity| C4[🗝️ Politics_Memory_Work]
  Cpick -->|UK gov nudge units & coercive applications| C5[🧠 HM_Dept_Coercive_Nudges]
  Cpick -->|Radicalisation, Prevent & platform dynamics| C6[🪬 Radicalisation_Extremism]
  Cpick -->|Laws & statutory architectures| C8[📜 Statutes]
  Cpick -->|Money, donors, media capture| C9[📺 Money_Talks_Media]
  Cpick -->|Safeguarding industry shadows| C10[🕯 Exorcising_Safeguarding_Shadows]
  Cpick -->|Global entanglements & diasporas| C11[🕸️ World_Webs]
  Cpick -->|Borders, asylum & maritime control| C12[🛟 Borders_Boats_Walls]
  Cpick -->|Oversight of oversight| C13[🧿 Watch_The_Watchers]

  %% BBC split for datasets vs narrative nodes
  C7 --> C7pick{Dataset / structured analysis?}
  C7pick -->|Yes| C7a[🎶 BBC → data/]
  C7pick -->|No| C7b[🎶 BBC main cluster]

  %% Survivor Tools
  D -->|Yes| D1[Disruption_Kit → Survivor_Tools]
  D -->|No| E{Forensic evidence, dated log, or anomaly?}

  %% Logs vs Weirdness vs Evidence
  E -->|Dated tactical field log| E1[Disruption_Kit → Field_Logs]
  E -->|Weirdness triage of system behaviour| E2[👾 Weirdness_Screening]
  E -->|Evidence sets / screenshots / constellations| E3[Metadata_Sabotage_Network → Evidence_And_Anomalies]

  %% Weirdness Screening subfolders
  E2 --> E2a[🖥 Interface_Glitches — device oddities]
  E2 --> E2b[📬 Comms_Breaks — lost referrals, attachments]
  E2 --> E2c[🌐 Connection_Hiccups — Wi-Fi drops, call cuts]
  E2 --> E2d[📂 Data_Shifts — missing records, mismatched timestamps]
  E2 --> E2e[🔑 Access_Barriers — login failures, MFA loops]
  E2 --> E2f[🎛 Systematic_Patterns — scheduled/synced glitches]
  E2 --> E2g[🚉 Infrastructure_Hiccups — trains, ATMs, payments]
  E2 --> E2h[🛒 Service_Blockages — consumer-facing anomalies]

  %% Metadata Evidence subfolders
  E3 --> E3a[✨ Constellations — visual anomalies, screenshots]
  E3 --> E3b[👾 Breakpoints_And_Glitches — transport failures, logs]

  %% Suppression Layers
  E3 --> F{Suppression / visibility manipulation?}
  F -->|Yes| Fpick{Which suppression layer?}
  F -->|No| G{Case testimony or personal record?}

  Fpick -->|Commit & comment failures, UI sabotage| F1[📉 Suppression_Interference_Logs]
  Fpick -->|Search erosion, indexing failures| F2[🔮 Visibility_Indexing_Anomalies]
  Fpick -->|Platform throttling & ranking behaviours| F3[🪅 Platform_Sabotage]
  Fpick -->|Field signal & proximity interference| F4[🛰️ Proximity_Control_Logs]

  %% Casefiles
  G -->|Yes| G1[Polaris_Nest → SCP-VoiceX_Casefiles]
  G -->|No| H{Structural mapping or metadata logic?}

  %% Metadata Structural Analysis
  H -->|Yes| Hpick{Which structural analysis?}
  H -->|No| I{Narrative / psych ops?}

  Hpick -->|Rupture logs, schema maps, pathways| H1[🧬 Structural_Mapping]
  Hpick -->|Leaks & unintended reveals| H2[🧼 System_Leakage_Signatures]
  Hpick -->|Targeting heuristics & rulesets| H3[🧿 Targeting_Logic_Metadata_Signatures]

  %% Metadata Narrative / Psych Ops
  I -->|Yes| Ipick{Which narrative/psych-ops vector?}
  I -->|No| Gc{Governance / containment rulesets?}

  Ipick -->|Semantic drift, clone tone| I1[🪆 Narrative_Interference]
  Ipick -->|Waiting, observers, compliance by delay| I2[🧠 Psychological_Containment]
  Ipick -->|Voice smears, sexualisation, discrediting| I3[👅 Voice_Disruption_Discrediting]
  Ipick -->|Harassment mis-ID, mimic theatre| I4[👹 Fork_Behaviour_Containment]

  %% Metadata Governance / Containment
  Gc -->|Yes| GcPick{Which governance axis?}
  Gc -->|No| J{Correspondence or reflective writing?}

  GcPick -->|Contracts, NDA dragnets| Gc1[㊙ Containment_Contracts]
  GcPick -->|Escalation triggers, thresholds| Gc2[🉑 System_Thresholds]
  GcPick -->|Training data harms, dispatch logs| Gc3[🈸 Dispatch_And_Training]
  GcPick -->|Prevent logic, governance suppression| Gc4[🈺 Governance_And_Prevent]
  GcPick -->|Alliances, ethics, authorship| Gc5[🈴 Allies_And_Ethics]

  %% Letters
  J -->|Yes| J1[Polaris_Nest → ✨ Letters_to_Stars]
  J -->|No| K{Apparitional Objects family?}

  %% Apparitional Objects hub
  K -->|Ghostly presences / phantoms / echoes| K1[👻 Apparitional_Objects → 👻 Ghosts]
  K -->|Forks, doubles, execution drift| K2[👻 Apparitional_Objects → 🍴 Forks]
  K -->|Haunted artifacts, cursed records, traces| K3[👻 Apparitional_Objects → 📿 Artifacts]
  K -->|Skeleton frameworks, haunted scaffolds| K4[👻 Apparitional_Objects → 🦴 Skeletons]
  K -->|None| L{Utility glossary or external reference?}

  L -->|Yes| L1[Disruption_Kit → 💎 Resources]
  L -->|No| M{Syntax bombs or tags?}

  M -->|Yes| M1[Disruption_Kit → 💣 Syntax_Bombs / 🔖 Tag_Pack]
  M -->|No| N[Default closest thematic folder per index]

  %% Final housekeeping
  B1 --> X[📑 Update index.md with emoji link + one-line scope]
  C1 --> X
  C1b --> X
  C1c --> X
  C2 --> X
  C3 --> X
  C4 --> X
  C5 --> X
  C6 --> X
  C7 --> X
  C7a --> X
  C7b --> X
  C8 --> X
  C9 --> X
  C10 --> X
  C11 --> X
  C12 --> X
  C13 --> X
  D1 --> X
  E1 --> X
  E2 --> X
  E3 --> X
  E3a --> X
  E3b --> X
  F1 --> X
  F2 --> X
  F3 --> X
  F4 --> X
  G1 --> X
  H1 --> X
  H2 --> X
  H3 --> X
  I1 --> X
  I2 --> X
  I3 --> X
  I4 --> X
  Gc1 --> X
  Gc2 --> X
  Gc3 --> X
  Gc4 --> X
  Gc5 --> X
  J1 --> X
  K1 --> X
  K2 --> X
  K3 --> X
  K4 --> X
  L1 --> X
  M1 --> X
  N --> X

  X[✅ Ensure filename follows House Style + 🏮 Footer block]
