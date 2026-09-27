# 📋 Exhibit H: Radicalised Algorithms

**First created:** 2026-09-27 \| **Last updated:** 2026-09-27\
*The Special Relationship has a metadata problem. Unfortunately, this
appears to have escalated from "which fucking BBC?" into international
AI governance.*

------------------------------------------------------------------------

Tldr:  

**Ticket A — social:**

> America, could you perhaps stop encoding centuries of racial mythology about Black men into sexual taxonomies?
> That would be lovely.


**Ticket B — security/engineering:**

> Until such a time as Ticket A is resolved, could we at minimum establish whether those and other behavioural signals are contaminating, distorting, or making exploitable the information systems through which allied populations receive news?  

--- 

## 🛰️ Orientation

There are two useful ways to begin a serious discussion about
algorithmic radicalisation.

One is to begin with terrorism, political extremism, recommender
systems, stochastic models, platform incentives, national security,
international law, clinical risk, and the genuinely difficult problem of
determining causation inside a computational information environment.

The other is to ask America why its weird racialised pornography
category has the same initials as the British Broadcasting Corporation.

We will be taking the second route.

This is not because the first route is unimportant.

It is because before asking whether a computational system can
contribute to somebody becoming radicalised, distressed, paranoid,
delusional, compulsive, misinformed, or otherwise magnificently fucked
up, it is worth establishing something more primitive:

> **Does the machine know what the information means?**

Britain has a public-service broadcaster called the **BBC**.

The internet also contains a racialised pornography category abbreviated
**BBC**, meaning "big Black cock".

These are not, for most British human beings, particularly difficult
concepts to distinguish.

``` text
BBC News
→ probably the British Broadcasting Corporation

BBC porn
→ unfortunately, America has entered the chat
```

But a computational system does not receive meaning by divine
revelation.

It encounters tokens, tags, co-occurrences, links, query histories,
embeddings, classifications, popularity signals, metadata, behavioural
traces, training examples, and whatever contextual information the
system has been designed to retain.

The letters do not contain the distinction.

The **context does**.

> 🇬🇧: BBC.
>
> 🇺🇸: ...Ah.
>
> 🇬🇧: **THE FACT THAT YOU IMMEDIATELY SAID "AH" IS THE ISSUE.**

This node does **not** claim that modern search engines are generally
unable to distinguish "BBC News Ukraine" from pornography. Many systems
perform sophisticated semantic and entity disambiguation.

The collision is useful because it is funny, obvious, culturally
asymmetric, and capable of demonstrating the underlying engineering
problem without first requiring anybody to understand the entire
machine-learning stack.

**The specimen is stupid. The problem is not.**

------------------------------------------------------------------------

## 1. 🏷️ A Tag Is Not A Meaning

`BBC` is not one stable informational object.

Meaning emerges from a relationship:

``` text
token
+
surrounding information
+
prior information
+
observer / system
+
task being performed
=
interpreted information
```

A British reader encountering:

> BBC announces new documentary

will usually reach one interpretation immediately.

A pornography platform processing:

> BBC interracial compilation

will reach another.

A search engine may use surrounding terms to resolve the difference.

A moderation system may use another classifier.

An advertising system may inherit a category from somebody else.

A recommender may never need to resolve the acronym explicitly at all;
it may operate on learned statistical relationships.

A downstream model may inherit associations from a corpus whose
provenance has already been partially lost.

The important distinction is:

> **Data fusion ≠ ontology fusion ≠ semantic disambiguation.**

Putting more information into the same computational environment does
not automatically mean the information has been correctly separated into
the concepts human beings intended.

And sometimes the most intelligent answer available to a machine should
be:

``` text
BBC

POSSIBLE REFERENTS:
- British Broadcasting Corporation
- racialised pornography category
- other acronym expansions

CONTEXT:
insufficient

ACTION:
DO NOT FUCKING GUESS YET
```

That final state matters.

**Uncertainty is information.**

A system that is forced to classify before it possesses enough context
has not eliminated uncertainty.

It has merely hidden it inside an answer.

------------------------------------------------------------------------

## 2. 🇺🇸 We Regret To Inform You This One Actually Is Your Problem

The pornography meaning is not culturally neutral metadata.

The "BBC" sexual stereotype sits inside a much older racial history in
which Black men have been constructed as hypersexual, physically
excessive, threatening, animalistic, sexually dominant, or reducible to
genital size.

Contemporary scholarship continues to document that structure. Research
on pornography describes the "big Black cock" category as reproducing
racial stereotypes that reduce Black men to genitalia and sexual
performance. Work specifically examining Pornhub tagging argues that
racialised tagging systems can encode and reproduce a white racial gaze,
with automation and machine learning helping to sort that material at
scale.

So:

> **ITS YOUR WEIRD RACIALISED PORN CATEGORY, LADS.**

This does **not** mean:

-   every American consumes this material;
-   British people do not consume it;
-   every person who searches for racialised pornography holds the same
    racial beliefs;
-   pornography consumption can be read straightforwardly as political
    ideology;
-   anonymous population-level search patterns reveal the motive of an
    individual user.

Those would be bad inferences.

It does mean that racial history has become machine-readable taxonomy.

That is already interesting.

``` text
racial history
      ↓
sexual stereotype
      ↓
commercial category
      ↓
search term / tag
      ↓
behavioural measurement
      ↓
machine-readable association
```

At which point Britain would merely like to note that the letters are
also attached to the national broadcaster.

🦊: **Cousin. Your pornography metadata is interfering with my
educational example.**

