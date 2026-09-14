# 📰 How To Report Without Overclaiming
**First created:** 2026-08-01 | **Last updated:** 2026-09-14  
*Preserve the event, the source, the evidentiary layer, the confidence, the limit, the rival explanation, and what would change the assessment.*

---

## 🛰️ Orientation

Cyber reporting becomes unreliable when uncertainty is compressed before the evidence is ready.

The familiar failure looks like:

```text
incident
→ claim
→ headline
→ repetition
→ caveat disappears
→ suspicion becomes certainty
```

There is an equal and opposite failure:

```text
incident
→ attribution incomplete
→ story treated as inconclusive
→ operational effect disappears
→ another similar incident occurs
→ attribution remains incomplete
→ developing pattern disappears too
```

This pack should do neither.

A more defensible reporting chain is:

```text
event
→ source
→ evidentiary layer
→ confidence
→ limit
→ rival explanation
→ interpretation
→ review
→ correction where necessary
```

This matters especially during war.

Military escalation creates pressure to explain quickly.

Cyber attribution often develops slowly.

Operational consequences can become visible before sponsorship does.

Campaign-level patterns can strengthen before common-operator confidence does.

Claims can be real while causation is false.

And a system can remain technically available while its users absorb substantial operational harm.

The reporting rule for this pack is therefore:

> Do not attribute beyond the evidence. Do not erase a developing strategic pattern merely because public attribution is incomplete.

And underneath that sit several further rules:

```text
recognise the pattern
≠
manufacture the customer

record the claim
≠
accept the claim

record the effect
≠
infer the sponsor

recognise strategic relevance
≠
declare lawful targetability

recognise adversary benefit
≠
infer adversary causation
```

---

## 🚦 Use The Traffic Lights On The Proposition

Reporting should use the traffic-light system defined in [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md).

The colour belongs to the **specific proposition**, not to the whole incident.

### 🟢 Established / Confirmed

The proposition is strongly supported by the public evidence.

### 🟡 Probable

The available evidence strongly favours the proposition, but an important gap remains.

### 🟠 Suspected / Developing

There is a credible evidentiary basis for scrutiny, but substantial uncertainty remains.

### ⚪ Open / Unattributed

The proposition has not been established.

### ❌ Excluded

Later evidence no longer supports the proposition or inclusion.

A report may therefore correctly say:

```text
INCIDENT:
🟢 CONFIRMED

OPERATIONAL EFFECT:
🟢 CONFIRMED

COMMON OPERATOR:
🟡 PROBABLE

IRANIAN STATE AFFILIATION:
🟠 SUSPECTED

IRANIAN STATE DIRECTION:
⚪ OPEN
```

That is not inconsistent.

It is more informative than giving the entire story one confidence label.

---

## 📣 Actor-Claimed Is Not A Confidence Level

Where an actor claims responsibility, record:

```text
CLAIM STATUS:
📣 ACTOR-CLAIMED
```

Then separately assess whether the attribution is:

```text
🟢 CONFIRMED
🟡 PROBABLE
🟠 SUSPECTED
⚪ OPEN
```

For example:

```text
CLAIM STATUS:
📣 ACTOR-CLAIMED

ATTRIBUTION:
⚪ OPEN
```

means:

> The claim is real. The attribution is not established.

Do not turn:

> The group claimed responsibility.

into:

> The group carried out the attack.

A claim is evidence that somebody wants the public to associate them with the event.

It is not automatically evidence that they caused it.

---

## 📣 Worked Example — A Known Affiliated Actor Claims A New Operation

The Minnesota water case requires more care than either:

> An unknown Telegram account claimed the attack.

or:

> Iran admitted attacking American water systems.

An account using the name **APT IRAN** reportedly said the Minnesota operation was conducted jointly with **CyberAv3ngers** and that the two actors took direct responsibility.

US government reporting had previously described CyberAv3ngers as affiliated with the IRGC Cyber-Electronic Command.

That history makes the new claim materially relevant.

It does not prove:

- current operator continuity;
- current IRGC tasking;
- the accuracy of every claimed effect;
- common responsibility for the wider multi-state wave;
- or formal US attribution of the current campaign.

