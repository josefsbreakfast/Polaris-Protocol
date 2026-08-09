# 🔎 Confidence Labels And Source Rules
**First created:** 2026-08-01 | **Last updated:** 2026-08-09  
*Keeping event, effect, pattern, attribution, sponsorship, source quality, recovery, and legal significance separate enough to remain useful when the evidence changes.*

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

Those are not contradictions.

They are different propositions.

The most familiar failure looks like:

```text
early claim
→ repeated reporting
→ dropped caveat
→ stronger wording
→ actor becomes sponsor
→ sponsor becomes state
→ suspicion becomes fact
```

There is an equal and opposite failure:

```text
real incident
→ attribution incomplete
→ incident treated as isolated

another real incident
→ attribution incomplete
→ incident treated as isolated

another real incident
→ attribution incomplete
→ developing pattern disappears inside uncertainty
```

This pack should do neither.

The governing structure is:

```text
CLAIM
→ SOURCE
→ SOURCE QUALITY
→ EVIDENTIARY LAYER
→ CONFIDENCE
→ LIMIT
→ RIVAL EXPLANATION
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

The purpose of this node is therefore to make the record capable of saying:

```text
this happened
```

while still saying:

```text
we do not yet know who caused it
```

or:

```text
these incidents form a real pattern
```

while still saying:

```text
we do not yet know whether they share one operator or customer
```

or:

```text
Iranian involvement is plausible
```

while still saying:

```text
the public evidence does not establish state direction
```

The pack needs to hold two disciplines at once:

```text
avoid false certainty
+
avoid false emptiness
```

The first protects accuracy.

The second protects situational awareness.

---

## 🚦 The Traffic-Light System

The traffic-light system is the quick visual index used for confidence in a **specific proposition**.

It does not replace the written confidence label.

It does not describe severity.

It does not describe political importance.

It does not describe how alarming the incident feels.

It tells the reader how strongly the current evidence supports the proposition written beside it.

### 🟢 Established / Confirmed

Use **🟢 Established / Confirmed** where the public record strongly supports the proposition.

Examples may include:

- an affected institution confirming an incident;
- independently supported operational disruption;
- a verified physical-process change;
- a formal governmental attribution;
- a court or sanctions record;
- or strong technical evidence supported by genuinely independent sources.

Green applies only to the proposition actually established.

Therefore:

```text
INCIDENT:
🟢 CONFIRMED

SERVICE DISRUPTION:
🟢 CONFIRMED

TECHNICAL OPERATOR:
🟡 PROBABLE

IRANIAN STATE DIRECTION:
🟠 SUSPECTED
```

is coherent.

A green incident does not make every field in the row green.

### 🟡 Probable

Use **🟡 Probable** where the available evidence strongly favours one explanation but an important evidentiary gap remains.

Possible support includes:

- several independent indicators;
- distinctive infrastructure reuse;
- operator overlap;
- matching victimology;
- repeated tooling;
- repeated operational behaviour;
- credible official assessment;
- or technically independent findings pointing in the same direction.

Yellow means:

> This is presently the best-supported explanation.

It does not mean:

> This has been established beyond meaningful doubt.

Probable should not be rounded upward because the theory is tidy.

### 🟠 Suspected / Developing

Use **🟠 Suspected / Developing** where there is a credible basis for keeping a proposition live but material uncertainty remains.

Possible support includes:

- preliminary official assessment;
- limited technical overlap;
- incomplete intelligence reporting;
- credible investigative reporting;
- historical resemblance;
- target selection;
- military timing combined with other evidence;
- or an emerging cluster.

Orange means:

> There is enough here to test this proposition seriously.

It does not mean:

> Repeat this as fact.

### ⚪ Open / Unattributed

Use **⚪ Open / Unattributed** where the proposition remains unresolved.

This may mean:

- no credible public attribution exists;
- competing explanations remain genuinely viable;
- the answer has not yet been established;
- or the available information is insufficient to choose between them.

White is not a negative finding.

It means:

```text
OPEN QUESTION
```

rather than:

```text
RULED OUT
```

Therefore:

```text
IRANIAN STATE DIRECTION:
⚪ OPEN
```

does not mean:

```text
IRAN RULED OUT
```

And:

```text
COMMON SPONSOR:
⚪ OPEN
```

does not mean:

```text
THE INCIDENTS ARE UNRELATED
```

### ❌ Excluded

Use **❌ Excluded** where a claim, relationship, incident, or proposed cluster no longer meets the evidentiary or scope threshold.

Reasons may include:

- unsupported reporting;
- disproved actor claims;
- duplicated incidents;
- generic indicators originally mistaken for distinctive ones;
- mistaken identification of the affected system;
- an unrelated technical failure;
- an unrelated criminal cause;
- later evidence disproving a proposed relationship;
- or evidence that the incident falls outside the pack's scope.

Do not silently delete exclusions.

Record why the assessment changed.

Corrections are part of the evidentiary history.

---

## 📣 Actor-Claimed Is A Modifier, Not A Traffic Light

**Actor-claimed** should not be forced into the confidence spectrum.

It answers:

> Has somebody claimed responsibility?

It does not answer:

> How confident are we that the claimant actually caused the incident?

Use it as a modifier.

For example:

```text
CLAIM STATUS:
📣 ACTOR-CLAIMED

ATTRIBUTION CONFIDENCE:
⚪ OPEN
```

or:

```text
CLAIM STATUS:
📣 ACTOR-CLAIMED

ATTRIBUTION CONFIDENCE:
🟠 SUSPECTED
```

or:

```text
CLAIM STATUS:
📣 ACTOR-CLAIMED

ATTRIBUTION CONFIDENCE:
🟢 INDEPENDENTLY CONFIRMED
```

An actor claim establishes that the claim exists.

It does not establish:

- that the claimant conducted the intrusion;
- that the claimed access existed;
- that the claimed effect occurred;
- that the group is who it says it is;
- that the same people still control a familiar alias;
- that a state directed the operation;
- or that political branding reflects the real command chain.

---

## 🗝️ Visual Grammar

The pack uses several visual systems.

They should not be confused.

```text
🟢 🟡 🟠 ⚪
=
confidence in a proposition

