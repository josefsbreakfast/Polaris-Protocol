# ⏱️ Timeline Of Essential Infrastructure Attacks
**First created:** 2026-08-01 | **Last updated:** 2026-09-14  
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

## 🌌 Constellations

⏱️ 🕸️ 🚰 🧬 🤖 — chronology; attribution; operational technology; overlapping threat ecosystems; AI-assisted capability diffusion.

---

## ✨ Stardust

critical infrastructure, cyber incidents, iran, attribution, operational technology, ransomware, access brokerage, supply chain, ai-assisted attacks, cyber-to-physical effects

---

## 🏮 Footer

*⏱️ Timeline Of Essential Infrastructure Attacks* is a living node of the **Polaris Protocol**.  
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

_Last updated: 2026-09-14_
