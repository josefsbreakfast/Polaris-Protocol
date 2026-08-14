# 📰 How To Report Without Overclaiming

**First created:** 2026-08-01 \| **Last updated:** 2026-08-14\
*Preserve the event, the source, the evidentiary layer, the confidence,
the limit, the rival explanation, and what would change the assessment.*

------------------------------------------------------------------------

## 🛰️ Orientation

Cyber reporting becomes unreliable when uncertainty is compressed before
the evidence is ready.

The familiar failure looks like:

``` text
incident
→ claim
→ headline
→ repetition
→ caveat disappears
→ suspicion becomes certainty
```

There is an equal and opposite failure:

``` text
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

``` text
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

The reporting rule for this pack is therefore:

> Do not attribute beyond the evidence. Do not erase a developing
> strategic pattern merely because public attribution is incomplete.

And underneath that sits a second rule:

``` text
recognise the pattern
≠
manufacture the customer
```

------------------------------------------------------------------------

## 🚦 Use The Traffic Lights On The Proposition

Reporting should use the traffic-light system defined in [🔎 Confidence
Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md).

The colour belongs to the **specific proposition**, not to the whole
incident.

### 🟢 Established / Confirmed

The proposition is strongly supported by the public evidence.

### 🟡 Probable

The available evidence strongly favours the proposition, but an
important gap remains.

### 🟠 Suspected / Developing

There is a credible evidentiary basis for scrutiny, but substantial
uncertainty remains.

### ⚪ Open / Unattributed

The proposition has not been established.

### ❌ Excluded

Later evidence no longer supports the proposition or inclusion.

A report may therefore correctly say:

``` text
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

It is more informative than giving the entire story one confidence
label.

------------------------------------------------------------------------

## 📣 Actor-Claimed Is Not A Confidence Level

Where an actor claims responsibility, record:

``` text
CLAIM STATUS:
📣 ACTOR-CLAIMED
```

Then separately assess whether the attribution is:

``` text
🟢 CONFIRMED
🟡 PROBABLE
🟠 SUSPECTED
⚪ OPEN
```

For example:

``` text
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

A claim is evidence that somebody wants the public to associate them
with the event.

It is not automatically evidence that they caused it.

------------------------------------------------------------------------

## 🧱 Start With The Event

The event is what happened.

That may include:

-   a system became unavailable;
-   data was copied;
-   records were altered;
-   a payment service was disrupted;
-   a water operator moved to manual control;
-   pressure changed;
-   a hospital supplier lost access;
-   an actor published stolen material;
-   or a government acknowledged an intrusion.

Write the event before the theory.

For example:

> A regional water operator moved part of its system to manual control
> after unauthorised access was detected.

That sentence may remain valid even if attribution changes three times.

A headline beginning:

> Iran attacks regional water system

may not survive the next update.

The most durable sentence is usually the one closest to the observable
event.

------------------------------------------------------------------------

## 🧱 Separate Event From Effect

Even after the event is established, the effect may require its own
confidence assessment.

Distinguish where relevant:

``` text
OPERATIONAL EFFECT:
PHYSICAL EFFECT:
SERVICE EFFECT:
SAFETY EFFECT:
DATA-CONFIDENTIALITY EFFECT:
DATA-INTEGRITY EFFECT:
RECORD-INTEGRITY EFFECT:
CIVILIAN EFFECT:
```

A confirmed intrusion does not automatically establish a confirmed
physical-process change.

A confirmed breach does not automatically establish that records were
altered.

A temporary service interruption does not automatically establish wider
system compromise.

Write only the effect the evidence supports.

------------------------------------------------------------------------

## 🪜 Report How Far Into The Machinery The Evidence Reaches

Operational-technology reporting should distinguish access depth.

Use the ladder from [🚰 When Cyber Reaches The
Machinery](./🚰_when_cyber_reaches_the_machinery.md):

``` text
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

``` text
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

``` text
loss of view
≠
loss of control
≠
attacker control
```

------------------------------------------------------------------------

## 🧯 Manual Fallback Is Not No Effect

Reporting often understates incidents where fallback procedures work.

If a utility moves to manual operation, the correct description may be:

``` text
AUTOMATED CONTROL DEGRADED
+
MANUAL FALLBACK WORKED
```

