# ☎️ The Call Is Coming From Inside The House  
**First created:** 2026-08-21 | **Last updated:** 2026-08-25  
*Why "who leaked it?" is only one of several possible explanations for information escaping a supposedly secure environment.*  

---

## 🛰️ Orientation

When sensitive information appears somewhere it should not, there is an extremely tempting story:

**Someone leaked it. Find the leaker.**

Sometimes that is exactly what happened.

Sometimes it is not.

Information can leave a secure environment because somebody deliberately disclosed it. It can also become exposed because a device was compromised, an account was inadequately protected, somebody had inappropriate access, a conversation was overheard, metadata revealed a pattern, security controls were inconsistently applied, or several individually unremarkable pieces of information were assembled by somebody outside the system.

Those are different security problems.

Treating all of them as **"a leak"** can therefore produce a particularly unfortunate investigation: an organisation becomes extremely good at hunting for a person who may not exist, while leaving the pathway by which the information escaped completely intact.

This folder exists because journalists need enough security literacy to ask the second question.

Not merely:

> **Who told someone?**

But:

> **How could this information have become available?**

Those questions overlap.

They are not the same question.

More fundamentally:

```text
INFORMATION GOT OUT
        ≠
SOMEBODY LEAKED IT
```

The first describes an **outcome**.

The second proposes a **mechanism**.

Do not quietly turn one into the other.

---

## ☎️ Before We Decide Where The Call Is Coming From

The title comes from a familiar horror-film structure.

Something alarming is happening.

The threat is traced.

And then comes the revelation:

> **The call is coming from inside the house.**

There is just one problem with importing that structure into information security.

In the film, somebody has already established that there **is a call**.

In an information incident, that is often precisely what remains uncertain.

Everybody can end up shouting:

> **THE CALL IS COMING FROM INSIDE THE HOUSE**

before establishing whether it was a phone call.

That distinction matters.

```text
THE INFORMATION
IS OUTSIDE THE HOUSE

        ≠

A PERSON INSIDE THE HOUSE
DELIBERATELY PUT IT THERE
```

And even if some part of the exposure pathway does originate inside:

```text
inside access
        ≠
deliberate disclosure

deliberate disclosure
        ≠
disclosure to a journalist

insider involvement
        ≠
malicious insider

malicious insider
        ≠
foreign agent
```

Those are progressively different propositions.

Each requires evidence.

---

## 🧠 Outcome Is Not Mechanism

An information-security incident can contain several separate questions.

### What happened?

Information became available somewhere it was not expected to be.

### How did it happen?

That is the mechanism.

### Who or what was involved?

That is the actor question.

### Why did it happen?

That is the intent question.

### Who ultimately acquired or exploited it?

That is another question again.

Do not collapse them.

```text
OUTCOME
    ≠
MECHANISM
    ≠
ACTOR
    ≠
INTENT
    ≠
ATTRIBUTION
```

A journalist may possess strong evidence for the first proposition and very little evidence for the others.

That is fine.

**Uncertainty is an evidential state, not a reporting failure.**

The problem begins when uncertainty is made to disappear by choosing a familiar noun.

---

## ☎️ The Comforting Theory Of Naughty Dave

The traditional leak narrative has an appealingly simple architecture:

```text
protected information
        ↓
authorised person
        ↓
deliberate disclosure
        ↓
unauthorised recipient
```

Find the authorised person who made the disclosure and you have found the failure.

Call him Naughty Dave.

Naughty Dave certainly exists as a category of security problem.
Governments really do experience deliberate unauthorised disclosures.
Insider threats really do exist. People really do mishandle information intentionally.

The problem begins when **Naughty Dave becomes the default explanation for every unexplained information escape.**

Because the actual architecture might instead look like:

```text
sensitive environment
        ↓
person / device / account / meeting / calendar
        ↓
uncontrolled or compromised interface
        ↓
information exposure
```

Nobody in that chain necessarily decided to disclose anything.

Dave may be guilty.

Dave may be innocent.

**Dave may be completely unnecessary to the causal model.**

---

## 🕸️ You Do Not Need A Leaker

Consider several simplified possibilities.

### Deliberate Disclosure

```text
Official → Journalist
```

