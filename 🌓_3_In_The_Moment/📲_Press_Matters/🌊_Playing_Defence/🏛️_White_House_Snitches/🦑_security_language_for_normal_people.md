# 🦑 Security Language For Normal People

**First created:** 2026-08-21 | **Last updated:** 2026-08-21
*A plain-language guide to the security words that get collapsed into
"leak", "hack", "spy", and other nouns that quietly claim more evidence
than we actually have.*

---

## 🛰️ Orientation

Security reporting has a vocabulary problem.

Something strange happens around sensitive information and, within
approximately twelve seconds, everybody is using one of four words:

> **leak**

> **hack**

> **breach**

> **spy**

Unfortunately, those words do not all mean the same thing.

Worse, choosing the wrong one can quietly smuggle an entire theory of
the incident into the reporting before the underlying facts have been
established.

If information appears somewhere unexpected, we may know an **outcome**.

We may not yet know:

- the mechanism;
- the pathway;
- the actor;
- the intent;
- whether anybody deliberately disclosed anything;
- whether a technical system was compromised;
- whether an external actor exploited the exposure;
- or who, if anybody, should ultimately be blamed.

This node is therefore not an attempt to turn journalists into
counterintelligence officers.

It is a translation sheet.

The governing rule is simple:

> **Words are evidence labels. Do not promote the evidence by changing
> the noun.**

---

## 🧠 Start With The Evidential Ladder

Before the glossary, keep this distinction available:

```text
something could happen
        ↓
there is reason to consider it plausible
        ↓
evidence suggests it may have happened
        ↓
evidence establishes that it happened
        ↓
evidence identifies the mechanism
        ↓
evidence supports attribution
        ↓
evidence supports intent / knowing cooperation
```

Those are different evidential states.

So are these:

```text
EXPOSURE
    ≠
COMPROMISE

COMPROMISE
    ≠
DELIBERATE DISCLOSURE

DELIBERATE DISCLOSURE
    ≠
ESPIONAGE

CAPABILITY
    ≠
EXPLOITATION

EXPLOITATION
    ≠
ATTRIBUTION
```

A great deal of bad security commentary consists of climbing this ladder
without noticing.

---

## 💧 Leak

In ordinary reporting, **leak** usually means that somebody with access
to information deliberately provided it outside the authorised channel.

Simplified:

```text
person knows information
        ↓
person intentionally discloses it
        ↓
unauthorised recipient
```

This is a perfectly real category.

It is not a synonym for:

> **information became public**

or:

> **information escaped**

If the mechanism has not been established, "leak" may be premature.

### Better language when the mechanism is unknown

- "the information became public";
- "the information was disclosed";
- "the information appeared outside the expected security
    environment";
- "investigators are examining how the information became available."

See:

[☎️ The Call Is Coming From Inside The
House](./☎️_the_call_is_coming_from_inside_the_house.md).

---

## 📤 Unauthorised Disclosure

An **unauthorised disclosure** is information being communicated or made
available without the required authorisation.

That category is broader and more useful than casually shouting
**LEAK**.

Depending upon the facts, an unauthorised disclosure may be:

- deliberate;
- accidental;
- negligent;
- oral;
- written;
- digital;
- physical;
- or produced through inappropriate handling.

The useful question is:

> **What was disclosed, to whom, through what pathway, and with what
> evidence of intent?**

Do not infer the final answer from the label.

---

## 👀 Exposure

**Exposure** is the broadest useful word in this folder.

Information is exposed when it becomes accessible, observable or
inferable outside the controls that were supposed to constrain it.

Exposure does not necessarily mean anybody actually exploited the
opportunity.

For example:

```text
sensitive material visible
to an unauthorised person
```

may constitute an exposure.

It does not automatically establish:

```text
unauthorised person
noticed it
        ↓
understood it
        ↓
recorded it
        ↓
used it
        ↓
passed it onwards
```

This distinction matters because:

> **A vulnerability or exposure can be serious even when successful
> exploitation has not been demonstrated.**

