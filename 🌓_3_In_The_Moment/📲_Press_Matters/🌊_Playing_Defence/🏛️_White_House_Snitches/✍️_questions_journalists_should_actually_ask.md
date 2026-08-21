# ✍️ Questions Journalists Should Actually Ask
**First created:** 2026-08-21 | **Last updated:** 2026-08-21  
*A practical reporting checklist for separating access, vulnerability, mechanism, intent and attribution when a political security story starts collapsing into “who leaked?”*

---

## 🛰️ Orientation

You do not need to become a counterintelligence officer to report a security story competently.

You do need to stop collapsing several different questions into:

> **WHO LEAKED?**

That question may be appropriate.

It is not the whole investigation.

A useful reporting sequence is:

```text
WHAT HAPPENED?
        ↓
WHAT ACCESS EXISTED?
        ↓
WHAT CONTROLS SHOULD HAVE EXISTED?
        ↓
WHAT CONTROLS ACTUALLY EXISTED?
        ↓
WHAT MECHANISMS COULD PRODUCE THE OUTCOME?
        ↓
WHAT DOES THE EVIDENCE SUPPORT?
        ↓
WHO, IF ANYONE, CAN BE ATTRIBUTED RESPONSIBILITY?
```

This node is the working checklist for the cluster.

Open it while reporting.

Ask the boring questions.

The boring questions are where an astonishing amount of the story lives.

---

## 🧾 1. Establish What Actually Happened

Before explaining the incident, establish the incident.

Ask:

- What information became available?
- To whom did it become available?
- When?
- How sensitive was it?
- Was it formally classified, otherwise protected, operationally sensitive, or simply politically embarrassing?
- What is directly confirmed?
- What has been reported by unnamed sources?
- What remains inference?
- Has deliberate unauthorised disclosure actually been established?
- Or has the reporting established only that information appeared somewhere unexpected?

Keep the distinction visible:

```text
INFORMATION APPEARED OUTSIDE
        ≠
INSIDER DELIBERATELY LEAKED IT
```

See [☎️ The Call Is Coming From Inside The House](./☎️_the_call_is_coming_from_inside_the_house.md).

---

## 👀 2. Map Access Before Deciding Who Had It

Do not reduce access to:

> **Who could open the document?**

Ask instead:

- Who had formal access?
- Who had technical access?
- Who had physical access?
- Who had observational access?
- Who had administrative access?
- Who had contextual access?
- Who could see schedules, visitors, movements or meeting patterns?
- Which roles routinely sat close to the relevant information environment?
- Did anyone possess fragments that became more revealing when combined?

A person can lack permission to retrieve a particular file while still occupying an information-rich position.

```text
NO DOCUMENT ACCESS
        ≠
NO RELEVANT ACCESS
```

See [👀 Access Is More Than Opening The Document](./👀_access_is_more_than_opening_the_document.md).

---

## 🪪 3. Establish The Assurance Model

If clearance or vetting is part of the story, ask what it was supposed to accomplish.

Do not treat clearance as a ceremonial badge reading:

> **GOVERNMENT SAYS THIS PERSON IS GOOD.**

Ask:

- What vetting or clearance was normally required for the role?
- Had it been completed?
- If not, why not?
- Was the person operating under an interim arrangement?
- What access restrictions applied?
- What compensating controls existed?
- Were escorts, device restrictions or other safeguards used where appropriate?
- Who authorised the exception?
- Who accepted the residual risk?
- Was the arrangement time-limited?
- Was it reviewed?
- Did temporary become normal?

And keep this distinction intact:

```text
INCOMPLETE CLEARANCE
        ≠
SPY

INCOMPLETE CLEARANCE
        =
ASK WHAT ASSURANCE EXISTED INSTEAD
```

See [🪪 Clearance Is Not A Lanyard](./🪪_clearance_is_not_a_lanyard.md).

---

## 📱 4. Ask About Devices And Accounts

Trusting the human does not secure the endpoint.

Ask, at an appropriately non-operational level:

- What devices were authorised for the role?
- What accounts were authorised?
- Were personal devices or accounts capable of interacting with the work environment?
- Were official and personal systems appropriately separated?
- Were relevant devices managed within the expected security regime?
- Has device compromise been considered?
- Has account or credential compromise been considered?
- What access and authentication logs exist?
- Can suspicious activity actually be attributed to the human, rather than merely to a credential associated with them?
- Did devices physically enter sensitive environments?
- What information other than message content could those systems expose?

The basic rule:

```text
TRUSTWORTHY PERSON
        ≠
SECURE DEVICE

LEGITIMATE CREDENTIAL
        ≠
LEGITIMATE HUMAN ACTIVITY
```

See [📱 The Phone Is Part Of The Security Boundary](./📱_the_phone_is_part_of_the_security_boundary.md).

---

## 🧩 5. Test Whether The Information Could Have Been Reconstructed

Ask whether anybody actually had to disclose the final proposition.

- What component facts supported the conclusion?
- Which were already public?
- Which were observable?
- Which were available administratively?
- Which were available to different people?
- Could metadata supply part of the picture?
- What contextual knowledge would an informed observer already possess?
- Could several individually limited fragments compose into the sensitive conclusion?
- Is there evidence that the final proposition itself was ever directly communicated?

Keep the mechanism open:

```text
A + B + C + CONTEXT
        ↓
X
```

Nobody necessarily has to say X.

See [🧩 A Plus B Plus C Equals Classified](./🧩_a_plus_b_plus_c_equals_classified.md).

---

## 📞 6. Separate Metadata From Message Content

If communications records form part of the story, ask what they actually establish.

- Do the records show contact?
- Timing?
- Duration?
- Frequency?
- Sequence?
- A change from baseline?
- Do they reveal content?
- What alternative explanations fit the same pattern?
- What contextual information is being combined with the records?
- What independent evidence corroborates the interpretation?

Do not let the grammar upgrade the evidence:

```text
A CONTACTED B
        ≠
A TOLD B X

CONTACT OCCURRED BEFORE EVENT
        ≠
CONTACT CAUSED EVENT
```

Metadata can be extremely informative.

It does not explain itself.

See [📞 Metadata Can Tell The Story](./📞_metadata_can_tell_the_story.md).

---

## 🕸️ 7. Establish Mechanism Before Attribution

Once the outcome is clear, ask how it could have occurred.

Keep several pathways on the board:

```text
deliberate disclosure

accidental disclosure

technical compromise

credential compromise

physical observation

metadata

aggregation / inference

mixed pathway
```

Then ask:

- What evidence supports deliberate human disclosure?
- What evidence supports technical compromise?
- Were physical or observational pathways examined?
- Was reconstruction from fragments considered?
- Could several mechanisms have interacted?
- What logs or records distinguish between them?
- What plausible pathways have been excluded?
- On what evidence?
- Has the mechanism actually been established?

Do not start with the suspect and reverse-engineer the mechanism.

```text
OUTCOME
        ↓
MECHANISM
        ↓
EVIDENCE
        ↓
ATTRIBUTION
```

See [🕸️ You Do Not Need A Leaker](./🕸️_you_do_not_need_a_leaker.md).

---

## 🥸 8. Be Precise About People

Words such as **insider threat**, **compromised**, **targeted**, **asset** and **spy** are not interchangeable.

Ask:

- What does the institution mean by **insider threat** in this context?
- Is the concern intentional, unintentional or undetermined?
- Did the person merely possess legitimate access?
- Is there evidence they created an exposure?
- Is there evidence they acted deliberately?
- Is there evidence an outside actor targeted them?
- If so, is there evidence the targeting succeeded?
- Is there evidence of knowing cooperation?
- Is there evidence of deliberate unauthorised disclosure?
- What evidence supports the stronger allegation being made?

Preserve the ladder:

```text
ACCESS
        ≠
EXPOSURE

EXPOSURE
        ≠
INTENT

TARGETED
        ≠
COMPROMISED

COMPROMISED
        ≠
KNOWING COOPERATION

KNOWING COOPERATION
        ≠
ESPIONAGE ESTABLISHED
```