The classic leak.

Someone knows protected information and intentionally communicates it to somebody who is not authorised to receive it.

### Accidental Disclosure

```text
Official → insecure handling → unintended recipient
```

The information escapes, but there is no intention to leak it.

### Technical Compromise

```text
Official → compromised device/account → outside actor
```

The official may behave entirely loyally.

The information still escapes.

### Environmental Exposure

```text
meeting / screen / document / conversation
                    ↓
              observable person
```

The information becomes available because somebody can see, hear or
otherwise encounter something they should not.

### Aggregation

```text
A + B + C + context → sensitive conclusion
```

Nobody necessarily discloses the sensitive conclusion at all.

Someone else reconstructs it.

### Multiple Independent Fragments

```text
Source A ─┐
Source B ─┼─→ outside observer → conclusion
OSINT    ─┤
metadata ─┘
```

There may not even be one decisive information transfer.

The final conclusion can emerge from several routes.

These pathways require different investigations and different
mitigations.

The point is not:

> **Anything could have happened.**

It is:

> **Until evidence discriminates between pathways, several materially
> different mechanisms may remain possible.**

That is why **"who leaked?" should not silently become "how was this
compromised?"**

---

## 🪪 Vetting Is Not A Magic Trust Certificate

Security clearance is frequently described in public discussion as though the government has performed an elaborate ceremony and declared:

> THIS PERSON IS GOOD.

That is not a useful mental model.

Vetting and clearance processes form part of a wider personnel-security system intended to assess and manage risks associated with giving people access to sensitive environments and information.

And that wider environment matters.

A security system may need to consider not merely whether someone *intends* to betray an organisation, but whether relevant risks surrounding their access have been identified and appropriately managed.

Depending on the system and role, that wider security picture can include matters such as:

- what information the person may access;
- what systems they may use;
- what devices or communications arrangements are permitted;
- what reporting obligations apply;
- what outside contacts or circumstances require assessment;
- what continuing security requirements accompany the role;
- and what restrictions or compensating controls are necessary.

This creates an important distinction.

**An uncleared or incompletely vetted person is not thereby a spy.**

Nor does the absence of a completed clearance automatically establish that appropriate security controls were absent.

Interim arrangements, restricted access, escorts, separately managed devices or other compensating controls may exist.

But if the ordinary assurance process has not been completed, journalists have an entirely legitimate next question:

> **What controls were actually in place instead?**

That is a security question.

It is not an accusation of espionage.

There is another reason this matters after an incident.

A functioning assurance system gives investigators a baseline.

It helps establish:

- who should have had access;
- what access they should have had;
- which systems and devices were authorised;
- what restrictions applied;
- which exceptions existed;
- what should have been logged;
- and which pathways should, in theory, have been impossible.

If those controls were unclear, bypassed or poorly documented, later reconstruction becomes harder.

> **Security assurance is partly what gives you the map you need when
> something goes wrong.**

---

## 👀 "Who Knew?" Is More Complicated Than It Sounds

Journalists naturally ask:

> **Who knew the information?**

But knowing is not binary.

Someone may:

- know the proposition explicitly;
- know one part of it;
- see a relevant document without possessing it;
- overhear a fragment of a conversation;
- know who entered a meeting;
- know when somebody travelled;
- notice a sudden change in routine;
- know which issue senior officials suddenly became interested in;
- possess two of the three facts necessary to infer the rest.

So:

```text
WHO HAD THE DOCUMENT?
```

is a narrower question than:

```text
WHO HAD ACCESS TO INFORMATION
FROM WHICH THE RELEVANT FACT
COULD BE LEARNED OR INFERRED?
```

Access is more than opening the document.

---

## 📱 Your Phone Is Part Of The Problem

People are not freestanding security objects.

They have phones.

And laptops.

And accounts.

And passwords.

And cloud services.

And calendars.

And messages.

And contacts.

And physical environments.

And other human beings standing next to them.

This is why assessing access solely by asking whether somebody was formally handed a particular classified document can miss enormous portions of the security boundary.

An inadequately secured endpoint can expose information without its owner deliberately communicating anything.

An account can expose relationships.

A calendar can expose patterns.

