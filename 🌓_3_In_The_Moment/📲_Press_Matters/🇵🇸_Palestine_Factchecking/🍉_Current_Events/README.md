# 🍉 Current Events

**Status:** scaffold / awaiting live-question and source map  
**First created:** 2026-08-20 | **Last updated:** 2026-08-20  
*Factchecking live and recently developing claims about Palestine while preserving dates, uncertainty, source provenance and the difference between early reporting and settled evidence.*

---

## 🛰️ Orientation

This folder is the live-events branch of **🇵🇸 Palestine Factchecking**.

It exists because current events create a particular factchecking problem:

> **the demand for certainty is usually highest when the evidence is least complete.**

During war, political crisis and rapidly developing events, information can change within minutes or hours.

Early reports may rely on:

- witnesses;
- emergency services;
- military statements;
- government officials;
- hospitals;
- journalists;
- humanitarian organisations;
- photographs or video;
- satellite imagery;
- social-media posts;
- anonymous briefings;
- and preliminary estimates.

Some early claims will later be confirmed.

Some will be revised.

Some will prove wrong.

Some will remain unresolved.

The purpose of this folder is therefore not to make the archive **fastest**.

It is to make it **time-aware, source-aware and corrigible**.

---

## 🍉 What This Folder Is For

This branch should eventually help answer questions such as:

- What is happening now?
- What happened today, yesterday or this week?
- What is confirmed?
- What is being reported but not independently verified?
- Who made the original claim?
- Has the claim changed since first publication?
- Are different outlets independently confirming it or repeating the same source?
- Is a casualty figure preliminary, identified, verified or estimated?
- Has responsibility for an attack been established?
- What does available imagery show?
- What does it not show?
- Has an official statement been revised?
- Is an old image being presented as current?
- Has a court, government or international body actually made the decision being reported?
- Is a political proposal being described as implemented policy?
- What remains unknown?

The exact node list should be built from recurring live questions rather than guessed in advance.

---

## ⏱️ Time Is Evidence

Every important current-events claim should carry a date.

Where necessary, it should carry a time and timezone too.

Prefer:

> **As of 14:00 UTC on 20 August 2026...**

to:

> **Right now...**

when the proposition can change quickly.

A reader returning three days later should still be able to understand what the node meant when it was written.

---

## 🧭 Separate Event Time From Reporting Time

These are not always the same.

Record where relevant:

- when the event allegedly occurred;
- when it was first reported;
- when the source obtained the information;
- when the archive checked it;
- when later evidence emerged;
- and when the assessment changed.

A report published today may concern an event from last week.

A video uploaded today may have been recorded years ago.

A casualty identification announced today may concern a death that occurred months earlier.

Chronology should survive the news cycle.

---

## 🚦 Working Live-Claim States

For rapidly developing events, the archive may use temporary states such as:

### 🟢 Confirmed / Established

The available evidence is strong enough to state the proposition as established at the time of review.

### 🟡 Reported

A credible source has reported the proposition, but the archive does not yet have enough independent evidence to treat the underlying event as established.

### 🟠 Contested

Materially conflicting accounts exist.

### 🔵 Developing

The situation is changing rapidly enough that the node should be treated as provisional.

### ⚪ Unresolved

Available evidence does not currently permit a reliable determination.

### 🔴 Contradicted

Substantial reliable evidence conflicts with the original proposition.

These labels are temporary aids.

The evidence underneath them matters more than the icon.

---

## 🧬 The First Report Is Not The Final Record

Breaking-news ecosystems reward speed.

Historical records reward accuracy.

Those incentives are not identical.

A useful current-events node should therefore preserve the evolution of a claim.

For example:

```text
09:10 — initial eyewitness report
09:24 — local authority statement
09:40 — military denial
10:15 — first geolocated footage
12:30 — humanitarian organisation update
16:00 — revised casualty figure
next day — satellite imagery available
three days later — investigative reconstruction published
```

The point is not to create enormous timelines for every event.

It is to avoid rewriting history so that everybody appears to have known the final answer from the beginning.

---

## 📣 Official Statements Are Claims

During active conflict, official communications matter enormously.

