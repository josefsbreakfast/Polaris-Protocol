# 📋 Exhibit J: Where The Fuck Is That Email?

**First created:** 2026-09-24 \| **Last updated:** 2026-09-24\
*An email goes from A to B. Except when it doesn't. Except when it does
and nobody can find it. Welcome to information infrastructure.*

------------------------------------------------------------------------

## 🛰️ Orientation

This node begins with an extremely small question.

**Where the fuck is that email?**

More precisely: on 28 August 2026, Mike Wood MP tabled Parliamentary
Question 20754 to the Cabinet Office, asking which division of the
Cabinet Office the National Cyber Security Centre had passed the Labour
Together/APCO dossier to, and whether the Joint Intelligence
Organisation had received it. The Parliament record showed the question
as due for answer on 2 September and still awaiting answer when checked
in September.[^1]

That is the observable fact.

It is not, by itself, an explanation.

An overdue answer may be interesting. It may eventually turn out to
involve substantive policy, security handling, legal clearance,
cross-government consultation, records retrieval, ordinary
parliamentary-question processing, or something else entirely. We do not
currently know.

This distinction matters because humans are extremely good at observing
an unusual output and immediately constructing a mechanism capable of
producing it.

Sometimes that mechanism is right.

Sometimes we have spent six weeks contemplating the machinery of the
state and somebody has put the fucking thing in the wrong folder.

This is therefore not a node alleging that the Cabinet Office has lost
an email. Nor is it a node asserting that Microsoft, the NCSC, the JIO,
the CIA, a malicious octopus, or anybody else has eaten one.

It is a node about a more useful question:

> **How many things have to work before "A sent information to B"
> becomes "B can find, understand, retrieve, route and act upon the
> information A intended to send"?**

Quite a lot, unfortunately.

And once we follow that problem far enough, we end up somewhere much
larger than Outlook.

We end up with human attention, identity records, Unicode, occupational
health, database matching, AI-assisted reconciliation, resilience
engineering, software maintenance, SaaS, procurement, international
trade, and the slightly awkward discovery that American software has
become important enough to other countries that those countries now have
opinions about how it should behave.

Congratulations, America.

Your software is infrastructure now.

We need to talk about maintenance.

------------------------------------------------------------------------

## 1. 📋 What We Actually Know

Before touching the machinery, establish the evidence boundary.

The Parliamentary record gives us an observable output state:

-   a named question exists;
-   it was asked on a particular date;
-   it was directed to a particular department;
-   it asked about a particular information-transfer question;
-   it had an expected answer date;
-   and the public record continued to show it as awaiting answer when
    checked.[^2]

What the public record does **not** establish is why.

We do not know from that status alone:

-   whether the underlying information is difficult to retrieve;
-   whether several organisations need to be consulted;
-   whether security considerations are relevant;
-   whether legal or disclosure review is occurring;
-   whether the information moved in the form imagined by the question;
-   whether an email is missing;
-   whether an email ever existed;
-   whether somebody has found the relevant record but cannot yet
    answer;
-   whether the delay is remarkable inside the actual administrative
    workflow;
-   or whether something much more boring is happening.

This is a useful discipline because an anomalous output is not a
diagnosis.

``` text
OBSERVATION
    ↓
EVIDENCE
    ↓
FAILURE LOCALISATION
    ↓
MECHANISM
    ↓
ATTRIBUTION
```

Not:

``` text
OBSERVATION
    ↓
VIBES
    ↓
CIA
```

But also not:

``` text
OBSERVATION
    ↓
"COMPUTERS DON'T DO THAT"
    ↓
DISMISS THE HUMAN REPORTING THE ANOMALY
```

Both shortcuts destroy information.

The first fills uncertainty with drama.

The second fills uncertainty with institutional confidence.

Neither has actually investigated the system.

> **Before attributing an anomalous output to an extraordinary actor,
> establish whether the ordinary system can generate the same anomaly
> unaided.**

That is not scepticism for scepticism's sake.

It is debugging.

------------------------------------------------------------------------

## 2. 📮 "A Sent An Email To B"

The social model of email is beautifully simple:

``` text
[A] ─────────────── email ───────────────> [B]
```

Alice sends.

Bob receives.

Excellent.

Unfortunately, computers have become involved.

A simplified technical and organisational pathway looks more like this:

``` text
AUTHOR
  ↓
MAIL CLIENT
  ↓
OUTBOUND MAIL SYSTEM
  ↓
ADDRESS / DOMAIN RESOLUTION
  ↓
NETWORK TRANSPORT
  ↓
RECIPIENT MAIL INFRASTRUCTURE
  ↓
SECURITY / POLICY FILTERING
  ↓
MAILBOX STORAGE
  ↓
INDEXING / CLASSIFICATION
  ↓
RECIPIENT CLIENT / INTERFACE
  ↓
HUMAN ATTENTION
  ↓
ORGANISATIONAL HANDLING
  ↓
RECORDS / RETRIEVAL
  ↓
ACTION
```

This is deliberately generic. It is **not** a diagram of the Cabinet
Office's specific mail architecture.

The point is that "email" is a human abstraction laid over a chain of
systems.

At the beginning, somebody has to create the message.

Their mail client has to submit it.

The sender's infrastructure has to accept it.

The destination has to be resolved.

Servers and gateways have to move it.

The recipient infrastructure has to accept it.

Security systems may inspect it.

Policy systems may classify, quarantine, reject or redirect it.

Mailbox systems have to store it.

Indexes have to make it retrievable.

Interfaces have to render it.

The human has to encounter it.

Then, if B is not merely a person but an institution, the information
has to enter another ecology entirely.

Who owns the matter?

Who forwards it?

Who records it?

Who recognises that it is important?

Does the covering email remain attached to the document?

Does the attachment enter a records-management system independently?

Is there a case reference?

Is there an acknowledgement?

Does a second team inherit it?

Can anybody reconstruct what happened six months later?

The simple arrow is not wrong.

It is just hiding nearly everything interesting.

------------------------------------------------------------------------

## 3. 👁️ Delivered Is Not Seen

This is the first major distinction.

``` text
MESSAGE EXISTS
      ≠
MESSAGE IS SUBMITTED
      ≠
MESSAGE IS TRANSMITTED
      ≠
MESSAGE IS ACCEPTED
      ≠
MESSAGE IS DELIVERED
      ≠
MESSAGE IS VISIBLE
      ≠
MESSAGE IS NOTICED
      ≠
MESSAGE IS UNDERSTOOD
      ≠
MESSAGE IS REMEMBERED
      ≠
MESSAGE IS RETRIEVABLE
      ≠
MESSAGE ENTERS ORGANISATIONAL ACTION
      ≠
MESSAGE CAN BE DISCLOSED
```

