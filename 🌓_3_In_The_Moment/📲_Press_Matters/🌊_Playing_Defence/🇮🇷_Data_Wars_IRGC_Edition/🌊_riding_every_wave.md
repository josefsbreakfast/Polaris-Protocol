# 🌊 Riding Every Wave
**First created:** 2026-08-14 | **Last updated:** 2026-09-14  
*How state campaigns, aligned actors, shared vulnerabilities, criminal follow-on, narrative capture, alliance seams, and ordinary opportunism can overlap without sharing a command structure.*

---

## 🛰️ Orientation

Cyber campaigns rarely arrive as a neat procession of attributable incidents conducted by one actor under one chain of command.

Conflict changes the environment around an attack.

A state operation may generate publicity, expose vulnerable infrastructure, reveal working techniques, consume defensive capacity, create stolen access, attract ideologically aligned actors, advertise profitable targets, or alter allied behaviour.

Criminal groups may then exploit the same environment.

Some may have relationships with the state.

Some may merely share its enemies.

Some may have noticed that everyone is looking the other way.

Some may buy access created by someone else.

Some may falsely claim an outage they did not cause.

Some may act after a political or alliance seam has already widened.

The resulting activity can look like one large campaign from a distance.

It may not be.

The analytical task is therefore not simply to ask:

> **Who is attacking?**

It is also to ask:

> **Which wave are we looking at, what produced it, and what kind of relationship—if any—connects it to the waves around it?**

By September 2026, a further rule belongs beside that question:

> **A later actor can exploit a condition it did not create.**

That condition may be:

- technical;
- organisational;
- economic;
- narrative;
- or political.

The exploitation can still be real.

The command relationship may still be absent.

---

## 🌊 One Conflict Can Produce Several Waves

A useful starting model distinguishes between several kinds of activity that may coexist.

### 🏛️ State-directed activity

Operations can be directly tasked, coordinated, resourced or controlled by a state institution.

This is the strongest organisational relationship.

Evidence may include:

- government attribution;
- intelligence reporting;
- command relationships;
- infrastructure or tooling tied to state operators;
- tasking patterns;
- operational coordination;
- or technical evidence linking activity to a previously attributed state unit.

Even here, attribution should remain evidence-led.

State interest in an outcome does not by itself establish state direction of an operation.

### 🕸️ State-linked or proxy activity

An actor may have an established relationship with a state while retaining significant operational autonomy.

Relationships can include:

- funding;
- technical assistance;
- historical cooperation;
- ideological alignment;
- personnel overlap;
- intelligence sharing;
- tolerated activity;
- or intermittent tasking.

“State-linked” therefore does not automatically mean:

> **the government ordered this particular incident.**

The relationship between actor and state and the attribution of a specific operation are separate evidentiary questions.

### 💰 Commissioned Or Purchased Outcomes

A customer may commission an outcome without selecting the hands-on operator or technical method.

An operator may obtain access without knowing who will ultimately buy or use it.

A plausible chain is:

```text
requirement
→ commissioner
→ payer or procurement route
→ intermediary
→ access broker or operator
→ effect, data, or access
→ end user or later beneficiary
```

The customer can enter before the intrusion, during it, or after access already exists.

Those timings support different claims:

```text
commission before access
→ possible prior tasking

purchase after compromise
→ later acquisition, not automatically original direction

payment for an outcome
→ relationship and demand, not automatically method control
```

This is a distinct way of riding a wave.

The later customer may redirect, deepen, publicise, or operationalise access created for another purpose.

The commissioning chain must be evidenced rather than inferred from usefulness alone.

### 📣 Aligned opportunism

Conflict attracts participants.

Hacktivists, ideological fellow-travellers, patriotic hacking groups and other sympathetic actors may independently attack the same adversary.

Their activity may reinforce a state's strategic objectives without being commissioned by that state.

Alignment of interests is not proof of command.

### 🤑 Criminal follow-on

Criminal actors may exploit conditions created by earlier activity.

This can include:

