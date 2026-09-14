# 🕸️ Attribution Is Not A Light Switch
**First created:** 2026-08-01 | **Last updated:** 2026-09-14  
*Cyber attribution is graded, delayed, layered, contested, politically managed, and legally consequential at different thresholds.*

---

## 🛰️ Orientation

Public discussion often treats attribution as binary:

```text
Iran did it
Iran did not do it
```

That is not how most cyber attribution works.

The more accurate picture is a ladder of confidence built from different kinds of evidence:

- technical indicators;
- infrastructure reuse;
- malware families;
- operator behaviour;
- target selection;
- timing;
- intelligence reporting;
- actor claims;
- law-enforcement findings;
- private-sector analysis;
- recovered tasking;
- access-transfer evidence;
- payment or procurement evidence;
- and political judgement.

Those layers do not always arrive at the same time.

They do not always point in the same direction.

They are not always made public.

And they do not all answer the same question.

The public may ask:

> Who hacked the system?

A government may ask:

> Which intelligence service, proxy, contractor, criminal network, access broker, customer, or commissioner sits behind the operator?

A lawyer may ask:

> Can the operation be attributed to a state, connected to the armed conflict, or tied to an identifiable person with the required responsibility?

Those are related questions.

They are not interchangeable.

So the absence of a definitive public statement does not make an incident analytically empty.

It also does not permit the incident to be confidently assigned to Iran.

Both limits matter.

---

## 🎚️ Attribution Has Levels

### 🟢 Confirmed

A competent public authority, affected institution, court record, sanctions record, indictment, coordinated advisory, or well-supported technical investigation has made a clear attribution with a sufficient public basis.

Confirmed does not mean metaphysically certain.

It means the public record supports a high-confidence proposition.

### 🟡 Probable

The available evidence strongly favours one actor, organisation, relationship, or state connection, but an important gap remains.

Possible support includes:

- operator overlap;
- distinctive infrastructure reuse;
- repeated tooling;
- credible intelligence reporting;
- victimology;
- tasking;
- or multiple independent technical indicators.

Probable should not be rounded upward because the theory is tidy.

### 🟠 Suspected / Developing

There is a credible basis for scrutiny but substantial uncertainty remains.

Possible support includes:

- preliminary official assessment;
- limited technical overlap;
- historical resemblance;
- credible investigative reporting;
- target fit;
- or an emerging cluster.

### 📣 Actor-Claimed

A group has claimed responsibility.

That proves the claim exists.

It does not prove:

- the claimant conducted the intrusion;
- the claimed access existed;
- the claimed effect occurred;
- the group is who it says it is;
- the same people still control a familiar alias;
- the state directed the operation;
- or the claimant caused the incident it is attaching itself to.

Actor claims belong in the record.

They do not control the record.

### ⚪ Unattributed / Open

No credible public attribution has yet been established.

Open does not mean unrelated.

It does not mean Iran.

It means the proposition remains unresolved.

### ❌ Excluded

Later evidence shows the proposed attribution, relationship, or incident should not remain in the analytical set.

Exclusion should be preserved with the reason.

---

## 🎯 Confidence Belongs To A Proposition

An incident is not simply “confirmed” or “suspected.”

A particular proposition about it is.

These are different propositions:

```text
the intrusion occurred

the claimed effect occurred

the named persona had access

the named operator performed the intrusion

the operator belonged to a particular organisation

the organisation had a state relationship

a commissioner requested the outcome

a payer funded the capability

a customer purchased or received the access

a later user exploited the access

the state benefited

the state directed or controlled this operation

the conduct is legally attributable to the state

an identifiable person bears criminal responsibility
```

Evidence may confirm one proposition while leaving the next unresolved.

The confidence label must therefore attach to a written claim, role, time period, and incident.

If the proposition changes, reassess it.

---

## 🪜 There Is More Than One Attribution Ladder

A useful distinction is:

```text
technical attribution
→ who appears to have operated the intrusion?

organisational attribution
→ what group, contractor, criminal network or proxy did they belong to?

commissioning attribution
→ who generated, requested or paid for the requirement?

customer attribution
→ who purchased, received or later used access, data or effects?

state-relationship attribution
→ what relationship exists between the relevant actor and a state?

state-responsibility attribution
→ can the conduct legally be attributed to a state?

public governmental attribution
→ what is the state willing to say publicly?

individual criminal responsibility
→ which identifiable person can be shown to bear criminal responsibility?
```

Those ladders can move at different speeds.

That is normal.

---

## 🧱 Different Evidence Does Different Work

### Technical Evidence

Technical evidence may show:

- common infrastructure;
- matching malware;
- code reuse;
- account patterns;
- persistence techniques;
- controller interaction;
- or familiar operational mistakes.

Technical similarity can support linkage.

It does not always prove common sponsorship.

Tools can be copied, bought, shared, leaked, imitated, or independently used against the same exposed technology.

### Behavioural Evidence

Target selection and operator behaviour may reveal recurring interests.

This can help establish campaign logic.

It is weaker as stand-alone attribution.

### Timing

Timing may support a hypothesis.

It does not establish causation.

Ordinary cybercrime continues during war.

### Intelligence Evidence

Governments may possess:

- intercepted communications;
- human intelligence;
- covert telemetry;
- partner intelligence;
- financial links;
- recovered tasking;
- or knowledge of a counter-operation.

That can produce high internal confidence with sparse public evidence.

### Political Attribution

States decide whether, when, and how to attribute publicly.

Language can move through:

```text
malicious actor
→ suspected Iranian actor
→ Iran-linked
→ Iranian-affiliated
→ IRGC-affiliated
→ Iranian state-sponsored
→ Iranian state-directed
```

Movement along that ladder matters.

The underlying technical event may be unchanged.

The public responsibility claim has changed.

---

## 🔗 Evidence Can Be Strong Without Being Independent

Several reports may descend from one:

- official assessment;
- advisory;
- leak;
- company disclosure;
- security-vendor report;
- or actor claim.

Therefore distinguish:

```text
SOURCE QUALITY:
EVIDENCE STRENGTH:
SOURCE INDEPENDENCE:
PUBLICATION STATUS:
```

Five articles repeating one Telegram post remain one actor-origin route.

Five articles repeating one unnamed official remain one reported official assessment unless independently sourced.

---

## 🚰 The Water Campaign Shows Why Attribution Must Stay Layered

The current water picture supports several different levels at once.

By late August:

- more than 100 internet-exposed US water and wastewater systems had been targeted;
- some incidents involved PLC access and operational disruption;
- the Minnesota / core wave had strengthened Iran-linked indicators;
- prior US government reporting had already linked CyberAv3ngers to IRGC-affiliated activity;
- and actor claims from APT IRAN / CyberAv3ngers had appeared.

That can support:

```text
SECTOR-SCALE WATER CAMPAIGN:
🟢 ESTABLISHED

IRAN-LINKED CORE WAVE:
🟡 PROBABLE / STRENGTHENED

PRIOR CYBERAV3NGERS–IRGC RELATIONSHIP:
🟢 ESTABLISHED

CURRENT ACTOR CLAIM:
📣 ESTABLISHED AS A CLAIM

CURRENT IRGC DIRECTION OF EVERY INCIDENT:
⚪ NOT ESTABLISHED

ONE COMMON OPERATOR ACROSS 100+ SYSTEMS:
⚪ NOT ESTABLISHED
```

This is more informative than either:

> Iran did all of it.

or:

> We know nothing.

---

## ⚡ Campaign-Level Confidence Can Rise Before Incident-Level Attribution Converges

By early September, reporting described increased Iranian government-linked attempts against:

- electricity;
- telecommunications;
- and other critical infrastructure.

That can strengthen:

```text
IRAN-FACING CAMPAIGN CONFIDENCE
```

without automatically strengthening:

```text
ATTRIBUTION OF EVERY NEW INCIDENT
```

This distinction is important.

Campaign-level assessment may be:

```text
🟡 / 🟢 STRONG
```

while one specific outage remains:

```text
⚪ OPEN
```

There is no contradiction.

---

## 📣 Claim Does Not Equal Causation