not:

``` text
NO DISRUPTION
```

Manual fallback can demonstrate resilience and operational impact at the
same time.

Report:

-   what stopped working normally;
-   what staff had to do instead;
-   how long the fallback lasted;
-   whether service changed;
-   and what additional risk or workload was created.

Resilience and harm can coexist.

------------------------------------------------------------------------

## 🗣️ A Claim Is Not A Finding

Different people may make different claims about the same incident.

Possible sources include:

-   the affected institution;
-   a government;
-   a regulator;
-   police;
-   an intelligence or cyber agency;
-   a security company;
-   an alleged attacker;
-   a researcher;
-   a journalist;
-   or an anonymous official.

Each claim should remain attached to the person or institution making
it.

Write:

> Officials said investigators suspected an Iran-linked actor.

Not:

> Iran was responsible.

Write:

> The company said customer data was not affected.

Not:

> No customer data was affected.

unless that proposition is independently established or the sentence
clearly preserves who is making the assessment.

A claim becomes a finding only when the evidence supports that
transition.

------------------------------------------------------------------------

## 🔗 Preserve The Source Chain

Ten articles do not necessarily represent ten sources.

They may all trace back to:

-   one official statement;
-   one security-vendor report;
-   one anonymous briefing;
-   one leak-site post;
-   or one actor claim.

Repetition is not corroboration.

For material claims, preserve:

``` text
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

------------------------------------------------------------------------

## 🧬 Preserve Source Provenance

Where the source chain is complicated, record how the claim travelled.

For example:

``` text
affected institution
→ government briefing
→ wire service
→ newspaper
→ social-media summary
```

or:

``` text
security vendor
→ technical report
→ journalist
→ aggregation
```

The final article may look independent even where every branch returns
to one source.

Source provenance prevents repetition from masquerading as
corroboration.

------------------------------------------------------------------------

## 🧪 Source Type Is Not Source Quality

An official source, technical report, reputable newspaper, specialist
analyst, and actor claim perform different evidentiary jobs.

But source category alone is not enough.

Where important, ask:

``` text
IS THE SOURCE NAMED?
IS THE SOURCE DIRECT?
IS DOCUMENTARY SUPPORT AVAILABLE?
IS THE TECHNICAL METHOD REPRODUCIBLE?
DOES THE SOURCE HAVE RELEVANT EXPERTISE?
IS THE CLAIM FIRST-HAND OR SECOND-HAND?
IS THERE INDEPENDENT CORROBORATION?
```

Two reputable news reports may have radically different evidentiary
weight.

Two government statements may answer completely different questions.

Do not treat the source hierarchy as an automatic truth hierarchy.

------------------------------------------------------------------------

## 🧪 Match The Source To The Claim

An affected utility may be authoritative about:

-   operator lockout;
-   pressure loss;
-   manual fallback;
-   service continuity;
-   and recovery.

It may know very little about the ultimate sponsor.

A cyber-security company may establish:

-   malware;
-   infrastructure;
-   tooling;
-   technical overlap;
-   or controller access.

It may be less well placed to establish:

-   political intent;
-   state direction;
-   legal responsibility;
-   or the final customer.

A government may possess classified evidence unavailable publicly.

An alleged attacker is authoritative about one proposition:

> We are claiming responsibility.

It is not authoritative merely by assertion about:

> We caused the effect we are describing.

Use each source only for the proposition it can reasonably support.

------------------------------------------------------------------------

## ⚖️ Credible Sources Can Disagree

Do not average conflicting reports into false certainty.

Where credible sources disagree, preserve the disagreement.

Use:

``` text
SOURCE A:
WHAT IT SAYS:

SOURCE B:
WHAT IT SAYS:

