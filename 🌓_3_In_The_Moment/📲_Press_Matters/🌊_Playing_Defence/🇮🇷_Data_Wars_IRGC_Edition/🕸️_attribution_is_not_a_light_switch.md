# 🕸️ Attribution Is Not A Light Switch

**First created:** 2026-08-01 \| **Last updated:** 2026-08-14\
*Cyber attribution is usually graded, delayed, contested, politically
managed, and legally consequential in different ways at different
thresholds.*

------------------------------------------------------------------------

## 🛰️ Orientation

Public discussion often treats attribution as binary:

``` text
Iran did it
Iran did not do it
```

That is not how most cyber attribution works.

The more accurate picture is a ladder of confidence built from different
kinds of evidence:

-   technical indicators;
-   infrastructure reuse;
-   malware families;
-   operator behaviour;
-   target selection;
-   timing;
-   intelligence reporting;
-   actor claims;
-   law-enforcement findings;
-   private-sector analysis;
-   recovered tasking;
-   and political judgement.

Those layers do not always arrive at the same time.

They do not always point in the same direction.

They are not always made public.

And they do not all answer the same question.

The public discussion may ask:

> Who hacked the system?

A government may be asking:

> Which intelligence service, proxy, criminal network, contractor, or
> access broker sits behind the operator?

A lawyer may need to ask:

> Can the operation be attributed to a state, connected to the armed
> conflict, or tied to an identifiable person with the required
> responsibility?

Those are related questions.

They are not interchangeable.

So the absence of a definitive public statement does not make an
incident analytically empty.

It also does not permit the incident to be confidently assigned to Iran.

Both limits matter.

------------------------------------------------------------------------

## 🎚️ Attribution Has Levels

This pack uses a graded model.

### Confirmed

A competent public authority, affected institution, or well-supported
technical investigation has made a clear attribution and provided enough
basis to understand the claim.

That may include:

-   government attribution;
-   court filings;
-   sanctions documentation;
-   indictments;
-   coordinated cyber-agency advisories;
-   or detailed technical reporting with strong evidentiary support.

Confirmed does not mean metaphysically certain.

It means the public record supports a high-confidence attribution.

### Probable

The evidence strongly points towards an Iranian state, IRGC-linked,
intelligence-linked, or proxy actor, but no definitive public
governmental attribution has been made.

This may rest on:

-   known infrastructure;
-   repeated tooling;
-   operator overlap;
-   target selection;
-   campaign timing;
-   or several independent technical assessments.

Probable should not be written as confirmed.

### Suspected

There are credible indicators, but the evidence remains incomplete or
disputed.

This may include:

-   early governmental suspicion;
-   a leaked assessment;
-   preliminary technical overlap;
-   or a pattern consistent with known Iranian activity.

Suspected is a prompt for further investigation, not a verdict.

### Actor-claimed

A group has publicly claimed responsibility.

That tells us something about messaging.

It does not prove:

-   that the group conducted the attack;
-   that it acted alone;
-   that it had state direction;
-   that it understood the ultimate tasking;
-   or that its description of the impact is accurate.

Actor claims belong in the record.

They do not control the record.

### Unattributed

No credible public attribution has yet been made.

An unattributed incident may still be strategically important because
of:

-   its timing;
-   its sector;
-   its operational effect;
-   its similarity to other incidents;
-   the layer of infrastructure reached;
-   or its place inside a wider pattern.

Unattributed does not mean unrelated.

It also does not mean Iranian.

### Excluded

An incident should be excluded where:

-   the claim is unsupported;
-   the operational effect is negligible;
-   the source chain collapses into one unreliable actor;
-   the incident falls outside essential state infrastructure;
-   or later evidence shows that it does not belong in the pack.

Exclusion is part of analytical discipline.

------------------------------------------------------------------------

## 🪜 There Is More Than One Attribution Ladder

One reason cyber debates become confused is that several separate
attribution problems are treated as if they were one.

A useful distinction is:

``` text
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

``` text
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

