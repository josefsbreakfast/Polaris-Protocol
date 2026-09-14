# 🔎 Confidence Labels And Source Rules
**First created:** 2026-08-01 | **Last updated:** 2026-09-14  
*Keeping event, effect, pattern, attribution, sponsorship, source quality, recovery, alliance effect, and legal significance separate enough to remain useful when the evidence changes.*

---

## 🛰️ Orientation

A wartime cyber timeline becomes unreliable when several different evidentiary questions are collapsed into one.

An incident may be real.

Its operational effect may be well established.

Its relationship to a wider pattern may be increasingly difficult to dismiss.

The identity of the technical operator may still be uncertain.

The customer may be different from the operator.

A state may possess an internal attribution it has not published.

A civilian infrastructure incident may raise a serious legal question without the available evidence establishing a war crime.

An ally may be hedging around another ally's policy without the alliance collapsing.

Those are not contradictions.

They are different propositions.

The governing structure is:

```text
CLAIM
→ SOURCE
→ SOURCE QUALITY
→ PROPOSITION
→ CONFIDENCE
→ LIMIT
→ RIVAL EXPLANATION
→ NEGATIVE FINDINGS
→ REVIEW
→ HISTORY
```

The governing rule is:

> Confidence belongs to the proposition being made.

Not to the article.

Not to the incident as a whole.

Not to the actor name.

Not to the current preferred theory.

And not to the fact that this pack happens to be called *IRGC Edition*.

The pack needs to hold two disciplines at once:

```text
avoid false certainty
+
avoid false emptiness
```

---

## 🚦 The Traffic-Light System

The traffic-light system is the quick visual index used for confidence in a **specific proposition**.

It does not describe:

- severity;
- political importance;
- strategic importance;
- legal seriousness;
- or how alarming an incident feels.

### 🟢 Established / Confirmed

Use where the public record strongly supports the proposition.

Examples:

- an affected institution confirms an incident;
- an operational effect is independently supported;
- a physical-process change is verified;
- a formal government attribution is published;
- or strong technical evidence is corroborated independently.

### 🟡 Probable

Use where the evidence strongly favours one explanation but an important gap remains.

Examples may include:

- several independent indicators;
- credible intelligence reporting;
- distinctive infrastructure reuse;
- repeated operator behaviour;
- or technically independent findings converging.

### 🟠 Suspected / Developing

Use where there is a credible basis for keeping a proposition live but material uncertainty remains.

Examples:

- preliminary assessment;
- incomplete technical overlap;
- historical resemblance;
- credible investigative reporting;
- or an emerging cluster.

### ⚪ Open / Unattributed

Use where the proposition remains unresolved.

White means:

```text
OPEN QUESTION
```

not:

```text
RULED OUT
```

### ❌ Excluded

Use where later evidence no longer supports the proposition or inclusion.

Examples:

- disproved actor claim;
- duplicate incident;
- unrelated technical failure;
- incorrect system identification;
- unrelated criminal cause;
- or evidence placing the incident outside scope.

Do not silently delete exclusions.

Record why the assessment changed.

---

## 📣 Actor-Claimed Is A Modifier, Not A Traffic Light

Use:

```text
CLAIM STATUS:
📣 ACTOR-CLAIMED
```

separately from:

```text
ATTRIBUTION CONFIDENCE:
```

An actor claim establishes that the claim exists.

It does not establish:

- authorship;
- access;
- effect;
- causation;
- state direction;
- group continuity;
- or command chain.

The September AT&T case makes this especially clear:

```text
REAL OUTAGE:
🟢 CONFIRMED

APT IRAN CLAIM:
📣 CONFIRMED AS A CLAIM

CYBER CAUSATION:
❌ REJECTED BY AT&T

IRAN CAUSATION:
⚪ NOT ESTABLISHED
```

Therefore:

```text
CLAIM
≠
CAUSATION
```

must now remain explicit across the pack.

---

## 🗝️ Visual Grammar

The pack uses several visual systems.

Do not confuse them.

```text
🟢 🟡 🟠 ⚪
=
confidence in a proposition

📣
=
actor-claim status

❌
=
excluded / disproved / outside current analytical set

⚪ 🟡 🟠 🔴
=
pattern development
```

Always preserve the written label beside the symbol.

Do not rely on colour alone.

---

## 🧮 One Incident Can Carry Many Confidence Assessments

Where relevant, separate:

```text
INCIDENT CONFIDENCE:
SCOPE CONFIDENCE:
OPERATIONAL-EFFECT CONFIDENCE:
PHYSICAL-EFFECT CONFIDENCE:
DATA-EFFECT CONFIDENCE:
ATTRIBUTION CONFIDENCE:
RELATIONSHIP CONFIDENCE:
PATTERN CONFIDENCE:
COMMON-OPERATOR CONFIDENCE:
COMMON-CUSTOMER CONFIDENCE:
COMMON-SPONSOR CONFIDENCE:
SHARED-DEFENDER-BURDEN CONFIDENCE:
ALLIANCE-EFFECT CONFIDENCE:
LEGAL CONFIDENCE:
RECOVERY CONFIDENCE:
```

A single incident may therefore read:

```text
INCIDENT:
🟢 CONFIRMED

OPERATIONAL EFFECT:
🟢 CONFIRMED

TECHNICAL OPERATOR:
🟡 PROBABLE

STATE DIRECTION:
⚪ OPEN

PATTERN:
🔴 ESTABLISHED

COMMON SPONSOR:
⚪ OPEN

SHARED DEFENDER BURDEN:
🟢 ESTABLISHED
```

That is not indecision.

It is the method.

---

## 🎨 Pattern Status Is A Separate Axis

Use:

```text
⚪ ISOLATED
🟡 POSSIBLE RECURRENCE
🟠 CREDIBLE CLUSTER
🔴 ESTABLISHED CAMPAIGN PATTERN
```

Pattern confidence answers:

> Are related things happening repeatedly?

It does not answer:

> Who is commanding them?

Therefore:

```text
PATTERN:
🔴 ESTABLISHED

COMMON OPERATOR:
⚪ OPEN

COMMON CUSTOMER:
⚪ OPEN

COMMON SPONSOR:
⚪ OPEN
```

is valid.

This distinction is now especially important because the September dataset contains:

- a strong Iran-facing OT pattern;
- separate ransomware activity;
- a China-linked contractor ecosystem;
- shared-software access manufacturing;
- and unrelated administrative incidents

inside one war environment.

---

## 🧬 Campaign Effect Is Not Common Command

September requires a further distinction.

A defender can experience real campaign-like cumulative pressure even where the incidents do not share one operator.

Therefore record separately:

```text
CUMULATIVE CAMPAIGN EFFECT:
SHARED DEFENDER BURDEN:
COMMON OPERATOR:
COMMON CUSTOMER:
COMMON SPONSOR:
```

For example:

```text
CUMULATIVE ESSENTIAL-INFRASTRUCTURE PRESSURE:
🟢 ESTABLISHED

SHARED DEFENDER BURDEN:
🟢 ESTABLISHED

COMMON OPERATOR:
⚪ OPEN

COMMON SPONSOR:
⚪ OPEN
```

This prevents:

```text
same queue of defensive work
```

from becoming:

```text
same hostile command chain
```

---

## 🚰 Water Shows Why The Layers Matter

The late-August disclosure of more than 100 targeted US water and wastewater systems supports:

```text
SECTOR-SCALE TARGETING:
🟢 ESTABLISHED
```

It does not automatically support:

```text
100+ PHYSICAL DISRUPTIONS:
NO

ONE COMMON OPERATOR:
NO

ONE COMMON SPONSOR:
NO
```

The core Minnesota / Iran-linked wave can be stronger than the attribution of the entire 100+ system population.

That distinction should remain visible.

---

## ⚡ Small Physical Effect Still Gets Its Own Green

The UK generator case demonstrates:

```text
PHYSICAL GENERATION SHUTDOWN:
🟢 CONFIRMED

NATIONAL GRID EFFECT:
❌ NOT REPORTED

IRAN-LINKED ASSESSMENT:
🟠 / 🟡 DEVELOPING

FORMAL PUBLIC NCSC ATTRIBUTION:
⚪ NOT IDENTIFIED
```

Do not downgrade a confirmed physical effect because the national consequence was limited.

Severity and confidence are separate.

---

## 📉 Severity Is Not Confidence

A confidence colour must not double as a severity scale.

A small incident may be:

```text
CONFIDENCE:
🟢 HIGH

SEVERITY:
LOW
```

A catastrophic allegation may be:

```text
CONFIDENCE:
🟠 SUSPECTED

SEVERITY IF TRUE:
VERY HIGH
```

Where useful, record:

```text
SEVERITY:
OPERATIONAL SIGNIFICANCE:
STRATEGIC SIGNIFICANCE:
```

separately.

---

## 🏗️ Strategic Importance Is Not Attribution

A system may be strategically important because it involves:

- water;
- energy;
- healthcare;
- banking;
- telecoms;
- transport;
- government;
- defence;
- or justice.

