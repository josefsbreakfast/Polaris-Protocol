# ☎️ The Call Is Coming From Inside The House
**First created:** 2026-08-21 | **Last updated:** 2026-08-21  
*Why “who leaked it?” is only one of several possible explanations for information escaping a supposedly secure environment.*

---

## 🛰️ Orientation

When sensitive information appears somewhere it should not, there is an extremely tempting story:

**Someone leaked it. Find the leaker.**

Sometimes that is exactly what happened.

Sometimes it is not.

Information can leave a secure environment because somebody deliberately disclosed it. It can also become exposed because a device was compromised, an account was inadequately protected, somebody had inappropriate access, a conversation was overheard, metadata revealed a pattern, security controls were inconsistently applied, or several individually unremarkable pieces of information were assembled by somebody outside the system.

Those are different security problems.

Treating all of them as **“a leak”** can therefore produce a particularly unfortunate investigation: an organisation becomes extremely good at hunting for a person who may not exist while leaving the pathway by which the information escaped completely intact.

This folder exists because journalists need enough security literacy to ask the second question.

Not merely:

> **Who told someone?**

But:

> **How could this information have become available?**

Those questions overlap.

They are not the same question.

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

Naughty Dave certainly exists as a category of security problem. Governments really do experience deliberate unauthorised disclosures. Insider threats really do exist. People really do mishandle information intentionally.

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

The information becomes available because somebody can see, hear or otherwise encounter something they should not.

### Aggregation

```text
A + B + C + context → sensitive conclusion
```

Nobody necessarily discloses the sensitive conclusion at all.

Someone else reconstructs it.

These pathways require different investigations and different mitigations.

That is why **“who leaked?” should not silently become “how was this compromised?”**

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

> **Do we understand and control the systems through which her access occurs?**

Those are profoundly different propositions.

---

## 🧩 A + B + C = Oh, Fuck

There is another reason the hunt for a single leaker can become misleading.

Humans are quite good at inference.

Journalists are professionally encouraged to be good at it.

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

## 📰 What The Press Should Ask

When officials say they are **“looking for the leaker,”** journalists do not need to reject that explanation.

They need to avoid assuming it.

Useful questions include:

- What evidence establishes that this was a deliberate unauthorised disclosure?
- Which people had access to the information or environment concerned?
- What *kind* of access did they have?
- What clearance or vetting was normally required?
- Had those requirements actually been completed?
- If not, what interim or compensating controls existed?
- What devices and communications systems were authorised?
- Were personal devices or accounts capable of interacting with the environment?
- Has technical compromise been investigated?
- What access and audit logs exist?
- Could the information have been reconstructed from several separately available facts?
- What physical or observational access existed?
- Has the organisation identified the exposure pathway, or merely identified people who knew the information?
- Most importantly: **if the alleged leaker disappeared tomorrow, would the same security failure still be possible?**

That final question is particularly useful.

Because if the answer is yes, finding Naughty Dave has not fixed your security problem.

You have merely fired Dave.

---

## ⚖️ Do Not Turn Uncertainty Into Espionage Allegations

There is an equal and opposite failure mode.

Recognising that an inadequately controlled person, device or relationship could create security exposure does **not** establish that the person concerned is malicious, compromised, recruited by a foreign service or knowingly providing information to anybody.

Those are substantially stronger claims requiring substantially stronger evidence.

Security analysis should preserve the distinction:

```text
possible exposure pathway
        ≠
evidence of compromise
        ≠
evidence of deliberate disclosure
        ≠
evidence of espionage
```

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

So when sensitive information unexpectedly appears in public and everybody begins looking furiously for the person responsible, there is one additional possibility worth keeping on the whiteboard:

**the call may already be coming from inside the house.**

---

## 🌌 Constellations

☎️ 🕸️ 🧩 🧅 🦠 — information security; personnel assurance; technical compromise; aggregation risk; institutional porosity.

## ✨ Stardust

information security, personnel security, security clearance, unauthorised disclosure, insider risk, attack surface, aggregation risk, compartmentation, endpoint security, information exposure

---

## 🏮 Footer

*☎️ The Call Is Coming From Inside The House* is a living node of the **Polaris Protocol**.  
It provides an introductory threat-model for distinguishing deliberate leaking from the wider set of pathways through which sensitive information can become exposed, compromised or inferable. It is intended particularly as security-literacy scaffolding for reporting on political institutions.

> 📡 Cross-references:
>
> - [🪪 Clearance Is Not A Lanyard](./🪪_clearance_is_not_a_lanyard.md) — *personnel assurance, vetting and access-control distinctions*
> - [📱 The Phone Is Part Of The Security Boundary](./📱_the_phone_is_part_of_the_security_boundary.md) — *devices, accounts and communications as exposure surfaces*
> - [🕸️ You Do Not Need A Leaker](./🕸️_you_do_not_need_a_leaker.md) — *non-deliberate pathways to information compromise*
> - [🧩 A Plus B Plus C Equals Classified](./🧩_a_plus_b_plus_c_equals_classified.md) — *aggregation and inferential disclosure*
> - [❓ Questions Journalists Should Actually Ask](./❓_questions_journalists_should_actually_ask.md) — *practical reporting prompts for security incidents*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-21_