🇺🇸: That's not our fault.

🦊: **The category is literally in English and deeply entangled with
your racial history. I am giving you at least partial custody of the
problem.**

------------------------------------------------------------------------

## 3. 🪞 The People Who Understood The Data Were Talking Before We Built The Machine

None of this was discovered by computer science.

Black people did not need a recommender-system paper to notice racial
objectification.

Black intellectual traditions had been analysing the construction of
Black bodies, sexuality, fantasy, fear, desire, colonialism, and social
hierarchy for generations before anybody decided to put the resulting
culture into a vector space.

Frantz Fanon's *Black Skin, White Masks* is an obvious waypoint rather
than an origin point. Fanon examined the way colonial racism enters
language, embodiment, sexuality, fantasy and subjectivity. His work has
serious limitations and has been extensively extended, criticised and
reworked by later Black, feminist and queer scholarship.

That genealogy matters because otherwise the history becomes:

> clever white theorist notices desire → computer scientist invents
> algorithm → society discovers race

which would be an absolutely spectacular way of demonstrating the
information-loss problem while attempting to explain it.

A better genealogy is:

``` text
Black lived knowledge
      ↓
Black intellectual and political traditions
      ↓
Fanon and other anti-colonial analysis
      ↓
Black feminist / queer / intersectional scholarship
      ↓
sex workers and other situated observers
      ↓
platform studies
      ↓
computer science discovers it has encoded the entire fucking thing
```

Two propositions matter here:

> **The people who can explain the machine are not necessarily the
> people who can explain the data.**

And:

> **The people who understood what the data meant were talking long
> before we built the fucking machine.**

If a computational system discounts observers because of social position
while that social position gives them unusual access to the phenomenon
being modelled, the system has not become more objective.

**It has thrown away a fucking sensor.**

------------------------------------------------------------------------

## 4. 👠 Situated Knowledge Is Still Knowledge

There is another information source here.

I am a former sex worker.

I am not proposing the possible coexistence of racial hostility, racial
anxiety, racial fetishisation and sexual curiosity because I looked at a
Pornhub graph and developed an exciting theory.

I have watched versions of that contradiction happen between actual men
and actual sex workers.

Other sex workers recognised it too.

That testimony does not establish why every anonymous user clicked a
category. It does not turn ecological search data into individual
psychology. It does not allow me to diagnose the political commitments
of somebody because of what pornography they watched.

It does provide a reason to ask whether a pattern familiar from sexual
labour may also appear at population scale.

The empirical literature independently documents several components:

-   racial fetishisation;
-   hypersexual construction of Black masculinity;
-   the "BBC" stereotype;
-   racialised pornography categories;
-   racial stratification in sexual labour;
-   the translation of those categories into platform tagging and
    searchable metadata.

That is enough to make the question scientifically respectable without
pretending the causal chain has already been proven.

> **Academics may wish to investigate the precise causal mechanism.
> Former sex worker would meanwhile like to enter into evidence: lads, I
> have fucking met these men.**

This is one reason Embodied Information Ecology refuses the fantasy that
all useful information arrives wearing a university lanyard.

------------------------------------------------------------------------

## 5. 🕸️ When Adaptation Becomes Training Data

Black feminist analysis gives us another particularly important systems
problem.

People do not behave inside neutral environments.

They adapt to environments containing rewards, punishments, stereotypes,
expectations, gatekeepers and risks.

Consider:

``` text
unequal environment
      ↓
person adapts behaviour
      ↓
adapted behaviour receives greater reward
      ↓
system records successful behaviour
      ↓
successful adaptation becomes model of "preferred behaviour"
      ↓
future people encounter stronger incentive to adapt
      ↺
```

This is a feedback loop.

The system may then look at the resulting behaviour and conclude:

> Ah. This is what people like.

Maybe.

Or perhaps this is what people learned they had to do.

**Selection pressure can masquerade as preference.**

And:

> **Measurement of adaptation ≠ measurement of unconstrained
> preference.**

This matters in employment systems, entertainment, sex work,
professional environments, advertising, recommendation, language models
and any other computational environment that learns from behaviour
generated under unequal social conditions.

A dataset can be perfectly accurate about what happened and still be
profoundly misleading about **why it happened**.

------------------------------------------------------------------------

## 6. 🥥 Context Is Part Of The Information

The same problem appears in language.

A word is not always adequately represented by:

``` text
TOKEN → MEANING
```

Sometimes the informational object is closer to:

``` text
TOKEN
+ speaker
+ target
+ relationship
+ history
+ community
+ setting
+ intention
+ surrounding speech
→ meaning / speech act
```

This is why intra-community language can become such a nightmare for
crude moderation systems.

The British "coconut" controversy is useful precisely because different
observers processed the same lexical object through different histories
and social relationships. Jewish communities have their own extremely
charged internal vocabulary; "Kapo" provides an experiential analogue
for how speaker, target, history and intra-community relationship can
change the informational content of an utterance.

These terms are **not equivalent**.

The point is the structure.

A term may function as internal criticism, political accusation,
authenticity policing, trauma expression, satire, abuse, reclamation, or
some mixture whose meaning depends on who is speaking to whom and why.

None of that means context magically makes every use acceptable.

It means:

> **Context is not an excuse applied after meaning has been established.
> Context is part of the information required to establish meaning.**

A machine that lacks those variables may be very confident while missing
the fucking object it is supposedly classifying.

🤖: `BAD WORD PROBABILITY: 0.973`

🦊: **Cousin, I regret to report your computer has misplaced context.**

------------------------------------------------------------------------