That changes:

```text
WHY IT MATTERS
```

It does not answer:

```text
WHO DID IT
```

Keep:

```text
IRAN-WAR RELEVANCE:
```

separate from:

```text
IRAN ATTRIBUTION:
```

---

## 🗺️ Country Relevance Is Its Own Field

A country may be relevant because it is:

- a belligerent;
- basing state;
- logistics provider;
- intelligence partner;
- sanctions participant;
- or part of the opposing coalition.

That makes it relevant to the war map.

It does not make Iran the default explanation for unexplained incidents there.

---

## 🕸️ Attribution Is A Stack

Use:

```text
TECHNICAL OPERATOR
↓
TOOLING / INFRASTRUCTURE
↓
GROUP OR ALIAS
↓
CRIMINAL / ACCESS INTERMEDIARY
↓
ACCESS BROKER
↓
CONTRACTOR / PROXY
↓
TASK ORIGINATOR / COMMISSIONER
↓
PAYER / PROCUREMENT ROUTE
↓
BUYER / CUSTOMER
↓
STATE AFFILIATION
↓
STATE DIRECTION
↓
END USER / FINAL BENEFICIARY
```

Confidence attaches separately to each relevant layer.

Do not compress:

```text
TECHNICAL OPERATOR:
🟢

STATE AFFILIATION:
🟡

STATE DIRECTION:
⚪
```

into:

```text
IRAN:
CONFIRMED
```

unless the evidence actually reaches that proposition.

---

## 🧅 Criminal Operator Does Not Resolve The Customer

Keep both directions:

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

A criminal operator may simply be criminal.

It may sell access later.

A state customer may appear only after compromise.

Several customers may use the same data or access.

Do not assume either direction.

---

## 🪜 Operator And Customer May Enter At Different Times

Possible sequence:

```text
initial compromise
→ credentials
→ access retained
→ access advertised
→ access sold
→ later tasking
→ downstream use
```

Therefore distinguish:

```text
INITIAL OPERATOR:
INITIAL PURPOSE:
ACCESS TRANSFER:
LATER OPERATOR:
LATER CUSTOMER:
LATER PURPOSE:
```

This is especially important for PaperCut-style access manufacturing.

---

## 💰 Commissioner, Payer, Customer And Beneficiary Are Separate

Record separately:

```text
TASK ORIGINATOR:
COMMISSIONER:
PAYER:
PROCUREMENT ROUTE:
CUSTOMER:
END USER:
FINAL BENEFICIARY:
```

Payment may support:

- demand;
- relationship;
- procurement;
- or access transfer.

It does not automatically prove:

- detailed control;
- intent regarding every method;
- or knowledge of every downstream effect.

Preserve:

```text
COMMISSIONING
≠
COMPLETE OPERATIONAL CONTROL
```

and:

```text
NO COMPLETE OPERATIONAL CONTROL
≠
NO RELATIONSHIP
```

---

## 🎭 State Relationship Terms Are Not Synonyms

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

### State-Linked

Some evidenced relationship exists.

### State-Affiliated

Meaningful organisational or institutional connection exists.

### State-Backed / State-Supported

Material support is evidenced.

### State-Sponsored

Use cautiously; define what sponsorship means in the source.

### State-Encouraged

Evidence of encouragement without necessarily tasking.

### State-Tolerated

Evidence of permissive space or knowing tolerance.

### State-Directed

Evidence supports the materially stronger proposition that the state directed or controlled the operation in question.

---

## 🎭 Proxy Is Not A Vibe

Do not use **proxy** merely to mean:

> politically aligned non-state actor.

Record the relationship:

- funding;
- tasking;
- command;
- shared personnel;
- infrastructure;
- technical support;
- access provision;
- or tolerated activity.

The term should not hide what is actually evidenced.

---

## 👤 Benefit Is Not Control

Keep:

```text
STRATEGIC BENEFIT
≠
SPONSORSHIP
```

and:

```text
LATER USE
≠
ORIGINAL TASKING
```

This now applies equally to alliance effects:

```text
ADVERSARY BENEFITS FROM ALLIED DIVERGENCE
≠
ADVERSARY CAUSED THE DIVERGENCE
```

---

## 🌍 Alliance Effect Is A Separate Proposition

Where alliance reliability matters, record separately:

```text
PREVIOUSLY COORDINATED POSITION:
POLICY DIVERGENCE:
ALLIED HEDGING:
OPERATIONAL / PLANNING COST:
ADVERSARY BENEFIT:
ADVERSARY CAUSATION:
```

