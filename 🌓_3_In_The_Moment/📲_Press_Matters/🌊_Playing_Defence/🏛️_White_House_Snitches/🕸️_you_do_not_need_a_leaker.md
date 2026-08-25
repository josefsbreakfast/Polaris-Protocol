# 🕸️ You Do Not Need A Leaker
**First created:** 2026-08-21 | **Last updated:** 2026-08-25  
*Why sensitive information appearing outside a protected environment does not, by itself, establish deliberate human disclosure.*

---

## 🛰️ Orientation

Sensitive information appears somewhere it should not.

The immediate question is often:

> **Who leaked it?**

Sometimes that is exactly the right question.

But notice what the wording has already done.

It has taken an **outcome**:

```text
OUTSIDER HAS INFORMATION
```

and quietly inserted a **mechanism**:

```text
INSIDER DELIBERATELY DISCLOSED INFORMATION
```

Those are not the same proposition.

Information can become available through deliberate disclosure.

It can also become available through accidental exposure, technical compromise, account compromise, physical observation, metadata, aggregation, inference, or several pathways interacting at once.

So the first analytical task is not to abolish the possibility of a leaker.

It is to avoid assuming one before the mechanism has been established.

> **You do not need a leaker to produce an information leak-shaped outcome.**

---

## 🕸️ Start With The Mechanism Tree

A useful investigation begins by keeping several pathways open.

```text
                 INFORMATION OUTCOME
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   DELIBERATE        ACCIDENTAL       TECHNICAL
   DISCLOSURE        DISCLOSURE       COMPROMISE
        │                │                │
        ├────────────────┼────────────────┤
        │                │                │
     ACCOUNT          PHYSICAL        METADATA /
    EXPOSURE        OBSERVATION       INFERENCE
        │                │                │
        └────────────────┼────────────────┘
                         │
                  MIXED PATHWAY
```

That is not an exhaustive taxonomy.

It is a reminder that:

```text
ONE OUTCOME
        ≠
ONE POSSIBLE CAUSE
```

The investigation can narrow as evidence accumulates.

It should not narrow merely because one explanation makes the easiest headline.

---

## 🙊 Sometimes There Really Is A Leaker

There is no need to become silly in the opposite direction.

People deliberately disclose protected information.

Officials brief journalists without authorisation.

Employees take information with them.

Insiders misuse legitimate access.

Espionage exists.

The category is real.

So:

```text
ALTERNATIVE PATHWAYS EXIST
        ≠
DELIBERATE DISCLOSURE DID NOT HAPPEN
```

The point is methodological.

If the evidence establishes that somebody intentionally disclosed the information, call it a deliberate disclosure.

If the evidence has established only that information became available outside the protected environment, do not silently upgrade that fact into knowledge of the mechanism.

> **Keep the hypothesis until you have the evidence.**

---

## 🤖 Machines Can Move Information Without Human Intent

A person can behave loyally and information can still escape through the systems around them.

At a high level, relevant pathways can include:

- compromised devices;
- compromised accounts;
- stolen credentials;
- insecure configurations;
- unintended synchronisation;
- inappropriate permissions;
- exposed services;
- or other technical failures.

The details vary enormously by system.

The analytical point does not.

```text
INFORMATION MOVED
        ≠
PERSON CHOSE TO MOVE IT
```

This is why [📱 The Phone Is Part Of The Security Boundary](./📱_the_phone_is_part_of_the_security_boundary.md) matters.

If the endpoint is part of the information environment, technical compromise belongs inside the incident model even where nobody suspects the endpoint's owner of wrongdoing.

---

## 👀 The Environment Can Expose Information

Not every pathway requires technical compromise either.

Information exists in physical and observational environments.

Someone may encounter:

- a screen;
- a conversation;
- a document;
- a meeting;
- a visitor;
- a schedule;
- a name;
- a movement pattern;
- or some other contextual clue.

Again:

```text
COULD OBSERVE
        ≠
DID OBSERVE

DID OBSERVE
        ≠
DISCLOSED

DISCLOSED
        ≠
MALICIOUS
```

But if the information could plausibly have been acquired through observation, then the incident review should not pretend that direct document access was the only possible route.

See [👀 Access Is More Than Opening The Document](./👀_access_is_more_than_opening_the_document.md).

---

## 🧩 Nobody Has To Possess The Final Proposition

Sometimes the outside observer does not acquire the final sensitive proposition at all.

They construct it.

```text
A
+
B
+
C
+
CONTEXT
        ↓
X
```

One fragment may come from a public source.

Another from an administrative system.

Another from observation.

Another from a legitimate conversation.

Nobody necessarily says X.

Nobody necessarily leaks X.

The observer builds X.

That is why [🧩 A Plus B Plus C Equals Classified](./🧩_a_plus_b_plus_c_equals_classified.md) treats aggregation as a distinct information pathway.

If an investigation searches only for the person who disclosed X, it may be searching for an event that never occurred.

---

## 📞 Nobody Has To Read The Message Either

The same principle applies to metadata.

An observer may learn something from:

```text
who
+
when
+
frequency
+
sequence
+
change
```

without knowing what anybody said.

A burst of contact does not reveal the conversation.

A meeting sequence does not prove coordination.

A recurring relationship does not explain itself.

But structure can contribute to inference.

So:

```text
NO MESSAGE CONTENT ACQUIRED
        ≠
NO INFORMATION ACQUIRED
```

See [📞 Metadata Can Tell The Story](./📞_metadata_can_tell_the_story.md).

---

## 🧬 Mixed Pathways Are Easy To Miss

Security incidents do not have to respect the neat categories in an explainer.

Several small conditions may interact.

For example:

```text
EXCESSIVE ACCESS
        +
ENDPOINT EXPOSURE
        +
CONTEXTUAL KNOWLEDGE
        ↓
USEFUL INFORMATION
```

Or:

```text
PUBLIC SCHEDULE
        +
PHYSICAL OBSERVATION
        +
METADATA
        +
KNOWN INSTITUTIONAL ROUTINE
        ↓
SENSITIVE INFERENCE
```

Or:

```text
HUMAN ERROR
        +
WEAK COMPARTMENTATION
        +
POOR LOGGING
        ↓
EXPOSURE THAT IS HARD TO RECONSTRUCT
```

This is why [🧬 The Attack Surface Has More Than One Strand](./🧬_the_attack_surface_has_more_than_one_strand.md) treats the joins between people, machines, organisations and information as part of the attack surface.

The mechanism may be a chain.

Do not insist that reality choose one box because the article needs one noun.

---

## 🔬 Mechanism Before Attribution

There are two different questions:

```text
HOW DID THE INFORMATION BECOME AVAILABLE?
```

and:

```text
WHO WAS RESPONSIBLE?
```

The first is about mechanism.

The second is about attribution and responsibility.

They interact.

But analytically, mechanism often needs to be established before strong attribution becomes possible.

If investigators do not know whether information left through:

- deliberate disclosure;
- a compromised account;
- physical observation;
- aggregation;
- or a mixed pathway;

then identifying everybody who knew the final proposition may not identify everybody relevant to the incident.

A useful sequence is:

```text
1. DEFINE THE INFORMATION OUTCOME
        ↓
2. MAP PLAUSIBLE PATHWAYS
        ↓
3. TEST PATHWAYS AGAINST EVIDENCE
        ↓
4. IDENTIFY THE SUPPORTED MECHANISM
        ↓
5. ATTRIBUTE RESPONSIBILITY WHERE EVIDENCE SUPPORTS IT
```

That sequence is slower than shouting **FIND THE LEAKER**.

It is also considerably more likely to identify the actual security problem.

---

## 🧅 Finding Dave Does Not Fix The Architecture

Suppose there really is a deliberate leaker.

Call him Naughty Dave.

Dave knowingly disclosed protected information.

Fine.

Investigate Dave.

