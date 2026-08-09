# ⏱️ Timeline Of Essential Infrastructure Attacks
**First created:** 2026-08-01 | **Last updated:** 2026-08-09  
*A provisional open-source chronology of cyber incidents affecting essential state infrastructure during the Iran war.*

---

## ⚠️ Evidence Boundary

This is a live working timeline.

It is not an attribution ledger.

It is not a list of Iranian attacks.

It is not a list of war crimes.

Some incidents are:

- officially attributed to Iranian or Iran-linked actors;
- assessed as probable or suspected;
- claimed by actors without independent confirmation;
- attributed to criminal or proxy operators whose ultimate customer remains unclear;
- unattributed;
- or included because they affected essential state infrastructure during the war window and remain analytically relevant.

Inclusion does **not** mean that Iran carried out the incident.

Timing, clustering, target selection, technical resemblance, operational effect, shared infrastructure, and known historical methods may justify scrutiny.

They do not establish causation by themselves.

Each entry should therefore preserve several different questions:

```text
DID THE INCIDENT HAPPEN?

WHAT DID IT AFFECT?

HOW FAR INTO THE SYSTEM DID IT REACH?

WHAT OPERATIONAL EFFECT FOLLOWED?

IS IT PART OF A REPEATED PATTERN?

WHO OPERATED IT?

WHO MAY HAVE DIRECTED IT?

WHAT CAN BE ATTRIBUTED PUBLICLY?

WHAT REMAINS UNKNOWN?
```

The answers may have different confidence levels.

The baseline used here is **28 February 2026**, marking the beginning of the US–Israeli military campaign against Iran for the purposes of this pack.

---

## 🧭 Reading Rule

The timeline records:

```text
date
→ country
→ sector
→ affected function
→ technical depth
→ operational / physical / data effect
→ incident / effect confidence
→ operator / customer / attribution status
→ relationship confidence
→ pattern significance
→ legal-routing significance
→ recovery status
→ source quality / provenance
→ review history
```

It does not assume that all incidents form one campaign.

It exists so that repeated small events, cross-sector movement, operational-technology targeting, shared dependencies, institutional response patterns, and changes in attribution can be compared without turning uncertainty into certainty.

---

## 🧮 Confidence Belongs To The Proposition

A single confidence label is no longer sufficient.

The timeline should attach confidence to the **specific proposition being made**.

That means separating, where relevant:

### Incident Confidence

> How confident are we that the reported event occurred?

### Scope Confidence

> How confident are we that the incident belongs inside this pack's essential-state-infrastructure perimeter?

### Effect Confidence

> How confident are we about the reported operational, physical, data, record-integrity, civilian, safety, or service consequences?

### Attribution Confidence

> How confident are we about the technical operator, organisation, intermediary, customer, state affiliation, or state direction?

### Relationship Confidence

> How confident are we that this incident is actually related to another incident or cluster?

### Pattern Confidence

> How confident are we that repeated incidents form a meaningful recurring pattern?

### Legal Confidence

> How far does the public evidence support a legal characterisation or justify legal review?

### Recovery Confidence

> How confident are we that technical, service, data, or person-centred recovery is actually complete?

These can diverge.

For example:

```text
INCIDENT:
🟢 CONFIRMED

SCOPE:
🟢 CONFIRMED

OPERATIONAL EFFECT:
🟢 CONFIRMED

RELATIONSHIP TO WATER CLUSTER:
🟡 PROBABLE

TECHNICAL OPERATOR:
🟡 PROBABLE

STATE AFFILIATION:
🟠 SUSPECTED

STATE DIRECTION:
⚪ OPEN

PATTERN STATUS:
🔴 ESTABLISHED CAMPAIGN PATTERN

LEGAL REVIEW:
REVIEW WARRANTED
```

That is not contradictory.

It is the point of the method.

A campaign pattern may become visible before its sponsor can responsibly be named.

---

## 🚦 Traffic-Light Confidence

The timeline uses the traffic-light system defined in [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md).

The light belongs to the **specific proposition beside it**.

It is not a severity scale.

It is not a measure of strategic importance.

It does not colour the entire incident.

Use:

```text
🟢 ESTABLISHED / CONFIRMED

The proposition is strongly supported
by the available public evidence.


🟡 PROBABLE

The available evidence strongly favours
the proposition, but an important gap remains.


🟠 SUSPECTED / DEVELOPING

There is a credible evidentiary basis
for scrutiny, but material uncertainty remains.


⚪ OPEN / UNATTRIBUTED

The proposition has not been established.


❌ EXCLUDED

Later evidence no longer supports
the proposition or inclusion.
```

Therefore:

```text
INCIDENT:
🟢 CONFIRMED

ATTRIBUTION:
🟠 SUSPECTED

COMMON CUSTOMER:
⚪ OPEN
```

is a legitimate result.

### 📣 Actor-Claimed Is A Modifier

Actor claims remain separate from confidence.

Use:

```text
CLAIM STATUS:
📣 ACTOR-CLAIMED

ATTRIBUTION CONFIDENCE:
⚪ OPEN
```

where that is what the evidence supports.

`📣 ACTOR-CLAIMED` means that a claim exists.

It does not establish that the claimant caused the incident.

### ⚪ Missing Information Is Not One Thing

Where information is missing, distinguish:

```text
UNKNOWN
```

The answer has not been established.

```text
NOT PUBLIC
```

The information may exist but is not publicly available.

```text
NO EVIDENCE FOUND
```

A search was conducted but no supporting public evidence was located.

```text
WITHHELD / NCND
```

The relevant authority declined to confirm or deny.

```text
NOT APPLICABLE
```

The question does not apply.

These statuses should not be collapsed into one blank field.

---

## 🎨 Pattern Status

Use:

```text
⚪ ISOLATED
No meaningful recurrence established.

🟡 POSSIBLE RECURRENCE
Some overlap in target, timing, technique, technology, geography, or effect.

🟠 CREDIBLE CLUSTER
Several incidents share enough characteristics to justify campaign-level scrutiny.

🔴 ESTABLISHED CAMPAIGN PATTERN
Repeated related activity is independently established, even where ultimate sponsorship remains unresolved.
```

This scale describes **pattern confidence**.

It does not describe attribution confidence.

Therefore:

```text
🔴 ESTABLISHED CAMPAIGN PATTERN
```

can coexist with:

```text
IRANIAN ATTRIBUTION:
UNRESOLVED
```

---

## 🪜 Operational Depth

Where operational technology is involved, record how far the evidence reaches.

```text
LEVEL 0 — EXTERNAL RECONNAISSANCE

LEVEL 1 — IT / ADMINISTRATIVE ACCESS

LEVEL 2 — OT NETWORK VISIBILITY

LEVEL 3 — HMI / CONTROL INTERFACE ACCESS

LEVEL 4 — CONTROLLER OR CONFIGURATION ACCESS

LEVEL 5 — COMMAND / SETTING MANIPULATION

LEVEL 6 — OBSERVED PHYSICAL-PROCESS CHANGE

LEVEL 7 — SAFETY / SERVICE / PHYSICAL HARM
```

Do not infer Level 6 or 7 from evidence establishing only Level 2 or 3.

Likewise:

```text
LOSS OF VIEW
≠
LOSS OF CONTROL
≠
ATTACKER CONTROL
≠
PHYSICAL MANIPULATION
```

The timeline should record the deepest publicly supported level.

---

## 📌 Current Chronology

## 2026-02-28

### 🇺🇸 United States / 🇮🇱 Israel / 🇮🇷 Iran

### Context

War baseline: beginning of the US–Israeli military campaign against Iran for the purposes of this pack.

This is the comparison point for subsequent cyber activity.

### Incident confidence

Context row; not a cyber incident.

### Attribution confidence

Not applicable.

### Pattern status

Not applicable.

### Sources

Baseline source should be attached in the next sourcing pass.

---

## 2026-03-02

### 🇬🇧 United Kingdom / 🇨🇾 Cyprus and British Sovereign Base Areas

### Sector

Cross-sector critical infrastructure / national cyber preparedness.

### What happened

The UK NCSC advised organisations to review their cyber posture following the escalation in the Middle East.

It assessed no significant immediate change in the direct Iranian cyber threat to the UK, while identifying heightened indirect risk for organisations with Middle East exposure and possible collateral activity by Iran-linked hacktivists.

### Operational effect

Threat advisory rather than a recorded infrastructure disruption.

