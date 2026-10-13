# 🇺🇦 Bombing the Bot Farms
**First created:** 2026-10-11 | **Last updated:** 2026-10-13  
*Distributed information operations, partial infrastructure failure, and the unequal human consequences of changes in the observed information space.*

---

## 🛰️ Orientation

🇺🇦 **SILENCE, BOT.**

An excellent line. Unfortunately, the research question is not quite so obliging.

Reports of Ukrainian drone strikes affecting Yandex data-centre infrastructure in October 2026 collided with a remarkable collection of accounts from people saying that their online environments had become quieter, less hostile, and more responsive to what they actually wanted to see. Some accounts came from Ukrainians; others came from women, racialised people, trans people, and other people who regularly encounter identity-based hostility. The author reports a marked change in her own feed: less friction, fewer unwanted diversions, and more of the material she had actually chosen to follow. That is a report about the functioning of an interface, not merely a statement about mood.

The circulating story was simple: Ukraine had bombed Russian bot farms; the bots had gone quiet. The available evidence is less simple. Reported damage to computing facilities is not proof that particular political influence operations were hosted there. A graph of bot-classified requests is not a census of propaganda accounts. And monitoring that finds propaganda-posting accounts still active does not, by itself, establish that the surrounding information ecology is unchanged.

**The question is not just which bots stopped posting. It is what dependencies may have changed, which outputs remained, which functions deteriorated, and who noticed.** This node separates documented reporting, attributed testimony, established technical mechanisms, and hypotheses requiring investigation. It does not identify the operator of any particular user's feed experience.

---

## 1. 💥 The Internet Has a Server Room, Actually

Reuters reported on 8 October 2026 that drones struck a Yandex data centre in Russia's Ryazan region, with fire, suspended operations and disruption affecting cloud services. Follow-up reporting described uncertainty over restoration at Sasovo. On 11 October Reuters reported a further shutdown in the Vladimir region and disruption at Kaluga. Yandex said core consumer services continued operating [1–3]. These are reports of damaged or interrupted infrastructure; the particular workloads hosted there have **not** been identified here as political influence operations.

A data centre is not an ideology. It is buildings, electricity, cooling, storage, processors, network routes, administrators and service contracts. A cloud dependency can serve people thousands of miles from the damaged building. It may also host ordinary civilian services. The distinction matters technically, evidentially and legally.

🇷🇺: We have constructed a sophisticated digital ecosystem.

🇺🇦: Have you considered having fewer computers?

The joke identifies a material vulnerability, **not** a verified inventory of what was inside.

---

## 2. 🕷️ A Bot Is Not Necessarily the Bot You're Looking For

'Bot' is doing several jobs at once. A crawler indexes pages; a scraper extracts material; a monitoring agent detects new topics; analytical automation processes data; a posting bot publishes; engagement automation manipulates apparent popularity; and a human-operated influence account may be deceptive without being automated at all. These functions can overlap, but they are not synonyms.

| Measurement | Can indicate | Cannot establish alone |
|---|---|---|
| Bot-classified HTTP requests | Automated request volume or share | Number of political propaganda accounts |
| YandexBot or other crawler requests | Search/indexing activity | Disinformation-posting capacity |
| Russian-labelled IP traffic | Network or geographical classification | Operator identity or political intent |
| Known influence accounts still posting | Continuity of visible publishing | Unchanged analysis, coordination, reach or effectiveness |
| Reduced hostile material in a feed | Changed user exposure | Which upstream system caused it |

The circulated **49%** claim needs its original chart, denominator, time window and definition. 'Fell by 49%', 'fell to 49%' and 'accounted for 49%' mean different things. Cloudflare Radar publishes bot-traffic measurements for Russia, but these are web-request metrics, not a political-bot census [4–5]. Subsequent commentary has pointed particularly to crawler activity. This node does not treat the viral percentage as a verified collapse of propaganda posting.

**A scraper does not have to publish propaganda to support an operation that does.** Equally, no evidence follows from the mere existence of a scraper that it supports such an operation. The dependency must be shown.

---

