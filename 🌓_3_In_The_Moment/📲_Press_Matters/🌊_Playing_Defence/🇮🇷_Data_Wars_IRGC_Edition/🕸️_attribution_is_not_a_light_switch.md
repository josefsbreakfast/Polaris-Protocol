# 🕸️ Attribution Is Not A Light Switch
**First created:** 2026-08-01 | **Last updated:** 2026-08-20  
*Cyber attribution is usually graded, delayed, contested, politically managed, and legally consequential in different ways at different thresholds.*

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
- and political judgement.

Those layers do not always arrive at the same time.

They do not always point in the same direction.

They are not always made public.

And they do not all answer the same question.

The public discussion may ask:

> Who hacked the system?

A government may be asking:

> Which intelligence service, proxy, criminal network, contractor, or access broker sits behind the operator?

A lawyer may need to ask:

> Can the operation be attributed to a state, connected to the armed conflict, or tied to an identifiable person with the required responsibility?

Those are related questions.

They are not interchangeable.

So the absence of a definitive public statement does not make an incident analytically empty.

It also does not permit the incident to be confidently assigned to Iran.

Both limits matter.

---

## 🎚️ Attribution Has Levels

This pack uses a graded model.

### Confirmed

A competent public authority, affected institution, or well-supported technical investigation has made a clear attribution and provided enough basis to understand the claim.

That may include:

- government attribution;
- court filings;
- sanctions documentation;
- indictments;
- coordinated cyber-agency advisories;
- or detailed technical reporting with strong evidentiary support.

Confirmed does not mean metaphysically certain.

It means the public record supports a high-confidence attribution.

### Probable

The evidence strongly points towards an Iranian state, IRGC-linked, intelligence-linked, or proxy actor, but no definitive public governmental attribution has been made.

This may rest on:

- known infrastructure;
- repeated tooling;
- operator overlap;
- target selection;
- campaign timing;
- or several independent technical assessments.

Probable should not be written as confirmed.

### Suspected

There are credible indicators, but the evidence remains incomplete or disputed.

This may include:

- early governmental suspicion;
- a leaked assessment;
- preliminary technical overlap;
- or a pattern consistent with known Iranian activity.

Suspected is a prompt for further investigation, not a verdict.

### Actor-claimed

A group has publicly claimed responsibility.

That tells us something about messaging.

It does not prove:

- that the group conducted the attack;
- that it acted alone;
- that it had state direction;
- that it understood the ultimate tasking;
- or that its description of the impact is accurate.

Actor claims belong in the record.

They do not control the record.

### Unattributed

No credible public attribution has yet been made.

An unattributed incident may still be strategically important because of:

- its timing;
- its sector;
- its operational effect;
- its similarity to other incidents;
- the layer of infrastructure reached;
- or its place inside a wider pattern.

Unattributed does not mean unrelated.

It also does not mean Iranian.

### Excluded

An incident should be excluded where:

- the claim is unsupported;
- the operational effect is negligible;
- the source chain collapses into one unreliable actor;
- the incident falls outside essential state infrastructure;
- or later evidence shows that it does not belong in the pack.

Exclusion is part of analytical discipline.

---

## 🎯 Confidence Belongs To A Proposition

An incident is not simply “confirmed” or “suspected.”

A particular proposition about it is.

These are different propositions:

```text
the intrusion occurred

the named persona had access

the named operator performed the intrusion

the operator belonged to a particular organisation

a commissioner requested the outcome

a customer purchased or received the access

the state benefited

the state directed or controlled the operation

the conduct is legally attributable to the state

an identified person bears criminal responsibility
```

Evidence may confirm one proposition while leaving the next unresolved.

For example:

```text
CONFIRMED:
a claimant published material obtainable only from the victim

PROBABLE:
the claimant had access to the compromised environment

OPEN:
whether the claimant obtained the first access

OPEN:
whether another customer commissioned or later acquired the result

NOT ESTABLISHED:
state direction or control
```

The confidence label must therefore attach to a written claim, role, time period, and incident.

If the proposition changes, the confidence assessment must be made again.

---

## 🪜 There Is More Than One Attribution Ladder

One reason cyber debates become confused is that several separate attribution problems are treated as if they were one.

A useful distinction is:

```text
technical attribution
→ who appears to have operated the intrusion?

organisational attribution
→ what group, contractor, criminal network, or proxy did they belong to?

state attribution
→ can the operation be attributed to a state as a matter of responsibility?

public governmental attribution
→ what is the state willing to say publicly?

individual criminal responsibility
→ which identifiable person can be shown to have committed, ordered, enabled, or otherwise borne responsibility for the conduct?
```

