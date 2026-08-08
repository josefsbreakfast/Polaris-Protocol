# 🧭 How I Use Robit To Build Nodes  
**First created:** 2026-08-08 | **Last updated:** 2026-08-08  
*A practical workflow for using an LLM to expand, test, organise and draft Polaris material without handing the model authorship, verification or judgement.*

---

## 🛰️ Orientation

There is no single magic prompt that produces a Polaris node.

That is not how I use Robit.

Most nodes emerge through a conversation in which the problem changes shape as I understand it better. Sometimes I arrive with a fairly precise question. Sometimes I have an observation, an irritation, a contradiction, a news story, a mechanism I think I can see, or several existing nodes that suddenly appear to belong together.

Robit's job is not to decide what any of that means.

Its job is to help me **hold the working surface open long enough to find out**.

The workflow is iterative rather than linear, but in broad terms it looks like this:

```text
question
→ preload
→ expansion
→ factual hinges
→ working inventory
→ anti-forking
→ chunking
→ correction
→ gap analysis
→ selection
→ architecture
→ drafting
→ adversarial pass
→ publication
→ later revision
```

Not every node needs every stage.

Large clusters usually do.

---

## 1. 🧩 Start With The Actual Question

The useful starting point is usually not:

> Write me a node about X.

It is closer to:

> Something about X does not make sense to me.

Or:

> These two things seem structurally related. Are they?

Or:

> We keep describing this as one problem, but I think there are three different mechanisms hiding inside it.

Or:

> I know what happened. I do not yet know what the node is *about*.

That distinction matters.

If I ask for polished prose too early, Robit is very capable of supplying polished prose before the analytical problem has stabilised.

Then I have a nice paragraph and no idea whether it belongs anywhere.

The first task is therefore to identify the unresolved object.

```text
What am I actually trying to understand?
What distinction feels missing?
What mechanism might be operating?
What would this node need to teach the reader?
```

The title can come later.

---

## 2. 📚 Preload The Relevant Polaris Context

Robit works better when it knows what has already been built.

For a small node, that may mean giving it:

- the parent README;
- the neighbouring node list;
- one or two closely related nodes;
- the House Style;
- and any specific evidence or source material relevant to the question.

For a large cluster, I may preload substantially more.

The purpose is not simply stylistic consistency.

Existing Polaris material tells Robit:

- which distinctions already exist;
- which arguments do not need rebuilding;
- what terminology is already in use;
- what should be cross-linked rather than duplicated;
- where a proposed idea may actually belong;
- and which conceptual commitments must remain consistent across the archive.

This is especially important in a large linked repository.

Without context, an LLM has a strong tendency to reinvent things.

Sometimes it reinvents them worse.

---

## 3. 🌱 Expand Before Narrowing

Early generation is allowed to be excessive.

At this stage I may ask:

- What does this connect to?
- What examples have we already raised?
- What mechanisms could explain this?
- What distinctions are being collapsed?
- What rival explanations exist?
- What historical comparisons might be useful?
- What other Polaris clusters does this touch?
- What daughter nodes might this imply?
- What would a sceptical reader ask?
- What am I forgetting?

The point is **coverage**, not publication.

A useful early pass may contain repetition, weak ideas, over-specific branches, speculative links and things that later disappear entirely.

That is fine.

I would rather see the working pile before deciding what belongs in the cupboard.

---

## 4. 🔎 Check The Factual Hinges Early

Not every sentence needs immediate verification during brainstorming.

Some claims do.

A **factual hinge** is a proposition that materially changes the architecture if it is wrong.

Examples include:

- whether a law actually applies;
- whether an institution had a particular power at the relevant date;
- whether an event happened in the sequence being assumed;
- whether a historical comparison rests on a real feature of the historical case;
- whether two organisations are actually connected;
- whether a technical capability exists;
- whether the terminology being used has a specific legal meaning.

If the skeleton depends upon the answer, check it before building descendants underneath it.

The rule is simple:

> **Do not allow an error to become architecture.**

A mistaken factual premise can otherwise become:

```text
bad assumption
→ analytical claim
→ heading
→ daughter node
→ cross-link
→ apparently coherent cluster
```

Correcting the first line is cheap.

