# 📊 From Records To Scores
**First created:** 2026-07-20 | **Last updated:** 2026-07-20  
*How raw records become numerical or categorical judgements—and how policy choices disappear inside apparently objective outputs.*

---

## 🛰️ Orientation

Observation produces records.

Intervention requires a way to decide which records matter.

Scores promise:

- consistency;
- speed;
- prioritisation;
- comparability;
- apparent objectivity.

They also compress:

- context;
- uncertainty;
- disagreement;
- human relationships;
- political judgement.

A score is not the opposite of judgement.

It is judgement arranged into a reusable form.

The score looks numerical only after judgement has been hidden inside the arithmetic.

This node examines how systems move from records to features, weights, thresholds, and decisions—and what happens when those outputs begin to govern people who cannot inspect, challenge, or understand them.

---

## 🧮 What Is A Score?

A score may be:

- a number;
- a rank;
- a category;
- a traffic-light label;
- a confidence band;
- a priority tier;
- a recommendation.

Examples include:

- low, medium, high;
- 0–100;
- monitor, review, intervene;
- trusted, uncertain, risky;
- routine, elevated, urgent.

A system does not need to display a number to perform scoring.

A label can function like a score even when the arithmetic remains hidden.

The essential questions are:

- What enters the judgement?
- How are the inputs combined?
- What threshold follows?
- What decision does the output trigger?

---

## 🩸 The Records Entering The Score

Possible inputs include:

- communications;
- location;
- finance;
- employment;
- institutional affiliation;
- religious affiliation;
- family relationships;
- friendship;
- intimacy;
- public speech;
- platform activity;
- prior classifications;
- institutional complaints;
- administrative history.

One score may combine:

- directly observed facts;
- inferred relationships;
- predictions;
- copied institutional judgements;
- stale records;
- disputed allegations.

A single output may contain several different levels of certainty disguised as one value.

The input layer is examined in [🩸 Feed Me Data](../🩸_Feed_Me_Data/README.md).

The scoring layer converts those inputs into authority.

---

## 🔧 The Scoring Pipeline

A simplified pipeline is:

> **collect → clean → match → derive → weight → combine → threshold → act**

### Collect

Receive records from one or more sources.

### Clean

Standardise:

- names;
- dates;
- addresses;
- locations;
- identifiers;
- organisational labels.

### Match

Decide whether records concern the same:

- person;
- device;
- household;
- institution;
- relationship.

### Derive

Convert raw records into features.

### Weight

Decide which features matter more.

### Combine

Produce a score, rank, category, or recommendation.

### Threshold

Decide when the output becomes consequential.

### Act

Trigger:

- monitoring;
- manual review;
- referral;
- restriction;
- intervention.

Every arrow in the pipeline is a place where error or politics can enter.

---

## 🧷 Entity Resolution

Entity resolution asks whether two records concern the same entity.

The system may try to decide whether:

- two names refer to one person;
- two devices belong to one person;
- two addresses describe one household;
- two contacts represent one relationship;
- two organisations are affiliated.

Errors may arise from:

- common names;
- transliteration;
- shared devices;
- recycled phone numbers;
- family accounts;
- outdated records;
- institutional aliases;
- inconsistent spelling.

A wrong match contaminates every later step.

The score may be mathematically consistent and attached to the wrong person.

Once copied into other systems, the mistake may become harder to locate and correct.

---

## 🧩 Features

A feature is a measurable input used by a score.

Possible features include:

- contact frequency;
- network centrality;
- number of affiliations;
- international travel;
- financial transfers;
- event attendance;
- access to institutions;
- proximity to flagged people;
- changes in communication pattern;
- role in a network.

The stages should remain visible.

For example:

- raw fact: ten calls occurred;
- derived feature: high contact frequency;
- inference: close trust;
- classification: important relationship.

The feature may be measurable while the meaning attached to it remains speculative.

A system should not erase the difference between:

- what happened;
- what was calculated;
- what was inferred.

---

## 🪞 Proxies

Many politically relevant concepts cannot be measured directly.

Systems may use proxies for:

- trust;
- influence;
- allegiance;
- vulnerability;
- coalition capacity;
- likelihood of disclosure;
- ability to mobilise others.

Examples include:

- frequency as a proxy for trust;
- centrality as a proxy for influence;
- remittance as a proxy for dependency;
- attendance as a proxy for belief;
- shared address as a proxy for intimacy;
- professional status as a proxy for credibility.

A proxy is not the thing itself.

The danger is proxy drift.

A rough indicator may begin as:

> This may suggest trust.

After repetition, it becomes:

> This relationship is trusted.

The uncertainty disappears while the label remains.

---

## ⚖️ Weighting

Weighting determines:

- which records matter;
- how much they matter;
- what combinations are treated as serious;
- which absences are ignored;
- which patterns dominate the result.

Questions include:

- Is foreign travel weighted heavily?
- Is religious affiliation weighted at all?
- Does care access increase risk?
- Does professional credibility increase intervention priority?
- Does proximity to one flagged contact outweigh years of ordinary conduct?

Weights encode:

- policy;
- institutional priorities;
- cultural assumptions;
- historical bias;
- tolerance for error.

The arithmetic cannot tell us what deserves weight.

Someone must decide.

---

## ➕ Positive And Negative Weights

Some features may increase a score.

Others may reduce it.

Possible risk-reducing features include:

- institutional sponsorship;
- formal employment;
- approved intermediary;
- previous cooperation;
- administrative stability.

Possible risks include:

- approved status becoming mistaken for safety;
- marginality becoming risk;
- lack of records becoming suspicion;
- institutional legibility becoming a proxy for reliability.

The score may reward administrative legibility rather than actual safety.

A person who fits recognised categories may receive a lower score.

A person whose life is less formally documented may appear more uncertain and therefore more risky.

---

## 🕳️ Missing Data

Missing data may be treated as:

- zero;
- unknown;
- suspicious;
- average;
- imputed.

Each choice changes the result.

Missing data may reflect:

- privacy;
- poverty;
- digital exclusion;
- disability;
- migration;
- deliberate minimisation;
- ordinary absence;
- record failure.

Absence of data is not evidence of concealment.

A system that treats unknown as suspicious may systematically penalise people whose lives are:

- less documented;
- less institutionally legible;
- more private;
- more precarious.

---

## 📐 Normalisation

Scores may compare people across:

- communities;
- regions;
- institutions;
- time periods;
- demographic groups.

Normalisation requires a baseline.

That baseline may contain:

- majority norms;
- class assumptions;
- cultural misunderstanding;
- unequal data coverage.

Ten calls may be unusual for one relationship and ordinary for another.

Frequent family contact may be normal in one community and exceptional in another.

A behaviour becomes abnormal only after someone chooses the population against which it will be compared.

The baseline is therefore not neutral.

---

## 🚦 Thresholds

A threshold decides when a score becomes consequential.

Possible outcomes include:

- no action;
- monitoring;
- manual review;
- referral;
- intervention;
- exclusion.

Thresholds are policy choices.

They are not natural facts.

A small threshold change may affect:

- hundreds;
- thousands;
- entire communities.

The score measures.

The threshold governs.

A person may know the outcome while never learning:

- what line they crossed;
- who set it;
- why it moved;
- whether others crossed a different line.

---

## 📝 Descriptive Scores

Descriptive scores summarise what the system has recorded.

Examples include:

- number of contacts;
- network centrality;
- travel frequency;
- number of affiliations;
- financial activity.

They may describe:

- observed volume;
- recorded frequency;
- graph position.

A descriptive score says what the system sees, not necessarily what exists.

The underlying data may still be:

- incomplete;
- duplicated;
- stale;
- misidentified;
- contextless.

Description does not remove uncertainty.

---

## 🔮 Predictive Scores

Predictive scores estimate future events or hidden traits.

Examples include:

- likely influence;
- probable relationship;
- chance of coalition;
- expected non-compliance;
- likelihood of further contact.

Risks include:

- false positives;
- circular validation;
- demographic bias;
- predictions treated as facts;
- intervention effects treated as confirmation.

Prediction turns uncertainty into an output.

It does not remove uncertainty.

A probability should not become a factual statement merely because it appears in a dashboard.

---

## 🧭 Prescriptive Scores

Prescriptive scores recommend what should be done.

Examples include:

- prioritise monitoring;
- route for review;
- disrupt contact;
- use an intermediary;
- apply additional friction;
- restrict access.

These are the most consequential scores.

They embed:

- values;
- institutional goals;
- tolerance for harm;
- assumptions about acceptable intervention;
- beliefs about what outcomes matter.

A prescriptive score does not merely estimate the world.

It proposes how the world should be altered.

This is where scoring becomes governance.

---

## 🎯 Confidence Scores

Systems may attach confidence to:

- identity matches;
- relationship types;
- risk predictions;
- intervention recommendations.

But confidence in the model is not confidence in reality.

A system may be highly confident because:

- several dependent datasets agree;
- uncertainty was discarded;
- the model has narrow assumptions;
- contradictory evidence was excluded;
- duplicated sources appear independent.

Confidence can measure internal consistency while missing external truth.

Confidence should always be tied to:

- source quality;
- independence;
- date;
- method;
- contestability.

---

## 🧱 Composite Scores

Composite scores combine several inputs.

A simplified example might include:

> communications + location + finance + affiliation + relationship centrality