## 3. 🕸️ A Distributed Operation Does Not Die All at Once

A sophisticated information campaign can distribute collection, analysis, content production, posting, amplification and monitoring across different services, people and jurisdictions. These are *functions*, not necessarily separate companies or server rooms. A single provider can support several; a single function can run across many providers. Redundancy protects some capacities while leaving shared dependencies vulnerable.

| Function | Possible result of partial disruption | What may continue |
|---|---|---|
| Collection | Less fresh information | Old datasets and scheduled posts |
| Analysis / audience modelling | Slower or less context-sensitive targeting | Broad messaging |
| Content production | Less adaptation to events | Existing content libraries |
| Distribution | Fewer or delayed posts | Other channels |
| Amplification | Reduced apparent popularity or reach | Original posts |
| Monitoring / feedback | Poorer campaign measurement | Human operators and prior strategies |

A system may continue operating while its **effectiveness** changes. In engineering terms, the interesting signature may be *partial failure*, *graceful degradation*, or *substitution*. Failure patterns can expose shared dependencies, although they cannot identify a covert operator without independent evidence.

This is why 'the posting bots are still there' is an incomplete systems-level answer. It may be a correct observation about one component and still leave the rest of the architecture untested.

---

## 4. 🧠 Cambridge Analytica: We Have Been Here Before

The Cambridge Analytica scandal supplies a documented historical reason to take the combination of personal data, behavioural modelling, political messaging and institutional accountability seriously. It is **not** proof that the Yandex facilities supported a Cambridge Analytica-style operation.

Christopher Wylie gave evidence to the UK House of Commons Digital, Culture, Media and Sport Committee on **27 March 2018**. His evidence described Cambridge Analytica/SCL contacts with senior representatives of the Russian oil company Lukoil and discussions of political profiling and influence capabilities [6–7]. That is more specific than 'somebody met somebody Russian'. It is also narrower than proof that Lukoil received Facebook-derived data or that Cambridge Analytica knowingly collaborated with Russian intelligence: those conclusions are **not established** by Wylie's account.

The useful distinction is not between magical personality prediction and no capability at all. It is between commercial claims about psychographics, which were not all independently validated, and the practical capacity to segment audiences, select issues, test messages and model **context-dependent choices**. A campaign need not know the innermost soul of every voter to seek influence over what people encounter and how they respond.

The UK's Information Commissioner's Office investigated political data analytics, improper data practices and questions concerning derived models [8]. Its October 2020 account to Parliament set out findings, evidential limits and referrals, including concerns passed to the National Crime Agency; it did **not** establish additional Russian involvement from its examination of seized Cambridge Analytica/SCL servers [9]. We must not turn a limit of public knowledge into proof of a hidden transfer. Nor should the closure of a company be mistaken for a complete public history of every dataset, derivative, method, contractor or professional relationship.

**Historical question:** what was established, what was referred elsewhere, what was not established, and what has never received a complete public accounting? Those are four different columns, not one convenient narrative.

---

## 5. 🧿 The Immediate Target May Not Be the Intended Audience

An operation might collect information from one population, concentrate hostility on a second, and hope to influence a third through the spectacle of conflict. The data subject, immediate target, visible intermediary and intended audience need not be the same person. They may overlap.

For example, **hypothetically**, concentrated hostility against a marginalised speaker could generate public argument; genuine users and journalists might then circulate that argument; a wider audience might encounter it as evidence of a supposedly spontaneous social controversy. The original coordinated contribution can become a real human feedback loop. This mechanism is plausible; it is **not** an attribution to a named campaign or evidence that particular individuals were selected by a state.

There is also a cost question. An operator trying to shape a broad public conversation could, in principle, focus intense effort on a smaller set of speakers or communities whose treatment will be noticed by a larger audience. That is a plausible *strategy of indirect influence*, not evidence that minority speakers are invariably the cheapest or most effective targets. Its effectiveness would depend on social networks, audience response, media uptake and the political objective.