------------------------------------------------------------------------

## 🧱 Different Evidence Does Different Work

Not all indicators prove the same thing.

### Technical Evidence

Technical indicators may show:

-   shared command-and-control infrastructure;
-   reused malware;
-   matching code;
-   similar persistence methods;
-   recurring account patterns;
-   familiar industrial-control targeting;
-   or familiar operational security failures.

Technical similarity can support linkage.

It does not always prove common sponsorship.

Tools can be copied, leaked, bought, shared, deliberately imitated, or
independently directed against the same weak technology.

### Behavioural Evidence

Target selection and operator behaviour may reveal:

-   a consistent interest in dissidents;
-   government administration;
-   water systems;
-   defence contractors;
-   banking;
-   healthcare;
-   or regional political organisations.

Behavioural evidence helps establish campaign logic.

It is weaker as a stand-alone attribution method.

### Timing

An incident occurring immediately after military escalation may be
relevant.

Timing can support a hypothesis.

Timing does not establish causation.

The world contains ordinary cybercrime even during war.

### Intelligence Evidence

Governments may hold intelligence that cannot be released publicly.

That can produce a high-confidence internal attribution with a sparse
public explanation.

The underlying evidence might include things unavailable to outside
researchers:

-   intercepted communications;
-   human intelligence;
-   access to command infrastructure;
-   partner intelligence;
-   covert technical collection;
-   financial relationships;
-   recovered tasking;
-   or knowledge of an ongoing counter-operation.

This can be operationally necessary.

It also creates an accountability problem where the affected public is
asked to trust a conclusion it cannot inspect.

### Political Attribution

States decide not only **whether** to attribute but **when, how, and at
what level**.

A technically strong case may remain unspoken.

A weaker case may be publicised because the political moment demands it.

Language can also be deliberately graded:

``` text
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

------------------------------------------------------------------------

## 🚰 The Water-Control Cases Show Why This Matters

The widening United States water-system campaign is a useful live
example.

By late July and early August 2026, water and wastewater utilities
across multiple states had reported intrusions affecting technology used
to maintain and control physical water operations.

More than 30 Minnesota community water systems were targeted over 26--27
July, and the FBI subsequently said utilities in at least seven states
had reported incidents, some of which degraded water operations.
Reporting by 4 August described affected systems across at least 12
states.

Investigators and officials have treated Iranian involvement as a
serious possibility.

Reporting has described the recent activity as likely linked to Iranian
hackers, while federal agencies have previously attributed campaigns
against internet-exposed programmable logic controllers to
IRGC-affiliated actors.

But those two statements are not identical.

The earlier advisory establishes that IRGC-affiliated actors have used
this general target class and method.

It does not automatically attribute every later compromise of similar
technology to the same actor.

The current analytical position can therefore look like:

``` text
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

That distinction is exactly why this pack preserves unattributed and
suspected incidents rather than forcing them prematurely into a
confirmed category.

------------------------------------------------------------------------

## 🧬 Clustering Can Raise Significance Without Raising Attribution To Confirmed

A single incident may have several plausible explanations.

A cluster can change the analytical weight.

Useful clustering indicators include:

-   repeated targeting of the same controller families;
-   the same exposed protocols;
-   similar credential manipulation;
-   similar loss of control or monitoring;
-   repeated forced manual fallback;
-   geographically distributed targeting;
-   incidents occurring in a narrow wartime window;
-   the same sectors appearing in Iranian threat reporting;
-   or cross-sector movement into water, energy, transport, or
    telecommunications.

Clustering can support:

``` text
this deserves coordinated investigation
```

before it supports:

``` text
this was one coordinated Iranian campaign
```

That is an important distinction.

Pattern recognition should increase scrutiny before it increases
certainty.

------------------------------------------------------------------------

## 🧅 The Chain May Be Layered

The operator carrying out the task may not know the ultimate customer.

A chain may look like:

``` text
recruit
→ small task
→ criminal intermediary
→ access broker
→ contractor or proxy
→ state customer
```