The combination may appear stronger than any one input.

But risks include:

- several weak proxies becoming one authoritative number;
- the same underlying event being counted repeatedly;
- correlated variables creating artificial certainty;
- one false match contaminating every component.

Combining five uncertain signals does not automatically create one certain conclusion.

The system should preserve the uncertainty of each component.

---

## 🪞 Double Counting

One event may appear as:

- location overlap;
- event attendance;
- device co-presence;
- social-media interaction;
- financial co-occurrence.

A system may count these as separate evidence.

But all may descend from one event.

One fact can masquerade as several signals when the system forgets their common source.

Double counting can inflate:

- confidence;
- severity;
- centrality;
- priority.

The source lineage of every feature should remain visible.

---

## 📤 Inherited Scores

Scores may travel between:

- agencies;
- banks;
- platforms;
- employers;
- regulators;
- charities;
- professional bodies.

One institution’s score may become another institution’s input.

Risks include:

- stale labels;
- missing original evidence;
- no correction route;
- apparent independent confirmation;
- escalating severity.

A borrowed score can become more powerful each time it travels farther from its source.

The receiving institution may know only:

- the category;
- the warning;
- the recommended caution.

It may not know:

- how the score was created;
- what evidence supported it;
- whether it was disputed.

---

## 🔁 Feedback Features

Intervention outcomes may return as new features.

Examples include:

- reduced contact;
- job loss;
- distress;
- isolation;
- fewer public appearances;
- changed communication;
- withdrawal from institutions.

The system may treat these as evidence of:

- instability;
- weakness;
- concealment;
- declining legitimacy;
- failed integration.

The score can absorb the damage caused by the score and call it fresh evidence.

This connects directly to [👁️ From Observation To Intervention](./👁️_from_observation_to_intervention.md).

A feedback loop must distinguish:

- behaviour that existed before intervention;
- behaviour produced by intervention;
- behaviour unrelated to the model.

---

## 👤 Human Review

A system may claim to include a human in the loop.

But meaningful review requires more than presence.

The reviewer may:

- correct context;
- rubber-stamp the score;
- see only the final category;
- lack authority to override;
- face pressure to follow the recommendation.

Questions include:

- Does the reviewer see source data?
- Can they inspect uncertainty?
- Can they record disagreement?
- Can they override the score?
- Is override penalised?
- Is the review independent?

Human review is not meaningful when the human sees only the machine’s conclusion.

---

## 🧠 Automation Bias

People may trust scores because they:

- look precise;
- are standardised;
- came from a technical system;
- appear less subjective;
- resemble scientific measurement.

Numerical form can turn a weak inference into an institutionally respectable fact.

Automation bias may lead reviewers to:

- defer;
- stop asking questions;
- discount contradictory evidence;
- treat uncertainty as resolved.

The apparent objectivity of the score may become more powerful than the evidence beneath it.

---

## 🌀 Score Drift

A score’s meaning may change over time.

Causes include:

- new data;
- new policy;
- altered weights;
- changed thresholds;
- different institutional purpose;
- revised categories.

A person may move categories without changing behaviour.

The person may remain the same while the model moves around them.

This creates problems for:

- explanation;
- consistency;
- appeal;
- historical comparison.

A score should therefore record:

- model version;
- weights;
- threshold;
- date;
- intended use.

---

## 🏺 Population And Historical Bias

Historical data may reflect:

- over-policing;
- discriminatory reporting;
- unequal access;
- institutional prejudice;
- previous targeting;
- selective documentation.

A model trained on those records may reproduce the past.

A model trained on unequal treatment may learn inequality as if it were risk.

Removing explicit protected characteristics may not remove discrimination.

The pattern may persist through proxies.

Historical data are not neutral merely because they are old.

---

## 🧬 Sensitive And Protected Characteristics

Scores may infer or encode:

- religion;
- ethnicity;
- nationality;
- disability;
- sexuality;
- political belief;
- family origin.

Even where explicit variables are excluded, proxies may remain.

Examples include:

- postcode;
- language;
- institution;
- travel;
- family network;
- cultural participation;
- employment history.

A protected characteristic does not disappear merely because the model gives it another name.

Sensitive inferences require:

- strict necessity;
- proportionality;
- transparency;
- oversight;
- challenge rights.

---

## 🕸️ Scoring Relationships Rather Than People

Scores may attach to:

- pairs;
- groups;
- institutions;
- potential coalitions;
- relationship types.

A person’s score may change depending on:

- whom they contact;
- who contacts them;
- what capacity the relationship creates;
- whether they connect separate networks;
- whether they provide protection or credibility.

The unit being scored may not be the person.

It may be the possibility between people.

This prepares the move into:

- [🧮 The Disruption Score](./🧮_the_disruption_score.md);
- [🕸️ Relationship Risk, Not Person Risk](./🕸️_relationship_risk_not_person_risk.md).

---

## 🔍 Explainability

A meaningful explanation should reveal:

- input data;
- derived features;
- weights;
- threshold;
- confidence;
- decision route;
- model version;
- source lineage.

Weak explanations include:

- “automated checks”;
- “risk indicators”;
- “multiple factors”;
- “internal criteria.”

An explanation that names no feature, weight, or threshold is not an explanation.

It is a refusal in technical language.

Explainability must be specific enough to support challenge.

---

## ⚔️ Contestability

A person affected by a score should be able to:

- inspect relevant data;
- challenge identity matches;
- correct stale relationships;
- contest inferences;
- seek meaningful human review;
- receive reasons;
- propagate corrections;
- obtain remedy.

Appeal after intervention may be inadequate.

The relationship may already be damaged.

The job may already be lost.

The account may already be restricted.

A score that cannot be challenged is not merely analysis.

It is authority.

---

## 🛡️ Minimum Governance Questions

Any scoring system should answer:

- What outcome is the score intended to predict?
- What records enter it?
- Which inputs are facts, proxies, or predictions?
- How are identities matched?
- What features are derived?
- What weights apply?
- How is missing data treated?
- What population provides the baseline?
- What threshold triggers action?
- Is the score descriptive, predictive, or prescriptive?
- Does it score a person, relationship, group, or institution?
- Is the score inherited from another system?
- Are duplicate signals counted?
- Can a reviewer override it?
- Can the subject inspect and challenge it?
- What happens when the score is wrong?
- Are intervention effects fed back into the model?
- What evidence would falsify the model’s conclusion?
- Are protected characteristics encoded through proxies?
- Can corrections propagate across institutions?

A system that cannot answer these questions should not treat its output as objective authority.

---

## ⚠️ What This Node Is Not Claiming

This node does not claim that:

- a numerical score is automatically objective;
- a high score proves dangerous conduct;
- multiple inputs automatically constitute corroboration;
- confidence equals truth;
- human review automatically creates accountability;
- capability to score proves use in a particular case;
- a hypothetical feature set proves a deployed model;
- scoring errors automatically prove malicious intent.

The node identifies:

- scoring capability;
- decision points;
- proxy risks;
- threshold governance;
- feedback loops;
- accountability requirements.

Specific claims require specific evidence.

---

## 🧿 Compact Definition

**From Records To Scores** describes the transformation of raw records into numerical or categorical judgements.

The pipeline may include:

- entity matching;
- feature derivation;
- proxy selection;
- weighting;
- normalisation;
- thresholding;
- recommendation.

The central danger is not only that the score may be wrong.

It is that judgement may disappear inside the number, while the number continues to govern.

---

## 🧮 Next Movement

Once records have been converted into scores, the system can ask a more operational question:

> Where is interference expected to reduce the most collective capacity at the lowest cost?

The next node, [🧮 The Disruption Score](./🧮_the_disruption_score.md), develops that hypothetical composite model.

It asks how systems might combine:

- importance;
- relational capacity;
- access;
- dependency;
- intervention cost;
- backlash risk.

---

## 🌌 Constellations

📊 🧩 ⚖️ 🚦 🕸️ — scoring; features; weights; thresholds; relationship possibility.

## ✨ Stardust

risk scoring, feature engineering, proxies, thresholds, confidence, composite scores, inherited scores, automation bias, explainability, contestability

---

## 🏮 Footer

*📊 From Records To Scores* is a living node of the **Polaris Protocol**.  
It examines how records become features, weights, thresholds, rankings, and recommendations—and how policy choices may disappear inside apparently objective outputs.

> 📡 Cross-references:
>
> - [👁️ From Observation To Intervention](./👁️_from_observation_to_intervention.md) — *the transition from seeing to acting*  
> - [🩸 Feed Me Data](../🩸_Feed_Me_Data/README.md) — *the records entering the scoring pipeline*  
> - [💾 What The Database Eats](../🩸_Feed_Me_Data/💾_what_the_database_eats.md) — *data inputs, proxies, and context collapse*  
> - [🕸️ Social Graphs And Network Analysis](../🩸_Feed_Me_Data/🕸️_social_graphs_and_network_analysis.md) — *network features and relational metrics*  
> - [🔭 Capability, Not Allegation](../🧭_Orientation/🔭_capability_not_allegation.md) — *the central evidentiary guardrail*  
> - [🔬 The Smallest Claim First](../🧭_Orientation/🔬_the_smallest_claim_first.md) — *testable claims and disproof conditions*  
> - [🧮 The Disruption Score](./🧮_the_disruption_score.md) — *the next node in the cluster*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-07-20_
