# 🧵 Narrative Scaffolding

**First created:** 2026-09-18 | **Last updated:** 2026-09-18  
*Reducing sequencing and working-memory load while preserving the author's authorship of narrative prose.*

---

## 🛰️ Orientation

Polaris is being written during the author's recovery.

That matters to the method.

Some forms of writing are useful parts of that recovery, including the work of turning evidence, events, absurdity, conflict and institutional behaviour into narrative. The purpose of machine assistance is therefore not always to produce the prose as quickly as possible.

Sometimes the useful job is to make the writing possible.

For narrative nodes, the machine should preferentially help by building the factual and chronological rails underneath the story: ordering events, identifying who did what, separating evidence from interpretation, tracking what was known at each point, and flagging places where chronology is easy to muddle.

The author can then do the narration.

This is both an accessibility practice and an authorship practice.

---

## 🧠 What the Scaffold Is For

A narrative scaffold reduces the amount of information that has to be held in working memory at once.

It should help answer:

- What happened first?
- What happened next?
- Who acted?
- What were they responding to?
- What information existed at that point?
- What had not happened yet?
- Which claims are documented facts?
- Which are reported claims or party positions?
- Which are interpretations?
- Which questions remain unresolved?
- Which later developments should not be projected backwards into an earlier scene?

The scaffold is not the finished narrative.

It is the sequence underneath it.

---

## ✍️ Preserve the Author's Writing Space

Where the author intends to write the narrative prose, the machine should not automatically replace that work by producing a polished narrative.

Default division of labour:

**Machine:**
- retrieve and organise sources
- establish chronology
- identify actors
- distinguish evidence status
- track information available at each stage
- identify temporal and causal dependencies
- flag contradictions and unresolved points
- identify sequence traps
- provide a compact writing scaffold

**Author:**
- narration
- pacing
- voice
- metaphor
- satire
- scene construction
- callbacks
- aesthetic judgement
- deciding what is actually funny
- deciding what the story feels like

If the author explicitly asks the machine to draft narrative prose, it can do so.

Otherwise, scaffolding should support authorship rather than silently substituting for it.

---

## 🧵 Default Narrative Scaffold

A working scaffold may use the following structure:

```markdown
# 🧵 Narrative Scaffold

*Working chronology for writing the narrative section. Not finished prose.*

## 🎬 Where the story starts

- DATE — Event.
- Who is relevant at this point.
- What has already happened that the reader needs to know.
- What nobody knows yet.
- Source(s).

## 1. First movement

- DATE/TIME — Actor A does X.
- This happens BEFORE Y.
- At this point:
    - A knows...
    - B has said...
    - C has not happened yet.
- Documentary status:
    - Documented / reported / party position / interpretation / unknown.
- Narrative significance:
    - This introduces...
    - This creates the problem that later produces...
- Safe artistic licence:
    - tone
    - metaphor
    - compression
    - comic description
- Do not accidentally imply:
    - motive not established
    - coordination not established
    - later knowledge was already available

## 2. Second movement

- DATE — B responds.
- Response is specifically to...
- New information entering the system:
    - ...
- What changes because of this:
    - ...
- What remains unresolved:
    - ...

## 3. The turn

- DATE — ...
- This is the point where the story changes direction because...
- Earlier thread it picks up:
    - ...
- Later consequence:
    - ...

## 🧶 Threads to carry through the narration

- Thread A first appears at event 1.
- Thread B first appears at event 3.
- Thread A and B intersect at event 6.
- Do not introduce Thread C until event 8.

## ⚠️ Sequence traps

- X happened before Y, despite later reporting discussing them together.
- Statement A was made before Document B became public.
- Do not give Actor C knowledge they could only have obtained later.
- Allegation D remains an allegation at this stage.
```

The exact headings can change with the material. The function should not.

---

## ⏳ Chronology Is Also an Evidence Rule

Chronology is not merely a list of dates.

In a feedback environment, the information available at a particular moment helps define the environment in which an actor moved.

A later document may explain an earlier event.

It must not be silently treated as though everybody already knew its contents.

A later allegation may change how an earlier event is interpreted.

It does not travel backwards in time and become an established fact at the earlier date.

A later judgment may resolve a dispute.

It does not mean the resolved position was already known while the dispute was live.

The scaffold should therefore track both:

**event time** — when something happened

and

**information time** — when the relevant information became available to the actor, institution, public, or author.

Where that distinction cannot be established, preserve the uncertainty.

---

## 📋 Evidence Status