See [🥸 Insider Threat Does Not Mean Spy](./🥸_insider_threat_does_not_mean_spy.md).

---

## 🍯 9. Do Not Cast The Spy Movie

Before treating proximity as mysterious, establish the person's actual job.

Ask:

- What is the person's formal role?
- What proximity is ordinary for that role?
- What access is structurally produced by the job?
- Is apparently unusual behaviour actually occupationally normal?
- Is professional support labour being narrated as personal devotion?
- Is sexual or romantic framing supported by evidence?
- Is a feminised role being over-personalised while its professional access is under-analysed?
- Is cultural familiarity being mistaken for security assurance?
- Is foreignness being mistaken for threat?
- Is there evidence of targeting, cultivation or recruitment?
- Or is the reporting simply assigning somebody a character in a spy story?

For executive support in particular:

> **If an executive assistant repeatedly follows the executive, first check whether following the executive is literally part of the job.**

Then ask the security question:

> **What access does that job create, and were the controls appropriate to it?**

```text
OCCUPATIONAL PROXIMITY
        ≠
PERSONAL INTIMACY

PERSONAL INTIMACY
        ≠
CULTIVATION

ATTRACTIVE
        ≠
HONEYPOT
```

See [🍯 Honeypots Are Not Magic](./🍯_honeypots_are_not_magic.md).

---

## 🦠 10. Ask Whether The Architecture Is Porous

An incident may reveal a wider condition.

Ask:

- What security boundary was supposed to exist?
- What could actually cross it?
- Was this one exceptional failure or part of a recurring pattern?
- Were exceptions routinely granted?
- Did temporary arrangements become permanent?
- Were personal and official environments bleeding together?
- Were access rights broader than necessary?
- Did different security teams understand the arrangement in the same way?
- Who owned the joins between personnel, devices, accounts and physical security?
- Who accepted residual risk?
- Were controls operating in practice or merely existing on paper?
- Would removing the suspected person actually eliminate the pathway?
- Could essentially the same failure happen again tomorrow?

That last pair matters.

```text
REMOVE PERSON
        +
PATHWAY SURVIVES
        =
YOU HAVE NOT FIXED THE SECURITY PROBLEM
```

See [🦠 Porosity Is A Security Failure](./🦠_porosity_is_a_security_failure.md).

---

## 🇮🇷 11. Put The External Threat Environment Back In The Story

Security incidents do not occur in laboratory conditions.

Ask:

- What geopolitical and counterintelligence environment existed at the relevant time?
- Which capable external actors would plausibly value the information?
- What would they want to know?
- What collection surfaces would be relevant?
- Had military or political developments altered the threat environment?
- Were technical and foreign-intelligence acquisition pathways considered?
- Were Iran, Russia, China and other relevant actors assessed according to their own capabilities and interests rather than flattened into one interchangeable category?
- What evidence exists of actual attempted exploitation?
- What evidence exists of successful compromise?
- What evidence supports attribution to any particular actor?

And keep the firewall enormous:

```text
MOTIVE
        ≠
OPERATION

CAPABILITY
        ≠
USE

THREAT ENVIRONMENT
        ≠
ATTRIBUTION
```

Asking whether a foreign-intelligence pathway was considered is **not** accusing a foreign state.

It is asking whether the threat model contained threats.

See [🇮🇷 Guys, You Are In A War. Remember?](./🇮🇷_guys_you_are_in_a_war_remember.md).

---

## 🛡️ 12. Ask Who Actually Assessed The Security

A political institution may contain plenty of people with opinions about security.

That is not the same thing as having the relevant security expertise in the decision loop.

Ask:

- Which personnel-security professionals assessed the arrangement?
- Which protective-security professionals assessed it?
- Which technical-security or cybersecurity professionals assessed it?
- Was counterintelligence advice relevant?
- What did the appropriate experts recommend?
- Were their recommendations followed?
- If not, who overrode them?
- Was that override documented?
- Was residual risk formally accepted?
- Did the people identifying risk have enough authority to require mitigation?
- Were legacy security principles being combined with current technical expertise?
- Has institutional memory about earlier failure modes been retained?