That structure complicates attribution because different layers can be
true at once.

The immediate operator may be a criminal.

The access may be sold commercially.

The buyer may be an intelligence-linked intermediary.

The final use may serve a state objective.

A public statement that says:

> This was criminal activity.

may therefore describe one layer accurately while missing the wider
operational relationship.

The reverse is also possible.

A state may benefit from criminal activity it did not direct.

Benefit is not the same as control.

------------------------------------------------------------------------

## 🎭 Proxy, Hacktivist, Criminal, Or State

These labels are often treated as mutually exclusive.

They are not always.

A group may:

-   act independently most of the time;
-   take occasional direction;
-   use patriotic branding;
-   receive protection or tolerance;
-   sell access to several customers;
-   exaggerate links to a state;
-   conduct activity that is later exploited by a state;
-   or be used as a cut-out for one operation and not another.

The relevant questions are:

-   Who selected the target?
-   Who supplied the access?
-   Who paid?
-   Who provided the infrastructure?
-   Who supplied the exploit or malware?
-   Who benefited?
-   Who amplified the claim?
-   Who protected the operators?
-   Who used the stolen material?
-   Who supplied follow-on tasking?
-   And was the relationship continuous, occasional, or merely
    opportunistic?

The label should follow the evidence.

It should not replace it.

------------------------------------------------------------------------

## ⚖️ State Responsibility And War-Crime Responsibility Are Not The Same Attribution Problem

This distinction becomes especially important during armed conflict.

Suppose investigators establish that an Iranian-linked operator
interfered with civilian water infrastructure.

That still leaves several separate questions:

``` text
Did Iran direct or control the operation?

Can the conduct legally be attributed to Iran?

Was the target a protected civilian object?

Did the operation amount to an attack for the relevant IHL rule?

What effects were intended or reasonably expected?

Was there the required armed-conflict nexus?

Which individuals knew, ordered, performed, or facilitated the conduct?
```

A strong answer to one question does not automatically answer the
others.

That means:

``` text
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

For the deeper legal and public-attribution problem, see:

[⚖️ When Attribution Controls The Public War-Crime
Claim](./⚖️_when_attribution_controls_the_public_war_crime_claim.md)

------------------------------------------------------------------------

## 🗣️ Public Attribution Creates Political Leverage

Public attribution is not legally necessary for conduct to have
occurred.

It can nevertheless matter enormously for what governments can credibly
say about it in public.

Imagine a government privately assesses with high confidence that a
foreign state directed an operation against protected civilian
infrastructure.

If it attributes publicly, it may gain the ability to say:

> this state attacked our civilian infrastructure during the armed
> conflict.

Depending on the facts, that can support diplomatic condemnation,
alliance coordination, sanctions, legal argument, criminal
investigation, or public claims under international humanitarian law.

But making the attribution may require revealing:

-   intelligence sources;
-   technical collection;
-   allied reporting;
-   covert access;
-   operational knowledge;
-   or the level of confidence actually held internally.

If the government does not attribute publicly, it may retain those
capabilities but lose some of the political and legal leverage that
public attribution would create.

The resulting bind can look like:

``` text
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

------------------------------------------------------------------------

## 🤐 Silence Has More Than One Meaning

A state may have good reasons not to disclose an attribution
immediately.

It may be protecting:

-   an investigation;
-   an intelligence source;
-   a technical capability;
-   an allied capability;
-   an ongoing counter-operation;
-   criminal proceedings;
-   or diplomatic space.

But public silence is analytically ambiguous.

It can mean:

``` text
we know substantially more than we can say
```

It can also mean:

``` text
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

------------------------------------------------------------------------

## 🤐 Non-Confirmation Can Also Become Part Of The Vulnerability

A blanket posture of:

> We can neither confirm nor deny.\
> We are not discussing the incident.\
> We do not comment on operational matters.

may protect some investigations.

Used too broadly, it may tell an adversary that:

-   responsibility is fragmented;
-   affected people may be left without a protection pathway;
-   institutions cannot coordinate visibly;
-   the state cannot explain what category of threat exists;
-   and further exploitation may occur before any public body accepts
    ownership.

That matters especially where the data concerns an individual.

The old organisational ransomware model is:

``` text
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