Security exists partly to prevent the opportunity becoming the incident.

---

## 🧨 Compromise

**Compromise** generally indicates that a person, account, device,
system, credential, process or body of information can no longer be
treated as securely controlled in the expected way.

Examples might include:

- compromised credentials;
- a compromised account;
- a compromised endpoint;
- compromised classified material;
- a compromised source;
- a compromised security procedure.

But even this word needs specificity.

> **What exactly is believed to be compromised, and what evidence
> establishes that?**

"Compromised person" can also be particularly slippery in political
conversation.

It might mean anything from:

- vulnerable to pressure;
- subject to a conflict;
- technically surveilled;
- manipulated;
- knowingly cooperating with somebody;
- or merely "I don't trust them."

Those are not interchangeable.

Name the actual condition wherever possible.

---

## 🚨 Breach

**Breach** usually describes a violation of a security boundary,
requirement or control.

Depending on context, that might mean:

- unauthorised access;
- unauthorised disclosure;
- loss of protected information;
- violation of a security procedure;
- or compromise of a technical system.

But "breach" should not become a magical word meaning:

> **bad security thing happened somehow**

If reporting says there was a breach, ask:

- Which boundary was breached?
- Which control failed?
- What became accessible?
- Was access actually obtained?
- Was information taken?
- Is the term being used technically, legally, organisationally, or
    colloquially?

The noun does not answer those questions for you.

---

## 🕳️ Vulnerability

A **vulnerability** is a weakness that could potentially be exploited.

That weakness may be:

- technical;
- procedural;
- organisational;
- physical;
- human;
- social;
- or some combination.

Examples include:

- excessive permissions;
- poor authentication;
- unmanaged devices;
- weak physical controls;
- inadequate separation of duties;
- incomplete personnel assurance;
- poorly designed procedures.

A vulnerability is not evidence that exploitation occurred.

```text
vulnerability exists
        ≠
vulnerability was exploited
```

But:

```text
no proven exploitation
        ≠
vulnerability does not matter
```

This is one of the most important distinctions in preventive security.

---

## 🛠️ Exploit / Exploitation

To **exploit** a vulnerability is to use it to achieve some result.

In technical security, an exploit may refer to a method that takes
advantage of a particular weakness.

In broader security analysis, exploitation can also describe taking
advantage of:

- access;
- relationships;
- predictable behaviour;
- organisational weaknesses;
- information asymmetries;
- or personal circumstances.

Keep the level of claim clear.

```text
vulnerability
        ↓
possible exploitation
        ↓
evidence of attempted exploitation
        ↓
evidence of successful exploitation
```

Do not jump from the first box to the last.

---

## 🖥️ Intrusion

An **intrusion** generally means unauthorised entry into a system,
network, account, environment or protected space.

A technical intrusion is more specific than "something weird happened
with the phone."

Evidence might support:

- suspicious activity;
- attempted access;
- successful unauthorised access;
- persistence;
- data acquisition.

Those are different findings.

"Hack" is often used conversationally for all of them.

Which brings us to---

---

## 🪓 Hack

**Hack** is an extremely useful word if your goal is to make five
technically different things sound identical.

It may refer to:

- credential theft;
- account takeover;
- malware;
- exploitation of a software vulnerability;
- social engineering;
- unauthorised access;
- device compromise;
- data theft;
- website defacement;
- or merely unexpected technical behaviour.

If you know the mechanism, **name the mechanism**.

If you do not, say what is actually known.

> "The account was accessed without authorisation" is better than
> "hackers hacked the account" if that is all the evidence supports.

Security language becomes clearer remarkably quickly once the word
**hack** is denied unlimited employment.

---

## 🥸 Insider Risk / Insider Threat

An **insider** is somebody whose legitimate relationship with an
organisation gives them some degree of trusted access, knowledge or
proximity.

An **insider risk** is the possibility that this position could
contribute to harm.

An **insider threat** generally refers to the security threat associated
with insiders, but public discussion often hears the phrase and
immediately translates it into:

> **SECRET TRAITOR**

