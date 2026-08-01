# 🔎 Confidence Labels And Source Rules  
**First created:** 2026-08-01 | **Last updated:** 2026-08-01  
*Every claim should carry its source, confidence, limit, and review status with it.*  

---

## 🛰️ Orientation  

A cyber timeline becomes unreliable when claims detach from the evidence that originally supported them.

The common failure looks like:

```text
early claim
→ repeated reporting
→ dropped caveat
→ stronger wording
→ false certainty
```

This node sets the minimum source and confidence rules for the *🇮🇷 Data Wars: IRGC Edition* pack.

The governing structure is:

```text
CLAIM
→ SOURCE
→ CONFIDENCE
→ LIMIT
→ REVIEW
```

No element should be removed merely because the claim has become familiar.

Familiarity is not corroboration.

Repetition is not verification.

---

## 🎚️ Confidence Labels  

This pack uses six principal labels.

### Confirmed  

Use **confirmed** where the public record supports a high-confidence finding.

That may include:

- a clear government attribution;
- a coordinated cyber-agency advisory;
- an indictment;
- a sanctions notice;
- a court filing;
- an affected institution's verified account;
- or detailed technical research with strong supporting evidence.

Confirmed does not mean absolute certainty.

It means the evidence available publicly is strong enough to support the claim without a material caveat changing its basic meaning.

### Probable  

Use **probable** where several credible indicators point in the same direction, but the public case remains incomplete.

Possible support includes:

- infrastructure reuse;
- operator overlap;
- known tooling;
- matching victimology;
- several independent technical assessments;
- or credible official suspicion.

Probable must not be rewritten as confirmed.

### Suspected  

Use **suspected** where there is a credible basis for concern but significant uncertainty remains.

Possible support includes:

- preliminary official assessment;
- limited technical overlap;
- incomplete intelligence reporting;
- a credible leak;
- or a developing pattern.

Suspected is an analytical status.

It is not an accusation stated as fact.

### Actor-Claimed  

Use **actor-claimed** where a person or group has publicly claimed responsibility.

That label says only that the claim exists.

It does not establish:

- that the claimant carried out the attack;
- that the claimed impact is accurate;
- that the actor is who it says it is;
- or that a state directed the operation.

### Unattributed  

Use **unattributed** where no credible public attribution has been established.

An unattributed incident may still belong in the pack because of:

- operational effect;
- timing;
- sector;
- location;
- target selection;
- or possible relationship to a wider pattern.

Unattributed does not mean irrelevant.

It also does not mean Iranian.

### Excluded  

Use **excluded** where an incident no longer meets the pack's threshold.

Reasons may include:

- unsupported reporting;
- false or exaggerated actor claims;
- negligible operational consequence;
- a clear unrelated cause;
- duplication;
- or later evidence showing the incident falls outside the scope.

Exclusion should be recorded, not silently erased.

---

## 🧱 The Four-Part Claim Rule  

Every material claim should preserve:

```text
CLAIM:
SOURCE:
CONFIDENCE:
LIMIT:
```

Example:

```text
CLAIM:
Iran-linked actors may have targeted the payment platform.

SOURCE:
Preliminary official assessment and two independent technical reports.

CONFIDENCE:
Suspected.

LIMIT:
No definitive public attribution; ordinary criminal activity remains a credible alternative.
```

The limit is not decorative.

It defines what the evidence does not establish.

Without it, a careful claim can become an overstatement when copied.

---

## 🔗 Source Hierarchy  

Sources should be assessed by what they can actually establish.

### Tier One — Primary And Official Sources  

Examples include:

- official advisories;
- court filings;
- indictments;
- sanctions documents;
- affected institutions;
- parliamentary statements;
- regulator notices;
- technical incident reports;
- and direct records.

These are generally strongest for establishing:

- what was officially said;
- what action was taken;
- what systems were affected;
- and what attribution was publicly adopted.

They may still be incomplete or politically framed.

### Tier Two — Independent Technical Research  

Examples include:

- reputable cyber-security research;
- malware analysis;
- infrastructure mapping;
- incident-response findings;
- and peer-reviewed or methodologically transparent research.

These are strongest where they show:

- technical linkage;
- operator behaviour;
- infrastructure reuse;
- malware families;
- or campaign patterns.

Technical expertise does not automatically establish state direction.

### Tier Three — Reputable Reporting  

Examples include established news organisations with:

- named sources;
- direct access;
- documentary support;
- or several independently corroborated accounts.

These may be strong for:

- chronology;
- political context;
- institutional response;
- and reporting what officials or investigators believe.

They remain secondary unless they publish the underlying evidence.

### Tier Four — Specialist Commentary And Open-Source Analysis  

Examples include:

- specialist newsletters;
- researchers;
- open-source intelligence accounts;
- sector analysts;
- and professional commentary.

These may be useful for:

- interpretation;
- comparison;
- discovery;
- and identifying leads.

They should not be treated as stronger than the evidence they cite.

### Tier Five — Actor Claims, Anonymous Posts, And Unverified Material  

Examples include:

- Telegram claims;
- social-media posts;
- anonymous leaks;
- screenshots;
- paste sites;
- and claims from alleged attackers.

These may be relevant to messaging or chronology.

They are weak evidence of responsibility or impact unless independently corroborated.

---

## 📰 Repetition Is Not Corroboration  

Several reports may rely on one original source.

The record should distinguish:

```text
NUMBER OF ARTICLES
≠
NUMBER OF INDEPENDENT SOURCES
```

For each claim, identify:

```text
ORIGINAL SOURCE:
FIRST REPORT:
LATER REPORTS:
INDEPENDENT CORROBORATION:
```

A claim repeated by ten outlets remains single-sourced where all ten trace back to the same advisory, anonymous official, vendor report, or actor statement.

The source chain matters more than circulation volume.

---

## 🧪 Match The Source To The Claim  

A source may be strong for one proposition and weak for another.

For example:

An affected company may be authoritative about:

- service disruption;
- recovery;
- and systems affected.

It may not be authoritative about:

- who carried out the attack;
- whether a state directed it;
- or the wider strategic purpose.

A cyber-security company may be strong on:

- malware;
- infrastructure;
- and technical overlap.

It may be weaker on:

- legal responsibility;
- political intent;
- or the final customer.

An actor claim may establish:

- that a group wants public credit.

It does not establish:

- that the group caused the incident.

Every source should be used only for the proposition it can reasonably support.

---

## 🕸️ Separate Attribution Layers  

Where possible, attribution should be broken into layers:

```text
IMMEDIATE OPERATOR:
TOOLING OR INFRASTRUCTURE:
INTERMEDIARY:
BUYER OR CUSTOMER:
STATE LINK:
FINAL BENEFICIARY:
```

Do not assume these are the same actor.

A criminal operator may sell access.

A proxy may receive tasking.

A state-linked buyer may enter the chain later.

A state may benefit without directing the original attack.

The confidence label should attach to each layer separately.

---

## 📅 Review Dates Are Mandatory  

Cyber attribution changes.

Every live incident should include:

```text
LAST REVIEWED:
NEXT REVIEW:
REVIEW TRIGGER:
```

Useful review triggers include:

- a new government statement;
- a technical report;
- an indictment;
- a sanctions notice;
- a correction;
- a withdrawn actor claim;
- evidence of data publication;
- or a change in operational impact.

A claim without a review date can become stale while still appearing current.

---

## 🔄 Confidence Must Be Able To Move Both Ways  

Confidence may increase where new evidence shows:

- matching infrastructure;
- repeated operator overlap;
- payment or communications links;
- recovered tasking;
- independent corroboration;
- official attribution;
- or later use by a known state-linked actor.

Confidence should decrease where:

- technical indicators are generic;
- the source withdraws the claim;
- timestamps do not match;
- the actor exaggerated impact;
- ordinary criminal activity fits better;
- or the original reporting was based on one weak source.

A robust method must permit:

```text
suspected → probable → confirmed
```

and also:

```text
probable → suspected → excluded
```

The second path is just as important.

---

## ⚠️ Timing Is Not Attribution  

An incident occurring during military escalation may justify scrutiny.

It does not prove causation.

Timing should be recorded as:

```text
CONTEXT:
Occurred during escalation.

INFERENCE:
May be relevant to campaign timing.

LIMIT:
No direct evidence yet links the incident to the escalation.
```

Do not convert chronology into proof.

Do not ignore chronology either.

---

## 🎭 Branding Is Not Identity  

A group may use:

- Iranian symbols;
- IRGC language;
- patriotic slogans;
- anti-Western rhetoric;
- or political imagery.

That may reveal the message the group wants to send.

It does not prove:

- nationality;
- organisational identity;
- state control;
- technical authorship;
- or operational success.

Record the branding as evidence of presentation.

Do not treat it as evidence of command.

---

## 🤐 Silence Is Not A Denial  

Where an authority says:

> We can neither confirm nor deny.

the record should not convert that into:

> Officials denied involvement.

Where an authority says:

> We do not comment on operational matters.

the record should not convert that into:

> No national-security concern exists.

NCND means the authority has not publicly answered the question.

It may protect legitimate interests.

It may also leave a harmful gap.

The source record should preserve exactly what was and was not said.

---

## 🧍 Person-Centred Harm Requires Its Own Evidence  

Technical recovery does not establish personal recovery.

Where data concerns individuals, the record should separately assess:

```text
DATA EXPOSED:
PEOPLE AFFECTED:
NOTIFICATION:
CONTINUING RISK:
PROTECTION OFFERED:
DOMESTIC REUSE OR AMPLIFICATION:
```

A source saying:

> Systems are restored.

does not establish:

> Affected people are safe.

Those are different claims.

They require different evidence.

---

## 🧾 Minimum Incident Record  

Every incident should include:

```text
DATE:
COUNTRY:
SECTOR:
AFFECTED BODY:
EVENT:
OPERATIONAL EFFECT:
DATA EFFECT:
CLAIMED ACTOR:
OFFICIAL ATTRIBUTION:
OTHER ATTRIBUTION:
CONFIDENCE:
SOURCE TIER:
ORIGINAL SOURCE:
INDEPENDENT CORROBORATION:
LIMIT:
RIVAL EXPLANATIONS:
LAST REVIEWED:
NEXT REVIEW:
CORRECTION STATUS:
```

Where a field is unknown, write:

```text
UNKNOWN
```

Do not leave ambiguity hidden in a blank field.

---

## 🚫 Common Source Errors  

Avoid:

- counting repeated articles as independent confirmation;
- using a headline where the underlying report is available;
- citing an actor claim as proof of responsibility;
- treating technical similarity as proof of state direction;
- treating anonymous official suspicion as confirmed attribution;
- treating NCND as denial;
- treating absence of public attribution as proof of irrelevance;
- omitting the limit from a repeated claim;
- and allowing old confidence labels to survive after the evidence changes.

These errors make the timeline look cleaner than the evidence really is.

That is not strength.

It is distortion.

---

## 🧭 Working Rule  

The working rule is:

> Every material claim must carry its source, confidence, limit, and review status with it.

The method is simple:

```text
state what happened
name who says so
show how strong the support is
state what remains unknown
record what would change the assessment
```

That is enough to preserve uncertainty without collapsing into vagueness.

---

## 🌌 Constellations  

🔎 🎚️ 🔗 🧪 🔄 — source discipline; confidence; provenance; evidence; review.

## ✨ Stardust  

confidence labels, source rules, provenance, corroboration, attribution, review dates, corrections, cyber reporting, evidentiary limits

---

## 🏮 Footer  

*🔎 Confidence Labels And Source Rules* is a living node of the **Polaris Protocol**.  
It defines the minimum evidentiary and provenance standards for claims included in the *🇮🇷 Data Wars: IRGC Edition* pack.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *graded attribution*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *newsroom application*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *layered attribution*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *live incident chronology*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-01_
