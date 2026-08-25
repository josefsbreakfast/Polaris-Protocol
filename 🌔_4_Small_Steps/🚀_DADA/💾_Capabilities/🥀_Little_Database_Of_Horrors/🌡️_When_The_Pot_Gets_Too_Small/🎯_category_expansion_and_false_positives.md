# 🎯 Category Expansion And False Positives
**First created:** 2026-07-17 | **Last updated:** 2026-08-25  
*How pressure for greater coverage can widen categories, lower thresholds, and expose increasingly large populations to consequential error.*

---

## 🛰️ Orientation

The model is not certain enough.

So the category gets bigger.

This can feel like a practical solution.

If the system missed somebody because the definition was too narrow, widen the definition.

If one indicator was insufficient, combine several.

If known actors are difficult to identify early, include associates.

If direct relationships miss important networks, add indirect relationships.

If a binary category is too crude, create several intermediate categories.

If officials cannot identify exactly who will become consequential, identify everyone who might.

Coverage improves.

So does the number of people who do not belong there.

That is the central trade-off of this node:

> **A system can catch more true cases by catching more false ones.**

Whether that trade is acceptable depends on what the category does.

A broad category used to decide what receives a second look is one thing.

A broad category that restricts travel, damages reputation, shapes policing, alters access, or follows a person across institutions is another.

The problem is not simply that categories expand.

It is that **the consequences of being inside them may expand too**.

---

## 🎯 Categories Are Decisions About Boundaries

A category is not discovered in nature.

Someone defines it.

Even apparently simple classifications require decisions about:

- inclusion;
- exclusion;
- threshold;
- time;
- evidence;
- uncertainty;
- exceptions.

Consider a category such as:

> associate.

How much contact counts?

Recent contact?

Historical contact?

One meeting?

Regular communication?

A shared organisation?

A mutual contact?

An inferred connection?

Does the category distinguish:

- friend;
- colleague;
- lawyer;
- journalist;
- relative;
- adversary;
- investigator;
- service provider?

If not, a technically accurate statement —

> these two people are connected

— may conceal a much more uncertain proposition:

> this connection is relevant to the risk being assessed.

The category therefore does analytical work before the score ever appears.

---

## 📈 Sensitivity Has A Price

A system designed to find more possible cases can often increase its sensitivity.

It can:

- lower thresholds;
- accept weaker indicators;
- use more proxies;
- expand graph depth;
- lengthen retention;
- widen population coverage;
- combine more datasets.

This may reduce false negatives.

It may also increase false positives.

That trade-off is not automatically bad.

Medical screening, fraud detection, safeguarding, intelligence triage, and many other systems deliberately tolerate false positives at an early stage because missing a true case may be costly.

But early-stage screening usually assumes something important:

> **the positive result is not the final conclusion.**

It triggers further assessment.

A screening category becomes dangerous when the institution forgets that it was designed to over-include.

---

## 🚨 The Screening Result Becomes The Identity

A common failure occurs when a category created for triage begins travelling downstream.

At the first stage:

> possible concern.

At the next:

> risk marker.

Then:

> known risk.

Then perhaps:

> risky person.

The language has changed.

The evidence may not have.

This can happen because downstream users do not see:

- why the category was created;
- how sensitive it was designed to be;
- what the false-positive rate is;
- which caveats applied;
- whether the information was ever reviewed.

A temporary screening state can harden into an institutional identity.

> **The flag survives the reason for the flag.**

---

## 🕸️ Association Expands Faster Than Conduct

Relationship systems are especially vulnerable to category expansion because association is abundant.

If a system begins with:

> people suspected of harmful conduct

and expands to:

> their direct associates

the population can grow quickly.

Add:

> associates of associates

and it grows again.

Add:

- shared events;
- common organisations;
- financial links;
- co-location;
- family;
- online interaction;
- mutual contacts;

and the graph can encompass people with increasingly weak relationships to the original concern.

The system may still describe all of them using the language of connection.

But connection is not a constant quantity.

A spouse is not a retweet.

A lawyer is not a co-conspirator.

A journalist's source contact is not political allegiance.

A person attending the same public meeting is not necessarily part of the same organisation.

> **Graph distance is not evidential distance unless the system can explain what the edge means.**

---

## 🪜 The Ladder From Conduct To Context

Category expansion often proceeds gradually.

A simplified ladder might look like:

1. documented harmful conduct;
2. credible suspicion of harmful conduct;
3. direct operational support;
4. close association with a relevant actor;
5. indirect association;
6. shared institution or event;
7. demographic, geographic, political, or behavioural similarity;
8. contextual resemblance to previous cases.

Every step may add information.

Every step also moves further from the conduct that originally justified attention.

The analytical question should therefore become stricter, not looser:

> **What additional inference is being made at this rung, and what consequence is that inference allowed to support?**

A system can use contextual information intelligently.

It should not allow context to impersonate conduct.

---

## 🏷️ Intermediate Categories Can Become Permanent

One response to uncertainty is to avoid binary classification.

Instead of:

> safe / dangerous

the system creates:

- low concern;
- moderate concern;
- elevated concern;
- high concern;
- unknown;
- monitor;
- review;
- priority.

This can be more honest.

Human risk rarely fits a binary.

But intermediate categories create their own governance problem.

What does “moderate concern” actually do?

Does it:

- expire;
- trigger review;
- increase surveillance;
- alter access;
- affect travel;
- change policing;
- travel to another institution;
- influence future scoring?

If the category produces consequences but lacks a clear route back out, uncertainty has merely been converted into a durable administrative state.

> **A middle category needs an exit as much as an entry rule.**

---

## ⏱️ Time Can Expand The Population Too

Categories do not only widen sideways.

They can widen backwards.

Historical records may remain relevant long after:

- a relationship ended;
- a political position changed;
- a person left an organisation;
- an investigation closed;
- an allegation was disproved;
- the original context disappeared.

Long retention can transform old association into current risk.

This is especially problematic when systems combine data collected at different times.

A current profile may silently contain:

- a ten-year-old protest;
- an obsolete address;
- a former partner;
- a closed investigation;
- an old workplace;
- a political affiliation that no longer exists.

The record may be factually historical and analytically current.

Those are not the same thing.

---

## 🧮 Cumulative Weak Signals Can Look Strong

A common modelling strategy is to combine multiple weak indicators.

That can be sensible.

No single variable may predict much, while several together provide useful information.

But accumulation can create false confidence if the signals are:

- correlated;
- derived from the same source;
- consequences of the same underlying bias;
- different expressions of one event;
- generated by previous institutional intervention.

Suppose a person is:

- recorded at a protest;
- linked to several protesters;
- mentioned in public-order intelligence;
- flagged by a system trained partly on protest intelligence.

Those may appear to be four indicators.

They may substantially reflect one underlying fact:

> the person attended a protest.

Counting correlated signals separately can make a weak case look numerically dense.

> **More rows are not necessarily more independent evidence.**

---

## 🪞 Proxy Categories Can Smuggle In Protected Characteristics

When direct prediction is difficult, institutions may rely on proxies.

Some proxies can closely track:

- ethnicity;
- religion;
- nationality;
- disability;
- socioeconomic status;
- neighbourhood;
- migration history;
- age;
- gender.

Even if the protected characteristic is removed from the dataset, combinations of other variables may reconstruct it.

That does not mean every correlated variable is impermissible.

It means fairness cannot be assessed merely by checking whether a prohibited field is absent.

Researchers should ask:

- Who enters the category?
- Who remains in it longest?
- Who experiences the strongest consequences?
- Which variables drive inclusion?
- Are those variables causally relevant?
- Could the same purpose be achieved with less discriminatory information?

A category can be formally neutral and still reproduce an unequal history.

---

## 🚓 Policing Makes The Feedback Problem Concrete

Policing provides a clear example of why category expansion needs careful interpretation.

Suppose an area, group, or network receives increased attention.

More attention produces:

- more stops;
- more intelligence reports;
- more recorded contacts;
- more detected offences;
- more associations in police systems.

Those records can then support the conclusion that the same population contains more indicators of concern.

The original decision about where to look has become part of the evidence for looking there again.

This does not mean detected offending is unreal.

It means recorded prevalence can reflect both:

> behaviour

and:

> **measurement intensity.**

A model trained on institutional records needs to distinguish the two as far as possible.

Otherwise yesterday's enforcement pattern can become tomorrow's predictive category.

---

## 🧷 Family And Intimate Association Are Particularly Dangerous Shortcuts

Family relationships are easy to identify and often stable in administrative records.

That makes them attractive analytical variables.

They can also be profoundly misleading.

A person may:

- disagree with a relative;
- be estranged;
- have no control over them;
- be endangered by them;
- have contact only because of caregiving;
- share a surname without meaningful relationship.