Possible confidence example:

```text
POLICY DIVERGENCE:
🟢 CONFIRMED

ALLIED HEDGING:
🟡 DEVELOPING

TRANSACTION COST:
🟡 DEVELOPING

NATO COLLAPSE:
❌ NOT ESTABLISHED

ADVERSARY CAUSED THE DIVERGENCE:
⚪ OPEN / NO EVIDENCE
```

Do not collapse disagreement into alliance failure.

---

## 🤖 Capability Is Not Use

Evidence of:

- a technique;
- exploit;
- AI workflow;
- malware family;
- target interest;
- or vulnerability research

does not establish use in a specific incident.

Therefore:

```text
CAPABILITY
≠
USE
```

and:

```text
AI-ASSISTED RESEARCH
≠
SUCCESSFUL EXPLOITATION
```

The Anthropic naval-reconnaissance case is the clean comparator.

---

## ⚓ Reconnaissance Is Not Exploitation

Use:

```text
RECONNAISSANCE:
🟢 CONFIRMED

SUCCESSFUL ACCESS:
⚪ OPEN

EXPLOITATION:
⚪ OPEN

OPERATIONAL EFFECT:
⚪ OPEN
```

where that is the evidence.

Do not upgrade CVE research into attack.

---

## 🪞 Similarity Is Not A Common Operator

Several incidents may look similar because they involve:

- the same PLC;
- the same VPN;
- the same cloud service;
- the same identity provider;
- the same MSP;
- the same software;
- or the same vulnerability.

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
shared-provider dependency
```

or:

```text
copycat activity
```

Preserve the rivals.

---

## 🕸️ Shared Providers Need Their Own Field

Where relevant record:

```text
COMMON VENDOR:
COMMON CLOUD PROVIDER:
COMMON MSP:
COMMON IDENTITY PROVIDER:
COMMON OT INTEGRATOR:
COMMON REMOTE-ACCESS PLATFORM:
COMMON CONTRACTOR:
COMMON SOFTWARE:
COMMON VULNERABILITY:
```

A shared dependency may explain clustering without one common operator.

---

## 🤖 Shared Software Is Not Strategic Selection

PaperCut and similar mass-exploitation campaigns require:

```text
EXPOSED POPULATION:
ACTUAL VICTIM POPULATION:
SECTOR DISTRIBUTION:
LATER SELECTIVE USE:
```

Do not infer:

```text
several important sectors affected
=
each strategically selected
```

without evidence.

---

## 🧯 Service Continuity Is Not No Effect

Where fallback worked, record:

```text
NORMAL SERVICE DEGRADED:
MANUAL / LOCAL FALLBACK:
ADDITIONAL STAFFING:
DELAY / DIVERSION:
HIGH-DEPENDENCY USER EFFECT:
```

Examples include:

- water systems moving manual;
- Manitoba local HVAC monitoring;
- Luminis ambulance diversion.

Therefore:

```text
SERVICE CONTINUED
≠
NO OPERATIONAL EFFECT
```

---

## 🧍 Technical Recovery Is Not Person-Centred Recovery

Keep:

```text
SYSTEM RESTORED
≠
DATA RECALLED
≠
RECORD TRUST RESTORED
≠
PERSON PROTECTED
```

Where relevant record:

```text
TECHNICAL RECOVERY:
SERVICE RECOVERY:
DATA RECOVERY:
RECORD-INTEGRITY RECOVERY:
PERSON-CENTRED RECOVERY:
```

---

## ⚖️ Legal Confidence Is Its Own Axis

Keep:

```text
CIVILIAN INFRASTRUCTURE AFFECTED
≠
IHL VIOLATION CONFIRMED
≠
WAR CRIME CONFIRMED
```

Legal confidence may depend on:

- armed-conflict nexus;
- target status;
- whether the operation qualifies as an attack;
- applicable IHL rule;
- breach;
- state attribution;
- individual actor;
- mental element;
- mode of liability;
- and jurisdiction.

Do not use the incident confidence colour as the legal confidence colour.

---

## 📚 Source Quality And Proposition Fit Are Separate

A source can be excellent and still not support the proposition being attached to it.

Record both:

```text
SOURCE QUALITY:
PROPOSITION FIT:
```

Examples:

- affected operator: strong for operational effect, weak for ultimate sponsor;
- CISA advisory: strong for threat class, may not attribute one local incident;
- actor claim: strong for claim existence, weak for causation;
- White House statement: strong for presidential position, weak as technical attribution evidence;
- security vendor: strong for telemetry, may be weak for political intent.

---

## 🔗 Source Independence Must Be Tested

Several reports may rely on:

- the same advisory;
- the same company disclosure;
- the same unnamed official;
- the same Telegram post;
- or the same vendor.

Record:

```text
ORIGINAL SOURCE:
INDEPENDENT CORROBORATION:
COMMON SOURCE DEPENDENCY:
```

Do not count repetition as corroboration.

---

## ❌ Negative Findings Are Evidence Too

Preserve important negatives.

Examples:

```text
NO GRID-WIDE EFFECT
NO COURT-SERVICE SHUTDOWN
NO CLINICAL DISRUPTION REPORTED
NO PORT OT COMPROMISE
NO IRAN LINK FOUND
NO SUCCESSFUL EXPLOITATION DISCLOSED
FORMAL PUBLIC ATTRIBUTION NOT IDENTIFIED
```

Negative findings stop the reader silently inflating the incident.

---

## 🔀 Rival Explanations Must Stay Visible

Where material, record:

```text
PREFERRED EXPLANATION:
RIVAL EXPLANATION 1:
RIVAL EXPLANATION 2:
WHAT WOULD DISTINGUISH THEM:
```

The presence of a preferred explanation does not erase the rival.

---

## 🧪 Evidence, Inference, Limit, Rival

For difficult propositions use:

```text
EVIDENCE:
INFERENCE:
LIMIT:
RIVAL EXPLANATION:
```

Example:

```text
EVIDENCE:
More than 100 internet-exposed US water and wastewater systems were targeted.

