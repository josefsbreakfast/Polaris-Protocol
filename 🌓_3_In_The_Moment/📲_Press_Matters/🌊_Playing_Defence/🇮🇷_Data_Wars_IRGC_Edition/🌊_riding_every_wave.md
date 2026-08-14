# 🌊 Riding Every Wave

**First created:** 2026-08-14 \| **Last updated:** 2026-08-14 *How state
campaigns, aligned actors, criminal follow-on and ordinary opportunism
can overlap without sharing a command structure.*

------------------------------------------------------------------------

## 🛰️ Orientation

Cyber campaigns rarely arrive as a neat procession of attributable
incidents conducted by one actor under one chain of command.

Conflict changes the environment around an attack.

A state operation may generate publicity, expose vulnerable
infrastructure, reveal working techniques, consume defensive capacity,
create stolen access, attract ideologically aligned actors and advertise
profitable targets. Criminal groups may then exploit the same
environment. Some may have relationships with the state. Some may merely
share its enemies. Some may have noticed that everyone is looking the
other way.

The resulting activity can look like one large campaign from a distance.

It may not be.

The analytical task is therefore not simply to ask:

> **Who is attacking?**

It is also to ask:

> **Which wave are we looking at, what produced it, and what kind of
> relationship---if any---connects it to the waves around it?**

------------------------------------------------------------------------

## 🌊 One Conflict Can Produce Several Waves

A useful starting model distinguishes between several kinds of activity
that may coexist.

### 🏛️ State-directed activity

Operations can be directly tasked, coordinated, resourced or controlled
by a state institution.

This is the strongest organisational relationship.

Evidence may include:

-   government attribution;
-   intelligence reporting;
-   command relationships;
-   infrastructure or tooling tied to state operators;
-   tasking patterns;
-   operational coordination;
-   or technical evidence linking activity to a previously attributed
    state unit.

Even here, attribution should remain evidence-led. State interest in an
outcome does not by itself establish state direction of an operation.

### 🕸️ State-linked or proxy activity

An actor may have an established relationship with a state while
retaining significant operational autonomy.

Relationships can include:

-   funding;
-   technical assistance;
-   historical cooperation;
-   ideological alignment;
-   personnel overlap;
-   intelligence sharing;
-   tolerated activity;
-   or intermittent tasking.

"State-linked" therefore does not automatically mean:

> **the government ordered this particular incident.**

The relationship between actor and state and the attribution of a
specific operation are separate evidentiary questions.

### 📣 Aligned opportunism

Conflict attracts participants.

Hacktivists, ideological fellow-travellers, patriotic hacking groups and
other sympathetic actors may independently attack the same adversary.

Their activity may reinforce a state's strategic objectives without
being commissioned by that state.

Alignment of interests is not proof of command.

### 🤑 Criminal follow-on

Criminal actors may exploit conditions created by earlier activity.

This can include:

-   monetising stolen credentials;
-   purchasing access from brokers;
-   deploying ransomware into already-weakened environments;
-   extorting disrupted organisations;
-   exploiting vulnerabilities publicised by earlier incidents;
-   reusing publicly discussed techniques;
-   targeting sectors revealed to be poorly defended.

This activity may be **causally downstream** from a state campaign
without being **organisationally downstream** from the state.

That distinction matters.

### 🦹 Background opportunistic crime

Some attacks occurring during a conflict will simply be crime.

War does not suspend the normal cybercrime economy.

Indeed, instability may increase ordinary offending by:

-   stretching defenders;
-   increasing the number of exposed systems;
-   creating confusion about attribution;
-   disrupting routine maintenance;
-   increasing demand for illicit access;
-   generating more politically plausible cover for criminal activity.

A rise in cybercrime during conflict does not require every criminal
actor to have joined the war.

Sometimes war increases crime because war increases opportunity.

------------------------------------------------------------------------

## 🧿 Downstream Is Not The Same As Directed

One of the easiest analytical errors is to see a sequence like this:

``` text
state operation
      ↓
system disruption
      ↓
criminal exploitation
```

and silently convert it into:

``` text
state
  ↓
criminal operator
```

Those are different claims.

The first describes a **causal sequence**.

The second describes a **command or organisational relationship**.

A criminal group can benefit from conditions created by state activity
without receiving instructions, funding or assistance from that state.

Likewise, criminals can reuse:

-   credentials;
-   exposed services;
-   vulnerabilities;
-   malware concepts;
-   target lists;
-   public reporting;
-   or generalised defender exhaustion

created by an earlier campaign.

The state operation may therefore help explain **why the later crime
became possible or profitable** while explaining nothing about **who
ordered the later crime**.

------------------------------------------------------------------------

## 🌀 Conflict Changes The Opportunity Environment

Large cyber campaigns do not operate inside sealed laboratories.

They alter the environment in which subsequent actors make decisions.

A significant attack can produce several secondary effects at once:

``` text
                    STATE / STATE-LINKED ACTIVITY
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            ▼                  ▼                  ▼
      disruption         exposed access      publicity
            │                  │                  │
            ▼                  ▼                  ▼
     defender load       access markets      imitation
            │                  │                  │
            └──────────┬───────┴──────────┬──────┘
                       ▼                  ▼
                criminal follow-on   aligned activity
                       │                  │
                       └────────┬─────────┘
                                ▼
                    larger apparent campaign
```

From outside, this can resemble coordinated escalation.

Sometimes it is.

Sometimes it is several actors riding the same wave.

------------------------------------------------------------------------

## 🧩 Several Relationships Can Exist At Once

An actor relationship should not be forced into a single binary category
of either **state-controlled** or **completely unrelated**.