Intimate and family association can matter to legitimate investigations.

But guilt, allegiance, or political risk should not be inferred simply through kinship.

The same applies to friendship, romance, religious community, and professional representation.

> **Association can explain access without establishing alignment.**

That distinction becomes critical when categories widen under political pressure.

---

## 🌍 Diasporas Are Especially Exposed To Category Creep

Diaspora populations can accumulate many variables that become security-relevant during external or internal crisis:

- foreign family;
- travel;
- remittances;
- multilingual communication;
- dual nationality;
- community organisations;
- religious institutions;
- political interest in another country;
- contact with embassies;
- contact with dissidents;
- humanitarian activity.

Each may be ordinary.

Combined, they can create a profile that looks unusually dense to a system built around domestic baseline assumptions.

This is one reason comparative validation matters.

A model calibrated on a population with fewer cross-border relationships may overclassify people for whom transnational life is normal.

The system can mistake:

> **diaspora-ness**

for:

> **anomalous foreign connection.**

That is not merely a technical problem.

It can become discriminatory governance.

---

## ⚖️ False Positives Are Not Harmless Because They Are Temporary

Institutions sometimes defend broad categories on the basis that they merely trigger further review.

That may be proportionate.

But review itself can have costs.

A false positive can produce:

- delay;
- repeated questioning;
- financial friction;
- travel disruption;
- lost opportunities;
- increased surveillance;
- reputational damage;
- anxiety;
- altered treatment by institutions;
- information sharing;
- records that persist after clearance.

The relevant question is therefore not only:

> Was the person eventually cleared?

It is:

> **What happened to them while the system was deciding?**

And afterwards:

> **Did the clearance propagate as efficiently as the suspicion did?**

Suspicion that travels faster than correction creates a particularly durable form of administrative harm.

---

## 🧹 Correction Must Shrink The Category

A functioning system needs mechanisms that can genuinely reduce classification.

Evidence against the hypothesis should matter.

A corrected record should propagate.

An expired association should stop carrying current weight.

A closed investigation should not remain indistinguishable from an active one.

A person should be able to leave an intermediate category when its criteria are no longer met.

If categories only expand, the system is not performing risk assessment.

It is accumulating people.

Useful questions include:

- What lowers a score?
- What removes a flag?
- What expires automatically?
- What requires human review?
- Does exculpatory information travel?
- Are old inferences recalculated after correction?
- Can linked records be separated?
- Can the institution identify how many people have ever left the category?

A category with no meaningful exit is not simply cautious.

It is sticky.

---

## 🧯 The Difference Between Broad Screening And Broad Coercion

Broad inclusion can sometimes be justified when consequences remain light and review is strong.

For example:

> broad signal → human assessment → no further action unless corroborated.

The danger rises when the pathway becomes:

> broad signal → durable flag → information sharing → consequential intervention.

So proportionality should be assessed across the entire pipeline.

The relevant design questions are:

- How broad is the entry rule?
- How serious is the consequence?
- How independent is the corroboration?
- How easy is correction?
- How long does the category persist?
- How widely does it travel?

A system can tolerate greater uncertainty at the beginning only if it becomes more demanding before imposing serious consequences.

> **Wide gates require narrow exits into coercion.**

---

## 📣 Political Pressure Rewards Visible Coverage

Category expansion can also be institutionally attractive because it produces visible evidence of action.

After a crisis, leaders may want to demonstrate that:

- more cases are being reviewed;
- more networks are being mapped;
- more threats are being identified;
- more referrals are being made;
- more institutions are sharing information.

Those metrics can show activity.

They do not necessarily show effectiveness.

A system that doubles the number of people flagged may look more vigilant.

If most additional flags are false positives, it may instead have become less discriminating.

Coverage is therefore not a success metric by itself.

Neither is the number of alerts.

The relevant question is:

> **Did expansion improve the institution's ability to distinguish the relevant cases from everyone else?**

---

## 🧠 Humans Adapt To Categories

People do not remain passive when institutions classify them.

They may change behaviour.

They may:

- avoid certain events;
- stop contacting people;
- change platforms;
- seek legal advice;
- alter financial routes;
- become more cautious;
- withdraw from institutions.

Some adaptations may be benign.

Some may be harmful.

Some may make the underlying behaviour harder to observe.

A system can then interpret the changed behaviour as evidence that the category was correct.

That is where category expansion begins moving towards the next failure.

If someone does not behave as predicted, perhaps they are concealing.

