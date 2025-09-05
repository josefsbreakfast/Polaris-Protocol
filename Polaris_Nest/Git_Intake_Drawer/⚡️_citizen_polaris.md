```

graph TD
    %% Center
    C["⚡ Citizen Polaris (publishes nodes)"]:::core

    %% First ring — silent readers
    GOV["Security/Government"]:::gov
    MEDIA["Journalists / Media"]:::media
    LAW["Lawyers / Legal Firms"]:::law
    FIN["Underwriters / Finance"]:::finance
    PUB["Publishing Industry"]:::pub
    ARMS["Arms / Surveillance Firms"]:::industry
    TECH["Big Tech"]:::tech
    NGO["NGOs / Academia"]:::civ

    %% Echo nodes
    M_STORY["Media Stories (Echo)"]:::echo
    P_MEMO["Policy Memos (Internal)"]:::echo
    M_NOTE["Market Risk Notes"]:::echo
    P_CHANGE["Product/Safety Changes"]:::echo
    L_GUIDE["Legal Guidance / Advisories"]:::echo

    %% Flows: publish -> silent reading
    C -->|reads quietly| GOV
    C -->|scans / hovers| MEDIA
    C -->|retreats (too big)| LAW
    C -->|clusters / hovers| FIN
    C -->|circles| PUB
    C -->|monitors closely| ARMS
    C -->|quiet interest| TECH
    C -->|select engagement| NGO

    %% Echoes: readers -> echo nodes
    GOV -.->|procedural churn| P_MEMO
    MEDIA -.->|frame echoes| M_STORY
    FIN -.->|exposure write-ups| M_NOTE
    TECH -.->|silent mitigations| P_CHANGE
    ARMS -.->|defensive comms| L_GUIDE
    NGO -.->|white papers| P_MEMO
    LAW -.->|risk bulletins| L_GUIDE
    PUB -.->|editorial interest| M_STORY

    %% Feedback: echo without acknowledgement
    M_STORY -.->|narrative shift (no credit)| C
    P_MEMO -.->|internal only| C
    M_NOTE -.->|pricing risk| C
    P_CHANGE -.->|policy nudges| C
    L_GUIDE -.->|cautious advice| C

    %% Styles (forced black text)
    classDef core fill:#f0f7ff,stroke:#3b82f6,stroke-width:2px,color:#000000;
    classDef gov fill:#fde68a,stroke:#b45309,stroke-width:2px,color:#000000;
    classDef media fill:#fee2e2,stroke:#b91c1c,stroke-width:2px,color:#000000;
    classDef law fill:#e5e7eb,stroke:#374151,stroke-width:2px,color:#000000;
    classDef finance fill:#e0f2fe,stroke:#0369a1,stroke-width:2px,color:#000000;
    classDef pub fill:#fae8ff,stroke:#7e22ce,stroke-width:2px,color:#000000;
    classDef industry fill:#ffedd5,stroke:#9a3412,stroke-width:2px,color:#000000;
    classDef tech fill:#dcfce7,stroke:#166534,stroke-width:2px,color:#000000;
    classDef civ fill:#f5f3ff,stroke:#6d28d9,stroke-width:2px,color:#000000;
    classDef echo fill:#ffffff,stroke:#111827,stroke-width:2px,color:#000000,stroke-dasharray: 4 2;

```