These states can overlap. They are not interchangeable.

"Did B receive the email?" therefore contains several possible
questions:

-   Did B's domain accept the message?
-   Did B's mail infrastructure accept it?
-   Did security policy permit it through?
-   Did it reach the intended mailbox?
-   Did it remain in that mailbox?
-   Was it indexed correctly?
-   Did the intended human see it?
-   Did the human recognise its significance?
-   Did the organisation register it?
-   Was it routed to the correct function?
-   Can the organisation retrieve it now?
-   Can it reconstruct provenance and handling history?
-   Is the organisation permitted to disclose what happened?

The answer can be **yes** at one layer and **no** at the next.

This is one of the central mistakes people make when reasoning about
information systems: treating the successful transport of data as
equivalent to the successful production of usable information.

It isn't.

> **An information system can successfully transport information while
> still failing to make that information available to the person or
> institution that needs to act upon it.**

The distinction becomes even more important when a system is partly
designed to manage human attention.

Microsoft's own documentation says Outlook's Focused Inbox separates
messages into "Focused" and "Other" and uses interactions and contacts
to decide which messages it considers most important.[^3]

That is useful functionality.

It is also conceptually fascinating.

There is now an algorithmic operation between:

``` text
MESSAGE ARRIVES
       ↓
HUMAN ENCOUNTERS MESSAGE
```

The user may think:

> My inbox contains my incoming mail.

The interface is doing something more sophisticated:

> Here is our representation of which incoming mail you are most likely
> to want first.

Again: useful.

But it means **receipt and visibility are technically distinct states**.

Welcome to the fucking node.

------------------------------------------------------------------------

## 4. 🇺🇸 Has Anyone Checked The American Software Stack?

At this point it is worth being very clear about the joke.

This is not:

> **THE AMERICANS HAVE THE EMAIL.**

It is:

> **WHERE THE SHITTING HELL IS MY EMAIL, MICROSOFT.**

Modern British institutions operate through layered enterprise
information systems. A great deal of commercially important software and
cloud infrastructure comes from American companies.

That does not establish that an American supplier caused any particular
British administrative anomaly.

It does establish something much more mundane:

**ordinary software belongs inside the hypothesis space.**

Possible explanations for a delayed institutional output can include:

``` text
security / classification
legal or disclosure review
cross-government consultation
records retrieval
human workflow
mail infrastructure
search / indexing
permissions
interface behaviour
ordinary administrative delay
something else
```

We do not have to pick one before evidence distinguishes them.

The information ecology does not stop being mundane because some of the
actors have security clearances.

The Cabinet Office does not cease to consist of humans using computers
because the subject matter happens to involve the NCSC or JIO.

🦊: Cousin. We appear to be having some difficulty locating one fucking
email.

🇺🇸: National security?

🦊: Potentially.

🇺🇸: Intelligence sharing?

🦊: Possibly.

🇺🇸: Then why are you looking at us?

🦊: **Has anyone checked Outlook?**

This is *Putting On Less Ritz* in miniature.

Preserve the dramatic hypothesis.

Preserve the boring hypothesis.

Then investigate.

------------------------------------------------------------------------

## 5. 🔎 Before The Help Desk Will Believe You

Anyone who has spent enough time with computers knows the ritual.

Something has gone wrong.

Before the system is permitted to be wrong, the user must first
establish that the user is not an idiot.

Have you checked the address?

Have you checked Junk?

Have you checked Archive?

Have you checked Other?

Have you searched by sender?

Subject?

Date?

Attachment?

Are you signed into the right account?

Is it in the browser?

Desktop app?

Phone?

Has it synchronised?

Have you restarted it?

Can you reproduce the problem?

Have you turned it off and on again?

Only after sufficient ritual purification may the anomaly be escalated.

There are good reasons for some of this. A large proportion of faults
genuinely are local, common and easily resolved.

But it produces an interesting epistemic burden.

The person experiencing the failure sees the **end-to-end task** fail.

The people maintaining individual components may see every component
reporting success.

``` text
SENDER:       SENT ✓
TRANSPORT:    ACCEPTED ✓
GATEWAY:      PROCESSED ✓
MAILBOX:      EXISTS ✓
INDEX:        ???
INTERFACE:    NOT HERE
HUMAN:        WHERE THE FUCK IS IT
```

Everybody can be reporting their local observation accurately.

The task can still have failed globally.

> **Locally correct behaviour can produce globally incorrect
> information.**

That sentence is going to matter again.

------------------------------------------------------------------------

## 6. 🧮 Computers Were Never Just Calculators

There is a persistent folk model of computing:

``` text
INPUT
  ↓
COMPUTER
  ↓
CORRECT OUTPUT
```

This model is useful if we are discussing a sufficiently constrained
calculation.

It is terrible for reasoning about large sociotechnical information
systems.

Even before contemporary generative AI, institutional computing already
contained:

-   filters;
-   rankings;
-   search indexes;
-   permissions;
-   identity resolution;
-   synchronisation;
-   retention rules;
-   workflow automation;
-   integrations;
-   configuration;
-   categorisation;
-   human judgement;
-   exceptions;
-   migrations;
-   legacy systems;
-   and databases designed by people who had extremely reasonable
    assumptions in 2004 and would quite like not to be blamed personally
    for what happened in 2026.

AI does not introduce uncertainty into a previously pristine world of
deterministic institutional truth.

It changes the kinds of inference available, the scale at which they can
operate, and the failure modes we need to manage.

The relevant comparison is therefore not:

> perfect old computer versus unreliable AI.

It is:

> **existing sociotechnical system with known and unknown failure modes
> versus new sociotechnical system with different capabilities and
> different failure modes.**

This is why resilience matters more than fantasies of perfection.

------------------------------------------------------------------------

## 7. 📎 Clippy, Focused Inbox And Notification Sludge

There is, unfortunately, a historical complication.

We are still carrying post-Clippy trauma.

A generation of computer users was trained in a very particular lesson:

> **When Microsoft interrupts you to offer assistance, make Microsoft go
> away.**

This is not necessarily because the animated character was intrinsically
bad.

The problem was contextual.

Assistance appeared when the user did not necessarily want assistance.

The intervention competed with the user's existing task.

The interface had insufficient understanding of whether its interruption
was useful.

So users learned a behaviour:

``` text
SOFTWARE INTERRUPTS
       ↓
DISMISS SOFTWARE
       ↓
CONTINUE ACTUAL TASK
```

Then, several decades later:

> Why aren't users engaging with feature education?

