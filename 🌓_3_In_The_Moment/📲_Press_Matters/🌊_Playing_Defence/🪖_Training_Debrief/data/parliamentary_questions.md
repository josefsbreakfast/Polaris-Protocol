# 🏛️ Parliamentary Questions
**First created:** 2026-09-07 | **Last updated:** 2026-09-08  
*Governance chronology for parliamentary scrutiny of training, readiness, affordability and ministerial awareness.*

> **Status:** Research infrastructure / governance chronology  
> **Cluster:** `🪖_Training_Debrief`  
> **Purpose:** Track parliamentary scrutiny relevant to Army training, Defence readiness, affordability, implementation of the Strategic Defence Review and Defence Investment Plan, and the ministerial decision chain surrounding the 2026 collective-training reductions.

---

## 🧭 What This File Is

This file records parliamentary questions, answers, statements and committee interventions relevant to the current training dispute and its wider policy context.

It is designed to answer:

- When did Parliament begin asking about training reductions?
- How specific were those questions?
- What did ministers say in response?
- Did answers become more or less specific over time?
- What commitments had already been made publicly?
- Which ministers were responsible for answering at different points?
- Which issues had already become salient before the September 2026 reporting?
- What information can reasonably be inferred to have entered the ministerial/parliamentary system?

This file does **not** assume that:

- a minister personally knew every fact contained within their department;
- the person answering a question made the underlying decision;
- an evasive answer proves concealment;
- a parliamentary question proves the underlying allegation;
- holding office establishes knowledge.

The purpose is to reconstruct the public governance trail.

---

## 🎯 Priority Questions

The immediate priorities are:

1. Army collective training.
2. Royal Navy training.
3. RAF training.
4. Exercise reductions.
5. Readiness.
6. Defence affordability.
7. SDR 2025 implementation.
8. Defence Investment Plan implementation.
9. Training modernisation / synthetic training.
10. Training estate.
11. Personnel availability.
12. Treasury–MOD funding discussions.
13. Service-specific savings.
14. Risk acceptance.
15. Ministerial awareness.

---

## 🧱 Source Types

Include:

### Written Parliamentary Questions

Record:

- question number;
- date tabled;
- MP/peer;
- department;
- minister answering;
- question wording;
- answer wording;
- date answered;
- whether answered directly;
- follow-up questions.

These will probably form the largest part of this file.

### Oral Questions

Include where relevant:

- Defence Questions;
- Treasury Questions;
- PMQs;
- urgent questions;
- topical questions.

Useful where ministers are pressed beyond written departmental language.

### Ministerial Statements

Include:

- SDR statements;
- DIP statements;
- spending announcements;
- training/readiness announcements;
- responses to current controversy.

### Select Committees

Priority:

- Defence Committee;
- Public Accounts Committee;
- Treasury Committee where relevant;
- Lords committees where useful.

Include:

- oral evidence;
- written evidence;
- committee reports;
- government responses.

---

## 🗓️ Core Chronology

### Late 2025 — Early Warning

Priority known material:

#### November 2025

James Cartlidge asks whether Defence had discussed reducing training across:

- British Army;
- Royal Navy;
- Royal Air Force.

Important analytical point:

The first answer reportedly framed “training” narrowly around Phase 1 / Phase 2 activity.

Follow-up research:

- exact wording;
- exact answer;
- whether collective/unit training was excluded by definition;
- who answered;
- whether answer referred to 2025–26 or 2026–27.

#### Late November / December 2025

Cartlidge follows up explicitly on:

- collective training;
- unit training;
- 2025–26;
- 2026–27.

Government response reportedly states that training remains a priority and that collective/unit activity will continue.

This should be treated as an important baseline assurance.

Questions:

- Was any reduction already under discussion?
- Was the answer technically accurate at the time?
- What commitments were made about future years?
- Was any distinction drawn between planned and funded activity?

### Early / Mid 2026 — Affordability Becomes More Visible

Search for parliamentary material concerning:

- Defence affordability;
- spending gaps;
- Army exercises;
- training estate;
- training cancellations;
- NATO commitments;
- Ukraine training;
- readiness;
- personnel shortfalls.

### 16 June 2026 — Service-by-Service Training Question

Priority item.

James Cartlidge reportedly asks specifically about reductions to training/exercises for:

- Army;
- RAF;
- Royal Navy.

Need exact wording and answer.

Important questions:

- Did the answer say yes/no?
- Did it use general language about “prioritising training”?
- Did it refer to changing operational circumstances?
- Did it distinguish the services?
- Did it commit to maintaining collective training?
- Did it mention affordability?

This is potentially a key pivot in the public chronology.

### 30 June 2026 — Defence Investment Plan

Parliamentary material to capture:

- questions on total funding;
- unfunded / later-funded elements;
- training;
- readiness;
- capital versus operating expenditure;
- implementation;
- service allocation;
- Treasury assumptions.

Especially important:

> What did Parliament ask about how the DIP would actually translate into usable readiness?

### July–August 2026 — Implementation / Pressure

Search for:

- training;
- exercises;
- readiness;
- Army affordability;
- Army Command;
- estate;
- personnel;
- recruitment;
- reserves;
- NATO commitments;
- Dreadnought;
- protected programmes;
- RDEL / CDEL;
- Treasury support.

Also capture ministerial changes and handovers where relevant.

### September 2026 — Current Training Decision

Record:

- questions prompted by current reporting;
- statements from ministers;
- responses from MOD;
- questions to Streeting;
- questions to Healey/Treasury;
- questions to Burnham;
- any Conservative / Lib Dem / Reform / crossbench scrutiny;
- service-specific comparisons;
- risk assessments;
- reversal or mitigation proposals.

This section should eventually become high-resolution and date-specific.

---

## 👥 Actor Register

Maintain an actor table.

```yaml
actor:
  name:
  office:
  office_start:
  office_end:
  role_in_parliamentary_record:
    - "asked question"
    - "answered question"
    - "made statement"
    - "committee witness"
  relevant_topics: []
  notes:
```

Priority figures:

- James Cartlidge;
- John Healey;
- Wes Streeting;
- Al Carns;
- Andy Burnham;
- Kemi Badenoch;
- relevant Defence ministers;
- Chief Secretary / Treasury ministers where relevant;
- Defence Committee chairs/members;
- relevant Lords ministers.

Important rule:

Office establishes responsibility for a portfolio, not personal knowledge of every underlying decision.

---

## 🔗 Question → Answer → Follow-Up Chains

Do not treat individual questions in isolation.

Where possible, build chains.

```yaml
question_chain:
  topic:
  entries:
    - date:
      questioner:
      question_number:
      question:
      answering_minister:
      answer:
      directness:
      new_information:
      unresolved:
      follow_up_triggered:
  interpretation:
    what_was_publicly_known:
    what_remained_unanswered:
    significance_to_current_case:
```

This is particularly useful for Cartlidge.

The interesting thing may not be one answer.

It may be:

> **question becomes more specific → answer remains general → issue later materialises publicly.**

That pattern is evidence of scrutiny chronology, not automatically evidence of deception.

---

## 🎯 Directness of Answer

Use a simple classification.

```yaml
answer_quality:
  directness:
    - "direct"
    - "partially_direct"
    - "general_response"
    - "did_not_answer_core_question"
    - "information_withheld"
    - "unable_to_answer"
  reason_if_stated:
  notes:
```

This lets us track whether government language shifts over time.

For example:

> **Question:** Will Army collective training be reduced?

Possible answer patterns:

- “No.”
- “Yes, by X.”
- “Training remains a priority.”
- “Activity is continually reviewed.”
- “Information is operationally sensitive.”

Those are very different governance signals.

---

## 🧠 Knowledge and Awareness Ladder

Because the cluster cares about who could reasonably have known what when, use cautious categories.

```yaml
awareness_assessment:
  actor:
  issue:
  date:
  evidence_level:
    0: "No public evidence of awareness."
    1: "Issue within portfolio / institutional responsibility."
    2: "Public parliamentary question directed to department."
    3: "Minister personally answered or signed response."
    4: "Minister publicly discussed issue."
    5: "Documented direct briefing / decision involvement."
  evidence:
  limitations:
```

This is extremely important.

It prevents us making the lazy move:

> Healey was Defence Secretary, therefore Healey knew.

Instead we can say:

> By date X, the issue had reached the department.  
> By date Y, a ministerial response existed.  
> Public evidence of Healey personally receiving the specific £30m proposal is / is not currently available.

Much stronger.

---

## 💷 Treasury / MOD Interface

Create a dedicated subsection for parliamentary evidence about money.

Track questions concerning:

- Treasury relief;
- supplementary funding;
- spending settlements;
- RDEL;
- CDEL;
- in-year savings;
- underspends;
- contingency;
- DIP affordability;
- nuclear ringfencing;
- contractual commitments;
- training budgets;
- service allocations.