### Attribution confidence

Official threat assessment.

No incident attribution.

### Pattern status

⚪ **Context / preparedness marker**

### Iran-war relevance

Direct.

The advisory establishes the British government's early-war public cyber-risk position against which later incidents can be compared.

### Sources

- NCSC — *NCSC advises UK organisations to take action following conflict in Middle East*

---

## 2026-03-10

### 🇮🇱 Israel

### Sectors

Healthcare; government; defence; telecommunications.

### What happened

Open-source reporting described Iran-linked actors using criminal tooling against Israeli hospitals and organisations in government, defence and telecommunications.

### Attribution confidence

Campaign-level Iran-linked reporting.

Individual incidents require separate attribution where available.

### Pattern status

🟡 **Possible recurrence / multi-sector activity**

### Iran-war relevance

High.

Israel is a direct belligerent and a longstanding target of Iranian and Iran-linked cyber operations.

---

### 🇦🇱 Albania

### Sector

Government administration / parliamentary infrastructure.

### What happened

Albania's parliament reported an attempted data-wiping and systems-compromise attack.

Internal email and staff computer access were disrupted.

Iran-linked Homeland Justice claimed responsibility.

### Operational effect

Administrative disruption.

### Claimed actor

Homeland Justice.

### Attribution confidence

Actor claim plus established historical Iran nexus.

Current state direction not independently established by the source recorded here.

### Pattern status

🟡 **Possible recurrence**

### Rival explanations

Actor branding and historical affiliation do not independently establish direction of the specific operation.

### Sources

- CERT-EU Cyber Brief 2026-04

---

## 2026-03-11

### 🇺🇸 United States / 🇮🇪 Ireland / wider international operations

### Sector

Healthcare / medical-device manufacturing and supply.

### Affected body

Stryker.

### What happened

A cyberattack disrupted Microsoft systems, order processing, manufacturing and shipments.

Stryker's Irish operations were also affected.

Handala claimed the attack as retaliation for US–Israeli strikes.

### Operational effect

Disruption to manufacturing, ordering and medical-device supply operations.

### Claimed actor

Handala.

### Attribution confidence

Iran-linked actor claim.

The company confirmed disruption but did not itself publicly attribute the attacker in the source chain recorded here.

### Pattern status

🟡 **Possible recurrence**

### Civilian / IHL relevance

Healthcare supply infrastructure.

The incident warrants preservation for legal analysis because medical supply can have downstream civilian consequences.

This does **not** establish an IHL violation or war crime.

### Sources

- Reuters, 11 March 2026
- CERT-EU Cyber Brief 2026-04

---

## 2026-03-12

### 🇵🇱 Poland

### Sector

Nuclear research / government scientific infrastructure.

### Affected body

National Centre for Nuclear Research.

### What happened

Poland reported an unsuccessful cyberattack against the centre.

Early indicators reportedly pointed toward Iranian origins.

Officials explicitly warned that those indicators could represent misdirection.

### Operational effect

System integrity reportedly remained intact.

### Attribution confidence

**Low / suspected Iran link.**

The source itself preserves the possibility of deliberate misdirection.

### Pattern status

⚪ **Isolated**

### Rival explanations

False-flag indicators, opportunistic intrusion, or another actor.

### Sources

- CERT-EU Cyber Brief 2026-04

---

## 2026-03-13

### 🇸🇪 Sweden

### Sector

Government administration / e-government.

### What happened

Researchers reported alleged theft of data associated with a Swedish e-government platform through contractor CGI Sweden.

Source code was reportedly released and citizen databases offered for sale.

### Data effect

Potential loss of state-held or state-service data from custody.

### Attribution confidence

Unattributed cybercrime claim.

No public Iran attribution recorded.

### Pattern status

⚪ **Isolated**

### Iran-war relevance

Included because it affects state digital-service infrastructure during the war window.

Timing alone does not establish Iran relevance.

### Sources

- CERT-EU Cyber Brief 2026-04

---

## 2026-03-19

### 🇳🇱 Netherlands

### Sector

Government administration / finance.

### Affected body

Dutch Ministry of Finance.

### What happened

The ministry detected a breach after notification by a third party.

Some employee systems were affected.

Tax, customs and benefits services reportedly remained operational.

### Operational effect