📣
=
actor-claim status

❌
=
excluded from the current analytical set

⚪ 🟡 🟠 🔴
=
pattern development
```

The same colour can therefore appear in different systems for different reasons.

The label beside it must always remain visible.

Do not rely on colour alone.

---

## 🧮 One Incident Can Carry Many Confidence Assessments

A single incident should not be forced into one overall confidence category.

Where relevant, separate:

### Incident Confidence

How confident are we that the event occurred?

### Scope Confidence

How confident are we that the event belongs inside this pack's essential-state-infrastructure perimeter?

### Effect Confidence

How confident are we about the reported operational, physical, data, record-integrity, or civilian consequences?

### Attribution Confidence

How confident are we about the operator, organisation, intermediary, customer, state affiliation, or state direction?

### Relationship Confidence

How confident are we that this incident is actually related to another incident or cluster?

### Pattern Confidence

How confident are we that repeated incidents form a meaningful recurring pattern?

### Legal Confidence

How far does the public evidence support a legal characterisation?

### Recovery Confidence

How confident are we that technical, service, data, or person-centred recovery is actually complete?

A single entry may therefore read:

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

That is not indecision.

It is the point of the method.

---

## 🎨 Pattern Status Is A Separate Axis

Attribution asks:

> Who did this?

Pattern analysis asks:

> Are related things happening repeatedly?

Those questions can move at different speeds.

Use:

```text
⚪ ISOLATED

No meaningful recurrence established.


🟡 POSSIBLE RECURRENCE

Some overlap exists in target, timing, technique,
technology, geography, infrastructure, operator,
provider, or effect.


🟠 CREDIBLE CLUSTER

Several incidents share enough characteristics
to justify cluster-level scrutiny.


🔴 ESTABLISHED CAMPAIGN PATTERN

Repeated related activity is independently established,
even where ultimate sponsorship remains unresolved.
```

Pattern status does not automatically establish a common operator.

It does not automatically establish one coordinated command chain.

And it does not automatically establish one state sponsor.

Therefore:

```text
PATTERN STATUS:
🔴 ESTABLISHED

COMMON OPERATOR:
⚪ OPEN

COMMON TASKING:
⚪ OPEN

COMMON SPONSOR:
⚪ OPEN
```

is a legitimate result.

---

## 🧬 A Pattern Is Not Necessarily One Campaign

Even where a recurring operational pattern is real, several explanations may remain possible.

For example:

```text
one coordinated operator
```

or:

```text
several coordinated operators
```

or:

```text
several operators with one customer
```

or:

```text
one operator serving several customers
```

or:

```text
criminal reuse of the same exploit
```

or:

```text
independent actors exploiting the same exposed technology
```

or:

```text
shared contractor or provider failure
```

or:

```text
copycat activity
```

or:

```text
some mixture of these
```

A repeated pattern may therefore be analytically important before evidence supports the stronger proposition that all incidents belong to one centrally coordinated campaign.

The record should preserve that distinction.

---

## 🚰 Water Shows Why The Layers Matter

Water and wastewater infrastructure makes the distinction unusually visible.

Suppose several utilities experience some combination of:

- access to exposed controllers;
- operator lockouts;
- configuration changes;
- loss of visibility;
- forced manual operation;
- pressure disruption;
- pump interference;
- or service degradation.

As the number of incidents rises, the evidence may strongly support:

```text
REPEATED WATER-SECTOR PATTERN:
🟢 ESTABLISHED
```

while still supporting only:

```text
COMMON OPERATOR:
🟡 PROBABLE
```

or:

```text
IRANIAN STATE DIRECTION:
🟠 SUSPECTED
```

or:

```text
COMMON CUSTOMER:
⚪ OPEN
```

The physical consequences may matter before attribution catches up.

Strategic importance does not supply the missing attribution.

---

## 📉 Severity Is Not Confidence

A confidence colour should never double as a severity scale.

These are different questions.

A small incident may be:

```text
CONFIDENCE:
🟢 HIGH

SEVERITY:
LOW
```

A potentially catastrophic claim may be:

```text
CONFIDENCE:
🟠 SUSPECTED

SEVERITY IF TRUE:
VERY HIGH
```

Where useful, record separately:

```text
SEVERITY:
OPERATIONAL SIGNIFICANCE:
STRATEGIC SIGNIFICANCE:
```

Water being strategically important does not make Iranian attribution more likely.

A dramatic consequence does not make weak evidence stronger.

---

## 🏗️ Strategic Importance Is Not Attribution

An incident affecting:

- water;
- energy;
- healthcare;
- banking;
- transport;
- government;
- telecommunications;
- defence;
- or justice

may deserve greater scrutiny because of its consequences.

That changes:

```text
WHY THE INCIDENT MATTERS
```

It does not answer:

```text
WHO CAUSED IT
```

The same applies to countries.

A state may be highly relevant to Iran's wartime operational map while attribution of a specific incident remains weak.

Record:

```text
IRAN-WAR RELEVANCE:
```

separately from:

```text
IRANIAN ATTRIBUTION:
```

---

## 🗺️ Country Relevance Is Its Own Field

A country may sit inside the pack's tracking perimeter because it is:

- a direct belligerent;
- a basing state;
- a logistics provider;
- an interceptor;
- an intelligence partner;
- a maritime partner;
- a sanctions participant;
- or part of infrastructure supporting the opposing coalition.

That may make the country a plausible target environment.

It does not make Iran the default explanation for unexplained cyber incidents there.

The pack is an Iran-war cyber pack.

It is not entitled to fill unattributed space with Iran.

---

## 🕸️ Attribution Is A Stack

Cyber attribution may involve several different layers.

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
BUYER / CUSTOMER
↓
STATE AFFILIATION
↓
STATE DIRECTION
↓
FINAL BENEFICIARY
```

Confidence should attach separately to each material layer.

For example:

```text
TECHNICAL OPERATOR:
🟢 CONFIRMED

GROUP IDENTITY:
🟡 PROBABLE

STATE AFFILIATION:
🟡 PROBABLE

STATE DIRECTION OF THIS INCIDENT:
⚪ OPEN
```