POINT OF DISAGREEMENT:
POSSIBLE REASON:
CURRENT STATUS:
```

Possible reasons may include:

-   different observation windows;
-   different technical visibility;
-   different definitions;
-   different institutional roles;
-   later evidence;
-   or genuine disagreement.

If the conflict remains unresolved, write that it remains unresolved.

------------------------------------------------------------------------

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

------------------------------------------------------------------------

## 🕳️ Absence Of Evidence Is Not A Finding Of Absence

Write:

> No public evidence currently links the incident to Iran.

where that is the supportable statement.

Do not silently upgrade that into:

> Iran was not involved.

But do not make the opposite leap either:

> No public evidence exists, therefore officials must secretly know Iran
> did it.

Both exceed the evidence.

Use the narrowest proposition the record supports.

------------------------------------------------------------------------

## ⚖️ The Headline Must Not Outrun The Source

The headline should reflect the strongest supportable proposition.

Bad:

> IRGC Shuts Down British Hospital Network

Better:

> Hospital Network Disrupted In Cyberattack; Attribution Remains Open

Bad:

> Iranian Hackers Steal Government Records

Better:

> Group Claiming Iran Links Publishes Alleged Government Records

Bad:

> No Evidence Iran Was Involved

Better:

> No Public Attribution Has Been Made; Investigation Remains Open

Bad:

> Iranian Cyber Campaign Hits US Water

Better, where pattern is stronger than sponsorship:

> Multi-State Water Cyber Campaign Expands; Iranian Link Remains Under
> Investigation

The less dramatic headline may be more durable.

------------------------------------------------------------------------

## 🕸️ Distinguish Attribution From Relevance

An incident can belong in the Iran-war timeline without being attributed
to Iran.

Its relevance may arise from:

-   sector;
-   timing;
-   location;
-   target selection;
-   operational effect;
-   the country's role in the wider war;
-   similarity to another cluster;
-   or shared technology.

Write why the incident is being watched.

For example:

> The breach remains unattributed. It is included because it affected
> essential state infrastructure during the war period and because its
> relationship to a wider cluster remains open.

That is an explanation of inclusion.

It is not an accusation.

------------------------------------------------------------------------

## 🗺️ Country Relevance Is Not Attribution

A state may be highly relevant to the Iranian operational map because it
is:

-   a direct belligerent;
-   a basing state;
-   a logistics provider;
-   an interception partner;
-   an intelligence partner;
-   a sanctions participant;
-   or part of infrastructure supporting the opposing coalition.

That may increase the strategic relevance of an incident there.

It does not make Iran the default explanation.

Report separately:

``` text
IRAN-WAR RELEVANCE:
```

and:

``` text
IRANIAN ATTRIBUTION:
```

Do not let one perform the work of the other.

------------------------------------------------------------------------

## 🎯 Target Selection Is Not Attribution

Water, energy, hospitals, government administration, banks, transport,
telecommunications, defence systems, or dissidents may all be
strategically attractive targets.

But many actors can share the same target interest.

Target selection can strengthen interpretation.

It cannot identify the operator by itself.

------------------------------------------------------------------------

## ⚠️ Timing Is Not Attribution

An incident occurring immediately after military escalation, a public
threat, or a major strike may deserve scrutiny.

It does not prove causation.

A useful formulation is:

``` text
CONTEXT:
The incident occurred during military escalation.

INFERENCE:
The timing justifies comparison with related activity.