### Durable headline

> Iran-linked actors claim Minnesota water attacks; US agencies do not publicly validate claim.

### Durable first paragraph

> APT IRAN and CyberAv3ngers have claimed responsibility for the July attacks on Minnesota water systems. US government reporting has previously identified CyberAv3ngers as affiliated with the IRGC's cyber apparatus, but Minnesota authorities and the FBI did not publicly validate the new claim and the investigation remained open.

### Acceptable analytical follow-up

> The claim strengthens the existing Iran-linked assessment because it comes from an actor ecosystem with a relevant, previously attributed history. It does not independently establish authorship, current state direction, or responsibility for every incident in the wider water-system wave.

### Headline that outruns the evidence

> IRGC admits attacking US water systems

That formulation collapses:

```text
prior actor affiliation
+
new responsibility claim
```

into:

```text
proved current IRGC direction
```

without the missing evidentiary steps.

Report the propositions separately:

```text
CLAIM EXISTS:
🟢 ESTABLISHED

PRIOR CYBERAV3NGERS–IRGC AFFILIATION:
🟢 ESTABLISHED IN PRIOR US GOVERNMENT REPORTING

CURRENT AUTHORSHIP:
🟡 PROBABLE / STRENGTHENED

CURRENT IRGC DIRECTION:
⚪ NOT PUBLICLY ESTABLISHED BY THE CLAIM

FORMAL PUBLIC FEDERAL ATTRIBUTION:
⚪ NOT IDENTIFIED
```

---

## 📡 Worked Example — A Real Outage, A Real Claim, And No Causation

The September AT&T episode provides an even cleaner reporting lesson.

A real AT&T outage occurred.

APT IRAN claimed it.

AT&T said the outage was caused by attempted physical cable theft and rejected the cyberattack explanation.

The correct structure is:

```text
OUTAGE:
🟢 CONFIRMED

APT IRAN CLAIM:
🟢 CONFIRMED AS A CLAIM

CYBER CAUSATION:
❌ REJECTED BY THE OPERATOR

IRAN CAUSATION:
⚪ NOT ESTABLISHED
```

### Durable headline

> APT IRAN claims AT&T outage; company says physical cable theft caused disruption.

### Bad headline

> Iran knocks AT&T offline

The second converts:

```text
real outage
+
real claim
```

into:

```text
real causation
```

without evidence.

This is **claim ≠ causation** in its cleanest form.

---

## 🧱 Start With The Event

The event is what happened.

That may include:

- a system became unavailable;
- data was copied;
- records were altered;
- a payment service was disrupted;
- a water operator moved to manual control;
- pressure changed;
- a hospital diverted ambulances;
- a generator stopped producing;
- an actor published stolen material;
- or a government acknowledged an intrusion.

Write the event before the theory.

For example:

> A regional water operator moved part of its system to manual control after unauthorised access was detected.

That sentence may remain valid even if attribution changes three times.

A headline beginning:

> Iran attacks regional water system

may not survive the next update.

The most durable sentence is usually the one closest to the observable event.

---

## 🧱 Separate Event From Effect

Even after the event is established, the effect may require its own confidence assessment.

Distinguish where relevant:

```text
OPERATIONAL EFFECT:
PHYSICAL EFFECT:
SERVICE EFFECT:
SAFETY EFFECT:
DATA-CONFIDENTIALITY EFFECT:
DATA-INTEGRITY EFFECT:
RECORD-INTEGRITY EFFECT:
CIVILIAN EFFECT:
DEPENDENCY EFFECT:
```

A confirmed intrusion does not automatically establish a confirmed physical-process change.

A confirmed breach does not automatically establish that records were altered.

A temporary service interruption does not automatically establish wider system compromise.

Write only the effect the evidence supports.

---

## 🏥 “Still Open” Is Not The Same As “Unaffected”

Healthcare reporting repeatedly demonstrates this problem.

A hospital may remain open while:

- ambulances are diverted;
- appointments are delayed;
- treatment is cancelled;
- patient systems are unavailable;
- central HVAC monitoring is degraded;
- or additional staff are required to keep services running.