Internal systems affected without reported interruption to major citizen-facing services.

### Attribution confidence

Unknown actor.

No public Iran attribution.

### Pattern status

⚪ **Isolated**

### Sources

- CERT-EU Cyber Brief 2026-04

---

## 2026-03-25

### 🇳🇱 Netherlands

### Sector

Policing / justice infrastructure.

### Affected body

Dutch National Police.

### What happened

Police reported a successful phishing breach.

Access was blocked.

No citizen or investigative data was reported exposed.

### Attribution confidence

Unknown actor.

No public Iran attribution.

### Pattern status

⚪ **Isolated**

### Sources

- CERT-EU Cyber Brief 2026-04

---

## 2026-05-26

### 🇺🇸 United States

### Sector

Transport.

### Affected body

Los Angeles County Metropolitan Transportation Authority.

### What happened

Security researchers attributed a March breach of Los Angeles Metro systems to Iranian-backed hackers.

Recovery reportedly took weeks.

### Operational effect

Extended recovery from compromise of public transport infrastructure.

### Attribution confidence

Researcher attribution to an Iran-backed / MOIS-linked operation.

Formal US governmental attribution was not established in the source recorded here.

### Pattern status

🟡 **Possible recurrence**

### Iran-war relevance

Significant.

The affected body performs an essential metropolitan transport function in a direct belligerent state.

### Sources

- TechCrunch, 26 May 2026

---

## 2026-06-17

### 🇬🇧 United Kingdom

### Sector

Aggregate critical infrastructure.

### What happened

NCSC said it had managed more than 200 incidents affecting UK critical infrastructure and its supporting ecosystem in the year to May 2026.

Approximately three-quarters were believed linked to hostile states.

### Attribution confidence

Aggregate hostile-state assessment.

Not Iran-specific.

### Pattern status

🔴 **Established hostile-state cyber pressure at aggregate UK level**

### Important limit

This does **not** establish that three-quarters of incidents were Iranian.

The entry is relevant as background for assessing the wider hostile-state environment in which Iran-war incidents occur.

### Sources

- NCSC, 17 June 2026

---

## 🚰 The US Water / Wastewater OT Sequence

The following entries should be read both individually and as successive observations of a developing campaign picture.

The crucial distinction is:

```text
PATTERN CONFIDENCE
≠
IRAN ATTRIBUTION CONFIDENCE
```

---

## 2026-07-26 — 2026-07-27

### 🇺🇸 United States — Minnesota

### Sector

Water and wastewater.

### Affected bodies

More than 30 Minnesota community water systems were reported targeted over approximately 48 hours.

### What happened

A coordinated series of cyber incidents affected municipal water infrastructure.

Reported effects across the developing campaign included:

- operator lockouts;
- changes to network or controller settings;
- communications disruption;
- pressure loss;
- flooding;
- temporary shutdowns;
- and movement to manual operation.

### Operational depth

Evidence indicates interaction with operational technology rather than merely public websites or ordinary office IT.

Individual facilities may have experienced different levels of access.

Do not assign the deepest reported effect to every affected system.

### Operational effect

Operational degradation occurred at some facilities.

Manual intervention and fallback procedures appear to have limited wider consequences.

### Physical effect

Pressure loss and flooding were reported within the wider investigated campaign.

No evidence presently recorded here establishes drinking-water contamination.

### Manual / fallback response

Manual operation was used at affected facilities.

### Attribution confidence

**Moderate / developing suspicion of Iran-linked activity.**

No definitive public attribution of the entire current wave was established at this stage.

State and federal reporting connected the investigation to known Iran-affiliated PLC / OT activity.

### Pattern status

🟠 **Credible cluster**

### Iran-war relevance

High.

The campaign affects civilian water infrastructure in a direct belligerent state and closely follows previously documented Iranian-affiliated interest in exposed industrial controllers.

### IHL / protected-infrastructure relevance

**Review warranted.**

Civilian drinking-water infrastructure deserves particular legal scrutiny during armed conflict.

This status does **not** mean a war crime has been established.

### Rival explanations

- opportunistic exploitation of exposed controllers;
- criminal activity;
- hacktivist activity;
- copycat use of known Iranian methods;
- or a mixture of operators.

### Sources

- Reuters, 28 July 2026
- Reuters, 30 July 2026