LIMIT:
Timing alone does not establish Iranian direction.
```

Chronology is evidence of chronology.

Do not make it do more work than that.

------------------------------------------------------------------------

## 🎭 Branding Is Not Identity

Groups may use:

-   Iranian symbols;
-   IRGC language;
-   pro-Palestinian messaging;
-   patriotic slogans;
-   religious imagery;
-   anti-Western rhetoric;
-   or familiar actor names.

Those may matter as messaging.

They do not independently prove:

-   nationality;
-   operator continuity;
-   technical authorship;
-   state control;
-   state tasking;
-   or even that the claimed incident occurred.

Report the branding.

Do not let the branding perform the attribution.

------------------------------------------------------------------------

## 🎭 A Familiar Alias May Not Mean Familiar Operators

The reuse of a known group name does not automatically establish
continuity.

Where important, distinguish:

``` text
ALIAS CONTINUITY:
OPERATOR CONTINUITY:
INFRASTRUCTURE CONTINUITY:
TOOLING CONTINUITY:
```

A historic attribution attached to an alias should not silently migrate
to every later person using that name.

------------------------------------------------------------------------

## 🕸️ "Iran-Linked" Needs A Link

Avoid using **Iran-linked** as a self-explanatory label.

Where possible, state what the link actually is.

It may mean:

-   historic government attribution;
-   sanctions designation;
-   infrastructure overlap;
-   operator overlap;
-   organisational affiliation;
-   contractor relationship;
-   state support;
-   public government assessment;
-   or ideological alignment.

Those are not equivalent.

Write the relationship rather than relying on the adjective.

------------------------------------------------------------------------

## 🎭 Proxy Is Not A Synonym For Aligned

Do not write **Iranian proxy** merely because a non-state actor appears
politically sympathetic to Iran.

Where proxy language is used, identify the relationship actually
supported by evidence.

That may include:

-   funding;
-   tasking;
-   command;
-   shared personnel;
-   technical assistance;
-   access provision;
-   infrastructure sharing;
-   operational coordination;
-   tolerated activity;
-   or ideological alignment.

Those relationships carry different implications.

------------------------------------------------------------------------

## 🕸️ State Relationship Terms Need Precision

These phrases should not be treated as interchangeable:

``` text
state-linked
state-affiliated
state-backed
state-supported
state-sponsored
state-encouraged
state-tolerated
state-directed
```

A report should use the narrowest term justified by the evidence.

In particular:

``` text
STATE AFFILIATION
≠
STATE DIRECTION
```

and:

``` text
STATE TOLERANCE
≠
STATE DIRECTION
```

and:

``` text
STATE BENEFIT
≠
STATE CONTROL
```

------------------------------------------------------------------------

## 🧅 The Operator And Customer May Differ

The immediate operator may be:

-   a criminal;
-   an access broker;
-   a contractor;
-   a hacktivist;
-   a security-for-hire operator;
-   or a recruit completing a narrow technical task.

The eventual customer may be different.

Avoid collapsing:

``` text
operator
=
organiser
=
broker
=
buyer
=
beneficiary
=
state
```

Where evidence supports only one layer, report that layer.

For example:

> Investigators linked the intrusion to a criminal access broker. No
> public evidence has established who ultimately purchased or used the
> access.

That preserves the open question without inventing an answer.

------------------------------------------------------------------------

## 🧅 Criminal Does Not Finish The Attribution

A cybercrime explanation may accurately identify the immediate operator.

It does not necessarily settle the wider access chain.

Preserve both propositions:

``` text
CRIMINAL OPERATOR
≠
NO STATE CUSTOMER
```

and:

``` text
CRIMINAL OPERATOR
≠
STATE CUSTOMER
```

A criminal actor may simply be a criminal actor.

The actor may also:

-   sell access;
-   resell data;
-   work for several customers;
-   accept later tasking;
-   or unknowingly provide material that another actor subsequently
    uses.

Do not infer any of those relationships without evidence.

But do not declare the customer question closed merely because the hands
on the keyboard were criminal.

------------------------------------------------------------------------

## 🪜 The Customer May Enter Later

The cyber chain may develop over time.

For example:

``` text
initial compromise
→ access retained
→ access advertised
→ broker involved
→ access purchased
→ later tasking
→ downstream exploitation
```

Evidence about the initial operator may therefore say little about the
final customer.

Report the chronology of the relationship where it is known.

Do not flatten a layered ecosystem into one actor.

------------------------------------------------------------------------

## 🧪 Capability Is Not Use

A group may be known to possess:

-   a particular malware family;
-   a credential-theft technique;
-   a controller exploit;
-   a target interest;
-   or access to infrastructure.

That does not establish that it used that capability in this incident.

Write:

> The method resembles activity previously associated with X.

where that is all the evidence supports.

Do not write:

> X carried out the attack.

unless the rest of the attribution supports that conclusion.

------------------------------------------------------------------------

## 🪞 Similarity Is Not A Common Operator

Several incidents may look similar because they share:

-   the same PLC;
-   the same VPN;
-   the same cloud provider;
-   the same identity platform;
-   the same managed-service provider;
-   the same OT integrator;
-   the same remote-access platform;
-   or the same vulnerability.

That may indicate:

``` text
one operator
```

or:

``` text
many actors exploiting one weakness
```

or:

``` text
shared supplier exposure
```

or:

``` text
copycat activity
```

A reporter should ask which explanation the evidence actually supports.

------------------------------------------------------------------------

## 🌐 Report Shared Dependencies

Where several institutions are affected, ask whether they share:

``` text
VENDOR:
CLOUD PROVIDER:
MSP:
IDENTITY PROVIDER:
OT INTEGRATOR:
REMOTE-ACCESS PLATFORM:
CONTRACTOR:
VULNERABILITY:
```

A shared provider may explain apparent clustering.

It may also reveal a campaign relationship hidden beneath apparently
unrelated victims.

Both possibilities deserve examination.

------------------------------------------------------------------------

## 🎨 Pattern Is Not Sponsor

The reporting language should allow a pattern to become strong before
the sponsor does.

Use the separate pattern scale:

``` text
⚪ ISOLATED
🟡 POSSIBLE RECURRENCE
🟠 CREDIBLE CLUSTER
🔴 ESTABLISHED CAMPAIGN PATTERN
```

This allows a report to say:

> A repeated water-sector campaign pattern is now established.

while also saying:

> Common sponsorship remains unresolved.

Pattern recognition should narrow the question.

It should not manufacture the answer.

------------------------------------------------------------------------

## 🧪 Separate Evidence From Inference

The report should distinguish:

``` text
EVIDENCE:
What is directly established.