Do not compress that into:

```text
IRAN:
CONFIRMED
```

unless the evidence actually reaches that proposition.

---

## 🧅 Criminal Operator Does Not Resolve The Customer

The label:

```text
CYBERCRIME
```

may accurately describe the immediate activity.

It does not necessarily answer:

```text
WHO BOUGHT THE ACCESS?
WHO SELECTED THE TARGET?
WHO RECEIVED THE DATA?
WHO TASKED THE LATER OPERATION?
```

The pack should preserve both directions:

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

A criminal operator may simply be a criminal operator.

A criminal operator may sell access later.

A customer may appear only after the initial compromise.

Several customers may purchase the same access or data.

A state may opportunistically benefit from material it did not originally commission.

None of those possibilities should be assumed without evidence.

The purpose of the model is to keep the questions open long enough to distinguish them.

---

## 🪜 The Operator And Customer May Enter At Different Times

A cyber chain does not have to begin with one customer issuing one clean instruction.

It may look like:

```text
initial compromise
→ credential theft
→ access retained
→ access advertised
→ access sold
→ data copied
→ data resold
→ later tasking
→ downstream exploitation
```

Or:

```text
operator
→ broker
→ several buyers
```

Or:

```text
operator
→ one customer
→ later resale
→ second customer
```

This means evidence about the first intrusion may tell us very little about the final user.

The chronology of the access chain matters.

---

## 🪞 Historical Comparators Are Mechanisms, Not Findings

Other states and cyber ecosystems can demonstrate that:

- financially motivated activity and state utility are not mutually exclusive;
- criminal infrastructure can be reused;
- stolen access can be purchased;
- and operators do not always need to know the ultimate strategic customer.

Those comparators justify questions.

They do not transfer findings.

Therefore:

```text
another state has used criminal-style cyber activity
→
criminal/state overlap is analytically possible
```

not:

```text
another state has done this
→
Iran did this
```

Mechanisms travel.

Findings do not.

---

## 🎭 State Relationship Terms Must Not Be Used As Synonyms

The pack should distinguish carefully between terms such as:

```text
state-linked
state-affiliated
state-backed
state-sponsored
state-supported
state-encouraged
state-tolerated
state-directed
```

These are not interchangeable.

Where possible, define what the evidence actually shows.

### State-Linked

There is some evidenced relationship to state structures, personnel, infrastructure, financing, past attribution, or activity.

The relationship itself must be described.

### State-Affiliated

The actor has a more meaningful organisational or institutional connection to the state than mere ideological alignment.

The nature of that affiliation should be stated.

### State-Backed / State-Supported

Evidence indicates material support.

That may involve:

- funding;
- infrastructure;
- technical assistance;
- safe harbour;
- resources;
- or other support.

It does not necessarily establish operational direction.

### State-Sponsored

Use cautiously.

Where used, identify what sponsorship means in the source being relied upon.

Do not use it as a vague synonym for suspicious.

### State-Encouraged

Evidence indicates encouragement or signalling without necessarily establishing direct tasking.

### State-Tolerated

Evidence supports knowing tolerance or permissive operating space.

Tolerance does not equal direction.

### State-Directed

Evidence supports a materially stronger proposition:

> the state directed or controlled the operation in question.

That requires stronger evidence than ideological alignment, state benefit, or general affiliation.

---

## 🎭 Proxy Is Not A Vibe

Do not use **proxy** merely to mean:

> non-state actor that appears politically aligned with Iran.

Where the term is used, record the evidenced relationship.

Possible relationships include:

- funding;
- tasking;
- command;
- shared personnel;
- access provision;
- technical support;
- infrastructure sharing;
- operational coordination;
- ideological alignment;
- or tolerated activity.

These are different relationships.

The word proxy should not hide which one is actually evidenced.

---

## 👤 Benefit Is Not Control

A state may benefit from an incident without causing it.

A state may later exploit stolen material without commissioning the original intrusion.

An incident may weaken an adversary in a way that fits Iranian strategic interests without Iran having any involvement.

Therefore:

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

Strategic incentives belong in interpretation.

They do not substitute for attribution evidence.

---

## 🧪 Capability Is Not Use

Evidence that an actor possesses a technique, exploit, malware family, infrastructure capability, or target interest does not establish that it used that capability in the current incident.

Therefore:

```text
CAPABILITY
≠
USE
```

Technical resemblance may increase attribution confidence.

It should not carry the whole attribution by itself.

---

## 🪞 Similarity Is Not A Common Operator

Several incidents may look similar because they involve:

- the same exposed PLC;
- the same VPN product;
- the same cloud service;
- the same identity provider;
- the same managed service provider;
- the same remote-access tool;
- the same OT integrator;
- or the same widely exploited vulnerability.

That can indicate:

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

The record should preserve those rival explanations.

---

## 🕸️ Shared Providers Need Their Own Field

Where relevant, record:

```text
COMMON VENDOR:
COMMON CLOUD PROVIDER:
COMMON MSP:
COMMON IDENTITY PROVIDER:
COMMON OT INTEGRATOR:
COMMON REMOTE-ACCESS PLATFORM:
COMMON CONTRACTOR:
COMMON VULNERABILITY:
```

A shared dependency may explain clustering without establishing a shared operator.

Conversely, a common provider may reveal a campaign relationship that is invisible when incidents are viewed institution by institution.

---

## 🎭 Alias Continuity Is Not Operator Continuity

A familiar actor name may be reused.

Therefore:

```text
SAME ALIAS
≠
SAME PEOPLE
```

Where relevant, distinguish:

```text
ALIAS CONTINUITY:
OPERATOR CONTINUITY:
INFRASTRUCTURE CONTINUITY:
TOOLING CONTINUITY:
```

A historic association between an alias and a state should not automatically transfer to every later use of the name.

---

## 🎭 False Flags And Mimicry Remain Possible

Attribution analysis should allow for:

- planted indicators;
- copied TTPs;
- reused political branding;
- deliberate infrastructure imitation;
- false actor claims;
- or attempts to exploit an expected attribution narrative.

The existence of possible mimicry does not make all attribution impossible.

It means distinctive evidence should carry more weight than easily copied indicators.