Well.

We have some historical evidence.

### 🌸 Mini Chloe meets Mr Paperclip

There is another side to this.

A very small child encounters an animated paperclip with eyes.

It moves.

It appears to notice things.

It addresses the user.

The reasonable childhood inference is:

> **Oh. A little computer person.**

So 🌸 Mini Chloe attempts to converse with Mr Paperclip.

Eventually she discovers that this is not, in fact, an artificial
conversational intelligence.

It is a help interface.

Fine.

Replace him with the paper cat.

The cat has better animations.

This is not merely nostalgia. It demonstrates something important about
interface design:

> **Users interpret systems from the affordances presented to them, not
> from the designer's internal ontology.**

Microsoft may have intended:

> friendly assistance.

A child could experience:

> social agent.

An adult office worker could experience:

> interruption.

A later generation can experience the same object as:

> affectionate cultural joke.

Same paperclip.

Different information.

The meaning is produced in the relationship between object, observer and
context.

### Notification sludge

Now widen the problem.

The contemporary user encounters:

-   onboarding cards;
-   feature tours;
-   "What's New" panels;
-   privacy notices;
-   cookie banners;
-   security warnings;
-   red notification badges;
-   terms updates;
-   subscription notices;
-   consent modals;
-   product announcements.

Every one may have a reason to exist.

Collectively, they train behaviour.

The intended signal:

> **THIS INFORMATION REQUIRES YOUR ATTENTION.**

The learned response:

> **WHERE IS THE FUCKING BUTTON THAT MAKES THE RECTANGLE GO AWAY.**

This matters because formal disclosure and effective communication are
not the same thing.

A disclosure can be:

1.  available somewhere;
2.  presented to the user;
3.  reasonably comprehensible and salient to the user.

Those are different achievements.

A cookie banner may successfully record that a user interacted with a
consent mechanism while the human's experienced task was:

> remove obstacle between me and article.

Again:

**same interaction, different information.**

### The Creatives™️

None of this means interfaces should become grey rectangles designed by
an international committee for the prevention of joy.

Never underestimate tasteful and limited use of **The Creatives™️**.

The funny animated paperclip was not necessarily the problem.

The funny animated paperclip **refusing to stop interrupting you** was
the problem.

The Creatives™️ may make the infrastructure charming.

They must not be permitted to turn every interaction with the
infrastructure into an event.

Tasteful.

Limited.

Cat animations retained.

------------------------------------------------------------------------

## 8. 💿 Encarta Without A Sound Card

🌸 Mini Chloe also had Microsoft Encarta.

Encarta contained sound files.

The computer did not contain a sound card.

This was incredible.

Not because the audio could be heard.

It could not.

But because the encyclopaedia **contained sound**.

The information existed.

The receiving system did not possess the apparatus required to render it
experientially available.

``` text
AUDIO DATA EXISTS
       ↓
SOFTWARE CAN REFERENCE AUDIO
       ↓
NO SOUND HARDWARE
       ↓
NO AUDIBLE EXPERIENCE
```

🌸: This encyclopaedia contains AUDIO.

🔇 Computer: no it fucking doesn't.

🌸: But theoretically it does.

🔇: correct.

🌸: INCREDIBLE.

This is Embodied Information Ecology in an unusually pure form.

> **The existence of information somewhere in a system does not
> establish its availability to the organism expected to receive it.**

Data is not experience.

Storage is not rendering.

Transmission is not perception.

A message can exist and still fail to become actionable information
because the receiving environment lacks something required to make it
available.

Sometimes that missing component is a sound card.

Sometimes it is an index.

Sometimes it is a permission.

Sometimes it is a screen reader.

Sometimes it is a person with enough time and contextual knowledge to
understand what they are looking at.

------------------------------------------------------------------------

## 9. 🐕 BONK BONK BONK

Old computers were educational because they exposed their seams.

You learned very quickly that:

``` text
DATA
≠
SOFTWARE
≠
HARDWARE
≠
INTERFACE
≠
OUTPUT
```

CD drive not reading?

Eject.

Reinsert.

Listen.

Peripheral not recognised?

Unplug.

Replug.

Computer frozen?

Wait.

Threaten.

Ctrl-Alt-Delete.

CRT suspicious?

Do not slap the screen.

Sufficiently ancient hard drive?

Well.

If the data is valuable: **absolutely do not hit the drive**. Mechanical
impact and repeated spin-up can worsen a recoverable hardware failure.

If the drive is already dead, contains nothing important, and its
prognosis cannot meaningfully become more dead:

🐕 **BONK BONK BONK**

*click ... whirr ... click*

🐕 bonk

**WHIRRRR**

> I HAVE REMEMBERED MY PURPOSE.

This is not recommended data-recovery practice.

It is, however, a beautiful meme-sized representation of a
troubleshooting instinct:

> **What physical or informational intervention changes the observable
> state?**

The Creatives™️ compressed the protocol more efficiently than
management.

------------------------------------------------------------------------

## 10. 🧬 The One-Character Catastrophe

Now we move from missing messages to missing people.

The analogy here is to a point mutation: a very small representational
change can sometimes produce a disproportionately large downstream
consequence.

This is an analogy, not a claim that databases behave biologically.

The important principle is:

> **The scale of the downstream consequence need not resemble the scale
> of the original error.**

Consider:

``` text
Chloe
Chloë
```

To a human reader, these strings contain an obvious relationship.

To a strict equality operation:

``` text
"Chloe" == "Chloë"
FALSE
```

And:

``` text
"Chloe" == "Reginald"
FALSE
```

The computer has not necessarily concluded that *Chloë* resembles
*Reginald* as much as *Chloe*.

It has answered a narrower question:

> Do these strings satisfy the equality condition I was given?

No.

No.

Humans can then accidentally perform a catastrophic conceptual upgrade:

``` text
NO EXACT MATCH
      ↓
NOT THE SAME RECORD
      ↓
NOT THE SAME PERSON
```

That last step is not contained in the Boolean.

We added it.

And Unicode can make the problem still more entertaining, because
visually similar text can have different underlying representations
depending on whether an accented character is precomposed or represented
using a base character plus combining mark. Whether two values compare
as equivalent depends on normalisation, collation and application logic.

The human sees identity.

The database sees characters.

The institution may mistakenly treat the database's answer as reality.

------------------------------------------------------------------------

## 11. 🗃️ One Woman, Two Records

Imagine:

``` text
SYSTEM A
Chloë Birney
ID: 123456
      ↓
TRANSFER
      ↓
SYSTEM B
Chloe Birney
      ↓
EXACT-MATCH JOIN
      ↓
NO MATCH
      ↓
NEW RECORD
```