INFERENCE:
What the evidence may suggest.

LIMIT:
What the evidence does not establish.

RIVAL EXPLANATION:
What else could account for the same observations.
```

Analysis is allowed.

Disguised inference is not.

------------------------------------------------------------------------

## 🧯 Rival Explanations Should Be Real

Do not include a rival explanation merely for appearances.

Use the strongest credible alternative.

That may include:

-   ordinary cybercrime;
-   another hostile state;
-   insider activity;
-   provider compromise;
-   opportunistic scanning;
-   shared-vulnerability exploitation;
-   copycat behaviour;
-   false flag;
-   technical failure;
-   or unrelated incidents.

------------------------------------------------------------------------

## ➖ Negative Findings Matter

Report important negative findings too.

Examples include:

-   no contamination identified;
-   no physical-process change observed;
-   no customer data found exposed;
-   no service interruption;
-   no lateral movement;
-   no shared infrastructure identified;
-   or a proposed attribution ruled out.

Negative findings help define the incident.

------------------------------------------------------------------------

## 📉 Severity Is Not Confidence

Where helpful, separate:

``` text
CONFIDENCE:
SEVERITY:
OPERATIONAL SIGNIFICANCE:
STRATEGIC SIGNIFICANCE:
```

A serious consequence does not make the attribution stronger.

A strong attribution does not make the incident more damaging.

------------------------------------------------------------------------

## 🧍 Report The Human Continuation

Institutional recovery may not end the incident for the people whose
information was exposed.

Because:

``` text
SYSTEM RESTORED
≠
DATA RECALLED

EXFILTRATION ENDED
≠
COPIES DESTROYED

SERVICE RECOVERED
≠
PERSON SAFE
```

The institution may be outside the technical incident.

The affected person may still be inside it.

------------------------------------------------------------------------

## 🪪 Report Integrity Separately From Theft

Report separately:

``` text
DATA CONFIDENTIALITY:
DATA INTEGRITY:
RECORD INTEGRITY:
PROVENANCE:
AUTHORITATIVE RECORD STATUS:
```

A system that remains online while its records can no longer be trusted
may have suffered a serious operational effect.

------------------------------------------------------------------------

## 🤐 Report Silence Precisely

Silence is not a denial.

NCND is not exoneration.

It is also not evidence that the concealed answer is yes.

Record exactly what was said and what remains unanswered.

------------------------------------------------------------------------

## 🔐 Government Attribution Is A Fact About Government Position

These are different propositions:

``` text
THE GOVERNMENT ATTRIBUTED THE INCIDENT TO IRAN
```

and:

``` text
IRAN DIRECTED THE INCIDENT
```

Report them separately.

------------------------------------------------------------------------

## 🔐 Public And Private Attribution Can Diverge

There may be a difference between:

``` text
WHAT THE STATE KNOWS
```

and:

``` text
WHAT THE STATE CAN PUBLICLY ESTABLISH
```

No public attribution does not prove that no internal assessment exists.

Possible internal assessment does not prove that the hidden assessment
is correct.

------------------------------------------------------------------------

## 🛡️ Protection Does Not Require Public Attribution

Protective action may reveal assessed risk.

It does not necessarily reveal the source of that risk.

Do not reverse-engineer a hidden attribution from protective action
alone.

------------------------------------------------------------------------

## 👾 Legal Language Needs Another Evidentiary Brake

Preserve:

``` text
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