---

## 🪜 Effect Confidence Must Match Operational Depth

For operational technology, record the deepest level actually supported.

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

The distinctions matter.

```text
saw the controller
≠
accessed the controller
≠
changed the controller
≠
changed the physical process
≠
caused physical harm
```

Likewise:

```text
loss of view
≠
loss of control
≠
attacker control
```

Do not take the deepest effect reported anywhere in a cluster and apply it to every affected facility.

---

## 🧯 Manual Fallback Is Still An Operational Effect

If a utility must move to manual operation, that does not mean:

```text
NO HARM
```

It may mean:

```text
AUTOMATED CONTROL DEGRADED
+
HUMAN FALLBACK WORKED
```

Manual resilience can reduce consequence while still proving that the incident reached an operationally meaningful layer.

Record both:

```text
AUTOMATED EFFECT:
MANUAL / FALLBACK RESPONSE:
SERVICE CONSEQUENCE:
```

---

## 🧱 Effect Confidence Should Be Decomposed

Where useful, separate:

```text
OPERATIONAL EFFECT:
PHYSICAL EFFECT:
DATA-CONFIDENTIALITY EFFECT:
DATA-INTEGRITY EFFECT:
RECORD-INTEGRITY EFFECT:
CIVILIAN EFFECT:
SERVICE EFFECT:
SAFETY EFFECT:
```

Confidence may differ between them.

A service disruption may be confirmed while a claimed physical manipulation remains suspected.

A data breach may be confirmed while record alteration remains open.

---

## 🪪 Confidentiality, Integrity And Provenance Are Different Problems

Cyber incidents do not only copy data.

They may:

- delete it;
- alter it;
- corrupt provenance;
- create conflicting records;
- make the authoritative version uncertain;
- or cause downstream institutions to rely on compromised information.

Distinguish:

```text
DATA COPIED:
DATA DELETED:
DATA ALTERED:
PROVENANCE AFFECTED:
AUTHORITATIVE RECORD STATUS:
DOWNSTREAM RELIANCE:
```

An integrity failure may be more strategically important than ordinary theft.

---

## 🧍 Technical Recovery Is Not Person-Centred Recovery

Where people are affected, separately record:

```text
DATA EXPOSED:
PEOPLE AFFECTED:
NOTIFICATION:
CONTINUING RISK:
PROTECTION OFFERED:
DOMESTIC REUSE OR AMPLIFICATION:
PERSON-CENTRED RECOVERY:
```

Because:

```text
SYSTEM RESTORED
≠
DATA RECALLED
```

and:

```text
EXFILTRATION ENDED
≠
COPIES DESTROYED
```

and:

```text
SERVICE RECOVERED
≠
AFFECTED PERSON SAFE
```

The technical incident may end while downstream harm continues.

---

## 🔗 Source Hierarchy

Sources should be assessed according to what they can establish.

### 🏛️ Tier One — Primary And Official

Examples include:

- affected institutions;
- official cyber advisories;
- regulator notices;
- court filings;
- indictments;
- sanctions records;
- parliamentary material;
- emergency notices;
- and direct technical records.

These sources may be authoritative for:

- what happened operationally;
- what the institution observed;
- what action it took;
- or what attribution the government publicly adopted.

An official source is authoritative evidence of the official position.

That does not automatically expose or independently prove every inference underlying that position.

### 🧪 Tier Two — Independent Technical Research

Examples include:

- malware analysis;
- infrastructure mapping;
- incident-response findings;
- OT research;
- campaign analysis;
- and methodologically transparent security research.

These may be especially strong for:

- tooling;
- infrastructure reuse;
- technical linkage;
- controller behaviour;
- operator overlap;
- or campaign structure.

Technical expertise does not automatically establish political intent, ultimate customer, state direction, or legal responsibility.

### 📰 Tier Three — Reputable Reporting

Established reporting may be strong for:

- chronology;
- institutional response;
- political context;
- investigative direction;
- and what officials or investigators currently assess.

Its evidentiary value still depends on the source chain.

### 🔭 Tier Four — Specialist And Open-Source Analysis

Specialist researchers, analysts, newsletters, and open-source investigators may be useful for:

- discovery;
- comparison;
- pattern recognition;
- technical leads;
- and interpretation.

Their conclusions should not be treated as stronger than the evidence underneath them.

### 📣 Tier Five — Actor Claims And Unverified Material

This may include:

- attacker statements;
- anonymous posts;
- screenshots;
- social-media claims;
- leak sites;
- and unattributed documents.

These may be useful for establishing:

- claimed responsibility;
- messaging;
- propaganda;
- claimed motive;
- chronology;
- or target selection.

They are weak evidence of actual authorship or effect without independent corroboration.

---

## 🧪 Source Type Is Not Source Quality

A source tier describes what kind of source something is.

It does not fully describe how good that source is.

Where material, separately assess:

```text
SOURCE TIER:
SOURCE QUALITY:
```

Useful quality factors include:

- named versus anonymous sourcing;
- direct versus second-hand access;
- documentary support;
- technical reproducibility;
- methodological transparency;
- relevant expertise;
- corrections history;
- and whether the source is reporting what it directly observed or what somebody else told it.

Two Tier Three reports may differ substantially in quality.

Two official statements may answer different questions.

---

## 🪞 Repetition Is Not Corroboration

Record:

```text
ORIGINAL SOURCE:
FIRST REPORT:
LATER REPORTS:
INDEPENDENT CORROBORATION:
COMMON SOURCE DEPENDENCY:
```

Ten articles tracing back to one advisory remain one underlying evidentiary route.

The relevant question is not:

> How many links exist?

It is:

> How many genuinely independent routes support this proposition?

---

## 🧬 Preserve The Provenance Chain

Where the source chain is complex, record how the claim travelled.

For example:

```text
affected institution
→ government brief
→ journalist
→ wire report
→ secondary outlet
```

or:

```text
security vendor
→ technical blog
→ journalist
→ later aggregation
```

This allows the reader to identify when apparent corroboration is actually repetition.

---

## ⚖️ Conflicting Credible Sources Should Stay Conflicting

Do not average disagreement into fake certainty.