But there is still another security question:

> **What did the architecture allow Dave to reach, and why?**

Perhaps Dave had appropriate access and deliberately abused it.

Perhaps Dave had far more access than his function required.

Perhaps logging was inadequate.

Perhaps compartmentation failed.

Perhaps the institution could not reconstruct what Dave accessed.

Perhaps one person's misuse had a much larger blast radius than necessary.

Finding the responsible human can therefore be necessary without being sufficient.

```text
FOUND DAVE
        ≠
FIXED SYSTEM
```

See [🧅 Compartmentation Exists For A Reason](./🧅_compartmentation_exists_for_a_reason.md).

---

## 🥸 Insider Risk Is Wider Than Deliberate Leaking

The phrase **insider threat** can make this problem worse if everybody hears it as:

> **spy inside the building.**

A person with legitimate access can be associated with security risk through many different circumstances.

They may:

- make an error;
- misunderstand a rule;
- possess excessive permissions;
- be deceived;
- be targeted;
- become aggrieved;
- have an account compromised;
- deliberately misuse access;
- or knowingly cooperate with an outside actor.

Those are not interchangeable states.

And they are not necessarily stages in a progression.

So even when an incident involves somebody **inside** the security boundary, the next question remains:

> **What actually happened?**

See [🥸 Insider Threat Does Not Mean Spy](./🥸_insider_threat_does_not_mean_spy.md).

---

## ⚖️ Alternative Mechanisms Are Not Alternative Facts

There is an equal and opposite analytical failure available here.

Once somebody learns that technical compromise, aggregation and metadata exist, they can begin inventing elaborate alternative explanations for everything.

No.

```text
POSSIBLE PATHWAY
        ≠
PATHWAY USED

TECHNICALLY POSSIBLE
        ≠
EVIDENTIALLY SUPPORTED

ALTERNATIVE EXPLANATION
        ≠
BETTER EXPLANATION
```

The purpose of widening the mechanism tree is to improve investigation.

Not to make every incident unknowable.

Evidence should narrow the tree.

Logs may support or exclude technical access.

Witness evidence may support deliberate disclosure.

Device analysis may identify compromise.

Access records may constrain who could have encountered particular information.

Public records may show that some supposedly secret inference was already reconstructable.

The objective is not permanent uncertainty.

It is **earned certainty**.

---

## 📰 “Who Leaked It?” Is Not A Neutral Question

Journalistic language can quietly encode an assumption.

Consider:

> **Officials are searching for the leaker.**

That may accurately describe what officials are doing.

Now compare:

> **Investigators are trying to determine how the information became public.**

The second formulation leaves the mechanism open.

The first may not.

This matters because readers often treat the grammar of a report as part of the evidence.

If every article says **leak**, **leaker**, and **who told whom**, the public can come away believing deliberate human disclosure has already been established even when the reporting supports only an unexplained information exposure.

That does not mean journalists should ban the word **leak**.

It means they should know when they are using it descriptively and when they are using it mechanistically.

> **“Who leaked it?” is a hypothesis about mechanism disguised as a neutral question.**

Sometimes the hypothesis is right.

It still needs proving.

---

## ✍️ Questions Journalists Should Actually Ask

When sensitive information appears outside a protected environment, useful questions include:

- What exactly became available?
- Was the final proposition directly disclosed, or could it have been reconstructed?
- What evidence supports deliberate human disclosure?
- Which people had formal, technical, physical, observational or contextual access?
- Which devices and accounts interacted with the relevant environment?
- Has technical compromise been examined?
- What access and audit logs exist?
- Could metadata have contributed to the inference?
- Which component facts were already public or legitimately available?
- Could several fragments have been aggregated?
- Were physical or observational pathways examined?
- Could multiple pathways have interacted?
- What evidence excludes plausible alternatives?
- Has the mechanism actually been established?
- Is attribution being made to a person, device, account, process or institution?
- If a human leaker is identified, what architectural failures allowed the exposure to become as serious as it did?