The important governance distinction is:

```text
SECURITY TEAM WARNED
        ≠
SECURITY CONTROL IMPLEMENTED
```

Expertise becomes decorative if nobody has to listen to it.

See [🛡️ Useful Old-School Defence Expertise](./🛡️_useful_old_school_defence_expertise.md).

---

## ⚖️ 13. Label The Evidence

Every national-security story benefits from an explicit evidential ladder.

Use one.

For example:

```text
CONFIRMED
directly established by reliable evidence

SUPPORTED
multiple pieces of evidence point in this direction

PLAUSIBLE
consistent with known facts and mechanisms

POSSIBLE
cannot presently be excluded

SPECULATIVE
requires assumptions not yet supported by evidence
```

The exact vocabulary can vary.

The discipline should not.

Ask of every major proposition:

> **Which rung is this actually on?**

Then write accordingly.

Do not convert:

```text
POSSIBLE
```

into:

```text
OFFICIALS FEAR
```

and then allow the next article to convert:

```text
OFFICIALS FEAR
```

into:

```text
THE SECURITY BREACH
```

without somebody producing evidence in between.

Language can accidentally launder uncertainty.

Do not let it.

---

## 🗣️ 14. Ask Officials To Define Their Nouns

Security language can sound much more precise than it is.

If somebody says:

- leak;
- breach;
- compromise;
- classified;
- clearance;
- access;
- insider threat;
- surveillance;
- hack;
- foreign actor;
- asset;
- intelligence;
- or secure;

ask what they mean **in this case**.

Useful follow-ups include:

> What specific mechanism are you describing?

> Is that a formal technical term here or ordinary language?

> What evidence supports that description?

> What stronger claim should readers *not* infer from it?

This is particularly important when an official term and its ordinary-language meaning diverge.

See [🦑 Security Language For Normal People](./🦑_security_language_for_normal_people.md).

---

## 🔬 15. Separate The Person, The Pathway And The Institution

A good security story may contain three different accountability questions.

### The person

Did somebody make an error, misuse access or deliberately disclose information?

### The pathway

What technical, physical, administrative or informational mechanism allowed the exposure?

### The institution

Why did the architecture permit the incident to have the consequences it did?

These can produce different answers.

```text
PERSON RESPONSIBLE
        ≠
PERSON SOLELY RESPONSIBLE

TECHNICAL FAILURE
        ≠
NO GOVERNANCE FAILURE

NO MALICIOUS INSIDER
        ≠
NO SECURITY FAILURE
```

Do not let the most visible human absorb every institutional question.

And do not let institutional weakness erase evidence of individual wrongdoing where it exists.

Both directions are lazy.

---

## 🚨 16. Ask What Would Fix It

A useful reporting question is:

> **If the institution did exactly what it says it is doing now, would the same class of incident still be possible?**

If the answer is yes, the remedy may be addressing the wrong thing.

Ask:

- Has access changed?
- Have devices or accounts changed?
- Have exceptions been reviewed?
- Has compartmentation changed?
- Has logging improved?
- Has the assurance process changed?
- Has somebody been given ownership of previously unmanaged seams?
- Has the external threat model changed?
- Has security advice gained more authority?
- Or has the institution simply identified somebody to blame?

Accountability matters.

So does remediation.

A security investigation that produces a villain but leaves the pathway open has produced a sequel.

---

## 📋 The One-Page Version

If you remember nothing else, keep these beside the keyboard:

1. **What exactly happened?**
2. **What kinds of access actually existed?**
3. **What assurance was required, and what was actually completed?**
4. **What controls operated in practice?**
5. **Could a device, account or credential be part of the mechanism?**
6. **Could fragments, metadata or observation reconstruct the information?**
7. **Has the mechanism been established, or merely assumed?**
8. **What does the evidence actually establish about intent and cooperation?**
9. **Would removing the suspected person fix the pathway?**
10. **What external threat environment was relevant?**
11. **Which security professionals assessed the arrangement, and were they listened to?**
12. **Which claims are confirmed, supported, plausible, possible or speculative?**