The correct formulation may be:

```text
SERVICE CONTINUED
+
SERVICE DEGRADED
```

not:

```text
NO IMPACT
```

### Luminis example

Durable:

> Luminis Health remained operational while diverting some non-critical ambulances and delaying or cancelling some treatment during a cyber incident.

Poor:

> Luminis avoids disruption in cyberattack.

The first records the actual service state.

The second erases the burden carried by patients and staff.

---

## 🏨 Facility Support Is Not “Just Admin”

The Manitoba ransomware incident affected central HVAC monitoring and access-card administration while clinical care continued.

The durable description is:

> Ransomware affected hospital facility-management and access-control support systems; local monitoring and additional security were used while clinical care continued.

Avoid:

> Hospital unaffected by ransomware.

and avoid:

> Hackers took control of hospital ventilation.

Neither matches the evidence.

The correct report preserves:

```text
FACILITY-SUPPORT EFFECT:
YES

LOCAL FALLBACK:
YES

CLINICAL DISRUPTION:
NOT ESTABLISHED

ATTACKER CONTROL OF PHYSICAL PLANT:
NOT ESTABLISHED
```

---

## 🪜 Report How Far Into The Machinery The Evidence Reaches

Operational-technology reporting should distinguish access depth.

Use the ladder from [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md):

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

Do not write:

> Attackers took control of the water system.

where the evidence supports only:

> Attackers accessed an exposed control interface.

Because:

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

---

## ⚓ Reconnaissance Is Not Exploitation

The September Anthropic disclosure concerning an Iran-nexus actor researching:

- US naval movements;
- personnel;
- maritime VSAT;
- Cisco communications;
- and industrial-control products

should be reported as reconnaissance or capability development unless further evidence appears.

Durable:

> Anthropic says an Iran-nexus actor used Claude for naval and technical reconnaissance, including research on maritime communications and industrial-control products.

Not durable:

> Iran hacked US naval control systems using Claude.

The difference is:

```text
research
≠
access

access
≠
exploitation

exploitation
≠
operational effect
```

---

## 🧯 Manual Fallback Is Not No Effect

Reporting often understates incidents where fallback procedures work.

If a utility moves to manual operation, the correct description may be:

```text
AUTOMATED CONTROL DEGRADED
+
MANUAL FALLBACK WORKED
```

not:

```text
NO DISRUPTION
```

Manual fallback can demonstrate resilience and operational impact at the same time.

Report:

- what stopped working normally;
- what staff had to do instead;
- how long the fallback lasted;
- whether service changed;
- and what additional risk or workload was created.

Resilience and harm can coexist.

---

## ⚡ Small Physical Effect Is Still Physical Effect

The UK generator incident provides a useful reporting boundary.

The generator was reportedly offline for four days.

Officials said the wider grid was not threatened.

Durable:

> A cyberattack forced a small UK power generator offline for four days; officials said the wider grid was not affected.

Avoid:

> UK grid hit by Iranian cyberattack.

Avoid:

> No significant effect because the grid stayed up.

Both distort the record.

The accurate structure is:

```text
LOCAL PHYSICAL EFFECT:
YES

NATIONAL GRID EFFECT:
NO

IRAN-LINKED REPORTING:
YES

FORMAL PUBLIC NCSC ATTRIBUTION:
NOT IDENTIFIED
```

---

## 🗣️ A Claim Is Not A Finding

Different people may make different claims about the same incident.

Possible sources include:

- the affected institution;
- a government;
- a regulator;
- police;
- an intelligence or cyber agency;
- a security company;
- an alleged attacker;
- a researcher;
- a journalist;
- or an anonymous official.

Each claim should remain attached to the person or institution making it.

Write:

> Officials said investigators suspected an Iran-linked actor.

Not:

> Iran was responsible.

Write:

> The company said customer data was not affected.

Not:

> No customer data was affected.

unless that proposition is independently established or the sentence clearly preserves who is making the assessment.

A claim becomes a finding only when the evidence supports that transition.

---

## 🔗 Preserve The Source Chain

Ten articles do not necessarily represent ten sources.

They may all trace back to:

- one official statement;
- one security-vendor report;
- one anonymous briefing;
- one leak-site post;
- or one actor claim.

Repetition is not corroboration.

For material claims, preserve:

```text
ORIGINAL SOURCE:
FIRST REPORT:
LATER REPORTS:
INDEPENDENT CORROBORATION:
COMMON SOURCE DEPENDENCY:
```

The newsroom question is not:

> How many outlets are reporting this?

It is:

> How many independent evidentiary routes support this proposition?

Circulation is not verification.

---

## 🧬 Preserve Source Provenance

Where the source chain is complicated, record how the claim travelled.

For example:

```text
affected institution
→ government briefing
→ wire service
→ newspaper
→ social-media summary
```

or:

```text
security vendor
→ technical report
→ journalist
→ aggregation
```

The final article may look independent even where every branch returns to one source.

Source provenance prevents repetition from masquerading as corroboration.

---

## 🧪 Match The Source To The Claim

An affected utility may be authoritative about:

- operator lockout;
- pressure loss;
- manual fallback;
- service continuity;
- and recovery.

It may know very little about the ultimate sponsor.

A cyber-security company may establish:

- malware;
- infrastructure;
- tooling;
- technical overlap;
- or controller access.

It may be less well placed to establish:

- political intent;
- state direction;
- legal responsibility;
- or the final customer.

A government may possess classified evidence unavailable publicly.

An alleged attacker is authoritative about one proposition:

> We are claiming responsibility.

It is not authoritative merely by assertion about:

> We caused the effect we are describing.

Use each source only for the proposition it can reasonably support.

---

## ⚖️ Credible Sources Can Disagree

Do not average conflicting reports into false certainty.

Where credible sources disagree, preserve the disagreement.

Use:

```text
SOURCE A:
WHAT IT SAYS:

SOURCE B:
WHAT IT SAYS:

POINT OF DISAGREEMENT:
POSSIBLE REASON:
CURRENT STATUS:
```

Possible reasons may include:

- different observation windows;
- different technical visibility;
- different definitions;
- different institutional roles;
- later evidence;
- or genuine disagreement.

If the conflict remains unresolved, write that it remains unresolved.

---

## 🍊 Presidential Statements Need Their Own Evidentiary Lane

A presidential statement is a primary source for:

```text
WHAT THE PRESIDENT SAID
```

It is not automatically a primary technical source for:

```text
WHO CONDUCTED THE CYBER OPERATION
```

The Minnesota example is useful.

Durable:

> President Trump publicly rejected Iran as the explanation for the Minnesota water attacks. The White House did not publicly identify an alternative actor, while reporting indicated that intelligence agencies suspected Iran.

Avoid:

> Trump disproved the Iran attribution.

Avoid:

> Trump knowingly lied about the Iran attribution.

Neither follows from the public record.

The first overweights political authority as technical evidence.

The second invents motive and knowledge.

---

## ⚪ Unknown Is Not One Thing

Missing information should be described precisely.

Use:

### UNKNOWN

The answer has not been established.

### NOT PUBLIC

The information may exist but is not publicly available.

### NO EVIDENCE FOUND

A search was performed but no supporting public evidence was identified.

### WITHHELD / NCND

The relevant authority declined to confirm or deny.

### NOT APPLICABLE

The question does not apply.

Do not turn all five into:

> Unknown.

They describe different evidentiary situations.

---

## 🕳️ Absence Of Evidence Is Not A Finding Of Absence

Write:

> No public evidence currently links the incident to Iran.

where that is the supportable statement.

Do not silently upgrade that into:

> Iran was not involved.

But do not make the opposite leap either:

> No public evidence exists, therefore officials must secretly know Iran did it.

Both exceed the evidence.

Use the narrowest proposition the record supports.

---

## ⚖️ The Headline Must Not Outrun The Source

The headline should reflect the strongest supportable proposition.

Bad:

> IRGC Shuts Down British Power Grid

Better:

> Small UK Generator Offline Four Days After Cyberattack; Iran Link Reported

Bad:

> Iran Uses AI To Hack US Naval Systems

Better:

> Anthropic Reports Iran-Nexus AI-Assisted Naval And Technical Reconnaissance

Bad:

> Russian Hackers Take Over Global Critical Infrastructure With AI

Better:

> PaperCut Campaign Uses AI Agents To Exploit Hundreds Of Servers Across Multiple Sectors

Bad:

> Iran Knocks AT&T Offline

Better:

> APT IRAN Claims AT&T Outage; Company Says Physical Cable Theft Was Cause

Bad:

> Cyberattack Leaves Hospital Unaffected

Better:

> Hospital Maintains Care While Cyber Incident Disrupts Facility-Support Systems

The less dramatic headline may be more durable.

---

## 🕸️ Distinguish Attribution From Relevance

An incident can belong in the Iran-war timeline without being attributed to Iran.

Its relevance may arise from:

- sector;
- timing;
- location;
- target selection;
- operational effect;
- the country's role in the wider war;
- similarity to another cluster;
- shared technology;
- defender load;
- or an important rival explanation.

Write why the incident is being watched.

For example:

> The breach remains unattributed. It is included because it affected essential state infrastructure during the war period and because its relationship to a wider cluster remains open.

That is an explanation of inclusion.

It is not an accusation.

---

## 🧬 Pattern Confidence Is Not Sponsor Confidence

This distinction now needs to be explicit in reporting.

By September, the pack supports:

```text
MULTIPLE THREAT ECOSYSTEMS:
🟢 ESTABLISHED

CUMULATIVE DEFENDER BURDEN:
🟢 ESTABLISHED

ONE COMMON OPERATOR:
⚪ NOT ESTABLISHED

ONE COMMON SPONSOR:
⚪ NOT ESTABLISHED
```

A durable sentence may therefore be:

> Essential infrastructure across several sectors is experiencing elevated cyber pressure during the Iran war, including an Iran-linked water/OT core and several unrelated criminal or state-linked ecosystems.

Avoid:

> Iran launches sweeping cyberattack across water, hospitals, courts and finance.

The latter borrows evidence across ecosystems.

That is exactly what the pack is designed not to do.

---

## 🤖 Shared Vulnerability Is Not Strategic Selection

PaperCut and Cl0p-style campaigns require special care.

A broad victim list may arise because:

```text
many organisations
run the same vulnerable software
```

not because:

```text
the attacker strategically selected
every victim
```

Durable:

> A mass-exploitation campaign compromised organisations across government, education, healthcare, finance and industrial sectors through a shared software vulnerability.

Avoid:

> Attackers strategically targeted multiple critical sectors.

unless victim selection evidence exists.

The right follow-up question is:

> What was the exposed denominator?

Only then can strategic selection be tested.

---

## 🧅 Initial Access And Later Use Need Separate Sentences

One actor may create access.

Another may buy or use it later.

Therefore write:

> The campaign appears to have created privileged access across a broad victim population. Public evidence has not established whether any footholds were later sold or used by state customers.

Do not write:

> The campaign created access for hostile states.

unless the transfer is evidenced.

The distinction is:

```text
ACCESS MANUFACTURED:
YES

ACCESS TRANSFER:
OPEN

LATER STATE CUSTOMER:
OPEN
```

---

## 🌊 Causal Contribution Is Not Command

A later incident may be enabled by an earlier one without sharing the same command structure.

Durable:

> The earlier compromise may have reduced the cost of later exploitation.

Avoid:

> The first actor directed the later attack.

unless there is evidence of tasking or control.

Keep:

```text
CAUSALLY DOWNSTREAM
≠
ORGANISATIONALLY DOWNSTREAM
```

visible.

---

## 🌍 Alliance Benefit Is Not Alliance Causation

The same discipline applies to geopolitics.

Durable:

> Allied policy divergence may create a wider opportunity window for adversaries by slowing common assessment or response.

Avoid:

> Iran caused allied division.

unless evidence exists.

The distinction is:

```text
ADVERSARY BENEFIT
≠
ADVERSARY CAUSED THE CONDITION
```

This prevents a real strategic effect from turning into an unsupported influence claim.

---

## 🇬🇧 Alliance Friction Is Not NATO Collapse