Those ladders can move at different speeds.

An incident may reach:

```text
high technical confidence
+
moderate organisational confidence
+
strong private intelligence confidence
+
weak public governmental attribution
+
no identified individual defendant
```

without contradiction.

That is not analytical failure.

It is a description of different evidentiary thresholds.

---

## 🧱 Different Evidence Does Different Work

Not all indicators prove the same thing.

### Technical Evidence

Technical indicators may show:

- shared command-and-control infrastructure;
- reused malware;
- matching code;
- similar persistence methods;
- recurring account patterns;
- familiar industrial-control targeting;
- or familiar operational security failures.

Technical similarity can support linkage.

It does not always prove common sponsorship.

Tools can be copied, leaked, bought, shared, deliberately imitated, or independently directed against the same weak technology.

### Behavioural Evidence

Target selection and operator behaviour may reveal:

- a consistent interest in dissidents;
- government administration;
- water systems;
- defence contractors;
- banking;
- healthcare;
- or regional political organisations.

Behavioural evidence helps establish campaign logic.

It is weaker as a stand-alone attribution method.

### Timing

An incident occurring immediately after military escalation may be relevant.

Timing can support a hypothesis.

Timing does not establish causation.

The world contains ordinary cybercrime even during war.

### Intelligence Evidence

Governments may hold intelligence that cannot be released publicly.

That can produce a high-confidence internal attribution with a sparse public explanation.

The underlying evidence might include things unavailable to outside researchers:

- intercepted communications;
- human intelligence;
- access to command infrastructure;
- partner intelligence;
- covert technical collection;
- financial relationships;
- recovered tasking;
- or knowledge of an ongoing counter-operation.

This can be operationally necessary.

It also creates an accountability problem where the affected public is asked to trust a conclusion it cannot inspect.

### Political Attribution

States decide not only **whether** to attribute but **when, how, and at what level**.

A technically strong case may remain unspoken.

A weaker case may be publicised because the political moment demands it.

Language can also be deliberately graded:

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

The underlying incident may not have changed.

The government's willingness to describe responsibility has.

---

## 🔗 Evidence Can Be Strong Without Being Independent

Several reports may all descend from one assessment, one leak, one advisory, or one actor statement.

That can widen distribution without adding corroboration.

The pack should distinguish:

```text
SOURCE QUALITY
→ how competent and well placed is the source?

EVIDENCE STRENGTH
→ how directly does the material support this proposition?

SOURCE INDEPENDENCE
→ does this source add a genuinely separate evidentiary route?

PUBLICATION STATUS
→ is the assessment formal, public, reported, leaked, private, or actor-claimed?
```

Five articles repeating one unnamed official do not create five official assessments.

Five articles repeating one Telegram claim do not create five responsibility claims.

An official advisory may be excellent evidence of a method or threat class while remaining silent about the operator of the incident under investigation.

The source register should therefore preserve the provenance chain, not merely the number of links.

---

## 🚰 The Water-Control Cases Show Why This Matters

The widening United States water-system campaign is a useful live example.

By late July and early August 2026, water and wastewater utilities across multiple states had reported intrusions affecting technology used to maintain and control physical water operations.

More than 30 Minnesota community water systems were targeted over 26--27 July, and the FBI subsequently said utilities in at least seven states had reported incidents, some of which degraded water operations.
Reporting by 4 August described affected systems across at least 12 states.

Investigators and officials have treated Iranian involvement as a serious possibility.

Reporting has described the recent activity as likely linked to Iranian hackers, while federal agencies have previously attributed campaigns against internet-exposed programmable logic controllers to IRGC-affiliated actors.

But those two statements are not identical.

The earlier advisory establishes that IRGC-affiliated actors have used this general target class and method.

It does not automatically attribute every later compromise of similar technology to the same actor.

The current analytical position can therefore look like:

```text
known Iranian-affiliated interest in PLCs
+
similar exposed control technology
+
wartime motive
+
geographically distributed water incidents
+
some operational degradation
=
serious Iranian attribution hypothesis

not

=
proved Iranian responsibility for every incident
```

That distinction is exactly why this pack preserves unattributed and suspected incidents rather than forcing them prematurely into a confirmed category.

---

## 🧬 Clustering Can Raise Significance Without Raising Attribution To Confirmed

A single incident may have several plausible explanations.

A cluster can change the analytical weight.

Useful clustering indicators include:

- repeated targeting of the same controller families;
- the same exposed protocols;
- similar credential manipulation;
- similar loss of control or monitoring;
- repeated forced manual fallback;
- geographically distributed targeting;
- incidents occurring in a narrow wartime window;
- the same sectors appearing in Iranian threat reporting;
- or cross-sector movement into water, energy, transport, or
    telecommunications.

Clustering can support:

```text
this deserves coordinated investigation
```

before it supports:

```text
this was one coordinated Iranian campaign
```

That is an important distinction.

Pattern recognition should increase scrutiny before it increases certainty.

---

## 🧅 The Chain May Be Layered

The operator carrying out the task may not know the ultimate customer.

The commissioner may not know the hands-on operator either.

A chain may look like:

```text
requirement generator
→ commissioner
→ payer or procurement route
→ intermediary
→ access broker
→ hands-on operator
→ end user or beneficiary
```

That structure complicates attribution because different layers can be true at once.

The immediate operator may be a criminal.

The access may be sold commercially.

The buyer may be an intelligence-linked intermediary.

The final use may serve a state objective.

The customer may enter before the breach, during it, or after access has already been obtained.

That timing changes the proposition:

```text
commissioning before access
→ may support prior tasking

purchase after compromise
→ supports later acquisition, not automatically original direction

payment for an outcome
→ may support a commercial relationship without proving operational control

repeated procurement
→ may show sustained demand without revealing every command
```

A public statement that says:

> This was criminal activity.

may therefore describe one layer accurately while missing the wider operational relationship.

The reverse is also possible.

A state may benefit from criminal activity it did not direct.

Benefit is not the same as control.

Payment is not automatically command.

Compartmentalisation is not automatically innocence.

For the full role model, see [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md).

---

## 🎭 Proxy, Hacktivist, Criminal, Or State

These labels are often treated as mutually exclusive.

They are not always.

A group may:

- act independently most of the time;
- take occasional direction;
- use patriotic branding;
- receive protection or tolerance;
- sell access to several customers;
- exaggerate links to a state;
- conduct activity that is later exploited by a state;
- or be used as a cut-out for one operation and not another.

The relevant questions are:

- Who generated the requirement?
- Who commissioned the outcome?
- Who selected the target?
- Who supplied the access?
- Who paid?
- What did the payment purchase?
- Did the commission precede or follow the compromise?
- Who provided the infrastructure?
- Who supplied the exploit or malware?
- Who controlled method, timing, and scope?
- Who benefited?
- Who received or used the result?
- Who chose whether to conceal or publicise it?
- Who amplified the claim?
- Who protected the operators?
- Who used the stolen material?
- Who supplied follow-on tasking?
- And was the relationship continuous, occasional, or merely opportunistic?

The label should follow the evidence.

It should not replace it.

---

## ⚖️ State Responsibility And War-Crime Responsibility Are Not The Same Attribution Problem

This distinction becomes especially important during armed conflict.

Suppose investigators establish that an Iranian-linked operator interfered with civilian water infrastructure.

That still leaves several separate questions:

```text
Did Iran direct or control the operation?

Can the conduct legally be attributed to Iran?

Was the target a protected civilian object?

Did the operation amount to an attack for the relevant IHL rule?

What effects were intended or reasonably expected?

Was there the required armed-conflict nexus?

Which individuals knew, ordered, performed, or facilitated the conduct?
```

A strong answer to one question does not automatically answer the others.

That means:

```text
Iran-linked
≠
Iranian state responsibility

Iranian state responsibility
≠
war crime

war crime
≠
identified individual offender
```

The legal analysis therefore has its own evidentiary ladder.

This is why the pack should not use **war crime** as shorthand for:

> cyberattack against civilians during wartime.

The term requires more.

For the deeper legal and public-attribution problem, see [👾 Cyber War Crimes](./👾_cyber_war_crimes.md).

---

## 🗣️ Public Attribution Creates Political Leverage

Public attribution is not legally necessary for conduct to have occurred.

It can nevertheless matter enormously for what governments can credibly say about it in public.

Imagine a government privately assesses with high confidence that a foreign state directed an operation against protected civilian infrastructure.

If it attributes publicly, it may gain the ability to say:

> this state attacked our civilian infrastructure during the armed conflict.

Depending on the facts, that can support diplomatic condemnation,
alliance coordination, sanctions, legal argument, criminal
investigation, or public claims under international humanitarian law.

But making the attribution may require revealing:

- intelligence sources;
- technical collection;
- allied reporting;
- covert access;
- operational knowledge;
- or the level of confidence actually held internally.

If the government does not attribute publicly, it may retain those
capabilities but lose some of the political and legal leverage that
public attribution would create.

The resulting bind can look like:

```text
strong private attribution
+
limited public disclosure
=
strong internal threat assessment
+
weak public evidentiary foundation
```

That does not alter the underlying law.

It alters what can be demonstrated and politically used in public.

---

## 🤐 Silence Has More Than One Meaning

A state may have good reasons not to disclose an attribution
immediately.

It may be protecting:

- an investigation;
- an intelligence source;
- a technical capability;
- an allied capability;
- an ongoing counter-operation;
- criminal proceedings;
- or diplomatic space.

But public silence is analytically ambiguous.

It can mean:

```text
we know substantially more than we can say
```

It can also mean:

```text
we genuinely have not established who did this
```

From outside government, those situations may look almost identical.

That means analysts must not convert silence into hidden certainty.

A statement such as:

> The government has not publicly attributed the incident.

is evidence.

A statement such as:

> The government secretly knows Iran did it.

requires additional evidence.

The distinction is essential.

---

## 🤐 Non-Confirmation Can Also Become Part Of The Vulnerability

A blanket posture of:

> We can neither confirm nor deny.\
> We are not discussing the incident.\
> We do not comment on operational matters.

may protect some investigations.

Used too broadly, it may tell an adversary that:

- responsibility is fragmented;
- affected people may be left without a protection pathway;
- institutions cannot coordinate visibly;
- the state cannot explain what category of threat exists;
- and further exploitation may occur before any public body accepts
    ownership.

That matters especially where the data concerns an individual.

The old organisational ransomware model is:

```text
do not pay
contain the breach
restore from backups
notify regulators
resume operations
```

That does not map cleanly onto a person whose identity, health records,
intimate material, political history, or safeguarding information may
now circulate beyond recall.

A company can rebuild a server.

A person cannot restore a previous identity.

The state may still need to keep attribution confidential.

It does not follow that it should provide the affected person with
nothing.

At minimum, the response should distinguish:

- what can be disclosed publicly;
- what can be disclosed privately;
- what risk category applies;
- who owns the protective response;
- and what practical measures follow.

Silence is not always neutral.

Sometimes it protects an operation.

Sometimes it advertises the vulnerability.

---

## 📰 Why Headlines Flatten The Problem

Headlines prefer clean statements.

Cyber attribution rarely offers them.

This creates two recurring errors.

The first is overclaiming:

> Iran attacks British education system.

when the public evidence only shows:

- an education-sector breach;
- during the Iran war;
- claimed by a criminal group;
- with no proven Iranian link.

The second is underclaiming:

> No evidence of Iranian involvement.

when the real position may be:

- no definitive public attribution;
- credible technical concern;
- known Iranian interest in the same target class;
- unresolved state involvement;
- and a wider pattern worth monitoring.

The better wording is often less dramatic and more useful.

For example:

> The breach remains publicly unattributed. It is included because it
> affected essential state infrastructure during the war period,
> resembles activity already under investigation, and attribution
> remains open.

That preserves both the evidence and the uncertainty.

---

## 📊 The Confidence Label Must Travel With The Claim

Every incident in this pack should preserve:

```text
INCIDENT / EVENT:
CLAIM:
ATTRIBUTED OBJECT OR ROLE:
RELEVANT TIME PERIOD:
SOURCE:
PROVENANCE CHAIN:
SOURCE INDEPENDENCE:
ATTRIBUTION TYPE:
CONFIDENCE:
PUBLIC / PRIVATE STATUS:
FORMAL / INFORMAL STATUS:
ALTERNATIVE EXPLANATIONS:
LIMIT:
SUPERSEDES / SUPERSEDED BY:
```

For example:

```text
CLAIM:
Iran-linked actors may have targeted the system.

ATTRIBUTED OBJECT OR ROLE:
Suspected operator or sponsor relationship; commissioner unresolved.

SOURCE:
Preliminary state assessment and technical reporting.

PROVENANCE CHAIN:
Reported assessment plus observable technical context.

SOURCE INDEPENDENCE:
Partly unresolved; multiple reports may descend from the same assessment.

ATTRIBUTION TYPE:
Suspected operator / sponsor linkage.

CONFIDENCE:
Moderate.

PUBLIC / PRIVATE STATUS:
Publicly reported suspicion; no definitive state attribution.

FORMAL / INFORMAL STATUS:
Reported investigative assessment, not formal public attribution.

ALTERNATIVE EXPLANATIONS:
Criminal, copycat, access-broker, or mixed-ecosystem activity.

LIMIT:
Alternative criminal or copycat explanations remain open.
```

The confidence label should not disappear when the claim is repeated
elsewhere.

A suspected attribution does not become confirmed because ten newspapers
copied the same source.