That is too narrow.

Insider-associated harm can involve:

- malicious activity;
- deliberate leaking;
- fraud;
- sabotage;
- negligence;
- mistakes;
- excessive access;
- compromised credentials;
- coercion;
- social engineering;
- or exploitation of the insider by somebody else.

So:

```text
insider risk
        ≠
malicious insider
        ≠
spy
```

A person can even be simultaneously:

```text
an insider security risk
+
the victim of an outside actor
```

See:

[🥸 Insider Threat Does Not Mean
Spy](./🥸_insider_threat_does_not_mean_spy.md).

---

## 🛰️ Intelligence Collection

**Intelligence collection** is the acquisition of information for
intelligence purposes.

That information does not have to arrive through a recruited spy
carrying classified documents.

Collection can draw upon many kinds of sources, including:

- human reporting;
- technical collection;
- cyber activity;
- imagery;
- signals;
- open-source material;
- public records;
- commercial information;
- metadata;
- observation;
- and combinations of otherwise unremarkable facts.

This matters because:

> **Information can have intelligence value without being classified.**

And:

> **Collection does not require the target to knowingly cooperate.**

The collector may simply be observing, acquiring, combining or
inferring.

---

## 🕵️ Espionage

**Espionage** is a substantially stronger and more specific concept than
"security risk".

At the broadest level, it concerns obtaining sensitive or protected
information through clandestine intelligence activity.

In reporting on an individual, alleging espionage is serious.

Do not turn:

```text
person had access
```

into:

```text
person was vulnerable
```

into:

```text
person may have been targeted
```

into:

```text
person was compromised
```

into:

```text
person was spying
```

without evidence supporting every necessary step.

Security analysis becomes **more** useful when it preserves these
distinctions.

It does not become timid.

---

## 🗣️ Elicitation

**Elicitation** is obtaining useful information through interaction
without necessarily asking an obvious direct question.

At a high level, this can involve conversation designed to encourage
somebody to reveal information, context or confirmation.

The person providing the information may not understand its
significance.

They may not realise that information is being systematically gathered
at all.

This is one reason security training sometimes contains rules that feel
strangely cautious about apparently ordinary conversations.

The point is not:

> **Everyone you meet is a spy.**

The point is:

> **You may understand the value of the information you hold differently
> from the person trying to obtain it.**

---

## 🤝 Recruitment

**Recruitment** is a much stronger proposition.

In intelligence language, it generally implies that somebody has been
brought into some form of knowing or managed relationship to provide
assistance or information.

Do not use **recruited** when what you actually mean is:

- approached;
- befriended;
- cultivated;
- targeted;
- manipulated;
- elicited from;
- surveilled;
- or technically compromised.

Those may all be security-relevant.

They are not synonyms.

---

## 🍯 Honeypot

A **honeypot** or **honey trap**, in the human-intelligence sense,
generally refers to the deliberate use of romantic or sexual attraction
as part of an intelligence or influence operation.

It is not:

> attractive person near important person.

Nor:

> person of a particular nationality dating somebody interesting.

Nor:

> woman standing next to politician.

Actual security analysis requires evidence of deliberate cultivation or
operational purpose.

More importantly, intelligence exploitation does not require sex or
romance at all.

Friendship, professional relationships, ego, ideology, money, grievance,
access, coercion, technical surveillance and simple human sociability
can all matter.

See:

[🍯 Honeypots Are Not Magic](./🍯_honeypots_are_not_magic.md).

---

## 👤 Asset / Source / Agent

These words are often used loosely, and terminology varies between
organisations and contexts.

That is precisely why journalists should be careful.

### Source

A **source** provides information.

That does not automatically tell you:

- whether they know they are providing intelligence;
- whether they are formally recruited;
- whether they are paid;
- whether they act repeatedly;
- or whether they understand the ultimate recipient.

### Asset

**Asset** is used in several ways across intelligence, security and
popular culture.

It can imply a person or capability considered useful to an intelligence
organisation, but public usage is inconsistent.

If you mean:

> **knowingly recruited human source**