---

## 2026-07-29

### 🇬🇧 United Kingdom

### Sectors

Education / government administration / policing and justice data.

### Affected bodies

Department for Education and Police National Legal Database.

### What happened

Breaches exposed more than 740,000 data items.

ExfilSquad claimed the intrusions and demanded payment.

DfE, NCSC, NCA and ICO investigations were under way.

### Data effect

Large-scale exposure of data associated with essential public administration and policing infrastructure.

### Claimed actor

ExfilSquad.

### Attribution confidence

Claimed by a previously unknown cybercriminal group.

No public Iran attribution.

### Pattern status

🟡 **Possible cross-institutional cluster**

### Iran-war relevance

Unresolved.

The incidents fall inside the wartime monitoring window and affect essential state data infrastructure.

That is not evidence of Iranian involvement.

### Operator / customer question

The criminal attribution should not automatically be treated as resolving ultimate sponsorship.

Equally, the possibility of hidden tasking should not be inferred without evidence.

### Person-centred recovery

Open question.

Technical recovery does not by itself resolve the consequences of exposed state-held personal data.

### Sources

- The Guardian, 29 July 2026

---

## 2026-07-30

### 🇺🇸 United States — multi-state

### Sector

Water and wastewater / operational technology.

### What happened

CISA and FBI warned of a significant increase in attacks affecting water and wastewater control technology.

Similar incidents had by then been reported in at least seven states.

Some produced operational degradation.

### Operational depth

The warning concerned industrial-control and operational-technology environments rather than only conventional IT.

### Attribution confidence

**Moderate / unresolved.**

Iranian involvement was reportedly suspected by investigators and the activity was consistent with earlier Iran-affiliated targeting.

No definitive federal or state attribution of the whole current wave had been publicly established at publication.

### Pattern status

🟠 **Credible multi-state cluster**

### What changed

The analytical unit widened from:

```text
Minnesota incident cluster
```

to:

```text
multi-state US water / wastewater OT campaign
```

### Rival explanations

The exposed-controller environment permits opportunistic exploitation by multiple actors.

Common target technology does not by itself establish a common sponsor.

### Sources

- Reuters, 30 July 2026
- Reuters, 31 July 2026

---

## 2026-08-04 — 2026-08-07

### 🇺🇸 United States — widening multi-state water campaign

### Sector

Water and wastewater / operational technology.

### What changed

Subsequent reporting widened the known or investigated footprint of the water-sector activity beyond the seven states publicly discussed on 30 July.

Reporting described affected or targeted utilities across **at least 12 states**.

Michigan subsequently confirmed multiple affected systems.

### Operational effect

The developing national picture included:

- controller or network-setting changes;
- operator lockouts;
- forced manual intervention;
- temporary shutdowns;
- pressure disruption;
- and flooding at some facilities.

The effects were not uniform across every system.

No single operational consequence should therefore be attributed to every affected utility.

### Operational depth

The campaign increasingly supports the assessment that the relevant pattern involves **operational technology and industrial controllers**, rather than merely generic municipal IT compromise.

### Incident confidence

**High** for the existence of a geographically distributed water-sector campaign.

### Attribution confidence

**Moderate / developing.**

Iran remained a leading investigative hypothesis in public reporting.

Definitive public federal attribution of the entire current wave remained incomplete.

### Pattern status

🔴 **Established campaign pattern**

This label refers to the recurrence of related water / wastewater OT activity.

It does **not** mean Iranian sponsorship has been established for every incident.

### Why the pattern status changed

The evidence now combines:

```text
repeated target class
+
repeated OT / PLC exposure
+
multiple states
+
compressed time window
+
similar operational effects
+
earlier documented Iran-affiliated PLC activity
```

That is sufficient to treat the activity as a campaign-level phenomenon for defensive analysis.

It is not sufficient by itself to assign every incident to Iran.

### Iran-war relevance

**High.**

The target is essential civilian infrastructure in a direct belligerent state.

The activity also resembles a known Iranian-affiliated operational interest in exposed industrial controllers.

### IHL / protected-infrastructure relevance

**Review warranted.**

The legal question depends upon:

- armed-conflict nexus;
- actual target;
- civilian or military function;
- operational effect;
- foreseeable civilian consequences;
- attribution;
- state responsibility;
- and, separately, evidence of individual criminal responsibility.