And then one final question:

> **What fact would make me change the story I currently think I am telling?**

If the answer is **nothing**, you are no longer investigating.

---

## 🧿 The Actual Lesson

Journalists do not need access to classified intelligence to improve security reporting.

They need better conceptual hygiene.

Do not confuse:

```text
access
with
misuse

vulnerability
with
exploitation

targeting
with
compromise

compromise
with
cooperation

information outcome
with
disclosure mechanism

threat assessment
with
attribution
```

Ask what happened.

Map the access.

Establish the controls.

Test the mechanisms.

Label the evidence.

Then attribute responsibility where the evidence supports it.

And please, for the love of every exhausted security professional watching the story unfold:

> **“Who leaked?” is one question.**

> **It is not the entire field of information security.**

---

## 🌌 Constellations  
✍️ ☎️ 🪪 🕸️ 🛡️ — security reporting; access and assurance; mechanism testing; attribution discipline; defensive accountability.

## ✨ Stardust  
journalism, information security, security reporting, counterintelligence, access control, personnel assurance, incident investigation, attribution, evidential discipline

---

## 🏮 Footer  

*✍️ Questions Journalists Should Actually Ask* is a living node of the **Polaris Protocol**.  
It converts the White House Snitches cluster into a practical reporting workflow for distinguishing information outcomes, access, assurance, technical and human mechanisms, external threat context, evidential confidence and attribution. It is intended as a desk-side checklist: enough security literacy to ask better questions without pretending journalism and counterintelligence are the same profession.

> 📡 Cross-references:
>
> - [☎️ The Call Is Coming From Inside The House](./☎️_the_call_is_coming_from_inside_the_house.md) — *the cluster-level distinction between information appearing outside a protected environment and the mechanism that produced that outcome*  
> - [🦑 Security Language For Normal People](./🦑_security_language_for_normal_people.md) — *plain-language distinctions for security terms that reporting can otherwise accidentally collapse*  
> - [🪪 Clearance Is Not A Lanyard](./🪪_clearance_is_not_a_lanyard.md) — *questions about vetting, assurance, interim arrangements and compensating controls*  
> - [👀 Access Is More Than Opening The Document](./👀_access_is_more_than_opening_the_document.md) — *formal, technical, physical, observational, administrative and contextual access*  
> - [📱 The Phone Is Part Of The Security Boundary](./📱_the_phone_is_part_of_the_security_boundary.md) — *devices, accounts and credentials as security surfaces distinct from the intentions of their legitimate user*  
> - [🧩 A Plus B Plus C Equals Classified](./🧩_a_plus_b_plus_c_equals_classified.md) — *aggregation and reconstruction of sensitive conclusions from individually limited fragments*  
> - [📞 Metadata Can Tell The Story](./📞_metadata_can_tell_the_story.md) — *how communication structure can inform an investigation without establishing message content or causation*  
> - [🕸️ You Do Not Need A Leaker](./🕸️_you_do_not_need_a_leaker.md) — *mechanism-first analysis of deliberate, accidental, technical, observational and inferential pathways*  
> - [🥸 Insider Threat Does Not Mean Spy](./🥸_insider_threat_does_not_mean_spy.md) — *the evidential distinctions between insider status, exposure, intent, targeting, compromise and espionage*  
> - [🍯 Honeypots Are Not Magic](./🍯_honeypots_are_not_magic.md) — *why occupational proximity and human exploitation should not be reduced to a cinematic seduction narrative*  
> - [🦠 Porosity Is A Security Failure](./🦠_porosity_is_a_security_failure.md) — *how recurring exceptions and weak seams turn a discrete incident into an institutional security condition*  
> - [🇮🇷 Guys, You Are In A War. Remember?](./🇮🇷_guys_you_are_in_a_war_remember.md) — *the external threat environment and the boundary between threat modelling and attribution*  
> - [🛡️ Useful Old-School Defence Expertise](./🛡️_useful_old_school_defence_expertise.md) — *the institutional and technical expertise needed to turn identified risk into actual defensive control*  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-08-21_