- monetising stolen credentials;
- purchasing access from brokers;
- deploying ransomware into already-weakened environments;
- extorting disrupted organisations;
- exploiting vulnerabilities publicised by earlier incidents;
- reusing publicly discussed techniques;
- targeting sectors revealed to be poorly defended.

This activity may be **causally downstream** from a state campaign without being **organisationally downstream** from the state.

That distinction matters.

### 📡 Narrative follow-on

An operational wave can also produce a publicity wave.

Later actors may:

- claim an intrusion they did not initiate;
- exaggerate the operational effect;
- selectively publish the most politically useful victims;
- wrap criminal access in ideological language;
- amplify genuine stolen material;
- use ordinary outages as evidence of supposed reach;
- or use public attention to advertise capability, recruit participants, or attract customers.

The narrative actor, hands-on operator, customer, and publicity selector may be different people.

Narrative coordination therefore has to be tested separately from intrusion coordination.

### 🦹 Background opportunistic crime

Some attacks occurring during a conflict will simply be crime.

War does not suspend the normal cybercrime economy.

Indeed, instability may increase ordinary offending by:

- stretching defenders;
- increasing the number of exposed systems;
- creating confusion about attribution;
- disrupting routine maintenance;
- increasing demand for illicit access;
- generating more politically plausible cover for criminal activity.

A rise in cybercrime during conflict does not require every criminal actor to have joined the war.

Sometimes war increases crime because war increases opportunity.

### 🧬 Shared-vulnerability waves

One exploitable product can generate a cross-sector victim list without any actor selecting each victim for its strategic value.

A shared-vulnerability wave may look like:

```text
widely used software
→ one exploitable flaw
→ mass scanning or repeatable access
→ victims across several sectors
→ data theft or extortion at scale
```

The resulting victim list may include energy, healthcare, finance, defence, industrial, retail, and ordinary commercial organisations.

That distribution can resemble strategic cross-sector targeting.

The organising mechanism may instead be:

> **Who was running the vulnerable product?**

rather than:

> **Which sectors did the attacker choose for geopolitical effect?**

This does not make the campaign strategically irrelevant.

It changes the attribution question.

### 🧱 Governance-seam waves

A further category has become harder to ignore.

Separate actors may repeatedly benefit from the same institutional weakness even where they share no command, tooling or customer.

The common mechanism may be:

- unclear ownership;
- delayed mitigation;
- fragmented disclosure;
- poor asset inventory;
- shared suppliers;
- weak public/private coordination;
- or uncertainty between allies about attribution and response.

That can produce:

```text
SAME DEFENSIVE SEAM
+
DIFFERENT ACTORS
=
REPEATED EXPLOITATION
```

The common cause may sit on the defender's side of the boundary.

### 🌍 Alliance-seam waves

The same logic can operate internationally.

If allied governments become less certain about:

- whether a previously agreed position still holds;
- whether public attribution will be coordinated;
- whether retaliation or assistance will follow;
- whether basing assumptions remain valid;
- or whether the largest coalition member will maintain the agreed line,

then several unrelated actors may benefit from the resulting hesitation.

That produces:

```text
ALLIED POLICY DIVERGENCE
→ SLOWER COORDINATION
→ WEAKER SIGNAL
→ MORE OPPORTUNITY
```

An adversary does not have to create the disagreement to exploit it.

That distinction is central.

---

## 🧿 Downstream Is Not The Same As Directed

One of the easiest analytical errors is to see a sequence like this:

```text
state operation
      ↓
system disruption
      ↓
criminal exploitation
```

and silently convert it into:

```text
state
  ↓
criminal operator
```

Those are different claims.

The first describes a **causal sequence**.

The second describes a **command or organisational relationship**.

A criminal group can benefit from conditions created by state activity without receiving instructions, funding or assistance from that state.

Likewise, criminals can reuse:

- credentials;
- exposed services;
- vulnerabilities;
- malware concepts;
- target lists;
- public reporting;
- or generalised defender exhaustion

created by an earlier campaign.

The state operation may therefore help explain **why the later crime became possible or profitable** while explaining nothing about **who ordered the later crime**.

The reverse caution also matters.