And one question should remain on the whiteboard until the evidence answers it:

> **Are we investigating how the information escaped, or are we investigating only the explanation we assumed at the beginning?**

---

## 🧿 The Actual Lesson

Sometimes there is a leaker.

Sometimes there is a compromised device.

Sometimes there is an exposed account.

Sometimes somebody sees something they should not.

Sometimes several people reveal fragments without revealing the conclusion.

Sometimes metadata supplies the pattern.

Sometimes the outside observer does the final analytical work.

Sometimes several of those things happen together.

The outcome:

```text
INFORMATION IS OUTSIDE
```

does not tell you, by itself, which mechanism produced it.

So do not invert the evidence.

Do not begin with:

```text
WHO LEAKED?
```

and make every fact fit underneath it.

Begin with:

```text
WHAT BECAME AVAILABLE?
        ↓
HOW COULD IT HAVE BECOME AVAILABLE?
        ↓
WHAT DOES THE EVIDENCE SUPPORT?
```

Then attribute responsibility.

> **You do not need a leaker to produce an information leak-shaped outcome.**

And if there was a leaker?

Excellent.

Now you know because you investigated the mechanism.

Not because the headline supplied it for you.

---

## 🌌 Constellations  
🕸️ 🧩 📞 🥸 ⚖️ — exposure mechanisms; aggregation; metadata; insider risk; evidential discipline.  

---

## ✨ Stardust  
information security, unauthorised disclosure, information exposure, technical compromise, aggregation risk, metadata, insider risk, attribution, incident investigation

---

## 🏮 Footer  

*🕸️ You Do Not Need A Leaker* is a living node of the **Polaris Protocol**.  

It distinguishes the outcome of sensitive information becoming externally available from the mechanism that produced that outcome.  
Within the White House Snitches cluster, it synthesises aggregation, metadata, endpoint and observational pathways before the folder turns to insider-risk and exploitation language, while retaining deliberate disclosure as a real hypothesis that must be established rather than assumed.

> 📡 Cross-references:
>
> - [☎️ The Call Is Coming From Inside The House](./☎️_the_call_is_coming_from_inside_the_house.md) — *the cluster-level introduction to distinguishing information outcomes from disclosure mechanisms*  
> - [🧩 A Plus B Plus C Equals Classified](./🧩_a_plus_b_plus_c_equals_classified.md) — *aggregation and reconstruction of sensitive conclusions without direct disclosure of the final proposition*  
> - [📞 Metadata Can Tell The Story](./📞_metadata_can_tell_the_story.md) — *how relationships, timing and structural patterns can contribute information without revealing message content*  
> - [📱 The Phone Is Part Of The Security Boundary](./📱_the_phone_is_part_of_the_security_boundary.md) — *technical interfaces through which information can become exposed without deliberate cooperation by the device owner*  
> - [🧬 The Attack Surface Has More Than One Strand](./🧬_the_attack_surface_has_more_than_one_strand.md) — *the wider sociotechnical system in which several exposure mechanisms can interact*  
> - [🧅 Compartmentation Exists For A Reason](./🧅_compartmentation_exists_for_a_reason.md) — *why identifying a responsible person does not remove the need to examine architectural blast radius and containment*  
> - [🥸 Insider Threat Does Not Mean Spy](./🥸_insider_threat_does_not_mean_spy.md) — *the distinction between insider-associated risk, error, compromise, deliberate misuse and espionage*  
> - [✍️ Questions Journalists Should Actually Ask](./✍️_questions_journalists_should_actually_ask.md) — *practical reporting prompts for establishing mechanism before attribution*
>   
> 🏮 Return To:
>
> - [🏛️ White House Snitches](./README.md) — *1up*  
> - [🌊 Playing Defence](../README.md) — *2up*  
> - [📲 Press Matters](../../README.md) — *3up*  
> - [🌗 In The Moment](../../../README.md) — *3up* 
> - [🌌 Polaris Protocol - Root](../../../../README.md) — *root*  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-08-25_