Route substantive analysis to [👾 Cyber War
Crimes](./👾_cyber_war_crimes.md).

------------------------------------------------------------------------

## ⚖️ Public Legal Claims May Depend On Public Attribution

Preserve:

``` text
PRIVATE / INTERNAL ASSESSMENT
≠
PUBLICLY DEMONSTRABLE ATTRIBUTION

PUBLIC ATTRIBUTION
≠
LEGAL FINDING
```

------------------------------------------------------------------------

## 🧵 Ask Who Owns The Response

The useful question is:

> Who has accepted ownership of the continuing risk?

Do not allow every institution to disappear behind another institution's
remit.

------------------------------------------------------------------------

## 🧾 Suggested Incident Format

``` text
DATE:
COUNTRY:
SECTOR:
AFFECTED BODY:

WHAT HAPPENED:
SYSTEM LAYER:
DEPTH OF ACCESS:

OPERATIONAL EFFECT:
PHYSICAL EFFECT:
DATA EFFECT:
RECORD-INTEGRITY EFFECT:
CIVILIAN EFFECT:
MANUAL / FALLBACK RESPONSE:

CLAIM STATUS:
CLAIMED ACTOR:

TECHNICAL OPERATOR:
INTERMEDIARY / BROKER:
BUYER / CUSTOMER:
STATE AFFILIATION:
STATE DIRECTION:

PUBLIC GOVERNMENT ATTRIBUTION:

INCIDENT TRAFFIC LIGHT:
EFFECT TRAFFIC LIGHT:
ATTRIBUTION TRAFFIC LIGHT:
PATTERN STATUS:

IRAN-WAR RELEVANCE:
IRANIAN ATTRIBUTION:

SOURCE TIER:
SOURCE QUALITY:
ORIGINAL SOURCE:
INDEPENDENT CORROBORATION:
SOURCE PROVENANCE:

EVIDENCE:
INFERENCE:
LIMIT:
RIVAL EXPLANATIONS:

LEAD RESPONSE BODY:
PROTECTION PATHWAY:

LAST REVIEWED:
REVIEW TRIGGER:
CORRECTION STATUS:
```

------------------------------------------------------------------------

## 🔄 Corrections Are Part Of The Method

A responsible record should show:

-   what changed;
-   when it changed;
-   why it changed;
-   what evidence caused the change;
-   and whether the assessment was upgraded, downgraded, withdrawn, or
    excluded.

Correction demonstrates that the method can distinguish evidence from
attachment to a theory.

------------------------------------------------------------------------

## 🧭 Corrections Must Propagate

Where a material finding changes, update every place relying on the old
assessment.

That may include:

-   timeline entry;
-   campaign record;
-   prose analysis;
-   CSV;
-   XLSX;
-   attribution history;
-   pattern status;
-   legal-routing status;
-   and any reporting language based on the earlier finding.

------------------------------------------------------------------------

## 📰 Language Has To Preserve Evidentiary Distance

These terms should not be treated as synonyms.

### Reported

A source says something occurred.

### Claimed

An interested actor asserts something.

### Suspected

There is a credible but incomplete evidentiary basis.

### Assessed

A named institution or analyst has reached a judgement.

### Attributed

A source has assigned responsibility.

### Demonstrated

The available evidence independently establishes the proposition.

### Proved

Use sparingly and only where the relevant evidentiary standard genuinely
supports it.

------------------------------------------------------------------------

## 🏛️ Report The Attribution Source Type

The July--August 2026 US water campaign shows why **who holds the
assessment** must be reported alongside the confidence.

Use, where relevant:

``` text
ATTRIBUTION SOURCE TYPE:

FORMAL PUBLIC GOVERNMENT ATTRIBUTION
REPORTED GOVERNMENT ASSESSMENT
REPORTED INTELLIGENCE ASSESSMENT
REPORTED INVESTIGATIVE ASSESSMENT
STATE / FUSION-CENTRE ASSESSMENT
TECHNICAL RESEARCHER ASSESSMENT
AFFECTED-INSTITUTION ASSESSMENT
ACTOR CLAIM
POLITICAL STATEMENT
```

