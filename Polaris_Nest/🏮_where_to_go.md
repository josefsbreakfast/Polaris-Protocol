flowchart TD
    A[📂 New file arrives] --> B{Repo level meta or style?}
    B -->|Yes| B1[Place in Admin_Kit e.g. House Style or Branding Usage Guide]
    B -->|No| C{Defines systemic rules or protocol structure?}

    C -->|Yes| C1[Place in Disruption_Kit → Big_Picture_Protocols (use correct subfolder e.g. 🌀 System Governance)]
    C -->|No| D{Practical survivor tool or countermeasure?}

    D -->|Yes| D1[Place in Disruption_Kit → Survivor_Tools]
    D -->|No| E{Forensic evidence / logs / anomaly?}

    %% NEW: split forensic vs triage vs evidence buckets
    E -->|Tactical daily/dated field log| E1[Place in Disruption_Kit → Field_Logs]
    E -->|Weirdness / triage of system behaviour| E2[Place in 🩻 Weirdness_Screening (choose subfolder)]
    E -->|Evidence set / screenshots / constellation| E3[Place in Metadata_Sabotage_Network → 🔎 Evidence_And_Anomalies]

    %% NEW: Weirdness_Screening sub-chooser
    E2 --> E2a[🌐 Connection_Hiccups]
    E2 --> E2b[🎛 Systematic_Patterns]
    E2 --> E2c[📂 Data_Shifts]
    E2 --> E2d[📬 Comms_Breaks]
    E2 --> E2e[🔑 Access_Barriers]
    E2 --> E2f[🖥 Interface_Glitches]
    E2 --> E2g[🚉 Infrastructure_Hiccups]

    E3 --> F{Suppression or visibility manipulation method?}

    F -->|Yes| F1[Place in Disruption_Kit → Containment_Scripts]
    F -->|No| G{Case testimony or personal record?}

    G -->|Yes| G1[Place in Polaris_Nest → SCP-VoiceX_Casefiles]
    G -->|No| H{Structural mapping or metadata logic analysis?}

    H -->|Yes| H1[Place in Metadata_Sabotage_Network → Structural_Analysis]
    H -->|No| I{Narrative or psych ops material?}

    I -->|Yes| I1[Place in Metadata_Sabotage_Network → Narrative_And_Psych_Ops]
    I -->|No| J{Correspondence or reflective writing?}

    J -->|Yes| J1[Place in Polaris_Nest → ✨ Letters_to_Stars]
    J -->|No| K{Apparitional Object family?}

    %% NEW: Apparitional Objects hub
    K -->|Forks / clones / execution drift| K1[👻 Apparitional_Objects → Fork_Taxonomy]
    K -->|Haunted artefacts / exhibits| K2[👻 Apparitional_Objects → 🎞️ Haunted_Artefacts_Catalogue]
    K -->|Ghosty vignettes / fragments| K3[👻 Apparitional_Objects → 👻 Glitchy_Ghosties]
    K -->|Concept shards / notes| K4[👻 Apparitional_Objects → 🦴 Skeletal_Shards]
    K -->|None| L{Utility glossary or external reference?}

    L -->|Yes| L1[Place in Disruption_Kit → 💎 Resources]
    L -->|No| M{Tactical writing device like syntax bombs or tags?}

    M -->|Yes| M1[Place in Disruption_Kit → 💣 Syntax_Bombs or 🔖 Tag_Pack]
    M -->|No| N[Default: closest thematic folder per index]

    %% Final step (unchanged)
    B1 --> X[📑 Update index.md with link emoji + one-line scope]
    C1 --> X
    D1 --> X
    E1 --> X
    E2 --> X
    E3 --> X
    F1 --> X
    G1 --> X
    H1 --> X
    I1 --> X
    J1 --> X
    K1 --> X
    K2 --> X
    K3 --> X
    K4 --> X
    L1 --> X
    M1 --> X
    N --> X

    X[Ensure filename follows House Style + includes required Footer block]