A message notification can expose a name.

Repeated contact can expose an association.

Location or timing information can expose activity.

None of this requires the person holding the device to be malicious.

The relevant question is therefore not simply:

> **Do we trust her?**

It is also:

> **Do we understand and control the systems through which her access
> occurs?**

Those are profoundly different propositions.

```text
PERSON DID NOT DISCLOSE INFORMATION
        ≠
PERSON'S INFORMATION ENVIRONMENT
WAS NOT EXPOSED
```

---

## 🧩 A + B + C = Oh, Fuck

There is another reason the hunt for a single leaker can become misleading.

Humans are quite good at inference.

Journalists are professionally encouraged to be good at it.

Intelligence services have also, historically, shown some enthusiasm for the activity.

Imagine that no single source reveals proposition **X**.

Instead:

- Person One reveals **A**.
- A public schedule reveals **B**.
- Person Two confirms **C**.
- Somebody notices that **D** suddenly stopped happening.
- An outside observer already understands the institutional context.

No participant necessarily says **X**.

The observer calculates:

```text
A + B + C + D = probably X
```

That is an information-security problem even though the final sensitive proposition was never directly disclosed.

It is also why compartmentation, need-to-know rules and access controls exist.

Security cannot depend upon every individual fragment remaining meaningless when combined with every other fragment available to the outside world.

An investigation built entirely around:

> **WHO TOLD THEM X?**

may therefore contain a rather fundamental problem.

**Nobody told them X.**

They worked it out.

---

## 🧅 Security Assumes Things Will Fail

A robust security architecture does not require belief in perfect humans.

People make mistakes.

Devices fail.

Credentials are stolen.

Relationships change.

Procedures are ignored.

Attackers adapt.

Someone eventually clicks something unfortunate.

Someone eventually says something in the wrong room.

Someone eventually leaves something somewhere stupid.

The purpose of layered controls is partly to prevent a single failure from becoming a catastrophic one.

That is the logic behind concepts such as:

- defence in depth;
- least privilege;
- need to know;
- compartmentation;
- endpoint security;
- access logging;
- authentication;
- personnel assurance;
- monitoring;
- and incident response.

Security therefore asks not merely whether a control failed.

It asks:

**What happened after it failed?**

If one ordinary human mistake can expose everything, the human is not the only security problem.

The architecture is.

---

## 🥸 Inside Does Not Mean Malicious

Even where an exposure pathway runs through somebody inside an institution, another distinction remains necessary:

```text
INSIDER
        ≠
MALICIOUS INSIDER
        ≠
SPY
```

An insider-associated security failure could involve:

- deliberate leaking;
- accidental disclosure;
- negligence;
- excessive privilege;
- compromised credentials;
- a compromised endpoint;
- social engineering;
- elicitation;
- coercion;
- changing personal circumstances;
- grievance;
- or entirely legitimate activity interacting badly with weak controls.

The person may be responsible for the problem.

They may also be the victim of somebody else's operation.

Those possibilities require different evidence and different responses.

---

## 🌍 There Is Also An Outside Of The House

Political reporting can become strangely closed-system.

A White House story becomes a story about:

```text
White House person
        ↓
other White House person
        ↓
journalist
        ↓
political drama
```

Sometimes that is the correct model.

But the White House does not exist in a hermetically sealed American social network.

A sensitive political environment exists inside a much larger information environment containing potential collectors with very different motives and capabilities.

Those can include:

- journalists;
- political opponents;
- activists;
- criminals;
- private intelligence actors;
- hostile individuals;
- foreign intelligence services;
- proxies and intermediaries;
- and other governments.

The existence of any such actor does **not** establish their involvement
in a particular incident.

Nor does a theoretical capability establish that it was used.

But the defensive question remains legitimate:

> **Who might plausibly want this information, and which available
> pathways could they realistically exploit?**

An investigation that assumes only Americans deliberately talking to other Americans can explain an information loss has artificially truncated its own threat model.

In periods of acute interstate confrontation, that omission becomes particularly difficult to justify.

See:

[🇮🇷 Guys, You Are In A War, Remember](./🇮🇷_guys_you_are_in_a_war_remember.md).

---

## 🦠 The Porosity Problem