Key question:

> Was Parliament ever told that the Defence settlement could require reductions to collective training?

And:

> Did MOD state that additional Treasury support had been requested or refused?

Do not infer a Treasury refusal without evidence.

---

## 🪖 Service-by-Service Comparison

Create a matrix.

| Date | Question | Army | Royal Navy | RAF | Joint | Answer / Source |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Track:

- exercise reductions;
- training reductions;
- readiness;
- personnel;
- savings;
- modernisation.

This matters because the current story appears to affect the Army differently.

We need to know whether Parliament had already identified that asymmetry.

---

## 📋 SDR / DIP Commitments Crosswalk

For relevant parliamentary answers, link them to formal commitments.

```yaml
commitment_check:
  parliamentary_date:
  issue:
  answer:
  relevant_policy:
    document:
    commitment:
  relationship:
    - "consistent"
    - "qualified"
    - "potential_tension"
    - "superseded"
    - "unclear"
  notes:
```

Example:

> Parliamentary assurance that collective training remains a priority  
> versus  
> SDR commitment to warfighting readiness  
> versus  
> later collective-training restriction.

This does not prove contradiction automatically.

It flags the need for explanation.

---

## 🔬 Questions Parliament Has Not Yet Asked

This is important.

Maintain a list of obvious governance questions absent from the parliamentary record.

Examples:

- Who first proposed collective training as the saving?
- What alternatives were costed?
- What readiness assessment accompanied the proposal?
- What minimum training level does Army Command consider necessary?
- What risks were formally accepted?
- Was Treasury asked for relief?
- Why did the services experience different reductions?
- Which spending lines were protected?
- What role did training modernisation play?
- When were ministers first informed?

Absence matters because it helps shape `open_questions.md` and `🚑_immediate_management.md`.

---

## 📰 Parliament / Media Interaction

Track cases where:

- parliamentary questions precede media reporting;
- media reporting triggers questions;
- leaks produce parliamentary scrutiny;
- ministers clarify press reports;
- parliamentary answers contradict or modify media claims.

```yaml
parliament_media_link:
  issue:
  parliamentary_event:
  media_event:
  sequence:
  significance:
```

This will be particularly useful for September 2026.

---

## 🤖 Machine-Readable Research Specification

```yaml
parliamentary_research:
  project: "Polaris"
  cluster: "Training Debrief"
  file: "data/parliamentary_questions.md"
  objective: >
    Reconstruct the public parliamentary governance trail surrounding UK
    military training, readiness and Defence affordability, with particular
    attention to the development of the 2026 British Army collective-training
    reductions.
  primary_period:
    start: "2025-01-01"
    end: "2026-12-31"
  extended_period:
    purpose: >
      Retrieve earlier parliamentary material when needed to establish
      recurring concerns about training, readiness, personnel, estate,
      force generation or affordability.
    start: "2010-01-01"
  priority_actors:
    - "James Cartlidge"
    - "John Healey"
    - "Wes Streeting"
    - "Al Carns"
    - "Andy Burnham"
    - "Kemi Badenoch"
    - "Defence ministers"
    - "Treasury ministers"
  priority_topics:
    - "British Army training"
    - "collective training"
    - "unit training"
    - "military exercises"
    - "Royal Navy training"
    - "RAF training"
    - "Defence readiness"
    - "warfighting readiness"
    - "Defence affordability"
    - "Defence Investment Plan"
    - "Strategic Defence Review"
    - "Army savings"
    - "service-specific savings"
    - "training estate"
    - "personnel"
    - "reserves"
    - "mobilisation"
    - "Treasury Defence funding"
  search_queries:
    - "site:questions-statements.parliament.uk James Cartlidge Army training"
    - "site:questions-statements.parliament.uk James Cartlidge collective training"
    - "site:questions-statements.parliament.uk Army RAF Royal Navy training"
    - "site:questions-statements.parliament.uk Defence training reductions"
    - "site:hansard.parliament.uk Army training readiness"
    - "site:hansard.parliament.uk Defence affordability training"
    - "site:committees.parliament.uk Defence readiness training"
    - "site:committees.parliament.uk Army collective training"
    - "Defence Investment Plan parliamentary questions training"
    - "Strategic Defence Review parliamentary questions readiness"
  extraction_fields:
    - "date_tabled"
    - "date_answered"
    - "question_number"
    - "questioner"
    - "questioner_party"
    - "department"
    - "answering_minister"
    - "question_text"
    - "answer_text"
    - "topic"
    - "service"
    - "directness"
    - "new_information"
    - "commitments"
    - "information_withheld"
    - "stated_reason_for_withholding"
    - "follow_up"
    - "related_policy_document"
    - "related_media_reporting"
    - "knowledge_relevance"
    - "open_questions"
    - "source_url"
  methodological_rules:
    - "Quote or preserve precise parliamentary wording where wording itself matters."
    - "Do not infer personal knowledge solely because a minister held office."
    - "Do not assume the named minister personally drafted a written answer."
    - "Treat departmental answers as evidence of the department's public position."
    - "Distinguish refusal, inability, generality and direct answer."
    - "Record question and answer dates separately."
    - "Track follow-up chains."
    - "Distinguish questions asked before and after media disclosure."
    - "Do not interpret evasiveness as proof of misconduct."
    - "Link parliamentary answers to relevant SDR/DIP commitments."
    - "Preserve party identity but do not assume motivation from party alone."
  priority_outputs:
    - "current governance chronology"
    - "Cartlidge question chain"
    - "service-by-service training matrix"
    - "MOD-Treasury affordability trail"
    - "SDR/DIP commitment crosswalk"
    - "ministerial awareness evidence"
    - "unanswered parliamentary questions"
  central_question: >
    What had entered the public parliamentary and ministerial record before
    the September 2026 Army training controversy, and what does that record
    permit us to say — cautiously — about institutional and ministerial
    awareness?
```

