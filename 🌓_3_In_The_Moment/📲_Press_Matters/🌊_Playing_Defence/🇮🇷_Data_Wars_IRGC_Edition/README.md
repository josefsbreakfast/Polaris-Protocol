# 🇮🇷 Data Wars: IRGC Edition
**First created:** 2026-08-01 | **Last updated:** 2026-09-14  
*Tracking essential-infrastructure cyber disruption across the widening Iran war without turning wartime proximity, actor branding, target overlap, or political convenience into proof.*

---

## 🛰️ Orientation

This pack tracks cyber incidents affecting the systems through which states and ordinary life continue to function during the Iran war.

That means more than defence networks.

It includes:

- water and wastewater;
- energy and industrial control;
- healthcare and medical supply;
- education and public records;
- government administration;
- policing and justice;
- transport, ports and logistics;
- telecommunications;
- banking and payments;
- identity and authoritative records;
- shared software;
- suppliers and integrators;
- and the contracted infrastructure that keeps those functions operating.

The war did not begin in cyberspace.

It does not remain neatly outside it either.

Iranian and Iran-linked cyber activity can be decentralised, deniable, layered through state units, affiliated groups, contractors, proxies, access brokers, hacktivist branding, commercial operators, criminal intermediaries, and people who may not know who ultimately benefits from the task they have been given.

But the same wartime attack surface also contains:

- ordinary ransomware;
- shared-vulnerability waves;
- access manufacturing;
- other state-linked contractor ecosystems;
- unrelated criminal activity;
- copycats;
- actor claims that ride real outages;
- supplier compromise;
- and incidents whose operator may never become public.

The pack therefore refuses two opposite mistakes:

```text
attribute every badly timed breach to Iran
```

and:

```text
treat every unattributed breach as strategically meaningless
```

Its governing discipline is:

```text
preserve the incident
+
preserve the effect
+
preserve the uncertainty
+
preserve the pattern
+
preserve the rival explanation
```

No single field is allowed to swallow the others.

---

## 🧭 What The Pack Contains

The pack now has four interacting layers.

### The Evidence Spine

The evidence spine records:

- incidents;
- clusters;
- attribution developments;
- context events;
- operational effects;
- physical and data effects;
- rival explanations;
- source provenance;
- review history;
- correction status;
- and relationship confidence.

The canonical portable dataset is:

- [📊 Timeline CSV](./📊_iran_war_essential_infrastructure_cyber_timeline.csv)

The aligned spreadsheet is:

- [📊 Timeline XLSX](./📊_iran_war_essential_infrastructure_cyber_timeline.xlsx)

As at **14 September 2026**, the working dataset contains:

```text
50 RECORDS
40 FIELDS
```

The human-readable chronology is:

- [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md)

The source-audit layer is:

- [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md)

The record count is a description of the present evidence spine.

It is not a count of Iranian attacks.

### The Analytical Layer

The analytical nodes explain:

- what counts as state infrastructure;
- when cyber reaches machinery;
- how small disruptions accumulate;
- how one war contains several threat ecosystems;
- how access can be manufactured before a later customer exists;
- how an operator, commissioner, payer, buyer and beneficiary may differ;
- and why campaign effect can become clear before common-command confidence does.

### The Public And Legal Layer

These nodes explain:

- how to report unresolved attribution;
- how confidence labels work;
- how IHL questions should be separated from war-crime claims;
- how effects reach civilians and public institutions;
- and how public language can remain durable when attribution changes.

### The Governance And Alliance Layer

The pack also now tracks the defender side.

That includes:

- fragmented British responsibility;
- American domestic-security externalities;
- presidential attribution and regulatory posture;
- allied hedging;
- alliance-response coherence;
- and the transaction cost created when previously coordinated positions become less predictable.

Those are not cyber incidents.

They can materially change the environment in which cyber incidents are prevented, attributed, contained and answered.

The result is not merely an incident list.

It is a live evidence architecture.

---

## 🚦 Four Routing Outcomes

Not every relevant development belongs in the same evidentiary category.

### Core

An actual cyber incident affecting an essential function, system, state-held information layer, operational dependency, or protected civilian service.