Therefore:

```text
WATER CAMPAIGN ESTABLISHED
≠
IRANIAN RESPONSIBILITY ESTABLISHED
≠
IHL VIOLATION ESTABLISHED
≠
WAR CRIME ESTABLISHED
```

### Rival explanations

Still include:

- opportunistic criminal exploitation;
- hacktivist activity;
- multiple unrelated actors exploiting the same exposed technology;
- copycat operations;
- and deliberate imitation or misdirection.

### Trend change since 28 February 2026

The water / OT line should now be described as:

> A geographically distributed and repeated campaign against US municipal water operational technology is visible in the public record. Iranian involvement remains a serious investigative hypothesis, strengthened by earlier documented Iran-affiliated PLC activity, but public attribution of the entire current wave remains unresolved.

This is a stronger statement than:

> several similar incidents have occurred.

It remains weaker than:

> Iran conducted the campaign.

---

## 📈 Campaign-Level Trend Since 28 February 2026

The public record currently supports several different observations.

## 1. Iranian and Iran-linked activity is not confined to defence networks

Recorded or reported activity during the war window has touched:

- healthcare;
- government;
- defence;
- telecommunications;
- transport;
- scientific infrastructure;
- and operational technology.

## 2. Essential civilian infrastructure is inside the cyber-risk perimeter

The strongest current example is water.

The important development is not a spectacular nationwide outage.

It is:

```text
many local systems
+
shared technological weakness
+
repeated intrusion
+
real operational effects
+
geographic spread
```

## 3. Pattern confidence can outrun attribution confidence

The US water campaign now demonstrates why these must be recorded separately.

A repeated campaign can be evident before the public record establishes its ultimate sponsor.

## 4. Small operational effects matter

Manual intervention, short shutdowns, loss of pressure, lockouts, flooding, unavailable systems, extended recovery and data exposure should not disappear merely because national services continue functioning.

## 5. Criminal branding does not necessarily resolve sponsorship

Some incidents are plainly consistent with ordinary cybercrime.

Others involve actors described as proxies, affiliates, hacktivists or criminal operators.

The timeline should preserve the distinction between:

```text
WHO PERFORMED THE TECHNICAL ACTION
```

and:

```text
WHO ULTIMATELY REQUESTED / DIRECTED / BENEFITED FROM IT
```

without inventing an answer to the second question.

---

## 🧬 What Would Constitute A Further Pattern Shift?

The trend should be upgraded again where credible evidence shows one or more of the following:

- movement from access into repeated physical-process manipulation;
- confirmed contamination or safety effects;
- simultaneous attacks across water and energy;
- movement from local utilities into major regional infrastructure;
- common infrastructure linking incidents previously treated separately;
- confirmed reuse of the same operational tooling;
- coordinated attacks across several coalition countries;
- repeated healthcare disruption;
- disruption to systemically important banking or payment infrastructure;
- confirmed state direction;
- or official attribution linking previously separate clusters.

The absence of one spectacular outage should not prevent recognition of a campaign.

Conversely, several dramatic headlines should not manufacture a campaign where the technical evidence does not connect them.

---

## 👾 Legal Review Is A Routing Function

This timeline should flag legal questions.

It should not decide them casually.

Use:

```text
IHL REVIEW:

NOT INDICATED
MONITOR
REVIEW WARRANTED
ACTIVE LEGAL QUESTION
FORMAL FINDING
```

The existence of civilian or specially protected infrastructure may justify moving an incident into legal review.

It does not establish unlawfulness.

For cyber incidents:

```text
CYBER INCIDENT
≠
CYBERATTACK FOR IHL PURPOSES
≠
UNLAWFUL ATTACK
≠
WAR CRIME
```

Attribution creates additional layers:

```text
TECHNICAL OPERATOR
≠
ORGANISATIONAL AFFILIATION
≠
STATE DIRECTION
≠
STATE RESPONSIBILITY
≠
INDIVIDUAL CRIMINAL RESPONSIBILITY
```

Route serious cases to:

[👾 Cyber War Crimes](./👾_cyber_war_crimes.md)

---

## 🔎 Gaps In The Current Record

The present dataset remains uneven.

It currently contains stronger public-source coverage for:

- the United States;
- the United Kingdom;
- Israel;
- and parts of wider Europe.

It contains little or no structured coverage yet for:

- Gulf and regional partner states;
- Canada as a separate category;
- other allied or partner states;
- privately disclosed incidents;
- incidents suppressed for operational or commercial reasons;
- locally reported OT incidents that never reach national media;
- incidents reported in languages not yet systematically reviewed;
- and cases where personal harm continued after technical recovery.

Absence from this timeline is not evidence that no incident occurred.

It may reflect:

- no public disclosure;
- weak reporting;
- delayed attribution;
- language barriers;
- fragmented local records;
- classification;
- commercial confidentiality;
- or a decision by the affected institution not to publish details.

The timeline should therefore describe the **visible public record**, not pretend to represent the total universe of incidents.

---

## 🔄 Attribution History Must Remain Visible

Do not silently overwrite an earlier attribution assessment.

Where the assessment changes, preserve the movement.

For example:

```text
2026-07-26
UNATTRIBUTED / INVESTIGATION OPEN

↓

2026-07-30
IRANIAN INVOLVEMENT SUSPECTED

↓

2026-08-07
IRAN-LINK STRENGTHENED / STILL NOT FORMALLY ATTRIBUTED
```

Use:

```text
PREVIOUS STATUS:
NEW STATUS:
WHAT CHANGED:
SOURCE:
DATE REVIEWED:
```

This allows readers to distinguish:

```text
WHAT WAS KNOWN THEN
```

from:

```text
WHAT IS KNOWN NOW
```

That distinction is essential in a live wartime chronology.

---

## 🔄 General Update Rules

An entry should be updated where:

- an official attribution is made;
- technical evidence strengthens or weakens a suspected link;
- an actor claim is disproved;
- operational impact changes;
- physical consequences become known;
- stolen data is published or reused;
- record manipulation is discovered;
- another incident reveals a common provider or technology;
- the pattern classification changes;
- an IHL assessment changes;
- a correction is issued;
- or a rival explanation becomes stronger.

Entries should be downgraded or removed where the evidence no longer supports inclusion.

Corrections are part of the timeline.

They are not a failure of it.

---

## 🧾 New-Entry Template

The incident record should preserve enough structure to distinguish:

```text
event
≠
effect
≠
relationship
≠
pattern
≠
operator
≠
customer
≠
state direction
≠
legal conclusion
```

Use:

```text
DATE:
COUNTRY:
SECTOR:
AFFECTED BODY:

IRAN-WAR RELEVANCE:
SCOPE TRAFFIC LIGHT:
SCOPE CONFIDENCE:

WHAT HAPPENED:
SYSTEM LAYER:
DEPTH OF ACCESS:

OPERATIONAL EFFECT:
PHYSICAL EFFECT:
DATA-CONFIDENTIALITY EFFECT:
DATA-INTEGRITY EFFECT:
RECORD-INTEGRITY EFFECT:
CIVILIAN EFFECT:
SAFETY EFFECT:
SERVICE EFFECT:
MANUAL / FALLBACK RESPONSE:

SEVERITY:
OPERATIONAL SIGNIFICANCE:
STRATEGIC SIGNIFICANCE:

TECHNICAL RECOVERY:
PERSON-CENTRED RECOVERY:
RECOVERY CONFIDENCE:

CLAIM STATUS:
CLAIMED ACTOR:

TECHNICAL OPERATOR:
GROUP / ALIAS:
TOOLING / INFRASTRUCTURE:
CRIMINAL / ACCESS INTERMEDIARY:
ACCESS BROKER:
CONTRACTOR / PROXY:
BUYER / CUSTOMER:
STATE AFFILIATION:
STATE RELATIONSHIP TYPE:
STATE DIRECTION:
FINAL BENEFICIARY:

PUBLIC GOVERNMENT ATTRIBUTION:
INTERNAL / INTELLIGENCE POSITION:
PUBLIC SUPPORTING EVIDENCE:

INCIDENT TRAFFIC LIGHT:
INCIDENT CONFIDENCE:

EFFECT TRAFFIC LIGHT:
EFFECT CONFIDENCE:

ATTRIBUTION TRAFFIC LIGHT:
ATTRIBUTION CONFIDENCE:

RELATIONSHIP CONFIDENCE:
PATTERN STATUS:

IHL / PROTECTED-INFRASTRUCTURE RELEVANCE:
LEGAL REVIEW:

RELATED INCIDENTS:
SHARED TECHNOLOGY / PROVIDER:
COMMON VULNERABILITY:
PATTERN SIGNIFICANCE:

SOURCE TIER:
SOURCE QUALITY:
ORIGINAL SOURCE:
SOURCE DATE:
EVIDENCE CUTOFF:
FIRST REPORT:
LATER REPORTS:
INDEPENDENT CORROBORATION:
COMMON SOURCE DEPENDENCY:
SOURCE PROVENANCE:

EVIDENCE FOR:
EVIDENCE AGAINST:
NEGATIVE FINDINGS:
LIMIT:
RIVAL EXPLANATIONS:

WHAT WOULD STRENGTHEN THIS:
WHAT WOULD WEAKEN THIS:
WHAT WOULD RULE THIS OUT:

LEAD RESPONSE BODY:
PROTECTION PATHWAY:

OPERATIONAL HISTORY:
ATTRIBUTION HISTORY:

LAST REVIEWED:
NEXT REVIEW:
REVIEW TRIGGER:
CORRECTION STATUS:
EXCLUSION REASON:
```