Repetition is not corroboration.

---

## 🧪 What Would Increase Confidence

Confidence should rise where new evidence shows:

- matching infrastructure across several incidents;
- operator overlap with previously attributed campaigns;
- financial or communications links;
- payment timing tied to a target, access, dataset, effect, or publication decision;
- procurement records linking a requirement to a commissioner or intermediary;
- official findings;
- recovered tasking;
- technical artefacts difficult to imitate;
- consistent victimology;
- common control infrastructure;
- law-enforcement seizure of operator infrastructure;
- or independent corroboration from several competent sources.

The evidence must still be matched to the proposition it proves.

Financial evidence may establish demand, relationship, timing, or acquisition.

It does not automatically establish operational control, knowledge of method, or responsibility for every downstream act.

Confidence should fall where:

- the source withdraws the claim;
- technical indicators are shown to be generic;
- the alleged actor exaggerates impact;
- the incident is traced to ordinary criminal activity;
- timestamps or infrastructure do not match;
- several unrelated operators are found exploiting the same
    vulnerability;
- or rival explanations fit better.

The timeline should be able to move in both directions.

---

## 🔁 Attribution Changes Are Events

The timeline should not record only changes in operational impact.

Changes in attribution are themselves substantive developments.

For example:

```text
UNATTRIBUTED
↓
SUSPECTED IRAN-LINKED
↓
IRANIAN-AFFILIATED
↓
IRGC-AFFILIATED
↓
STATE-DIRECTED
```

Each step can change:

- diplomatic consequences;
- legal significance;
- defensive priorities;
- media language;
- alliance response;
- sanctions exposure;
- and the interpretation of earlier incidents.

A later attribution can therefore change the meaning of an older event.

The timeline should preserve that history rather than silently
overwriting it.

---

## 🧭 Attribution Confidence And Attribution Publication Are Different Axes

The July--August 2026 US water cases require a further distinction.

It is no longer enough to ask only:

```text
HOW CONFIDENT IS THE ATTRIBUTION?
```

The pack must also ask:

```text
WHO HOLDS THE ASSESSMENT?
+
WHAT KIND OF ASSESSMENT IS IT?
+
IS IT PUBLIC?
+
IS IT FORMAL?
+
IS THE PUBLIC POSITION THE SAME AS THE INVESTIGATIVE POSITION?
```

A useful matrix is:

```text
TECHNICAL INFERENCE
→ researcher or vendor judgement from observable technical evidence

REPORTED INVESTIGATIVE ASSESSMENT
→ journalists report what investigators / officials currently believe

REPORTED INTELLIGENCE ASSESSMENT
→ journalists report an intelligence-community judgement not formally published

INTERAGENCY / SECTOR WARNING
→ government warns defenders about a threat or method without necessarily attributing the incident under investigation

FORMAL PUBLIC ATTRIBUTION
→ a competent authority publicly assigns responsibility

POLITICAL STATEMENT
→ a political principal states a view; this may agree or disagree with the investigative record

ACTOR CLAIM
→ an actor claims responsibility or association
```

These are not stages on one ladder.

A reported intelligence assessment can be stronger than a public
political statement while still being less publicly demonstrable than a
formal agency attribution.

Therefore:

```text
HIGH INTERNAL CONFIDENCE
≠
FORMAL PUBLIC ATTRIBUTION

NO FORMAL PUBLIC ATTRIBUTION
≠
LOW INTERNAL CONFIDENCE

PRESIDENTIAL STATEMENT
≠
INTERAGENCY TECHNICAL FINDING
```

The source and publication status must travel with the proposition.

---

## 🚰 July--August 2026: The Water Case Became A Governance Problem

The Minnesota and wider US water campaign now provides a concrete
example.

Public reporting on 30 July described US and state investigators as
believing Iranian hackers were probably responsible for the Minnesota
attacks, while cautioning that the assessment was preliminary and could
change.

A WaterISAC communication reported by WIRED, drawing on Minnesota Fusion
Center information, separately linked the Minnesota activity to
Iranian-affiliated hacking activity.

Subsequent reporting described US intelligence agencies as holding a
substantially stronger Iran assessment than the public federal
attribution record suggested.

At the same time, President Trump publicly said that he did not think
Iran was responsible.

The resulting record therefore cannot be represented accurately as
either:

```text
AMERICA ATTRIBUTED THE ATTACK TO IRAN
```

or:

```text
AMERICA DOES NOT THINK IRAN DID IT
```

The more precise representation is:

```text
REPORTED INVESTIGATIVE / INTELLIGENCE ASSESSMENT:
Iranian responsibility strongly favoured / reportedly assessed at high confidence

FORMAL PUBLIC FBI / CISA / NSA / EPA ATTRIBUTION:
not established in the public record reviewed through 19 August

PRESIDENTIAL PUBLIC POSITION:
President Trump said he did not think Iran was responsible

STATE / SECTOR INFORMATION:
Minnesota Fusion Center-linked information, relayed through WaterISAC reporting, tied the activity to Iranian-affiliated actors

TECHNICAL / HISTORICAL CONTEXT:
federal agencies had already documented IRGC-affiliated exploitation of exposed PLCs in US critical infrastructure

CURRENT ANALYTICAL RESULT:
materially strengthened Iran-linked assessment, with a persistent public-attribution gap
```

This is not merely an attribution problem.

It is an **attribution-governance problem**.

The evidentiary assessment and the politically publishable assessment
may diverge.

That divergence is itself a fact worth recording.

---

## 📣 12--15 August 2026: A Known Ecosystem Made A New Claim

The public attribution record then changed again.

On 12 August, a Telegram account using the name **APT IRAN** reportedly
said that the Minnesota operation had been conducted jointly with
**CyberAv3ngers** and that the two actors took direct responsibility for
it.

Threat Beat, a project of Auburn University's McCrary Institute for
Cyber and Critical Infrastructure Security, reported the statement.
KSTP then reported the claim and sought comment from Minnesota IT
Services, the FBI, and CISA.

Minnesota IT Services and the FBI said they were aware of the posts but
did not validate them publicly. Minnesota's investigation remained
open. CISA had not responded by the time of the KSTP report.

The claim matters because CyberAv3ngers is not an unknown name invented
after the Minnesota incident.

US government reporting has previously described CyberAv3ngers as
affiliated with the IRGC Cyber-Electronic Command and associated it with
exploitation of programmable logic controllers used in US water and
other critical-infrastructure systems.

That prior relationship changes the weight of the new claim.

It does not change the kind of evidence the claim is.

The correct separation is:

```text
EXISTENCE OF THE RESPONSIBILITY CLAIM:
🟢 ESTABLISHED

PRIOR CYBERAV3NGERS--IRGC RELATIONSHIP:
🟢 ESTABLISHED in prior US government attribution

CURRENT MINNESOTA OPERATION CONDUCTED BY THE CLAIMANTS:
🟡 PROBABLE / materially strengthened, still requiring forensic corroboration

CURRENT MINNESOTA OPERATION DIRECTED BY THE IRGC:
not independently established by the claim

FORMAL PUBLIC FBI / CISA / NSA / EPA ATTRIBUTION
OF THE JULY--AUGUST CAMPAIGN:
still not identified in the reviewed public record
```

This is stronger than an unsupported claim by a newly created persona.

It is weaker than:

- agency validation of the claimant's access;
- technical evidence connecting the claimant to the intrusion;
- recovered tasking;
- infrastructure or operator evidence tying the operation to the
    previously attributed CyberAv3ngers activity;
- or a formal public attribution of the current campaign.

A known relationship cannot be inherited across time without evidence
of current operational continuity.

Likewise:

```text
KNOWN IRGC-AFFILIATED ACTOR
+
NEW RESPONSIBILITY CLAIM
≠
AUTOMATICALLY PROVED IRGC-DIRECTED OPERATION
```

But the reverse mistake also has to be avoided.

The claim cannot be treated as if it came from an actor with no
documented history, no relevant target interest, and no prior US
government attribution.

The evidentiary movement is therefore real but bounded:

```text
reported investigative / intelligence assessment
+
relevant technical and historical context
+
claim from an actor ecosystem with an established IRGC relationship
↓
Iran-linked assessment strengthened

while

formal public attribution
+
forensic validation of the claim
+
current state-direction finding
remain absent or not public
```

That is what an attribution update looks like when the new evidence is
meaningful but not dispositive.

---

## 🛡️ 19 August 2026: The Threat Warning Strengthened Without Naming The Water Operator

On 19 August, Reuters reported a new joint U.S. government advisory from the NSA, CISA, FBI, Department of Energy, and Environmental Protection Agency concerning an active threat to Siemens S7 Series programmable logic controllers.