Where credible sources conflict, record:

```text
SOURCE A:
WHAT IT CLAIMS:

SOURCE B:
WHAT IT CLAIMS:

POINT OF DISAGREEMENT:
WHY THEY MAY DIFFER:
CURRENT STATUS:
```

Possible reasons may include:

- different observation windows;
- different definitions;
- partial visibility;
- different institutional roles;
- later evidence;
- or genuine disagreement.

If the disagreement remains unresolved, leave it unresolved.

---

## 🎭 Sources Have Different Incentives

Governments, affected companies, security vendors, journalists, regulators, alleged attackers, and contractors may all have different incentives concerning disclosure.

That does not make any category automatically unreliable.

It means the analyst should ask:

```text
WHAT CAN THIS SOURCE ACTUALLY KNOW?
WHAT DOES IT HAVE AN INCENTIVE TO DISCLOSE?
WHAT MIGHT IT HAVE AN INCENTIVE TO WITHHOLD?
```

Source incentives are context.

They are not a substitute for evidence.

---

## 📅 Freshness Matters

Every material source should preserve enough date information to prevent stale evidence being treated as current.

Where relevant, record:

```text
SOURCE DATE:
EVIDENCE CUTOFF:
LAST REVIEWED:
```

A strong April report may remain valuable evidence of an April technical assessment.

It may not represent the attribution position in August.

---

## 🗄️ Preserve Enough Source Detail To Survive A Dead Link

For long-lived records, preserve where useful:

```text
SOURCE BODY / OUTLET:
TITLE:
AUTHOR:
PUBLICATION DATE:
DOCUMENT TYPE:
REFERENCE / ARCHIVE NOTE:
```

The source record should remain intelligible even if the original URL later disappears.

---

## 🧪 Match The Source To The Claim

An affected utility may be authoritative about:

- service disruption;
- operator lockout;
- manual fallback;
- pressure change;
- or recovery.

It may not know the ultimate sponsor.

A security company may establish:

- malware;
- infrastructure;
- tooling;
- controller access;
- or operator overlap.

It may not establish:

- political purpose;
- state direction;
- legal responsibility;
- or final customer.

An alleged attacker can establish:

> We are claiming responsibility.

It cannot establish merely by saying so:

> We caused the incident.

Use each source only for the proposition it can reasonably support.

---

## ⚪ Unknown Is Not One Thing

Do not collapse all missing information into one blank field.

Use explicit statuses.

### UNKNOWN

The answer has not been established.

### NOT PUBLIC

The information may exist but is not publicly available.

### NO EVIDENCE FOUND

A search was performed but no supporting public evidence was located.

### WITHHELD / NCND

An authority was asked or could have answered but declined to confirm or deny.

### NOT APPLICABLE

The question does not apply to this incident.

These statuses are analytically different.

---

## 🕳️ Absence Of Evidence Needs Discipline

Use:

```text
NO PUBLIC EVIDENCE OF X
```

where that is what the record supports.

Do not rewrite it as:

```text
X DID NOT HAPPEN
```

But the reverse mistake is equally dangerous.

Do not convert:

```text
NO PUBLIC EVIDENCE
```

into:

```text
THEREFORE THE STATE MUST SECRETLY KNOW
```

Absence should remain absence.

---

## 🤐 Silence Is Not A Denial

Where an authority says:

> We can neither confirm nor deny.

record that.

Do not translate it into:

> Officials denied it.

Where an authority says:

> We do not comment on operational matters.

do not translate that into:

> No national-security concern exists.

Silence may protect:

- intelligence;
- an investigation;
- operational capability;
- diplomatic space;
- or future legal proceedings.

It may also leave the public evidentiary picture unresolved.

Record the silence.

Do not fill it.

---

## 🔐 Government Attribution Is Itself A Proposition

These are different claims:

```text
THE US GOVERNMENT FORMALLY ATTRIBUTES THE OPERATION TO IRAN
```

and:

```text
IRAN DIRECTED THE OPERATION
```

The first may be:

```text
🟢 CONFIRMED
```

because the government publicly made the attribution.

The confidence attached to the second proposition depends on the evidence available for that proposition.

Government attribution matters.

Government attribution does not erase the distinction between:

```text
public state position
```

and:

```text
independently visible public evidence
```

---

## 🔐 Public Attribution And Private Assessment Are Different Records

The pack should distinguish:

```text
WHAT THE STATE MAY KNOW
```

from:

```text
WHAT THE STATE HAS PUBLICLY ESTABLISHED
```

Where relevant, record:

```text
INTERNAL / INTELLIGENCE POSITION:
UNKNOWN / REPORTED / DISCLOSED

PUBLIC GOVERNMENT ATTRIBUTION:
NONE / SUSPECTED / FORMAL

PUBLIC SUPPORTING EVIDENCE:
NONE / LIMITED / SUBSTANTIAL

PUBLIC LEGAL CONSEQUENCE CLAIMED:
YES / NO / OPEN
```

From outside, these situations can look similar:

```text
we know more than we can say
```

and:

```text
we do not yet know
```

Do not choose between them without evidence.

---

## 🛡️ Private Protection Does Not Require Public Attribution

A state may be unable or unwilling to publicly identify an attacker while still taking protective action.

Record separately:

```text
PUBLIC ATTRIBUTION:
PRIVATE THREAT ASSESSMENT:
PRIVATE PROTECTIVE ACTION:
```

Protective behaviour may provide evidence that an institution assessed some risk.

It does not automatically identify the source of that risk.

Do not reverse-engineer a hidden attribution from protective action alone.

---

## ⚠️ Timing Is Not Attribution

An incident occurring during military escalation may justify additional scrutiny.

Record:

```text
CONTEXT:
Occurred during military escalation.

INFERENCE:
Timing justifies comparison with related incidents.

LIMIT:
Timing alone does not establish Iranian direction.
```

Chronology should not become causation.

Chronology should not disappear either.

---

## 🎯 Target Selection Is Not Attribution

Iranian strategic interest in:

- water;
- energy;
- banks;
- government;
- defence;
- healthcare;
- transport;
- dissidents;
- or coalition support states

may make target selection analytically relevant.