Not every field will be known.

Where information is genuinely missing, use the appropriate explicit status:

```text
UNKNOWN
NOT PUBLIC
NO EVIDENCE FOUND
WITHHELD / NCND
NOT APPLICABLE
```

Do not fill an evidentiary gap through inference.

For campaign relationships, remember:

```text
PATTERN ESTABLISHED
≠
COMMON OPERATOR ESTABLISHED

COMMON OPERATOR
≠
COMMON CUSTOMER

CRIMINAL OPERATOR
≠
NO STATE CUSTOMER

CRIMINAL OPERATOR
≠
STATE CUSTOMER

STATE AFFILIATION
≠
STATE DIRECTION
```

The template exists so those distinctions survive later updates.

---

## 📰 Timeline Reporting Rule

The reporting rule is:

> Preserve the event, the effect, the attribution, the pattern and the legal question as separate evidentiary tracks.

Therefore:

```text
INCIDENT CONFIRMED
```

does not mean:

```text
ATTRIBUTION CONFIRMED
```

and:

```text
PATTERN CONFIRMED
```

does not mean:

```text
COMMON SPONSOR CONFIRMED
```

and:

```text
CIVILIAN INFRASTRUCTURE AFFECTED
```

does not mean:

```text
WAR CRIME CONFIRMED
```

The timeline becomes useful precisely because those distinctions remain visible.

---

## 🌌 Constellations

⏱️ 🇮🇷 🏗️ 🕸️ 📉 🚰 👾 — chronology; Iran war; essential infrastructure; attribution; cumulative disruption; operational technology; legal review.

## ✨ Stardust

timeline, iran, irgc, cyber incidents, critical infrastructure, attribution, operational technology, water, wastewater, public data, banking, health, transport, campaign pattern, industrial control systems, war crimes, international humanitarian law

---

## 🏮 Footer

*⏱️ Timeline Of Essential Infrastructure Attacks* is a living node of the **Polaris Protocol**.  
It provides the chronological evidentiary spine for the *🇮🇷 Data Wars: IRGC Edition* pack, preserving incident, effect, attribution, pattern and legal significance as related but distinct questions.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope and inclusion rules*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *graded attribution*
> - [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md) — *source and confidence method*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *pattern analysis*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *OT depth, control access, and physical-process effects*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *layered tasking and ultimate sponsorship*
> - [🏥 Health, Education And Admin Are Not Soft Extras](./🏥_health_education_and_admin_are_not_soft_extras.md) — *civilian functions, data integrity, and person-centred recovery*
> - [🇬🇧 Britain Is Advertising An Exploitable Seam](./🇬🇧_britain_is_advertising_an_exploitable_seam.md) — *institutional ownership, fragmented response, and protection pathways*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *IHL routing for cyber operations affecting civilian and specially protected infrastructure*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *reporting discipline under evolving attribution*
> - [📊 Timeline CSV](./📊_iran_war_essential_infrastructure_cyber_timeline.csv) — *structured working dataset*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-09_