Resource constraints make geographic and audience segmentation worth studying. In a UK electoral setting, constituency-level concentration could matter more than national averages. That does not justify assuming which seats or demographic groups are susceptible, or claiming a Russian-directed operation targeted them without documentation.

---

## 6. 🫀 Whose Internet Has Become Quieter?

The author describes a change in ordinary browsing: less unsolicited antagonism, fewer apparently intrusive recommendations, more content reflecting previous interests, and less need to push through hostile material to get to the thing she actually came online to do. She also describes experiencing misogyny and racialised hostility online over time. This is **first-person observation of a changed interface and participation environment**. It neither requires nor supplies a diagnosis of the upstream cause.

Other online accounts gathered in the node's constellation describe relief among Ukrainians, women, Black and brown people, trans people and other LGBTQIA+ users. These accounts are valuable leads, not a representative sample. They warrant comparison by platform, period, exposure and user context, rather than being dismissed or silently converted into population statistics.

Intersectionality matters because hostile exposures may overlap and interact. A racialised woman is not simply receiving 'women's content' plus 'racial content' as two independent streams. A long digital history may also make more information available for profiling through public archives, platforms, commercial intermediaries and institutions. **More available data is not proof that any particular actor obtained or exploited it.** The testable question is whether accumulated data and intersecting social positions are associated with different kinds or concentrations of hostile exposure.

One user may observe polarising political arguments. Another may repeatedly encounter arguments about whether people like her should be safe, employed, believed or permitted to participate. The same aggregate traffic volume does not describe those two environments equally. Nor does a similar technical disruption have to produce equal effects across them.

---

## 7. 🕳️ Reduced Noise Is Not Necessarily Reduced Posting

The observed information space is not a census of the population. It is what people can see through ranking, search, recommendation, networks, moderation and their own choices. Artificial engagement can alter visibility; human reactions can then amplify material further. That is a *possible* feedback pathway, not a verified description of any particular platform's ranking system.

We need separate instruments for **posting volume**, **collection freshness**, **targeting fidelity**, **coordination**, **engagement**, **recommendation placement**, **hostile exposure**, and **navigational autonomy**. An account can continue posting while its messages become less timely, less widely circulated or less frequently encountered by particular users. Conversely, a platform update could change recommendations without any foreign infrastructure being affected.

A reduction in *collection freshness* could mean slower reaction to new topics without fewer posts. A reduction in *amplification* could mean the same number of posts with fewer impressions. A change in *platform ranking* could produce a similar user-facing result without any campaign infrastructure failure at all. These are rival pathways, not interchangeable labels for one event.

The counterfactual question is: *what would these measures have looked like without the October outage?* Compare pre-event baselines, affected and unaffected networks, other platforms, moderation changes, contemporaneous news and later recovery. A striking coincidence is a reason to investigate, not a completed causal attribution.

---

## 8. 🔐 No, Brenda, a VPN Does Not Fix Institutional Data Governance

The standard 'just improve your cybersecurity' answer assumes people control all the relevant security boundaries. They don't. Strong passwords, multifactor authentication, careful sharing and VPNs may reduce particular risks. None can independently secure healthcare records, government databases, an employer's systems, a platform's data processing, a broker's files, or somebody else's disclosure of information. Even excellent personal practice cannot guarantee protection against harassment or profiling.

There is an ugly resemblance to the prevention conversation that tells women not to wear the skirt, drink the drink, walk the road or go out after dark. Every precaution is assigned to the person at risk until ordinary participation itself becomes the thing they are expected to surrender. **Responsibility for abusive conduct stays with those committing it; responsibility for institutional data security stays with those holding the data.** Practical self-protection has a place. It is not a substitute for enforcement, platform governance or investigation.

This is a governance argument, not evidence that the author's information was obtained through a particular breach. The source of any unusually personalised activity must be established, not guessed.

---

## 9. 🛰️ Wars Are Also Information Environments

The author's wider context includes the Gaza war and campaigns discussed under the name **Operation Iron Swords**, the war involving Iran, Russia's documented history of influence operations, and increasingly contentious political communication across the US and Europe. These are distinct contexts; their operators, techniques and evidence must not be merged into one undifferentiated conspiracy. State operations, contractors, commercial promotion, ordinary advocacy and genuine political disagreement require different attribution standards.