---

## 🧿 Key Analytical Distinctions

Keep these visible throughout.

### Department knew ≠ minister personally knew

A parliamentary answer establishes a departmental public position.

It does not automatically establish the personal knowledge of every relevant minister.

### Minister answered ≠ minister made the decision

Responsibility for answering Parliament and responsibility for originating a policy are different.

### Question asked ≠ allegation established

MPs can ask questions on incomplete information.

Questions are evidence of salience and scrutiny, not proof of their premise.

### General answer ≠ concealment

A general answer may be:

- deliberate avoidance;
- standard departmental drafting;
- uncertainty;
- operational caution;
- incomplete information;
- genuine inability to provide specificity.

Further evidence is required.

### Repeated questions matter

A sequence of increasingly precise questions can establish that an issue was repeatedly being brought into the governance system.

That is analytically different from proving what happened behind closed doors.

---

## 🪖 End-State

When populated, this file should allow us to say things like:

> By November 2025 Parliament was already asking whether service training would be reduced.
>
> By December the government had publicly stated X about collective training.
>
> By June 2026 Parliament was again asking service-by-service questions.
>
> The June answer did / did not directly rule out reductions.
>
> By date X the issue had therefore entered the departmental parliamentary record.
>
> Public evidence does / does not establish that Minister Y had personally received the later £30m proposal by that point.

That is the level of precision we want.

The objective is not to build a prosecution chronology.

It is to reconstruct the route by which an operational concern became — or failed to become — a political decision problem.

---

## 🌌 Constellations

🏛️ ❄️ 🪖 💷 🧾 🔬 🔁 — parliamentary scrutiny; Defence readiness; affordability; ministerial awareness; public governance trail.

---

## ✨ Stardust

parliamentary questions, british defence, army training, collective training, defence readiness, defence affordability, ministerial awareness, treasury, strategic defence review, defence investment plan

---

## 🏮 Footer

*🏛️ Parliamentary Questions* is a living research-infrastructure node of the **Polaris Protocol**.  
It reconstructs the public governance trail without converting parliamentary salience into unsupported claims about personal knowledge or decision authorship.

> 📡 Cross-references:
>
> - [❓ Open Questions](./open_questions.md) — *unresolved governance and evidence questions*
> - [📰 Current Reporting](./current_reporting.md) — *media disclosure and parliamentary interaction*
> - [🗃️ Source Bank](./source_bank.md) — *primary parliamentary and policy sources*
> - [💷 Thirty Million Pounds](../💷_thirty_million_pounds.md) — *the immediate decision chronology*
> - [🔬 Tests and Investigations](../🔬_tests_and_investigations.md) — *the wider evidential programme*
>
> 🏮 Return To:
>
> - [🪖 Training Debrief](../README.md) — *1up*
> - [🌊 Playing Defence](../../README.md) — *2up*
> - [📲 Press Matters](../../../README.md) — *3up*
> - [🌓 In The Moment](../../../../README.md) — *4up*
> - [🌌 Polaris Protocol — Root](../../../../../README.md) — *root*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-09-08_