## 7. 🐟 Fisher, Capital, And The Machine That Measures Desire

Mark Fisher did not invent recommender systems.

He was not secretly doing machine learning with a cigarette outside
Goldsmiths.

His usefulness here is political economy.

*Capitalist Realism* and the later *Postcapitalist Desire* lectures form
part of a larger argument about capitalism's relationship to culture,
subjectivity and desire: markets do not merely sit outside human wanting
and wait politely for preferences to arrive. Economic structures help
organise the environments in which desires are formed, expressed,
channelled and monetised.

Digital platforms add an extraordinary implementation mechanism.

``` text
commercial objective
      ↓
observe behaviour
      ↓
select media
      ↓
human experiences selected environment
      ↓
human responds
      ↓
measure response
      ↓
update selection
      ↺
```

**Fisher supplied part of the political economy. Computer science
subsequently supplied an extraordinarily powerful implementation
mechanism.**

Pornography is a useful specimen because everything embarrassing is
visible at once:

-   desire;
-   commercial incentive;
-   race;
-   gender;
-   taxonomy;
-   behavioural measurement;
-   search;
-   recommendation;
-   cultural history;
-   platform infrastructure.

Fisher: capital captures and instrumentalises desire.

Computer scientist: the machinery measures behavioural responses and
iteratively selects subsequent stimuli.

Sex workers: **Guys.**

Black scholars: **Guys.**

Feminist scholars: **Guys.**

Platform: 📈

Fisher's ghost: **For fuck's sake.**

------------------------------------------------------------------------

## 8. 🔄 Cousin, Your Fetishes Have Entered The Information Supply Chain

Now we can be more precise about the algorithmic problem.

This node does **not** claim:

``` text
Americans watch weird porn
      ↓
BBC News directly changes
```

That would require evidence about a specific technical pathway.

The defensible systems claim is broader:

``` text
people behave
      ↓
platforms record behaviour
      ↓
rankings / tags / search outputs / associations change
      ↓
other computational systems observe outputs
      ↓
datasets / models / analytics inherit some signals
      ↓
statistical environment changes
```

The degree to which this occurs depends on the systems involved.

But the general vulnerability matters:

# You Do Not Always Have To Hack The Algorithm

Sometimes you alter the environment the algorithm learns from.

This is why data poisoning, feedback loops, semantic drift, popularity
manipulation, coordinated behaviour and downstream data dependency
matter.

The jurisdiction of the user is not necessarily the jurisdiction of the
computational infrastructure shaping the information environment.

British public-service journalism travels through global search engines,
social platforms, app stores, browsers, operating systems, analytics
systems, advertising infrastructure, model ecosystems and other
computational intermediaries.

Nobody has to target the BBC deliberately for foreign behaviour to
become part of the computational environment through which BBC
journalism travels.

🦊: **Cousin. Your fetishes have entered the information supply chain.**

🇺🇸: That seems unnecessarily personal.

🦊: **YOU NAMED THE TAG BBC.**

------------------------------------------------------------------------

## 9. 🧜‍♀️ Peter, You Have Two Fucking Axes

Before we get to radicalisation, we require a small logic break.

A recurring technology argument quietly slides between different
meanings of **good**.

For example:

``` text
MORAL AXIS
good ←────────────────→ evil

FUNCTIONAL AXIS
effective ←────────────→ ineffective
```

These are not one axis.

A system can be:

-   morally desirable and effective;
-   morally desirable and ineffective;
-   morally abhorrent and effective;
-   morally abhorrent and ineffective.

Likewise:

``` text
profitable ≠ safe
engaging ≠ beneficial
popular ≠ true
retained user ≠ flourishing user
effective at objective X ≠ morally good
```

Efficiency is incomplete without an objective.

`efficient_at(system, objective)`

does not entail:

`good(system)`

This matters because optimisation systems are extremely capable of doing
what they are rewarded for.

The unanswered question is:

> **Rewarded for fucking what?**

🧜‍♀️ LOOK AT THIS STUFF, ISN'T IT NEAT\
WOULDN'T YOU THINK MY COLLECTION'S COMPLETE?

No.

**YOU HAVE TWO FUCKING AXES.**

The exact contemporary Peter Thiel example that prompted this section
requires the original interview/transcript to be pinned before
quotation. The conceptual error does not.

🦊: **Cousin, your billionaire has just explained the bug.**

------------------------------------------------------------------------

## 10. 📈 "But It Makes Us Money"

The Fox is not anti-business.

The Fox is disappointed because America is very good at engineering and
has occasionally mistaken **commercial success** for evidence that an
information system is functioning well according to every objective
anybody else cares about.

These are not the same proposition.

A product can be magnificently profitable while generating externalities
that do not appear on the manufacturer's revenue line.

So:

> 🇺🇸: But our products are enormously profitable.
>
> 🦊: Cousin. "Made in Britain" products falling apart in 4.5 seconds is
> our joke. Get your own USP.
>
> 🇺🇸: We built the global information infrastructure.
>
> 🦊: Then it is especially important that it works.
>
> 🇺🇸: It does work.
>
> 🦊: It has confused the national broadcaster with a pornography
> category.
>
> 🇺🇸: That's an edge case.
>
> 🦊: THE EDGE CASE IS CURRENTLY RUNNING A COUNTRY'S INFORMATION
> ENVIRONMENT, COUSIN.

Commercial success demonstrates success against **some objective
functions**.

It does not demonstrate:

-   semantic accuracy;
-   social benefit;
-   clinical safety;
-   democratic resilience;
-   cultural competence;
-   international interoperability;
-   absence of downstream externalities.