Correcting the whole tree is annoying.

---

## 5. 🧺 Ask For The Working Inventory

Once a conversation has become large, I periodically stop asking Robit for new ideas.

Instead I ask it to tell me what is already on the floor.

This is one of the most useful stages.

The instruction may effectively be:

> Give me every distinct argument, example, mechanism, unresolved question and proposed node we have raised so far. Do not improve it yet. Do not silently merge things. I want the inventory.

This catches a recurring LLM failure mode: abstraction can make specific examples disappear.

Robit may produce an elegant summary while quietly dropping three of the things that made the original discussion interesting.

An inventory forces the work back into particulars.

It also makes later editorial decisions visible.

---

## 6. 🥛 Watch For Husband-Going-For-Milk Syndrome

Robit can be impressively productive while failing to do the specific thing it was sent to do.

This is **husband-going-for-milk syndrome**.

The model has:

- understood the general problem;
- generated useful adjacent material;
- improved the conceptual framing;
- identified several new questions;
- perhaps reorganised half the cluster;

and has not returned with the fucking milk.

The fix is not necessarily a better mega-prompt.

Usually it is a smaller instruction.

```text
Stop.

What exactly did I ask for?

Which parts have you answered?

Which parts are still missing?

Give me those parts only.
```

This is one reason I prefer conversational drafting to pretending the model will follow a huge instruction perfectly from beginning to end.

When it wanders, I can send it back to the shop.

---

## 7. ✂️ Narrow Against Forking

Once the working inventory exists, expansion stops being the priority.

Now the question becomes:

> Which of these things are actually different enough to deserve separate nodes?

LLMs like forks.

A model can turn every interesting sentence into a plausible filename.

That does not mean the repository should.

I therefore look for:

- duplicate mechanisms;
- examples pretending to be concepts;
- concepts that belong as sections rather than nodes;
- nodes that would contain substantially the same evidence;
- attractive tangents that belong in another cluster;
- material that should remain parked until the evidence improves;
- and proposed daughters whose only purpose is to contain one paragraph.

The goal is not the smallest possible tree.

It is a tree in which **each surviving node has a job**.

---

## 8. 🏷️ Make The Editorial Decisions Explicit

During structural work, I find it useful to classify material.

```text
[KEEP]    — survives substantially as proposed
[MERGE]   — belongs with another item
[PARK]    — useful, but not for this drafting pass
[FORK]    — genuinely needs its own route
[DROP]    — does not earn a place
[RENAME]  — concept survives but framing is wrong
[VERIFY]  — cannot safely proceed as fact yet
```

These labels stop generation from masquerading as decision.

Robit can help recommend them.

I retain the decision.

This stage is also where a giant pile of apparently separate observations often reveals a much smaller number of underlying mechanisms.

That is usually progress.

---

## 9. 🧱 Work In Chunks Once The Structure Gets Large

Large clusters become less reliable if I ask Robit to hold the whole thing at equal resolution indefinitely.

So once the broad architecture exists, I work daughter by daughter or in small groups of nodes.

A typical pass might be:

```text
daughter remit
→ 5–10 proposed nodes
→ one-line remit for each
→ correction
→ duplication check
→ missing-question check
→ freeze that section
→ move to the next daughter
```

This has two advantages.

First, errors are easier to catch.

Second, the corrected version of one section can become context for the next.

The model is less likely to reiterate an early misunderstanding across fifty filenames before I notice it.

---

## 10. 🧯 Correct Robit As Soon As It Is Wrong

Correction is part of the method, not evidence that the method failed.

Robit will misunderstand things.

It may:

- flatten two legal categories together;
- infer a causal relationship I did not assert;
- lose an important asymmetry;
- make a historical comparison too strong;
- turn a possibility into a claim;
- interpret an example as the central argument;
- or simply forget something I told it fifteen messages ago.

I correct this when it appears.

I do not preserve a model-generated structure merely because the model already spent time generating it.

Sunk-cost fallacy is not improved by automation.

Sometimes a correction changes one sentence.

Sometimes it collapses an entire branch.

Good.

---

## 11. 🕳️ Run A Gap Analysis

Once the architecture looks coherent, I ask what it cannot yet explain.