Absence of command does not make every upstream decision consequence-free.

A commissioner, provider, platform, broker, earlier operator, government, or alliance partner may knowingly or negligently create:

- reusable capability;
- transferable access;
- a market for stolen data;
- a public target list;
- defender overload;
- uncertainty about response;
- or conditions in which wider downstream harm is foreseeable.

That may create governance, due-diligence, facilitation, alliance-management, or risk-allocation questions even where it does not prove command responsibility for the later actor.

Keep the propositions separate:

```text
causal contribution
≠
operational direction

foreseeable ecosystem support
≠
intent for every downstream offence

no direct command
≠
no responsibility question at all
```

---

## 🪜 Initial Access And Later Use May Have Different Organising Logic

The first actor to enter a system may be selecting for ease.

A later actor may select for value.

The chain can look like:

```text
mass scanning
→ opportunistic compromise
→ persistence or data access
→ criminal sorting
→ access sale or affiliate use
→ later customer recognises strategic value
```

Or:

```text
shared-vulnerability campaign
→ broad victim pool
→ selective extortion
→ selective publication
→ selective resale or follow-on tasking
```

This means two propositions can coexist:

```text
INITIAL ACCESS WAS OPPORTUNISTIC
```

and:

```text
LATER EXPLOITATION WAS SELECTIVE
```

The commissioning chain may enter at several points:

```text
BEFORE ACCESS
→ target or outcome commissioned in advance

AFTER ACCESS
→ broker or operator shops an existing foothold to possible customers

AFTER DATA THEFT
→ buyer acquires a dataset, intelligence value, or coercive opportunity

AFTER PUBLICATION
→ later actor amplifies, weaponises, or acts on material already released
```

But selective later use must be demonstrated.

It cannot be inferred merely because some compromised organisations would be useful to a state at war.

Useful evidence might include:

- which victims were compromised compared with the exposed customer population;
- which victims received extortion demands;
- which victims were named publicly;
- which data categories were prioritised;
- evidence of access sale;
- payment timing and procurement route;
- whether the same operator offered access to several customers;
- whether a commissioner specified the target, outcome, method, or publicity decision;
- later intrusion by a different actor;
- tasking or communications;
- or operational effects inconsistent with ordinary extortion.

Without that evidence:

```text
STRATEGICALLY INTERESTING VICTIM
≠
STRATEGICALLY SELECTED VICTIM
```

And:

```text
POSSIBLE LATER STATE CUSTOMER
≠
EVIDENCE OF A LATER STATE CUSTOMER
```

---

## 🤖 Access Manufacturing Can Now Be Partly Automated

The September PaperCut campaign makes the earlier access-market model more concrete.

GreyNoise reported a likely Russian-speaking operator using hundreds of AI agents to exploit PaperCut NG/MF vulnerabilities across hundreds of servers and organisations.

The campaign reportedly produced:

- credentials;
- OS and domain secrets;
- privileged access;
- and some domain-admin footholds.

The significance is not that every victim was strategically chosen.

It is that access can be produced at scale.

The sequence becomes:

```text
SHARED VULNERABILITY
→ AI-ASSISTED MASS EXPLOITATION
→ HUNDREDS OF FOOTHOLDS
→ CREDENTIALS / DOMAIN ACCESS
→ POSSIBLE RESALE / AFFILIATE USE
→ POSSIBLE LATER SELECTIVE USE
```

This is **access manufacturing**.

The original operator may be selecting for vulnerability.

A later user may select for strategic value.

The same foothold can therefore move between organising mechanisms over time.

That makes later-use evidence more important, not less.

---

## 🌀 Conflict Changes The Opportunity Environment

Large cyber campaigns do not operate inside sealed laboratories.

They alter the environment in which subsequent actors make decisions.

A significant attack can produce several secondary effects at once:

```text
STATE / STATE-LINKED ACTIVITY
→ disruption
→ exposed access
→ publicity
→ defender load
→ imitation
→ access markets
→ criminal follow-on
→ larger apparent campaign
```

A political rupture can produce something similar:

```text
ALLIED POLICY DIVERGENCE
→ uncertainty
→ slower shared response
→ weaker deterrent signalling
→ wider perceived opportunity window
→ separate actors probe the seam
```

From outside, both can resemble coordinated escalation.

Sometimes they are.

Sometimes they are several actors riding the same wave.

---

## 🧩 Several Relationships Can Exist At Once

An actor relationship should not be forced into a single binary category of either **state-controlled** or **completely unrelated**.

The useful questions are more granular.

### Organisational relationship

Is there evidence that the actors belong to, work for, receive direction from or maintain an established relationship with the same organisation?

### Operational relationship

Is there evidence that actors coordinated this specific campaign or incident?

### Technical relationship

Do incidents share infrastructure, malware, credentials, tooling or techniques?

Shared techniques alone may be weak evidence if those techniques are widely available.

### Causal relationship

Did one incident create conditions that enabled another?

This relationship may exist even where the actors have never communicated.

### Strategic relationship

Do separate actors produce effects beneficial to the same state or political objective?

Strategic alignment alone does not establish operational coordination.

### Temporal relationship

Did events occur close together?

Temporal clustering is useful for identifying patterns.

It is not proof of common command.

### Market relationship

Did credentials, access, data, tooling, infrastructure, or services change hands?

A market relationship can establish transfer and demand without establishing a shared political objective.

### Commissioning relationship

Did a requirement generator, commissioner, payer, or intermediary request or purchase a particular target, access type, dataset, effect, or publication decision?

Commissioning can exist without day-to-day control of method.

### Narrative relationship

Did one actor claim, frame, exaggerate, publish, or amplify another actor's activity?

Shared messaging does not automatically prove shared intrusion infrastructure.

### Downstream-use relationship

Did a later actor use access, data, publicity, or disruption created by an earlier wave?

Later use may be selective even where the original access was opportunistic.

### Governance relationship

Did the same defensive seam, fragmented responsibility, delayed disclosure, or overloaded response pathway enable several otherwise separate actors?

The common cause may sit on the defender's side of the boundary.

### Alliance relationship

Did uncertainty between allied governments reduce the speed, clarity or credibility of collective response?

This can matter even where no cyber actor caused the disagreement.

---

## 📣 Riding A Real Outage Without Causing It

The September AT&T episode gives a particularly clean narrative-wave example.

APT IRAN claimed it had disrupted AT&T service across Texas and an unnamed water utility.

A real AT&T outage had occurred.

AT&T said the outage resulted from attempted physical cable theft and rejected the cyber explanation.

That produces:

```text
REAL OUTAGE
+
REAL ACTOR CLAIM
≠
ACTOR CAUSED THE OUTAGE
```

The actor may still gain:

- publicity;
- perceived reach;
- fear;
- recruitment value;
- ideological signalling;
- or bargaining power.

This is **wave-riding without technical causation**.

The outage is the wave.

The claim rides it.

That makes claim analysis part of operational analysis.

Not because the claim proves the intrusion.

Because false or inflated claims can themselves change public perception of the campaign.

---

## 📡 Publicity Can Become A Force Multiplier

Once a genuine campaign exists, later actors can benefit from the expectation that more incidents are plausible.

That changes the information environment.

A false claim is more believable when:

- real attacks have already occurred;
- the target sector is already under warning;
- attribution remains contested;
- the public expects escalation;
- and political leaders are speaking inconsistently.

This can create:

```text
REAL CAMPAIGN
→ PUBLIC EXPECTATION OF MORE ATTACKS
→ LOWER BAR FOR BELIEVING NEW CLAIMS
→ MORE NARRATIVE VALUE FOR OPPORTUNISTS
```

The result is not only misinformation.

It can increase:

- operator workload;
- media confusion;
- political pressure;
- public fear;
- and the cost of correcting the record.

The defender therefore has to protect both:

```text
TECHNICAL REALITY
```

and:

```text
CAUSAL REALITY
```

---

## ⚖️ Do Not Make Criminal Activity Do Too Much Evidentiary Work

The appearance of criminal activity does not automatically weaken a state attribution.

