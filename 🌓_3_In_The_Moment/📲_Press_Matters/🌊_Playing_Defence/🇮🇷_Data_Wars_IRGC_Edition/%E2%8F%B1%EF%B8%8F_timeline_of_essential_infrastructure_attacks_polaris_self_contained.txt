# ⏱️ Timeline of Essential Infrastructure Attacks
**First created:** 2026-08-01 | **Last updated:** 2026-11-18  
*An evidence-graded chronology of essential-infrastructure incidents, disruptions, advisories and attribution developments in the context of the Iran war.*

---

## 🧾 Editorial review status — 18 November 2026

**Scope of this revision:** October incident-body entries have been replaced by the 27 reconciled 40-column CSV records, and source-qualified November staging findings have been integrated as individually labelled entries. Earlier chronology remains intact. This is a **Markdown integration**, not yet a synchronised CSV/XLSX release; November 1–11 coverage remains incomplete.

**Reconciliation position:** 28 original October CSV entries → 27 integrated October entries after merging two follow-up duplicates and splitting one mixed-provider entry. November staging has 13 tracked entries, including contextual exclusions and a research gap; it is **not** a census of November attacks. The interval **1–11 November remains incompletely audited**. These are editorial record counts, not incident or attack rates. October entries are integrated below; the 40-column CSV and XLSX master files have not been synchronised.

### 📚 Source provenance and evidentiary grades

| Provenance class | Examples and treatment |
|---|---|
| **Direct agency / operator original** | Unit 42 Blinder Tunnel report (research attribution); FBI–Secret Service FortiBleed advisory; Cloudflare 15 October incident pages; Google Cloud London status; FAA 13 November notice; FBI ARTEX FLASH. Preserve source date, the assessor's confidence, and whether the source describes earlier activity. |
| **Operator statement reproduced by a third party** | Stripe-origin Revolut Pay and Adyen-origin Eftpos status updates; original provider incident permalinks were not recovered. Attribute these as *archived operator messages*, not independently opened provider pages. |
| **Attributed reporting of an operator / agency statement** | Some November United, JPMorgan, Apple and NSA developments. Preserve the named speaker and intermediary publisher; do not promote this to direct technical postmortem evidence. |
| **Retrospective disclosure / attribution** | CenterPoint's October disclosure of a September breach; later reported French-government attribution of refrigeration-controller compromises. Record the attribution/disclosure date separately from attack onset. |
| **Unresolved or partial** | PayByBank-specific notice, direct Vicksburg municipal permalink, exact Microsoft 365 incident ID, individual November Cloudflare incident permalinks, and several final recovery times. Keep unknowns explicit. |

**A/B/C reading aid:** A = evidenced malicious activity; B = operational disruption without established malicious cause; C = advisories, vulnerabilities or protective developments. This supplementary label does not replace the existing traffic lights, incident-depth fields or attribution assessments. **No common October–November Iranian operator or campaign is established by this staging evidence.**

### 🛠️ Recovery and continuity register — selected confirmed or qualified developments

| Event | Recovery / operational-control information | Evidence limit |
|---|---|---|
| **Vicksburg (1 Oct)** | City shut down computer systems following ransomware; utilities and emergency response continued. A 27 October update anticipated utility-payment processing resuming 30 October, subject to testing. | An anticipated date is not proof of completed restoration; direct original municipal statement URL still not preserved in staging. |
| **Ahold Delhaize (11 Oct)** | Precautionary systems response; stores remained open; 19 October reporting/update belongs to the parent incident. | Do not count protective shutdown or follow-up as new attacks. |
| **US Bankruptcy Noticing Center (15 Oct disclosure)** | Service restart 26 October and restoration reported 27 October; legal/notice workarounds preceded recovery. | Notice dates reaching back to 7 October do not establish intrusion onset. |
| **Cloudflare London (15 Oct)** | Resolved 17:46 UTC after a 17:33 UTC start. | Regional service effects, not a proven malicious attack. |
| **Cloudflare eastern North America (15 Oct)** | Customer impact ceased by 21:24 UTC; incident resolved 21:38 UTC (opened 20:48 UTC). | Distinct from London and from Workers Cron Triggers on 16 October UTC. |
| **Google Cloud London / Revolut (20 Oct)** | Physical electrical failure; downstream banking and payment effects. Revolut's 13 November postmortem reports failed backup takeover. | Different institutions' effects are not interchangeable; no cyber cause established for the power failure. |
| **Adyen / Australian Eftpos (20 Oct)** | Archived Adyen-origin notice reports external Eftpos planned maintenance and subsequent resolution. | Not established as Google Cloud downstream impact or Adyen compromise. |
| **FAA (13 Nov)** | Precautionary nationwide ground stop lifted 20:15 ET; FAA reported no indication of cyberattack. | Technical investigation is not an attribution finding. |
| **Workday WD1 (13–14 Nov)** | Institutional notice reports production maintenance following a disaster-recovery environment problem and availability restored on 14 November. | Direct Workday global postmortem and total tenant count outstanding. |
| **AWS US-EAST-1 (15 Nov)** | AWS reported most authentication recovery by 05:20 PST and mitigation of last affected load-balancer cell by 06:21 PST. | Service effects do not establish malicious cause. |

### 🔗 Evidence and navigation

The October reconciliation, November source checks and cross-cluster review were **editorial working materials**, not required companion nodes. Their findings and qualifications are incorporated directly into this chronology, including the corrections history below. They are deliberately **not linked as repository files**.

For individual incidents, consult the original operator, agency, technical-research and attributed-reporting sources cited in the relevant entries. The standing Polaris pack navigation is retained in the footer.

### 🧷 Corrections history — October/November Markdown integrated

| Date recorded | Correction or qualification | Status in this document |
|---|---|---|
| 18 Nov | Merge French refrigeration-controller follow-up into parent; preserve **9 Nov reported French-government IRGC attribution** as later attribution, not contemporaneous proof. | Integrated in October record; correction history retained here. |
| 18 Nov | Merge 19 Oct Ahold Delhaize follow-up into 11 Oct parent. | Integrated in October record. |
| 18 Nov | 6 Oct Blinder Tunnel = Unit 42 **publication** concerning earlier activity; Iranian nexus assessed by researchers, specific group unresolved. | Integrated in October record. |
| 18 Nov | 6 Oct FortiBleed = FBI–Secret Service continuing-threat advisory, **not** newly discovered October vulnerability. | Integrated in October record. |
| 18 Nov | ConnectWise discovered 14 Oct; 19 Oct is follow-up. eMudhra weak CA keys were a script issue, not proven hostile key theft. | Integrated in October record. |
| 18 Nov | Google Cloud London outage was electrical; Revolut/Stripe payment effects distinct from Adyen/Eftpos external maintenance. | Integrated in October record. |
| 18 Nov | Separate two 15 Oct Cloudflare regional events; Workers Cron incident belongs to 16 Oct UTC. | Integrated in October record. |
| 18 Nov | CenterPoint underlying breach belongs to September; October SEC disclosure is retrospective. | Integrated in October record. |
| 18 Nov | SafePay, GitLab and ARTEX publications are advisories, not evidence of new attacks on publication dates. | Integrated in October record. |
| 18 Nov | November FAA, United, JPMorgan, NSA, Apple, AWS, Workday and Cloudflare events require distinct cause/recovery fields; do not aggregate as a campaign. | Source-qualified November records integrated. |

**Publication gate:** the October and November Markdown sections have been integrated. Finish the 1–11 November source audit and resolve outstanding operator identifiers where possible before treating November as comprehensive; synchronise the original master CSV/XLSX in a separate controlled step. Do not silently change confidence or attribution fields by analogy.

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

A single confidence label is not sufficient.

The timeline attaches confidence to the **specific proposition being made**.

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

### Event-Type Rule

This chronology records more than attacks. Each new entry should identify what kind of event changed the public record:

```text
INCIDENT
→ a reported compromise, disruption, theft, manipulation, or other operation

ACTOR CLAIM
→ a statement of responsibility requiring separate validation

ATTRIBUTION UPDATE
→ a change in an official, intelligence, investigative, or public assessment

DEFENSIVE ADVISORY
→ a warning about exposure or active threat; not proof that an incident occurred

CHARGING / ENFORCEMENT EVENT
→ an allegation or legal action; not a conviction and not automatically a wartime event

PREPAREDNESS / GOVERNANCE EVENT
→ a mitigation, response, inventory, ownership, or accountability development
```

The event type must not inherit the evidentiary status of another category.

So:

```text
WARNING
≠
COMPROMISE

CLAIM
≠
ATTRIBUTION

CHARGE
≠
PROOF

PREPAREDNESS RESPONSE
≠
NEW ATTACK
```

---

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

## 2026-07-30 — Attribution Assessment Strengthens

### 🇺🇸 United States — Minnesota

### What changed

Reporting citing US and state officials said investigators believed the Minnesota attack was **probably** the work of Iranian hackers, while explicitly preserving that the assessment was preliminary and could change.

Separately, WIRED reported that a WaterISAC communication, drawing on Minnesota Fusion Center information, linked the Minnesota attacks to Iranian-affiliated activity.

### Attribution source type

```text
REPORTED INVESTIGATIVE ASSESSMENT
+
STATE / FUSION-CENTRE-LINKED INFORMATION
```

### Formal public attribution

Not established.

### Attribution confidence

🟡 **Probable at Minnesota-cluster level**, subject to continuing investigation.

### Rival explanations

Officials and reporting preserved the possibility of deliberate Iranian mimicry / false flag, multiple operators, or exploitation of the same exposed technology by unrelated actors.

### Sources

- New York Times reporting, 30 July 2026
- WIRED, 30 July 2026
- Minnesota IT Services, 28 July 2026

---

## 2026-07-31 — Presidential Position Diverges

### 🇺🇸 United States

President Trump publicly said he did not think Iran was responsible for the Minnesota cyberattack.

This should be recorded as:

```text
POLITICAL PUBLIC POSITION
```

not as:

```text
FORMAL TECHNICAL OR LAW-ENFORCEMENT ATTRIBUTION
```

### What changed

The public record now contained a visible disagreement between:

```text
reported investigative / intelligence assessment
```

and:

```text
presidential public position
```

The FBI had not publicly issued a definitive attribution.

### Methodological significance

This is a high-value attribution-governance event.

It demonstrates why the timeline must preserve:

```text
WHO BELIEVES WHAT
+
ON WHAT BASIS
+
WHETHER IT IS FORMAL
+
WHETHER IT IS PUBLIC
```

rather than giving the United States one undifferentiated attribution field.

---

## 2026-08-01 — 2026-08-07 — Reported Intelligence Assessment Becomes Materially Stronger

### 🇺🇸 United States — widening water campaign

As the known footprint widened beyond Minnesota, high-quality reporting described US intelligence agencies as assessing Iranian responsibility with substantially greater confidence than the formal public record reflected.

Reporting on the widening campaign described officials familiar with the assessment as saying the intelligence agencies believed Iranian actors were highly likely responsible.

### Attribution source type

```text
REPORTED INTELLIGENCE ASSESSMENT
```

### Formal public attribution

Still not established in the reviewed public FBI / CISA / NSA / EPA record.

### Presidential position

Still materially inconsistent with the reported intelligence assessment.

### Current attribution position

The pack should therefore distinguish:

```text
MINNESOTA / CORE WATER WAVE:
🟡 PROBABLE IRANIAN / IRAN-LINKED RESPONSIBILITY
based on reported investigative and intelligence assessments

FORMAL PUBLIC FEDERAL ATTRIBUTION:
⚪ NOT ESTABLISHED

EVERY INCIDENT IN THE WIDER MULTI-STATE WAVE:
⚪ / 🟠 / 🟡 AS SUPPORTED INDIVIDUALLY
```

A stronger assessment of the central wave must not automatically attribute every later or adjacent incident to the same operator or sponsor.

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

This label refers to recurrence of related water / wastewater OT activity.

It does **not** mean Iranian sponsorship has been established for every incident.

### Iran-war relevance

**High.**

### IHL / protected-infrastructure relevance

**Review warranted.**

```text
WATER CAMPAIGN ESTABLISHED
≠
IRANIAN RESPONSIBILITY ESTABLISHED
≠
IHL VIOLATION ESTABLISHED
≠
WAR CRIME ESTABLISHED
```

---

## 🌊 2026-08-06 onward — Criminal Activity Does Not Collapse The State Question

The same wartime environment also contains strongly evidenced criminal campaigns against US essential and systemically important organisations.

The BlackFile / UNC6671 vishing and extortion activity is presently better explained as financially motivated cybercrime than as Iranian state activity.

That does not contradict a probable Iran-linked assessment for the central water wave.

It demonstrates a different point:

```text
WAR
→ MORE HOSTILE STATE ACTIVITY

WAR
→ MORE HACKTIVIST ACTIVITY

WAR
→ MORE CRIMINAL OPPORTUNITY

WAR
→ MORE COPYCATS AND ACCESS TRADING
```

The timeline should therefore preserve **wave identity** rather than forcing every incident into one sponsor.

See [🌊 Riding Every Wave](./🌊_riding_every_wave.md).

---

## 🏥 2026-07-26 onward — AnMed Healthcare Disruption And Extortion

### 🇺🇸 United States — South Carolina and Georgia

AnMed identified a malware-related cyber incident on 26 July.

The health system initially closed most of its facilities, postponed some appointments and elective procedures, and operated through downtime and recovery procedures while restoring records, communications, imaging, and other clinical services.

On 11 August, AnMed's Facebook page displayed repeated ransom demands purporting to come from **The Gentlemen** ransomware group.

AnMed removed the unauthorised material and said the claims had not been verified.

```text
HEALTHCARE DISRUPTION:
🟢 ESTABLISHED

THE GENTLEMEN RESPONSIBILITY:
🟡 PROBABLE

CRIMINAL / EXTORTION MOTIVE:
🟡 PROBABLE

CLAIMED DATA VOLUME AND CONTENT:
🟠 SUSPECTED / UNVERIFIED

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Sources

- [HIPAA Journal — AnMed service disruption](https://www.hipaajournal.com/anmed-closes-almost-80-facilities-while-it-grapples-with-cyberattack/)
- [The Record — ransomware group hijacks AnMed's Facebook page](https://therecord.media/ransomware-group-hijacks-hospital-facebook-amid-cyberattack-response)
- [WYFF4 — AnMed response](https://www.wyff4.com/article/anmed-response-cyberattack-facebook-post-hackers/73406207)

---

## 🚚 2026-07-29 onward — CEVA Logistics Warehouse Disruption

### 🇪🇺 Europe — private transport and logistics

A cyberattack beginning around 29 July affected contract-logistics operations at eight CEVA Logistics warehouses in Europe.

Public reporting described shipment delays and later confirmed that some customer delivery information had been exposed.

It does not currently establish compromise of port-control systems, transport OT, deliberate targeting of military logistics, or an Iranian connection.

```text
OPERATIONAL LOGISTICS EFFECT:
🟢 ESTABLISHED

DATA EXPOSURE:
🟢 ESTABLISHED in affected customer reporting; full scope developing

ATTRIBUTION:
⚪ OPEN

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Sources