say that.

If you mean:

> **person whose access could potentially be useful**

do **not** quietly upgrade them into an "asset".

### Agent

**Agent** is another word with jurisdictional and institutional
ambiguity.

It may refer to somebody acting on behalf of another actor; in American
everyday usage it can also mean an officer of an agency such as the FBI.

Again:

> **Name the relationship you actually have evidence for.**

Do not use spy-film vocabulary as an evidentiary shortcut.

---

## 🪪 Clearance

A **security clearance** is part of a system for determining and
managing eligibility for access to particular categories of sensitive or
classified information.

It is not:

```text
GOOD PERSON CERTIFICATE
```

Nor does holding a clearance ordinarily mean:

```text
ACCESS TO EVERYTHING
```

Clearance interacts with:

- role;
- authorisation;
- need-to-know;
- compartmentation;
- system permissions;
- physical access;
- continuing security obligations;
- and other controls.

Likewise:

```text
no completed clearance
        ≠
spy
```

The relevant questions are:

- What assurance was required?
- What had been completed?
- What access existed?
- What interim controls applied?
- What remained unassessed?

See:

[🪪 Clearance Is Not A Lanyard](./🪪_clearance_is_not_a_lanyard.md).

---

## 👁️ Access

**Access** is not one binary property.

Someone can have:

- formal access;
- technical access;
- physical access;
- contextual access;
- observational access;
- indirect access;
- temporary access;
- excessive access;
- or access to fragments from which something else can be inferred.

This matters because:

> **"She did not have access to that document" does not necessarily
> answer whether she could know, observe or infer the relevant
> information.**

Equally:

> **Being physically near sensitive activity does not establish that
> somebody actually acquired sensitive information.**

Again: pathway first, evidence second.

See:

[👀 Access Is More Than Opening The
Document](./👀_access_is_more_than_opening_the_document.md).

---

## 🔐 Need-To-Know

**Need-to-know** is the principle that being generally trusted or
cleared does not automatically entitle somebody to every piece of
sensitive information.

Access should be related to what they require for their function.

This reduces unnecessary exposure.

It also limits the consequences when something else goes wrong.

```text
CLEARED
        ≠
NEEDS EVERYTHING
```

Need-to-know is not necessarily a judgment on the person's character.

It is a way of reducing the attack surface.

---

## 🧅 Compartmentation

**Compartmentation** separates sensitive information so that access to
one area does not automatically provide access to another.

Think:

```text
one failure
        ↓
limited damage
```

rather than:

```text
one failure
        ↓
welcome to absolutely everything
```

Compartmentation is one expression of a broader security principle:

> **Assume individual controls will eventually fail and design the
> system so that one failure does not become universal exposure.**

See:

[🧅 Compartmentation Exists For A
Reason](./🧅_compartmentation_exists_for_a_reason.md).

---

## 📞 Metadata

**Metadata** is data about data.

Depending upon the system, it can include things such as:

- who communicated;
- when;
- how often;
- duration;
- account identifiers;
- device information;
- routing information;
- file properties;
- or other contextual records.

Metadata is not automatically trivial merely because it is not message
content.

Patterns can reveal:

- relationships;
- routines;
- changes in behaviour;
- organisational structure;
- unusual activity;
- or associations worth further investigation.

But metadata also requires interpretation.

```text
pattern
        ≠
proven explanation for pattern
```

See:

[📞 Metadata Can Tell The Story](./📞_metadata_can_tell_the_story.md).

---

## 🧩 Aggregation

**Aggregation** is what happens when individually limited pieces of
information become substantially more revealing when combined.

```text
A + B + C + existing context
        =
something nobody explicitly disclosed
```

This is particularly important in political and national-security
reporting because journalists, researchers, intelligence services and
ordinary observers can all combine information from multiple sources.

The collector does not begin with an empty brain.

See:

[🧩 A Plus B Plus C Equals
Classified](./🧩_a_plus_b_plus_c_equals_classified.md).

---

## 🎯 Attribution