This becomes especially important in large political institutions.

Information does not exist only in documents.

It exists in:

```text
people
meetings
devices
accounts
buildings
briefings
calendars
travel
relationships
metadata
behaviour
patterns
```

The larger and more interconnected the environment becomes, the more potential pathways exist through which information can move or be inferred.

Eventually the useful analytical object may cease to be:

```text
WHO LEAKED?
```

and become:

```text
WHAT WAS THE EXPOSURE ARCHITECTURE?
```

That change sounds pedantic.

It isn't.

One question investigates culpability.

The other investigates security.

A competent incident investigation may need to do both.

---

## 🔍 Finding Naughty Dave Does Not Necessarily Solve The Problem

Suppose investigators eventually find Naughty Dave.

Dave confesses.

Dave deliberately disclosed the information.

Excellent.

One question has now been answered.

But several others remain available:

- Was Dave the only pathway?
- Why could Dave access the information?
- Was that access appropriate?
- What controls should have constrained it?
- Could the information have escaped independently?
- Could another actor already have acquired it?
- Did the incident reveal other weak interfaces?
- Does removing Dave actually prevent recurrence?

This produces a useful test:

> **If Naughty Dave disappeared tomorrow, could the same security
> failure still happen?**

If the answer is yes:

**Dave was not your entire security problem.**

Finding a culpable person can resolve a personnel problem while leaving the underlying exposure architecture intact.

---

## 🕵️ Leak Investigation ≠ Security Investigation ≠ Counterintelligence Investigation

These inquiries can overlap.

They are not interchangeable.

### Leak / Culpability Investigation

```text
Who deliberately disclosed information?
What rule or law was breached?
What evidence establishes responsibility?
```

### Security Investigation

```text
What information escaped?
Which pathways existed?
Which controls failed?
What else may have been exposed?
How can recurrence be prevented?
```

### Counterintelligence Investigation

```text
Did an external intelligence actor target,
acquire, exploit or attempt to exploit
the relevant environment?
```

Evidence developed in one inquiry may matter enormously to another.

But solving one does not automatically solve the others.

```text
DOMESTIC LEAKER IDENTIFIED
        ≠
ALL EXPOSURE PATHWAYS IDENTIFIED
        ≠
FOREIGN COLLECTION EXCLUDED
```

That is why the language used at the beginning of an investigation matters.

The question defines the search space.

---

## 📰 What The Press Should Ask

When officials say they are **"looking for the leaker,"** journalists do not need to reject that explanation.

They need to avoid assuming it.

Useful questions include:

- What evidence establishes that this was a deliberate unauthorised
    disclosure?
- Which people had direct, indirect, technical, physical or contextual
    access?
- What *kind* of access did they have?
- What clearance or vetting was normally required?
- Had those requirements actually been completed?
- If not, what interim or compensating controls existed?
- What devices and communications systems were authorised?
- Were personal devices or accounts capable of interacting with the
    environment?
- Has technical compromise been investigated?
- What access and audit logs exist?
- Could metadata have exposed relevant patterns?
- Could the information have been reconstructed from several
    separately available facts?
- What physical or observational access existed?
- Which outside actors had plausible collection requirements?
- Which exposure pathways have actually been investigated?
- Has the organisation identified the exposure pathway, or merely
    identified people who knew the information?
- Most importantly: **if the alleged leaker disappeared tomorrow,
    would the same security failure still be possible?**

That final question is particularly useful.

Because if the answer is yes, finding Naughty Dave has not fixed your
security problem.

You have merely fired Dave.

---

## ⚖️ Do Not Turn Uncertainty Into Espionage Allegations

There is an equal and opposite failure mode.

Recognising that an inadequately controlled person, device or relationship could create security exposure does **not** establish that the person concerned is malicious, compromised, recruited by a foreign service or knowingly providing information to anybody.

Likewise, recognising that a foreign government possesses motive and capability does not establish that it conducted the particular operation being discussed.

Those are substantially stronger claims requiring substantially stronger evidence.

Security analysis should preserve the distinctions:

```text
possible pathway
        ↓
evidence supporting pathway
        ↓
evidence of exposure
        ↓
evidence of exploitation / compromise
        ↓
attribution
        ↓
evidence of knowing cooperation
```