- [TechCrunch — CEVA breach](https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/)
- [FreightWaves — warehouse disruption](https://www.freightwaves.com/news/cyberattack-on-ceva-logistics-warehouses-in-europe-impacts-retailers)
- [SecurityWeek — CEVA operations disrupted](https://www.securityweek.com/ceva-logistics-operations-disrupted-by-cyberattack/)

---

## 🏛️ 2026-08-07 — 2026-08-11 — Suisun City Public-Safety And Administrative Disruption

### 🇺🇸 United States — California

Malicious software compromised Suisun City's IT systems on 7 August.

The city shut down its network to contain the incident and preserve evidence for a federal investigation.

The disruption affected 911 routing, police and fire dispatch, records, and ordinary city services.

Emergency calls were rerouted through Solano County while police and fire responses continued.

On 11 August, the city council met in closed session to consider a demand from the perpetrators.

```text
PUBLIC-SAFETY / ADMINISTRATIVE DISRUPTION:
🟢 ESTABLISHED

PERPETRATOR DEMAND:
🟢 ESTABLISHED as an event considered by the city council

CRIMINAL / EXTORTION EXPLANATION:
🟠 SUSPECTED / DEVELOPING

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Sources

- [San Francisco Chronicle — initial attack](https://www.sfchronicle.com/bayarea/article/cyberattack-suisun-city-22380837.php)
- [San Francisco Chronicle — city council considers demand](https://www.sfchronicle.com/bayarea/article/suisun-city-cyberattack-demand-22384401.php)

---

## 🏘️ 2026-08-12 — Darlington County Systems Taken Offline

### 🇺🇸 United States — South Carolina

Darlington County disclosed a cybersecurity incident affecting computer systems and limiting some county services.

Officials took systems offline, engaged external cybersecurity specialists and law enforcement, and began restoration work.

Emergency services and 911 remained operational.

```text
INCIDENT AND SERVICE EFFECT:
🟢 ESTABLISHED

ATTRIBUTION:
⚪ OPEN

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Sources

- [News and Press — Darlington County statement](https://www.newsandpress.net/darlington-county-issues-statement-on-cybersecurity-incident/)
- [WMBF — limited services](https://www.wmbfnews.com/2026/08/12/cybersecurity-incident-limits-some-services-darlington-county/)
- [WPDE — investigation and service effects](https://wpde.com/news/local/darlington-co-investigating-cybersecurity-incident-affecting-some-services-county-computer-systems-darlington-county-administrator-marion-charles-stewart-iii-911-communications-center)

---

## 📣 2026-08-12 — 2026-08-15 — APT IRAN And CyberAv3ngers Claim Minnesota

An account using the name **APT IRAN** reportedly said on Telegram that the Minnesota water operation had been conducted jointly with CyberAv3ngers.

Minnesota IT Services and the FBI said they were aware of the posts but did not validate them publicly.

```text
ACTOR CLAIM:
📣 ESTABLISHED AS A CLAIM

PRIOR CYBERAV3NGERS--IRGC RELATIONSHIP:
🟢 ESTABLISHED IN PRIOR US GOVERNMENT ATTRIBUTION

MINNESOTA / CORE-WAVE IRAN-LINKED ASSESSMENT:
🟡 PROBABLE / STRENGTHENED

FORMAL PUBLIC ATTRIBUTION OF THE CURRENT CAMPAIGN:
⚪ NOT IDENTIFIED

FORENSIC VALIDATION OF THE CLAIM:
NOT PUBLIC / NOT ESTABLISHED IN THE REVIEWED RECORD
```

### Sources

- [KSTP — claim reporting](https://kstp.com/kstp-news/top-news/hacking-group-linked-to-iran-claims-responsibility-for-cyberattack-on-minnesota-water-systems-report-says/)
- [McCrary Institute Threat Beat briefing](https://www.linkedin.com/pulse/cyber-briefing-81226-au-mccrary-institute-7cfre)
- [CISA — prior IRGC-affiliated PLC activity](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)
- [CISA — 2026 Iranian-affiliated PLC exploitation](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)

---

## 🧬 2026-08-13 — Cl0p Windchill / FlexPLM Mass Extortion Campaign

Cl0p claimed data theft from nearly 50 organisations, including Shell, Philips, GE, and Fiserv.

Public reporting connected the mass-extortion activity to exploitation of PTC Windchill and FlexPLM.

```text
CL0P CAMPAIGN:
🟢 ESTABLISHED AS A MASS-EXTORTION CAMPAIGN

INDIVIDUAL DATA-THEFT CLAIMS:
🟠 / 🟡 / 🟢 AS SUPPORTED BY EACH ORGANISATION

ORGANISING MECHANISM:
🟡 PROBABLE SHARED-SOFTWARE EXPLOITATION

ESSENTIAL-SERVICE OPERATIONAL EFFECT:
NOT GENERALLY ESTABLISHED

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

The present evidence supports:

```text
shared vulnerability
→ scalable criminal access
→ cross-sector extortion
```

more strongly than:

```text
Iranian strategic selection
→ coordinated state-disruption campaign
```

### Sources

- [Reuters — Cl0p mass data-theft claims](https://www.reuters.com/legal/government/philips-shell-targeted-by-hacking-group-2026-08-13/)
- [PTC — Windchill / FlexPLM advisory](https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability)

---

## 2026-08-13 — 2026-08-18 — France Tax-Administration Breach And Response

### 🇫🇷 France

### Event type

Incident disclosure followed by preparedness and governance response.

### Sector

National tax administration / public finance / government data.

### Affected body

Direction générale des Finances publiques.

### What happened

The French Finance Ministry confirmed that an attacker had obtained illegitimate access to a tax-authority system in late June and had consulted and extracted data concerning individuals and businesses.

Later government reporting put the affected population at about 700,000 taxpayers.

On 18 August, France announced a wider vulnerability-testing and security response.

### Effect

```text
CONFIDENTIALITY LOSS:
🟢 CONFIRMED

SERVICE DISRUPTION:
NOT ESTABLISHED

RECORD MANIPULATION:
NOT ESTABLISHED

PERSON-CENTRED RECOVERY:
ONGOING
```

### Attribution

The sale of data and access provides a strong financially motivated criminal explanation.

```text
CRIMINAL MOTIVE:
🟡 PROBABLE

IRAN / IRGC CONNECTION:
⚪ NO EVIDENCE FOUND

COMMON OPERATOR WITH THE US WATER CAMPAIGN:
⚪ NO EVIDENCE FOUND
```

### Sources

- [Reuters — France confirms taxpayer-data theft](https://www.reuters.com/legal/litigation/french-taxpayers-data-stolen-cyber-attack-french-finance-ministry-says-2026-08-14/)
- [Reuters — France announces wider security response](https://www.reuters.com/world/france-use-ai-tools-test-cybsecurity-vulnerabilities-after-tax-agency-hacking-2026-08-18/)
- [Le Monde — taxpayers' data stolen](https://www.lemonde.fr/en/pixels/article/2026/08/14/french-taxpayers-data-stolen-in-hack-of-finance-ministry_6756510_13.html)

---

## 2026-08-17 — Connecticut Water-Sector Preparedness Disclosure

### 🇺🇸 United States — Connecticut

### Event type

Preparedness and governance event.

### What changed

Connecticut authorities described distributing federal mitigation guidance to community water systems after attacks in other states.

No Connecticut water-system attack was reported in the source.

The state also disclosed that it did not maintain a central inventory showing which local systems used the affected controller classes.

```text
CONNECTICUT INCIDENT:
⚪ NONE REPORTED

DEFENSIVE RESPONSE:
🟢 CONFIRMED

CENTRAL COMPONENT INVENTORY:
NOT HELD / NOT AVAILABLE TO THE STATE IN THE REPORTED FORM

IRAN ATTRIBUTION:
NOT APPLICABLE TO A NEW CONNECTICUT INCIDENT
```

### Source

- [CT Insider — Connecticut water preparedness and inventory gap](https://www.ctinsider.com/connecticut/article/connecticut-water-systems-cyberattack-controller-22374980.php)

---

## 2026-08-18 — Mabna Institute Superseding Charges

### 🇺🇸 United States / 🇮🇷 Iran

### Event type

Charging and attribution-history event.

### What happened

The US Department of Justice announced a superseding indictment charging 17 alleged members of the Iran-based Mabna Institute.

The charging announcement describes a campaign beginning in 2013 and continuing through at least 2017.

It alleges intrusions affecting universities, private-sector companies, US federal and state government agencies and NGOs, and says the university spearphishing campaign was conducted on behalf of the IRGC.

### Evidentiary status

```text
CHARGING EVENT:
🟢 CONFIRMED

ALLEGATIONS:
FORMALLY PLEADED / NOT PROVED BY THE ANNOUNCEMENT

HISTORICAL IRGC TASKING ALLEGATION:
🟢 CONFIRMED AS A US GOVERNMENT ALLEGATION

NEW 2026 WARTIME ATTACK:
❌ NOT ESTABLISHED

CONNECTION TO WATER, RANSOMWARE, LOGISTICS OR FRENCH TAX INCIDENTS:
⚪ NO EVIDENCE FOUND
```

### Source

- [US Department of Justice — 17 Mabna Institute members charged](https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary)

---

## 2026-08-19 — Active Threat To Siemens S7-Series Controllers

### 🇺🇸 United States — cross-sector critical infrastructure

### Event type

Defensive advisory and threat-surface expansion.

### What changed

CISA, NSA, FBI, Department of Energy, EPA and other federal partners warned of an **active threat** to Siemens S7-series PLCs across manufacturing, energy, water and wastewater, chemical, and food and agriculture facilities.

The advisory described the possibility of read-and-write access and consequences including disruption of critical processes, safety incidents, downtime, equipment damage, sensitive-data compromise and cascading effects.

### Evidentiary boundary

```text
ACTIVE THREAT:
🟢 OFFICIALLY WARNED

SPECIFIC COMPLETED INCIDENT:
NOT ESTABLISHED BY THE ADVISORY ALONE

ACTUAL SAFETY OR EQUIPMENT DAMAGE:
NOT ESTABLISHED BY THE ADVISORY ALONE

IRAN ATTRIBUTION:
⚪ NOT MADE IN THE ADVISORY
```

This changes the timeline from a narrow Rockwell water-controller problem into a broader shared-machinery warning.

It does not turn a defensive advisory into a new attack count.

### Sources

- [CISA — active threat to Siemens S7-series PLCs](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a)
- [Reuters — US warning concerning Siemens devices](https://www.reuters.com/world/us-warns-siemens-devices-can-be-hacked-amid-fears-iran-is-breaching-water-plants-2026-08-19/)

---

## 2026-08-19 — Public Executive Attribution Remains Unresolved

### 🇺🇸 United States

### Event type

Attribution-governance update.

### What changed

Federal officials continued to stop short of formally attributing the recent local water-system attacks to Iran.

President Trump had publicly rejected Iranian involvement on 31 July and instead blamed Minnesota without presenting evidence.

By 19 August, that divergence had remained unresolved in public for **19 days — nearly three weeks**.

```text
REPORTED INVESTIGATIVE / INTELLIGENCE ASSESSMENT:
IRANIAN INVOLVEMENT FAVOURED

ACTOR CLAIM:
APT IRAN / CYBERAV3NGERS CLAIM RECORDED

FORMAL FEDERAL ATTRIBUTION:
⚪ STILL ABSENT

PRESIDENTIAL POSITION:
PUBLICLY DIVERGENT SINCE 2026-07-31
```

Duration is not proof of Iranian responsibility.

It is evidence of an extended public executive-level uncertainty during an active domestic critical-infrastructure investigation.

### Source

- [Reuters — formal Iran attribution still absent](https://www.reuters.com/world/us-warns-siemens-devices-can-be-hacked-amid-fears-iran-is-breaching-water-plants-2026-08-19/)

---

## 🧩 Backfill — 2026-08-10 to 2026-08-17 — Manitoba Hospital Facilities Ransomware

### 🇨🇦 Canada — Manitoba

### Event type

Incident / recovery update.

### Sector

Healthcare / hospital facilities / physical-support infrastructure.

### Affected bodies

Health Sciences Centre Winnipeg and CancerCare Manitoba.

### What happened

Shared Health said ransomware discovered on **10 August 2026** affected the facilities-maintenance network supporting Manitoba's largest hospital and CancerCare Manitoba.

By **17 August**, central monitoring of heating, ventilation and cooling systems remained affected. Those systems continued operating under local monitoring.

The incident also affected physical-access administration: the hospital security office was closed and could not issue or update ID access cards.

Clinical care was reported as continuing.

The initial public review found no indication that personal health or financial information had been accessed.

### Operational depth

The incident reached networked systems supporting physical hospital operations.

It did **not** establish attacker control of HVAC processes themselves.

The supported distinction is:

```text
CENTRAL FACILITY MONITORING:
🟢 AFFECTED

LOCAL HVAC OPERATION:
🟢 CONTINUED

PHYSICAL-ACCESS ADMINISTRATION:
🟢 DEGRADED

CLINICAL CARE:
REPORTED CONTINUING

ATTACKER MANIPULATION OF HVAC SETTINGS:
⚪ NOT ESTABLISHED
```

### Attribution confidence

```text
RANSOMWARE:
🟢 CONFIRMED BY AFFECTED AUTHORITY

SPECIFIC OPERATOR:
⚪ OPEN

STATE SPONSOR:
⚪ OPEN

IRAN / IRGC CONNECTION:
⚪ NO PUBLIC EVIDENCE FOUND
```

Straightforward financially motivated ransomware is presently the stronger explanation.

### Pattern significance

This is a useful cyber-to-physical comparator.

It shows that network compromise can reach systems supporting temperature control and physical access inside protected healthcare infrastructure without sharing the operator, sponsor or method of the U.S. water campaign.

### Sources

- [Shared Health — ransomware incident update](https://sharedhealthmb.ca/news-releases/2026-08-14-ransomware-incident-update/)
- [CityNews Winnipeg — recovery position one week after discovery](https://winnipeg.citynews.ca/2026/08/17/health-sciences-centre-winnipeg-ransomware-attack-update/)


---

## ⚡ 2026-08-23 — UK Power Generator Shutdown Disclosed

### 🇬🇧 United Kingdom

### Event type

Incident disclosure.

### Sector

Energy / electricity generation / operational technology.

### What happened

British reporting disclosed that a cyberattack had forced a small-scale UK power generator offline for **four days in July 2026**.

The facility has not been publicly identified.

Officials said the site was too small to threaten the wider electricity system and no national-grid-level effect occurred.

The government briefed energy-sector chief executives and issued guidance after the incident.

### Operational effect

This was a real cyber-induced interruption of physical energy generation.

```text
FACILITY SHUTDOWN:
🟢 CONFIRMED IN PUBLIC REPORTING

DURATION:
FOUR DAYS

NATIONAL GRID DISRUPTION:
❌ NOT REPORTED

CASCADING FAILURE:
❌ NOT REPORTED
```

### Attribution confidence

Multiple reports described the attackers as **Iran-linked**.

The NCSC had not publicly issued a formal technical attribution naming Iran, the IRGC or a specific Iranian group in the reviewed record.

```text
IRAN-LINKED ASSESSMENT:
🟠 / 🟡 DEVELOPING

FORMAL PUBLIC NCSC ATTRIBUTION:
⚪ NOT IDENTIFIED

CYBERAV3NGERS-SPECIFIC ATTRIBUTION:
⚪ NOT ESTABLISHED
```

### Pattern significance

This materially widens the strongest wartime OT pattern:

```text
US water / wastewater disruption
→ broader PLC reconnaissance and capability development
→ UK electricity-generation disruption
```

The incident makes it harder to treat the July activity as merely one vulnerable American water-device ecosystem.

It supports scrutiny of a broader search for reachable Western operational technology where relatively limited compromises can create disproportionate political signalling.

### Sources

- [BBC — “Cyber attack shut down small power plant”](https://www.bbc.co.uk/news/articles/ce9793g34yvo)
- [The Guardian — Iran-linked hackers shut down UK power generator for four days](https://www.theguardian.com/technology/2026/aug/23/iran-linked-hackers-uk-power-generator-cyber-attack)
- [NCSC — UK organisations urged to bolster cyber resilience amid Iran conflict](https://www.ncsc.gov.uk/news/uk-organisations-urged-bolster-cyber-resilience-amid-iran-conflict)

---

## 🚰 2026-08-26 — CISA Quantifies The July Water Campaign At More Than 100 Systems

### 🇺🇸 United States — multi-state

### Event type

Campaign-scale disclosure / attribution update.

### Sector

Water and wastewater / operational technology.

### What changed

CISA publicly quantified the July activity at **more than 100 internet-exposed water and wastewater systems**.

The affected environment commonly involved PLCs connected directly through cellular modems.

This disclosure materially widened the public understanding of scale beyond the smaller number of individually reported utilities and states.

### Operational effect

Most systems did not suffer major interruption to water supply.

However, the wider campaign produced outages and operational disruption during response, and previously described incidents included interference with PLC behaviour, shutdown processes and alarms.

### Attribution confidence

Reporting citing senior U.S. officials said American intelligence considered Iran likely responsible for much of the opportunistic campaign.

Federal agencies still had not publicly attributed every incident in the July cluster to Tehran.

```text
CAMPAIGN SCALE:
🟢 100+ SYSTEMS PUBLICLY DISCLOSED

CORE IRAN-LINKED ASSESSMENT:
🟡 PROBABLE / MATERIAL

FORMAL ATTRIBUTION OF EVERY INCIDENT:
⚪ NOT ESTABLISHED
```

### Pattern significance

The useful model is no longer:

```text
several water utilities were hacked
```

It is:

```text
one essential-services sector
→ 100+ exposed OT systems encountered during a wartime campaign
→ repeated opportunity for access, learning, disruption and defensive-response observation
```

This strengthens **search behaviour** and **sector-scale reconnaissance** as analytical objects.

It does not eliminate the possibility that several actor populations exploited the same exposed technology.

### Sources

- [SecurityWeek — CISA: Over 100 internet-exposed water systems targeted](https://www.securityweek.com/cisa-over-100-internet-exposed-water-systems-targeted-in-july-cyberattacks/)
- [TechCrunch — CISA confirms hackers targeted over 100 US water systems](https://techcrunch.com/2026/08/26/cisa-confirms-hackers-targeted-over-100-us-water-systems-during-july/)

---

## 🧰 2026-08-26 — Micro-Comm Water-Technology Supplier Breach

### 🇺🇸 United States — Kansas / downstream water customers

### Event type

Incident / supply-chain comparator.

### Sector

Water-sector technology / SCADA / industrial-control supply chain.

### What happened

The FBI investigated a breach of **Micro-Comm**, a Kansas company supplying PLC and supervisory-control technology used by wastewater facilities.

Micro-Comm discovered the intrusion on **31 July**.

The Barracuda ransomware group later published what it claimed were approximately **850,000 files / 644 GB** of data.

### Operational effect

No public evidence established that the breach itself compromised operation of a downstream water utility.

Micro-Comm said customer passwords, credentials and information enabling its own remote access to devices were not stolen, and sensitive material in the affected files was encrypted.

Reporting nevertheless described references to government customers, a U.S. military facility, employee information and product diagrams.

### Attribution confidence

```text
CRIMINAL RANSOMWARE / EXTORTION:
🟡 STRONGLY FAVOURED

IRAN CONNECTION:
⚪ NO CREDIBLE PUBLIC EVIDENCE FOUND

RELATIONSHIP TO JULY WATER ATTACKS:
⚪ NOT ESTABLISHED
```

### Pattern significance

The incident adds a supply-chain layer without joining the arrows prematurely:

```text
industrial-control supplier compromised by crime
→ product / customer information potentially exposed
→ future infrastructure becomes easier for unrelated actors to understand
```

The original criminal need not know who later benefits from the information.

### Source

- [Reuters — Hack of water-sector supplier draws FBI scrutiny](https://www.reuters.com/world/hack-water-sector-supplier-draws-fbi-scrutiny-iran-linked-cyber-concerns-grow-2026-08-26/)

---

## 🧬 2026-08-26 — QTFY Disruption Demonstrates A Concurrent China-Linked Infrastructure Ecosystem

### 🇺🇸 United States

### Event type

Charging / enforcement / competing-actor comparator.

### Sectors

Government; energy; telecommunications; healthcare; defence-adjacent systems.

### What happened

The U.S. Department of Justice and FBI disrupted the **QScan** and **QTRouter** platforms operated by the China-linked group **QTFY**.

Authorities said QTFY targeted U.S. government agencies, power companies, telecommunications providers and major hospital systems.

DOJ identified victims including NASA, the Federal Reserve, the Departments of Energy, Justice and Health and Human Services, and NIH.

### Attribution confidence

U.S. authorities described QTFY as a PRC state-sponsored hacker-for-hire ecosystem linked to Nanjing Xinjiuwei Network Technology and customers including China's Ministry of State Security and People's Liberation Army.

### Pattern significance

This does **not** strengthen Iranian attribution.

It raises the cost of casual attribution from timing or sector alone.

The same U.S. infrastructure estate is being hunted simultaneously by:

```text
Iran-linked / suspected-Iran actors
+
China-linked state-contractor ecosystems
+
criminal ransomware / access markets
```

That actor density contaminates attribution by superficial resemblance.

### Sources

- [U.S. Department of Justice — seizure of QScan and QTRouter platforms](https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers)
- [FBI — QTFY disruption](https://www.fbi.gov/video-repository/fbi-and-doj-announce-botnet-disruption-082626.mp4/view)

---

## 🗃️ 2026-08-26 to 2026-08-27 — ATF Investigative System Breach

### 🇺🇸 United States

### Event type

Incident.

### Sector

Federal law enforcement / investigative administration.

### What happened

The Bureau of Alcohol, Tobacco, Firearms and Explosives confirmed a cyberattack on a standalone system containing information about targets of ATF investigations.

Senior Justice Department officials classified the compromise as a **major incident**.

The affected environment was disconnected.

ATF said its enterprise network, eForms, case-management and laboratory systems were not affected.

### Operational effect

No mission-wide outage was reported.

The principal risk is investigative compromise and possible exposure of sensitive law-enforcement information.

### Attribution confidence

Qilin listed ATF on its leak site.

ATF had not publicly attributed the breach to Qilin in the reviewed record.

```text
QILIN CLAIM:
📣 ACTOR-CLAIMED

QILIN RESPONSIBILITY:
🟠 SUSPECTED / DEVELOPING

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Pattern significance

The case strengthens the mixed-ecosystem model:

```text
wartime infrastructure probing
+
state-linked espionage
+
ransomware-as-a-service
→ overlapping institutional attack surface
```

---

## ✈️ 2026-08-27 — Manchester Airports Group Data Breach

### 🇬🇧 United Kingdom

### Event type

Incident disclosure.

### Sector

Transport / airport digital infrastructure.

### What happened

Manchester Airports Group disclosed a cyberattack compromising data belonging to approximately **8.7 million customers** across Manchester, London Stansted and East Midlands airports.

The stolen material included email addresses, phone numbers, vehicle registrations and postcodes associated with Wi-Fi, parking, lounges and Fast Track services.

### Operational effect

Flights, passenger safety and aviation security were reported as unaffected.

Some customer-facing booking functionality was temporarily affected.

### Attribution confidence

No responsible group had been publicly identified by MAG or UK authorities in the reviewed record.

```text
INCIDENT:
🟢 CONFIRMED

DATA EXPOSURE:
🟢 CONFIRMED

AVIATION-OPERATIONS EFFECT:
❌ NOT REPORTED

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Pattern significance

This adds a strategically important transport operator to the wider wartime attack surface while fitting data theft / extortion better than coercive OT disruption.

### Source

- [Manchester Airports Group — data security incident](https://www.manchesterairport.co.uk/help/data-security-incident/)

---

## 🏛️ 2026-08-28 — Berlin State Government Ransomware And Service Disruption

### 🇩🇪 Germany — Berlin

### Event type

Incident / attribution development.

### Sector

State government administration.

### What happened

Berlin treated its August network compromise as an extortion attack.

The Rhysida ransomware group claimed responsibility.

Berlin said data had left the networks of the departments responsible for mobility, transport, climate protection and environment, and urban development / housing.

Two departments had been disconnected from the state network on **14 August**.

### Operational effect

Housing-benefit applications and payments could not be processed while affected systems were isolated.

All Senate departments were reconnected by **23 August**.

Berlin said infrastructure for the **20 September state election** was not affected.

### Attribution confidence

```text
RHYSIDA CLAIM:
📣 ESTABLISHED

RHYSIDA RESPONSIBILITY:
🟡 PROBABLE

STATE SPONSOR:
⚪ NOT ESTABLISHED

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Pattern significance

Berlin provides a clear example of ordinary ransomware disabling public administration during the same period as suspected Iranian OT activity.

The target sector and timing therefore cannot carry attribution by themselves.

### Source

- [Reuters — Berlin says it will not submit to extortion](https://www.reuters.com/world/berlin-city-government-says-it-wont-submit-extortion-after-pre-election-2026-08-28/)

---

## 🤖 2026-09-01 — AI-Assisted Scaling Of Iran-Aligned OT Activity

### 🇺🇸 United States / 🇬🇧 United Kingdom / wider Western OT environment

### Event type

Capability-development / threat-method update.

### Sector

Energy / industrial control / operational technology.

### What changed

Reuters reported that Iranian-aligned actors were using AI-generated or AI-assisted scripts against operational-technology assets, including PLCs used in power generation and substations.

The reporting described AI as reducing some of the expertise required to identify, sort and interact with vulnerable industrial systems.

### Operational effect

No new physical outage was attributed specifically to these scripts in the reporting.

The significance is scaling:

```text
mass discovery
→ AI-assisted target sorting
→ reusable protocol interaction
→ more operators able to attempt OT intrusion
```

### Attribution confidence

```text
IRAN-ALIGNED USE OF AI-ASSISTED OT TOOLING:
🟡 / 🟢 CREDIBLY REPORTED

ATTRIBUTION OF EVERY AI-ASSISTED OT ATTACK TO IRAN:
❌ NOT SUPPORTED
```

### Pattern significance

Lowering the skill threshold increases expected attack volume.

It simultaneously makes technique resemblance **less** probative of sponsorship because copied or generated tooling can converge across hacktivists, criminals, contractors and states.

### Source

- [Reuters — Energy firms face AI-enhanced cyber attacks](https://www.reuters.com/business/energy/energy-firms-face-ai-enhanced-cyber-attacks-connectivity-push--reeii-2026-09-01/)

---

## 🏥 2026-08-31 to 2026-09-02 — Nutex Health Material Cybersecurity Incident

### 🇺🇸 United States

### Event type

Incident / materiality update.

### Sector

Healthcare / hospital administration / sensitive data.

### What happened

Nutex Health escalated its August cyber incident to an SEC Item 1.05 **Material Cybersecurity Incident**.

The company confirmed exfiltration of patient, employee, credentialed-provider, business and financial information and said the actor threatened publication.

### Operational effect

Nutex had not identified material disruption to hospital operations or financial-reporting systems.

The demonstrated effect is therefore data exfiltration and extortion exposure rather than interruption of clinical services.

### Attribution confidence

Reporting pointed toward **The Gentlemen** ransomware ecosystem.

Nutex itself had not publicly named the attacker in the reviewed record.

```text
CRIMINAL EXTORTION:
🟡 STRONGLY FAVOURED

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Pattern significance

Healthcare now contains several distinct mechanisms:

```text
Iran-linked medical-device disruption
+
criminal hospital-data extortion
+
unattributed hospital operational disruption
```

One sector does not imply one campaign.

---

## 🏥 2026-09-01 to 2026-09-04 — Luminis Health Operational Disruption

### 🇺🇸 United States — Maryland

### Event type

Incident.

### Sector

Healthcare / hospital operations.

### What happened

Luminis Health disclosed a cyberattack affecting systems across its network, including Anne Arundel Medical Center and Doctors Community Medical Center.

By **3 September**, some systems remained unavailable.

Non-critical ambulances were being diverted and at least some treatment had been cancelled or delayed.

Patient-facing systems including MyChart were also affected.

### Operational effect

```text
AMBULANCE DIVERSION:
🟢 CONFIRMED IN PUBLIC REPORTING

TREATMENT DELAY / CANCELLATION:
🟢 REPORTED

FULL EMERGENCY-CARE LOSS:
❌ NOT ESTABLISHED
```

### Attribution confidence

The attacker, intrusion vector, ransomware status and data-theft position remained publicly unresolved.

```text
ATTRIBUTION:
⚪ OPEN

IRAN CONNECTION:
⚪ NO SUPPORTING PUBLIC EVIDENCE IDENTIFIED
```

### Pattern significance

This strengthens the finding that healthcare cyber incidents are repeatedly affecting actual care delivery while attribution remains heterogeneous.

---

## 📡 2026-09-02 to 2026-09-05 — Reported Iranian Expansion Into Energy And Telecommunications

### 🇺🇸 United States

### Event type

Campaign / attribution update.

### Sectors

Telecommunications; energy; water; other critical infrastructure.

### What changed

Reporting citing U.S. government and industry threat information described increased attempts by Iranian government-linked hackers to compromise systems capable of affecting electricity, telecommunications and other critical infrastructure.

The activity remained concentrated on internet-exposed automated and control systems.

No major operational disruption was publicly attached to this new tranche.

### Attribution confidence

```text
CAMPAIGN-LEVEL IRANIAN GOVERNMENT LINK:
🟡 / 🟢 CREDIBLY REPORTED

ATTRIBUTION OF EACH ATTEMPT:
LOWER / CASE-SPECIFIC

NEW MAJOR OUTAGE:
❌ NOT ESTABLISHED
```

### Pattern significance

Telecommunications is the notable addition.

The developing model becomes:

```text
search for inexpensive, internet-reachable leverage
across
water + energy + telecommunications
```

rather than:

```text
one actor happens to like vulnerable water PLCs
```

A further technical question remains open: whether telecom targeting is simply another form of exposed automation-system exploitation or a separate carrier-network access campaign.

### Source

- [The National — Iran's cyber attack strategy is 'perfect weapon' against US](https://www.thenationalnews.com/future/technology/2026/09/02/iran-cyberattack-hack-us-infrastructure/)

---

## ⚖️ 2026-09-02 to 2026-09-03 — C-Track Court Platform Compromise Disclosed

### 🇺🇸 United States / 🇨🇦 Canada

### Event type

Incident disclosure / shared-provider compromise.

### Sector

Judiciary / court administration / government data.

### What happened

Thomson Reuters disclosed that an unauthorised actor obtained files from its **C-Track** court case-management platform.

Affected users included court systems in **11 U.S. states**, the U.S. Virgin Islands and Ontario.

The intrusion itself occurred in **March 2026** and was detected on **30 June**.

### Operational effect

C-Track remained operational and court services were not reported disrupted.

The information-security impact may be substantial because affected records contained personal information and reporting indicated that confidential, sealed or redacted material may have been implicated.

### Attribution confidence

```text
INCIDENT:
🟢 CONFIRMED

OPERATOR:
⚪ OPEN

IRAN CONNECTION:
⚪ NO PUBLIC EVIDENCE FOUND
```

### Pattern significance

This is a concentration-risk case:

```text
commercial platform
→ one compromise
→ multiple sovereign court environments exposed
```

A wartime adversary does not necessarily need to breach each public body separately when essential administration is concentrated in shared providers.

### Sources

- [Reuters — Thomson Reuters detects C-Track cybersecurity incident](https://www.reuters.com/legal/litigation/thomson-reuters-detects-cybersecurity-incident-says-unauthorized-party-accessed-2026-09-03/)
- [Ontario Courts — joint statement by Ontario's Chief Justices](https://www.ontariocourts.ca/en/public-statement-cybersecurity.htm)

---

## 🗃️ 2026-09-05 to 2026-09-08 — Berlin Stolen Data And Credentials Published

### 🇩🇪 Germany — Berlin

### Event type

Incident escalation / post-compromise exploitation risk.

### What changed

Berlin confirmed that data stolen in the August ransomware incident had been published.

A second package subsequently included login credentials.

Authorities established a central crisis response and tightened mitigations.

### Operational effect

The immediate service disruption had already occurred in August.

The new effect is persistence of risk after recovery:

```text
government compromise
→ data theft
→ public release
→ credentials released
→ phishing / credential reuse / follow-on access becomes cheaper
```

### Attribution confidence

Rhysida remained the principal criminal attribution.

Germany's BSI reportedly assessed associated initial-access activity as cybercriminal and had not established a state-sponsored or political connection.

### Iran-war relevance

Weak for attribution.

Strong for **secondary exploitation risk**.

A financially motivated criminal can manufacture reconnaissance and access material later consumed by unrelated actors.

### Sources

- [Reuters — Berlin launches crisis response after hackers publish stolen data](https://www.reuters.com/world/berlin-launches-crisis-response-after-hackers-publish-stolen-data-2026-09-05/)
- [Berlin government — second package and credentials published](https://www.berlin.de/rbmskzl/aktuelles/pressemitteilungen/2026/pressemitteilung.1710816.php)
- [Berlin Data Protection Authority — assessment of exposed data](https://www.datenschutz-berlin.de/datenschutz/hinweise-zum-hackerangriff-auf-berlin/)

---

## 🛠️ 2026-09-01 to 2026-09-09 — Stadtwerke Landsberg Utility Compromise Stopped At The IT / OT Boundary

### 🇩🇪 Germany — Bavaria

### Event type

Incident / resilience comparator.

### Sector

Electricity; water; wastewater; district heating; telecommunications.

### What happened

Stadtwerke Landsberg said it was hit overnight on **1 September** by a criminal cyberattack.

Attackers encrypted central corporate IT systems.

The utility disconnected internet links, shut affected systems down and began rebuilding with external forensic support.

### Operational effect

Normal telephony, email and customer-service processes were impaired.

Essential services remained operational:

- electricity distribution;
- drinking water;
- wastewater treatment;
- district heating;
- fibre infrastructure;
- EV charging.

### Attribution confidence

```text
CRIMINAL CYBERATTACK:
🟢 AFFECTED AUTHORITY ASSESSMENT

SPECIFIC RANSOMWARE GROUP:
⚪ OPEN

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Pattern significance

Landsberg is an unusually useful control case:

```text
enterprise IT compromise
→ central systems encrypted
→ administrative degradation
→ OT remains isolated
→ physical services continue
```

It demonstrates why the meaningful question is increasingly not merely:

> Can attackers penetrate utilities?

but:

> **Can compromise cross the IT / OT boundary and change service delivery?**

### Sources

- [Stadtwerke Landsberg — incident updates](https://www.stadtwerke-landsberg.de/presse/)
- [The Record — cyberattack encrypts systems at Bavarian municipal utility](https://therecord.media/cyberattack-bavaria-germany-utility)

---

## 📣 2026-09-08 to 2026-09-10 — APT IRAN Claims Texas Telecom And Water Disruption

### 🇺🇸 United States — Texas

### Event type

Actor claim / attribution caution.

### Sectors

Telecommunications; water.

### What happened

The Iranian-linked persona **APT IRAN** claimed that it had disrupted AT&T internet service across several Texas cities and penetrated an unnamed Texas water utility.

A real AT&T service outage occurred.

AT&T rejected the cyberattack claim and attributed the Dallas-area outage to attempted **physical cable theft**.

The claimed water utility had not been independently identified or confirmed in the reviewed public record.

### Evidentiary status

```text
APT IRAN CLAIM:
📣 CONFIRMED AS A CLAIM

AT&T OUTAGE:
🟢 REAL

APT IRAN CAUSATION OF AT&T OUTAGE:
❌ NOT SUPPORTED ON CURRENT EVIDENCE

COMPETING PHYSICAL CAUSE:
🟢 SUPPLIED BY AT&T

TEXAS WATER DISRUPTION CLAIM:
⚪ UNVERIFIED
```

### Pattern significance

This adds an information-operation problem to the technical one:

```text
real Iranian-linked cyber capability exists
→ actor publicly threatens sectors
→ unrelated outage occurs
→ actor claims it
```

During a genuine campaign, ordinary failure and physical sabotage can be harvested into a narrative of greater cyber reach.

Temporal correlation therefore becomes **less** probative without victim confirmation or technical evidence.

### Sources

- [Threat Beat — APT IRAN Texas claims](https://threatbeat.com/attacks-and-incidents/iran-hackers-claim-texas-att-outage-vow-to-intensify-attacks-before-9-11/)
- [FOX 26 Houston — AT&T rejects cyberattack claim and cites cable theft](https://www.fox26houston.com/news/iranian-hacker-group-claims-responsibility-dallas-internet-outage.amp)

---

## 🩺 2026-09-08 to 2026-09-11 — Veradigm Third-Party Credential And API Breach

### 🇺🇸 United States

### Event type

Incident / supply-chain identity compromise.

### Sector

Healthcare technology / clinical-support infrastructure.

### What happened

Veradigm disclosed that an attacker obtained credentials from one of its third-party vendors and used them to access a customer-service API.

Patient information was downloaded, including Social Security numbers in some cases.

### Operational effect

Veradigm said clinical services and its broader systems were not disrupted.

The stolen credentials were restricted to the affected API rather than the wider network, databases or servers.

### Attribution confidence

The Gentlemen claimed Veradigm on its leak site.

Veradigm had not publicly attributed the incident.

```text
THE GENTLEMEN CLAIM:
📣 ACTOR-CLAIMED

CRIMINAL EXTORTION:
🟡 STRONGLY FAVOURED

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

### Pattern significance

The attack path matters:

```text
third-party supplier
→ legitimate credential
→ authorised API
→ downstream healthcare data
```

Shared identity and service infrastructure can create cross-organisation exposure without breaching each provider directly.

### Source

- [BleepingComputer — Veradigm patient-data breach](https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/)

---

## ⚓ 2026-09-12 — Anthropic Discloses Iran-Nexus Reconnaissance Against U.S. Naval Systems

### 🇺🇸 United States / Middle East theatre

### Event type

Reconnaissance / capability-development disclosure.

### Sector

Defence / naval communications and control systems.

### What happened

Anthropic disclosed that an **Iran-nexus threat actor** used Claude between **December 2025 and August 2026** to develop targeting material concerning U.S. naval forces.

The actor combined ship and aircraft movement data, personnel information, satellite-imagery queries and public-source material with vulnerability research concerning maritime VSAT terminals, Cisco communications equipment and industrial-control products used in shipboard environments.

Anthropic disrupted the account and shared information with government authorities.

### Operational effect

No successful compromise, communications degradation or manipulation of a Navy control system was publicly established.

```text
TARGETED TECHNICAL RECONNAISSANCE:
🟢 DISCLOSED BY ANTHROPIC

SUCCESSFUL EXPLOITATION:
⚪ NOT ESTABLISHED

OPERATIONAL EFFECT:
⚪ NONE PUBLICLY CONFIRMED
```

### Attribution confidence

```text
IRAN-NEXUS ACTOR:
🟡 / 🟢 MODERATE-TO-STRONG PLATFORM ASSESSMENT

NAMED IRGC UNIT:
⚪ NOT IDENTIFIED

DIRECT STATE COMMAND:
⚪ NOT ESTABLISHED
```

### Pattern significance

This adds targeted military reconnaissance to a picture previously dominated by opportunistic civilian OT:

```text
military OSINT
→ asset tracking
→ named equipment families
→ vulnerability catalogue
→ possible exploitation planning
```

Researching a vulnerability is not exploiting it.

The distinction remains essential.

### Source

- [Anthropic — Countering misuse of AI: September 2026](https://www.anthropic.com/threat-intelligence-report-september-2026)

---

## 🤖 2026-09-09 to 2026-09-14 — AI-Orchestrated PaperCut Mass Compromise

### 🌍 United States / United Kingdom / Canada / France / Germany and others

### Event type

Cross-sector mass compromise / access-ecology comparator.

### Sectors

Education; government; healthcare; manufacturing; energy / utilities; finance.

### What happened

GreyNoise disclosed that a likely Russian-speaking operator used hundreds of AI agents to exploit two PaperCut NG/MF vulnerabilities.

The campaign began on **31 August** and compromised at least **440 servers belonging to 395 organisations in 48 countries**.

GreyNoise reported credential harvesting at 280 victims, operating-system or domain secrets at 147, and full domain-administrator control at 12.

Education dominated the victim set, but government, healthcare, industrial / energy / utility and financial organisations were also affected.

### Operational effect

No widespread essential-service outage was established.

The significant effect was **access generation at scale**.

GreyNoise said it remained unclear whether the actor intended to exploit the accesses itself or transfer them to affiliated actors for ransomware, data theft or other follow-on activity.

### Attribution confidence

```text
LIKELY RUSSIAN-SPEAKING OPERATOR:
🟡 GREYNOISE ASSESSMENT

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND

IRAN AS AVOIDED COUNTRY IN OPERATOR CONFIGURATION:
REPORTED BY GREYNOISE
```

### Pattern significance

This is not evidence for Iranian sponsorship.

It materially strengthens the operator/customer problem:

```text
AI-orchestrated exploitation
→ hundreds of privileged footholds created rapidly
→ access can potentially be transferred
→ original intruder may differ from eventual operator / customer
```

Attribution therefore increasingly needs to ask:

```text
WHO FOUND THE DOOR?
WHO OPENED IT?
WHO BOUGHT THE ACCESS?
WHO USED IT?
WHO CHOSE THE OBJECTIVE?
```

Those may be different actors.

### Source

- [GreyNoise — Agents Gone Wild: An AI-Orchestrated Global Campaign Against PaperCut NG/MF](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf)

---

## 🧭 Pattern Shift By 14 September 2026

The post-20-August record materially changes the pack.

The strongest current picture is no longer simply:

```text
Iran-linked water attacks
+
background cybercrime
```

It is:

```text
IRAN-LINKED / SUSPECTED-IRAN OT ACTIVITY
→ 100+ water-sector systems encountered
→ physical water-control effects in part of the campaign
→ reported expansion into energy and telecommunications
→ UK power-generation shutdown
→ AI-assisted scaling
→ targeted naval technical reconnaissance

PLUS

OTHER STATE-LINKED ACTIVITY
→ China-linked contractor / hacker-for-hire infrastructure
→ overlapping government, energy, telecom and healthcare targets

PLUS

CRIMINAL ACCESS AND RANSOMWARE ECOSYSTEMS
→ hospitals
→ government administration
→ airports
→ industrial suppliers
→ shared software
→ third-party credentials

PLUS

ACCESS-GENERATION AND DATA-LEAK EFFECTS
→ credentials
→ diagrams
→ court records
→ administrative data
→ privileged footholds
→ information that unrelated later actors can consume
```

### 1. The Iran-facing infrastructure pattern has widened

The strongest Iran-facing sequence now runs:

```text
exposed U.S. water PLCs
→ multi-state operational disruption
→ 100+ water / wastewater systems encountered
→ broader Siemens / multi-vendor OT preparation
→ UK energy-generation shutdown
→ reported U.S. energy + telecom targeting
→ AI-assisted scaling
→ targeted U.S. naval communications / ICS reconnaissance
```

That is materially broader than one water-device family.

### 2. Common-sponsor confidence must not rise merely because actor density rises

The same period contains strongly evidenced Chinese state-linked contractor activity and conventional ransomware / access-market activity.

Therefore:

```text
MORE INCIDENTS
≠
MORE EVIDENCE FOR ONE SPONSOR
```

In several parts of the dataset, the opposite is true.

More simultaneous operators make attribution from timing, sector and copied technique less reliable.

### 3. Criminal activity can manufacture future strategic opportunity

Micro-Comm, Berlin, Veradigm, C-Track and PaperCut illustrate different routes by which one compromise can lower the cost of later operations:

```text
customer / product information
credentials
shared-platform access
API identities
domain-admin footholds
government records
```

The original intruder does not need to share a sponsor with the later user.

### 4. IT / OT segmentation is now empirically visible as a consequence boundary

The July U.S. water incidents and the UK generator shutdown demonstrate cyber activity reaching operational effects.

Landsberg demonstrates the opposite outcome:

```text
IT compromised
→ OT isolated
→ essential service continues
```

That makes segmentation a demonstrated resilience variable rather than an abstract recommendation.

### 5. AI affects both scale and attribution

AI-assisted OT scripts and the PaperCut campaign both point toward faster, cheaper capability diffusion.

That creates two simultaneous effects:

```text
attack volume can rise
+
technical resemblance can become less distinctive
```

The first increases defensive urgency.

The second raises the evidentiary bar for attribution.

### 6. Claims themselves are becoming part of the campaign environment

The APT IRAN / AT&T episode shows why actor claims need their own track.

A real outage can be opportunistically claimed even when the affected operator supplies a credible non-cyber cause.

Therefore:

```text
ACTOR CLAIM
≠
INCIDENT CAUSATION
```

remains a first-order rule, not a methodological nicety.

### 7. Cyber-to-physical recurrence is real; common sponsorship is not

By mid-September, network compromise has repeatedly touched:

- water-control systems;
- electricity generation;
- hospital facility monitoring;
- municipal utility enterprise environments;
- and systems capable of supporting physical access or control.

That establishes a broader **structural cyber-to-physical exposure problem**.

It does not establish one common campaign.

### 8. The strategic burden increasingly falls on defenders regardless of sponsor

Different threat ecosystems still draw on the same finite pool of:

- local operators;
- OT engineers;
- incident responders;
- federal investigators;
- healthcare administrators;
- public-sector IT teams;
- intelligence analysts;
- and public trust.

So the cumulative state-capacity effect can be real even where common command is absent.

---

## 📈 Campaign-Level Trend Since 28 February 2026

The current public record supports the following working findings:

```text
IRAN-LINKED / SUSPECTED-IRAN OT CAMPAIGN:
STRONGER AND BROADER THAN ON 20 AUGUST

FORMAL ATTRIBUTION OF EVERY INCIDENT:
NOT ESTABLISHED

CROSS-SECTOR CYBER-TO-PHYSICAL EXPOSURE:
STRONGLY ESTABLISHED AS A STRUCTURAL PROBLEM

MULTIPLE STATE-LINKED ECOSYSTEMS:
ESTABLISHED

CRIMINAL / RANSOMWARE / ACCESS-MARKET OVERLAP:
ESTABLISHED

SHARED-SPONSOR THEORY FOR THE WHOLE DATASET:
NOT SUPPORTED

AI-ASSISTED SCALING:
NOW MATERIAL

SUPPLY-CHAIN / SHARED-PROVIDER CONCENTRATION RISK:
INCREASINGLY VISIBLE

SECONDARY USE OF STOLEN ACCESS / DATA:
PLAUSIBLE AND IN SOME CASES STRUCTURALLY ENABLED;
CASE-SPECIFIC USE REQUIRES EVIDENCE
```

The central methodological rule therefore remains:

> **Preserve the event, the effect, the attribution, the pattern and the legal question as separate evidentiary tracks.**

And the September additions require two further questions:

> **Who created the access?**

and:

> **Who ultimately used or benefited from it?**

Those questions may not have the same answer.

---

---

## ⚓ 2026-08-07 to 2026-09-17 — Texas-Bound Energy Tankers And The Emerging Maritime Cyber Cluster

### 🌍 International maritime / 🇺🇸 United States-bound

### Event type

Incident disclosure / federal response / campaign-scale threat update.

### Sector

Energy transport / maritime operational technology.

### What happened

The U.S. Coast Guard and FBI have now publicly acknowledged that federal cyber teams boarded **two inbound foreign-flagged commercial energy vessels** in the Gulf of Mexico on **21 and 24 August** after indications that the networks of both vessels had been compromised.

Reporting identified the vessels as:

- **VL Prosperity**, a Liberian-flagged crude-oil tanker bound for Galveston, Texas;
- **Kohaku**, an LPG carrier heading towards Texas to load cargo.

The VL Prosperity incident appears to reach back to **7 August**, when Iranian state media reported that the vessel had suffered a cyberattack while crossing the Strait of Gibraltar.

That reporting alleged approximately 30 hours of communications loss and attacker access to propulsion, navigation and cargo systems.

Those deeper physical-control claims remain **unverified by the U.S. government in the reviewed public record**.

### Operational effect

The Coast Guard's public position is narrower than the Iranian reporting:

```text
NETWORK COMPROMISE INDICATORS:
🟢 ACKNOWLEDGED

FEDERAL CYBER / INSPECTION BOARDINGS:
🟢 CONFIRMED

OPERATIONAL DISRUPTION:
❌ NOT REPORTED BY THE COAST GUARD

VESSEL INSTABILITY:
❌ NOT REPORTED

CREW PHYSICAL DANGER:
❌ NOT REPORTED

ENVIRONMENTAL IMPACT:
❌ NOT REPORTED

PROPULSION / NAVIGATION / CARGO MANIPULATION:
🟠 ALLEGED / NOT PUBLICLY VERIFIED
```

### Attribution confidence

The U.S. is reportedly investigating whether Iran was responsible.

That is now materially different from saying the incidents are unrelated to Iran.

But it remains materially different from attribution.

```text
FOREIGN ACTOR / NETWORK-COMPROMISE PROBLEM:
🟢 PUBLICLY ACKNOWLEDGED

IRAN AS INVESTIGATIVE HYPOTHESIS:
🟠 CREDIBLE / DEVELOPING

FORMAL PUBLIC US ATTRIBUTION TO IRAN:
⚪ NOT ESTABLISHED

NAMED IRGC / MOIS UNIT:
⚪ NOT ESTABLISHED
```

### Pattern expansion

By **16–17 September**, reporting citing U.S. officials said federal agencies were tracking cyber threats involving **nearly 20 commercial vessels worldwide**.

The Coast Guard requested advance notice if those vessels intended to enter U.S. ports.

CISA separately said several commercial vessels had been targeted in potential cyberattacks in late August, while noting that attackers did not appear to have taken control of the targeted ships.

This changes the analytical object from:

```text
one strange tanker incident
```

to:

```text
two confirmed vessel-network compromise investigations
+
several commercial vessels reportedly targeted
+
nearly 20 vessels under particular US cyber-threat watch
```

It does **not** establish that those vessels share:

```text
one operator
one vulnerability
one vendor
one access broker
one customer
or one state sponsor
```

### Iran-war relevance

Very high.

Commercial energy shipping is a strategically useful pressure point because interference can impose:

- delay;
- inspection;
- port-security burden;
- safety uncertainty;
- insurance and commercial cost;
- energy-logistics friction;
- and defensive attention

without requiring a spectacular physical attack.

That strategic fit is a reason to investigate.

It is not attribution evidence.

### Sources

- [CBS News — Coast Guard and FBI boarded two energy tankers after cyberattacks](https://www.cbsnews.com/news/coast-guard-fbi-boarded-energy-tankers-cyberattacks-amy-grable-iran/)
- [Insurance Journal / Bloomberg — US tracking cyber threats against nearly 20 ships worldwide](https://www.insurancejournal.com/news/national/2026/09/17/885384.htm)
- [Wall Street Journal — US probes Iran link to cyberattacks on Texas-bound energy tankers](https://www.wsj.com/politics/national-security/u-s-probes-cyberattacks-on-energy-tankers-bound-for-american-coast-33d92f3a)

---

## 🚰 2026-08 — Colorado Water Utilities: Foreign Actors Reach The Control Layer

### 🇺🇸 United States — Colorado

### Event type

Incident / late disclosure.

### Sector

Water and wastewater / operational technology.

### What happened

Colorado confirmed that unidentified foreign hackers breached **two privately owned drinking-water utilities**, each serving fewer than 200 people, in late August.

The attackers:

- changed equipment settings;
- disabled remote access;
- disabled alarms;
- and altered pumping cycles.

### Operational depth

This is not merely enterprise IT or reconnaissance.

The public evidence supports direct interaction with the control layer:

```text
CONTROLLER / CONFIGURATION ACCESS:
🟢 ESTABLISHED

SETTING MANIPULATION:
🟢 ESTABLISHED

PUMP-CYCLE CHANGE:
🟢 ESTABLISHED

ALARM / REMOTE-ACCESS INTERFERENCE:
🟢 ESTABLISHED

WATER-SERVICE LOSS:
❌ NOT REPORTED

WATER-QUALITY EFFECT:
❌ NOT REPORTED

PUBLIC-SAFETY EFFECT:
❌ NOT REPORTED
```

### Attribution confidence

Colorado described the intruders as **foreign actors** but said it could not identify which foreign actors were responsible.

The governor's office separately noted the ongoing national effort by an Iranian-backed group to access drinking-water and wastewater systems.

That contextual statement must not be converted into attribution of these two incidents.

```text
FOREIGN ACTOR:
🟢 CONFIRMED BY COLORADO

RELATIONSHIP TO WIDER US WATER WAVE:
🟡 PROBABLE / DEVELOPING

IRAN RESPONSIBILITY FOR COLORADO:
🟠 SUSPECTED / UNRESOLVED

FORMAL ATTRIBUTION:
⚪ ABSENT
```

### Pattern significance

Colorado strengthens the operational pattern more than it strengthens the attribution.

The recurring sequence is increasingly:

```text
reachable water OT
→ unauthorised access
→ operator visibility / remote control degraded
→ settings or pump behaviour changed
→ local intervention prevents wider service effect
```

That is important because the campaign's significance is increasingly visible in **repeated penetration to the control layer**, not merely in the number of people who lose water.

### Sources

- [Reuters — Foreign hackers targeted Colorado water systems in August](https://www.investing.com/news/general-news/foreign-hackers-targeted-colorado-water-systems-in-august-governors-office-says-4908010)
- [Axios Denver — Foreign actors breach Colorado water systems](https://www.axios.com/local/denver/2026/09/18/water-utilities-cyberattack-hackers)

---

## ⚡ 2026-09-14 — CenterPoint Energy Customer-System Compromise

### 🇺🇸 United States — Texas / multi-state utility footprint

### Event type

Incident disclosure.

### Sector

Electricity and natural gas.

### What happened

CenterPoint Energy disclosed in an SEC filing that an unauthorised third party obtained personal information relating to some customers through one of the company's external-facing systems.

The company began investigating after becoming aware of an online post claiming to possess customer information.

### Operational effect

```text
CUSTOMER-DATA COMPROMISE:
🟢 CONFIRMED

ELECTRIC DELIVERY DISRUPTION:
❌ NOT REPORTED

GAS DELIVERY DISRUPTION:
❌ NOT REPORTED

OT COMPROMISE:
⚪ NOT ESTABLISHED
```

### Attribution confidence

```text
OPERATOR:
⚪ OPEN

STATE RELATIONSHIP:
⚪ OPEN

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

Conventional data theft or criminal intrusion is presently better supported than a wartime infrastructure-disruption explanation.

### Pattern significance

CenterPoint is useful precisely because the target is strategically important but the demonstrated effect stops at the enterprise / data layer.

```text
MAJOR ENERGY UTILITY
→ EXTERNAL-FACING SYSTEM COMPROMISED
→ CUSTOMER DATA OBTAINED
→ ENERGY DELIVERY CONTINUES
```

This is a reminder not to infer physical-process intent from sector alone.

### Sources

- [SEC — CenterPoint Energy Form 8-K, 14 September 2026](https://www.sec.gov/Archives/edgar/data/48732/000110465926107560/tm2625326d1_8k.htm)
- [Reuters — CenterPoint Energy discloses customer data breach](https://www.reuters.com/legal/litigation/centerpoint-energy-discloses-customer-data-breach-sec-filing-2026-09-14/)

---

## 🏥 2026-09-16 onward — Nipigon District Memorial Hospital Ransomware

### 🇨🇦 Canada — Ontario

### Event type

Incident / business-continuity response.

### Sector

Healthcare / hospital operations.

### What happened

Nipigon District Memorial Hospital activated ransomware response and business-continuity procedures after its IT systems were disrupted and files were encrypted.

### Operational effect

The incident reached patient-facing service delivery.

```text
OUTPATIENT LABORATORY:
🔴 TEMPORARILY UNAVAILABLE

DIAGNOSTIC IMAGING:
🔴 TEMPORARILY UNAVAILABLE

MANUAL PROCEDURES:
🟢 ACTIVATED

OTHER HOSPITAL ACTIVITY:
CONTINUING WITH DELAY RISK
```

### Attribution confidence

```text
RANSOMWARE:
🟢 CONFIRMED

SPECIFIC OPERATOR:
⚪ OPEN

STATE SPONSOR:
⚪ OPEN

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

Financially motivated ransomware remains the leading explanation.

### Pattern significance

Nipigon strengthens the healthcare operational-disruption strand without strengthening Iranian attribution.

Healthcare now contains repeated examples in which cyber incidents move beyond confidentiality loss into:

```text
appointment disruption
ambulance diversion
diagnostic unavailability
manual fallback
manufacturing / supply interruption
```

The mechanisms and operators remain heterogeneous.

### Source

- [TMC Insight — Nipigon District Memorial Hospital activates ransomware response](https://insight.tmcnet.com/insight/nipigon-district-memorial-hospital-activates-ransomware-response-mu52wwyh)

---

## 🚢 2026-09-18 onward — Vivit Africa LNG Systems Failure / Suspected Cyberattack

### 🇮🇹 Italy / Mediterranean / transatlantic U.S.–European energy route

### Event type

Operational incident / suspected cyber cause.

### Sector

LNG transport / maritime operational technology.

### What happened

The **Vivit Africa LNG**, carrying U.S. gas towards Italy, suffered a systems failure after crew members lost access to some internal control systems.

The crew reported the event as a suspected cyberattack.

The Italian Coast Guard independently confirmed that the master reported a malfunction affecting systems used to monitor cargo parameters and that company technicians had to intervene.

The Coast Guard did **not** determine that the cause was cyber.

The vessel remained unable to complete its intended discharge at Rovigo and diverted west.

### Operational effect

```text
CONTROL-SYSTEM / CARGO-MONITORING MALFUNCTION:
🟢 CONFIRMED

INTENDED LNG DISCHARGE:
🟢 NOT COMPLETED

VOYAGE DIVERSION:
🟢 CONFIRMED

CYBER CAUSATION:
🟠 SUSPECTED

ATTACKER:
⚪ OPEN

IRAN CONNECTION:
⚪ OPEN / NO ATTRIBUTION
```

Later crew allegations described interference with steam pressure, safety valves, tank-pressure controls, pressure-relief valves and boil-off-gas management.

Those allegations are potentially very significant.

They remain **unverified**.

### Rival explanation

Ordinary equipment, automation or software failure remains a live explanation and cannot be displaced merely because genuine maritime cyber investigations are occurring elsewhere.

### Pattern significance

Vivit Africa is therefore a third energy-vessel event worth preserving beside the U.S. tanker investigations, but on a different evidentiary footing:

```text
VL PROSPERITY / KOHAKU:
NETWORK COMPROMISE INDICATORS CONFIRMED BY US AUTHORITIES

VIVIT AFRICA:
OPERATIONAL CONTROL-SYSTEM FAILURE CONFIRMED
CYBER CAUSE SUSPECTED BY CREW
CYBER CAUSE NOT ESTABLISHED BY ITALIAN AUTHORITIES
```

The cluster is now strong enough to monitor as a maritime-energy-OT problem.

It is not strong enough to attribute as one campaign.

### Sources

- [Bloomberg Law — Another tanker suffers failure as crew suspect cyber attack](https://news.bloomberglaw.com/tech-and-telecom-law/another-tanker-suffers-failure-as-crew-suspect-cyber-attack)
- [Insurance Journal / Bloomberg — Vivit Africa LNG systems failure](https://www.insurancejournal.com/news/international/2026/09/18/885689.htm)

---

## 🏛️ 2026-09-21 — The U.S. Executive Has Acknowledged The Maritime Problem Without Attributing It To Iran

### 🇺🇸 United States

### Event type

Attribution-governance update.

### What changed

The public U.S. position has moved beyond:

```text
UNVERIFIED REPORT OF A STRANGE TANKER EVENT
```

The executive branch has now acknowledged:

```text
INDICATIONS THAT TWO VESSEL NETWORKS WERE COMPROMISED
+
FOREIGN-ACTOR CONCERN
+
COAST GUARD AND FBI BOARDINGS
+
CISA INVOLVEMENT
+
DHS / FBI / COAST GUARD WIDER MONITORING
+
NEARLY 20 VESSELS UNDER PARTICULAR CYBER-THREAT WATCH
```

What it has **not** publicly done is attribute those compromises to Iran.

### Current public position

```text
GENUINE MARITIME CYBER PROBLEM:
🟢 ACKNOWLEDGED

IRAN AS INVESTIGATIVE HYPOTHESIS:
🟠 ACKNOWLEDGED IN REPORTING

FORMAL PUBLIC ATTRIBUTION TO IRAN:
⚪ NOT ESTABLISHED

WIDER NEARLY-20-VESSEL POPULATION SHARES ONE ACTOR:
⚪ NOT ESTABLISHED
```

That distinction matters.

The public record is no longer well described as:

> America says it is unrelated.

It is better described as:

> **America acknowledges a real foreign maritime cyber problem, is investigating an Iranian connection in at least part of it, and has not crossed the public attribution threshold.**

---

## 🧭 Pattern Shift By 21 September 2026

The post-14-September record adds two particularly important layers.

### 1. Maritime energy transport is now a separate watch object

The strongest Iran-facing / wartime infrastructure sequence now includes:

```text
US water OT
→ UK electricity generation
→ reported US energy + telecom targeting
→ naval technical reconnaissance
→ confirmed vessel-network compromises
→ nearly 20 vessels under US cyber-threat watch
→ separate LNG control-system failure under cyber investigation
```

The maritime evidence is **not** yet equivalent to the water evidence.

But it is no longer reasonable to treat each vessel as an isolated curiosity.

### 2. The control layer remains more informative than the headline outage

Colorado again demonstrates that a small incident can be technically deep:

```text
tiny utility
→ alarms disabled
→ remote access disabled
→ pump cycles changed
→ no public water outage
```

CenterPoint demonstrates the inverse:

```text
major utility
→ confirmed compromise
→ customer data stolen
→ energy delivery untouched
```

Therefore:

```text
SIZE OF ORGANISATION
≠
DEPTH OF COMPROMISE

AND

HEADLINE OUTAGE SIZE
≠
TECHNICAL SIGNIFICANCE
```

### 3. Maritime attribution now has an executive-governance track of its own

The tanker investigation has developed the same methodological requirement already visible in the water campaign:

```text
WHAT INVESTIGATORS ARE EXAMINING
≠
WHAT INTELLIGENCE MAY ASSESS
≠
WHAT THE EXECUTIVE PUBLICLY ACKNOWLEDGES
≠
WHAT THE GOVERNMENT FORMALLY ATTRIBUTES
```

Those stages should remain separately timestamped.

### 4. The mixed-ecosystem warning has become stronger, not weaker

CenterPoint and Nipigon are real essential-sector incidents with no positive Iran evidence.

Vivit Africa may still prove to be equipment failure.

Colorado may belong to the Iran-linked water wave or may represent another foreign operator exploiting the same exposed environment.

So:

```text
MORE CLUSTERING
→ MORE REASON TO INVESTIGATE RELATIONSHIPS

BUT

MORE ACTOR DENSITY
→ HIGHER ATTRIBUTION BAR
```

Both propositions can be true simultaneously.


## 🗂️ September–October 2026 — Integrated Chronology Update

*Integrated from the 15 October 2026 CSV evidence register. Earlier incident entries remain unchanged. Dates below follow the register's routing date; the narrative distinguishes underlying activity from disclosure, warning, and enforcement dates.*

**Counting rule:** A defensive advisory is not an incident; a law-enforcement action is not a new intrusion; a disclosure may describe an earlier attack; multiple customers of one supplier are not automatically independent attacks. These entries are evidence-register statements, not a new independent verification of every cited source.

## 2026-09-25 — Kiteworks

### 🌍 International · Cross-sector / other

**Record type:** Preparedness / defensive action

**Sector:** Cross-sector secure file transfer

**What happened:** Precautionary shutdown advised 25 September following credible threat intelligence; 28 September restoration statement reported no detected compromise.

**Operational effect:** Temporary defensive shutdown / customer availability consequence.

**Physical / data effect:** No confirmed exfiltration or successful attack.

**Claim status:** Official company statements

**Technical operator:** Not applicable

**State relationship:** Potential actor unknown; no successful incident attributed.

**Incident confidence:** 🟢 Established defensive response

**Effect confidence:** 🟢 Established preventive availability effect

**Attribution confidence:** ⚪ Not applicable

**Relationship confidence:** ⚪ Open

**Pattern status:** ⚪ Context / isolated

**Iran-war relevance:** Illustrates operational costs of threat warnings

**Iran attribution:** No incident Iran attribution

**Rival explanations:** Preventive risk mitigation, not evidence of compromise.

**Negative findings:** No Kiteworks or customer compromise detected in company review.

**Manual fallback:** Services temporarily shut as precaution

**Organising mechanism:** Threat / defensive response

**Common operator confidence:** ⚪ Open

**Strategic campaign confidence:** ⚪ Open

**Civilian / IHL relevance:** Not a confirmed hostile attack.

**Stakeholder effect:** Customer service availability affected by protective measure.

**Source provenance:** Company statements; no independent compromise claimed.

**Attribution history:** 25 September advisory → 28 September restoration

### 📚 Sources recorded in CSV

- https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/
- https://www.kiteworks.com/company/press-releases/kiteworks-restores-systems-credible-threat/

*CSV review date: 2026-10-15; correction status: New — defensive action; exclude attack count.*

---

## 2026-09-27 — Citrix NetScaler affected organisations

### 🌍 North America / Europe · Cross-sector / other

**Record type:** Campaign reporting / defensive advisory

**Sector:** Government; finance; education; technology

**What happened:** Exploitation of internet-facing NetScaler devices reported from early September; CERT-EU notice 27 September; Google/Mandiant report 29 September.

**Operational effect:** Some organisations reportedly compromised; essential-service outages not established.

**Physical / data effect:** Access and credential exposure risk; no general physical effect.

**Claim status:** Technical investigation / advisory

**Technical operator:** Multiple / unknown

**State relationship:** No common state sponsor established.

**Incident confidence:** 🟢 Established campaign

**Effect confidence:** 🟠 Developing victim-specific effects

**Attribution confidence:** ⚪ Open

**Relationship confidence:** ⚪ Open — potentially multiple actors

**Pattern status:** 🟠 Credible cluster

**Iran-war relevance:** Cross-sector access route to essential services

**Iran attribution:** No public Iran evidence

**Rival explanations:** Multiple criminal/state actors may exploit same vulnerabilities.

**Negative findings:** No confirmed essential-service outage in cited technical report.

**Manual fallback:** Not reported

**Organising mechanism:** Internet-facing edge access / credential theft

**Common operator confidence:** ⚪ Open

**Strategic campaign confidence:** ⚪ Open

**Civilian / IHL relevance:** No confirmed OT effect.

**Stakeholder effect:** Exposed organisations face access risk.

**Source provenance:** Technical research and CERT warning; avoid double-counting.

**Attribution history:** Early September exploitation → 27–29 September disclosures

### 📚 Sources recorded in CSV

- https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances/
- https://cert.europa.eu/publications/security-advisories/2026-014

*CSV review date: 2026-10-15; correction status: New — campaign/advisory, not one outage.*

---

## 🧾 October 2026 — reconciled incident and disclosure records

**Editorial status:** 27 distinct records reconciled from 28 original October CSV entries (two follow-ups merged; one mixed payment-provider entry split). Record dates may be *publication/disclosure* dates, not incident onset. A record is not necessarily an attack. The full 40-column staging dataset remains the field-level companion to these narratives.

**Deduplication:** Ahold Delhaize 19 October and French refrigeration 14 October are follow-ups to their parent incidents, not separate records. Stripe/Revolut Pay and Adyen/Eftpos are separate payment-method events with distinct reported causes.

---

## 2026-10-01 — City of Vicksburg

**Record type:** Cyber incident  
**Routing:** Core  
**Location / sector:** United States — Mississippi · Municipal administration / utility billing  
**System layer:** Municipal IT / utility billing

**Incident and chronology:** Ransomware led the city to temporarily shut down municipal computer systems on 1 October. The mayor said police, fire, emergency response and utility supply continued; in-person utility payments were disrupted. Recovery update dated 27 October anticipated utility-payment processing on 30 October subject to testing.

**Operational effect:** Municipal IT shutdown; in-person utility-payment processing disrupted; emergency services and utility supply continued.  
**Physical / data effect:** Data theft not established.  
**Manual fallback:** Utilities and 911 continued

**Evidence / attribution:** Incident 🟢 Established; effect 🟢 Established limited administration effect; attribution ⚪ Open. Claim status: Mayor statement via press. Technical actor: Unknown. Public government attribution: Not established.

**Iran relevance and attribution:** Local government and utility administrative continuity. No public Iran evidence. No state affiliation established.

**Rival explanations / negative findings:** Financially motivated ransomware likely; other intrusion possible. No verified compromise of utility delivery, emergency response or personal data; 27 October is a recovery update, not a second attack.

**Retrospective attribution and correction history:** 1 October incident → 2 October reporting. New — October incident; Reconciled 2026-11-18 — municipal statement and recovery dates reconciled; original city permalink still not recorded

**Source tier and independence:** Contemporary reporting quoting mayor; original municipal statement cited in follow-up audit but direct municipal URL not preserved. Mayor cited by local press; no independent forensic attribution.

**Sources:** https://www.wlbt.com/2026/10/02/city-vicksburg-hit-by-ransomware-cyberattack-mayor-says/

**Last reviewed:** 2026-11-18

---

## 2026-10-03 — Ivanti Connect Secure / UTA0576

**Record type:** Cyber incident / technical campaign; 13 October research disclosure  
**Routing:** Context  
**Location / sector:** Undisclosed · Enterprise VPN / cross-sector access  
**System layer:** VPN appliance / enterprise identity

**Incident and chronology:** Exploitation observed from 3 October involving chained Ivanti Connect Secure vulnerabilities, privileged appliance access and credential theft. Volexity published technical findings 13 October; later vendor remediation followed.

**Operational effect:** Internal compromise and reconnaissance; affected victim country/sector not public; no essential-service outage established.  
**Physical / data effect:** Credential extraction; no OT process effect demonstrated.  
**Manual fallback:** Not reported

**Evidence / attribution:** Incident 🟢 Established exploitation; effect 🟢 Established access; ⚪ essential-service effect open; attribution ⚪ Open. Claim status: First-hand technical investigation. Technical actor: UTA0576. Public government attribution: Not established.

**Iran relevance and attribution:** Cross-sector access mechanism; essential-sector victim not identified. No public Iran evidence. Volexity low-confidence criminal motivation; state sponsor unknown.

**Rival explanations / negative findings:** Criminal access brokerage, espionage, pre-ransomware foothold. No named essential-service victim or physical outage.

**Retrospective attribution and correction history:** 3–5 October compromise → 13 October technical disclosure → 14 October CERT warning. New — access campaign, contextual route; Reconciled 2026-11-18 — incident 3 October; publication 13 October

**Source tier and independence:** Tier 2 — first-hand technical research. Volexity; motivation low confidence and LLM use medium confidence.

**Sources:** https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/

**Last reviewed:** 2026-11-18

---

## 2026-10-05 — CPR register / private authorised access holder

**Record type:** Retrospective data-access incident / 5 October disclosure  
**Routing:** Core  
**Location / sector:** Denmark · National population identity registry  
**System layer:** Delegated registry query / identity data

**Incident and chronology:** Unauthorised use of a private organisation’s legitimate access occurred in September; detected 2 October and publicly disclosed 5 October. Approximately 8.8 million registered CPR records were queried; this figure is not necessarily 8.8 million living residents.

**Operational effect:** No national registry outage established.  
**Physical / data effect:** Personal numbers, names and addresses potentially exposed; count includes historic and deceased records.  
**Manual fallback:** Registry services not reported interrupted

**Evidence / attribution:** Incident 🟢 Established access abuse; effect 🟢 Established record access; downstream misuse open; attribution ⚪ Open. Claim status: Official registry disclosure. Technical actor: Unknown. Public government attribution: Not established.

**Iran relevance and attribution:** National-scale identity data custody. No public Iran evidence. No state nexus established.

**Rival explanations / negative findings:** Credential misuse; criminal data extraction; unrelated insider activity. 8.8m records not equal 8.8m current residents; no outage.

**Retrospective attribution and correction history:** September query abuse → 2 October detection → 5 October disclosure. New — approximate occurrence date; Reconciled 2026-11-18 — September access; October detection and disclosure; denominator qualified

**Source tier and independence:** Tier 1 — registry and ministry. Official registry and ministry statements; figures are record counts.

**Sources:** https://www.cpr.dk/cpr-nyt/nyhedsarkiv/2026/okt/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger | https://fudm.dk/aktuelt/pressemeddelelser/2026/oktober/omfattende-uautoriseret-adgang-til-borgeres-cpr-oplysninger/

**Last reviewed:** 2026-11-18

---

## 2026-10-06 — CL-STA-1178 / Blinder Tunnel

**Record type:** Threat research disclosure / earlier malicious campaign  
**Routing:** Adjacent  
**Location / sector:** Iraq / Israel / UAE · Critical infrastructure recruitment / aviation impersonation  
**System layer:** Phishing / malicious development project / tunnelling

**Incident and chronology:** Unit 42 report published 6 October describes earlier Blinder Tunnel activity targeting Iraqi critical-infrastructure personnel through fraudulent recruitment and malicious coding tasks. Infrastructure preparation observed in 2025; activity in March 2026.

**Operational effect:** Espionage and attempted foothold; no essential-service outage verified.  
**Physical / data effect:** Credential / access risk; no confirmed physical process change.  
**Manual fallback:** Not reported

**Evidence / attribution:** Incident 🟢 Established research; effect 🟠 Developing access impact; attribution 🟡 Probable Iranian nexus (researcher). Claim status: Unit 42 technical research; high-confidence Iranian nexus assessment, specific known-group linkage less certain. Technical actor: CL-STA-1178 / Blinder Tunnel. Public government attribution: Not established.

**Iran relevance and attribution:** High — Iraqi critical-infrastructure recruitment targeting; pre-war staging. Unit 42 assesses a high-confidence Iranian nexus; no conclusive identification of a specific state agency or established Iranian group. Unit 42 assessed Iranian nexus with high confidence; specific Iranian agency or state tasking not independently established.

**Rival explanations / negative findings:** Espionage campaign; deceptive recruitment; other sponsors not excluded by independent evidence. 6 October is publication date, not campaign onset; no confirmed October operational outage or precise state-agency attribution.

**Retrospective attribution and correction history:** Preparatory infrastructure 2025 → campaign March 2026 → Unit 42 publication 6 October 2026; high-confidence Iranian nexus assessment, specific actor overlap lower confidence. New — source-led October backfill; Reconciled 2026-11-18 — original Unit 42 report recovered; attribution confidence qualified

**Source tier and independence:** Tier 1 original threat research. Researcher assessment, not an official Iranian admission.

**Sources:** https://unit42.paloaltonetworks.com/?search=9D8D8997D1083C4B2DFB2272F765733 | https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/

**Last reviewed:** 2026-11-18

---

## 2026-10-06 — Country-code TLD registries .gh / .sl / .as

**Record type:** Cyber incident / campaign disclosure  
**Routing:** Adjacent  
**Location / sector:** Ghana / Sierra Leone / American Samoa · DNS registry / internet trust infrastructure  
**System layer:** DNS authority / certificate trust

**Incident and chronology:** Late-September compromise of third-party country-code top-level-domain registries enabled unauthorised DNS changes and issuance of fraudulent TLS certificates; Google Chrome security team disclosed findings 6 October.

**Operational effect:** Integrity of domain resolution affected; no national outage established.  
**Physical / data effect:** Fraudulent certificates / possible traffic diversion; mass interception unproven.  
**Manual fallback:** Not reported

**Evidence / attribution:** Incident 🟢 Established registry compromise; effect 🟢 Established integrity compromise; ⚪ mass impact open; attribution ⚪ Open. Claim status: Primary technical research. Technical actor: Unknown. Public government attribution: Not established.

**Iran relevance and attribution:** Internet trust layer supporting state and public services. No public Iran evidence. No state sponsor established.

**Rival explanations / negative findings:** Cybercrime or another intelligence actor. Not a compromise of Google infrastructure; October is disclosure date rather than established intrusion date.

**Retrospective attribution and correction history:** Late September activity → 6 October research disclosure. New — approximate occurrence date; Reconciled 2026-11-18 — third-party registries and September onset distinguished

**Source tier and independence:** Tier 2 — first-hand technical disclosure. Google security research; country-level outage not inferred.

**Sources:** https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/

**Last reviewed:** 2026-11-18

---

## 2026-10-06 — FortiBleed / Fortinet devices

**Record type:** Joint law-enforcement advisory / ongoing campaign  
**Routing:** Context  
**Location / sector:** International · VPN / firewall access across critical sectors  
**System layer:** Firewall / VPN / administrative credentials

**Incident and chronology:** FBI and US Secret Service issued joint alert JCSA-20261006-01 on 6 October about ongoing attacks against exposed Fortinet firewalls and VPN gateways, including use of compromised credentials, password spraying, credential stuffing and administrator lockouts.

**Operational effect:** Access and lockout risk; no sector-specific OT outage established.  
**Physical / data effect:** Credential theft and attempted lateral movement; victim effects vary.  
**Manual fallback:** Not reported

**Evidence / attribution:** Incident 🟢 Established warning; effect 🟠 Developing individual victim effects; attribution ⚪ Open. Claim status: Original FBI–USSS 6 October advisory verified. Technical actor: Criminal access-broker ecosystem (suspected). Public government attribution: Not established.

**Iran relevance and attribution:** Recurring edge-device intrusion pathway. No public Iran evidence. No Iranian sponsor established.

**Rival explanations / negative findings:** Credential resale / criminal ransomware; multiple actors possible. FortiBleed is not a newly discovered October vulnerability; ongoing campaign known by June 2026; no common Iranian sponsor established.

**Retrospective attribution and correction history:** 6 October warning → 7 October sector summary. New — advisory, not one outage; Reconciled 2026-11-18 — exact October advisory recovered; no new CVE inferred

**Source tier and independence:** Tier 1 FBI–USSS original advisory. FBI index is non-specific; preserve uncertainty over device counts.

**Sources:** https://www.fbi.gov/investigate/cyber/alerts/2026 | https://www.aha.org/news/headline/2026-10-07-agencies-warn-credential-compromising-campaign-actively-targeting-critical-infrastructure-networks | https://www.ic3.gov/CSA/2026/261006.pdf

**Last reviewed:** 2026-11-18

---

## 2026-10-07 — IDC Frontier — East Japan Region 1

**Record type:** Cyber incident  
**Routing:** Core  
**Location / sector:** Japan · Cloud hosting / government / transport logistics  
**System layer:** Cloud virtual machines / shared hosting

**Incident and chronology:** Ransomware disrupted East Japan Region 1 from 7 October, affecting services for 495 customer organisations according to provider notices; 27 October investigation was a follow-up.

**Operational effect:** Virtual servers stopped or failed to restart; customer government and logistics functions affected.  
**Physical / data effect:** Some data recovery difficult; downstream exposure claims require customer-specific verification.  
**Manual fallback:** Recovery and possible data loss under review

**Evidence / attribution:** Incident 🟢 Established; effect 🟢 Established cloud outage; attribution ⚪ Open. Claim status: Provider-confirmed ransomware. Technical actor: Unknown ransomware operator. Public government attribution: Not established.

**Iran relevance and attribution:** High — government and essential transport/logistics reliance. No public Iran evidence. No Iranian state link established.

**Rival explanations / negative findings:** Financial ransomware; unrelated criminal attack. 495 affected customer organisations does not establish 495 separately compromised environments.

**Retrospective attribution and correction history:** 7 October service disruption → 27 October provider technical investigation. New — October incident; Reconciled 2026-11-18 — provider and follow-up dates distinguished

**Source tier and independence:** Tier 1 provider + specialist reporting. Provider statement controls primary incident count.

**Sources:** https://www.idcf.jp/news/topics/20261007002 | https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/ | https://www.idcf.jp/news/topics/20261007001/ | https://www.idcf.jp/news/topics/20261027001

**Last reviewed:** 2026-11-18

---

## 2026-10-08 — Flax Typhoon / Integrity Technology Group tooling

**Record type:** Law-enforcement seizure / retrospective campaign  
**Routing:** Context  
**Location / sector:** United States / Japan / Poland / Taiwan · Energy / transport / education reconnaissance  
**System layer:** Internet scanning / phishing / access tooling

**Incident and chronology:** US DOJ/FBI announced 8 October seizure of scanning and spear-phishing tooling infrastructure attributed to Flax Typhoon-related activity; this is an enforcement action, not a newly dated intrusion.

**Operational effect:** Scanning and some intrusions; no specific energy or airport service outage established by seizure.  
**Physical / data effect:** Reconnaissance and potential data compromise; no confirmed physical-process effect.  
**Manual fallback:** Not reported

**Evidence / attribution:** Incident 🟢 Established seizure; effect 🟠 Developing specific intrusions; ⚪ outages unproven; attribution 🟡 Probable PRC linkage per US government. Claim status: US law-enforcement action. Technical actor: Flax Typhoon / Integrity Technology Group. Public government attribution: US DOJ/FBI enforcement action.

**Iran relevance and attribution:** Competing state-linked campaign in same strategic sectors. No Iran nexus. US government alleges PRC-linked activity.

**Rival explanations / negative findings:** PRC-linked cyberespionage per US allegations; no evidence Iran customer. Scanning ≠ compromise ≠ outage.

**Retrospective attribution and correction history:** Prior scanning/intrusions → 8 October domain seizure. New — enforcement event; Reconciled 2026-11-18 — enforcement event not attack onset

**Source tier and independence:** Tier 1 — DOJ enforcement. Official allegation and seizure, not conviction or service disruption.

**Sources:** https://www.justice.gov/usao-wdpa/pr/justice-department-and-fbi-seize-vulnerability-scanning-and-spear-phishing-tools

**Last reviewed:** 2026-11-18

---

## 2026-10-08 — Publica external software supplier

**Record type:** Retrospective supplier incident / October disclosure  
**Routing:** Adjacent  
**Location / sector:** Switzerland · Federal pension administration / supplier data  
**System layer:** Supplier application / personal data

**Incident and chronology:** Attack on external software supplier occurred in late September; PUBLICA disclosed on 8 October that pension-related personal data may have been exposed. Production pension systems were unaffected.

**Operational effect:** Pension payments not shown interrupted.  
**Physical / data effect:** Member data potentially exposed; scope under investigation.  
**Manual fallback:** Pension payments continued

**Evidence / attribution:** Incident 🟢 Established supplier incident; effect 🟠 Developing data scope; attribution ⚪ Open. Claim status: Official operator / federal disclosure. Technical actor: Unknown. Public government attribution: Not established.

**Iran relevance and attribution:** Government financial-data custody dependency. No public Iran evidence. No state nexus established.

**Rival explanations / negative findings:** Ordinary criminal breach / extortion. No evidence PUBLICA production pension systems were compromised or pension payments interrupted.

**Retrospective attribution and correction history:** Late September occurrence (exact day not public) → 8 October disclosure. New — approximate occurrence date; Reconciled 2026-11-18 — late September attack vs 8 October disclosure

**Source tier and independence:** Tier 1 — operator and federal. Official disclosures; exact occurrence day uncertain.

**Sources:** https://www.publica.ch/de/ueber-uns/aktuell/cyberangriff-auf-softwarelieferant-von-publica-datenabfluss-bestaetigt | https://www.astra.admin.ch/en/newnsb/FjG4XOIms04s

**Last reviewed:** 2026-11-18

---

## 2026-10-11 — Ahold Delhaize and retail brands

**Record type:** Cyber incident / protective shutdown  
**Routing:** Core  
**Location / sector:** Netherlands / Belgium / United States · Food retail logistics / distribution  
**System layer:** Retail enterprise IT / distribution systems

**Incident and chronology:** Cybersecurity incident reported 11–12 October prompted precautionary IT shutdowns and disruptions to digital ordering and distribution. In a 19 October update the company confirmed malicious activity; stores remained open while affected services were restored.

**Operational effect:** Online services and logistics disrupted; physical stores remained open.  
**Physical / data effect:** No evidence of customer/employee data theft at 13 October statement.  
**Manual fallback:** Controlled restoration 13 October

**Evidence / attribution:** Incident 🟢 Established; effect 🟢 Established service disruption; attribution ⚪ Open. Claim status: Operator-confirmed cybersecurity incident; malicious activity confirmed in later 19 October update. Technical actor: Unknown. Public government attribution: Not established.

**Iran relevance and attribution:** Food distribution and cross-border shared-service continuity. No public Iran evidence. No state sponsor established.

**Rival explanations / negative findings:** Criminal intrusion; precautionary isolation; other technical fault under review. No confirmed Iranian attribution; 19 October update is not a second attack; stores remained open.

**Retrospective attribution and correction history:** 11 October incident → 12 October initial operator communication → 19 October confirmation of malicious activity and recovery update. New — October incident; Reconciled 2026-11-18 — merged 19 October Ahold follow-up into 11 October parent

**Source tier and independence:** Tier 1 company operator notices. Company statements distinguish shutdown from confirmed attack mechanism.

**Sources:** https://newsroom.aholddelhaize.com/ahold-delhaize-takes-precautionary-measures-following-cybersecurity-incident | https://newsroom.aholddelhaize.com/update-on-ahold-delhaizes-cybersecurity-incident/ | https://www.reuters.com/business/albert-heijn-expects-distribution-centres-be-operational-soon-after-cyber-2026-10-14/ | https://newsroom.aholddelhaize.com/ahold-delhaize-update-on-status-of-cybersecurity-incident/

**Last reviewed:** 2026-11-18

---

## 2026-10-11 — Supermarket refrigeration management controllers

**Record type:** Cyber incident  
**Routing:** Core  
**Location / sector:** France · Food refrigeration / supermarket supply  
**System layer:** Remote refrigeration control / OT-like building systems

**Incident and chronology:** Compromise of internet-connected supermarket refrigeration controllers reported 11–12 October; French CERT confirmed compromises and subsequent reporting expanded potential store counts. A French-government attribution to the IRGC was reported on 9 November, as a later attribution development.

**Operational effect:** Refrigeration temperatures altered; food spoilage and some equipment overheating reported.  
**Physical / data effect:** Physical food loss; store disruption; no national food shortage established.  
**Manual fallback:** Not fully established; activity possibly ongoing

**Evidence / attribution:** Incident 🟢 Established; effect 🟢 Established physical-process effect; attribution ⚪ Open. Claim status: French CERT confirmed controller compromises; later French-government attribution reported by AP. Technical actor: Unknown. Public government attribution: Not established.

**Iran relevance and attribution:** High — cyber-to-physical civilian food preservation. French-government attribution to IRGC reported 9 November 2026; not established at initial 11–12 October incident date. No sponsor established.

**Rival explanations / negative findings:** Opportunistic exposed-interface exploitation; vandalism; criminal or targeted sabotage. Store-count estimates evolved; 14 October entry is follow-up not separate incident; government attribution is not independent forensic confirmation of command chain.

**Retrospective attribution and correction history:** 11–12 October compromise → 12 October CERT alert → 14 October scope update → 9 November AP reports French-government attribution to IRGC. New — October incident; Reconciled 2026-11-18 — merged 14 October duplicate; preserved 9 November attribution

**Source tier and independence:** Tier 1 French CERT + AP reporting of later government attribution. CERT confirms equipment compromise; media support physical effects and counts.

**Sources:** https://cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/ | https://www.reuters.com/legal/litigation/investigators-hunt-french-supermarket-fridge-hackers-no-claim-responsibility-2026-10-13/ | https://apnews.com/article/81c2d5721f4df77f601f71741ef7c291 | https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012 | https://apnews.com/article/6914ecf1a3285291653e103655f9e4a4

**Last reviewed:** 2026-11-18

---

## 2026-10-13 — Housing Ombudsman Service

**Record type:** Cyber incident / supplier update  
**Routing:** Core / verified operator notice  
**Location / sector:** United Kingdom · Government complaints administration  
**System layer:** Supplier-hosted case management

**Incident and chronology:** Housing Ombudsman confirmed 13 October security incident affecting a third-party case-management provider; precautionary shutdown affected complaint and landlord portals and web chat. 3 November follow-up describes restoration/investigation.

**Operational effect:** Digital complaints and case access disrupted.  
**Physical / data effect:** Potential contact information exposure; scope open.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Original Ombudsman notice and later update confirmed. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Precautionary shutdown is not proof all data was exfiltrated; personal-data scope was under investigation.

**Retrospective attribution and correction history:** No new Iranian attribution established. New provisional row / verification required; Reconciled 2026-11-18 — operator source verified; November follow-up retained

**Source tier and independence:** Tier 1 Ombudsman operator notice. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://www.housing-ombudsman.org.uk/2026/10/13/housing-ombudsman-service-statement-it-security-incident/ | https://www.housing-ombudsman.org.uk/2026/11/03/it-security-incident-latest/

**Last reviewed:** 2026-11-18

---

## 2026-10-14 — 16 South Korean financial institutions (regulatory cluster)

**Record type:** Regulatory disclosure / multi-firm incident cluster  
**Routing:** Core  
**Location / sector:** South Korea · Banking / financial services / payment firms  
**System layer:** Peripheral financial IT / customer data

**Incident and chronology:** Financial Services Commission disclosed on 14 October incidents involving 16 financial firms and approximately 100,000 pieces of exposed data; investigation of common causes ongoing. This is a regulator reporting cluster, not 16 individually dated 14 October attacks.

**Operational effect:** Data exposure; no confirmed core banking, settlement or market outage.  
**Physical / data effect:** Approximately 100,000 personal records exposed.  
**Manual fallback:** Core financial services reportedly operational

**Evidence / attribution:** Incident 🟢 Established regulatory cluster; effect 🟢 Established data effect; attribution ⚪ Open. Claim status: Financial regulator announcement. Technical actor: Common operator under investigation. Public government attribution: Not established.

**Iran relevance and attribution:** Systemically important sector exposure; no systemic interruption. No public Iran evidence. No Iranian state affiliation established.

**Rival explanations / negative findings:** Financial crime; AI-assisted intrusion suspected; unrelated actors possible. 130 security deficiencies do not mean 130 breaches; common operator and common campaign not established.

**Retrospective attribution and correction history:** Late September–October intrusions → 14 October regulatory disclosure. New — regulatory update, occurrence dates not fixed; Reconciled 2026-11-18 — regulatory disclosure and unresolved common cause

**Source tier and independence:** Tier 1 regulator + Yonhap. Regulator aggregate; individual incident dates not public.

**Sources:** https://www.fsc.go.kr/eng/pr010101/87928 | https://www.yna.co.kr/view/AKR20261014134852002

**Last reviewed:** 2026-11-18

---

## 2026-10-15 — BAE Systems / US Bankruptcy Noticing Center

**Record type:** Cyber incident / supplier disruption  
**Routing:** Core / verified court notice  
**Location / sector:** United States · Federal justice administration  
**System layer:** Outsourced federal court administrative IT

**Incident and chronology:** Cybersecurity incident affecting Bankruptcy Noticing Center contractor interrupted nationwide bankruptcy notices; US Courts issued 15 October notice, emergency rules followed 22 October, services restarted 26 October and were restored by 27 October.

**Operational effect:** Official bankruptcy notice processes unavailable.  
**Physical / data effect:** No established impact on defence programmes.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: US Courts primary confirmation of service disruption. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Affected notices dated back to 7 October; this does not establish intrusion onset on 7 October.

**Retrospective attribution and correction history:** 15 October public US Courts notice → 22 October emergency rules → 26 October restart → 27 October restoration. New provisional row / verification required; Reconciled 2026-11-18 — recovery history preserved

**Source tier and independence:** Tier 1 US Courts. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://www.uscourts.gov/data-news/judiciary-news/2026/10/15/update-bankruptcy-noticing-center-access-restored

**Last reviewed:** 2026-11-18

---

## 2026-10-15 — CenterPoint Energy

**Record type:** Retrospective September breach disclosure  
**Routing:** Context / verified retrospective SEC filing  
**Location / sector:** United States — Texas · Energy utility / customer data  
**System layer:** Customer-facing utility data systems

**Incident and chronology:** 15 October SEC filing describes customer-information exposure arising from a September security incident. Company reports no disruption to electricity or natural-gas delivery.

**Operational effect:** No electricity or gas delivery disruption reported.  
**Physical / data effect:** Customer PII exposure; not grid compromise.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: SEC 8-K original filing. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Not a new October breach; no reported electricity or gas delivery disruption.

**Retrospective attribution and correction history:** September underlying incident → 15 October SEC disclosure. New provisional row / verification required; Reconciled 2026-11-18 — September incident; October disclosure

**Source tier and independence:** Tier 1 SEC/company filing. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://www.sec.gov/Archives/edgar/data/1042773/000110465926107560/tm2625326d1_8k.htm

**Last reviewed:** 2026-11-18

---

## 2026-10-15 — Cloudflare network services

**Record type:** Regional service availability / two distinct incidents  
**Routing:** Adjacent / verified operator status  
**Location / sector:** United Kingdom / United States · CDN / cloud  
**System layer:** CDN / distributed cloud

**Incident and chronology:** Separate Cloudflare operator incidents on 15 October: London network performance disruption 17:33–17:46 UTC affecting Durable Objects, R2 and RealtimeKit; Ashburn/Newark network degradation 20:48–21:38 UTC. Workers Cron Triggers incident began 16 October UTC and is not part of the 15 October event.

**Operational effect:** Short-lived service performance degradation reported.  
**Physical / data effect:** No malicious cause established.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Direct Cloudflare status incident permalinks recovered. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Two geographically distinct notices; no verified shared cause, global outage, malicious actor or Iranian nexus.

**Retrospective attribution and correction history:** 15 October London and eastern-US incidents; separate Workers Cron Triggers incident 16 October UTC. New provisional row / verification required; Reconciled 2026-11-18 — direct operator incident IDs; Workers corrected to 16 October

**Source tier and independence:** Tier 1 Cloudflare operator status. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://www.cloudflarestatus.com/incidents/ybyy2whvd8ef | https://www.cloudflarestatus.com/incidents/fiv2bu3zf8kx | https://www.cloudflarestatus.com/incidents/51udczr46uj2

**Last reviewed:** 2026-11-18

---

## 2026-10-19 — ConnectWise Cloud Backup / Microsoft 365 customers

**Record type:** Cloud identity intrusion / update  
**Routing:** Adjacent / verified operator notice  
**Location / sector:** United States / international · Cloud backup / identity / strategic policy  
**System layer:** Cloud identity / application credentials / backup

**Incident and chronology:** ConnectWise discovered unauthorised application-identity activity on 14 October involving cloud backup/Microsoft 365 connections; 19 October update described response and downstream precautions.

**Operational effect:** Cloud backup, security monitoring and cloud-management functions suspended during remediation.  
**Physical / data effect:** No confirmed compromise of specifically targeted national-security organisations.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Operator security advisory confirms activity and remediation. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Partner/customer exposure does not mean all connected tenants were compromised; no confirmed common Iranian actor.

**Retrospective attribution and correction history:** 14 October discovery → 19 October follow-up. New provisional row / verification required; Reconciled 2026-11-18 — 14 October discovery and 19 October update

**Source tier and independence:** Tier 1 ConnectWise operator advisory. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://www.connectwise.com/company/trust/advisories

**Last reviewed:** 2026-11-18

---

## 2026-10-19 — TeamUpdraft / UpdraftCentral

**Record type:** Cyber incident / managed administration  
**Routing:** Adjacent / verified vendor notice  
**Location / sector:** Global / United Kingdom · Managed websites / backup  
**System layer:** Trusted remote site administration

**Incident and chronology:** Vendor and Patchstack describe compromise of connection keys used to gain administrative access to connected WordPress sites and install malicious plugins; activity detected 17–18 October, disclosed and remediated from 19 October.

**Operational effect:** Downstream website compromises reported; essential-service effects not established.  
**Physical / data effect:** Extent of downstream compromise unresolved.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Vendor and independent security researcher confirmed malicious key misuse. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. AI-assisted attacker hypothesis unproven; no named critical-infrastructure victim established.

**Retrospective attribution and correction history:** No new Iranian attribution established. New provisional row / verification required; Reconciled 2026-11-18 — credential/control-plane mechanism confirmed; victim scope limited

**Source tier and independence:** Tier 1 vendor + security researcher. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://teamupdraft.com/blog/security-incident-october-2026/ | https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/

**Last reviewed:** 2026-11-18

---

## 2026-10-19 — eMudhra intermediate certificate keys / Cloudflare advisory

**Record type:** Certificate trust weakness / remediation advisory  
**Routing:** Context / verified issuer statement  
**Location / sector:** Global · PKI / certificates / identity  
**System layer:** Certificate signing / PKI

**Incident and chronology:** eMudhra disclosed that a script error produced weak, mathematically recoverable private keys for eight intermediate certificate authorities. Revocation and remediation followed; hostile key theft or issuer intrusion not established.

**Operational effect:** No specific service outage established.  
**Physical / data effect:** Potential trust and impersonation exposure; actual exploitation open.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Original certificate issuer statement confirms weak keys. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. No proven attacker theft, operational outage or critical-infrastructure compromise.

**Retrospective attribution and correction history:** No new Iranian attribution established. New provisional row / verification required; Reconciled 2026-11-18 — weak recoverable keys, not demonstrated intrusion

**Source tier and independence:** Tier 1 certificate issuer. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://emudhra.com/en/post/certificate-security-incident/

**Last reviewed:** 2026-11-18

---

## 2026-10-20 — Adyen / Australian Eftpos

**Record type:** Payment-method disruption / external planned maintenance  
**Routing:** Adjacent / qualified archival operator text  
**Location / sector:** United Kingdom / Europe / Brazil · Payments / banking  
**System layer:** Payment processing / upstream partner dependencies

**Incident and chronology:** Archived Adyen-origin status messages report elevated errors for Australian Eftpos transactions on 20 October, attributed by Adyen to last-minute planned maintenance at the external Eftpos partner.

**Operational effect:** Some payment authorisations, settlement or refunds degraded; not a general payment-system failure.  
**Physical / data effect:** Common cause across notices not established.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Operator-origin messages reproduced in third-party archive; direct Adyen incident permalink not recovered. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Not an Adyen-wide outage, not a confirmed cyberattack, and not shown to arise from Google Cloud London.

**Retrospective attribution and correction history:** 20 October Australian Eftpos errors → Adyen-origin notice attributes cause to external planned maintenance. Reconciled 2026-11-18 — split from mixed payment row; distinct cause and geography

**Source tier and independence:** Tier 2 third-party archive of operator status updates. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://pingoru.io/providers/adyen/incidents/12310036

**Last reviewed:** 2026-11-18

---

## 2026-10-20 — Google Cloud London zone and downstream services

**Record type:** Non-malicious cloud outage  
**Routing:** Core / verified operator postmortem  
**Location / sector:** United Kingdom / Europe · Cloud / banking / payments / justice  
**System layer:** Cloud availability zone / power dependency

**Incident and chronology:** 20 October external electrical power failure in Google Cloud London zone disrupted cloud-hosted services; Bank of England and Revolut subsequently confirmed downstream UK financial-services, payment, cash-withdrawal and app impacts. Revolut reported backup failover did not work as intended.

**Operational effect:** Banking and payment access and remote court services disrupted; other downstream links not uniformly established.  
**Physical / data effect:** No malicious intrusion established.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Google Cloud incident report; Bank of England letter; Revolut postmortem. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Physical electrical cause; no cyberattack established. Not every payment-provider error can be attributed to this incident.

**Retrospective attribution and correction history:** 20 October Google Cloud electrical failure → 4 November Bank of England letter → 13 November Revolut technical postmortem. New provisional row / verification required; Reconciled 2026-11-18 — physical root cause and dated downstream confirmations

**Source tier and independence:** Tier 1 Google Cloud + Bank of England + Revolut. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://status.cloud.google.com/incidents/Xs2XTHzAVC9YnafnPyzj | https://www.bankofengland.co.uk/-/media/boe/files/letter/2026/letter-from-the-governor-to-dame-meg-hillier-4-november-2026.pdf | https://www.revolut.com/en-US/blog/post/20octoutagetechnicaloverview/

**Last reviewed:** 2026-11-18

---

## 2026-10-20 — SafePay ransomware campaign

**Record type:** Joint advisory / historical ransomware campaign  
**Routing:** Context / verified joint advisory  
**Location / sector:** Multinational · Critical infrastructure / enterprise IT / backup  
**System layer:** VPN / ransomware / backup

**Incident and chronology:** 20 October CISA/FBI/US Secret Service joint advisory describes SafePay ransomware operations since August 2024 and at least 600 affected organisations historically; this is not a new single 20 October attack.

**Operational effect:** Encryption, extortion and recovery disruption across reported historical victims; per-sector service impact varies.  
**Physical / data effect:** State sponsorship not established.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Original joint government advisory. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Historical 600-victim figure must not be counted as 600 October incidents.

**Retrospective attribution and correction history:** No new Iranian attribution established. New provisional row / verification required; Reconciled 2026-11-18 — advisory vs historical attacks

**Source tier and independence:** Tier 1 CISA/FBI/USSS. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://content.govdelivery.com/accounts/USDHSCISA/bulletins/42fd782

**Last reviewed:** 2026-11-18

---

## 2026-10-20 — Stripe / Revolut Pay (PayByBank unverified)

**Record type:** Payment-method service disruption / operator status archive  
**Routing:** Adjacent / qualified archival operator text  
**Location / sector:** United Kingdom / Europe / Brazil · Payments / banking  
**System layer:** Payment processing / upstream partner dependencies

**Incident and chronology:** Archived Stripe-origin status messages describe elevated Revolut Pay, 3D Secure and some Revolut-issued card errors on 20 October; upstream partner problems reported. PayByBank-specific operator impact has not been established independently.

**Operational effect:** Some payment authorisations, settlement or refunds degraded; not a general payment-system failure.  
**Physical / data effect:** Common cause across notices not established.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Operator-origin messages reproduced in third-party archive; original Stripe incident permalink not recovered. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Not a Stripe-wide outage; Google Cloud linkage is plausible in context but not conclusively demonstrated for every reported error; PayByBank unverified.

**Retrospective attribution and correction history:** 20 October Stripe-origin status notices; upstream partner cited; separate from Google Cloud root incident unless independently linked. New provisional row / verification required; Reconciled 2026-11-18 — split Stripe and Adyen; PayByBank remains unverified

**Source tier and independence:** Tier 2 third-party archive of operator status updates. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://isdown.app/status/stripe/incidents/672587-elevated-revolut-pay-errors

**Last reviewed:** 2026-11-18

---

## 2026-10-21 — GitLab self-managed

**Record type:** Security patch / vulnerability advisory  
**Routing:** Context / verified vendor advisory  
**Location / sector:** Global / European Union · Software development / CI-CD  
**System layer:** Source control / CI-CD

**Incident and chronology:** GitLab 21 October emergency patch release addresses critical CVE-2026-110264 and other vulnerabilities; no specific critical-infrastructure intrusion established by the advisory.

**Operational effect:** No confirmed service outage or successful exploitation in supplied account.  
**Physical / data effect:** Exposure potential, not established intrusion.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Original GitLab patch notice. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. Vulnerability advisory does not establish exploitation or an October attack on a named operator.

**Retrospective attribution and correction history:** No new Iranian attribution established. New provisional row / verification required; Reconciled 2026-11-18 — verified advisory not new attack

**Source tier and independence:** Tier 1 GitLab. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/

**Last reviewed:** 2026-11-18

---

## 2026-10-21 — LiteLLM PyPI and Docker distribution

**Record type:** Software supply chain compromise  
**Routing:** Adjacent / verified supply-chain compromise  
**Location / sector:** Global · AI gateway / cloud secrets / software supply  
**System layer:** Package distribution / release credentials

**Incident and chronology:** Malicious LiteLLM release 1.107.0 was distributed through package channels with credential-stealing functionality; vendor and Microsoft published technical analysis.

**Operational effect:** Potential credential theft and downstream code execution; no confirmed essential-service outage.  
**Physical / data effect:** Package distribution not equivalent to downstream compromise.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Vendor incident report and Microsoft technical analysis. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. No named essential-infrastructure victim established by these reports.

**Retrospective attribution and correction history:** No new Iranian attribution established. New provisional row / verification required; Reconciled 2026-11-18 — malicious release confirmed; downstream scope constrained

**Source tier and independence:** Tier 1 vendor + independent technical analysis. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://docs.litellm.ai/blog/security-incident-oct-21-2026 | https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/

**Last reviewed:** 2026-11-18

---

## 2026-10-21 — PHP2Shell / PHP server deployments

**Record type:** Vulnerability disclosure / unverified exploitation claims  
**Routing:** Context / verified vulnerability; exploitation unverified  
**Location / sector:** Global / United Kingdom / Japan · PHP / government / healthcare / finance / transport / public warning  
**System layer:** PHP web runtime / application servers

**Incident and chronology:** PHP 2026 security archive confirms CVE-2026-109618 and CVE-2026-109619; reported exploitation and Japanese emergency-alert suspensions remain insufficiently verified and should not be asserted as established consequences.

**Operational effect:** Reported defensive website, online banking, transport and public-warning service shutdowns; not evidence of compromise.  
**Physical / data effect:** Successful exploitation of production essential services unestablished.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: PHP primary archive confirms vulnerabilities only. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. No primary confirmation here of emergency-alert disruption, specific victim or active exploitation.

**Retrospective attribution and correction history:** No new Iranian attribution established. New provisional row / verification required; Reconciled 2026-11-18 — vulnerability confirmed; claimed operational impacts held

**Source tier and independence:** Tier 1 PHP for CVEs; downstream claims unresolved. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://www.php.net/archive/2026.php

**Last reviewed:** 2026-11-18

---

## 2026-10-22 — GMO Onamae.com Desktop Cloud

**Record type:** Cyber incident / impact update  
**Routing:** Core / verified operator notice  
**Location / sector:** Japan · Cloud hosting / financial trading  
**System layer:** Hosted desktops / customer trading credentials

**Incident and chronology:** GMO investigated unauthorised access from 19 October, identified malware on 20 October, took precautionary shutdown measures on 21 October and issued update on 22 October. Up to 26,739 hosted servers were potentially affected, not individually confirmed compromised.

**Operational effect:** Cloud-hosting plans suspended; reported trading-account consequences.  
**Physical / data effect:** 26,739 potentially affected servers not verified compromised; losses unknown.  
**Manual fallback:** Not established / not applicable

**Evidence / attribution:** Incident 🟠 Developing — source recheck; effect 🟠 Developing — source recheck; attribution ⚪ Open. Claim status: Original GMO Onamae.com operator notice. Technical actor: Unknown. Public government attribution: None established.

**Iran relevance and attribution:** Contextual / systemic relevance; not evidence of Iranian operation. No established Iranian connection. Not established

**Rival explanations / negative findings:** Criminal or opportunistic activity; unrelated provider failure; defensive isolation; independent actors. Assess per event. 26,739 is potential exposure count, not confirmed infected-server count; alleged customer account misuse requires separate evidence.

**Retrospective attribution and correction history:** 19 October investigation → 20 October malware identification → 21 October precautionary shutdown → 22 October operator update. New provisional row / verification required; Reconciled 2026-11-18 — server denominator and investigation chronology

**Source tier and independence:** Tier 1 operator. Prior watch summary, not independently corroborated for this update; do not treat repeated summaries as independent sources.

**Sources:** https://www.onamae.com/news/article/11593

**Last reviewed:** 2026-11-18

---

## 🗓️ November 2026 — source-qualified incident and advisory updates

**Coverage warning:** This section incorporates the 13-entry November editorial staging register, **not** an exhaustive November census. The 1–11 November interval remains incompletely audited. Contextual items and research gaps are listed separately below, not counted as incidents.

**Classification:** A = evidenced malicious activity; B = operational disruption without established malicious cause; C = advisory or defensive publication. These do not replace the underlying evidence and attribution fields.

---

## 2026-11-12–14 — Microsoft 365 / Outlook / Exchange

**Classification:** B · **Verification:** CORROBORATED — operator notice outstanding  
**Editorial decision:** STAGE QUALIFIED; no single blanket global outage claim

**Finding and operational/recovery evidence:** Microsoft service disruption including Outlook/Teams reported; precise service-health incident ID and scope not recovered in this pass

**Provenance:** Reuters citing Microsoft  
**Source:** https://www.reuters.com/world/us-official-says-recent-tech-woes-not-tied-cyberattacks-2026-11-17/

**Remaining uncertainty:** Original Microsoft service-health ID, service-by-service timeline

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-13 — FAA FTI telecommunications / nationwide ground stop

**Classification:** B · **Verification:** VERIFIED — primary  
**Editorial decision:** IMPORT; one event with ground stop as safety control

**Finding and operational/recovery evidence:** FAA reports ~15:30 ET onset; instability at 17 of 22 en-route centres; data flooding and router investigation; stop lifted 20:15 ET; no indications of cyberattack; all airborne aircraft landed safely

**Provenance:** FAA primary 13 and 15 Nov  
**Source:** https://www.faa.gov/newsroom/nationwide-ground-stop-questions-and-answers

**Remaining uncertainty:** Final root-cause report; contractor and equipment chain of custody

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-13 — FBI ARTEX FLASH

**Classification:** C · **Verification:** VERIFIED — primary  
**Editorial decision:** IMPORT as advisory, not 13 Nov attack

**Finding and operational/recovery evidence:** FBI FLASH-20261113-001 confirms malicious use of ARTEX autonomous penetration testing framework in earlier campaigns; no connection to FAA or November outages established

**Provenance:** FBI original PDF  
**Source:** https://www.ic3.gov/CSA/2026/261113.pdf

**Remaining uncertainty:** Individual campaign claims and downstream scope separately assess

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-13–14 — Workday WD1 production tenant disruption

**Classification:** B · **Verification:** VERIFIED — downstream operator  
**Editorial decision:** IMPORT qualified; one event

**Finding and operational/recovery evidence:** University operator reproduced Workday notice: disaster-recovery environment issue caused inconsistent production data and WD1 tenant maintenance; service available 14 Nov 10:30 local per FAU

**Provenance:** FAU OIT original status updates quoting Workday  
**Source:** https://wordpress.fau.edu/oit/2026/11/13/

**Remaining uncertainty:** Direct Workday postmortem, global tenant count

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-15 — AWS US-EAST-1 identity/connectivity

**Classification:** B · **Verification:** VERIFIED — primary  
**Editorial decision:** IMPORT one regional incident

**Finding and operational/recovery evidence:** AWS reports issues from 03:05 PST; most authentication restored 05:20; last affected NLB cell 06:21 PST; incident resolved; no malicious cause established

**Provenance:** AWS Health dashboard  
**Source:** https://health.aws.amazon.com/health/status

**Remaining uncertainty:** Root cause beyond service effects

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-16 — United Airlines departure technology failure

**Classification:** B · **Verification:** CORROBORATED — company statement via press  
**Editorial decision:** IMPORT QUALIFIED; distinct from FAA

**Finding and operational/recovery evidence:** United says technology issue delayed departing flights, resolved; flights in progress and United Express unaffected; no cyber indication

**Provenance:** CBS/AP quoting United  
**Source:** https://www.cbsnews.com/news/united-airlines-system-outage-departing-flights/

**Remaining uncertainty:** Original United dated operator notice and precise flight count

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-16 — JPMorgan Chase transaction processing

**Classification:** B · **Verification:** CORROBORATED — company statement via Reuters  
**Editorial decision:** IMPORT QUALIFIED; do not duplicate other bank complaints

**Finding and operational/recovery evidence:** JPMorgan attributes delayed transactions to software bug in on-premise systems; no cyber evidence; other banks complaints not separate confirmed outages

**Provenance:** Reuters quoting JPMorgan and US Bank  
**Source:** https://www.reuters.com/legal/transactional/downdetector-reports-outages-major-us-banks-2026-11-16/

**Remaining uncertainty:** Original JPMorgan incident statement and final recovery time

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-17 — NSA internal communications degradation

**Classification:** B · **Verification:** CORROBORATED — agency statement via Reuters  
**Editorial decision:** IMPORT QUALIFIED; not an established intrusion

**Finding and operational/recovery evidence:** NSA says scheduled-maintenance degradation affected some internal systems, mission-critical capabilities operational

**Provenance:** Reuters quoting NSA  
**Source:** https://www.reuters.com/technology/highly-classified-us-national-security-communications-network-is-down-cnn-2026-11-17/

**Remaining uncertainty:** Original NSA notice, exact duration and technical cause

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-17 — Apple services internal update disruption

**Classification:** B · **Verification:** CORROBORATED — company statement via Reuters  
**Editorial decision:** IMPORT QUALIFIED; one operator event

**Finding and operational/recovery evidence:** Apple attributes disruption to internal update, affecting iCloud and Apple Pay among services; says not cyberattack

**Provenance:** Reuters quoting Apple  
**Source:** https://www.reuters.com/business/retail-consumer/apple-works-restore-services-after-outage-caused-by-internal-update-2026-11-17/

**Remaining uncertainty:** Official archived status entries and exact recovery times

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 2026-11-16–17 — Cloudflare separate status incidents

**Classification:** B · **Verification:** VERIFIED — operator history  
**Editorial decision:** STAGE as separate operator incidents, do not count as one global outage

**Finding and operational/recovery evidence:** Cloudflare lists distinct incidents including 17 Nov Turnstile, Gateway regionalized domains, and LAX/FRA network performance; no common cause established

**Provenance:** Cloudflare official status history  
**Source:** https://www.cloudflarestatus.com/history

**Remaining uncertainty:** Individual incident permalinks and downstream effect threshold

**Iran attribution:** None established by the cited November event evidence. A coincident advisory or service failure is not proof of a common campaign.

---

## 🗂️ November context and unresolved research — excluded from incident counts

- **NOV-11 — Iran-related Washington DC threat reporting (CONTEXT):** Reporting of potential threats is not an infrastructure incident; official credibility assessments and exact claims need checking **Disposition:** DO NOT IMPORT AS INCIDENT.
- **NOV-12 — AI/Nvidia procurement, rollout, staffing hypotheses (CONTEXT):** No technical evidence tying launches, staffing changes or AI deployment to the listed failures **Disposition:** KEEP IN NARRATIVE ONLY.
- **NOV-13 — Earlier-November coverage gap (RESEARCH):** November 1–11 not systematically audited; absence of rows is not absence of incidents **Disposition:** OPEN RESEARCH QUEUE.

---

## 🧭 October–November cross-cluster analysis — interpretation, not incident evidence

The following analysis compares **mechanisms, dependencies, operational continuity and attribution limits**. It does not change any incident-level classification or establish a coordinated campaign.

## 🔎 Evidence boundary — read this first
The chronology records distinct **A — malicious activity**, **B — operational disruption without established malicious cause**, and **C — advisories, vulnerabilities and protective developments**. These labels describe *what is evidenced*, not who is responsible. A research publication, a retrospective disclosure, a recovery notice and an operational outage are not four new attacks. Publication date, event onset, detection, recovery and later attribution must remain separate.

The observations below are **cross-record analysis**. They do not add incidents or override the source and confidence fields of any individual record.

## 🕸️ Cross-cluster observations

| Analytical theme | Evidence anchors in the reconciled records | What can reasonably be inferred | What cannot be inferred |
|---|---|---|---|
| **Shared-provider dependencies** | 20 Oct Google Cloud London external electrical power failure; documented Revolut effects and Stripe/Revolut Pay errors; 15 Nov AWS US-EAST-1 identity/connectivity disruption | Dependencies on regional cloud and payment infrastructure can transmit effects beyond the initial failed component; redundancy and failover merit examination | That the London and US incidents shared a trigger, attacker or campaign; that Adyen's Australian Eftpos maintenance issue was part of the London event |
| **Administrative access and software supply chains** | October ConnectWise cloud administrative identities, UpdraftCentral key compromise, LiteLLM malicious package release, GMO Desktop Cloud malware; GitLab patch notice as C | Identity, remote-management privileges and distribution channels are recurring *exposure pathways* with potentially wide downstream reach | That all potentially exposed tenants were compromised, or that an advisory proves a named infrastructure victim |
| **Operational continuity and protective controls** | Vicksburg ransomware and municipal payment interruption; bankruptcy-noticing service disruption and restoration; November FAA precautionary ground stop; Workday WD1 maintenance | Shutdowns, manual alternatives, restrictions and restoration are material outcomes and safeguards; recovery time can matter as much as the initial trigger | That every precautionary closure is a second attack, or that the FAA ground stop itself establishes sabotage |
| **Cyber–physical and service-layer boundaries** | French supermarket refrigeration controllers; Google Cloud electrical supply failure; November airline, bank and Apple service problems | Physical equipment, enterprise IT, hosted platforms and consumer-facing services require separate effect and causation fields | That a physical power failure is cyberattack, or that an online payment error means settlement infrastructure was compromised |
| **Threat research versus observed attacks** | 6 Oct Unit 42 Blinder Tunnel publication on earlier activity; 6 Oct FortiBleed continuing-threat warning; 20 Oct SafePay advisory; 13 Nov FBI ARTEX FLASH | Advisories help explain attack methods and defensive priorities, but their dates chiefly identify *publication* | That a campaign described in October or November newly attacked essential infrastructure on the publication date; that ARTEX caused the FAA outage |
| **Attribution evolves after the event** | Later reported French-government IRGC attribution for refrigeration-controller compromises; Unit 42's Iranian-nexus assessment for Blinder Tunnel | Retrospective attribution may change an individual record's evidentiary status and must be dated and attributed to the assessor | That these findings transfer Iranian attribution to unrelated October or November failures |

## 🧩 Mechanism matters more than proximity

The recurring *questions* are identifiable: Where did access concentrate? Which supplier or identity system had authority over many downstream organisations? Did failover work? Was a shutdown an impact or a deliberate safety control? Which services recovered first, and which remained impaired? These are useful comparisons even when the incidents have different causes.

A disciplined causal account separates **trigger → preconditions → amplifiers → operational effects → protective response → recovery**. The 20 October Google Cloud/Revolut relationship has direct supporting evidence for downstream dependency. The contemporaneous Adyen/Eftpos disruption has a separately reported maintenance explanation; proximity alone is not a link. Similarly, the 13 November FAA telecommunications event and 16 November United Airlines departure-system issue remain distinct.

## 🇮🇷 Iran-war relevance and attribution boundary

The war context explains why resilience, targeting and strategic signalling deserve attention. It **does not provide actor attribution**. The reconciled set contains malicious incidents, non-malicious failures, uncertain causes and protective advisories. There is **no established common operator or coordinated Iranian campaign spanning the October–November records**. The French refrigeration attribution is a *specific later claim*; Unit 42's Iranian-nexus assessment is *research attribution* with its own confidence limits. Neither is a licence to reclassify neighbouring records.

Nor does this staging set establish a rising rate of attacks. October has been systematically reconciled against its 28-record baseline, while 1–11 November has not received equivalent coverage. Record totals also mix different event types. **Comparing raw counts would be misleading.**

## 🛠️ Publication and research controls

- Keep this annex **after** incident-level evidence and clearly marked as analysis; do not insert its inferences into `Claimed Actor`, `Public Government Attribution` or `Strategic Campaign Confidence` fields.
- Preserve operator/agency statements, third-party reproductions, technical research and retrospective reporting as different source-provenance classes.
- Avoid duplicate counts for follow-up disclosures, restored services, downstream symptoms and precautionary restrictions.
- Finish the 1–11 November audit and remaining original operator identifiers before any quantitative comparison or stronger campaign-level conclusion.
- Keep uncertainty visible: missing public proof is not proof of impossibility, but it is not permission to assert causation.

## 🌌 Constellations

⏱️ 🕸️ 🚰 🧬 🤖 — chronology; attribution; operational technology; overlapping threat ecosystems; AI-assisted capability diffusion.

---

## ✨ Stardust

critical infrastructure, cyber incidents, iran, attribution, operational technology, ransomware, access brokerage, supply chain, ai-assisted attacks, cyber-to-physical effects

---

## 🏮 Footer

*⏱️ Timeline of Essential Infrastructure Attacks* is a living node of the **Polaris Protocol**.  
It provides the chronological evidentiary spine for the *🇮🇷 Data Wars: IRGC Edition* pack, preserving incident, effect, attribution, relationship, campaign significance and legal routing as separate but connected questions.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope, inclusion and routing rules*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *graded attribution across operators, customers and states*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *OT depth, control access and physical effects*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *separating concurrent state-linked, criminal and access-market ecosystems*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *cumulative strategic burden without false unification*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *public reporting discipline under uncertain attribution*
> - [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *source provenance and correction history*
>
> 🏮 Return To:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *1up*
> - [🌊 Playing Defence](../README.md) — *2up*
> - [📲 Press Matters](../../README.md) — *3up*
> - [🌓 In The Moment](../../../README.md) — *4up*
> - [🌌 Polaris Protocol — Root](../../../../README.md) — *root*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-11-18_