The author's observation of **stepwise increases** in hostile online exposure over recent years is a longitudinal research question: what events, platform changes, campaigns or social shifts coincide with measurable jumps? The MI5 Director General's **13 October 2026** threat update belongs in the dated security chronology, but specific claims about terrorism, online radicalisation and disinformation should be quoted only after checking the full primary statement [10]. None of these surrounding events independently proves a link to the Yandex strikes.

---

## 10. 📊 The Fact-Check That Answers Only One Question

If a fact-check establishes that a viral graph mostly measured Yandex crawling rather than political posting, **good**: correct the graph. If monitoring finds that known Russian influence accounts continued publishing, **good**: record the continuity. Neither finding establishes that all possible supporting functions remained unaffected, or that users' feeds did not change. Nor does an untested possibility become likely merely because it has not been ruled out.

| Question answered | Question still open |
|---|---|
| Were the requests mostly crawlers? | Did any affected collection capacity feed influence operations? |
| Are known posting accounts still active? | Did targeting, responsiveness, amplification or reach change? |
| Did a viral numerical claim misuse its denominator? | What did individual users actually encounter before and after? |
| Is a particular causal claim unproven? | What other explanations fit the observations? |

A reported reduction in friction is an observation to examine. A causal account of that reduction is a separate claim. **Disproving an explanation is not the same as disproving the observation.** Equally, observing a change does not prove its preferred explanation.

The methodological error would be to declare the whole subject closed because the most quotable version of the story failed.

---

## 11. 🎭 When the Noise Drops, Who Starts Shouting?

If political actors are accustomed to artificial reinforcement, their behaviour might change when that reinforcement weakens. Three possibilities must remain distinct: **knowing coordination** with an operation; **unknowing adaptation** to distorted engagement signals; and **ordinary political behaviour** driven by elections, news, strategy or personal incentives. Posting louder after an outage is not evidence of secret contacts.

🪿: The room appears quieter.

🎭: SOMEONE FETCH ME A LOUDER MICROPHONE.

🪿: Interesting. Not proof. Interesting.

The question is whether a measured change in one kind of activity precedes a measured change in another, survives comparison with controls, and can be connected through a documented mechanism.

---

## 12. 🕸️ Diagrams — What Breaks, What Continues, Who Notices?

These diagrams describe **hypothetical dependencies**, not a verified map of the Yandex facilities. A solid arrow means a possible ordinary functional flow; a dashed arrow means a connection that must be evidenced for this case; `[X]` marks a hypothetical interruption; `↺` marks feedback. No diagram can substitute for service inventories, network evidence or platform exposure data.

### A. Distributed operation and partial failure

```text
       PROVIDER A             PROVIDER B            PROVIDER C
       collection             datasets /             posting /
          [X]                 analysis              distribution
           │                      │                      │
           └ - - - - ┐            │                      │
                     ▼            ▼                      │
                AUDIENCE MODELLING                       │
                     │                                   │
                     ▼                                   │
                MESSAGE SELECTION ───────────────────────┤
                                                         ▼
                                                  POSTS CONTINUE
                                                         │
                                         ENGAGEMENT / AMPLIFICATION
                                                         │
                                                  PLATFORM SYSTEMS
                                                         │
                                                    USER EXPOSURE
                                                         │
                                               MONITORING / FEEDBACK
                                                         ↺
```

**Reading A:** losing a collection dependency might reduce freshness or precision while existing posts continue. Other providers may substitute. The diagram does **not** claim this happened in October; it shows why continued posting is not a full operational-health test.

### B. Unequal exposure, feedback and embodied effects