Examples include:

- service disruption;
- OT access;
- forced manual fallback;
- hospital diversion;
- physical-process effect;
- state-record compromise;
- or material degradation of an essential provider.

### Adjacent

A strategically relevant event that does not yet clear the threshold for a core essential-infrastructure incident.

Examples include:

- supplier compromise without downstream operational effect;
- reconnaissance without exploitation;
- access manufacturing without demonstrated later strategic use;
- a logistics breach without port-control impact;
- or a financial-sector claim without payment-system disruption.

### Context

A development that changes:

- attribution;
- motive;
- exposure;
- policy;
- regulation;
- rhetoric;
- alliance behaviour;
- legal interpretation;
- or defender capacity

without itself being a new cyber incident.

### Excluded

A duplicate, false claim, unsupported item, unrelated technical failure, out-of-scope event, or source chain that cannot sustain the proposed description.

The routing rule is:

```text
relevant enough to watch
≠
strong enough to count

strong enough to count
≠
strong enough to attribute

strong enough to attribute
≠
strong enough to establish state direction
```

---

## 🧩 Linked Record Objects

The pack now distinguishes several objects that may share a date without belonging in one row.

```text
INCIDENT
what happened to one system or organisation

CLUSTER
what recurs across several incidents

ATTRIBUTION DEVELOPMENT
how operator, affiliation, direction and confidence change

CONTEXT DEVELOPMENT
how policy, rhetoric, regulation, war posture or alliance behaviour changes

ACCESS DEVELOPMENT
how credentials, footholds or data are created, transferred or reused

STAKEHOLDER CONSEQUENCE
who carries the service, financial, political, military or alliance effect
```

A responsibility claim can change attribution history without producing a new operational effect.

A software campaign can create access without yet creating service disruption.

A political statement can alter allied confidence without changing the technical facts of an intrusion.

A cluster can become established while common authorship remains open.

---

## 🔎 Confidence Belongs To The Proposition

A cyber incident does not have one confidence level.

Use:

```text
🟢 ESTABLISHED / CONFIRMED
🟡 PROBABLE
🟠 SUSPECTED / DEVELOPING
⚪ OPEN / UNATTRIBUTED
❌ EXCLUDED
```

And keep:

```text
📣 ACTOR-CLAIMED
```

as a separate claim-status modifier.

A record may therefore say:

```text
INCIDENT:
🟢 ESTABLISHED

PHYSICAL EFFECT:
🟢 ESTABLISHED

TECHNICAL OPERATOR:
🟡 PROBABLE

COMMON CUSTOMER:
⚪ OPEN

FORMAL STATE DIRECTION:
⚪ NOT PUBLICLY ESTABLISHED
```

The pack also separates:

```text
PATTERN CONFIDENCE:
ORGANISING-MECHANISM CONFIDENCE:
COMMON-OPERATOR CONFIDENCE:
COMMON-CUSTOMER CONFIDENCE:
COMMON-SPONSOR CONFIDENCE:
SHARED-DEFENDER-BURDEN CONFIDENCE:
```

Those answers may move at different speeds.

---

## 🧬 One War Does Not Mean One Threat Ecosystem

By 14 September, the environment is **more differentiated**, not less.

### 🚰 Iran-Linked / Suspected-Iran Water OT

The US water wave remains the strongest Iran-facing operational cluster.

The public record now includes:

- repeated access to internet-facing PLCs;
- configuration or credential changes;
- monitoring / control loss;
- manual fallback;
- some physical-process effects;
- a Minnesota/core wave with strengthened Iran-linked indicators;
- prior US government reporting linking CyberAv3ngers to IRGC-affiliated activity;
- actor claims from APT IRAN / CyberAv3ngers;
- and a late-August CISA disclosure that more than **100 internet-exposed water and wastewater systems** were targeted in July.

That supports:

```text
WATER / OT PATTERN:
🟢 ESTABLISHED

100+ SYSTEM SCALE:
🟢 ESTABLISHED

IRAN-LINKED CORE:
🟡 PROBABLE / STRENGTHENED

ONE COMMON OPERATOR ACROSS 100+:
⚪ NOT ESTABLISHED

FORMAL PUBLIC ATTRIBUTION OF EVERY INCIDENT:
⚪ NOT ESTABLISHED
```