-   what can be disclosed publicly;
-   what can be disclosed privately;
-   what risk category applies;
-   who owns the protective response;
-   and what practical measures follow.

Silence is not always neutral.

Sometimes it protects an operation.

Sometimes it advertises the vulnerability.

------------------------------------------------------------------------

## 📰 Why Headlines Flatten The Problem

Headlines prefer clean statements.

Cyber attribution rarely offers them.

This creates two recurring errors.

The first is overclaiming:

> Iran attacks British education system.

when the public evidence only shows:

-   an education-sector breach;
-   during the Iran war;
-   claimed by a criminal group;
-   with no proven Iranian link.

The second is underclaiming:

> No evidence of Iranian involvement.

when the real position may be:

-   no definitive public attribution;
-   credible technical concern;
-   known Iranian interest in the same target class;
-   unresolved state involvement;
-   and a wider pattern worth monitoring.

The better wording is often less dramatic and more useful.

For example:

> The breach remains publicly unattributed. It is included because it
> affected essential state infrastructure during the war period,
> resembles activity already under investigation, and attribution
> remains open.

That preserves both the evidence and the uncertainty.

------------------------------------------------------------------------

## 📊 The Confidence Label Must Travel With The Claim

Every incident in this pack should preserve:

``` text
CLAIM:
SOURCE:
ATTRIBUTION TYPE:
CONFIDENCE:
PUBLIC / PRIVATE STATUS:
LIMIT:
```

For example:

``` text
CLAIM:
Iran-linked actors may have targeted the system.

SOURCE:
Preliminary state assessment and technical reporting.

ATTRIBUTION TYPE:
Suspected operator / sponsor linkage.

CONFIDENCE:
Moderate.

PUBLIC / PRIVATE STATUS:
Publicly reported suspicion; no definitive state attribution.

LIMIT:
Alternative criminal or copycat explanations remain open.
```

The confidence label should not disappear when the claim is repeated
elsewhere.

A suspected attribution does not become confirmed because ten newspapers
copied the same source.

Repetition is not corroboration.

------------------------------------------------------------------------

## 🧪 What Would Increase Confidence

Confidence should rise where new evidence shows:

-   matching infrastructure across several incidents;
-   operator overlap with previously attributed campaigns;
-   financial or communications links;
-   official findings;
-   recovered tasking;
-   technical artefacts difficult to imitate;
-   consistent victimology;
-   common control infrastructure;
-   law-enforcement seizure of operator infrastructure;
-   or independent corroboration from several competent sources.

Confidence should fall where:

-   the source withdraws the claim;
-   technical indicators are shown to be generic;
-   the alleged actor exaggerates impact;
-   the incident is traced to ordinary criminal activity;
-   timestamps or infrastructure do not match;
-   several unrelated operators are found exploiting the same
    vulnerability;
-   or rival explanations fit better.

The timeline should be able to move in both directions.

------------------------------------------------------------------------

## 🔁 Attribution Changes Are Events

The timeline should not record only changes in operational impact.

Changes in attribution are themselves substantive developments.

For example:

``` text
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

-   diplomatic consequences;
-   legal significance;
-   defensive priorities;
-   media language;
-   alliance response;
-   sanctions exposure;
-   and the interpretation of earlier incidents.

A later attribution can therefore change the meaning of an older event.

The timeline should preserve that history rather than silently
overwriting it.

------------------------------------------------------------------------

## 🧭 Attribution Confidence And Attribution Publication Are Different Axes

The July--August 2026 US water cases require a further distinction.

It is no longer enough to ask only:

``` text
HOW CONFIDENT IS THE ATTRIBUTION?
```

The pack must also ask:

``` text
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

``` text
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

``` text
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

------------------------------------------------------------------------

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

