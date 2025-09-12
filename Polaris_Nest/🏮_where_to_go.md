flowchart TD
    A[Start: You have a new file] --> B{Is this repo-level meta/governance?}
    B -->|Yes| B1[Place at top-level next to meta docs<br/>e.g. _house_style.md, survivor_voice_rules.md<br/>Name with leading underscore if your index does]
    B -->|No| C{Does it define or change the protocol itself?}

    C -->|Yes| C1[Put in the Protocol section named in index<br/>e.g. /protocol/ or the exact section path<br/>File lives with canonical specs + version notes]
    C -->|No| D{Is it a how-to / operator guide / playbook?}

    D -->|Yes| D1[Put in Guides/Operations section from index<br/>e.g. /guides/ or /ops/]
    D -->|No| E{Is it evidence, transcripts, case material, or records?}

    E -->|Yes| E1[Put in Records/Evidence section from index<br/>e.g. /records/, /evidence/, or what the index calls it]
    E -->|No| F{Is it research notes, analysis, or drafts not yet canonical?}

    F -->|Yes| F1[Put in Drafts/Notes/Research section from index<br/>e.g. /drafts/ or /notes/<topic>]
    F -->|No| G{Is it a template, checklist, or form?}

    G -->|Yes| G1[Put in Templates section from index<br/>e.g. /templates/ with clear filename + version]
    G -->|No| H{Is it a reference or explainer for external readers?}

    H -->|Yes| H1[Put in Public/Explainers section from index<br/>e.g. /explainer/ or /public/ if present]
    H -->|No| I{Is it a reusable asset (images, diagrams, datasets)?}

    I -->|Yes| I1[Put in Assets section from index<br/>e.g. /assets/ (images), /data/ (CSV/JSON), /figures/]
    I -->|No| J{Is it superseded or historical?}

    J -->|Yes| J1[Move to Archive section from index<br/>e.g. /archive/YYYY/<file> with a short tombstone note]
    J -->|No| K[Fallback: Place next to the nearest section your index links for this topic\nand add a short index entry]

    %% Cross-links / hygiene
    B1 --> X[Update the index: title + one-line purpose]
    C1 --> X
    D1 --> X
    E1 --> X
    F1 --> X
    G1 --> X
    H1 --> X
    I1 --> X
    J1 --> X
    K --> X

    X[Final step: Update index.md\n- Link the file under the right section\n- Add date + status (Draft/Canon/Archived)\n- Cross-link related items (suppression ↔ counter-nudge)]