```text
     CONTENT + GENUINE ENGAGEMENT + POSSIBLE ARTIFICIAL SIGNALS
                               │
                               ▼
                 PLATFORM RANKING / RECOMMENDATION
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
           USER SPACE A   USER SPACE B   USER SPACE C
           low hostile    overlapping    high exposure
           exposure       exposures      to one theme
                │              │              │
                ▼              ▼              ▼
          OBSERVATION     OBSERVATION     OBSERVATION
          + RESPONSE      + RESPONSE      + RESPONSE
                └──────────────┼──────────────┘
                               ▼
                        HUMAN PARTICIPATION
                               │
                               ↺ feeds the observable environment

     HYPOTHETICAL UPSTREAM CHANGE - - -> altered signals / placement
                                           (unequal downstream effects)
```

**Reading B:** people do not receive one uniform internet. A change in an upstream signal can have uneven consequences; the direction and size depend on platform behaviour, prior exposure, other causes and real user activity. This is not a claim that identity itself determines algorithmic treatment.

**Visual implementation rule:** In the final rendered version, label *platform ranking* as a separate actor, not an arm of the alleged operation. Draw more than one infrastructure provider, show failover, and mark the affected component as *hypothetical*. Show at least two differentiated user-exposure paths and a feedback route into collection. Use separate visual conventions for measured facts, user testimony, general technical mechanisms and October-specific hypotheses. A dashed arrow must not become a solid arrow merely because it looks nicer.

**Diagram development note:** these monospace diagrams are semantic scaffolds. A later designed visual should retain separate arrows for collection, modelling, posting, amplification and platform ranking, plus clear boundaries between established relationships and October-specific hypotheses. Do not silently turn a dashed connection into a solid one for aesthetic neatness.

---

## 13. 📰 An Assignment for Journalists Who Would Quite Like to Finish the Investigation

Start with a dated *before* baseline. Obtain facility/service outage and restoration records; request network series with absolute counts and denominators; distinguish crawlers, scraping, political accounts and coordinated engagement. Compare the posting behaviour of independently identified networks with their timing, topic responsiveness, repost structure and reach. Then examine **exposure**, not only output: recommendation relevance, unsolicited hostile encounters, navigation interruptions and the ability to reach intended content.

Recruit participants across different platforms, locations and forms of exposure without treating identity groups as interchangeable or their testimonies as a statistical sample. Preserve participant privacy; do not create new dossiers of people who have already experienced harassment. Compare against moderation changes, algorithm updates, elections, news cycles, other outages and restoration. Look for temporal alignment, specificity, dose-response, substitution and recovery. Publish negative findings too.

### A comparison that could actually discriminate between explanations

| Competing explanation | Distinctive prediction to test | Evidence needed |
|---|---|---|
| Disrupted collection or analysis | Posting persists, but topical adaptation or targeting becomes less timely | Dated network behaviour, collection/service evidence |
| Disrupted amplification | Similar posting volume, but lower reach or altered engagement pathways | Platform impressions, recommendation audits, coordinated-engagement traces |
| Platform-side change | Feed exposure shifts even in audiences or services with no plausible Yandex dependency | Platform change logs, matched unaffected comparison groups |
| Ordinary news or political-cycle change | Content and engagement shift alongside a major external event | Dated news, election and participation baselines |
| Selection or reporting effects | Dramatic anecdotes are more visible than unchanged experiences | Preregistered sampling, longitudinal panels, negative reports |
| Several mechanisms at once | Different measures change at different times or across different populations | Multi-platform, multi-measure time series and restoration windows |

**Do not ask people who have experienced harassment to hand over intimate browsing histories as the price of being believed.** Research design must include informed consent, data minimisation, safe withdrawal and publication rules that do not expose participants to renewed targeting. A prospective panel can record changes without demanding a complete personal dossier.

The author is not asking journalists to announce that Ukraine repaired the internet. She is asking them not to abandon a potentially consequential change in the information environment because a crawler chart was mistaken for a propaganda census.

---

## 14. ⚖️ Infrastructure Disruption Is Not Automatically Democratic Repair

Data centres can support civilian communications and commerce. Under international humanitarian law, the legality of an attack depends on facts including military-objective status and applicable rules on distinction, proportionality and precautions. A speculative benefit to online discourse does not itself justify attacking shared civilian infrastructure. And even a demonstrated reduction in artificial amplification would not reverse the social effects of earlier hostility: real people have already acted in the environment they encountered.