They should be preserved carefully.

But:

> **official**

does not mean:

> **independently verified.**

An IDF statement can establish what the IDF said.

A Hamas statement can establish what Hamas said.

A Palestinian Authority statement can establish what the Palestinian Authority said.

A British, American, Israeli or other government statement can establish the government's stated position.

Whether the underlying proposition is correct requires the appropriate evidence.

This distinction should remain visible even when an official source is usually considered credible.

---

## 📰 Journalism Needs Source Ancestry

A breaking story may appear simultaneously across dozens of outlets.

That can create an illusion of independent confirmation.

Trace where possible:

```text
official statement
      ↓
news agency
      ↓
multiple newspapers
      ↓
television commentary
      ↓
social media
      ↓
AI summary
```

or:

```text
local journalist
      ↓
international desk
      ↓
wire pickup
      ↓
global reporting
```

Count independent evidential routes, not logos.

---

## 📊 Live Numbers Need Verbs

Current-event statistics change quickly.

Preserve how a number was produced.

Prefer:

- **reported killed**;
- **identified**;
- **confirmed dead**;
- **reported missing**;
- **registered**;
- **verified by**;
- **estimated**;
- **surveyed**;
- **modelled**.

Avoid allowing:

> **officials reported 50 deaths**

to become:

> **exactly 50 people died**

without additional evidence.

Later revision does not automatically prove the original source acted dishonestly.

Early numbers are often produced under terrible conditions.

Record revisions rather than treating them as embarrassment.

---

## 🖼️ Images, Video & Audio

Visual evidence can become globally influential before basic provenance has been established.

For significant media, ask:

- Who uploaded it first?
- When?
- Is the account original or reposting?
- Can the location be established?
- Can the date be established?
- Is the full sequence available?
- Has the media been cropped or edited?
- Is there earlier circulation?
- Does the caption claim more than the image shows?
- Are independent angles available?
- Does specialist analysis exist?

A genuine video with a false caption is still misinformation.

An authentic photograph is not automatically proof of attribution or intent.

---

## 🛰️ OSINT During Breaking Events

OSINT can clarify rapidly developing events.

It can also produce premature certainty.

Early analysts may work with:

- incomplete footage;
- poor-resolution imagery;
- uncertain timestamps;
- missing weapon fragments;
- unknown camera orientation;
- partial satellite coverage;
- or incorrect assumptions about sequence.

Preserve confidence levels.

A first-pass geolocation may later be corrected.

A weapons assessment may change when higher-quality imagery appears.

Do not convert:

> **consistent with**

into:

> **proved by.**

---

## 🧵 Translation During Breaking News

Translations travel quickly and corrections travel slowly.

For consequential statements in Arabic or Hebrew:

- seek the original;
- preserve surrounding context;
- distinguish literal from idiomatic translation;
- note ambiguous words;
- identify whether subtitles were added by the original publisher or downstream;
- and avoid relying on a viral translation simply because many accounts repeat it.

Where the wording could materially change the interpretation of intent, threat, policy or identity, slow down.

---

## ⚖️ Law Moves More Slowly Than Headlines

Current events frequently produce headlines such as:

> **court rules...**

> **UN declares...**

> **arrest warrant means...**

> **country recognises...**

> **sanctions imposed...**

These may compress complicated procedural realities.

Route substantial legal questions to `⚖️_Law/`.

Current Events should establish **what happened procedurally and when**.

Law should establish **what the legal act means**.

Do not make a breaking-news node perform an entire legal memorandum in the middle of a live event.

---

## 🌍 Political Announcements Are Not Always Implemented Policy

Distinguish:

- proposal;
- announcement;
- cabinet decision;
- legislation;
- regulation;
- operational order;
- implementation;
- enforcement;
- and practical effect.

A politician saying something will happen does not establish that it has happened.

A government approving something does not necessarily establish implementation.

A leaked proposal is not policy.

Preserve the stage.

---

## 🧯 Rumour Control

A useful current-events branch should be willing to say:

> **We cannot currently substantiate this.**

That is different from:

> **This is false.**

For viral claims, preserve where possible:

- original wording;
- earliest traceable source;
- supporting evidence;
- contradicting evidence;
- current assessment;
- and what would be required to resolve it.

Do not amplify graphic or defamatory rumours merely to announce that they are unverified.

Sometimes the responsible factcheck is narrow.

---

## 🪞 Correct Without Rewriting The Past

When a live assessment changes:

### Do

- update the current conclusion;
- date the update;
- explain the material new evidence;
- preserve the previous assessment where appropriate;
- correct downstream nodes.

### Do not

quietly rewrite:

> **Reported / unresolved**

into:

> **We always knew this was false.**

The evolution of evidence is part of the record.

---

## 🚨 High-Risk Claims

Exercise particular caution with breaking allegations involving:

- massacres;
- sexual violence;
- torture;
- hostage deaths;
- deliberate targeting of civilians;
- attacks on hospitals, schools or religious sites;
- executions;
- chemical or unusual weapons;
- fabricated atrocities;
- covert state involvement;
- assassination;
- journalists or aid workers;
- and named individuals accused of crimes.

The seriousness of an allegation is not a reason to ignore it.

It is a reason to preserve attribution and evidential status with unusual care.

---

## 🧿 Absence Of Immediate Verification Is Not Disproof

Conflict conditions can make verification slow.

Journalists may not have access.

Investigators may arrive months later.

Bodies may be inaccessible.

Communications may be down.

Witnesses may be displaced.

Records may be destroyed.

Therefore:

> **not independently verified at 15:00**

does not mean:

> **did not happen.**

Equally, the difficulty of verification cannot be used to declare every allegation true.

Unknown remains available.

---

## 🪿 The Human Cost Of Live Information

Breaking events are not merely streams of claims.

They concern people experiencing violence, displacement, fear, grief and uncertainty while the rest of the world argues about what happened to them.

Factchecking should resist two opposite failures:

- treating testimony as untouchable because the witness has suffered;
- treating testimony as disposable because the witness is distressed, partisan or located inside the conflict.

Human beings remain evidence-bearing subjects under terrible conditions.

They are neither infallible nor noise.

---

## 🧭 Suggested Current-Events Structure

**Placeholder only — revise after the live-question review.**

A later structure might include:

```text
🍉_Current_Events/
├── README.md
├── 🚨_Breaking_Claims/
├── 🗓️_Timelines/
├── 📊_Live_Casualty_And_Aid_Data/
├── 🛰️_Strike_And_Incident_Attribution/
├── 🖼️_Media_Verification/
├── 🗣️_Statements_And_Translations/
├── ⚖️_Legal_And_Diplomatic_Developments/
├── 🌍_International_Response/
└── 🔄_Corrections_And_Resolved_Claims/
```

This is a routing sketch, not a committed architecture.

It may turn out that event-specific folders work better than source-type folders.

---

## 🔍 Likely Question Clusters

**Placeholder for later expansion.**

### Incident attribution

- Who carried out this strike?
- What evidence supports attribution?
- Has responsibility been acknowledged or denied?
- What does imagery establish?
- What remains uncertain?

### Casualties

- How many people are reported killed or injured?
- Who produced the number?
- How many have been identified?
- Are civilians and combatants being classified?
- Has the figure been revised?

### Aid and humanitarian conditions

- How much aid entered?
- Through which crossings?
- What does “entered Gaza” mean compared with distribution?
- What do food-security or health assessments actually measure?
- Are different institutions counting different things?

### Hostages and detainees

- How many remain held?
- Who has been released?
- Who is confirmed dead?
- What is allegation, testimony, official statement or verified evidence?
- Which legal categories apply?

### Diplomacy

- What did a government announce?
- Has recognition, sanction, suspension or embargo actually taken legal effect?
- What did the vote do?
- What happens next procedurally?

### Viral claims

- Is the image current?
- Is the translation accurate?
- Is the quotation real?
- Does the video show what the caption says?
- Is the account authentic?
- Is an old event being recirculated as new?

---

## 🔬 Current-Event Factcheck Template

A substantial live node can eventually use:

```text
## Question

## Checked At

## Short Answer

## Current Status

## Claim Being Checked

## What We Know

## What Is Being Reported

## Primary Sources

## Independent Corroboration

## Conflicting Evidence

## What Remains Unknown

## Timeline Of Updates

## Current Assessment

## Sources
```

Where the situation is developing, put **Checked At** near the top.

The reader should never have to guess how stale the answer might be.

---

## 🔄 Update Discipline

For live nodes, consider an update log:

```text
### 2026-08-20 14:00 UTC
Initial assessment.

### 2026-08-20 18:30 UTC
Added independent imagery; attribution remains unresolved.

### 2026-08-21 09:15 UTC
Updated casualty figure following identification data.

### 2026-08-23
Assessment changed from Contested to Strongly Supported following investigation.
```

Not every typo needs a changelog entry.

Material evidential changes do.

---

## 🔗 Relationship To Other Branches

Current events will frequently route outward.

Use:

- `🫒_History/` when a live claim depends on historical chronology;
- `⚖️_Law/` for legal classification and procedural interpretation;
- `📊_Statistics/` for casualty, demographic, aid and methodological disputes;
- `🧵_Identity_And_Language/` for contested terminology and translation;
- `🌍_Global_Powers/` for foreign-state policy, military support, diplomacy and material involvement;
- `🧿_Ethics/` for normative questions;
- `🪿_Embodying_The_Information_Ecology/` for virality, propaganda, platform behaviour, PR, search and AI mediation.

A live event can touch all of them.

Cross-link rather than duplicating whole analyses.

---

## 🧪 Questions For The Live-Source Review

To return to later:

- Which sources provide the fastest primary official statements?
- Which journalists and organisations have meaningful on-the-ground access?
- Which live casualty datasets should be monitored?
- Which humanitarian dashboards are canonical for which measures?
- Which crossing and aid datasets distinguish entry from distribution?
- Which OSINT organisations publish reproducible work?
- Which satellite sources are publicly accessible?
- Which Arabic and Hebrew sources need routine checking?
- Which news wires frequently sit upstream of international coverage?
- How should live claim status be displayed consistently?
- What threshold moves a claim from **Reported** to **Established**?
- When should an event get its own node?
- How long should a “current event” remain here before being routed into history?
- How should resolved misinformation be archived without continuing to amplify it?
- Which current questions are asked repeatedly enough to deserve standing explainers?

---

## 🌾 Current Status

**Status:** scaffold / awaiting dedicated live-question and source review.

This README establishes the operating logic for rapidly changing claims.

It does **not** yet commit the archive to a fixed folder architecture, canonical breaking-news source list or permanent set of live topics.

Those should emerge from actual use.

---

## 🌌 Constellations

🍉 ⏱️ 🚦 🛰️ 🔄 — breaking claims; timestamps; attribution; verification; revision.

## ✨ Stardust

palestine, israel, current events, breaking news, factchecking, live claims, casualty figures, osint, verification, corrections

---

## 🏮 Footer

*🍉 Current Events* is the live factchecking branch of the **Polaris Protocol's Palestine Factchecking** pack.

It routes rapidly developing claims through timestamped, source-aware verification while preserving the difference between reporting, corroboration, attribution, revision and settled evidence.

> 📡 Cross-references:
>
> - [🌾 Start Here](../🌾_Start_Here/README.md) — *methodological front door*
> - [⚖️ Factchecking Principles](../🌾_Start_Here/⚖️_factchecking_principles.md) — *working evidential standards*
> - [📚 Sources & Evidence Register](../🌾_Start_Here/📚_sources_and_evidence_register.md) — *source provenance and future live-source review*
> - [🫒 History](../🫒_History/README.md) — *historical chronology and evidence*
> - [⚖️ Law](../⚖️_Law/README.md) — *legal questions and classifications*
> - [📊 Statistics](../📊_Statistics/README.md) — *numbers, datasets and methodology*
>
> 🏮 Return To:
>
> - [🇵🇸 Palestine Factchecking](../README.md) — *1up*
> - [📲 Press Matters](../../README.md) — *2up*
> - [🌓 In The Moment](../../../README.md) — *3up*
> - [🌌 Polaris Protocol — Root](../../../../README.md) — *root*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-20_
