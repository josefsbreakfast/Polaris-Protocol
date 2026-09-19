# 🗺️ A Missing Battle Map?

**Path:** `🌖_6_Learning_The_Skies/🦑_The_Great_Kraken_Disturbance/⚔️_The_Battle_Of_Waterloo_Place/🗺️_a_missing_battle_map.md`

**Status:** Research and drafting scaffold

*What exactly was being proposed, what information architecture had been mapped before approval was sought, and what happens when governance has to evaluate a capability whose important feature may be the relationships between its parts.*

---

## 🛰️ Orientation

This node begins with an extremely ordinary governance problem:

> **What exactly was MOPAC being asked to approve?**

Not:

> Was Palantir good?

Not:

> Was Palantir bad?

Not:

> Was the Met allowed to use data?

Not even, initially:

> Was the proposed system lawful?

The prior question is simpler:

> **What was the proposed system?**

And, more specifically:

> **Was the information architecture sufficiently mapped for the approving authority to understand the capability, relationships and risks it was being asked to authorise?**

That is where the **battle map** metaphor enters.

A battle map is not the battle.

A DPIA is not literally a battle map.

But both can perform a related analytical function:

- identify relevant terrain;
- identify important objects;
- identify relationships;
- identify movement;
- identify exposure;
- identify foreseeable consequences;
- make a complicated environment governable enough for decisions to be made about it.

The question is therefore not merely:

> **Did a DPIA exist?**

It is:

> **What did the relevant assessments actually map?**

---

## 🗺️ 1. What We Mean By A Battle Map

Do not over-literalise the metaphor.

A useful map does not merely list the things present on the battlefield.

It shows enough of their relationships to make the terrain intelligible.

For an information system, relevant questions might include:

- what datasets exist?
- where do they originate?
- who controls them?
- who can access them?
- how are they combined?
- what queries can be performed?
- what analytical tools operate across them?
- what outputs can be produced?
- what inferences can be generated?
- who receives those outputs?
- what decisions may those outputs inform?
- what new relationships arise when previously separate systems are connected?

The map therefore concerns more than inventory.

It concerns:

> **architecture + relationship + movement + capability.**

---

## 📋 2. First Find The Actual Maps

Before drawing conclusions, obtain the relevant documentary material.

Research queue:

- DPIAs;
- updated DPIAs;
- screening assessments;
- data-flow diagrams;
- information-governance assessments;
- technical architecture documents;
- security assessments;
- procurement specifications;
- requirements documents;
- statements of work;
- trial documentation;
- UOA proposal documents;
- approval papers;
- risk assessments;
- supplier materials incorporated into decision-making;
- relevant governance correspondence.

For each document record:

- title;
- author;
- owner/controller;
- date created;
- date approved;
- version;
- scope;
- system/capability covered;
- datasets covered;
- processing covered;
- whether draft/final;
- whether superseded;
- who received it;
- what decision it informed.

Do not assume:

> **document with familiar title = document covering the relevant proposal.**

Version and scope matter.

---

## 🧭 3. A List Of Armies Is Not A Battle Map

This is the core teaching proposition.

Suppose an assessment says:

- Database A exists;
- Database B exists;
- Database C exists.

That tells us something.

But the important capability might arise from:

> **A + B + C + cross-querying + analytics + inference**

The individual datasets are not necessarily the most analytically important object.

The relationship between them may be.

Therefore ask whether the relevant assessment captures:

- combination;
- linkage;
- matching;
- querying;
- enrichment;
- analysis;
- inference;
- decision support;
- onward use.

> **A list of armies is not a battle map if it does not tell us where the armies can move.**

---

## 🔗 4. The Capability May Live In The Connections

This is where the node connects directly to Embodied Information Ecology.

Information systems can acquire capabilities through combination.

Abstractly:

> Dataset A can do X.  
> Dataset B can do Y.

But:

> A + B

may permit:

> Z.

And:

> A + B + analytical tooling

may permit:

> Z + Q + previously unavailable inference.

Therefore:

> **The capability of the whole cannot automatically be inferred from separate descriptions of the parts.**

This is particularly important when systems enable:

- cross-dataset querying;
- pattern identification;
- entity resolution;
- analytical enrichment;
- relationship mapping;
- decision support;
- inference.

Research the actual proposed UOA capability before assigning any of these functions to it.

---

## 🧮 5. One Plus One Can Create A New Risk

A governance assessment must sometimes consider not merely:

> What are the risks of Dataset A?

and:

> What are the risks of Dataset B?

but:

> **What becomes possible when A and B are connected?**

Potential abstract examples:

- previously separate attributes become linkable;
- larger behavioural patterns become visible;
- identities can be resolved more easily;
- relationships become inferable;
- queries become possible across previously separate information environments;
- outputs become available to different operational users.

This does not mean integration is inherently harmful.

Integration can also produce legitimate public benefits.

The analytical point is narrower:

> **Combination can change capability.**

Therefore combination can change risk.

---

## 🧱 6. Existing Assessments Do Not Automatically Assess A New Architecture

Be careful here.

An existing DPIA or assessment may remain highly relevant.

But do not reason:

> Dataset A already has a DPIA.  
> Dataset B already has a DPIA.  
> Therefore any new system combining A and B has already been assessed.

That conclusion requires evidence.

Ask:

- does the existing assessment cover the proposed processing?
- does it cover the new purpose?
- does it cover the new integration?
- does it cover the relevant analytical capability?
- does it cover the new recipients/users?
- does it cover new retention or access arrangements?
- does it cover the relevant supplier relationship?
- does it cover materially new risks?

The correct question is about **scope**, not paperwork count.

---

## 📝 7. A DPIA Is Not A Magical Compliance Scroll

Avoid:

> DPIA exists → lawful.

Also avoid:

> DPIA missing → unlawful.

Research the actual legal requirements before prose.

The useful analytical questions include:

- was a DPIA legally required?
- at what point?
- for what processing?
- who was responsible?
- what information was available when it was conducted?
- what risks did it identify?
- what mitigations did it specify?
- were those mitigations implemented?
- did the proposed processing later change?
- was the assessment revisited?

A DPIA is part of governance.

It is not an amulet.

---

## 🕰️ 8. The Map Has A Date

This is essential.

A perfect map of yesterday's battlefield may be a terrible map of today's.

For every relevant assessment ask:

> **What system existed when this document was written?**

Then distinguish:

- trial;
- pilot;
- Phase 1;
- proposed production system;
- later procurement;
- replacement procurement;
- subsequent technical development.

Do not merge them because:

- same supplier;
- same platform;
- same institution;
- similar capability;
- chronological proximity.

---

## ⏳ 9. Event Time And Information Time

Preserve the campaign's four-clock discipline.

Particularly:

### Event time

What capability was being proposed at the moment approval was sought?

### Information time

What information about that capability was available to:

- Met;
- MOPAC;
- supplier;
- relevant governance personnel

at that moment?

### Evidence time

When did documents establishing those facts become publicly available?

### Court time

When did the litigation place those documents or propositions before the court?

This prevents a major analytical error:

> **later information ≠ earlier knowledge.**

A document published in September may tell us something about May.

It does not automatically establish that every relevant actor knew that thing in May.

---

## 🚧 10. What Was MOPAC Actually Being Asked To Cross?

This should become one of the node's central questions.

The issue is not merely whether MOPAC received:

> **a proposal**

but whether it received enough information to understand the relevant governance boundary it was being asked to cross.

Ask:

- what authority was requested?
- what spending was requested?
- what processing was proposed?
- what systems would connect?
- what capability would result?
- what operational purpose would it serve?
- what supplier dependency would arise?
- what risks had been identified?
- what mitigations existed?
- what remained unresolved?