---

## 15. 🪿 Please Listen Before You Close the Investigation

I am not asking you to pretend that a Cloudflare graph proves the Kremlin's posting bots have all fallen into a hole. I am asking you to distinguish what your instrument measures from what the people using the internet are telling you has changed.

I have experienced a markedly different online environment: less friction, less unwanted antagonism, and browsing that feels more like my own directed browsing again. I have also experienced misogyny and racialised hostility online. I cannot reverse-engineer a distributed information operation from my feed. **That is not a reasonable condition to impose before listening to what has changed.**

And, respectfully, some of the security people explaining why the bots are still there are white men whose own social position may expose them to different kinds and concentrations of hostility. That does not make their technical findings wrong. It does make their experiences an inadequate proxy for everybody else's. The people who have been dealing with the sharp end of the environment may be noticing changes that a count of posting accounts will never capture.

Perhaps several things changed at once. Perhaps the strikes contributed. Perhaps they didn't. The evidence needs to decide that. But **a fact-check should correct a false attribution, not place a lid on a different and still-unanswered research question**. Before moving along, please investigate what people were exposed to, what has become less intrusive, and why the difference is not evenly felt.

🇺🇦 **SILENCE, BOT.**

🪿 **Well. Something appears quieter. Now let's see what the instruments actually say.**

---

## 16. 🔬 Evidence Register and Research Queue

| Proposition | Evidentiary position as of 13 October 2026 |
|---|---|
| Reported attacks disrupted Yandex facilities | Supported by cited Reuters reporting [1–3] |
| Cloudflare Radar measures bot-classified HTTP traffic | Supported by documentation [4–5] |
| Viral 49% figure proves political bots disappeared | **Not established**; original graph/denominator required |
| Particular influence workloads ran at struck facilities | **Not established** |
| Known propaganda posting continued | Attributed in contemporary fact-check reporting; verify scope, dataset and dates before treating as comprehensive [11–12] |
| Distributed operations can partially degrade | General systems mechanism; no case attribution |
| Data collection can inform audience modelling | General capability; specific linkage requires evidence |
| Wylie testified about Cambridge Analytica–Lukoil contacts | Documented testimony [6–7] |
| Lukoil obtained the Facebook-derived dataset | **Not established** |
| ICO investigated political data practices and reported limits | Supported by ICO material [8–9] |
| Marginalised people reported pronounced changes | Accounts collected in Constellations; not representative prevalence data |
| Author's browsing environment changed substantially | First-person testimony; causal source not established |
| October strikes caused the reported feed changes | **Open hypothesis**, not finding |

**Evidence provenance rule:** Keep three separate records for each significant claim: (1) what the original source directly says or measures; (2) what a journalist or creator infers from it; (3) what this node proposes as a further hypothesis. A link's presence is not authentication. In particular, obtain the underlying crawler series and confirm contemporary reports before upgrading any October-specific assertion from attributed reporting to established fact.

**Next evidence:** archive the Finnish commentator's original words; authenticate the 49% graph and API series; obtain dated Yandex service restoration information; retrieve the full MI5 speech; inspect the methods of October fact-checks; seek ethically collected pre/post feed-exposure data; compare unaffected networks and platforms; investigate Cambridge Analytica's documented international relationships and the boundaries of official investigations; and revisit the question after recovery and migration windows.

---

## 📚 Sources