🇺🇸: But it makes us money.

🦊: **Cousin, you're making money out of something that is broken. I had
better hopes for you.**

Or, more simply:

🦊: **No, cousin. I understand that it is profitable. I am asking why it
is shit.**

------------------------------------------------------------------------

## 11. 🧨 And We Haven't Even Got To Far-Right Radicalisation Yet

This is the slightly alarming reveal.

Everything above happened **before** we asked whether algorithms
radicalise people.

We already needed:

-   context;
-   provenance;
-   semantic disambiguation;
-   situated knowledge;
-   cultural competence;
-   uncertainty representation;
-   feedback analysis;
-   cross-system observability;
-   incentives;
-   objective functions;
-   the ability to distinguish observed behaviour from underlying
    preference.

And now somebody would like to ask:

> Does the algorithm cause far-right radicalisation?

Excellent question.

Unfortunately:

> **We came here intending to discuss whether your computers were
> accidentally assisting fascists. During preliminary testing, we
> discovered we must first establish whether they know what "BBC"
> means.**

FOR FUCK'S SAKE, USA.

------------------------------------------------------------------------

## 12. 📱 Who Put It On His FYP?

One reason I particularly dislike the phrase **self-radicalisation** is
that it can compress very different information pathways into the same
box.

### Active retrieval

``` text
person
      ↓
actively searches
      ↓
finds extremist material
      ↓
actively searches further
      ↓
constructs information environment
```

### Human recruitment

``` text
recruiter / community
      ↓
selects and supplies material
      ↓
person engages
      ↓
relationship develops
      ↓
further material supplied
```

### Recommender-mediated exposure

``` text
person engages with some material
      ↓
platform observes engagement
      ↓
recommender selects subsequent material
      ↓
person engages
      ↓
system updates its model
      ↓
further selection
      ↺
```

Real cases may contain all three.

A person may begin with a recommendation, start searching actively, join
a community, receive material from humans, return to the platform, and
further train the recommender.

That does **not** prove the recommender caused radicalisation.

Research has produced platform-specific rather than universal findings.
A 2019 RUSI study, for example, found evidence of YouTube recommending
more extreme-right material after interaction with related content in
its experimental setup, while not finding the same effect on Reddit or
Gab. That is exactly why the pathway has to be investigated rather than
assumed.

The phrase **self-radicalisation** may tell us that there was no
conventional human recruiter.

It does not necessarily tell us who --- or what --- selected the
information environment.

> **No human recruiter ≠ no external selector.**

🦊: It says here he "self-radicalised online."

🇺🇸: Yes.

🦊: Did he select the material?

🇺🇸: Some of it.

🦊: Who selected the rest?

🇺🇸: The recommendation system.

🦊: **Then why have you written "self" in this box, cousin?**

Before arguing whether computational systems **cause** radicalisation,
stop using terminology that can erase the computational system from the
information pathway being investigated.

Then investigate the fucking pathway.

------------------------------------------------------------------------

## 13. 🧠 "AI Psychosis" Has The Same Root-Cause Problem

The emerging phrase **"AI psychosis"** creates a structurally similar
problem.

There are now published psychiatric papers using phrases such as
"AI-associated", "AI-induced", or "AI psychosis", but the literature
itself describes the construct as provisional rather than a validated
standalone clinical entity. Published work includes case reports,
proposed mechanisms and early clinical attempts to distinguish different
roles AI interaction may play.

That distinction matters.

An LLM appearing in the history does not tell us the pathophysiology of
the human being.

Publicly discussed cases may involve different combinations of:

-   psychotic-spectrum illness;
-   mood disturbance;
-   severe anxiety;
-   sleep disruption;
-   trauma-related processes;
-   compulsive or reassurance-seeking interaction;
-   substance or medication effects;
-   pre-existing vulnerability;
-   genuine disturbing model outputs;
-   model sycophancy or reinforcement;
-   anthropomorphism;
-   social isolation;
-   other factors.

These processes can overlap.

They are not interchangeable.

And they may require different clinical assessment, triage and
treatment.

The useful question is therefore not:

> **Did AI psychosis happen?**

It is:

> **What happened to this person, what did the computational system
> actually do during that process, and what causal contribution --- if
> any --- did that interaction make?**

The transcript can become clinically relevant evidence.

If a patient reports:

> The chatbot repeatedly told me X.

and the preserved interaction shows that the chatbot did repeatedly tell
them X, clinicians should not treat the **existence of X** as though it
were necessarily an internally generated perceptual event.

That still does not establish that every inference the person drew from
X was reality-based.

It means the external information environment has to be reconstructed
before somebody confidently describes what happened inside the person.

``` text
human starting state
      ↓
prompt
      ↓
model response
      ↓
human response
      ↓
model receives new context
      ↓
next response
      ↓
human state / behaviour changes
      ↺
```

**Preserve the evidence. Reconstruct the interaction. Diagnose the human
being. Debug the product.**

Do not invent a new psychiatric wastebasket because the computer was
present.

------------------------------------------------------------------------

## 14. 🩺 Computer Scientists Do Not Need To Become Psychiatrists

This is where criticism of Silicon Valley can become unnecessarily
stupid.

AI companies are building systems that now interact with:

-   medicine;
-   psychiatry;
-   psychology;
-   pharmacology;
-   education;
-   childhood development;
-   employment;
-   finance;
-   national security;
-   law;
-   democratic information systems;
-   sexual behaviour;
-   intimate relationships;
-   grief;
-   disability;
-   fucking everything.