Then separately record:

``` text
PUBLIC / NON-PUBLIC STATUS:
FORMAL / REPORTED STATUS:
CONFIDENCE:
LIMIT:
```

This prevents several materially different sentences from collapsing
into one.

For example:

> US intelligence reportedly assesses Iranian responsibility as highly
> likely.

is not the same claim as:

> The United States has formally attributed the campaign to Iran.

And neither is the same as:

> President Trump said he did not think Iran was responsible.

All three can coexist in the same public record.

------------------------------------------------------------------------

## 🧭 Political Statements Must Keep Their Own Label

A president, minister, governor, or other political principal may make
an attribution statement.

Record it.

Do not silently convert it into an agency finding.

Use:

``` text
POLITICAL PUBLIC POSITION:
SOURCE:
DATE:
AGREES WITH INVESTIGATIVE ASSESSMENT:
YES / NO / UNCLEAR
```

Where a political statement conflicts with reported investigative or
intelligence assessments, the correct reporting move is not to choose
one and erase the other.

Preserve the disagreement.

For the US water cases, a durable formulation is:

> US and state officials were reported to assess Iranian responsibility
> as likely or highly likely, while no formal public federal attribution
> had been issued and President Trump publicly rejected the Iran
> explanation.

That sentence preserves the institutional conflict without pretending to
know why it exists.

------------------------------------------------------------------------

## 🏛️ No Formal Attribution Does Not Mean No Government Assessment

The phrase:

> no government attribution

can become misleading where credible reporting says government
investigators or intelligence agencies have reached an assessment but
the government has not formally published it.

Prefer:

``` text
NO FORMAL PUBLIC ATTRIBUTION
```

where that is what is actually meant.

Then record any credible reported assessment separately.

This distinction is especially important where the public record
contains:

``` text
reported high-confidence intelligence assessment
+
formal public silence
+
contrary political statement
```

The absence of a press release should not erase the reported assessment.

The reported assessment should not be promoted into a formal
attribution.

------------------------------------------------------------------------

## 🌊 Report Campaign Layers Separately

A wartime cyber environment can contain several overlapping waves.

For each incident or cluster, ask whether the evidence supports:

``` text
STATE-DIRECTED WAVE
STATE-AFFILIATED / PROXY WAVE
HACKTIVIST WAVE
CRIMINAL WAVE
COPYCAT WAVE
OPPORTUNISTIC EXPLOITATION
UNKNOWN / MIXED WAVE
```

Then ask whether a later wave is:

``` text
DOWNSTREAM OF EARLIER STATE ACTIVITY
```

or:

``` text
INDEPENDENT ACTIVITY IN THE SAME THREAT ENVIRONMENT
```

Do not infer either answer merely from chronology.

A war can increase ordinary cybercrime by creating:

-   exposed targets;
-   publicised vulnerabilities;
-   stolen access;
-   resale markets;
-   distracted defenders;
-   ideological cover;
-   and more actors looking at the same systems.

See [🌊 Riding Every Wave](./🌊_riding_every_wave.md).

## 🚫 Common Reporting Failures

Avoid:

-   treating actor claims as findings;
-   converting suspicion into certainty;
-   treating `📣 actor-claimed` as an attribution confidence level;
-   treating timing as causation;
-   treating target selection as attribution;
-   counting repeated articles as independent corroboration;
-   treating political branding as technical authorship;
-   treating a familiar alias as proof of operator continuity;
-   treating technical similarity as proof of one operator;
-   treating a common operator as proof of one customer;
-   treating a criminal operator as proof there is no later state
    customer;
-   treating a criminal operator as proof there is a state customer;
-   treating state affiliation as state direction;
-   using **proxy** without defining the evidenced relationship;
-   using **Iran-linked** without explaining the link;
-   treating a shared provider as proof of a shared attacker;
-   treating a recurring pattern as proof of one coordinated campaign;
-   treating pattern confidence as attribution confidence;
-   treating severity as confidence;
-   treating manual fallback as no harm;
-   applying one facility's deepest effect to an entire cluster;
-   treating NCND as denial;
-   treating silence as proof;
-   treating no public attribution as no strategic relevance;
-   treating protective action as proof of secret attribution;
-   treating technical recovery as the end of downstream human harm;
-   treating data theft and record manipulation as the same thing;
-   treating civilian infrastructure involvement as automatic proof of a
    war crime;