### ⚡ Iran-Linked Energy / Telecom Expansion

By early September, reporting described increased Iranian government-linked attempts against:

- electricity;
- telecommunications;
- and other critical infrastructure.

The newest tranche is more strongly characterised by:

- access;
- reconnaissance;
- capability development;
- and widening target scope

than by a sequence of major confirmed outages.

### ⚡ UK Generator

A cyberattack forced a small British generator offline for four days.

The wider grid was not threatened.

Reporting described the attackers as Iran-linked.

A formal public NCSC attribution naming Iran, the IRGC, or a specific operator was not identified in the reviewed record.

This is a genuine cyber-to-physical energy case.

It is not proof of one common US/UK operator.

### 🏥 Healthcare Ransomware / Data

AnMed, Manitoba, Nutex, Luminis and Veradigm show:

- ransomware;
- facility-support disruption;
- ambulance diversion;
- delayed or cancelled treatment;
- sensitive-data theft;
- and third-party credential abuse.

No common Iran sponsorship is established.

### 🏛️ Administrative / Justice Exposure

Berlin and C-Track show:

- administrative disruption;
- public-service delays;
- sensitive record access;
- later credential publication;
- and shared-provider concentration.

Again, one common operator is not established.

### 🤖 Shared-Software Access Manufacturing

The September PaperCut campaign demonstrates:

```text
shared software
→ AI-assisted mass exploitation
→ credentials / domain secrets
→ privileged footholds
```

across hundreds of organisations.

The victim population included:

- government;
- education;
- healthcare;
- finance;
- industrial;
- energy;
- and other sectors.

The current evidence supports access manufacturing.

It does not establish a later state customer.

### 🇨🇳 Separate State-Linked Contractor Ecosystem

QScan / QTRouter adds a distinct China-linked hacker-for-hire / contractor architecture affecting overlapping sectors.

That matters because:

```text
same sector
≠
Iran-specific signature
```

Target overlap becomes less distinctive as attribution evidence when several state-linked ecosystems are known to be operating against the same classes of infrastructure.

### 📣 Narrative Ride-Along

APT IRAN claimed a real AT&T outage.

AT&T rejected the cyber explanation and attributed the outage to attempted physical cable theft.

Therefore:

```text
REAL OUTAGE
+
REAL CLAIM
≠
REAL CAUSATION
```

The claim itself remains strategically relevant because it changes the information environment.

### ⚓ Iran-Nexus Naval Reconnaissance

Anthropic disclosed Iran-nexus use of Claude for:

- naval tracking;
- ship and aircraft movement;
- personnel research;
- maritime VSAT;
- Cisco communications;
- and industrial-control-product research.

No confirmed exploitation or operational effect was publicly established.

So:

```text
RECONNAISSANCE:
🟢 DISCLOSED

EXPLOITATION:
⚪ NOT ESTABLISHED

OPERATIONAL EFFECT:
⚪ NOT ESTABLISHED
```

### 🌍 Alliance / Governance Seam

The threat environment also includes a defender-side seam.

If previously coordinated allied positions become less predictable, partners may:

- hedge;
- duplicate planning;
- delay commitments;
- become more cautious about shared attribution;
- or retain capability nationally.

No adversary needs to have caused the divergence to benefit from it.

Keep:

```text
ADVERSARY BENEFIT
≠
ADVERSARY CAUSATION
```

visible.

---

## 🚰 The Control Layer Changes The Threshold

The pack distinguishes:

```text
ADMINISTRATIVE IT
→ records
→ communications
→ scheduling
→ billing
→ business systems

OPERATIONAL TECHNOLOGY
→ controllers
→ sensors
→ pumps
→ valves
→ generation
→ treatment
→ physical processes
```

Both layers matter.

OT creates a more direct path from intrusion to physical effect.

Use the depth ladder:

```text
LEVEL 0 — EXTERNAL RECONNAISSANCE
LEVEL 1 — IT / ADMINISTRATIVE ACCESS
LEVEL 2 — OT NETWORK VISIBILITY
LEVEL 3 — HMI / CONTROL INTERFACE ACCESS
LEVEL 4 — CONTROLLER / CONFIGURATION ACCESS
LEVEL 5 — COMMAND / SETTING MANIPULATION
LEVEL 6 — OBSERVED PHYSICAL-PROCESS CHANGE
LEVEL 7 — SAFETY / SERVICE / PHYSICAL HARM
```

Do not infer Level 6 from evidence that establishes only Level 2.

Manual fallback can mean:

```text
resilience worked
```

and:

```text
normal control was degraded
```

at the same time.

---

## 📉 Campaign Effect Can Arrive Before Common Command

The pack now distinguishes:

```text
CUMULATIVE CAMPAIGN EFFECT
```

from:

```text
COMMON OPERATOR
```

and:

```text
COMMON SPONSOR
```

The defender may be handling:

- Iran-linked OT activity;
- criminal ransomware;
- China-linked contractor activity;
- shared-software mass exploitation;
- supplier compromise;
- false actor claims;
- and political / alliance coordination costs

inside one finite queue.

That supports:

```text
SHARED DEFENDER BURDEN:
🟢 ESTABLISHED
```

without proving:

```text
ONE HOSTILE COMMAND STRUCTURE:
NO
```

The campaign effect is now easier to establish than the campaign command structure.

---

## 🧅 Attribution Is A Stack

The pack separates:

```text
technical operator
→ tooling / infrastructure
→ group or alias
→ access broker
→ intermediary
→ contractor / proxy
→ task originator
→ commissioner
→ payer / procurement route
→ customer
→ later user
→ state relationship
→ state direction
→ final beneficiary
```

Identifying one layer does not automatically identify the next.

Keep:

```text
CRIMINAL OPERATOR
≠
NO STATE CUSTOMER

CRIMINAL OPERATOR
≠
STATE CUSTOMER

IRAN-LINKED OPERATOR
≠
IRAN DIRECTED THIS OPERATION

LATER STATE USE
≠
ORIGINAL STATE TASKING
```

visible.

---

## 👾 Legal Significance Also Has Layers

Cyber operations do not sit outside international humanitarian law merely because the weapon is code.

But:

```text
CYBER INCIDENT
≠
CYBER OPERATION REGULATED BY IHL
≠
CYBERATTACK FOR IHL PURPOSES
≠
IHL VIOLATION
≠
WAR CRIME
```

And:

```text
STATE RESPONSIBILITY
≠
INDIVIDUAL CRIMINAL RESPONSIBILITY
```

Water, healthcare, telecoms, energy and other civilian systems may warrant serious IHL review.

That does not permit the pack to skip the armed-conflict nexus, target-status, attribution, breach, mental-element, or jurisdiction questions.

---

## 🗺️ The Operational War Map Is Wider Than The Formal War

The United States and Israel are the central direct belligerents.

The wider tracking perimeter includes states Iran may regard as participating where they:

- host forces;
- provide basing;
- provide logistics;
- provide intelligence;
- conduct interception or air defence;
- support maritime activity;
- participate in sanctions;
- or otherwise constrain Iran's ability to retaliate.

Keep:

```text
Iranian perception of participation
≠
operational support
≠
political alignment
≠
legal belligerency
```

separate.

The September update also adds an inward map:

```text
HOW CONFIDENT ARE ALLIES
THAT PREVIOUSLY COORDINATED POSITIONS
WILL STILL HOLD?
```

That question belongs to alliance resilience.

It does not alter legal belligerency.

---

## 🇺🇸 The American Governance Problem

The American layer now contains a measurable policy tension.

The administration formally supports:

- critical-infrastructure hardening;
- denial of adversary initial access;
- offensive and defensive cyber capability;
- and public-private coordination.

It also formally prioritises:

- regulatory streamlining;
- reduced compliance burden;
- private-sector agility;
- and presidential freedom of action.

Those preferences can coexist.

They become harder to reconcile where:

- vulnerable OT remains exposed;
- more than 100 water systems are targeted;
- AI lowers the cost of hostile discovery and exploitation;
- and federal agencies absorb the national-security cost of weak local or private security decisions.