**Attribution** is the process of determining who is responsible for an
action or operation.

It is often substantially harder than establishing that something
happened.

For example:

```text
account behaved abnormally
        ↓
evidence of unauthorised access
        ↓
evidence of a particular technique
        ↓
infrastructure / behavioural indicators
        ↓
assessment of responsible actor
```

Those steps may require different evidence.

And even where an operation is attributed to infrastructure or operators
associated with a state, further questions can remain about:

- direction;
- sponsorship;
- customer;
- intent;
- and the role of particular individuals.

The crucial rule:

> **Capability is not attribution. Motive is not attribution.
> Opportunity is not attribution.**

All three may inform an assessment.

None independently proves it.

---

## 🧿 Threat Assessment

A **threat assessment** asks what could plausibly harm the thing being
protected.

It can consider:

```text
asset
+
adversary / hazard
+
capability
+
intent
+
vulnerability
+
exposure
+
consequence
```

Not every assessment uses exactly those labels.

The important conceptual point is that threat assessment is prospective.

It asks:

> **What should we prepare for?**

That is different from attribution, which asks:

> **Who actually did this?**

So:

```text
FOREIGN INTELLIGENCE SERVICE
IS A RELEVANT THREAT
        ≠
FOREIGN INTELLIGENCE SERVICE
CAUSED THIS INCIDENT
```

See:

[🇮🇷 Guys, You Are In A War,
Remember](./🇮🇷_guys_you_are_in_a_war_remember.md).

---

## 🧬 Attack Surface

The **attack surface** is the collection of pathways through which a
system, person or organisation might be reached, influenced, observed,
accessed or exploited.

For modern political institutions, that can include:

```text
devices
+
accounts
+
networks
+
people
+
buildings
+
relationships
+
vendors
+
communications
+
procedures
+
information flows
```

The point is not that every surface is equally vulnerable.

The point is that:

> **security does not stop at the edge of the laptop.**

See:

[🧬 The Attack Surface Has More Than One
Strand](./🧬_the_attack_surface_has_more_than_one_strand.md).

---

## 🦠 Porosity

**Porosity** is useful Polaris shorthand for an environment containing
multiple poorly controlled pathways through which information, access or
influence can move.

One mistake may be an incident.

Repeatedly unclear interfaces can indicate an architectural problem.

```text
many weak boundaries
+
many informal pathways
+
unclear assurance
=
porous environment
```

Porosity does not tell you who exploited anything.

It tells you that there may be too many routes available for
investigators to sensibly treat one suspected person as the whole
security model.

See:

[🦠 Porosity Is A Security
Failure](./🦠_porosity_is_a_security_failure.md).

---

## ⚖️ The Words That Most Need Keeping Apart

If you remember nothing else, keep these:

```text
INFORMATION BECAME PUBLIC
        ≠
LEAK PROVEN
```

```text
VULNERABILITY
        ≠
EXPLOITATION
```

```text
EXPOSURE
        ≠
COMPROMISE
```

```text
COMPROMISE
        ≠
MALICIOUS COOPERATION
```

```text
INSIDER RISK
        ≠
SPY
```

```text
TARGETED
        ≠
RECRUITED
```

```text
CAPABILITY
        ≠
ATTRIBUTION
```

```text
CLEARANCE
        ≠
ACCESS TO EVERYTHING
```

```text
NO CLEARANCE
        ≠
ESPIONAGE
```

```text
FOREIGN INTELLIGENCE THREAT
        ≠
FOREIGN INTELLIGENCE CULPRIT
```

And perhaps most importantly:

```text
WE DO NOT YET KNOW
        ≠
NOTHING HAPPENED
```

It also does not mean:

```text
WE MAY INSERT WHICHEVER
SPY FILM PLOT WE LIKE
```

---