The useful questions are more granular.

### Organisational relationship

Is there evidence that the actors belong to, work for, receive direction
from or maintain an established relationship with the same organisation?

### Operational relationship

Is there evidence that actors coordinated this specific campaign or
incident?

### Technical relationship

Do incidents share infrastructure, malware, credentials, tooling or
techniques?

Shared techniques alone may be weak evidence if those techniques are
widely available.

### Causal relationship

Did one incident create conditions that enabled another?

This relationship may exist even where the actors have never
communicated.

### Strategic relationship

Do separate actors produce effects beneficial to the same state or
political objective?

Strategic alignment alone does not establish operational coordination.

### Temporal relationship

Did events occur close together?

Temporal clustering is useful for identifying patterns.

It is not proof of common command.

------------------------------------------------------------------------

## ⚖️ Do Not Make Criminal Activity Do Too Much Evidentiary Work

The appearance of criminal activity does not automatically weaken a
state attribution.

A campaign may contain:

-   state operations;
-   proxy operations;
-   criminal opportunism;
-   unrelated crime;
-   and incidents that remain unattributed.

Finding a criminal layer therefore does not establish that the state
layer was imaginary.

Equally, establishing state responsibility for part of a campaign does
not permit every nearby ransomware infection, intrusion or service
disruption to be assigned to the state.

Both errors flatten a mixed environment into a single story.

------------------------------------------------------------------------

## 🪆 Attribution Can Be Nested

A useful way to record complex campaigns is to attribute at several
levels.

For example:

``` text
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
└── Wave E
    └── unattributed / background activity
```

This prevents one attribution judgment from contaminating every incident
in the surrounding period.

It also allows confidence to change independently at each layer.

------------------------------------------------------------------------

## 🔎 Questions For Reading A Wave

When a new cluster of incidents appears around an existing state
campaign, ask:

-   What is actually shared between the incidents?
-   Are we seeing shared command, shared tooling, shared opportunity or
    merely shared timing?
-   Is the actor already known to have a relationship with the suspected
    state?
-   If so, is there evidence connecting that relationship to **this
    operation**?
-   Did earlier incidents expose access or vulnerabilities later actors
    could exploit?
-   Has publicity made the target class more attractive?
-   Has defensive capacity been diverted elsewhere?
-   Could criminal activity plausibly have increased independently
    because the environment became more permissive?
-   Is an actor claiming responsibility?
-   Does independent evidence corroborate the claim?
-   Are investigators attributing an incident, an operational cluster or
    the entire campaign?
-   Are we accidentally using evidence from one wave to attribute
    another?

The goal is not to fragment everything until attribution becomes
impossible.

The goal is to describe the relationships that the evidence actually
supports.

------------------------------------------------------------------------

## 🚨 Failure Mode: Everybody Works For Tehran

A state-linked actor appears.

A criminal actor appears later.

Both attack similar systems.

The incidents occur during the same geopolitical confrontation.

The temptation is to draw one enormous arrow back to the state.

That may eventually be correct.

But the intermediate relationships still require evidence.

Otherwise:

``` text
same enemy
+ same period
+ similar target
= same command
```

quietly becomes the attribution method.

It is not one.

------------------------------------------------------------------------

## 🚨 Failure Mode: One Criminal Means No State Campaign

The inverse error is equally poor.

If some incidents turn out to be:

-   ransomware;
-   financially motivated intrusion;
-   opportunistic scanning;
-   access brokerage;
-   or unrelated criminal exploitation,

that does not automatically disprove evidence connecting other incidents
to a state actor.

Mixed campaigns are allowed to be mixed.

Finding an opportunist riding the wave does not prove there was no wave.

------------------------------------------------------------------------

## 🧭 What This Model Preserves

This approach allows several propositions to remain true simultaneously:

> A state may initiate or direct a cyber campaign.

> State-linked actors may participate with varying degrees of autonomy.

> Ideologically aligned actors may independently join the activity.

> Criminals may exploit the resulting disruption.

> Some crime may be indirectly enabled by the campaign.

> Other crime may simply rise because conflict creates opportunity.

> None of those relationships should be upgraded into command without
> evidence.

The purpose is not to make attribution weaker.

It is to make attribution **more precise**.

------------------------------------------------------------------------

## 🌌 Constellations

🌊 🕸️ 🧿 🪆 📊 --- campaign ecology; layered attribution; state-linked
activity; criminal follow-on; causal versus organisational
relationships.

## ✨ Stardust

cyber conflict, attribution, state operations, proxy actors, criminal
follow-on, opportunistic crime, campaign waves, causal relationships,
command relationships, conflict ecology

------------------------------------------------------------------------

## 🏮 Footer

*Riding Every Wave* is a living node of the **Polaris Protocol**.\
It provides a reusable framework for distinguishing state-directed
operations, affiliated or aligned participation, criminal follow-on and
ordinary opportunism within conflict-driven cyber campaigns. It is
designed to preserve causal relationships without converting them
automatically into organisational attribution.

> 📡 Cross-references:
>
> -   [🕸️ Attribution Is Not A Light
>     Switch](./🕸️_attribution_is_not_a_light_switch.md) ---
>     *confidence, evidence and the limits of binary attribution*\
> -   [🔎 Confidence Labels And Source
>     Rules](./🔎_confidence_labels_and_source_rules.md) --- *separating
>     actor claims, investigative assessments and formal attribution*\
> -   [⏱️ Timeline Of Essential Infrastructure
>     Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) ---
>     *incident-level chronology in which different campaign waves can
>     be recorded separately*

*Survivor authorship is sovereign. Containment is never neutral.*

*Last updated: 2026-08-14*