One woman.

Two institutional identities.

Now time passes.

Record A contains:

-   old correspondence;
-   historic assessments;
-   previous address;
-   original reference numbers.

Record B contains:

-   current address;
-   current service;
-   recent correspondence;
-   new reference number.

Somebody searches Record B.

> We have checked the system. There is no record of that.

Person:

> **YES. THAT IS THE FUCKING PROBLEM.**

At this point, repeating the same search with greater confidence will
not solve the problem.

The investigation has to move sideways:

-   alternate spellings;
-   previous identifiers;
-   old addresses;
-   raw source records;
-   unmatched transactions;
-   duplicate identities;
-   rejected imports;
-   migration logs;
-   timestamps;
-   source-system references.

The question changes from:

> What does the normal interface say?

to:

> **What happened underneath the normal interface?**

That is an enormous epistemic upgrade.

------------------------------------------------------------------------

## 12. 🏺 Britain Has Never Had Perfectly Standardised Humans

There is a particularly British historical wrinkle here.

Administrative records did not begin with computers.

They inherited centuries of naming practice, literacy differences, local
language, clerical judgement, migration, marriage, anglicisation,
abbreviations, nicknames, regional conventions and changing ideas about
what constituted the "proper" form of somebody's name.

Scotland's official historical-record service explicitly warns that
names can vary because of transcription errors, phonetic spellings,
registrar or clerk interpretation, surname variants, anglicisation and
other changes. It offers exact, fuzzy, phonetic and wildcard searching
precisely because exact spelling is not a sufficient model of historical
identity.[^4]

Its forename guidance is even more direct: people may appear under
abbreviations, diminutives, nicknames, middle names, anglicised forms
and variant spellings, and it advises researchers to expect
inconsistency across records.[^5]

The UK Office for National Statistics has documented the same problem in
modern administrative-data matching. It notes that matching based on
names and dates of birth can produce false positives and false negatives
where names vary, and gives punctuation differences such as `Darcy` and
`D'arcy` as the kind of issue data-cleaning rules may need to
handle.[^6]

That gives us a firm documentary foundation:

> **Britain has never possessed a perfectly standardised population of
> perfectly standardised names.**

There is then a broader cultural observation, which should be labelled
as such rather than smuggled in as archival fact.

British naming is also class-coded.

There has long been a social distinction between familiar and formal
forms, between what somebody is called and what somebody believes ought
properly to appear in an official document, and between names as lived
identity and names as administrative respectability. Registrars, clerks,
families and informants have not always approached those questions from
the same position.

Sometimes a person falls through the cracks because somebody entered
their information incorrectly.

Sometimes:

> **they fall through because somebody entered it more correctly than
> the next database was designed to understand.**

The intention may have been conscientious.

The downstream effect can still be failure.

Good intentions do not abolish systems engineering.

------------------------------------------------------------------------

## 13. 🕳️ Go Looking For The Cracks

This is where modern entity resolution becomes genuinely exciting.

The old operation might be:

``` text
Chloe != Chloë
      ↓
NO MATCH
```

A richer matching process can ask:

``` text
name similarity
+ date of birth
+ address history
+ contact details
+ identifiers
+ timeline compatibility
+ source provenance
      ↓
PROBABLE SAME ENTITY?
```

That does not require handing identity over to an AI and asking it to
pronounce judgement from the mountain.

It can be an auditing instrument.

Very high-confidence cases may be supported by deterministic
corroboration.

High- or medium-confidence cases can be sent for human review.

Ambiguous cases can remain separate.

Contradictory cases should not be merged merely because a model feels
enthusiastic.

The important new possibility is backward-looking:

> **Find records that probably should have joined but didn't.**

Search for:

-   orphaned records;
-   duplicate identities;
-   near-match names;
-   diacritic differences;
-   apostrophe differences;
-   hyphenation;
-   transliteration;
-   historic address changes;
-   surname changes;
-   migration failures;
-   regenerated identifiers;
-   truncated fields;
-   mismatched date formats;
-   NULL/blank inconsistencies;
-   records that repeatedly fail automated joins.

Then ask:

> **Who disproportionately appears in the cracks?**

Because information architecture inherits society.

Names carry histories of:

-   class;
-   migration;
-   language;
-   gender;
-   marriage;
-   literacy;
-   colonial administration;
-   regional practice;
-   family convention;
-   ideas about respectability and correctness.

The machine may receive only:

``` text
STRING A ≠ STRING B
```

The historical ecology that produced those strings can be enormous.

### Feedback reversal

The original failure:

``` text
human social judgement
        ↓
administrative record
        ↓
database
        ↓
failed match
        ↓
person falls through crack
```

A possible repair loop:

``` text
historical records
        ↓
entity-resolution system
        ↓
anomalous near-match
        ↓
human review
        ↓
records reconciled
        ↓
historical failure discovered
```

> **The information environment can begin finding its own scars.**

That is a much more interesting use of AI than merely automating the
main road faster.

Use some of the new computational capacity to go looking in the fucking
cracks.

------------------------------------------------------------------------

## 14. 👩‍💻 Deborah Would Quite Like To Go To Lunch

We now need to discuss the human who entered the information.

No human performing repetitive data entry, classification, tagging,
indexing or reconciliation will maintain a literally zero error rate
forever.

This is not an accusation of laziness.

It is a property of humans.

Suppose, purely as an illustration, a process were 99.99% accurate per
operation.

Across 10,000,000 operations, a simplistic independent-rate calculation
would still imply roughly 1,000 erroneous operations.

At 99.999%, roughly 100.

Real-world errors are not independent and uniformly distributed, so
these figures are not predictions.

They demonstrate scale.

> **At institutional scale, "our staff are very accurate" is not an
> error-handling strategy.**

Neither is:

> our software is reliable.

Good.

How does the system behave when the residual failure occurs?

Because Deborah has processed 4,000 records.

Her eyes hurt.

Her back hurts.

Teams has interrupted her nine times.

The font is too small.

The two names differ by one character.

She would quite like to go to lunch.

And the entire information architecture has quietly placed the integrity
of somebody's future record on whether an exhausted mammal notices an
umlaut.

Congratulations on your fantastic database.

------------------------------------------------------------------------

## 15. 👁️ The Eyes Attached To The Database

This is why occupational health belongs inside information engineering.

Workers' rights matter because workers are people.

That is sufficient.

But there is also a systems consequence that organisations should stop
pretending not to understand:

> **The integrity of an information system partly depends on the working
> conditions of the humans who maintain it.**