The live question is therefore:

> **What happens when “get government out of the way” collides with “nobody gets to fuck with America”?**

The node does not need a secret motive to make that contradiction worth tracking.

---

## 🇬🇧 Britain And The Exploitable Seam

Britain may possess substantial cyber, defence, intelligence, regulatory and investigative capability while responsibility remains fragmented across:

- departments;
- regulators;
- private suppliers;
- police;
- national-security structures;
- and allied relationships.

The seam is not lack of capability.

It is the risk that:

> excellent institutions complete their own part while nobody owns the relationship between all the completed parts.

That can apply domestically and across alliances.

---

## 📰 Reporting Rule

> **Do not attribute beyond the evidence. Do not erase a developing strategic pattern merely because public attribution is incomplete.**

And:

> **Do not treat a real claim as real causation merely because a real incident exists nearby.**

And:

> **Do not call an incident a war crime merely because the target is civilian, the timing is wartime, or the suspected actor is Iranian.**

And:

> **Do not describe allied hedging as alliance collapse merely because coordination has become more expensive.**

Where information is missing, distinguish:

```text
UNKNOWN
NOT PUBLIC
NO EVIDENCE FOUND
WITHHELD / NCND
NOT APPLICABLE
```

Repetition is not corroboration.

Source provenance matters.

---

## 🧾 Current Evidence Trail

The full proposition-level register is maintained in:

- [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md)

The principal evidence routes now include:

### Government And Technical