The September AT&T case gives the cleanest example.

A real AT&T outage occurred.

APT IRAN claimed responsibility.

AT&T said attempted physical cable theft caused the outage and rejected the cyber explanation.

Therefore:

```text
REAL OUTAGE:
🟢 CONFIRMED

REAL CLAIM:
📣 CONFIRMED

CLAIMANT CAUSED OUTAGE:
❌ NOT SUPPORTED ON CURRENT RECORD
```

This adds an explicit attribution rule:

```text
CLAIM
≠
CAUSATION
```

A claimant can ride a real event it did not cause.

---

## ⚓ Reconnaissance Does Not Equal Exploitation

Anthropic disclosed Iran-nexus use of Claude for:

- naval tracking;
- ship and aircraft movements;
- personnel research;
- maritime VSAT;
- Cisco communications;
- and industrial-control-product research.

That supports:

```text
IRAN-NEXUS RECONNAISSANCE:
🟢 DISCLOSED

SUCCESSFUL EXPLOITATION:
⚪ NOT ESTABLISHED

OPERATIONAL EFFECT:
⚪ NOT ESTABLISHED

DIRECT IRGC TASKING:
⚪ NOT ESTABLISHED
```

Therefore:

```text
TARGET RESEARCH
≠
ACCESS

ACCESS
≠
EXPLOITATION

EXPLOITATION
≠
OPERATIONAL EFFECT
```

Do not let capability evidence become incident attribution.

---

## 🤖 Shared Software Does Not Equal Common Operator

The PaperCut campaign shows a different attribution trap.

One vulnerable product can produce:

```text
many victims
+
many sectors
+
similar access
```

without proving strategic target selection.

The organising mechanism may be:

```text
shared vulnerability
+
mass exploitation
```

rather than:

```text
one sponsor selected each victim
```

Record separately:

```text
COMMON SOFTWARE:
COMMON VULNERABILITY:
COMMON OPERATOR:
COMMON CUSTOMER:
LATER ACCESS TRANSFER:
```

The first two may be green while the later fields remain open.

---

## 🇨🇳 Sector Overlap Is Not Iran-Specific

The QScan / QTRouter ecosystem matters because a separate China-linked hacker-for-hire architecture targeted overlapping sectors such as:

- government;
- energy;
- telecoms;
- and hospitals.

That weakens:

```text
same sector
```

as a standalone Iran-attribution signal.

Sector choice can support context.

It cannot carry attribution alone.

---

## 🧬 Clustering Raises Significance Before It Necessarily Raises Sponsorship Confidence

Useful cluster indicators include:

- same controller family;
- same software;
- same remote-access route;
- similar credential manipulation;
- repeated manual fallback;
- geographic spread;
- narrow timing;
- shared provider;
- similar physical effect;
- common access broker;
- common tasking;
- or common customer.

Clustering can justify:

```text
coordinated investigation
```

before it justifies:

```text
one coordinated Iranian operation
```

Pattern recognition should increase scrutiny before it increases certainty.

---

## 🧅 The Chain May Be Layered

A cyber chain may look like:

```text
requirement generator
→ commissioner
→ payer / procurement route
→ intermediary
→ access broker
→ hands-on operator
→ buyer
→ later user
→ final beneficiary
```

Different layers may know different things.

The immediate operator may be criminal.

The customer may be state-linked.

Or there may be no state customer at all.

Keep both:

```text
CRIMINAL OPERATOR
≠
NO STATE CUSTOMER
```

and:

```text
CRIMINAL OPERATOR
≠
STATE CUSTOMER
```

---

## 💰 Payment Is Relationship Evidence, Not Automatic Command Evidence

Payment may support propositions about:

- demand;
- procurement;
- access purchase;
- employment;
- retainer;
- infrastructure rental;
- or commissioning.

It does not automatically establish:

- detailed operational control;
- knowledge of every subcontractor;
- approval of every technique;
- or intent concerning every downstream consequence.

Therefore:

```text
PAYMENT
≠
COMPLETE COMMAND
```

but also:

```text
NO COMPLETE COMMAND
≠
NO RELATIONSHIP
```