Where allies hedge, duplicate planning or become more cautious, describe the actual behaviour.

Use:

> Allies are building additional national contingency planning around uncertainty in US policy.

Not:

> NATO is collapsing.

unless the evidence genuinely supports institutional breakdown.

Useful distinctions are:

```text
POLICY DIVERGENCE
≠
ALLIANCE COLLAPSE

HEDGING
≠
WITHDRAWAL

HIGHER TRANSACTION COST
≠
LOSS OF ALL COOPERATION
```

Precision is especially important because geopolitical rhetoric tends to expand faster than the evidence.

---

## ⚖️ Strategic Importance Is Not Lawful Targetability

The pack uses phrases such as:

- state infrastructure;
- part of the battlespace;
- essential system;
- military-supporting logistics;
- strategic dependency.

None of these phrases automatically means:

> lawful military objective.

Reporting should preserve:

```text
STRATEGIC IMPORTANCE
≠
LAWFUL TARGETABILITY
```

and:

```text
CIVILIAN INFRASTRUCTURE AFFECTED
≠
WAR CRIME CONFIRMED
```

Durable:

> The cyber operation affected civilian water infrastructure during an armed conflict and warrants separate IHL review.

Avoid:

> Iran committed a cyber war crime against US water systems.

unless the relevant legal and attribution elements are actually established.

---

## 👾 War-Crime Reporting Needs A Longer Ladder

Before using **war crime**, establish:

```text
TECHNICAL EVENT
↓
ARMED-CONFLICT NEXUS
↓
QUALIFIES AS AN ATTACK UNDER THE APPLICABLE POSITION
↓
TARGET STATUS
↓
APPLICABLE IHL RULE
↓
BREACH
↓
ATTRIBUTION
↓
INDIVIDUAL ACTOR
↓
MENTAL ELEMENT
↓
MODE OF LIABILITY
↓
JURISDICTION
```

A serious civilian cyber incident can deserve urgent legal scrutiny without yet meeting that chain.

Do not make legal seriousness depend on rhetorical certainty.

---

## 📉 “Campaign” Needs A Modifier

The word **campaign** can mean several different things.

Use a modifier.

### Technically linked campaign

Where the same operator, infrastructure, tooling or access pattern joins the incidents.

### Strategically linked campaign

Where separate operations are credibly tied to one sponsor or objective.

### Shared-vulnerability campaign

Where one product or platform creates the victim population.

### Criminal-extortion campaign

Where the organising mechanism is monetisation.

### Access-manufacturing campaign

Where the primary output is privileged footholds.

### Narrative campaign

Where claiming, amplification or selective publicity is the main observable mechanism.

### Campaign environment

Where several threat ecosystems are operating in the same conflict period and consuming the same defenders.

Avoid writing:

> campaign

as though all six mean the same thing.

---

## 🧮 Campaign Effect Can Be Stronger Than Campaign Attribution

A useful September formulation is:

> The cumulative campaign effect is now easier to establish than a single campaign command structure.

That means:

```text
CUMULATIVE ESSENTIAL-INFRASTRUCTURE PRESSURE:
🟢 ESTABLISHED

ONE COMMON OPERATOR:
⚪ NOT ESTABLISHED

ONE COMMON CUSTOMER:
⚪ NOT ESTABLISHED

ONE COMMON SPONSOR:
⚪ NOT ESTABLISHED
```

That is not evasive.

It is the evidence.

---

## 📉 Small Does Not Mean Strategically Trivial

Avoid assuming that:

```text
small outage
=
small significance
```

A limited incident may demonstrate:

- physical reach;
- repeatable access;
- weak segmentation;
- exploitable suppliers;
- poor asset inventory;
- or a defender's response time.

Durable:

> The generator was small and the wider grid remained unaffected, but the incident demonstrated a cyber-induced physical shutdown lasting four days.

That sentence preserves both scale and significance.

---

## 🧱 Local Ownership Does Not Mean Local Significance

A small water utility may be locally owned.

If more than 100 similar systems are being targeted, the issue becomes national.

Durable:

> The affected systems are locally operated, but the repeated targeting of the same class of internet-exposed control technology creates a national resilience problem.

Avoid:

> These were only local incidents.

Ownership and significance are different propositions.

---

## 🧾 Negative Findings Belong In The Story

Where an important feared effect did **not** occur, preserve it.

Examples:

```text
NO CONTAMINATION ESTABLISHED
NO GRID-WIDE EFFECT
NO COURT-SERVICE SHUTDOWN
NO CLINICAL DISRUPTION REPORTED
NO PORT OT COMPROMISE ESTABLISHED
NO IRAN LINK FOUND
```

Negative findings prevent readers from imagining a larger event than the evidence supports.

They are not concessions.

They are part of accurate reporting.

---

## 🔀 Rival Explanations Belong Beside The Preferred One

Where several explanations remain plausible, state them.

For example:

```text
IRAN-LINKED ACTIVITY
vs
COPYCAT
vs
CRIMINAL ACCESS
vs
OTHER STATE ACTOR
vs
SHARED-VULNERABILITY EXPLOITATION
```

or:

```text
CYBERATTACK
vs
PHYSICAL CABLE THEFT
vs
TECHNICAL FAILURE
```

Do not bury the rival in a final sentence after presenting the preferred explanation as fact.

If the rival remains live, it belongs in the main evidentiary structure.

---

## 🧭 Report The Organising Mechanism

When several incidents appear related, ask:

> What actually joins them?

Possible answers include:

- same actor;
- same malware;
- same infrastructure;
- same target class;
- same vulnerable product;
- same supplier;
- same customer;
- same commissioner;
- same access broker;
- same claim narrative;
- same defensive seam;
- or merely the same conflict window.

A durable report says:

> The incidents share exposure to the same controller family.

rather than:

> The incidents are part of one operation.

unless one operation is actually supported.

---

## 🧪 Separate Evidence, Inference, Limit And Rival

For analytical writing, use:

```text
EVIDENCE:
what the public record directly supports

INFERENCE:
what the evidence reasonably suggests

LIMIT:
what remains unproven

RIVAL EXPLANATION:
what else could plausibly explain the same facts
```

Example:

```text
EVIDENCE:
More than 100 internet-exposed water systems were targeted in July.

INFERENCE:
The water-sector problem is national in scale rather than a collection of isolated local incidents.

LIMIT:
Public evidence does not establish one operator across all 100+ systems.

RIVAL EXPLANATION:
Several actors may have exploited the same exposed technology during the same period.
```

This is the default structure when the evidence is complex.

---

## 🔄 Correction Is Part Of The Method

Cyber attribution changes.

Reporting should be designed to survive correction.

Where a proposition changes:

- preserve the earlier assessment;
- record the new evidence;
- explain why the confidence changed;
- and update the current status.

Use:

```text
PREVIOUS ASSESSMENT:
NEW EVIDENCE:
WHAT CHANGED:
CURRENT ASSESSMENT:
```

Do not quietly rewrite history so the pack appears to have been right all along.

A correction is evidence that the method works.

---

## 🚫 Common Overclaiming Failures

Avoid:

- “Iran attacked” where the source says “Iran-linked”;
- “IRGC” where the source says “Iran-nexus”;
- “state-directed” where the source says “state-linked”;
- “hacked” where the evidence only shows reconnaissance;
- “took control” where evidence shows access;
- “physical attack” where evidence shows administrative IT disruption;
- “hospital unaffected” where services continued under degraded conditions;
- “war crime” where only civilian cyber harm is established;
- “NATO collapse” where the evidence shows policy divergence or hedging;
- “cyberattack” where the affected operator says physical damage or theft caused the outage;
- “campaign” without identifying what kind of campaign is meant;
- “multiple sources confirm” where multiple articles repeat the same underlying source;
- “no evidence” when the correct status is “not public” or “not yet established”;
- “state benefit proves state control”;
- “criminal operator proves no later state use”;
- or “strategically useful victim proves strategic selection.”

These are not minor wording problems.

They change the proposition.

---

## 🧭 Reporting Template

For a complex incident, use:

```text
HEADLINE:

DATE:
LOCATION:
SECTOR:

EVENT:
EFFECT:

SYSTEM LAYER:
MANUAL FALLBACK:
PHYSICAL EFFECT:
SERVICE EFFECT:
DATA EFFECT:

PRIMARY SOURCE:
INDEPENDENT CORROBORATION:
SOURCE DEPENDENCY:

CLAIM STATUS:
CLAIMED ACTOR:

TECHNICAL OPERATOR:
STATE RELATIONSHIP:
STATE DIRECTION:
FORMAL ATTRIBUTION:

PATTERN STATUS:
ORGANISING MECHANISM:
COMMON OPERATOR CONFIDENCE:
COMMON CUSTOMER CONFIDENCE:
COMMON SPONSOR CONFIDENCE:
SHARED DEFENDER-BURDEN CONFIDENCE:

IRAN-WAR RELEVANCE:
IRAN ATTRIBUTION:

LEGAL RELEVANCE:
IHL REVIEW NEEDED:
WAR-CRIME STATUS:

NEGATIVE FINDINGS:
RIVAL EXPLANATIONS:

EVIDENCE:
INFERENCE:
LIMIT:
WHAT WOULD CHANGE THE ASSESSMENT:

LAST REVIEWED:
```

For political / alliance reporting, add:

```text
POLICY POSITION:
PREVIOUSLY COORDINATED POSITION:
CHANGE:
ALLIED RESPONSE:
OPERATIONAL CONSEQUENCE:
ADVERSARY BENEFIT:
ADVERSARY CAUSATION:
```

---

## 🧠 Current Reporting Rules — 14 September 2026

The September update adds several durable newsroom rules:

```text
100+ SYSTEMS TARGETED
≠
100+ SYSTEMS DISRUPTED

IRAN-LINKED CORE
≠
IRAN ATTRIBUTION FOR THE WHOLE DATASET

REAL OUTAGE
+
REAL CLAIM
≠
REAL CAUSATION

RECONNAISSANCE
≠
EXPLOITATION

SHARED SOFTWARE
≠
STRATEGIC SELECTION

ACCESS MANUFACTURED
≠
LATER STATE CUSTOMER PROVED

SERVICE CONTINUED
≠
NO OPERATIONAL EFFECT

SMALL PHYSICAL EFFECT
≠
NO STRATEGIC SIGNIFICANCE

CAMPAIGN EFFECT
≠
COMMON COMMAND

ALLIED HEDGING
≠
ALLIANCE COLLAPSE

ADVERSARY BENEFIT
≠
ADVERSARY CAUSATION

CIVILIAN INFRASTRUCTURE AFFECTED
≠
WAR CRIME CONFIRMED
```

These should now sit visibly across the pack.

---

## 🌌 Constellations

📰 🔎 🕸️ 📣 🧬 ⚖️ 🌍 🚰 — reporting discipline; confidence; attribution; actor claims; campaign structure; legal precision; alliance framing; infrastructure effects.

---

## ✨ Stardust

cyber reporting, evidence, confidence labels, attribution, actor claims, causation, campaign language, operational effects, reconnaissance, access manufacturing, shared vulnerabilities, negative findings, rival explanations, legal reporting, war crimes, alliance hedging, source provenance, corrections, overclaiming

---

## 🏮 Footer

*📰 How To Report Without Overclaiming* is a living node of the **Polaris Protocol**.  
It provides the language-control layer for the *🇮🇷 Data Wars: IRGC Edition* pack, ensuring incident, effect, attribution, campaign, legal and alliance claims remain attached to the evidence that actually supports them.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md) — *confidence mechanics and source hierarchy*
> - [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *source provenance, negative findings and rival explanations*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *proposition-level attribution*
> - [🌊 Riding Every Wave](./🌊_riding_every_wave.md) — *claims, causal relationships and mixed ecosystems*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *campaign-environment separation*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *cumulative effect without common-command inflation*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *technical depth and physical-effect language*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *legal-language discipline*
> - [🍊 Why Is the Orange Being Weird?](./🍊_why_is_the_orange_being_weird.md) — *presidential and governance claims*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *live chronology through 14 September 2026*
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