- [FBI: malicious actors targeting internet-facing water and wastewater PLCs](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)
- [CISA and partners: IRGC-affiliated CyberAv3ngers activity](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)
- [CISA: Iranian-affiliated PLC exploitation](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)
- [CISA: active threat to Siemens S7-series PLCs](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a)
- [White House: “President Trump's Cyber Strategy for America”](https://www.whitehouse.gov/wp-content/uploads/2026/03/president-trumps-cyber-strategy-for-america.pdf)
- [White House: Gold Eagle Initiative](https://www.whitehouse.gov/releases/2026/07/white-house-launches-gold-eagle-initiative-for-unprecedented-cybersecurity-vulnerability-coordination/)
- [U.S. GAO: cybersecurity regulations and duplicative reporting](https://www.gao.gov/products/gao-26-108606)

### Reporting / Attribution

- [Reuters: Minnesota coordinated water attack](https://www.reuters.com/legal/litigation/minnesota-it-officials-disclose-coordinated-cyberattack-more-than-30-local-water-2026-07-28/)
- [Washington Post: US intelligence suspicion of Iran](https://www.washingtonpost.com/national-security/2026/07/30/us-spy-agencies-suspect-iran-launched-cyberattack-minnesota-water-facilities/)
- [KSTP: APT IRAN / CyberAv3ngers claim](https://kstp.com/kstp-news/top-news/hacking-group-linked-to-iran-claims-responsibility-for-cyberattack-on-minnesota-water-systems-report-says/)
- [Reuters: Trump rejects Iran attribution](https://www.reuters.com/world/us/trump-says-iran-not-blame-minnesota-cyber-attack-2026-07-31/)
- [Reuters: AI-enhanced energy-sector cyberattacks](https://www.reuters.com/business/energy/energy-firms-face-ai-enhanced-cyber-attacks-connectivity-push--reeii-2026-09-01/)

### UK

- [BBC: “Cyber attack shut down small power plant”](https://www.bbc.co.uk/news/articles/ce9793g34yvo)
- [NCSC: UK organisations urged to bolster cyber resilience amid Iran conflict](https://www.ncsc.gov.uk/news/uk-organisations-urged-bolster-cyber-resilience-amid-iran-conflict)

The register should be used where exact proposition provenance matters.

The README should remain orientation, not become a second evidence ledger.

---

## 📂 Pack Map

### Start Here

- [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope, routing, inclusion, exclusions and live watch categories*
- [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *the current ecosystem map*
- [🗺️ Who Iran Sees As Inside The War](./🗺️_who_iran_sees_as_inside_the_war.md) — *the operational coalition map and inward alliance map*

### Evidence Spine

- [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *human-readable chronology through 14 September 2026*
- [📊 Timeline CSV](./📊_iran_war_essential_infrastructure_cyber_timeline.csv) — *canonical 50-record / 40-field portable dataset*
- [📊 Timeline XLSX](./📊_iran_war_essential_infrastructure_cyber_timeline.xlsx) — *aligned spreadsheet register*
- [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *proposition-level source, negative-finding and rival-explanation audit trail*

### Attribution And Method

- [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md) — *proposition-specific confidence and source rules*
- [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *technical, organisational, commissioning, customer and state attribution*
- [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *access brokers, commissioners, payers, later users and final beneficiaries*
- [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *language-control layer*
- [🌊 Riding Every Wave](./🌊_riding_every_wave.md) — *causal downstream use, narrative ride-alongs and governance seams*

### Infrastructure And Effects

- [🏗️ What Counts As State Infrastructure](./🏗️_what_counts_as_state_infrastructure.md) — *functional inclusion without automatic targetability*
- [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *OT depth, physical effect and manual fallback*
- [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *cumulative pressure, buffer depletion and shared defender burden*
- [⛴️ Do Ports Count?](./⛴️_do_ports_count.md) — *ports, logistics and enterprise-IT / OT distinctions*
- [🏦 Banks Are Part Of The Battlespace](./🏦_banks_are_part_of_the_battlespace.md) — *payments, decision integrity and financial transmission*
- [🏥 Health, Education And Admin Are Not Soft Extras](./🏥_health_education_and_admin_are_not_soft_extras.md) — *care, records, identity and person-centred recovery*

### Law, Governance And Stakeholders

- [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *IHL relevance, attribution and individual criminal responsibility kept separate*
- [🇬🇧 Britain Is Advertising An Exploitable Seam](./🇬🇧_britain_is_advertising_an_exploitable_seam.md) — *fragmented responsibility and alliance seams*
- [🇺🇸 Potential Impacts On Americans](./🇺🇸_potential_impacts_on_americans.md) — *domestic, financial, military and alliance consequences*
- [🍊 Why Is the Orange Being Weird?](./🍊_why_is_the_orange_being_weird.md) — *the US governance contradiction: resilience, deregulation, attribution and presidential optionality*

---

## 🧪 How To Use The Pack

For a new incident:

1. Begin with [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) and route the item as Core, Adjacent, Context or Excluded.
2. Use [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md) to separate incident, effect, relationship, operator, pattern, campaign and defender-burden confidence.
3. Use [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) and [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) before moving from operator to customer, commissioner, sponsor or state direction.
4. Use [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) where OT, monitoring, control, configuration, set-points or physical processes are involved.
5. Use [🌊 Riding Every Wave](./🌊_riding_every_wave.md) where one incident may be causally downstream from another without sharing a command structure.
6. Use [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) before treating sector overlap as one campaign.
7. Amend the CSV first, reproduce the same ordered record in the XLSX, and preserve attribution and correction history.
8. Update the human-readable timeline where the event changes the chronology.
9. Update [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) where the evidence base materially changes.
10. Propagate material corrections into every node where the previous assessment performs analytical work.

For reporting:

1. Name who knows each fact.
2. Distinguish event from effect.
3. Distinguish claim from causation.
4. Distinguish reconnaissance from exploitation.
5. Distinguish pattern from sponsor.
6. Preserve negative findings.
7. Preserve rival explanations.
8. Do not inherit attribution across a cluster.
9. Do not turn allied hedging into alliance collapse.
10. Do not turn civilian harm into a war-crime conclusion without the legal chain.

---

## 🧠 Current Pack Assessment — 14 September 2026

```text
US WATER / OT PATTERN:
🟢 ESTABLISHED

100+ WATER-SYSTEM TARGET SCALE:
🟢 ESTABLISHED

IRAN-LINKED CORE WATER ATTRIBUTION:
🟡 PROBABLE / STRENGTHENED

ENERGY / TELECOM TARGETING EXPANSION:
🟡 / 🟢 DEVELOPING

UK CYBER-TO-PHYSICAL ENERGY EFFECT:
🟢 ESTABLISHED

HEALTHCARE OPERATIONAL / DATA EFFECTS:
🟢 ESTABLISHED ACROSS SEPARATE INCIDENTS

SHARED-SOFTWARE ACCESS MANUFACTURING:
🟢 ESTABLISHED

CHINA-LINKED CONTRACTOR / HACKER-FOR-HIRE ECOSYSTEM:
🟢 ESTABLISHED

NARRATIVE RIDE-ALONG:
🟢 ESTABLISHED

IRAN-NEXUS NAVAL / ICS RECONNAISSANCE:
🟢 DISCLOSED

CUMULATIVE DEFENDER BURDEN:
🟢 ESTABLISHED

ALLIANCE / GOVERNANCE SEAM:
🟡 DEVELOPING

ONE COMMON OPERATOR ACROSS DATASET:
⚪ NOT ESTABLISHED

ONE COMMON CUSTOMER:
⚪ NOT ESTABLISHED

ONE COMMON COMMISSIONER:
⚪ NOT ESTABLISHED

ONE COMMON STATE SPONSOR:
⚪ NOT ESTABLISHED
```

The strongest current synthesis is therefore:

> **The Iran-facing infrastructure problem is real and widening, but it sits inside a much larger multi-actor threat environment. The campaign effect is easier to establish than one common command structure.**

That is the pack's current centre of gravity.

---

## 🌌 Constellations

🕸️ 🚰 ⚡ 🏥 🤖 ⚖️ 📉 🌍 — cyber attribution; operational technology; energy; healthcare; access manufacturing; civilian protection; cumulative pressure; alliance resilience.

*Follow the evidence:*

- [📰: Washington Post: “Water systems are ripe for cyberattacks, experts warn after suspected Iranian hacks”](https://www.washingtonpost.com/national-security/2026/08/10/us-water-systems-are-low-hanging-fruit-cyberattacks-experts-warn-after-suspected-iranian-hacks/)
- [📰: Wall Street Journal: “The Cyberattack That Brought a Distant War to Small-Town Minnesota”](https://www.wsj.com/politics/national-security/the-cyberattack-that-brought-a-distant-war-to-small-town-minnesota-66451b93)
- [📰: Reuters: “Trump says Iran not to blame for Minnesota cyberattack”](https://www.reuters.com/world/us/trump-says-iran-not-blame-minnesota-cyber-attack-2026-07-31/)
- [🏛️: CISA: “Defending Against an Active Threat to Siemens S7 Series PLCs”](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a)
- [🏛️: CISA and partners: “IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors”](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)
- [📰: BBC: “Cyber attack shut down small power plant”](https://www.bbc.co.uk/news/articles/ce9793g34yvo)
- [🏛️: White House: “President Trump's Cyber Strategy for America”](https://www.whitehouse.gov/wp-content/uploads/2026/03/president-trumps-cyber-strategy-for-america.pdf)

---

## ✨ Stardust

iran, cyber warfare, critical infrastructure, attribution, threat ecosystems, operational technology, water infrastructure, energy, telecommunications, healthcare, access manufacturing, shared software, civilian protection, evidence governance, reporting discipline, alliance reliability, regulatory externality

---

## 🏮 Footer

*🇮🇷 Data Wars: IRGC Edition* is a living node of the **Polaris Protocol**.  
It provides the orientation, scope, evidence spine, attribution discipline, legal caution, governance analysis, alliance context and routing structure for a live analytical pack on cyber disruption across the widening Iran war.

> 📡 Cross-references:
>
> - [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope and routing perimeter*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *incident chronology and evidentiary spine*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *the current multi-actor environment*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *the escalation from information systems into physical control*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *separate legal analysis for wartime cyber operations*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *reporting discipline*
> - [🍊 Why Is the Orange Being Weird?](./🍊_why_is_the_orange_being_weird.md) — *governance and executive context*
>
> 🏮 Return To:
>
> - [🌊 Playing Defence](../README.md) — *1up*
> - [📲 Press Matters](../../README.md) — *2up*
> - [🌓 In The Moment](../../../README.md) — *3up*
> - [🌌 Polaris Protocol — Root](../../../../README.md) — *root*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-09-14_