Then ask:

> **Was MOPAC being presented with a sufficiently mapped proposition to cross the authorisation boundary?**

This is a research question.

Do not answer it until the maps are found.

---

## 🎩 11. Which Tulpa Owns The Map?

Cross-link:

- `🎩_the_three_tulpae.md`

Separate the institutional roles.

Potential questions:

### Metropolitan Police

- Who designed the proposed capability?
- Who defined operational requirements?
- Who selected or assessed suppliers?
- Who determined purposes and means of processing where applicable?
- Who produced technical and information-governance material?

### MOPAC

- What exactly required approval?
- What information was MOPAC entitled or required to consider?
- What governance responsibility remained with MOPAC?
- What could MOPAC require before approval?

### Palantir

- What was the supplier's proposed technical role?
- What information did it provide?
- What contractual responsibilities were proposed?
- What processing role would it hold?
- What did it control and what did it not control?

Do not collapse:

> supplier provides system

into:

> supplier determines public purpose.

Likewise do not assume the supplier has no relevant responsibility.

Map the actual allocation.

---

## ⚖️ 12. Controller, Processor, Supplier, Decision-Maker

Research the precise legal and contractual roles.

Potential categories may include:

- controller;
- joint controller;
- processor;
- sub-processor;
- supplier;
- contracting authority;
- operational user;
- decision-maker.

These categories answer different questions.

Do not flatten them into:

> **who owns the data?**

Ask instead:

- who determines purpose?
- who determines means?
- who processes on whose behalf?
- who provides infrastructure?
- who can access what?
- who configures what?
- who authorises what?
- who bears which legal obligations?

The map must distinguish:

> **technical capability from legal authority.**

---

## 🏗️ 13. The Supplier Can Build A Road Without Choosing The Destination

Useful conceptual distinction.

A technology supplier may provide:

- infrastructure;
- tools;
- software;
- integration;
- analytical capability.

That does not automatically establish that the supplier determines:

- policing purpose;
- operational decisions;
- governance policy;
- lawful basis;
- public-sector objectives.

Conversely:

> **we merely provide the technology**

does not answer every governance question if the technology materially structures what becomes possible.

Therefore examine actual:

- contractual allocation;
- configuration;
- design;
- access;
- decision rights;
- technical dependency.

Avoid both:

> **supplier controls everything**

and:

> **supplier is merely an inert screwdriver.**

---

## 🧠 14. Technical Design Can Become Governance

This is one of the larger conceptual questions.

A system's architecture can affect:

- what can be searched;
- what can be combined;
- what can be inferred;
- what users can see;
- what decisions can be supported;
- what actions become easy or difficult.

Therefore technical design can have governance consequences even where the formal legal authority remains unchanged.

This does not mean:

> engineers secretly make the law.

It means:

> **practical capability is partly shaped by architecture.**

Cross-link:

- `🗡️_the_surgeons_knife.md`

because this is another place where:

> **formal authority ≠ practical capability.**

---

## 🔐 15. Access Is Not The Same Thing As Capability

Map different levels.

A person or system may have:

- no access;
- read access;
- query access;
- analytical access;
- ability to combine datasets;
- ability to configure workflows;
- administrative access;
- ability to export;
- ability to generate derived outputs.

These are different capabilities.

Likewise:

> access exists

does not establish:

> access was used.

Preserve:

> capability  
> → access  
> → opportunity  
> → use  
> → attribution  
> → causation

Stop where the evidence stops.

---

## 🧠 16. Inference Is Information Too

This may become important depending on the actual architecture.

A system need not merely retrieve stored facts.

Analytical systems can potentially produce:

- associations;
- classifications;
- scores;
- patterns;
- inferred relationships;
- derived attributes;
- prioritisation.

Research whether and how this applies to the proposed UOA.

Do not assign speculative capabilities to it.

But conceptually:

> **A map of input data may be incomplete if the system's important output is derived information.**

Therefore ask:

- what outputs could the system generate?
- what decisions could those outputs support?
- how were derived outputs governed?
- were relevant risks assessed?

---

## 🧬 17. Purpose Can Drift Even When The Database Does Not Move

Research purpose limitation and relevant data-protection principles before prose.

Conceptually:

A dataset can remain physically where it was while its practical role changes because:

- new querying becomes possible;
- new analytical tools are added;
- new purposes emerge;
- new users gain access;
- integration changes what can be inferred.

Therefore:

> **same database ≠ same processing environment.**

Again, this is a question to investigate, not a finding about the UOA.

---

## 🛡️ 18. Security Is Not The Whole Risk Map

A system can be technically secure while still presenting other governance questions.

Potential dimensions include:

- necessity;
- proportionality;
- purpose;
- transparency;
- accuracy;
- discrimination;
- access;
- retention;
- accountability;
- supplier dependency;
- rights impacts;
- operational consequences.

Do not collapse:

> **secure**

into:

> **appropriate**

or:

> **lawful.**

Likewise:

> governance concern

does not automatically imply:

> cybersecurity failure.

Different risk categories need different maps.

---

## 💷 19. The Commercial Map Matters Too

Information architecture is only one map.

The proposed capability may also create commercial dependencies.

Research:

- contract duration;
- licensing;
- switching costs;
- data portability;
- interoperability;
- proprietary components;
- exit arrangements;
- supplier substitution;
- knowledge transfer.

Do not assume vendor lock-in.

Ask whether it exists.

The wider Waterloo Place question remains:

> **Who governs when government buys capability?**

That includes:

> **How easily can government stop buying that capability from this particular supplier?**

---

## 🧯 20. Risk Mitigation Changes The Map

If a risk is identified and mitigated, the relevant architecture may change.

Possible abstract mitigations:

- restrict access;
- remove dataset;
- alter retention;
- change query permissions;
- introduce human review;
- limit integration;
- change supplier role;
- add approval steps.

Therefore a DPIA or risk assessment is not merely descriptive.

It may be part of the design feedback loop:

> proposed architecture  
> → risk assessment  
> → mitigation  
> → changed architecture  
> → reassessment

Cross-link:

- `📲_digital_angels_of_music.md`

The map can participate in changing the territory.

---

## ♻️ 21. The Map Can Change The Territory

This is the cybernetic bit.

Once institutional actors create a representation of risk:

- the representation can affect decisions;
- decisions can alter architecture;
- altered architecture changes the actual risk environment;
- the new environment may require another map.

Therefore:

> **territory → map → decision → changed territory → new map**

The battle map is not necessarily a passive document.

It can become part of the governance system.

But:

> bad outcome ≠ bad map  
> good outcome ≠ good map

Assess the mapping itself.

---

## 🗡️ 22. Why The Surgeon's Knife Makes The Missing Map Visible

Cross-link:

- `🗡️_the_surgeons_knife.md`

Ordinarily the public may have little reason or opportunity to ask:

- which DPIA existed;
- which version applied;
- what systems were mapped;
- who received it;
- what integration was proposed;
- which risks were identified.

The dispute creates the incision.

Once institutions disagree about:

- procurement;
- governance;
- approval;
- capability;

the adequacy of the underlying map can become much more interesting.

But:

> **interest in the map does not establish that the map was deficient.**

---

## 📲 23. Why Digital Angels May Help Us Find The Map

Cross-link:

- `📲_digital_angels_of_music.md`

Disclosure may potentially expose:

- references to DPIAs;
- drafts;
- requests for assessment;
- questions about architecture;
- risk discussions;
- approval chains;
- descriptions of the proposed capability.

Again:

> search ≠ finding.

But the documentary environment may help establish:

- which maps existed;
- when;
- who possessed them;
- which version informed which decision.