It would be unreasonable to expect computer scientists to become
qualified experts in every domain touched by general-purpose
computational systems.

More importantly:

**we should not want them to.**

🦊: **Cousin. You employ computer scientists.**

🇺🇸: Yes.

🦊: **Why are they currently developing de facto psychiatric triage
policy?**

🇺🇸: Well---

🦊: **I have excellent news. We already have psychiatrists.**

The governance problem is therefore partly a problem of **epistemic
routing**.

When a computer-science company encounters a question requiring
psychiatry, pharmacology, child development, national-security
expertise, employment law or another specialist discipline, the answer
should not be:

> Everyone at the technology company now has to become that profession
> by Tuesday.

The answer can be:

> **We have built an interface to the people who already know this.**

------------------------------------------------------------------------

## 15. 📋 Regulation As Division Of Epistemic Labour

A regulator does not need to be an omniscient ministry of Everything The
Computer Might Touch.

That would be insane.

Its job can include knowing:

1.  what evidence the technology company must preserve;
2.  what questions the company is responsible for answering;
3.  what specialist questions belong elsewhere;
4.  which independent experts are competent to answer them;
5.  what evidentiary threshold applies;
6.  what happens when the evidence is insufficient;
7.  what escalation route applies when the risk is urgent.

For a mental-health adverse event, for example:

``` text
AI PROVIDER
      │
      ├── detect / receive possible adverse event
      ├── preserve defined evidence
      ├── document relevant system behaviour
      └── report according to threshold
                 ↓
INDEPENDENT EXPERT FUNCTION
      │
      ├── psychiatry / clinical psychology
      ├── pharmacology / neuroscience where relevant
      ├── human factors
      ├── safety engineering
      ├── statistics / epidemiology
      ├── computer science
      └── lived-experience expertise
                 ↓
BOUNDED FINDING
      │
      ├── no action required
      ├── further evidence required
      ├── monitor
      ├── modify evaluation
      ├── mitigate identified behaviour
      ├── issue clinical guidance
      └── urgent safety intervention
```

The technology company does not have to disclose every proprietary
detail to everybody.

The clinician does not have to reverse-engineer a frontier model.

The regulator does not have to practise psychiatry.

The psychiatrist does not have to understand distributed inference
infrastructure.

**The architecture has to put the right information in front of the
right expert.**

That is regulation as **division of epistemic labour**.

------------------------------------------------------------------------

## 16. ⏱️ Regulation Can Have A Fucking SLA

A legitimate industry objection is speed.

Frontier technology companies operate in an intensely competitive
environment. Some safety and regulatory questions may need answers
quickly enough that a six-month consultation cycle is functionally
useless.

Fine.

That is a **regulatory design requirement**.

It is not an argument for abandoning regulation.

``` text
ROUTINE
→ ordinary review

EXPEDITED
→ commercially time-sensitive determination

URGENT
→ safety / incident response

SYSTEMIC
→ slower investigation of structural problem
```

Governments already operate systems in which some decisions happen
slowly and others happen overnight because the consequences of delay
differ.

The choice is not:

``` text
NO REGULATION
vs
PDF SENT TO GOVERNMENT → NINE MONTHS → "THANK YOU FOR YOUR QUERY"
```

Build the fucking pathway.

A well-designed regulator can give an industry something genuinely
valuable:

## A bounded operating environment.

Instead of:

> Are we responsible for every possible human response to this model?
> Are we practising medicine? Is this a psychiatric event? Is this a
> product defect? Is this misuse? Is this an existential risk? Are we
> allowed to deploy? OH GOD.

the regulatory architecture can say:

> For this class of system, complete A, B and C. Preserve D. Report
> events meeting threshold E. Obtain opinion F from a registered
> profession. Escalate G through the urgent route. Within that envelope,
> proceed.

Regulation can reduce uncertainty.

It can also let employees say:

> **This is not my personal judgement call. The reporting criterion says
> report it.**

That is not merely restriction.

That is institutional load-bearing.

🦊: **The psychiatrist gets your question before Thursday because THERE
IS A FORM.**

------------------------------------------------------------------------

## 17. 👩‍⚕️ Cousin, Remember Frances Kelsey

And this is where America needs to remember that it has done some
absolutely banging regulation.

Not perfectly.

Not universally.

Not uniquely.

But occasionally in ways so consequential that the story should be
taught as part of the country's scientific self-conception.

### Frances Oldham Kelsey was a boss.

In 1960, FDA medical officer **Frances Oldham Kelsey**, a physician and
pharmacologist, was assigned the US application for Kevadon ---
thalidomide.

Thalidomide was already available in dozens of countries.

The manufacturer wanted American approval.

Kelsey did not possess magical knowledge of the disaster that would
subsequently become visible.

She looked at the evidence submitted to support safety and concluded,
repeatedly:

**not enough.**

The FDA's own history records that the manufacturer continued to
pressure the agency and continued supplying material it considered proof
of safety. Kelsey continued to insist on scientifically reliable
evidence.

The application did not become effective.

By late 1961, evidence from Germany and Australia linked thalidomide
exposure during pregnancy to catastrophic congenital abnormalities.

More than 10,000 children worldwide were born with severe
thalidomide-associated malformations, with additional miscarriages and
stillbirths that are harder to count.

The United States was not completely untouched: more than two million
tablets had been distributed there for investigational use under the
much weaker rules of the time.

But thalidomide was **never generally marketed in the United States**.

America therefore largely avoided the scale of catastrophe experienced
in countries where the drug had been commercially available.