A campaign may contain:

- state operations;
- proxy operations;
- criminal opportunism;
- unrelated crime;
- shared-vulnerability waves;
- narrative opportunism;
- and incidents that remain unattributed.

Finding a criminal layer therefore does not establish that the state layer was imaginary.

Equally, establishing state responsibility for part of a campaign does not permit every nearby ransomware infection, intrusion, service disruption or actor claim to be assigned to the state.

Both errors flatten a mixed environment into a single story.

---

## 🪆 Attribution Can Be Nested

A useful way to record complex campaigns is to attribute at several levels.

For example:

```text
CAMPAIGN ENVIRONMENT
│
├── Wave A
│   └── state-directed — high confidence
│
├── Wave B
│   └── established state-linked actor
│       └── direction for this incident unproven
│
├── Wave C
│   └── aligned actor claim
│       └── claim not independently verified
│
├── Wave D
│   └── criminal exploitation
│       └── possibly enabled by earlier disruption
│
├── Wave E
│   └── shared-vulnerability access manufacturing
│       └── later users unknown
│
├── Wave F
│   └── narrative ride-along
│       └── real outage, false or unsupported causation claim
│
└── Wave G
    └── unattributed / background activity
```

This prevents one attribution judgment from contaminating every incident in the surrounding period.

It also allows confidence to change independently at each layer.

---

## 🔎 Questions For Reading A Wave

When a new cluster of incidents appears around an existing state campaign, ask:

- What is actually shared between the incidents?
- Are we seeing shared command, shared tooling, shared opportunity, shared defender weakness or merely shared timing?
- Is one vulnerable product producing the apparent cross-sector pattern?
- What is the exposed-customer denominator behind the named victims?
- Was initial access opportunistic but later exploitation selective?
- Who generated the requirement, if any?
- Who commissioned or paid for the outcome?
- What did payment purchase: access, data, disruption, concealment, or publicity?
- Did the customer enter before access, after compromise, or after publication?
- Did the commissioner control method, timing, scope, or only the desired result?
- Is the actor already known to have a relationship with the suspected state?
- If so, is there evidence connecting that relationship to **this operation**?
- Did earlier incidents expose access or vulnerabilities later actors could exploit?
- Has publicity made the target class more attractive?
- Has defensive capacity been diverted elsewhere?
- Could criminal activity plausibly have increased independently because the environment became more permissive?
- Is an actor claiming responsibility?
- Does independent evidence corroborate the claim?
- Is there a real outage but a false causation claim?
- Who selected which incidents or victims to publicise?
- Was a later actor using access, data, or attention created by an earlier wave?
- Did a political or alliance seam slow coordination?
- Did any actor benefit from that seam without causing it?
- Are investigators attributing an incident, an operational cluster or the entire campaign?
- Are we accidentally using evidence from one wave to attribute another?

The goal is not to fragment everything until attribution becomes impossible.

The goal is to describe the relationships that the evidence actually supports.

---

## 🧪 Worked Example — The September 2026 Environment

By 14 September, the infrastructure picture contains several clearly different waves.

### 🚰 Iran-linked water and OT pressure

The Minnesota / core water wave still carries the strongest Iran-linked assessment.

The public record includes:

- repeated interference with internet-facing PLCs;
- operational and some physical effects;
- prior government warnings about Iranian-affiliated targeting of the same class of technology;
- reported intelligence and investigative assessments favouring Iran;
- responsibility claims from APT IRAN / CyberAv3ngers;
- and a later CISA disclosure that more than 100 internet-exposed water and wastewater systems were targeted during July.

This is the strongest current state-linked or state-aligned OT wave.

It does not automatically absorb every later OT incident.

### ⚡ Energy and telecommunications expansion

By early September, reporting described increased Iranian government-linked attempts against electricity, telecommunications and other critical infrastructure.

This broadens the **campaign environment**.

It does not automatically establish a common operator across all affected sectors.

The correct update is:

```text
TARGETING SCOPE:
WIDER

COMMON OPERATOR CONFIDENCE:
STILL LIMITED

COMMON STRATEGIC CAMPAIGN CONFIDENCE:
STRONGER THAN COMMON-OPERATOR CONFIDENCE
```