``` text
WORKING CONDITIONS
        ↓
fatigue / pain / attention / perception
        ↓
probability of input error
        ↓
quality of stored information
        ↓
matching / routing / retrieval
        ↓
institutional decision
        ↓
human outcome
```

A decent monitor can be an accessibility measure.

It can also be an error-control mechanism.

Adequate breaks can be a worker protection.

They can also improve sustained discrimination performance.

Ergonomic equipment can prevent pain.

Preventing pain can also preserve attention.

Reasonable workload can make employment humane.

It can also reduce rushed processing.

These benefits are not in competition.

The worker does not have to earn humane conditions by proving that
kindness increases productivity.

But if management requires a spreadsheet before it remembers that the
person attached to the keyboard has a body, the spreadsheet is
available.

### Sitting down is still an occupational environment

Industrial hazards are intuitively legible:

``` text
heavy thing → back
loud thing → ears
chemical → lungs
```

Screen work disguises its demands because the worker appears to be
sitting still.

The body is nevertheless doing things.

Eyes focus.

Hands repeat movements.

Wrists maintain positions.

Muscles stabilise the body.

The spine continues existing despite management's best efforts.

Attention is sustained.

Humans require movement.

There is nothing inherently ridiculous about workplaces building brief
movement into the day.

There is also no need to turn it into corporate wellness theatre.

We do not require:

> **At DataFuckr™, Movement Is One Of Our Core Values™️**

We require:

> Deborah can stand up without being treated as if she has abandoned the
> defence of the realm.

Humans now perform enormous quantities of sedentary screen-based labour.

Design work around the known properties of human bodies.

------------------------------------------------------------------------

## 16. 🛡️ RESILIENCE ENGINEERING, AMERICA

And therefore:

# RESILIENCE ENGINEERING, AMERICA.

The engineering problem is not:

> How do we build a system in which nobody ever makes a mistake?

That system does not exist.

The useful question is:

> **When the inevitable fuck-up occurs, how difficult is it for the
> system to notice, identify, contain, correct and learn from it before
> one tiny error becomes somebody's entire fucking life?**

That gives us a much better design vocabulary:

-   **detectability** --- can the failure be noticed?
-   **observability** --- can we see enough system state to understand
    it?
-   **containment** --- can one error be prevented from propagating?
-   **redundancy** --- is there another route or source?
-   **provenance** --- can we reconstruct where information came from?
-   **diagnosability** --- can we identify the failed layer?
-   **recoverability** --- can the correct state be restored?
-   **repairability** --- can repair happen without rebuilding
    everything?
-   **auditability** --- can the process be inspected afterwards?
-   **feedback** --- does the failure alter future system behaviour?
-   **institutional learning** --- does somebody actually change the
    fucking process?

The pieces we have already discussed fit directly into this:

``` text
worker protections
        ↓
human reliability

accessibility
        ↓
information integrity

good interface design
        ↓
error reduction

provenance
        ↓
diagnosability

redundancy
        ↓
recoverability

entity resolution
        ↓
detection of historic cracks

human review
        ↓
protection against false automated matches

edge-case auditing
        ↓
institutional learning

feedback
        ↓
adaptation
```

🦊: America. You are extremely good at engineering systems that do
extraordinary things.

🇺🇸: Thank you.

🦊: Could we perhaps also engineer them on the assumption that Deborah
will eventually type one letter wrong because she has processed 4,000
records and would quite like to go to lunch?

🇺🇸: ...

🦊: **RESILIENCE ENGINEERING, AMERICA.**

🌸: **LET US DO THAT.**

------------------------------------------------------------------------

## 17. 🏗️ Congratulations, Your Software Is Infrastructure Now

This is where the engineering question becomes a political-economic
question.

The classic consumer-software model is something like:

> We made a product.
>
> You decide whether you like it.
>
> If you don't, buy something else.

That becomes progressively less adequate as software moves into:

-   healthcare;
-   government;
-   banking;
-   employment;
-   education;
-   logistics;
-   defence supply chains;
-   communications;
-   identity;
-   public administration.

The person affected by the software may not have chosen it.

A patient did not necessarily choose the hospital records platform.

A claimant did not choose the government's case-management system.

An employee may not choose their employer's productivity stack.

A citizen does not individually procure every system through which their
administrative identity travels.

Even the organisation that did choose the software may face enormous
switching costs once the product is deeply integrated.

So the normal competitive instruction:

> **If you don't like it, leave.**

can become technically true and operationally absurd.

Infrastructure has different politics from products.

If your photo editor crashes, that is irritating.

If your identity record fails to match and you lose access to an
essential service, that is an administrative failure.

If a communications platform silently misroutes consequential
institutional information, that can become an organisational-resilience
problem.

If the same technical architecture is deeply embedded across thousands
of consequential organisations, its failure characteristics can become a
systemic-risk question.

That is the threshold.

The software company has not become evil.

The product has become important.

------------------------------------------------------------------------

## 18. 💰 Who Pays For The Failure?

Now consider incentives.

A supplier can gain financially from reducing expenditure on:

-   support;
-   testing;
-   redundancy;
-   maintenance;
-   edge cases;
-   accessibility;
-   backwards compatibility;
-   observability;
-   difficult migrations.

This does not mean every supplier will cut all of those things.

The structural question is **who bears the residual cost if it does?**

``` text
SUPPLIER
reduces resilience expenditure
        ↓
captures some savings


RARE FAILURE
        ↓
individual
        ↓
employer / hospital / council
        ↓
public services
        ↓
courts / regulators / welfare
        ↓
sometimes national-security consequences
```

The organisation deciding how much resilience to purchase and the
organisations paying for failure may not be identical.

That is an externality problem.

It is also one reason societies become interested in regulation,
standards, procurement conditions and liability once a product becomes
infrastructural.

> **The edge case can have almost no statistical mass and enormous human
> weight.**

A company may reasonably observe:

> This affects 0.01% of transactions.

The person inside the 0.01% may reasonably respond:

> **Yes. I am the fucking transaction.**

For an entertainment product, society may tolerate quite a lot of that.

For a system deciding whether somebody exists in the right
administrative record, tolerance changes.

------------------------------------------------------------------------

## 19. 🔧 Maintenance Is Part Of The Product

The sticker price of infrastructure is not the cost of infrastructure.

``` text
TOTAL COST
    =
acquisition
+ integration
+ training
+ support
+ maintenance
+ upgrades
+ downtime
+ investigation
+ remediation
+ migration
+ exit
+ residual failure
```

A system can be cheap to acquire and catastrophically expensive to
maintain.

A system can contain extraordinary functionality and still be a poor
infrastructural purchase if:

-   support is painful;
-   faults are opaque;
-   integrations are brittle;
-   upgrades repeatedly break workflows;
-   data is difficult to extract;
-   staff require constant workarounds;
-   exit is prohibitively difficult;
-   ordinary failures consume huge amounts of institutional labour.

Therefore:

> **Maintainability is a product characteristic.**

So is repairability.

So is interoperability.

So is the cost of leaving.

So is the ease with which a customer can understand what happened when
the system says everything is fine and the human says:

> **WHERE THE FUCK IS MY EMAIL.**

This is not anti-innovation.

It is procurement.

Bridges are not evaluated solely on whether the exciting new bridge
technology allows the bridge to be erected quickly.

Inspection matters.

Maintenance matters.

Service life matters.

Failure modes matter.

Repair matters.

Software does not become exempt because the founders wear trainers.

------------------------------------------------------------------------

## 20. ☁️ SaaS Is Not The Villain

We should be equally clear about what this argument is **not** saying.

Software-as-a-service is not inherently bad.

Subscription pricing is not inherently bad.

There are very good reasons why continuously operated software may have
a recurring price.

A recurring revenue model can fund:

-   continuous maintenance;
-   security patching;
-   infrastructure;
-   compatibility work;
-   support;
-   feature development;
-   monitoring;
-   backups;
-   ongoing engineering.

There is nothing incoherent about:

> **Pay us continuously because we continuously operate and maintain the
> thing.**

Indeed, that relationship creates an obvious reciprocal expectation:

> **If I am paying continuously for a continuously evolving service,
> competent ongoing maintenance is part of what I am buying.**

The problem is not:

> SaaS BAD.

The question is:

> **What obligations accompany continuous payment, continuous operation
> and continuous dependency?**

That is a grown-up commercial question.

------------------------------------------------------------------------

## 21. 👶 Congratulations, Your Industry Grew Up

New industries need room.

Standards are unsettled.

Nobody knows which architecture will survive.

Experiments fail.

Companies appear and disappear.

Regulation can genuinely freeze an immature technical model too early.

There is therefore a reasonable period in which society says:

> **Go and discover what this thing can become.**

But infancy is not a permanent regulatory status.

At some point an industry cannot simultaneously maintain:

> 👶 We are too young and innovative to carry mature obligations.

and:

> 🏗️ Please build civilisation on top of us.

Those propositions eventually collide.

### Baby industry

> Give us room to experiment.

Fair enough.

### Adolescent industry

> WHY DOES EVERYBODY KEEP TELLING US WHAT TO DO?

Ah.

### Mature infrastructural industry

> Which standards apply?
>
> What reliability is required?
>
> What are our support obligations?
>
> What does maintenance cost?
>
> How do we demonstrate compliance?
>
> What happens when we fail?
>
> What is the upgrade path?
>
> How does the customer exit?
>
> Can we still make money under those conditions?

That last stage is not the death of innovation.

It is the point at which the industry has become important enough that
other people need it to behave predictably.

> **Growing up is discovering that maintenance is part of the fucking
> invention.**

------------------------------------------------------------------------

## 22. 🇺🇸 America Has Exported Enormous Things Before

This part needs historical precision.

America has absolutely had enormously important export industries before
software.

Agricultural commodities.

Machinery.

Manufactured goods.

Automobiles.

Aircraft.

Chemicals.

Energy.

Entertainment.

Finance.

Intellectual property.

The claim is **not** that America has suddenly discovered exporting.

Nor should we claim without much more historical work that no previous
American export relationship has ever had comparable strategic
significance.

The interesting distinction is the **shape of the relationship**.

In 2025, US services exports were about **\$1.235 trillion**, alongside
roughly \$2.198 trillion in goods exports.[^7] The Bureau of Economic
Analysis also reports \$1.238 trillion in services exports in its
expanded-detail release.[^8]

The UK relationship is substantial in its own right. USTR currently
reports approximately **\$110.8 billion in US services exports to the
United Kingdom in 2025**.[^9]

Those figures do not mean "software" alone. Services trade contains many
categories.

They do establish the scale of the economic environment in which
digitally delivered and continuously maintained services now operate.

And that is where the historically interesting question appears:

> **What happens when an enormously valuable export remains
> operationally entangled with the customer's infrastructure after the
> sale?**

------------------------------------------------------------------------

## 23. 🔄 The Export That Doesn't Finish

Consider a simplified traditional export:

``` text
🇺🇸 FACTORY
     ↓
PRODUCT
     ↓
EXPORT
     ↓
🇬🇧 CUSTOMER
```

This is already simplified.

Aircraft need parts.

Machinery needs maintenance.

Manufacturers provide warranties.

Technical standards cross borders.

Finance and intellectual property have long produced continuing
relationships.

So do not turn this into a false historical binary.

But cloud and SaaS can intensify persistence:

``` text
🇺🇸 SUPPLIER
     ↕
SOFTWARE
     ↕
CLOUD INFRASTRUCTURE
     ↕
SECURITY
     ↕
IDENTITY
     ↕
APIs
     ↕
DATA
     ↕
SUPPORT
     ↕
UPDATES
     ↕
SUBSCRIPTION
     ↕
🇬🇧 INSTITUTION
```

**The export does not really finish.**

The supplier can remain continuously present inside the customer's
operating environment.

The product changes.

The security environment changes.

The law changes.

The customer's organisation changes.

The supplier's architecture changes.

The customer continues paying.

The relationship persists.

This is not merely a box arriving at a port.

It is an ongoing dependency.

And once an export relationship has that form at enormous international
scale, the political economy changes with it.

------------------------------------------------------------------------

## 24. 🌍 You Don't Need To Sell Us America As Well As The Software

There are two propositions that should not be confused.

### Proposition one

**American technological capability is impressive.**

The world is aware.

American companies have built extraordinary technologies.

American capital markets have financed extraordinary technologies.

American firms occupy extremely important positions in global
information infrastructure.

Fine.

Established.

### Proposition two

**Therefore American governance preferences should automatically travel
with American technology.**

No.

That does not follow.

A British customer remains British.

A French customer remains French.

A German institution remains German.

India does not become culturally American because it purchases American
cloud services.

Japan does not surrender its institutional traditions at the login
screen.

African countries are not one interchangeable political unit, and their
histories of colonialism, state formation, infrastructure and external
dependency will shape their own concerns differently.

The same is true across Latin America, the Middle East, Asia, Europe and
the Pacific.

Global customers bring:

-   their own law;
-   political traditions;
-   procurement rules;
-   labour norms;
-   privacy expectations;
-   accessibility requirements;
-   security concerns;
-   historical experience;
-   risk tolerances;
-   administrative cultures.