INFERENCE:
The exposure is national in scale.

LIMIT:
One common operator across all systems is not established.

RIVAL EXPLANATION:
Several actors may have exploited the same exposed controller population.
```

---

## 🔄 Confidence Must Be Allowed To Move

When evidence changes, record:

```text
PREVIOUS ASSESSMENT:
NEW EVIDENCE:
WHAT CHANGED:
CURRENT ASSESSMENT:
```

Do not silently rewrite earlier uncertainty.

A correction is part of the evidence history.

---

## 🚫 Durable Separation Rules

Keep these visible across the pack:

```text
INCIDENT CONFIRMED
≠
ATTRIBUTION CONFIRMED

PATTERN CONFIRMED
≠
ONE COORDINATED CAMPAIGN CONFIRMED

CAMPAIGN EFFECT
≠
COMMON COMMAND

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

CLAIM
≠
CAUSATION

CAPABILITY
≠
USE

RECONNAISSANCE
≠
EXPLOITATION

SHARED SOFTWARE
≠
STRATEGIC SELECTION

SERVICE CONTINUED
≠
NO OPERATIONAL EFFECT

SYSTEM RESTORED
≠
PERSON-CENTRED RECOVERY COMPLETE

CIVILIAN INFRASTRUCTURE AFFECTED
≠
WAR CRIME CONFIRMED

ALLIED POLICY DIVERGENCE
≠
ALLIANCE COLLAPSE

ADVERSARY BENEFIT
≠
ADVERSARY CAUSATION
```

---

## 🧭 Working Rule

The working rule is:

> Give every material proposition its own evidentiary status.

Do not let:

- the actor name;
- the war context;
- the target sector;
- the legal stakes;
- the strategic usefulness;
- or the preferred theory

borrow confidence from another field.

Confidence should move only when evidence for **that proposition** moves.

That is what makes later correction possible without collapsing the whole record.

---

## 🌌 Constellations

🔎 🕸️ 📣 🧬 ⚖️ 🤖 🌍 — confidence; attribution; actor claims; campaign structure; legal status; capability; alliance effects.

---

## ✨ Stardust

confidence labels, source rules, attribution, actor claims, proposition confidence, pattern confidence, common operator, common customer, campaign effect, defender burden, source provenance, negative findings, rival explanations, reconnaissance, exploitation, shared software, legal confidence, alliance hedging, corrections

---

## 🏮 Footer

*🔎 Confidence Labels And Source Rules* is a living node of the **Polaris Protocol**.  
It defines the proposition-level confidence, source, pattern, relationship, recovery, legal and alliance rules used across the *🇮🇷 Data Wars: IRGC Edition* pack.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *source provenance and evidentiary roles*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *language-control layer*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *attribution stack and relationship confidence*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *commissioning, access transfer and end-user separation*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *ecosystem-level pattern separation*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *campaign effect and shared defender burden*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *separate legal-confidence ladder*
> - [🍊 Why Is the Orange Being Weird?](./🍊_why_is_the_orange_being_weird.md) — *political and governance proposition discipline*
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