``` text
AMERICA ATTRIBUTED THE ATTACK TO IRAN
```

or:

``` text
AMERICA DOES NOT THINK IRAN DID IT
```

The more precise representation is:

``` text
REPORTED INVESTIGATIVE / INTELLIGENCE ASSESSMENT:
Iranian responsibility strongly favoured / reportedly assessed at high confidence

FORMAL PUBLIC FBI / CISA / NSA / EPA ATTRIBUTION:
not established in the public record reviewed for this update

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

------------------------------------------------------------------------

## 🏛️ Attribution Can Become A Governance Output

Public attribution is produced by institutions.

That means the public label may depend on more than evidentiary
confidence.

Possible constraints include:

-   source protection;
-   an active investigation;
-   intelligence equities;
-   allied sensitivities;
-   diplomatic negotiations;
-   escalation management;
-   legal thresholds;
-   interagency disagreement;
-   and political leadership.

Analysts should therefore avoid treating the final public label as a
pure measurement of technical certainty.

The public output may be:

``` text
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

------------------------------------------------------------------------

## 🌊 Attribution Must Follow The Wave, Not Flood The Whole Campaign

A strengthened Iran assessment for an initial or central wave must not
automatically migrate to every later intrusion in the same sector.

War can generate:

``` text
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

``` text
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

-   strategic importance;
-   central state direction;
-   effectiveness;
-   operational success;
-   a coherent campaign;
-   an international humanitarian law violation;
-   or individual criminal responsibility.

Likewise, an unattributed incident may still expose:

-   weak infrastructure;
-   fragmented governance;
-   poor victim protection;
-   a repeated target set;
-   physical-system vulnerability;
-   or a seam that several hostile actors can exploit.

Attribution is one part of the analysis.

It is not the whole analysis.

------------------------------------------------------------------------

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

That means holding two disciplines at once:

``` text
avoid false certainty
+
avoid false emptiness
```

The first protects accuracy.

The second protects situational awareness.

------------------------------------------------------------------------

## 🌌 Constellations

🇮🇷 🕸️ 🧅 🔎 🤐 🚰 ⚖️ --- Iran war analysis; graded attribution; layered
operators; source discipline; institutional silence; control systems;
legal responsibility.

## ✨ Stardust

iran, irgc, cyber attribution, confidence levels, proxy actors,
hacktivists, criminal overlap, ncnd, intelligence, operational security,
state responsibility, public attribution, individual criminal
responsibility, water infrastructure, operational technology

------------------------------------------------------------------------

## 🏮 Footer

*🕸️ Attribution Is Not A Light Switch* is a living node of the **Polaris
Protocol**.\
It defines how this pack separates technical attribution, public
governmental attribution, state responsibility, individual
responsibility, and the confidence attached to each.

> 📡 Cross-references:
>
> -   [🇮🇷 Data Wars: IRGC Edition](./README.md) --- *root orientation
>     and pack map*
> -   [🧭 What This Pack Is
>     Tracking](./🧭_what_this_pack_is_tracking.md) --- *scope and
>     inclusion rules*
> -   [🚰 When Cyber Reaches The
>     Machinery](./🚰_when_cyber_reaches_the_machinery.md) ---
>     *operational technology, control systems, and physical effect*
> -   [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) --- *separate
>     legal analysis for wartime cyber operations*
> -   [🧅 The Operator May Not Know The
>     Customer](./🧅_the_operator_may_not_know_the_customer.md) ---
>     *layered tasking and deniable labour*
> -   [🔎 Confidence Labels And Source
>     Rules](./🔎_confidence_labels_and_source_rules.md) --- *claim,
>     source, confidence, and limit*
> -   [📰 How To Report Without
>     Overclaiming](./📰_how_to_report_without_overclaiming.md) ---
>     *newsroom discipline under uncertainty*
> -   [⏱️ Timeline Of Essential Infrastructure
>     Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) ---
>     *live incident chronology*

*Survivor authorship is sovereign. Containment is never neutral.*

*Last updated: 2026-08-14*