That distinction matters.

### ⚡ UK generator shutdown

The UK generator incident produced a real physical effect.

The plant was offline for four days.

Reporting described the attackers as Iran-linked.

A formal public NCSC attribution naming Iran, the IRGC or a specific group was not identified in the reviewed record.

This belongs in the Iran-facing campaign environment.

It should not be silently merged into the US water operator assessment.

### 🏥 Healthcare ransomware

AnMed, Manitoba, Nutex, Luminis and Veradigm provide a different wave.

The mechanisms include:

- ransomware;
- data theft;
- third-party credential abuse;
- operational healthcare disruption;
- and facility-support-system degradation.

The strongest current explanations are criminal or unresolved.

These incidents consume the same defensive capacity as the Iran-linked wave.

That does not make them part of it.

### 🏛️ Administrative and justice compromise

Berlin and C-Track provide another wave.

The effects include:

- administrative disruption;
- housing-benefit delays;
- data theft;
- credential publication;
- and shared court-record exposure.

Again:

```text
SAME WARTIME ENVIRONMENT
≠
SAME CAMPAIGN
```

### 🤖 PaperCut mass exploitation

PaperCut provides the clearest new shared-vulnerability / access-manufacturing wave.

The likely organising mechanism is:

```text
vulnerable software
→ automated exploitation
→ broad victim pool
→ privileged access
```

The current evidence does not establish one strategic customer behind the entire victim set.

Later selective use remains a testable question.

### 🇨🇳 China-linked contractor ecosystem

The QScan / QTRouter disruption adds a separate state-linked ecosystem.

The US government described a hacker-for-hire environment serving government and military customers.

That is important because it demonstrates:

```text
MULTIPLE STATE-LINKED ECOSYSTEMS
CAN OPERATE IN THE SAME SECTORS
AT THE SAME TIME
```

Target overlap therefore becomes less distinctive as attribution evidence.

### 📣 APT IRAN and AT&T

The AT&T episode is the cleanest narrative ride-along.

A real outage occurred.

APT IRAN claimed it.

AT&T rejected the cyber explanation and attributed the outage to attempted physical cable theft.

That is not campaign proof.

It is attribution contamination.

### ⚓ Iran-nexus naval reconnaissance

Anthropic's September disclosure adds a capability-development / reconnaissance wave.

The Iran-nexus actor researched:

- naval movements;
- personnel;
- satellite and maritime systems;
- VSAT;
- Cisco equipment;
- and shipboard industrial-control products.

No confirmed exploitation was disclosed.

That belongs at:

```text
RECONNAISSANCE / CAPABILITY DEVELOPMENT
```

not:

```text
OPERATIONAL EFFECT
```

### 🌍 Alliance and policy seam

A final wave sits on the defender side.

If the US president acts against previously coordinated allied interests, coalition partners may need to:

- hedge;
- delay;
- duplicate planning;
- retain capability nationally;
- or become more cautious about attribution and response.

No adversary needs to have caused that divergence.

But several adversaries may benefit from the resulting uncertainty.

That makes alliance instability a **governance wave** rather than an attribution finding.

---

## 🧠 Current Wave Assessment — 14 September 2026

```text
COMMON WARTIME ENVIRONMENT:
🟢 ESTABLISHED

IRAN-LINKED / SUSPECTED-IRAN OT CAMPAIGN:
🟡 / 🟢 STRONGLY SUPPORTED

MULTIPLE OVERLAPPING THREAT ECOSYSTEMS:
🟢 ESTABLISHED

SHARED-VULNERABILITY / ACCESS-MANUFACTURING WAVES:
🟢 ESTABLISHED

NARRATIVE RIDE-ALONG CLAIMS:
🟢 ESTABLISHED

ALLIANCE / GOVERNANCE SEAM AS OPPORTUNITY:
🟡 DEVELOPING ANALYTICAL FINDING

ONE COMMON OPERATOR:
⚪ NOT ESTABLISHED

ONE COMMON CUSTOMER:
⚪ NOT ESTABLISHED

ONE COMMON COMMISSIONER:
⚪ NOT ESTABLISHED

ONE COMMON STATE SPONSOR:
⚪ NOT ESTABLISHED
```