This is different from asking for more ideas.

A gap analysis tests the proposed structure against its own remit.

Useful questions include:

- What central question has no home?
- Which daughter is doing too much?
- Which mechanism appears repeatedly but has no dedicated explanation?
- What obvious counter-example is missing?
- What would make this analysis one-sided?
- Which affected group appears only as an object and never as an actor?
- What practical or institutional layer is absent?
- Where have we described a problem without describing the failure pathway?
- What safeguard would a sceptical reader reasonably expect?
- Which node assumes knowledge supplied nowhere else in the pack?

Some of the best additions happen here.

So do some of the best deletions.

---

## 12. 🧭 Find The Conceptual Spine

Before drafting prose, I want to be able to say what the node or cluster actually teaches.

A topic is not yet a remit.

For example:

```text
"political donations"
```

is a topic.

```text
"legal money can still alter access, dependency and the practical cost of refusal"
```

is a proposition.

Likewise:

```text
"foreign influence"
```

is a topic.

```text
"foreign influence, foreign interference and attribution require different evidentiary thresholds"
```

is something a node can teach.

The conceptual spine is what survives after the examples change.

If I cannot state it, the structure probably is not ready.

---

## 13. 🗺️ Freeze The Architecture Before Full Drafting

At some point the tree has to stop moving long enough to write it.

For a cluster, I usually want:

- the daughter structure;
- daughter summaries;
- filenames;
- one-line node remits;
- obvious cross-cluster links;
- and verification flags.

This does not make the architecture permanent.

It makes it stable enough to draft against.

Without this stage, prose generation can keep silently redesigning the repository.

That is occasionally useful during exploration.

It is maddening during production.

---

## 14. ✍️ Draft Only Once The Node Knows Its Job

Once the remit is stable, Robit becomes much more useful as a drafting engine.

At this stage it can work against:

- the node remit;
- relevant source material;
- parent and sibling context;
- Polaris House Style;
- drafting rules;
- known verification flags;
- and the conceptual boundaries established during structural work.

The draft should not have to discover what the node is about while simultaneously trying to explain it.

That work happened earlier.

Now the task is to make the reasoning legible.

---

## 15. ⚖️ Separate Evidence, Inference, Analogy And Hypothesis

A polished draft can blur epistemic categories unless they are deliberately kept apart.

So during drafting I keep asking:

```text
What is directly evidenced?

What is a reasonable inference from that evidence?

What is an analogy being used to explain a mechanism?

What is a hypothesis worth testing?

What remains unknown?
```

These categories can coexist in one node.

They should not impersonate one another.

Particularly:

```text
connection ≠ knowledge
knowledge ≠ control
control ≠ culpability

correlation ≠ coordination
capability ≠ attribution
analogy ≠ evidence
legal ≠ harmless
suspicious ≠ proven
```

Robit is useful for checking these distinctions because it is also very capable of accidentally violating them.

---

## 16. 🪞 Make Robit Argue With The Draft

Once a draft exists, I use the model again in a different role.

Now I want resistance.

I may ask:

- What does this accidentally imply?
- Where does the language exceed the evidence?
- Which claim would a hostile but reasonable reader challenge?
- Have I transferred a finding between cases?
- Have I confused mechanism with attribution?
- Is there a rival explanation I have hidden?
- Am I applying the same evidentiary standard to comparable actors?
- Does an analogy carry moral baggage I have not acknowledged?
- Have I described absence of evidence as evidence of concealment?
- What evidence would make this node change its mind?

This is not about manufacturing artificial balance.

It is about preventing the argument from becoming unfalsifiable.

A node should be able to survive being looked at from the other side.

---

## 17. 🧿 Check For Prejudice And Selection Effects

Where a node concerns identity, diaspora, religion, race, nationality, political movements or network relationships, the adversarial pass also needs to ask:

- Why did this person or group enter the hypothesis space?
- Would structurally similar conduct elsewhere attract the same scrutiny?
- Am I investigating behaviour, capability and control, or using identity as a proxy?
- Have I turned an individual's conduct into a claim about a population?
- Could a genuine underlying problem coexist with discriminatory selection or framing?