The advisory describes reconnaissance and capability development against U.S.-based PLC installations, including systems in water, energy, manufacturing, chemical, food and agriculture, and commercial facilities. It warns that exploitation could lead to disruption, safety incidents, downtime, equipment damage, data compromise, and cascading effects.
[NSA, CISA, FBI, DOE and EPA — *Defending Against an Active Threat to Siemens S7 Series PLCs*](https://media.defense.gov/2026/Aug/18/2003983494/-1/-1/1/CSA_ACTIVE_THREAT_TO_SIEMENS_S7_SERIES_PLCS.PDF)

The advisory materially strengthens the public evidence for:

```text
ACTIVE PLC THREAT:
confirmed by a joint federal advisory

TARGET CLASS:
critical infrastructure, including water and wastewater

CAPABILITY DEVELOPMENT:
assessed as preparation for possible future operational effects

CURRENT WATER-WAVE OPERATOR:
not named in the advisory

FORMAL IRAN ATTRIBUTION FOR THE RECENT LOCAL WATER INCIDENTS:
still not made publicly as of 19 August
```

Reuters explicitly reported that federal officials had stopped short of formally linking Iran to the recent local water attacks.
[Reuters — *US warns Siemens devices can be hacked amid fears Iran is breaching water plants*](https://www.reuters.com/world/us-warns-siemens-devices-can-be-hacked-amid-fears-iran-is-breaching-water-plants-2026-08-19/)

This is a useful demonstration of proposition-level attribution.

The government can confirm an active threat, describe the target class, identify techniques, assess likely capability development, and warn of potential effects without publicly naming the operator of the incident cluster.

The threat assessment moved.

The formal incident attribution did not.

---

## 🏛️ Attribution Can Become A Governance Output

Public attribution is produced by institutions.

That means the public label may depend on more than evidentiary
confidence.

Possible constraints include:

- source protection;
- an active investigation;
- intelligence equities;
- allied sensitivities;
- diplomatic negotiations;
- escalation management;
- legal thresholds;
- interagency disagreement;
- and political leadership.

Analysts should therefore avoid treating the final public label as a
pure measurement of technical certainty.

The public output may be:

```text
EVIDENCE
+
INSTITUTIONAL PROCESS
+
DISCLOSURE RULES
+
POLITICAL AUTHORITY
+
STRATEGIC COST
=
PUBLIC ATTRIBUTION
```

That does **not** mean political disagreement proves suppression.

It means that attribution publication is a governance act as well as an
evidentiary act.

Where credible reporting identifies a gap, record the gap rather than
guessing why it exists.

---

## 🌊 Attribution Must Follow The Wave, Not Flood The Whole Campaign

A strengthened Iran assessment for an initial or central wave must not
automatically migrate to every later intrusion in the same sector.

War can generate:

```text
state-directed activity
→ publicity
→ exposed technique / target awareness
→ copycats
→ criminal exploitation
→ access resale
→ hacktivist participation
→ unrelated opportunistic attacks
```

Later criminal activity may be downstream of a state campaign.

It may also be independent activity taking advantage of the same exposed
systems and heightened attention.

Therefore:

```text
STATE-LINKED FIRST WAVE
≠
EVERY LATER WAVE IS STATE-DIRECTED

LATER CRIMINAL WAVE
≠
EARLIER STATE ATTRIBUTION WAS WRONG
```

See [🌊 Riding Every Wave](./🌊_riding_every_wave.md) for the
campaign-layer model.

## 🚫 What Attribution Cannot Do Alone

Attribution does not answer every strategic question.

Even a confirmed Iranian operation does not automatically establish:

- strategic importance;
- central state direction;
- effectiveness;
- operational success;
- a coherent campaign;
- an international humanitarian law violation;
- or individual criminal responsibility.

Likewise, an unattributed incident may still expose:

- weak infrastructure;
- fragmented governance;
- poor victim protection;
- a repeated target set;
- physical-system vulnerability;
- or a seam that several hostile actors can exploit.

Attribution is one part of the analysis.

It is not the whole analysis.

---

## 🧾 Sources For The Live Water Attribution Record

The following sources perform different evidentiary functions. They
should not be counted as interchangeable votes for one conclusion.

### Primary And Government Sources

- [NSA, CISA, FBI, DOE and EPA: active threat to Siemens S7 Series PLCs](https://media.defense.gov/2026/Aug/18/2003983494/-1/-1/1/CSA_ACTIVE_THREAT_TO_SIEMENS_S7_SERIES_PLCS.PDF)
    — 19 August joint warning describing an active PLC threat, capability development, and possible operational effects; it does not name the operator of the recent water incidents.
- [CISA and partners: IRGC-affiliated cyber actors exploiting PLCs in
    multiple sectors](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)
    — prior US government attribution of the CyberAv3ngers-associated
    PLC activity; evidence of the historic actor relationship, not
    proof of the 2026 Minnesota operation.
- [CISA: Iranian-affiliated cyber actors exploit programmable logic
    controllers](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)
    — current technical and threat context for Iranian-affiliated OT
    exploitation.
- [FBI: malicious cyber actors targeting water and wastewater-sector
    internet-facing PLCs](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)
    — public operational warning and effect record; it does not name
    Iran as the operator of the current wave.

### Responsibility Claim And Local Investigative Reporting

- [KSTP: Iran-linked group claims responsibility for the Minnesota
    water-system attack](https://kstp.com/kstp-news/top-news/hacking-group-linked-to-iran-claims-responsibility-for-cyberattack-on-minnesota-water-systems-report-says/)
    — reports the Threat Beat account of the Telegram claim and records
    that Minnesota IT Services and the FBI were aware of the posts but
    declined to validate them publicly.
- [Auburn University McCrary Institute: Cyber Briefing, 12 August
    2026](https://www.linkedin.com/pulse/cyber-briefing-81226-au-mccrary-institute-7cfre)
    — specialist monitoring route through which the actor statement
    entered the wider public record.

### National Reporting On The Attribution Dispute

- [Reuters: US warns Siemens devices can be hacked amid fears Iran is breaching water plants](https://www.reuters.com/world/us-warns-siemens-devices-can-be-hacked-amid-fears-iran-is-breaching-water-plants-2026-08-19/)
    — records the new joint advisory and that federal officials still had not formally linked Iran to the recent local water attacks as of 19 August.
- [Reuters: Trump says Iran was not to blame for the Minnesota
    cyberattack](https://www.reuters.com/world/us/trump-says-iran-not-blame-minnesota-cyber-attack-2026-07-31/)
    — records the presidential position and the absence of a formal
    FBI attribution at that stage.
- [Washington Post: US intelligence agencies suspect Iran launched
    the Minnesota water attacks](https://www.washingtonpost.com/national-security/2026/07/30/us-spy-agencies-suspect-iran-launched-cyberattack-minnesota-water-facilities/)
    — reporting on the intelligence assessment; this is not itself a
    published agency attribution document.

The provenance chain for the new claim is therefore:

```text
Telegram actor statement
→ specialist monitoring report
→ local news report
→ agencies asked to validate
→ agencies acknowledge awareness but do not validate publicly
```

Repetition of that chain by further outlets would not create additional
independent corroboration.

---

## 🧭 Working Rule

The pack should use this rule:

> Do not attribute beyond the evidence. Do not treat unresolved
> attribution as a reason to stop looking at operational effect, target
> selection, clustering, physical-system access, or institutional
> weakness.

And where legal significance may arise:

> Keep technical attribution, public governmental attribution, state
> responsibility, and individual criminal responsibility separate until
> the evidence justifies joining them.

For every confidence label, write the proposition it belongs to:

> Attribute a role, relationship, action, or responsibility claim—not an entire incident by implication.

Do not allow confidence in the operator to migrate automatically to the commissioner, customer, state link, state direction, or legal conclusion.

That means holding two disciplines at once:

```text
avoid false certainty
+
avoid false emptiness
```

The first protects accuracy.

The second protects situational awareness.

---

## 🌌 Constellations

🇮🇷 🕸️ 🧅 🔎 🤐 🚰 ⚖️ — Iran war analysis; proposition-level attribution; graded confidence; layered operators and commissioners; source independence; institutional silence; control systems; legal responsibility.

---

## ✨ Stardust

iran, irgc, cyber attribution, proposition-level attribution, confidence levels, source independence, provenance chain, proxy actors, hacktivists, criminal overlap, commissioner, customer, procurement, ncnd, intelligence, operational security, state responsibility, public attribution, individual criminal responsibility, water infrastructure, operational technology

---

## 🏮 Footer

*🕸️ Attribution Is Not A Light Switch* is a living node of the **Polaris Protocol**.
It defines how this pack attaches confidence to specific claims while separating technical operation, organisational relationship, commissioning, public governmental attribution, state responsibility, and individual responsibility.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope and inclusion rules*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *operational technology, control systems, and physical effect*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *separate legal analysis for wartime cyber operations*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *layered tasking and deniable labour*
> - [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md) — *claim, source, confidence, and limit*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *newsroom discipline under uncertainty*
> - [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *provenance chains, source function, and claim-level evidence logging*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *live incident chronology*
>
> 🏮 Return To:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *1up*
> - [🌊 Playing Defence](../README.md) — *2up*
> - [📲_Press Matters](../../README.md) — *3up*
> - [🌓 In The Moment](../../../README.md) — *4up*
> - [🌌 Polaris Protocol — Root](../../../../README.md) — *root*  

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-20_