The pattern has become more differentiated as the evidence improves.

That is analytical progress.

It is not the disappearance of the campaign environment.

---

## 🚨 Failure Mode: Everybody Works For Tehran

A state-linked actor appears.

A criminal actor appears later.

Both attack similar systems.

The incidents occur during the same geopolitical confrontation.

The temptation is to draw one enormous arrow back to the state.

That may eventually be correct.

But the intermediate relationships still require evidence.

Otherwise:

```text
same enemy
+ same period
+ similar target
= same command
```

quietly becomes the attribution method.

It is not one.

---

## 🚨 Failure Mode: One Criminal Means No State Campaign

The inverse error is equally poor.

If some incidents turn out to be:

- ransomware;
- financially motivated intrusion;
- opportunistic scanning;
- access brokerage;
- or unrelated criminal exploitation,

that does not automatically disprove evidence connecting other incidents to a state actor.

Mixed campaigns are allowed to be mixed.

Finding an opportunist riding the wave does not prove there was no wave.

---

## 🚨 Failure Mode: Real Claim Means Real Cause

Another failure mode is now visible.

An actor makes a claim.

A real outage exists.

The claim therefore feels plausible.

That is not enough.

Use:

```text
REAL OUTAGE
+
REAL CLAIM
=
CLAIM REQUIRES CAUSATION EVIDENCE
```

not:

```text
REAL OUTAGE
+
REAL CLAIM
=
CLAIM CONFIRMED
```

The AT&T case belongs in the pack precisely because it shows why this distinction matters.

---

## 🚨 Failure Mode: No Command Means No Responsibility Question

A later actor may not have received orders from the actor who created the opportunity.

That defeats a claim of command only where command is the proposition being tested.

It does not automatically answer whether an earlier actor:

- commissioned a risky outcome;
- created or subsidised a reusable capability market;
- transferred access without adequate control;
- ignored foreseeable downstream use;
- externalised risk onto victims or public infrastructure;
- or failed to mitigate a hazard it had helped create.

Those questions require their own evidence and legal analysis.

The discipline is:

```text
do not invent command
+
do not erase causation, facilitation, foreseeability, or governance responsibility
```

---

## 🚨 Failure Mode: Adversary Benefit Means Adversary Causation

The alliance-seam problem adds one more failure mode.

If an adversary benefits from:

- allied disagreement;
- slower coordination;
- policy reversal;
- or public contradiction,

that does **not** establish that the adversary caused the disagreement.

Keep:

```text
BENEFIT
≠
CAUSATION
```

The security question is still valid:

> Can an adversary exploit the condition once it exists?

That can be yes without any conspiracy being required.

---

## 🧭 What This Model Preserves

This approach allows several propositions to remain true simultaneously:

> A state may initiate or direct a cyber campaign.

> State-linked actors may participate with varying degrees of autonomy.

> Ideologically aligned actors may independently join the activity.

> Criminals may exploit the resulting disruption.

> Commissioners or customers may purchase access or outcomes after an opportunistic compromise.

> Shared-vulnerability campaigns may manufacture large pools of privileged access.

> Narrative actors may claim, select, exaggerate, or amplify activity conducted elsewhere.

> Some crime may be indirectly enabled by the campaign.

> Other crime may simply rise because conflict creates opportunity.

> Alliance instability may create an exploitable seam without being adversary-created.

> None of those relationships should be upgraded into command without evidence.

> Absence of command should not erase evidence of causal contribution, foreseeable ecosystem support, downstream opportunity, or risk externalisation.

The purpose is not to make attribution weaker.

It is to make attribution **more precise**.

---

## 🔎 Wave Record Template

For each apparent wave, record:

```text
WAVE NAME:
DATE RANGE:
PRIMARY SECTOR:
GEOGRAPHIC SCOPE:

ORGANISING MECHANISM:
STATE-DIRECTED / STATE-LINKED / PROXY / CRIMINAL / SHARED VULNERABILITY / ACCESS MARKET / NARRATIVE / GOVERNANCE SEAM / OPEN:

INITIAL ACCESS LOGIC:
LATER-USE LOGIC:

COMMON PRODUCT:
COMMON VULNERABILITY:
COMMON TOOLING:
COMMON INFRASTRUCTURE:
COMMON CREDENTIAL SOURCE:

ACTOR CLAIM:
CLAIM CORROBORATED:
REAL INCIDENT BEING CLAIMED:
CAUSATION ESTABLISHED:

INITIAL OPERATOR:
LATER OPERATOR:
ACCESS BROKER:
INTERMEDIARY:
COMMISSIONER:
PAYER / PROCUREMENT ROUTE:
FINAL CUSTOMER:
DOWNSTREAM BENEFICIARY:

ACCESS TRANSFER:
DATA TRANSFER:
PUBLICATION:
LATER SELECTIVE USE:

ORGANISATIONAL RELATIONSHIP:
OPERATIONAL RELATIONSHIP:
TECHNICAL RELATIONSHIP:
CAUSAL RELATIONSHIP:
MARKET RELATIONSHIP:
COMMISSIONING RELATIONSHIP:
NARRATIVE RELATIONSHIP:
DOWNSTREAM-USE RELATIONSHIP:
GOVERNANCE RELATIONSHIP:
ALLIANCE-SEAM RELATIONSHIP:

COMMON OPERATOR CONFIDENCE:
COMMON CUSTOMER CONFIDENCE:
COMMON SPONSOR CONFIDENCE:
COMMON STRATEGIC-CAMPAIGN CONFIDENCE:

DEFENDER LOAD EFFECT:
POLICY / ALLIANCE EFFECT:
RIVAL EXPLANATIONS:
EVIDENCE THAT WOULD CHANGE THE ASSESSMENT:
SOURCES:
LAST REVIEWED:
```

This prevents:

```text
same wave
```

from silently becoming:

```text
same boss
```

---

## 🌌 Constellations

🌊 🕸️ 🧿 🪆 🤖 📡 🌍 — campaign ecology; layered attribution; access manufacturing; narrative ride-alongs; downstream use; governance seams; alliance opportunity.

---

## ✨ Stardust

cyber conflict, attribution, state operations, proxy actors, criminal follow-on, shared vulnerabilities, selective exploitation, access markets, commissioning, procurement routes, later customers, narrative amplification, false claims, access manufacturing, paperCut, APT IRAN, AT&T, alliance seams, governance seams, foreseeable ecosystem support, risk externalisation, opportunistic crime, campaign waves, causal relationships, command relationships

---

## 🏮 Footer

*🌊 Riding Every Wave* is a living node of the **Polaris Protocol**.  
It provides a reusable framework for distinguishing state-directed operations, affiliated or aligned participation, commissioned or purchased outcomes, shared-vulnerability waves, access-manufacturing campaigns, narrative ride-alongs, governance seams, alliance uncertainty, criminal exploitation and ordinary opportunism within conflict-driven cyber campaigns.  
It preserves causal, technical, market, commissioning, narrative and downstream-use relationships without converting them automatically into organisational attribution.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *the ecosystem map produced by overlapping waves*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *confidence, evidence and proposition-level attribution*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *commissioning, procurement, access transfer and layered operational roles*
> - [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md) — *separating actor claims, investigative assessments and formal attribution*
> - [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *claim-level provenance and source independence*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *language for downstream, linked, aligned and directed activity*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *incident-level chronology through 14 September 2026*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *cumulative pressure across distributed incidents*
> - [🇬🇧 Britain Is Advertising An Exploitable Seam](./🇬🇧_britain_is_advertising_an_exploitable_seam.md) — *domestic and alliance seams on the defender side*
> - [🇺🇸 Potential Impacts On Americans](./🇺🇸_potential_impacts_on_americans.md) — *how defender load, claims and alliance uncertainty reach the public*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *depth, scale and physical effects*
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