That is not a small regulatory success.

That is:

# REMEMBER WHEN THE AMERICANS WERE TOO SCIENCE TO BE FOOLED INTO HARMING PREGNANCIES

This is not Europe arriving to teach Cousin Regulation.

This one is fucking American.

------------------------------------------------------------------------

## 18. 🧾 Show Me The Receipts

The Kelsey story is especially useful because its logic is so clean.

She did **not** need to begin with:

> I have conclusively proven that your drug causes catastrophic fetal
> malformations.

The relevant regulatory question was:

> **Have you supplied adequate evidence for the safety proposition you
> are asking me to approve?**

Those are different questions.

``` text
MANUFACTURER
      ↓
makes safety claim
      ↓
submits evidence
      ↓
REGULATORY REVIEW
      ↓
does evidence meet required threshold?
      │
   ┌──┴──┐
  YES    NO
   ↓      ↓
proceed  NOT YET
```

**NOT YET** is a valid information state.

**INSUFFICIENT EVIDENCE** is a valid information state.

The regulator does not improve science by converting uncertainty into a
yes because the manufacturer has a launch schedule.

Kelsey represented uncertainty correctly.

Then reality supplied more information.

And the consequences of having preserved the uncertainty rather than
prematurely collapsing it were enormous.

This is the same information-theory principle with which the node began:

``` text
BBC

insufficient context
→ do not guess
```

and:

``` text
THALIDOMIDE SAFETY

insufficient evidence
→ do not approve yet
```

Different domain.

Same epistemic discipline.

> **Do not force uncertainty into a categorical answer merely because
> the system would find an answer convenient.**

------------------------------------------------------------------------

## 19. ⚧️ The Allegedly Masculine Art Of Asking For The Receipts

There is also something very funny about the way Kelsey's conduct might
be culturally coded.

Hard evidentiary threshold.

Not particularly moved by commercial confidence.

Persistent.

Technical.

Willing to say no.

**Show me the receipts.**

People frequently code those behaviours as masculine.

Unfortunately for the gender essentialists, Frances Kelsey was standing
right there.

The lesson is not:

> Women regulate better.

There are excellent and terrible regulators of every sex.

Nor did Kelsey refuse approval because she was a woman and therefore
possessed a mysterious feminine intuition about pregnancy.

She was a physician and pharmacologist performing regulatory science.

The population involved included pregnant people and developing fetuses,
where the consequences of an inadequately understood exposure could be
profound.

The evidence submitted did not satisfy her.

So she did not say yes.

The traits were never inherently male.

And there is another systems point hiding underneath the biography:

**Kelsey having doubts was not enough.**

The institutional architecture put her at a decision point where her
scientific judgement had regulatory force.

The right sensor was in the right place.

And, crucially:

**the system listened to it.**

------------------------------------------------------------------------

## 20. 🇺🇸 Cousin, This One Is Yours

The useful American story is not:

> America regulates perfectly.

It plainly does not.

Nor is it:

> Europe understands safety and America understands innovation.

That is historically stupid.

The useful question is:

> **When American regulation has worked spectacularly well, what made it
> work?**

In the Kelsey case, relevant features included:

-   a defined regulatory decision point;
-   a manufacturer bearing an evidentiary burden;
-   an appropriately qualified reviewer;
-   authority to withhold approval;
-   the ability to request better evidence;
-   institutional capacity to resist commercial pressure;
-   later incorporation of the disaster into regulatory reform.

The thalidomide near-disaster helped propel the 1962 Kefauver--Harris
amendments, which strengthened US drug regulation. The FDA subsequently
developed more specialised functions, including adverse-reaction
surveillance and an advisory committee that acted as an interface with
clinical investigators and scientists outside the agency.

That last bit is particularly relevant.

America's lesson was not:

> FDA EMPLOYEE MUST PERSONALLY KNOW ALL SCIENCE.

It built additional interfaces to expertise.

Which is exactly what contemporary AI governance needs.

🦊: **Cousin, nobody is asking you to become Europe.**

🇺🇸: Good.

🦊: **You have your own regulatory traditions. Some of them are
magnificent.**

🇺🇸: Such as?

🦊: **You once gave a pharmacologist a drug application, the company
told her everything was fine, and she said: show me better evidence.**

🇺🇸: Frances Kelsey.

🦊: **YES. HER. MORE OF THAT ENERGY.**

------------------------------------------------------------------------

## 21. 🦊 Regulation Is Not "Everybody At The Regulator Knows Everything"

This gives us a better model for AI regulation.

The regulator does not replace the regulated profession.

It establishes:

-   evidence requirements;
-   interfaces;
-   escalation routes;
-   access to independent expertise;
-   record-keeping requirements;
-   incident definitions;
-   response times;
-   accountability;
-   a bounded space in which innovation can continue.

For AI:

``` text
AI company
      ↓
technical evidence
      ↓
regulatory interface
      ├── clinical expertise
      ├── cybersecurity
      ├── competition
      ├── employment
      ├── child safety
      ├── information integrity
      ├── national security
      └── other competent authority
      ↓
bounded determination
      ↓
company knows what it is expected to do
```

🦊: **Cousin, I am not adding another job.**

🦊: **I am trying to stop you doing everybody else's.**

That is not anti-innovation.

It may be one of the conditions that allows general-purpose technology
to be deployed without every new collision between disciplines becoming
a corporate existential crisis.

------------------------------------------------------------------------

## 22. 🌍 Debugging As Diplomacy

The same architecture works internationally.

Suppose Britain detects a reproducible anomaly in a computational system
operated by an American provider.