-   treating state responsibility as individual criminal responsibility;
-   omitting credible rival explanations;
-   omitting negative findings;
-   failing to preserve source disagreement;
-   and ending the story when the institution restores service.

------------------------------------------------------------------------

## 🧭 Working Rule

The working rule is:

> Preserve the chain from event to source to evidentiary layer to
> confidence to limit.

Then interpret.

Not before.

A useful newsroom process is:

``` text
establish the event
↓
establish the effect
↓
identify who says so
↓
find the original source
↓
check source quality
↓
identify independent corroboration
↓
separate claim from finding
↓
separate operator from customer
↓
separate attribution from relevance
↓
separate pattern from sponsor
↓
apply the traffic light to the proposition
↓
state the strongest rival explanation
↓
state the limit
↓
record negative findings
↓
say what remains unknown
↓
say what would change the assessment
↓
review
↓
correct when necessary
```

A good report should leave the reader knowing:

-   what happened;
-   what effect actually occurred;
-   who says so;
-   how strong each important proposition is;
-   what remains unknown;
-   why the incident matters;
-   whether it belongs to a wider pattern;
-   what the strongest competing explanation is;
-   and what evidence would change the current assessment.

That is how to report without overclaiming.

------------------------------------------------------------------------

## 🌌 Constellations

📰 🚦 🔗 🕸️ 🔄 --- reporting discipline; confidence; source chains;
layered attribution; correction.

## ✨ Stardust

cyber reporting, source provenance, traffic lights, attribution, actor
claims, pattern recognition, newsroom method, corrections, evidentiary
limits

------------------------------------------------------------------------

## 🏮 Footer

*📰 How To Report Without Overclaiming* is a living node of the
**Polaris Protocol**.\
It provides a newsroom and research method for reporting
essential-infrastructure cyber incidents without allowing headlines,
repetition, actor branding, incomplete attribution, criminal
intermediaries, or wartime urgency to outrun the evidence.

> 📡 Cross-references:
>
> -   [🇮🇷 Data Wars: IRGC Edition](./README.md) --- *root orientation,
>     analytical perimeter, and pack routing*
> -   [🔎 Confidence Labels And Source
>     Rules](./🔎_confidence_labels_and_source_rules.md) --- *traffic
>     lights, source quality, confidence, provenance, and evidentiary
>     limits*
> -   [🕸️ Attribution Is Not A Light
>     Switch](./🕸️_attribution_is_not_a_light_switch.md) --- *technical
>     attribution, state attribution, and unresolved sponsorship*
> -   [🧅 The Operator May Not Know The
>     Customer](./🧅_the_operator_may_not_know_the_customer.md) ---
>     *operators, brokers, customers, and layered tasking*
> -   [📉 Small Disruptions Can Make A
>     Campaign](./📉_small_disruptions_can_make_a_campaign.md) ---
>     *pattern recognition and cumulative operational effect*
> -   [🚰 When Cyber Reaches The
>     Machinery](./🚰_when_cyber_reaches_the_machinery.md) --- *OT
>     depth, manual fallback, and physical-process reporting*
> -   [🏥 Health, Education And Admin Are Not Soft
>     Extras](./🏥_health_education_and_admin_are_not_soft_extras.md)
>     --- *civilian systems, record integrity, and person-centred
>     recovery*
> -   [🇬🇧 Britain Is Advertising An Exploitable
>     Seam](./🇬🇧_britain_is_advertising_an_exploitable_seam.md) ---
>     *fragmented response, institutional ownership, and protection
>     pathways*
> -   [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) --- *separate
>     legal analysis for wartime cyber operations*
> -   [⏱️ Timeline Of Essential Infrastructure
>     Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) ---
>     *live chronology, confidence movement, and campaign status*

*Survivor authorship is sovereign. Containment is never neutral.*

*Last updated: 2026-08-14*