Digital Angels explains why those communications may become searchable.

Missing Battle Map explains why their contents might matter to understanding the architecture.

---

## 🏛️ 24. Why Wizard Fight May Care About The Map

Cross-link:

- `🏛️_wizard_fight_at_rolls.md`

The litigation may place particular documents in issue because they bear on:

- procurement;
- governance;
- reasonableness;
- authority;
- process;
- stated reasons.

Do not assume the court must answer every wider data-governance question Polaris finds interesting.

The map may matter:

1. directly to a pleaded issue;
2. indirectly as factual context;
3. only to the wider Battle analysis;
4. not at all.

Keep those categories separate.

> **The court's map and Polaris's map do not have to be the same size.**

---

## 🪄 25. What Can The Pointy Hat Actually Require?

Cross-link:

- `🪄_the_powers_of_the_pointy_hat.md`

Research:

- what documents the court can require;
- what disclosure regime applies;
- relevance;
- proportionality;
- privilege;
- confidentiality;
- public access.

Do not assume:

> document exists → Polaris gets document.

Or:

> court can compel document → court will compel document.

Or:

> document disclosed between parties → document becomes public.

Different pathways.

---

## ❓ 26. The Missing Map Is A Question, Not A Finding

This needs to be painfully explicit.

At present:

> **"missing battle map" is a research hypothesis.**

It means:

> **we do not yet know whether the relevant public record contains a sufficiently complete map of the proposed information architecture and associated governance.**

It does **not** mean:

> no DPIA existed.

It does **not** mean:

> the Met failed to assess risk.

It does **not** mean:

> MOPAC lacked relevant information.

It does **not** mean:

> Palantir concealed architecture.

It does **not** mean:

> the proposed processing was unlawful.

The investigation begins by finding the maps.

Then we compare their scope with the capability they purported to assess.

> **The missing battle map remains a question until we find the maps.**

---

## 🔬 27. What Would Count As A Mapping Gap?

Define this before looking for one.

Possible examples, depending on the applicable law and actual system:

- relevant processing absent from scope;
- material integration omitted;
- outdated architecture;
- important dataset omitted;
- material derived/inferred output omitted;
- significant access pathway omitted;
- supplier role incorrectly described;
- material change after assessment without reassessment;
- relevant risk identified but mitigation status unclear.

These are candidate categories.

They are not findings.

A gap should require:

> **expected scope  
> + documentary evidence of actual scope  
> + identifiable difference**

Do not infer a gap merely because a public summary lacks technical detail.

The complete assessment may contain information unavailable publicly.

---

## 📏 28. How We Test The Map

For each relevant assessment:

### Scope

- What does it say it covers?

### Architecture

- What components does it identify?

### Flows

- What movement or combination of information does it describe?

### Capability

- What does it say the system can do?

### Purpose

- What processing purpose does it assess?

### Roles

- Who does it identify as controller, processor, supplier, user or approver?

### Risks

- What risks does it identify?

### Mitigations

- What changes or controls does it require?

### Time

- Which version of the proposed system existed when it was written?

### Decision

- Which later approval or operational decision relied upon it?

Then compare this with the best independently supported reconstruction of the actual proposed capability.

---

## 🧩 29. Three Different Kinds Of Missing

Useful distinction.

### The map does not exist

No relevant assessment was created.

Requires evidence.

### The map exists but is incomplete

Assessment exists but materially fails to cover relevant architecture or processing.

Requires comparison.

### The map exists but we cannot see it

Public record is incomplete.

This is epistemically very different.

Do not convert:

> **Polaris cannot find it**

into:

> **the institution never had it.**

That distinction should sit near the centre of the node.

---

## 🌫️ 30. Public Opacity Is Not Institutional Ignorance

Related rule.

Some information may be:

- confidential;
- commercially sensitive;
- operationally sensitive;
- legally privileged;
- security-sensitive;
- simply unpublished.