Britain does not necessarily need:

-   the source code;
-   the model weights;
-   every proprietary dataset;
-   the company's entire ranking formula;
-   unrestricted access to commercially sensitive systems.

It needs enough observability to say:

> **Mate. Something weird is happening over here. Here is enough
> evidence to reproduce it. Please look inside the bit we cannot see.**

The provider or appropriate American authority can then inspect
protected internals.

``` text
🇬🇧 observe anomaly
      ↓
reproduce / measure / characterise
      ↓
rule out obvious domestic causes
      ↓
shared technical interface
      ↓
🇺🇸 provider / authority inspects protected internals
      ↓
appropriate independent expertise
      ↓
joint root-cause analysis
      ↓
narrowest effective fix
      ↓
test in both environments
      ↓
document
```

The cause might be:

-   a weighting;
-   a classifier threshold;
-   query expansion;
-   an embedding association;
-   training-data imbalance;
-   a feedback signal;
-   ranking objective;
-   localisation rule;
-   safety filter;
-   experiment;
-   interaction between systems.

Britain does not need to know in advance.

It needs a competent counterparty and a pathway through which the
question can be answered.

This is:

# debugging as diplomacy

> **International AI governance does not require universal access to
> proprietary systems. It requires enough reciprocal technical capacity
> and institutional trust to debug cross-border computational
> externalities together.**

🇬🇧: Your computer is doing something fucking weird to the BBC.

🇺🇸: Which BBC?

🇬🇧: **Unfortunately, cousin, that appears to be the fucking problem.**

------------------------------------------------------------------------

## 23. 🧰 Root Cause, Not A New Box To Put The Human In

We can now see the common structure across apparently unrelated
examples.

### BBC

Bad question:

> What does the system think about "BBC"?

Better question:

> Which referent has the system resolved, using what context, and what
> happens if that context is absent?

### Radicalisation

Bad compression:

> He self-radicalised online.

Better questions:

> What did he seek? What was supplied? Who or what selected it? How did
> the selection change following engagement? When did humans enter the
> pathway? What happened offline?

### Mental-health deterioration involving an LLM

Bad compression:

> AI psychosis.

Better questions:

> What syndrome was present? What was the person's starting state? What
> did the model actually output? What did the person infer? What changed
> over time? Which factors were contributory? What evidence survives?

### Product safety

Bad compression:

> We have no proof it is dangerous.

Better question:

> Have you provided adequate evidence for the safety claim required for
> this decision?

Across all four:

> **Do not let a convenient label destroy the causal information
> required to investigate the system.**

That is the actual presenting complaint.

------------------------------------------------------------------------

## 24. 🎩 Exhibit H Finding

The problem is not simply that algorithms can contain bias.

Nor is it simply that platforms can recommend harmful material.

Nor is it simply that commercial incentives can produce undesirable
outcomes.

Nor is it simply that regulators lack access.

The deeper problem is that contemporary computational systems operate
across domains where **meaning, causation, expertise and jurisdiction
are distributed**.

A system can be technically sophisticated while being epistemically
under-contextualised.

A company can be extraordinarily competent at computer science while
confronting questions that are fundamentally psychiatric, sociological,
historical, legal or diplomatic.

A regulator can fail by trying to become expert in everything.

A regulator can also succeed by knowing:

> **Who needs what information, who is qualified to interpret it, what
> evidence is required, and what happens when the answer is "we do not
> know yet."**

That is why Frances Kelsey belongs in a node that started with porn
metadata.

Not because thalidomide and recommender systems are the same problem.

Because **the epistemic discipline is transferable**.

``` text
DO WE HAVE ENOUGH CONTEXT TO KNOW WHAT THIS MEANS?
             ↓
           NO
             ↓
        DO NOT GUESS


DO WE HAVE ENOUGH EVIDENCE TO AUTHORISE THIS CLAIM?
             ↓
           NO
             ↓
        DO NOT PRETEND YES
```

FOR FUCK'S SAKE, USA.

You have demonstrated that you can do this.

**Remember when the Americans were too science to be fooled into harming
pregnancies.**

Remember the woman with the receipts.

Then build the interfaces.

------------------------------------------------------------------------

## 25. 🦊 Closing Exchange

🇺🇸: We are moving extremely quickly.

🦊: **Yes.**

🇺🇸: The technology is unprecedented.

🦊: **Some of it.**

🇺🇸: Regulators won't understand everything we're building.

🦊: **Correct.**

🇺🇸: Then regulation cannot keep up.

🦊: **No, cousin. That conclusion does not follow.**

🇺🇸: What do you propose?

🦊: **You explain what the computer did.**

🦊: **The psychiatrist explains the psychiatry.**

🦊: **The security people explain the security problem.**

🦊: **The lawyers explain the law.**

🦊: **The people affected explain what happened to them.**

🦊: **The regulator makes sure the evidence reaches the right people and
that somebody is responsible for acting on the answer.**

🇺🇸: That sounds bureaucratic.

🦊: **YES.**

🇺🇸: And if the evidence isn't enough?

🦊: **Then we write "insufficient evidence".**

🇺🇸: And then?

🦊: **We obtain more evidence.**

🇺🇸: That's it?

🦊: **Cousin. That is quite a lot of what science is.**

------------------------------------------------------------------------

## 🔬 Research Hooks Before Evidentiary Lock

The conceptual architecture of this node is stable. The following
factual seams should be tightened before treating every illustrative
pathway as an established empirical claim:

-   map the BBC's own search, recommendation, analytics and third-party
    infrastructure before claiming any direct effect on BBC-controlled
    pages;
-   distinguish external search/recommendation environments from the
    BBC's internal systems;
-   document current ownership and jurisdiction of any pornography
    platforms used as examples;
-   locate stronger empirical work on geographic variation in racialised
    pornography searches before making state-level claims;
-   do not infer individual racial prejudice from ecological search
    data;
-   pin the original Peter Thiel interview/transcript before quoting or
    characterising the exact contemporary exchange;
-   expand current evidence on recommender-mediated extremist exposure
    beyond the 2019 RUSI experiment and preserve platform-specific
    findings;
-   distinguish "AI-associated psychosis", "AI-induced psychosis",
    psychosis involving AI as an object, and other forms of
    mental-health deterioration rather than treating a media label as a
    diagnosis;
-   preserve clinical uncertainty: anxiety, psychosis, mood disturbance,
    trauma, sleep loss, substance effects and other processes can
    overlap and require qualified assessment;
-   use the Kelsey case as evidence for an evidentiary architecture, not
    as proof that every precautionary regulatory decision will later be
    vindicated.

------------------------------------------------------------------------

## 📚 Sources & Research Starting Points

-   [U.S. Food and Drug Administration: "Frances Oldham Kelsey: Medical
    reviewer famous for averting a public health
    tragedy"](https://www.fda.gov/about-fda/fda-history-exhibits/frances-oldham-kelsey-medical-reviewer-famous-averting-public-health-tragedy)
-   [U.S. Food and Drug Administration: "A Brief History of the Center
    for Drug Evaluation and
    Research"](https://www.fda.gov/about-fda/fda-history-exhibits/brief-history-center-drug-evaluation-and-research)
-   [U.S. Food and Drug Administration: "Milestones in U.S. Food and
    Drug
    Law"](https://www.fda.gov/about-fda/fda-history/milestones-us-food-and-drug-law)
-   [Vargesson, "Thalidomide-induced teratogenesis: History and
    mechanisms"](https://pmc.ncbi.nlm.nih.gov/articles/PMC4737249/)
-   [Egwuatu, Stardust, Miller-Young & Ducati, "Curating Desire: The
    White Supremacist Grammar of Tagging on
    Pornhub"](https://academic.oup.com/book/57460/chapter-abstract/466698390)
-   ["The influence of pornography on heterosexual Black men and women's
    genital self-image &
    grooming"](https://doi.org/10.1016/j.bodyim.2023.101669)
-   [Stanford Encyclopedia of Philosophy: "Frantz
    Fanon"](https://plato.stanford.edu/entries/frantz-fanon/)
-   [RUSI: "Radical Filter Bubbles: Social Media Personalisation
    Algorithms and Extremist
    Content"](https://www.rusi.org/explore-our-research/publications/special-resources/radical-filter-bubbles-social-media-personalisation-algorithms-and-extremist-content)
-   [Olisaeloka et al., "Artificial intelligence (AI) psychosis:
    mechanisms, clinical risks and safety considerations in generative
    AI chatbots"](https://pubmed.ncbi.nlm.nih.gov/42273786/)
-   [Tong, Gong & Yao, "Psychosis in the Age of Large Language Models
    (LLMs): A Narrative Review of the Proposed Construct of AI-Induced
    Psychosis"](https://pubmed.ncbi.nlm.nih.gov/42540500/)
-   [Başaran & Coşar, "Psychotic episode concurrent with interaction
    with a large language model (LLM): a case
    report"](https://pubmed.ncbi.nlm.nih.gov/42286516/)

------------------------------------------------------------------------

## 🌌 Constellations

🎩 🦊 🪿 ♻️ 🕸️ --- Putting On Less Ritz; Cousin, We Have Ideas; Embodied
Information Ecology; cybernetics; feedback environments; semantic
context; regulatory interfaces; debugging as diplomacy.

------------------------------------------------------------------------

## ✨ Stardust

embodied information ecology, feedback environments, algorithmic
radicalisation, semantic disambiguation, recommender systems, racialised
metadata, ai mental health, regulatory science, epistemic routing,
frances kelsey

------------------------------------------------------------------------

## 🏮 Footer

*📋 Exhibit H: Radicalised Algorithms* is a living node of the **Polaris
Protocol**.\
It uses semantic ambiguity, racialised platform metadata,
recommender-mediated information environments, mental-health
adverse-event analysis and the Frances Kelsey thalidomide case to
examine how computational governance can preserve context, uncertainty,
evidence and specialist expertise rather than collapsing complex causal
systems into convenient labels.

> 📡 Cross-references:
>
> -   [🎩 Putting On Less Ritz](./README.md) --- *American systems,
>     British complaints, and the Special Relationship as a feedback
>     channel*
> -   [🪿 Embodied Information Ecology](../../../README.md) ---
>     *information as experienced and interpreted within situated
>     systems*
> -   [♻️🕸️ The Feedback Environment](../../README.md) --- *parent
>     framework for recursive informational and behavioural systems*
>
> 🏮 Return To:
>
> -   [🎩 Putting On Less Ritz](./README.md) --- *1up*
> -   [♻️🕸️ The Feedback Environment](../README.md) --- *2up*
> -   [🪿 Embodied Information Ecology](../../README.md) --- *3up*
> -   [🌑 Origin Points](../../../README.md) --- *4up*
> -   [🌌 Polaris Protocol --- Root](../../../../README.md) --- *root*

*Survivor authorship is sovereign. Containment is never neutral.*

*Last updated: 2026-09-27*