- [1] [Reuters: “Drones hit Yandex data centre in first major attack on Russian data hub” (8 October 2026)](https://www.reuters.com/world/drones-hit-yandex-data-centre-first-major-attack-russian-data-hub-2026-10-08/)
- [2] [Reuters: “Russia's Yandex says it is unclear whether data centre can be restored after drone strike” (8 October 2026)](https://www.reuters.com/world/europe/russias-yandex-says-unclear-whether-data-centre-can-be-restored-after-drone-2026-10-08/)
- [3] [Reuters: “Russia's Yandex says data centre in Vladimir area shut down after drone attack” (11 October 2026)](https://www.reuters.com/world/europe/russias-yandex-says-data-centre-vladimir-area-shut-down-after-drone-attack-2026-10-11/)
- [4] [Cloudflare Radar: “Bot Traffic from Russian Federation”](https://radar.cloudflare.com/bots/ru)
- [5] [Cloudflare Developers: “Cloudflare Radar — Overview”](https://developers.cloudflare.com/radar/)
- [6] [UK Parliament: Christopher Wylie, oral evidence to DCMS Committee (27 March 2018)](https://committees.parliament.uk/oralevidence/7803/html/)
- [7] [UK Parliament: Christopher Wylie, supplementary written evidence](https://www.parliament.uk/documents/commons-committees/culture-media-and-sport/Written-evidence-Chris-Wylie-supplementary.pdf)
- [8] [Information Commissioner's Office: “Investigation into the use of data analytics in political campaigns”](https://ico.org.uk/media2/migrated/2260271/investigation-into-the-use-of-data-analytics-in-political-campaigns-final-20181105.pdf)
- [9] [Information Commissioner's Office: Letter to Julian Knight MP (2 October 2020)](https://ico.org.uk/media2/migrated/2618383/20201002_ico-o-ed-l-rtl-0181_to-julian-knight-mp.pdf)
- [10] [MI5: Director General annual threat update (13 October 2026)](https://www.mi5.gov.uk/mi5-director-general-delivers-annual-threat-update)
- [11] [The Guardian: reporting on Ukrainian data-centre strikes and disinformation claims (13 October 2026)](https://www.theguardian.com/world/2026/oct/13/ukrainian-strikes-russian-datacentres-online-disinformation-bots)
- [12] [The Verge: coverage of Yandex strikes and online disinformation claims (October 2026)](https://www.theverge.com/news/1010424/yandex-drone-strike-outage-disinformation-zelenskyy)

*Source-status note: the original node's Reuters and Cloudflare references are retained. Additional historical and contemporary links were assembled in the preceding research discussion; this drafting pass did not independently re-open and authenticate every linked page. Treat details dependent on [10–12], including the exact scope of monitoring and MI5 wording, as pending primary-text review. Social videos below document circulating claims and reactions, not independently verified causal findings.*

---

## 🌌 Constellations

🪿 🕸️ 🧿 🤖 🕳️ — Embodied Information Ecology; the Observed Information Space; computational dependencies; artificial participation; observable reductions and human feedback.  

*Follow the evidence:*  

- [📹: ThotLine News and Politics: “This has always been the case. What else can be expected from a country run by a KGB agent and his cronies??”](https://vm.tiktok.com/ZN8BX9cP7/) – *personally I’m laughing my bollocks off that it’s this obvious at this point; Слава Україні! Героям слава!*
- [📹: Aaron Parnas, via TikTok: “News: Ukraine And Zelenskyy Confirm Strikes Disrupt Russian Bot Networks - They Will Continue”](https://vm.tiktok.com/ZN8B4Rmy5/)  
- [📹: MeidasTouch, via TikTok: “Zelenskyy: It ‘Suddenly Became A Little Easier To Breathe On Many Social Media Platforms’ After Ukraine Struck Russian Data Centers”](https://vm.tiktok.com/ZN8B4Yr1H/)  
- [📹: Nick Wolny, via TikTok: “How AI Is Changing Bots”](https://vm.tiktok.com/ZN8B42HM6/)
- [📹: The Champagne Socialist, via TikTok: “We’ve actually got some good news for once”](https://vm.tiktok.com/ZN8BbVrCy/)
- [📹: CJ Trowbridge, via TikTok: “It’s got to be tough to be an oligarch today”](https://vm.tiktok.com/ZN8Bb4Ywk/)
- [📹: Tessa, via TikTok: “Na das ist ja interessant :) ”](https://vm.tiktok.com/ZN8BbG9fy/)
- [📹: Captain Kev, via TikTok: “It’s almost like all the right wing pays Russian bots to spread propaganda!”](https://vm.tiktok.com/ZN8BbKJj3/)
- [📹: Виталий Дан, via TikTok: “Украина уничтожила Яндекс”](https://vm.tiktok.com/ZN8BbgvWb/)
- [📹: Jordan the Grey, via TikTok: “Now the Russian bot farms have been taken out, let’s do a little test…”](https://vm.tiktok.com/ZN8BbnRKM/) – *comment section is lit*
- [📹: Indy100, via TikTok: “Zelensky hailed 'genius’ for taking out Russian 'bot farms' weeks before midterm elections”](https://vm.tiktok.com/ZN8Bb7N4A/)
- [📹: Jeawok Media, via TikTok: “Do you think what we see online from the modern right wing is shaped by bots?”](https://vm.tiktok.com/ZN8Bb7WCw/)
- [📹: BootyWiz, via TikTok: “The Internet has been such a much more pleasant place since the bot farm data center got taken down in Russia by Ukraine.”](https://vm.tiktok.com/ZN8BgNwt6/)
- [📹: Trk ikiguy: “после внезапного отключения катацентров Яндекса ультраправая немецкая партия (AfD), резко потеряла поддержку в соцсетях.”](https://vm.tiktok.com/ZN8Bg6nKq/)
- [📹: mr.Black, via TikTok](https://vm.tiktok.com/ZN8BgrBSX/)
- [📹: Michael Adam, via TikTok: “поэтому не обращайте внимания. продолжайте хуярить Россию.”](https://vm.tiktok.com/ZN8BgUN7h/) – *Слава Україні ✌️*
- [📹: Bogdan NL, via TikTok](https://vm.tiktok.com/ZN8BgQFMT/)
- [📹: Danny, via TikTok: “the world is so much more peaceful rn”](https://vm.tiktok.com/ZN8Bg7rFW/) – *”Could mean nothing, though 🤷‍♀️”*
- [📹: Disco Barrington, via TikTok: “Down with the bots!”](https://vm.tiktok.com/ZN8BgK86K/)
- [📹: NM Media Report, via TikTok: “Российские боты исчезли после прилета по «Яндексу»”](https://vm.tiktok.com/ZN8Bg3oMC/)  
- [📹: Auntie Em, via TikTok: “If anyone is wondering why the Reform supporters are suddenly so quiet…”](https://vm.tiktok.com/ZN8BgsPCC/)
- [📹: BBC Verify: “Claims that Ukrainian strikes on Russian data centres reduced Kremlin-linked bot networks have spread widely online - but experts have told BBC Verify there is no evidence the attacks have significantly reduced them.”](https://vm.tiktok.com/ZN8B3kBLj/) – *the sources are a really interesting example of how many things can be true at once*   

*If Mamdani is our mayor, Zelenskyy is my president.*  

---

## ✨ Stardust

ukraine, yandex, data centres, runet, livejournal, russian internet, bot traffic, web crawlers, scraping, audience modelling, cambridge analytica, christopher wylie, lukoil, behavioural profiling, distributed systems, partial failure, shared dependencies, targeting fidelity, coordinated inauthentic behaviour, algorithmic recommendation, differential exposure, intersectionality, racialised misogyny, online harassment, institutional data governance, information warfare, observed information space, embodied information ecology, cybernetics, longitudinal journalism

---

## 🏮 Footer

*Bombing the Bot Farms* is a living node of the **Polaris Protocol**. It investigates what physical disruption of computational infrastructure might reveal about distributed information operations, mediated exposure, and unequal embodied consequences, without treating plausible mechanisms as demonstrated attribution.

> 📡 Cross-references:
>
> - [🕸️🧿 The Observed Information Space](./) — *immediate conceptual home*.
> - [🪿 Embodied Information Ecology](../) — *material and social dependencies*.
>
> 🏮 Return To:
>
> - [🕸️🧿 The Observed Information Space](./) — *1up*.
> - [🪿 Embodied Information Ecology](../) — *2up*.
> - [🌑 Origin Points](../../) — *3up*.
> - [🌌 Polaris Protocol — Root](../../../README.md) — *root*.

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-10-13_