It does not identify the operator.

Many actors can have overlapping incentives.

Target selection is one evidentiary layer.

It is not the whole attribution.

---

## 🧱 Every Material Claim Needs A Limit

Use:

```text
CLAIM:
SOURCE:
SOURCE TIER:
SOURCE QUALITY:
EVIDENTIARY LAYER:
TRAFFIC LIGHT:
WRITTEN CONFIDENCE:
LIMIT:
RIVAL EXPLANATIONS:
LAST REVIEWED:
```

For example:

```text
CLAIM:
The incidents constitute a repeated water-sector pattern.

TRAFFIC LIGHT:
🟢

WRITTEN CONFIDENCE:
High / established.

LIMIT:
The existence of the pattern does not establish
a common operator, customer, or state sponsor.

RIVAL EXPLANATIONS:
Several actors may be independently exploiting
the same exposed technology.
```

The limit is part of the finding.

---

## 🔄 Attribution History Must Remain Visible

Do not silently overwrite:

```text
UNATTRIBUTED
```

with:

```text
IRAN-LINKED
```

when later evidence emerges.

Preserve:

```text
PREVIOUS STATUS:
NEW STATUS:
WHAT CHANGED:
SOURCE:
DATE REVIEWED:
```

Where useful, maintain two histories.

### Operational Development

```text
what happened
→ how effect changed
→ whether more systems were affected
→ whether physical consequences emerged
```

### Attribution Development

```text
unattributed
→ suspected
→ probable
→ confirmed
```

These histories may evolve independently.

---

## ↕️ Confidence Must Move Both Ways

Confidence may increase where there is:

- distinctive shared infrastructure;
- operator overlap;
- financial or communications links;
- recovered tasking;
- independent corroboration;
- hard-to-imitate technical artefacts;
- consistent victimology;
- or formal attribution.

It should decrease where:

- indicators prove generic;
- a source withdraws its claim;
- timestamps conflict;
- actor impact claims are exaggerated;
- ordinary criminal activity fits better;
- apparent shared infrastructure proves coincidental;
- or rival explanations become stronger.

The method must permit:

```text
🟠 SUSPECTED
→
🟡 PROBABLE
→
🟢 CONFIRMED
```

and:

```text
🟡 PROBABLE
→
🟠 SUSPECTED
→
⚪ OPEN / UNATTRIBUTED
→
❌ EXCLUDED
```

A system that only upgrades will eventually convert every theory into fact.

---

## 🧪 Evidence For And Evidence Against

Campaign attribution should not accumulate only confirmatory indicators.

Record both:

```text
EVIDENCE FOR:
EVIDENCE AGAINST:
```

Where the evidence against is simply:

```text
none currently identified
```

say so.

Do not invent balance.

But do not hide evidence that weakens the preferred theory.

---

## 🧯 Rival Explanations Are Mandatory

Every material attribution or campaign hypothesis should record the strongest credible alternative.

Not a straw man.

Possible rival explanations may include:

- ordinary cybercrime;
- unrelated hostile-state activity;
- copycat operations;
- shared vulnerability exploitation;
- insider activity;
- technical failure;
- provider failure;
- false-flag activity;
- opportunistic access;
- or several unrelated incidents clustered by coincidence.

The useful question is:

> What explanation would a sceptical but technically competent reader consider plausible?

That explanation belongs in the record.

---

## 🪞 State What Would Weaken The Theory

For every significant live hypothesis, record where useful:

```text
WHAT WOULD STRENGTHEN THIS:
WHAT WOULD WEAKEN THIS:
WHAT WOULD RULE THIS OUT:
```

This keeps the analysis falsifiable.

The pack should be able to change its mind.

---

## 🇮🇷 The Pack Name Does Not Privilege The Iran Theory

This cluster exists because it tracks cyber risk across the Iran-war environment.

That means Iran is an important hypothesis.

It does not mean Iran is the default answer.

The record must leave genuine room for:

- ordinary crime;
- domestic actors;
- unrelated states;
- technical failure;
- supplier failure;
- independent hacktivists;
- private conflict;
- opportunistic exploitation;
- and mixed ecosystems.

The pack should neither:

```text
turn every unexplained incident into Iran
```

nor:

```text
stop analysing an incident because Iran is not yet proven
```

Both errors defeat the purpose.

---

## 📈 Unattributed Does Not Mean Do Not Analyse

Before sponsorship is known, the pack can still analyse:

- operational effect;
- sector;
- geographic spread;
- target class;
- timing;
- technology;
- infrastructure;
- shared providers;
- manual fallback;
- data effect;
- recurring technique;
- and institutional response.

Attribution is one analytical track.

It is not permission to begin analysis.

---

## 👾 Legal Confidence Is Separate Again

A cyber operation affecting civilians or civilian infrastructure may raise international humanitarian law questions.

That does not settle them.

Use:

```text
LEGAL REVIEW:

NOT INDICATED
MONITOR
REVIEW WARRANTED
ACTIVE LEGAL QUESTION
FORMAL FINDING
```

Preserve:

```text
CYBER INCIDENT
≠
CYBERATTACK FOR IHL PURPOSES
≠
IHL VIOLATION
≠
STATE RESPONSIBILITY
≠
WAR CRIME
≠
INDIVIDUAL CRIMINAL RESPONSIBILITY
```

Strong attribution does not prove unlawfulness.

Serious civilian harm does not prove authorship.

State responsibility does not automatically establish individual criminal responsibility.

Route substantive legal analysis to [👾 Cyber War Crimes](./👾_cyber_war_crimes.md).

---

## ⚖️ Public Legal Leverage May Depend On Public Attribution

A government may privately assess an incident strongly while withholding the evidence supporting that assessment.

That may protect:

- sources;
- methods;
- partner intelligence;
- operational access;
- or an investigation.

It can also leave the public evidentiary record weaker than the private assessment.

That affects what can responsibly be alleged or demonstrated publicly.

It does not determine whether the conduct **was**, as a matter of law, unlawful.

Preserve:

```text
PRIVATE / INTERNAL ASSESSMENT
≠
PUBLICLY DEMONSTRABLE ATTRIBUTION
```

and:

```text
PUBLICLY DEMONSTRABLE ATTRIBUTION
≠
LEGAL FINDING
```

---

## 📋 Relationship Confidence Between Incidents

When two incidents are proposed as related, record:

```text
RELATED INCIDENT:
WHY THEY MAY BE RELATED:
RELATIONSHIP CONFIDENCE:
COMMON TECHNOLOGY:
COMMON TECHNIQUE:
COMMON INFRASTRUCTURE:
COMMON TIMING:
COMMON EFFECT:
STRONGEST REASON THEY MAY BE UNRELATED:
```

This makes cluster construction auditable.

A relationship claim is itself a proposition.

It needs its own confidence.

---

## 🌐 Cross-Sector Pattern Types

Patterns should be described according to what actually recurs.

Possible forms include:

### Same-Sector Recurrence

Repeated attacks on the same type of infrastructure.

### Cross-Sector Recurrence

Similar operations appearing across water, energy, government, finance, health, or other essential systems.

### Common-Technology Recurrence

Several incidents share a product, controller, exploit, platform, or architecture.

### Common-Provider Recurrence

Several affected institutions depend on the same contractor, cloud provider, MSP, identity provider, or integrator.

### Common-Technique Recurrence

The same technique repeatedly appears across otherwise different systems.

### Geographic / Timing Recurrence

Incidents cluster in geography or around military or political events.

These patterns can overlap.

They should not be treated as interchangeable.

---

## 📋 Minimum Incident Record

Every significant incident should be capable of holding:

```text
DATE:
COUNTRY:
SECTOR:
AFFECTED BODY:

IRAN-WAR RELEVANCE:
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
LEGAL REVIEW:

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

COMMON VENDOR / PROVIDER:
COMMON VULNERABILITY:
RELATED INCIDENTS:

EVIDENCE FOR:
EVIDENCE AGAINST:
LIMIT:
RIVAL EXPLANATIONS:

WHAT WOULD STRENGTHEN THIS:
WHAT WOULD WEAKEN THIS:
WHAT WOULD RULE THIS OUT:

ATTRIBUTION HISTORY:
OPERATIONAL HISTORY:

LAST REVIEWED:
NEXT REVIEW:
REVIEW TRIGGER:
CORRECTION STATUS:
EXCLUSION REASON:
```

Where a field is unknown, do not hide it.

Use the correct status:

```text
UNKNOWN
NOT PUBLIC
NO EVIDENCE FOUND
WITHHELD / NCND
NOT APPLICABLE
```

---

## 📋 Minimum Campaign / Cluster Record

Once several incidents begin to matter together, create a campaign-level record.

Use:

```text
CAMPAIGN / CLUSTER NAME:

FIRST OBSERVED:
LATEST OBSERVED:

COUNTRIES:
SECTORS:
NUMBER OF CONFIRMED INCIDENTS:
NUMBER OF SUSPECTED RELATED INCIDENTS:

PATTERN TYPE:
PATTERN STATUS:

AFFECTED TECHNOLOGY:
COMMON VENDOR / PROVIDER:
COMMON VULNERABILITY:
REPEATED TECHNIQUES:
REPEATED EFFECTS:
GEOGRAPHIC CLUSTER:
MILITARY-TIMING RELEVANCE:

COMMON-OPERATOR CONFIDENCE:
COMMON-TASKING CONFIDENCE:
COMMON-CUSTOMER CONFIDENCE:
COMMON-SPONSOR CONFIDENCE:

IRANIAN LINK:
IRAN-WAR RELEVANCE:

EVIDENCE FOR:
EVIDENCE AGAINST:
RIVAL EXPLANATIONS:

WHAT WOULD STRENGTHEN THE RELATIONSHIP:
WHAT WOULD WEAKEN THE RELATIONSHIP:
WHAT WOULD RULE OUT A COMMON CAMPAIGN:

OPERATIONAL DEVELOPMENT:
ATTRIBUTION DEVELOPMENT:

TREND CHANGE:
LAST REVIEWED:
NEXT REVIEW:
REVIEW TRIGGER:
```

This prevents campaign-level conclusions being smuggled into individual incident rows.

It also prevents individual attribution uncertainty from hiding a pattern visible only at aggregate level.

---

## ➖ Negative Findings Matter Too

Relevant negative evidence should be recorded.

Examples include:

- no contamination identified;
- no data exfiltration found;
- no physical-process change observed;
- no service interruption;
- no lateral movement detected;
- no shared infrastructure identified;
- a proposed attribution specifically ruled out;
- or a claimed effect disproved.

A negative finding can narrow the hypothesis space.

It should not disappear merely because it is less dramatic.

---

## 📰 Language Has To Preserve Evidentiary Distance

These words are not interchangeable:

### Reported

A source has said something occurred.

### Claimed

An interested or involved actor has asserted something.

### Suspected

Evidence provides a credible basis for scrutiny but remains incomplete.

### Assessed

An institution or analyst has reached a stated judgement.

### Attributed

Responsibility has been assigned by the named source.

### Demonstrated

The supporting evidence is visible enough to establish the proposition independently.

### Proved

Use sparingly and only where the relevant evidentiary context genuinely warrants it.

Likewise, terms such as:

```text
Iran-linked
Iran-affiliated
Iran-backed
Iran-sponsored
Iran-directed
```

should not appear without enough context to explain what the relationship actually means.

---

## 🔎 Define “Iran-Linked”

The phrase **Iran-linked** is useful precisely because it can describe several different relationships.

It is also dangerous because those relationships can become invisible inside the phrase.

Where possible, specify whether the link means:

- historic government attribution;
- sanctions designation;
- shared infrastructure;
- operator overlap;
- organisational affiliation;
- contractor relationship;
- state support;
- public governmental assessment;
- ideological alignment;
- or another evidenced relationship.

Do not let **linked** do more evidentiary work than the underlying evidence.

---

## 🧭 Corrections Must Propagate

If an assessment materially changes, update every place where the old assessment performs analytical work.

That may include:

- the incident timeline;
- campaign record;
- prose nodes relying on the incident;
- CSV;
- XLSX;
- attribution history;
- pattern status;
- legal-routing status;
- and any reporting guidance built around the earlier assessment.