Therefore:

> **not publicly visible ≠ institutionally unknown.**

Conversely:

> institution possessed document ≠ every relevant decision-maker understood its contents.

Again:

> document existence  
> ≠ receipt  
> ≠ reading  
> ≠ understanding  
> ≠ reliance.

---

## 🔭 31. Sensors To Watch

Watch for:

- publication of DPIAs;
- revised DPIAs;
- disclosed risk assessments;
- technical architecture descriptions;
- court references to data-governance documents;
- witness evidence describing the UOA;
- procurement specifications;
- MOPAC committee papers;
- Met governance documents;
- London Assembly questions;
- FOI disclosures;
- supplier documentation;
- replacement procurement documentation;
- changes in public descriptions of the capability.

Each new item should first enter:

- `📜_tapestry_draft.md`

if it changes chronology or the public information state.

Then update this node's map register.

---

## 🧾 32. Battle Map Register

Maintain a live table during research.

| Document | Date | Version | Owner | Capability covered | Data/process covered | Decision informed | Public? | Evidential status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | Unknown | Find the fucking maps |

Add separate tables if needed for:

- technical architecture;
- data flows;
- risk assessments;
- procurement documents;
- governance approvals.

Do not force unlike documents into one category merely because all are useful for reconstruction.

---

## ⚠️ 33. Integrity Register

- Missing from public record ≠ never existed.
- Existing DPIA ≠ adequate DPIA.
- DPIA exists ≠ processing lawful.
- DPIA absent ≠ automatically unlawful.
- Old assessment ≠ assessment of new architecture.
- Same dataset ≠ same processing.
- Same supplier ≠ same system.
- Same platform ≠ same capability.
- Same database ≠ same information environment.
- Dataset inventory ≠ data-flow map.
- Component assessment ≠ integrated-system assessment.
- Technical security ≠ complete governance.
- Access ≠ use.
- Capability ≠ use.
- Supplier capability ≠ supplier authority.
- Public authority ≠ technical capability.
- Technical design ≠ legal authority.
- Derived information ≠ source information.
- Potential inference ≠ inference actually produced.
- Risk identified ≠ harm occurred.
- Mitigation proposed ≠ mitigation implemented.
- Document existence ≠ receipt.
- Receipt ≠ reading.
- Reading ≠ understanding.
- Understanding ≠ reliance.
- Later evidence ≠ earlier knowledge.
- Public opacity ≠ institutional ignorance.
- Institutional knowledge ≠ shared knowledge across every unit.
- Court relevance ≠ wider analytical importance.
- Wider analytical importance ≠ court relevance.
- Research hypothesis ≠ finding.
- **Do not invent the missing map.**
- **Do not invent the missing arrow.**

---

## 💬 34. Line Bank

- **What exactly was MOPAC being asked to approve?**
- **What did the relevant assessments actually map?**
- **A list of armies is not a battle map if it does not tell us where the armies can move.**
- **The capability may live in the connections.**
- **One plus one can create a new risk.**
- **The capability of the whole cannot automatically be inferred from separate descriptions of the parts.**
- **A DPIA is not a magical compliance scroll.**
- **The map has a date.**
- **A perfect map of yesterday's battlefield may be a terrible map of today's.**
- **Later information does not establish earlier knowledge.**
- **Was MOPAC being presented with a sufficiently mapped proposition to cross the authorisation boundary?**
- **Technical capability and legal authority are different layers of the map.**
- **The supplier can build a road without choosing the destination.**
- **But a road can still change which destinations become practically reachable.**
- **Practical capability is partly shaped by architecture.**
- **A map of input data may be incomplete if the important output is derived information.**
- **Same database does not necessarily mean same processing environment.**
- **The map can participate in changing the territory.**
- **Territory → map → decision → changed territory → new map.**
- **The court's map and Polaris's map do not have to be the same size.**
- **The missing battle map remains a question until we find the maps.**
- **Polaris cannot find it is not the same proposition as the institution never had it.**
- **Public opacity is not institutional ignorance.**
- **Do not invent the missing map.**