The existence of prejudice does not make legitimate investigation impossible.

The existence of a legitimate investigative question does not make prejudice irrelevant.

Both can be true.

The method has to survive that complexity.

---

## 18. 🧯 State What Would Change The Conclusion

One of the best protections against a theory becoming self-sealing is to ask what would falsify it.

Before publication, I want to know:

> What evidence would make us revise this?

That may be:

- a timeline that runs the other way;
- evidence of independent decision-making;
- a missing contractual relationship;
- a technical capability proving impossible;
- a source withdrawing or correcting a claim;
- a legal threshold not being met;
- a plausible rival explanation fitting the evidence better;
- or new information showing that an apparent connection had no operational significance.

If no imaginable evidence can weaken the interpretation, I probably do not have an investigation.

I have a belief system.

---

## 19. 🏮 Publish The Node, Not The Conversation

The working conversation can contain:

- abandoned ideas;
- jokes;
- errors;
- speculative branches;
- duplicate formulations;
- temporary shorthand;
- unverified claims;
- and arguments that existed only long enough to reveal why they were wrong.

The finished node does not need to reproduce that history.

It needs to preserve the reasoning that survived it.

This is why the model transcript is not the authored object.

The node is.

---

## 20. 🔁 Treat Publication As A Version, Not An Ending

Polaris nodes are living documents.

New evidence may:

- increase confidence;
- reduce confidence;
- change attribution;
- expose a missing mechanism;
- require a correction;
- split a node;
- collapse two nodes together;
- or make an old framing obsolete.

Using an LLM does not change that.

If anything, it makes disciplined versioning more important because revision is cheap enough that there is little excuse for pretending an old formulation must remain simply because it was once published.

---

## 🧰 The Short Version

For routine use, the workflow can be compressed to:

```text
1. What am I actually trying to understand?

2. What existing Polaris context does Robit need?

3. Expand the problem before drafting it.

4. Verify factual hinges before they become architecture.

5. Inventory everything already raised.

6. Stop Robit wandering off with the milk.

7. Merge, park, fork, drop and verify.

8. Work large structures in small corrected chunks.

9. Run a gap analysis.

10. State the conceptual spine.

11. Freeze the architecture.

12. Draft against the remit and evidence.

13. Separate evidence, inference, analogy and hypothesis.

14. Make Robit attack the draft.

15. State what would change the conclusion.

16. Publish the node, not the scaffolding.

17. Revisit when the evidence changes.
```

The sequence is less important than the discipline underneath it:

> **Generate widely. Select deliberately. Correct early. Verify separately. Keep uncertainty visible.**

---

## 🌌 Constellations

🤖 🧭 🔎 🧱 🧯 — LLM-assisted drafting; research architecture; verification discipline; iterative correction; adversarial review.

---

## ✨ Stardust

large language models, research methodology, node development, iterative drafting, verification, gap analysis, scope control, editorial judgement, adversarial review

---

## 🏮 Footer

*🧭 How I Use Robit To Build Nodes* is a living scaffolding node of the **Polaris Protocol**.  
It records the repeatable working method used to move from an unresolved question through generative exploration, correction, verification and structural editing into a bounded Polaris node or cluster. It should be read as a workflow for human-directed LLM use, not as a claim that every node follows an identical sequence.

> 📡 Cross-references:
>
> - [🤖 Meet Robit](./README.md) — *orientation to the role, limits and recurring failure modes of the LLM inside Polaris drafting*
> - [🧪 Hot Money Politics — A Worked Example](./🧪_hot_money_politics_a_worked_example.md) — *the workflow shown against a real cluster from broad working pile to settled architecture*
> - [🔮 House Style](../🔮_house_style.md) — *canonical structural and formatting conventions for Polaris nodes*
> - [🎛️ Polaris Drafting Rules — Survivor Voice Fidelity](../🎛️_polaris_drafting_rules_survivor_voice_fidelity.md) — *voice, undertone and authorship fidelity rules used during drafting*
>
> 🏮 Return To:
>
> - [🤖 Meet Robit](./README.md) — *pack root*
> - [🏮 Admin Kit](../README.md) — *1up*
> - [🏮 Admin Nest](../../README.md) — *2up*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-08_