The supplier does not have to privately agree with every one of them.

The supplier does have to decide whether it wants to do business there.

> **International disagreement with an American incentive structure is
> not necessarily an attack on America.**

Sometimes another component of the system is simply optimising for
something else.

------------------------------------------------------------------------

## 25. 🧒 Playing Nicely With The Other Children

This may be one of the genuinely new cultural problems created by the
success of American software exports.

Again, phrase this cautiously.

The United States has obviously conducted enormous international trade,
diplomacy and industrial cooperation before.

What is distinctive about contemporary software and cloud infrastructure
is the combination of:

-   scale;
-   value;
-   continuous operation;
-   persistent supplier involvement;
-   deep institutional embedding;
-   rapid technical change;
-   cross-border data and service dependency.

That combination requires unusually sustained relationships with
customers whose political systems and cultural assumptions remain their
own.

So perhaps the lesson is not even:

> play nicely with the other children.

It is:

> **You have become extraordinarily successful at something that
> requires unusually sustained international cooperation. That success
> changes what competent participation looks like.**

A company may encounter:

-   British expectations about public administration;
-   EU regulatory requirements;
-   Japanese organisational expectations;
-   Indian legal and market requirements;
-   Canadian procurement;
-   Australian security concerns;
-   dozens of other combinations.

The mature commercial response is not:

> Why won't everybody organise society like us?

It is:

> **What requirements apply here, what do they cost us, can we satisfy
> them, and do we still want this customer?**

Requirements famously impose costs.

So does reliability.

So does cybersecurity.

So does accessibility.

So does redundancy.

So does support.

So does testing.

The existence of cost does not settle whether the requirement is
justified.

Regulation can absolutely be badly designed.

Governments can impose incoherent requirements.

Compliance fragmentation can create real technical and commercial
friction.

Those are legitimate arguments to have.

But:

> **"This slows innovation" cannot remain a universal veto once the
> innovation has become infrastructure.**

At some point the industry has to participate in society.

------------------------------------------------------------------------

## 26. 🌎 We Already Know Your Stuff Is Cool

There is a cultural communication problem here that can be expressed,
with suitable academic restraint, as:

> **We already know how big your dick is.**

Meaning:

**the demonstration of capability has succeeded.**

The rest of the world does not generally require daily proof that:

-   America is powerful;
-   America is rich;
-   American firms can innovate;
-   American technology can be extremely good;
-   American capital can build things at astonishing scale.

We have seen the fucking computers.

The customer may already have moved several stages further through the
procurement conversation.

🇺🇸: **LOOK HOW ADVANCED AND POWERFUL WE ARE.**

🇬🇧: Yes, yes. Extremely impressive. Who maintains it?

🇩🇪: What standard does it comply with?

🇫🇷: Why have you designed it like that?

🌍: What happens when it breaks?

🇺🇸: BUT HAVE YOU SEEN THE AI---

🌍: **YES. VERY SHINY. NOW ANSWER THE FUCKING QUESTIONS.**

Those questions are not necessarily challenges to American greatness.

They are what happens **after the customer has already accepted that the
product is worth considering**.

Can we depend on it?

Can we afford to maintain it?

Can we understand what it is doing?

Can we integrate it?

Can we recover when it fails?

Can we get our data out?

Can we leave?

Will you comply with our law even if you personally think our law is
silly?

Will somebody answer the fucking support ticket?

This is the less glamorous second half of technological leadership.

The first half is making the extraordinary thing.

The second is maintaining a long-term relationship with customers who
have no intention whatsoever of becoming American.

------------------------------------------------------------------------

## 27. 🦊 The Fox Discovers Maintenance

🦊: Cousin. Congratulations.

🇺🇸: Thank you.

🦊: No. Unfortunately this is the bad news.

🇺🇸: What happened?

🦊: **Your industry grew up.**

🇺🇸: ...

🦊: We need to discuss maintenance.

There is a serious policy proposition underneath the fox.

Global market access increasingly requires software suppliers to accept
some of the ordinary obligations associated with mature infrastructural
industries:

-   reliability;
-   maintainability;
-   accountability;
-   interoperability;
-   support;
-   predictable lifecycle costs;
-   security;
-   accessibility;
-   compliance with the societies in which the product operates.

Different jurisdictions will draw those obligations differently.

There is an entire spectrum available before anybody starts yelling
about nationalisation:

``` text
technical standards
        ↓
interoperability requirements
        ↓
accessibility requirements
        ↓
auditability
        ↓
incident reporting
        ↓
support obligations
        ↓
data portability
        ↓
procurement conditions
        ↓
resilience testing
        ↓
liability
        ↓
regulatory supervision
        ↓
public alternatives
        ↓
public ownership
```

Countries will disagree about where to intervene.

That is normal.

The important principle is that once private software performs public or
infrastructural functions, **the public acquires an interest in its
failure characteristics whether or not the state owns the supplier**.

You do not have to nationalise the software company.

You do have to recognise why governments eventually ask:

> **Who bears the tail risk created by this infrastructure, and what
> incentive does the supplier have to reduce it?**

🦊: Good news, chaps. We have discovered a framework.

🇺🇸: Which framework?

🦊: **Apparently it is "maintenance".**

------------------------------------------------------------------------

## 28. 📋 Return To Exhibit J

We have now travelled from one overdue parliamentary answer through:

-   email transport;
-   human attention;
-   interface design;
-   Clippy;
-   Encarta;
-   ancient hard drives;
-   Unicode;
-   identity matching;
-   historical records;
-   AI;
-   worker fatigue;
-   occupational health;
-   resilience engineering;
-   SaaS;
-   infrastructure;
-   regulation;
-   international trade;
-   American cultural confidence.

Excellent.

Where is the email?

**We still don't know.**

That is the point.

The observed delay does not tell us whether the underlying cause is:

-   substantive;
-   political;
-   security-related;
-   legal;
-   administrative;
-   technical;
-   human;
-   organisational;
-   or completely mundane.

The correct response to uncertainty is not to erase it.

It is to map the system through which the answer must eventually travel.

Because if the eventual explanation is enormous, we want a method
capable of finding enormous things.

And if the eventual explanation is:

> somebody missed a character;

or:

> the attachment was separated from the covering email;

or:

> the search did not return the record;

or:

> two systems disagreed about an identifier;

or:

> everybody thought somebody else owned the question;

we want a method capable of finding those things too.

Same investigative method.

Different mechanism.

That is why "Where the fuck is that email?" is not actually a trivial
question.

It is a request for failure localisation.

------------------------------------------------------------------------

## 29. ♻️ What Exhibit J Actually Teaches