## 📰 A Small Translation Table For Journalists

  -----------------------------------------------------------------------
  If you are tempted to write         Ask whether you actually know
  ----------------------------------- -----------------------------------
  "the leaker"                        Was deliberate disclosure
                                      established?

  "the hack"                          What technical mechanism was
                                      identified?

  "the breach"                        Which boundary or control was
                                      breached?

  "the compromised aide"              Compromised in what specific sense?

  "the insider threat"                Malicious, negligent, exploited, or
                                      merely access-bearing?

  "the spy"                           What evidence establishes espionage
                                      or knowing cooperation?

  "the asset"                         What relationship has actually been
                                      established?

  "the foreign operation"             What evidence supports attribution?

  "they had access"                   Formal, technical, physical,
                                      contextual, observational, or
                                      inferential?

  "there is no evidence of hacking"   Does that exclude other exposure
                                      pathways, or merely one mechanism?
  -----------------------------------------------------------------------

Precision does not make the story less interesting.

Usually it reveals that the actual story is **more interesting than the
shorthand**.

---

## 🏛️ The Actual Lesson

Security language should help us distinguish hypotheses.

It should not conceal them.

If you call every unexplained information escape a **leak**, you have
already chosen a human disclosure mechanism.

If you call every strange technical event a **hack**, you may have
claimed a technical mechanism you cannot establish.

If you call every insider-associated risk a **spy**, you have
transformed security analysis into accusation.

And if you call every capable foreign intelligence service the
perpetrator of every unexplained incident, you have simply replaced one
lazy threat model with another.

The useful discipline is less exciting and considerably more powerful:

> **Say what you know.**

> **Label what you infer.**

> **Keep plausible pathways open until evidence closes them.**

> **Do not promote the evidence by changing the noun.**

Security is complicated enough without making the vocabulary lie.

---

## 🌌 Constellations  
🦑 ☎️ 🪪 🧿 🕸️ — security literacy; evidential discipline; personnel assurance; threat assessment; information exposure.

## ✨ Stardust  
information security, security language, threat assessment, information exposure, personnel security, insider risk, counterintelligence, attribution, press literacy

---

## 🏮 Footer

*🦑 Security Language For Normal People* is a living node of the
**Polaris Protocol**.
It provides a plain-language vocabulary for reporting and reasoning
about information-security, personnel-security and counterintelligence
questions without silently converting possibilities into established
mechanisms or allegations.

> 📡 Cross-references:
>
> - [☎️ The Call Is Coming From Inside The
>     House](./☎️_the_call_is_coming_from_inside_the_house.md) — *why
>     an observed information outcome does not establish a deliberate
>     leak mechanism*
> - [🪪 Clearance Is Not A
>     Lanyard](./🪪_clearance_is_not_a_lanyard.md) — *clearance,
>     personnel assurance, access and compensating controls*
> - [👀 Access Is More Than Opening The
>     Document](./👀_access_is_more_than_opening_the_document.md) —
>     *direct, indirect, physical, contextual and inferential access*
> - [🧬 The Attack Surface Has More Than One
>     Strand](./🧬_the_attack_surface_has_more_than_one_strand.md) —
>     *human, technical, physical, social and organisational security
>     surfaces*
> - [🧩 A Plus B Plus C Equals
>     Classified](./🧩_a_plus_b_plus_c_equals_classified.md) —
>     *aggregation and inferential disclosure*
> - [📞 Metadata Can Tell The
>     Story](./📞_metadata_can_tell_the_story.md) — *patterns and
>     contextual information beyond message content*
> - [🥸 Insider Threat Does Not Mean
>     Spy](./🥸_insider_threat_does_not_mean_spy.md) —
>     *insider-associated risk without premature espionage allegations*
> - [🦠 Porosity Is A Security
>     Failure](./🦠_porosity_is_a_security_failure.md) — *systemic
>     exposure architecture beyond individual culpability*
> - [🇮🇷 Guys, You Are In A War,
>     Remember](./🇮🇷_guys_you_are_in_a_war_remember.md) — *threat
>     assessment versus attribution in an active international security
>     environment*
> - [✍️ Questions Journalists Should Actually
>     Ask](./✍️_questions_journalists_should_actually_ask.md) —
>     *practical reporting prompts for preserving these distinctions*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-21_
