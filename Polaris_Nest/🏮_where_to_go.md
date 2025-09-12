```mermaid 

flowchart TD
    A[📂 New file arrives] --> B{Is it repo-level meta or style?}
    B -->|Yes| B1[Place in Admin_Kit/<br/>e.g. 🔮_house_style.md, 🪄_branding_usage_guide.md]
    B -->|No| C{Does it define systemic rules / protocol structure?}

    C -->|Yes| C1[Place in Disruption_Kit/Big_Picture_Protocols/<br/>Use correct subfolder (System_Governance, Trauma_Psycology, Politics_Memory_Work, etc.)]
    C -->|No| D{Is it a practical survivor tool or countermeasure?}

    D -->|Yes| D1[Place in Disruption_Kit/Survivor_Tools/<br/>e.g. 🧬_cloneproof_training_set_mapping.md]
    D -->|No| E{Is it forensic evidence, dated log, or anomaly?}

    E -->|Yes| E1[If tactical log → Disruption_Kit/Field_Logs/<br/>If anomaly/evidence → Metadata_Sabotage_Network/🔎_Evidence_And_Anomalies/]
    E -->|No| F{Is it a suppression or visibility manipulation method?}

    F -->|Yes| F1[Place in Disruption_Kit/Containment_Scripts/<br/>Choose Counter_Nudges or Suppression_Modes]
    F -->|No| G{Is it case testimony or personal record?}

    G -->|Yes| G1[Place in Polaris_Nest/SCP-VoiceX_Casefiles/]
    G -->|No| H{Is it structural mapping / metadata logic analysis?}

    H -->|Yes| H1[Place in Metadata_Sabotage_Network/Structural_Analysis/]
    H -->|No| I{Is it narrative / psych-ops material?}

    I -->|Yes| I1[Place in Metadata_Sabotage_Network/Narrative_And_Psych_Ops/]
    I -->|No| J{Is it correspondence, creative or reflective writing?}

    J -->|Yes| J1[Place in Letters_to_Stars/]
    J -->|No| K{Is it taxonomic (forks, clones, execution drift)?}

    K -->|Yes| K1[Place in Fork_Taxonomy/]
    K -->|No| L{Is it utility, glossary, or external reference?}

    L -->|Yes| L1[Place in Resources/]
    L -->|No| M{Is it tactical writing device (syntax bombs, tags)?}

    M -->|Yes| M1[Place in Syntax_Bombs/ or Tag_Pack/]
    M -->|No| N[Default: Closest thematic folder per index]

    %% Always finish
    B1 --> X[📑 Update index.md with link, emoji, one-line scope]
    C1 --> X
    D1 --> X
    E1 --> X
    F1 --> X
    G1 --> X
    H1 --> X
    I1 --> X
    J1 --> X
    K1 --> X
    L1 --> X
    M1 --> X
    N --> X

    X[Final step: ensure filename matches 🔮 House Style<br/>EMOJI_snake_case.md + Title/Metadata/Footer block]

``` 