If the expected network is not visible, perhaps it is hidden.

If the evidence is weak, perhaps the target has become sophisticated.

At that point, error stops correcting the model.

It starts protecting it.

---

## 🔎 What Would We Look For?

Evidence of category expansion may include:

- broader statutory or policy definitions;
- lower referral thresholds;
- expanded watchlist criteria;
- increased graph depth;
- more indirect associations;
- new intermediate risk categories;
- longer retention;
- broader data linkage;
- more proxy variables;
- increased numbers of people flagged without corresponding growth in substantiated cases;
- screening categories producing downstream consequences;
- old associations remaining operationally current;
- corrections failing to propagate;
- protected groups disproportionately entering or remaining in categories;
- repeated institutional claims that wider coverage itself demonstrates improved security.

No single indicator establishes abuse.

The important pattern is whether expansion improves discrimination or merely increases the population subject to suspicion.

---

## 🧭 Questions For Every Category

For any consequential category, ask:

1. What is the category for?
2. Who defined it?
3. What is the entry threshold?
4. What evidence counts?
5. What does not count?
6. How are indirect associations treated?
7. How many graph hops are permitted?
8. Are signals independent?
9. What is the expected false-positive rate?
10. What is the relevant base rate?
11. Which populations are disproportionately included?
12. Which proxies drive inclusion?
13. What consequences follow?
14. Does the category travel to other institutions?
15. How long does it persist?
16. What lowers the classification?
17. What removes it?
18. Does correction propagate?
19. Can historical relationships expire?
20. What observation would show that the category has become too broad?

A category should be capable of failing its own test.

Otherwise the category is not being evaluated.

Only the people inside it are.

---

## 🪤 The Next Failure

A healthy model treats contradictory evidence as useful.

A person repeatedly predicted to behave one way behaves another way.

The institution updates.

A relationship classified as threatening proves irrelevant.

The score falls.

A suspected network fails to materialise.

The hypothesis weakens.

But a pressured system has another option.

It can reinterpret contradiction as evidence of sophistication.

The missing connection is hidden.

The unexpected behaviour is deception.

The absence of evidence demonstrates concealment.

The model has stopped learning from error.

Continue to [🪤 When Error Is Reclassified As Concealment](./🪤_when_error_is_reclassified_as_concealment.md) — *how a risk model becomes increasingly difficult to falsify when contradictory observations are absorbed as evidence that the target is hiding the very behaviour the system expected to find*.

---

## 🌌 Constellations

🎯 📈 🕸️ 🚓 🧹 — category expansion; prediction pressure; association; measurement feedback; correction and exit.

---

## ✨ Stardust

false positives, category expansion, risk classification, watchlists, social graphs, screening, proxy variables, policing data, diaspora monitoring, correction, retention

---

## 🏮 Footer

*🎯 Category Expansion And False Positives* is a living node of the **Polaris Protocol**.  
It examines how institutions seeking greater coverage can widen thresholds, associations, populations, retention, and proxy variables faster than they improve the underlying quality of inference. The node distinguishes broad screening from consequential classification and treats correction, expiry, provenance, and meaningful exit as essential safeguards against suspicion becoming a permanent administrative identity.

> 📡 Cross-references:
>
> - [🌡️ When The Pot Gets Too Small](./README.md) — *parent branch mapping how political stress can turn model uncertainty into institutional expansion*
> - [📈 Demanding More Certainty From A Bad Model](./📈_demanding_more_certainty_from_a_bad_model.md) — *the preceding stage: pressure for categorical answers from incomplete and probabilistic evidence*
> - [🕸️ Relationship Risk Not Person Risk](../🎶_Suddenly_Surveillance/🕸️_relationship_risk_not_person_risk.md) — *why the significance assigned to relationships can expand beyond the risk attributed to either person individually*
> - [🧬 Family, Friendship And Intimate Relationships](../🩸_Feed_Me_Data/🧬_family_friendship_and_intimate_relationships.md) — *how intimate and family connections become legible as data without thereby establishing allegiance or shared intent*
> - [🪓 Don't Feed The Model](../🪓_Dont_Feed_The_Model/) — *stopping rules, review, deletion, correction, prohibited inference, and closure when expansion ceases to be proportionate*
> - [🪤 When Error Is Reclassified As Concealment](./🪤_when_error_is_reclassified_as_concealment.md) — *the next escalation stage: contradictory evidence ceases to correct the model and is instead absorbed as confirmation*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-25_