---

## 🌌 Constellations

- [`📜 Tapestry Draft`](../📜_tapestry_draft.md)
  - chronological record of when maps, assessments and descriptions become publicly knowable.

- [`🗡️ The Surgeon's Knife`](./🗡️_the_surgeons_knife.md)
  - explains why the dispute creates the incision through which information architecture becomes unusually visible.

- [`📲 Digital Angels Of Music`](./📲_digital_angels_of_music.md)
  - follows documentary searches, communications, distributed information and recursive information pathways.

- [`🎩 The Three Tulpae`](./🎩_the_three_tulpae.md)
  - separates MOPAC, Met and Palantir roles and prevents institutional labels becoming singular minds.

- [`🏛️ Wizard Fight At Rolls`](./🏛️_wizard_fight_at_rolls.md)
  - identifies which parts of the documentary terrain matter to the parties' legal arguments.

- [`🪄 The Powers Of The Pointy Hat`](./🪄_the_powers_of_the_pointy_hat.md)
  - distinguishes what the court can compel, inspect and decide from the wider questions Polaris can investigate.

- [`🌙 Imagining Athena Nike`](./🌙_imagining_athena_nike.md)
  - provides the physical and symbolic battlefield from which the modern information architecture is viewed.

- **Embodied Information Ecology**
  - information becomes consequential through relationships, movement, combination, interpretation and feedback.

---

## ✨ Stardust

- The missing battle map is a question, not a conclusion.
- The first job is to find the actual maps.
- A DPIA or technical assessment must be read for its scope, date and relationship to the proposed capability.
- A list of datasets does not necessarily map the relationships between them.
- Combination can create capabilities not visible from separate descriptions of components.
- New capability can create new risk.
- Existing assessments do not automatically cover materially changed processing.
- Technical capability, legal authority and institutional responsibility must remain distinct.
- Supplier, controller, processor, operational user and approving authority are different roles.
- The map has a date.
- Later evidence does not establish earlier knowledge.
- Public absence does not establish institutional absence.
- The court may need a smaller map than Polaris.
- Litigation may nevertheless expose documents that allow the wider architecture to be reconstructed.
- Risk assessment can alter design, meaning the map itself can participate in changing the territory.
- The research question remains:

> **Was MOPAC being presented with a sufficiently mapped proposition to cross the authorisation boundary?**

- Until the documents answer it:

> **The missing battle map remains a question until we find the maps.**

---

## 🏮 Footer

> 📡 **Cross-references**
>
> - [`📜 Tapestry Draft`](../📜_tapestry_draft.md) — *chronology and changing public information state*
> - [`🗡️ The Surgeon's Knife`](./🗡️_the_surgeons_knife.md) — *why the institutional anatomy becomes visible*
> - [`📲 Digital Angels Of Music`](./📲_digital_angels_of_music.md) — *how documentary information becomes searchable and recursive*
> - [`🎩 The Three Tulpae`](./🎩_the_three_tulpae.md) — *institutional roles and distributed knowledge*
> - [`🏛️ Wizard Fight At Rolls`](./🏛️_wizard_fight_at_rolls.md) — *legal relevance of the documentary record*
> - [`🪄 The Powers Of The Pointy Hat`](./🪄_the_powers_of_the_pointy_hat.md) — *judicial powers and evidential limits*
> - [`🌙 Imagining Athena Nike`](./🌙_imagining_athena_nike.md) — *the battlefield from which we are looking*

> 🏮 **Return To**
>
> - `⚔️_The_Battle_Of_Waterloo_Place` — *1up*
> - `🦑_The_Great_Kraken_Disturbance` — *2up*
> - `🌖_6_Learning_The_Skies` — *3up*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-09-19_