---

## 🎭 State Relationship Terms Must Not Be Used As Synonyms

Distinguish:

```text
state-linked
state-affiliated
state-backed
state-supported
state-sponsored
state-encouraged
state-tolerated
state-directed
```

Use the strongest term the evidence supports.

No stronger.

---

## 🎭 Proxy Is Not A Vibe

Do not use **proxy** merely to mean:

> politically aligned with Iran.

Record the evidenced relationship:

- funding;
- tasking;
- command;
- shared personnel;
- technical support;
- infrastructure;
- safe harbour;
- or tolerated activity.

The word should not hide the relationship.

---

## 👤 Benefit Is Not Control

Keep:

```text
STRATEGIC BENEFIT
≠
SPONSORSHIP

LATER USE
≠
ORIGINAL TASKING
```

This now applies equally to alliance effects:

```text
IRAN BENEFITS FROM ALLIED UNCERTAINTY
≠
IRAN CAUSED ALLIED UNCERTAINTY
```

---

## 🌍 Attribution And Alliance Effects Are Different Questions

A political or alliance seam may widen the attack surface.

That does not make the seam an attribution indicator.

Record separately:

```text
ALLIED POLICY DIVERGENCE:
ALLIED HEDGING:
RESPONSE DELAY:
ADVERSARY BENEFIT:
ADVERSARY CAUSATION:
```

The cyber-attribution question remains evidence-led.

---

## 🧪 Capability Is Not Use

Evidence that an actor possesses:

- a technique;
- exploit;
- malware family;
- AI workflow;
- reconnaissance method;
- or target interest

does not establish use in the present incident.

Therefore:

```text
CAPABILITY
≠
USE
```

---

## 🪞 Similarity Is Not A Common Operator

Several incidents may resemble each other because they share:

- a controller;
- VPN;
- cloud service;
- identity provider;
- MSP;
- software platform;
- remote-access tool;
- integrator;
- or vulnerability.

That may indicate:

```text
one campaign
```

or:

```text
several actors exploiting one weakness
```

or:

```text
shared provider dependency
```

or:

```text
copycat activity
```

Preserve the rivals.

---

## 🧱 Common Target Does Not Equal Common Customer

Different operators may attack the same infrastructure because it is:

- exposed;
- valuable;
- profitable;
- symbolic;
- or easy.

Likewise, one customer may use several operators.

Therefore record separately:

```text
COMMON TARGET:
COMMON OPERATOR:
COMMON CUSTOMER:
COMMON SPONSOR:
```

Do not let one field silently answer another.

---

## ⚖️ Public Attribution And Legal Attribution Are Different

A government may publicly say:

> Iran-linked actor

without making the legal claim:

> this conduct is attributable to Iran under the rules of state responsibility.

Likewise, a formal state attribution does not itself establish individual criminal responsibility.

Keep:

```text
TECHNICAL ATTRIBUTION
≠
PUBLIC POLITICAL ATTRIBUTION
≠
LEGAL STATE ATTRIBUTION
≠
INDIVIDUAL CRIMINAL RESPONSIBILITY
```

---

## 🔄 Attribution Must Be Allowed To Change

When evidence moves:

```text
PREVIOUS ASSESSMENT:
NEW EVIDENCE:
WHAT CHANGED:
CURRENT ASSESSMENT:
```

Do not rewrite the earlier state of knowledge.

A moving attribution is not methodological failure.

It is what a properly versioned evidentiary process should show.

---

## 🔎 Attribution Record Template