### Information transport is not information reception

A message can move successfully through infrastructure without becoming
usable information for the intended human.

### Information reception is not attention

The message can be present and unseen.

### Attention is not organisational action

A person can read something without the institution successfully
ingesting it.

### Local success can coexist with global failure

Every component can report green while the human-level task remains
broken.

### Tiny differences can produce enormous consequences

One character can be irrelevant in one context and identity-splitting in
another.

### Humans have non-zero error rates

At sufficient scale, residual mistakes are not shocking anomalies. They
are design conditions.

### Human bodies are part of information infrastructure

Eyes, attention, pain, fatigue, accessibility and working conditions
affect information quality.

### AI can create new errors and expose old ones

Probabilistic systems require safeguards, but richer entity resolution
can also discover historic false non-matches.

### Resilience beats fantasies of perfection

Design for detection, containment, diagnosis, recovery and learning.

### Infrastructure changes commercial obligations

A continuously embedded service is not merely a consumer object.

### Continuous software creates continuous relationships

SaaS can be an excellent model precisely because continuous operation
requires continuous maintenance.

### Global infrastructure suppliers have plural stakeholders

Customers do not cease having their own laws, institutions, cultures and
incentives because the supplier is American.

### An anomalous observation does not establish its mechanism

Keep uncertainty alive until evidence kills alternatives.

### A mistaken explanation does not make the underlying anomaly imaginary

Someone can be wrong about **why** a system failed while being entirely
correct that **something failed**.

That distinction may be one of the most important in the whole node.

------------------------------------------------------------------------

## 30. 🪭 Information Does Not Arrive Alone

There is a constellation here with the Austen Cybernetics problem.

The same observation can produce different information for different
observers because the observation is processed through different models.

Lady Catherine observes Elizabeth's refusal.

Lady Catherine extracts one meaning.

Darcy, possessing different context, can extract another.

The help desk observes green telemetry.

The help desk receives:

> components operational.

The user observes the absent email.

The user receives:

> task failed.

The database observes:

``` text
Chloe != Chloë
```

The database returns:

> FALSE.

The human observes both names.

The human receives:

> obviously potentially the same person.

The American supplier observes:

> regulatory friction.

The customer may observe:

> infrastructure risk requiring governance.

None of this means every interpretation is equally correct.

It means:

> **information does not possess a complete, fixed social meaning
> independent of the system processing it.**

Which is why context, provenance and feedback matter.

And why the most useful question is often not:

> Who is wrong?

but:

> **What information is each component actually receiving, and what
> operation is it performing on it?**

------------------------------------------------------------------------

## 🌌 Constellations

♻️ 🕸️ 🧬 🦾 🦊 --- feedback environments; embodied information; identity
and record-linkage failure; resilience engineering; transatlantic
infrastructure translation.

------------------------------------------------------------------------

## ✨ Stardust

embodied information ecology, feedback environments, information
infrastructure, email delivery, human attention, entity resolution,
resilience engineering, software maintenance, saas, international
digital trade

------------------------------------------------------------------------

## 🏮 Footer

*📋 Exhibit J: Where The Fuck Is That Email?* is a living node of the
**Polaris Protocol**.\
It uses a small information-routing anomaly as a teaching specimen for
the larger distinction between data transport, human experience,
institutional action and recoverable infrastructure. The node follows
that distinction outward into identity matching, embodied labour,
resilience engineering, software maintenance and the international
obligations created when continuously operated software becomes
infrastructure.

> 📡 Cross-references:
>
> -   [🎩 Putting On Less Ritz](./README.md) --- *parent cluster for
>     preserving mundane and extraordinary hypotheses until evidence
>     distinguishes them*
> -   [♻️🕸️ The Feedback Environment](../README.md) --- *feedback,
>     system response and information-routing context*
> -   [♻️ Cybernetics](../../README.md) --- *wider systems and feedback
>     framework*
> -   [🪿 Embodied Information Ecology](../../../README.md) ---
>     *information as situated, embodied and environmentally mediated*
>
> 🏮 Return To:
>
> -   [🎩 Putting On Less Ritz](./README.md) --- *1up*
> -   [♻️🕸️ The Feedback Environment](../README.md) --- *2up*
> -   [♻️ Cybernetics](../../README.md) --- *3up*
> -   [🪿 Embodied Information Ecology](../../../README.md) --- *4up*
> -   [🌑 Origin Points](../../../../README.md) --- *5up*
> -   [🌌 Polaris Protocol --- Root](../../../../../README.md) ---
>     *root*

*Survivor authorship is sovereign. Containment is never neutral.*

*Last updated: 2026-09-24*

------------------------------------------------------------------------

[^1]: UK Parliament, "Written questions and answers", Mike Wood MP, UIN
    20754, asked 28 August 2026.
    <https://questions-statements.parliament.uk/written-questions?MemberIds=5061&Page=1336>

[^2]: UK Parliament, "Written questions and answers", Mike Wood MP, UIN
    20754, asked 28 August 2026.
    <https://questions-statements.parliament.uk/written-questions?MemberIds=5061&Page=1336>

[^3]: Microsoft Support, "Focused Inbox for Outlook".
    <https://support.microsoft.com/en-us/outlook/mail/focused-inbox-for-outlook>

[^4]: Scotland's People, "Surnames" --- official guidance on spelling
    variation, exact matching, fuzzy matching and registrar/clerk
    interpretation.
    <https://www.scotlandspeople.gov.uk/help-and-support/guides/surnames>

[^5]: Scotland's People, "Forenames" --- official guidance on variant
    spellings, abbreviations, diminutives, anglicisation and
    inconsistent historical recording.
    <https://www.scotlandspeople.gov.uk/help-and-support/guides/forenames>

[^6]: Office for National Statistics, "Higher Education Statistics
    Agency data: quality assurance of administrative data used in
    population statistics", February 2017.
    <https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/methodologies/highereducationstatisticsagencydataqualityassuranceofadministrativedatausedinpopulationstatisticsfeb2017>

[^7]: US Bureau of Economic Analysis, "U.S. International Trade in Goods
    and Services, December and Annual 2025".
    <https://www.bea.gov/news/2026/us-international-trade-goods-and-services-december-and-annual-2025>

[^8]: US Bureau of Economic Analysis, "International Services (Expanded
    Detail)", current release 7 July 2026.
    <https://www.bea.gov/data/intl-trade-investment/international-services-expanded>

[^9]: Office of the United States Trade Representative, "United
    Kingdom", 2025 trade summary.
    <https://www.ustr.gov/countries-regions/europe-middle-east/europe/united-kingdom>