Scaffolds should use the project's ordinary evidence vocabulary.

Useful labels include:

- **Documented** — supported directly by an identified primary record.
- **Reported** — stated by a reliable secondary source, with attribution.
- **Party position** — what a participant says happened or argues is true.
- **Our reading** — an interpretation of the available material.
- **Unknown** — not established by the available evidence.

Narrative confidence must never increase evidential confidence.

A good joke does not upgrade a source.

---

## 🎨 Artistic Licence

The narrative layer is allowed to be entertaining.

It may use:

- metaphor
- satire
- battle language
- fantasy
- absurd institutional theatre
- heightened description
- comic characterisation
- compression of uneventful intervals
- callbacks
- dramatic pacing
- visual jokes
- recurring narrative devices

It does not need to reproduce the documentary record sentence by sentence.

Reasonable artistic licence is expected.

The important constraint is that artistic licence should not materially alter:

- what happened
- the order in which consequential events happened
- who actually did or said something
- what was known at that point
- the evidential status of disputed claims
- the distinction between interpretation and documented fact
- whether coordination, motive, causation or intent has actually been established

If the entertaining version and the documentary record materially diverge, the documentary record wins.

---

## 🎪 Satire and Narrative Are Not the Record

Narrative and satire can do work that a documentary ledger cannot.

They can make institutional behaviour legible, memorable and human.

They can also exaggerate aesthetic qualities without exaggerating the underlying facts.

That freedom depends on keeping the layers distinguishable.

The reader should be able to move from:

**🍿 Story / 🎪 Satire**

to:

**📋 Record**

and see what actually supports the telling.

The funny layer does not carry the evidential burden.

That is what permits it to be funny.

---

## ♿ Accessibility Is Part of the Method

This workflow is not an apology for an imperfect writing process.

It is a deliberate division of cognitive labour.

During recovery, sequencing, working-memory load and keeping multiple moving events correctly ordered can require disproportionate effort. Machine assistance can absorb some of that mechanical burden without taking away the part of the work the author wants to do.

The objective is not:

> machine writes because author cannot.

The objective is:

> machine holds the chronology steady so the author has more room to write.

That distinction should be preserved.

Accessibility support should increase the author's agency, not quietly replace it.

---

## 🤖 Machine Instruction

When assisting with a Polaris narrative node:

1. Determine whether the author wants a scaffold or actual narrative drafting.
2. If narrative drafting has not been requested, prefer the scaffold.
3. Ground factual chronology in the available sources.
4. Order consequential events explicitly.
5. Identify what each actor was responding to where the evidence permits.
6. Track what information was and was not available at each stage.
7. Label evidence status.
8. Preserve unresolved disagreements.
9. Flag sequence traps and hindsight risks.
10. Distinguish temporal sequence from causation.
11. Do not infer motive, coordination or intent merely because events form a compelling narrative.
12. Identify places where artistic compression is safe.
13. Leave voice, pacing, metaphor and final narration to the author unless asked to help draft them.

When uncertain:

> **Hold the sequence steady. Preserve the distinction. Leave the prose room to breathe.**

---

## 🦑 Kraken Use

For *The Great Kraken Disturbance*, narrative scaffolds can sit underneath the deliberately ridiculous apparatus.

The machine can establish:

- which letter came first
- which procurement preceded which dispute
- when litigation began
- which public statement responded to which event
- when a document entered the public domain
- which larger thread first became visible where
- what remained unknown at each point

The author is then free to decide whether the scene requires:

- a battle
- a wizard
- a KC appearing like a Pokémon
- a Hansard clerk sighing
- a woman on top of a Crimean War memorial holding things
- or merely the words:

> for fuck's sake.

The scaffold protects the chronology.

It does not police the fun.

---

## 🌌 Constellations

- `🦑_The_Great_Kraken_Disturbance/` — worked teaching ecology in which this method is being developed.
- `📜_tapestry_draft.md` — running chronological weave that can supply source material for individual scaffolds.
- `♻️🕸️_The_Feedback_Environment/` — conceptual home for understanding why event order and information order matter.
- `🫧_Krakens_Pearls/` — public continuity and methodology layer.

---

## ✨ Stardust

- **Scaffolding is not substitution.**
- **Chronology is part of epistemic integrity.**
- **Event time and information time are not always the same thing.**
- **Narrative confidence must never increase evidential confidence.**
- **Accessibility support should increase authorial agency.**
- **Hold the sequence steady. Leave the author room to write.**

---

[↑ Back to top](#-narrative-scaffolding)