A correction should not exist in one node while the rest of the pack quietly preserves the old claim.

---

## ⚖️ Common Confidence Failures

Avoid:

- counting repeated articles as independent corroboration;
- using a headline where the underlying source is available;
- treating an actor claim as a finding;
- forcing actor-claimed into the confidence scale;
- treating political branding as technical attribution;
- treating alias reuse as operator continuity;
- treating technical similarity as proof of common operator;
- treating common operator as proof of common customer;
- treating common customer as proof of state direction;
- treating state affiliation as state direction;
- treating proxy as a synonym for politically aligned;
- treating capability as use;
- treating timing as causation;
- treating target selection as attribution;
- treating strategic benefit as sponsorship;
- treating state benefit as control;
- treating criminal motive as proof that no state can later use the access;
- treating criminal activity as proof of state tasking;
- treating a shared provider as proof of a shared attacker;
- treating a pattern as proof of one coordinated campaign;
- treating pattern confidence as attribution confidence;
- treating severity as confidence;
- treating strategic importance as attribution;
- treating confirmed disruption as confirmed authorship;
- applying the deepest effect at one facility to every facility;
- treating manual fallback as no operational harm;
- treating anonymous official suspicion as formal attribution;
- treating government attribution as independently demonstrated public evidence;
- treating NCND as denial;
- treating absence of public evidence as proof something did not happen;
- treating absence of public evidence as proof something is secretly known;
- treating absence of public attribution as absence of strategic relevance;
- treating protective state behaviour as proof of hidden attribution;
- treating technical recovery as proof that downstream human harm ended;
- treating civilian infrastructure involvement as automatic proof of a war crime;
- treating state responsibility and individual criminal responsibility as interchangeable;
- silently overwriting an earlier assessment;
- omitting negative findings;
- omitting evidence against the preferred theory;
- omitting rival explanations;
- dropping the evidentiary limit;
- failing to distinguish unknown from withheld;
- and leaving stale confidence labels in place because they fit the existing narrative.

These errors make the record look cleaner than the evidence.

That is not analytical strength.

It is information loss.

---

## 📰 Reporting Rule

The reporting rule is:

> Say exactly which proposition the evidence supports, and stop where the evidence stops.

Therefore:

```text
INCIDENT CONFIRMED
≠
ATTRIBUTION CONFIRMED
```

and:

```text
PATTERN CONFIRMED
≠
ONE COORDINATED CAMPAIGN CONFIRMED
```

and:

```text
COMMON OPERATOR
≠
COMMON CUSTOMER
```

and:

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

and:

```text
IRAN-LINKED OPERATOR
≠
IRAN DIRECTED THIS OPERATION
```

and:

```text
STATE BENEFIT
≠
STATE CONTROL
```

and:

```text
SYSTEM RESTORED
≠
PERSON-CENTRED RECOVERY COMPLETE
```

and:

```text
CIVILIAN INFRASTRUCTURE AFFECTED
≠
WAR CRIME CONFIRMED
```

Precision does not weaken the analysis.

It makes the analysis capable of surviving the next update.

---

## 🧭 Working Method

For every material claim:

```text
state what happened
↓
decide whether it belongs inside the pack
↓
state what effect is actually established
↓
separate severity from certainty
↓
find the original source
↓
record the source provenance
↓
assess source quality as well as source type
↓
identify genuinely independent corroboration
↓
record credible source disagreement
↓
identify the evidentiary layer
↓
apply the traffic light to that proposition
↓
write the confidence in words
↓
separate incident from effect
↓
separate effect from attribution
↓
separate operator from intermediary
↓
separate intermediary from customer
↓
separate customer from beneficiary
↓
separate state affiliation from state direction
↓
separate attribution from relationship confidence
↓
separate relationship confidence from pattern status
↓
separate pattern from campaign coordination
↓
separate all of those from legal conclusion
↓
state the strongest rival explanation
↓
record evidence for
↓
record evidence against
↓
state the evidentiary limit
↓
record negative findings
↓
record what remains unknown
↓
distinguish unknown from withheld or not public
↓
preserve the previous assessment
↓
record what would strengthen the theory
↓
record what would weaken the theory
↓
record what would rule it out
↓
set the review trigger
```

The pack should recognise the pattern.

It should not manufacture the customer.

It should preserve uncertainty.

It should not allow uncertainty to become an excuse not to notice what is happening.

That is the discipline.

---

## 🌌 Constellations

🔎 🚦 🕸️ 📉 👾 — evidentiary confidence; traffic-light triage; layered attribution; campaign recognition; legal separation.

## ✨ Stardust

cyber attribution, confidence labels, source provenance, corroboration, traffic lights, pattern recognition, proxy operations, evidentiary limits, review status

---

## 🏮 Footer

*🔎 Confidence Labels And Source Rules* is a living node of the **Polaris Protocol**.  
It defines the evidentiary, provenance, confidence, relationship, attribution, campaign, recovery, and review rules used across the *🇮🇷 Data Wars: IRGC Edition* pack. It is intended to make developing patterns visible without allowing uncertainty, repetition, political branding, criminal intermediaries, or state interest to perform attribution work that the evidence has not yet done.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation, analytical perimeter, and pack routing*
> - [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope, country perimeter, and incident inclusion rules*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *technical attribution, public attribution, state responsibility, and uncertainty*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *operators, brokers, intermediaries, customers, and later exploitation*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *cumulative effect, pattern development, and campaign-level interpretation*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *OT depth, control access, manual fallback, and physical-process effects*
> - [🏥 Health, Education And Admin Are Not Soft Extras](./🏥_health_education_and_admin_are_not_soft_extras.md) — *data integrity, authoritative records, and person-centred recovery*
> - [🇬🇧 Britain Is Advertising An Exploitable Seam](./🇬🇧_britain_is_advertising_an_exploitable_seam.md) — *fragmented response, NCND, record reconciliation, and protection pathways*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *public reporting, source chains, corrections, and language discipline*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *separate IHL, state-responsibility, and individual-criminal-responsibility analysis*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *live incident chronology, confidence movement, and pattern status*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-09_