Do not skip rungs because one explanation feels intuitively satisfying.

And do not correct:

> **IT WAS DEFINITELY A LEAKER**

by replacing it with:

> **IT WAS DEFINITELY A FOREIGN INTELLIGENCE SERVICE.**

That is the same analytical error wearing a more exciting hat.

> **Expanding the threat model should increase analytical caution, not decrease it.**

That distinction protects both analytical accuracy and the people being discussed.

It also makes genuine security criticism considerably harder to dismiss.

---

## 🏛️ The Actual Lesson

Sometimes there really is a snitch.

Find them.

But security cannot begin from the comforting assumption that information only moves when a human being consciously carries it from **Inside** to **Outside**.

Modern sensitive environments are networks of humans and machines.

Information can travel across either.

And sometimes nobody has to carry the secret outside at all.

The outside world already has enough pieces to put it together.

Perhaps the call really is coming from inside the house.

Perhaps Naughty Dave really did ring the newspaper.

Fine.

**Prove it.**

But before turning an information-security incident into an Agatha Christie novel, establish what actually requires explanation.

What information escaped?

Who could access, observe or infer it?

Which pathways existed?

Which controls should have prevented those pathways?

Which controls actually existed?

What evidence distinguishes deliberate disclosure from compromise, inference or some other form of exposure?

And if you remove your suspected leaker from the diagram, does the security problem disappear?

Because if it doesn't:

> **the call was never the whole fucking problem.**

---

## 🌌 Constellations  
☎️ 🕸️ 🪪 🧩 🦠 — information exposure; leak attribution; personnel assurance; aggregation risk; institutional porosity.  

---

## ✨ Stardust  
information security, personnel security, unauthorised disclosure, insider risk, aggregation risk, compartmentation, counterintelligence, attribution, press literacy

---

## 🏮 Footer

*☎️ The Call Is Coming From Inside The House* is a living node of the **Polaris Protocol**.  

It provides an introductory threat model for distinguishing deliberate leaking from the wider set of pathways through which sensitive information can become exposed, compromised or inferable. It is intended particularly as security-literacy scaffolding for reporting on political institutions.

> 📡 Cross-references:
>
> - [🦑 Security Language For Normal People](./🦑_security_language_for_normal_people.md) — *plain-language distinctions between exposure, compromise, disclosure, insider threat, espionage and attribution*
> - [🪪 Clearance Is Not A Lanyard](./🪪_clearance_is_not_a_lanyard.md) — *personnel assurance, vetting and access-control distinctions*
> - [👀 Access Is More Than Opening The Document](./👀_access_is_more_than_opening_the_document.md) — *direct, indirect, physical and contextual access*
> - [📱 The Phone Is Part Of The Security Boundary](./📱_the_phone_is_part_of_the_security_boundary.md) — *devices, accounts and communications as exposure surfaces*
> - [🧩 A Plus B Plus C Equals Classified](./🧩_a_plus_b_plus_c_equals_classified.md) — *aggregation and inferential disclosure*
> - [📞 Metadata Can Tell The Story](./📞_metadata_can_tell_the_story.md) — *intelligence value in relationships, timing and patterns*
> - [🕸️ You Do Not Need A Leaker](./🕸️_you_do_not_need_a_leaker.md) — *non-deliberate pathways to information compromise*
> - [🥸 Insider Threat Does Not Mean Spy](./🥸_insider_threat_does_not_mean_spy.md) — *insider-associated risk without premature allegations of espionage*
> - [🧅 Compartmentation Exists For A Reason](./🧅_compartmentation_exists_for_a_reason.md) — *limiting the consequences of inevitable failures*
> - [🦠 Porosity Is A Security Failure](./🦠_porosity_is_a_security_failure.md) — *systemic exposure architecture beyond individual culpability*
> - [🇮🇷 Guys, You Are In A War, Remember](./🇮🇷_guys_you_are_in_a_war_remember.md) — *the contemporary external threat and collection environment*
> - [✍️ Questions Journalists Should Actually Ask](./✍️_questions_journalists_should_actually_ask.md) — *practical reporting prompts for security incidents*
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