```text
INCIDENT:
DATE:

INCIDENT CONFIDENCE:
EFFECT CONFIDENCE:

CLAIM STATUS:
CLAIMED ACTOR:

TECHNICAL OPERATOR:
TOOLING / INFRASTRUCTURE:
GROUP / ALIAS:
ALIAS CONTINUITY:

INTERMEDIARY:
ACCESS BROKER:
CONTRACTOR / PROXY:

TASK ORIGINATOR:
COMMISSIONER:
PAYER:
PROCUREMENT ROUTE:
CUSTOMER:
LATER USER:
FINAL BENEFICIARY:

STATE RELATIONSHIP:
STATE AFFILIATION:
STATE DIRECTION:
PUBLIC GOVERNMENT ATTRIBUTION:
LEGAL STATE ATTRIBUTION:

COMMON PRODUCT:
COMMON VULNERABILITY:
COMMON PROVIDER:

PATTERN CONFIDENCE:
COMMON OPERATOR CONFIDENCE:
COMMON CUSTOMER CONFIDENCE:
COMMON SPONSOR CONFIDENCE:
STRATEGIC CAMPAIGN CONFIDENCE:

CLAIM CAUSATION:
RECONNAISSANCE / ACCESS / EXPLOITATION / EFFECT:

RIVAL EXPLANATIONS:
NEGATIVE FINDINGS:
EVIDENCE THAT WOULD CHANGE THE ASSESSMENT:

SOURCES:
LAST REVIEWED:
```

---

## 🚫 Durable Attribution Separations

Keep these visible:

```text
INCIDENT CONFIRMED
≠
ATTRIBUTION CONFIRMED

ACTOR CLAIM
≠
CAUSATION

PATTERN CONFIRMED
≠
ONE COORDINATED CAMPAIGN CONFIRMED

CAMPAIGN-LEVEL IRAN CONFIDENCE
≠
IRAN ATTRIBUTION FOR EVERY INCIDENT

COMMON OPERATOR
≠
COMMON CUSTOMER

CRIMINAL OPERATOR
≠
NO STATE CUSTOMER

CRIMINAL OPERATOR
≠
STATE CUSTOMER

IRAN-LINKED OPERATOR
≠
IRAN DIRECTED THIS OPERATION

STATE BENEFIT
≠
STATE CONTROL

CAPABILITY
≠
USE

RECONNAISSANCE
≠
EXPLOITATION

SHARED SOFTWARE
≠
COMMON OPERATOR

SAME SECTOR
≠
IRAN-SPECIFIC SIGNATURE

PUBLIC ATTRIBUTION
≠
LEGAL ATTRIBUTION
```

---

## 🧭 Working Rule

The working rule is:

> Attribute each layer only as far as the evidence reaches.

Ask:

```text
WHO TOUCHED THE SYSTEM?
WHOSE TOOLING WAS USED?
WHO DID THE OPERATOR WORK WITH?
WHO COMMISSIONED THE OUTCOME?
WHO PAID?
WHO BOUGHT OR RECEIVED THE ACCESS?
WHO USED IT LATER?
WHAT STATE RELATIONSHIP IS ACTUALLY EVIDENCED?
WHAT IS THE GOVERNMENT WILLING TO SAY?
WHAT CAN BE LEGALLY ATTRIBUTED?
```

And when the answer changes:

change the field.

Do not change the whole story unless the evidence requires it.

Attribution is not a light switch.

It is a stack.

---

## 🌌 Constellations

🕸️ 🔎 🧅 📣 🤖 ⚖️ 🌍 — attribution; confidence; layered tasking; claims; capability; legal responsibility; alliance context.

---

## ✨ Stardust

cyber attribution, technical attribution, organisational attribution, state attribution, actor claims, causation, Iran-linked, IRGC, access brokers, commissioners, customers, shared vulnerabilities, reconnaissance, exploitation, campaign confidence, source independence, legal attribution, attribution history

---

## 🏮 Footer

*🕸️ Attribution Is Not A Light Switch* is a living node of the **Polaris Protocol**.  
It defines the layered attribution model used across the *🇮🇷 Data Wars: IRGC Edition* pack, separating technical operator, organisation, intermediary, commissioner, customer, state relationship, public attribution and legal responsibility.

> 📡 Cross-references:
>
> - [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md) — *proposition-level confidence rules*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *commissioning and access-transfer architecture*
> - [🌊 Riding Every Wave](./🌊_riding_every_wave.md) — *causal relationships without command inflation*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *multiple attribution architectures inside one war environment*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *language discipline*
> - [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *source provenance and negative findings*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *legal attribution and individual responsibility*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *technical depth and physical effect*
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
