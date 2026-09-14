# 📚 Sources And Evidence Register
**First created:** 2026-08-16 | **Last updated:** 2026-09-14  
*A consolidated provenance register for the sources carried through the Data Wars: IRGC Edition pack, its incident timeline, analytical nodes, and September 2026 update cycle.*

---

## 🛰️ Orientation

This node consolidates the recoverable public sources used, considered, carried forward, or flagged during development of the *🇮🇷 Data Wars: IRGC Edition* pack.

It draws from:

- the live analytical nodes;
- the human-readable timeline;
- the canonical CSV and aligned XLSX;
- the working README;
- `notes_to_add.txt`;
- the September update cycle;
- and primary or institutional sources used to tighten individual propositions.

This is not a declaration that every linked proposition has been independently verified.

It is a record of the source environment through which the pack was assembled.

The governing distinction is:

```text
source preserved
≠
source endorsed

source reports a claim
≠
source proves the claim

several links
≠
several independent evidentiary routes
```

The register should therefore be read proposition by proposition.

A source may be strong for:

- occurrence;
- timing;
- effect;
- attribution;
- relationship;
- or policy position

while being weak or silent on another part of the same incident.

---

## 🧭 How To Read This Register

Sources are grouped by the function they perform rather than ranked solely by outlet prestige.

### Primary Or Institutional Source

An affected authority, government department, regulator, law-enforcement body, technical advisory issuer, company, operator, or research body speaking from its own institutional position.

Primary does not mean complete, neutral, or independently demonstrated.

### Technical Or Sector Source

A security researcher, sector publication, specialist newsroom, industry body, or technical synthesis capable of supplying detail not present in general reporting.

### Independent Reporting

A newsroom reporting events, official assessments, interviews, leaks, claims, political statements, or downstream effects.

Its independence must be assessed proposition by proposition.

Several articles may still rely on one official, memo, advisory, vendor, Telegram post, or unnamed intelligence source.

### Actor Or Claim Route

A source that preserves what an actor said or claimed.

It establishes the existence and wording of the claim where the reporting route is reliable.

It does not independently establish:

- authorship;
- effect;
- customer;
- state direction;
- or causation.

### Context Source

Polling, policy, war-map, legal, economic, political, alliance, regulatory, or public-confidence evidence used to interpret consequences rather than prove a cyber incident.

### Lead Or Supporting Reference

A source retained because it may support later research, comparison, correction, or exclusion.

It should not be promoted silently into a stronger evidentiary role.

---

## 🎚️ Source-Tier Rule

For incident-level work, use:

```text
TIER 1:
primary / institutional / affected authority

TIER 2:
high-quality independent reporting with direct sourcing

TIER 3:
technical / sector synthesis with identifiable evidence basis

TIER 4:
actor claim / social post / unattributed leak / weak secondary route
```

Tier is not a substitute for proposition fit.

A Tier 1 source can still be weak for attribution if it only confirms service restoration.

A Tier 2 source can be stronger for political positioning if it contains the direct presidential statement.

The register should therefore preserve both:

```text
SOURCE QUALITY
```

and:

```text
PROPOSITION FIT
```

---

## 🧾 Evidence Register Template

For future additions, record:

```text
SOURCE:
SOURCE TYPE:
DATE:
SECTOR / CLUSTER:

PROPOSITION SUPPORTED:
PROPOSITION NOT SUPPORTED:

PRIMARY / SECONDARY:
INDEPENDENT OF OTHER SOURCES:
KNOWN SHARED SOURCE:
ACTOR CLAIM PRESENT:

INCIDENT STATUS:
EFFECT STATUS:
ATTRIBUTION STATUS:
RELATIONSHIP STATUS:

NEGATIVE FINDINGS:
RIVAL EXPLANATIONS:
CORRECTIONS / RETRACTIONS:

USED IN:
LAST REVIEWED:
```

This keeps the register auditable.

---

# 🚰 Water, Wastewater And Operational Technology

## United States Government And Technical Advisories

- [FBI: “Malicious Cyber Actors Targeting Water and Wastewater Sector Internet-Facing Programmable Logic Controllers Causing Operational Disruptions”](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions) — *multi-state incident reporting, access behaviour, configuration changes, monitoring/control loss and operational disruption. Strong for incident class and effect. Does not by itself establish one common operator or sponsor across every affected site.*

- [CISA: “Iranian-Affiliated Actors Exploiting Programmable Logic Controllers Across United States Critical Infrastructure”](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a) — *Iranian-affiliated threat context and relevant PLC tradecraft. Strong for actor-capability context; should not be used as automatic attribution for every July incident.*

- [CISA, FBI, EPA and partners: updated warning on Iran-affiliated threat actors targeting water and wastewater](https://www.cisa.gov/news-events/news/cisa-fbi-epa-and-us-government-partners-update-warning-iran-affiliated-threat-actors-targeting) — *government warning and sector-risk context.*

- [EPA, FBI, CISA and NSA: joint cybersecurity advisory concerning Iranian-affiliated activity against water systems](https://www.epa.gov/newsreleases/epa-fbi-cisa-nsa-issue-joint-cybersecurity-advisory-water-system-regarding-iranian) — *official water-sector warning and Iranian-affiliated framing.*

- [CISA and partners: “IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including U.S. Water and Wastewater Systems Facilities”](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a) — *prior United States government description of the CyberAv3ngers–IRGC relationship. Historical relationship evidence; not automatic proof of the 2026 campaign.*

- [CISA: Iran Advanced Persistent Threat reference page](https://www.cisa.gov/topics/cyber-threats-and-advisories/advanced-persistent-threats/iran) — *background threat reference.*

- [CISA, NSA and partners: “Guide to Securing Remote Access Software”](https://www.cisa.gov/sites/default/files/2023-06/guide_to_securing_remote_access_software_final_508c_v3.pdf) — *remote-access and defensive-method background.*

- [Rewards for Justice: “CyberAv3ngers”](https://rewardsforjustice.net/rewards/cyberav3ngers) — *United States government actor and reward framing.*

- [U.S. Treasury: sanctions for malicious cyber activity against critical infrastructure](https://home.treasury.gov/news/press-releases/jy2072) — *formal government relationship and sanctions evidence.*

- [CISA: “Defending Against an Active Threat to Siemens S7 Series PLCs”](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a) — *active threat to Siemens S7 PLCs across critical infrastructure; read/write capability, disruption and safety-risk framing. Strong for technology-level exposure. Does not publicly attribute the active threat to Iran and should not be used to complete attribution of the recent water incidents.*

## 100+ Water-System Scale

- [SecurityWeek: “CISA: Over 100 Internet-Exposed Water Systems Targeted in July Cyberattacks”](https://www.securityweek.com/cisa-over-100-internet-exposed-water-systems-targeted-in-july-cyberattacks/) — *reports CISA's late-August quantification of more than 100 internet-exposed water and wastewater systems targeted in July. Strong for scale; not by itself evidence of one operator or one sponsor.*

- [TechCrunch: “CISA confirms hackers targeted over 100 US water systems during July”](https://techcrunch.com/2026/08/26/cisa-confirms-hackers-targeted-over-100-us-water-systems-during-july/) — *independent reporting on the same CISA disclosure. Useful corroboration of scale, but not independent forensic evidence beyond the CISA source.*

## Affected States And Authorities

- [Michigan Department of Environment, Great Lakes and Energy: drinking-water cybersecurity](https://www.michigan.gov/egle/about/organization/drinking-water-and-environmental-health/drinking-water/cybersecurity) — *state guidance and Michigan incident context.*

- [Reuters: “Minnesota IT officials disclose coordinated cyberattack at more than 30 local water systems”](https://www.reuters.com/legal/litigation/minnesota-it-officials-disclose-coordinated-cyberattack-more-than-30-local-water-2026-07-28/) — *state-level incident disclosure reported independently. Strong for Minnesota scope and public official position.*

- [Associated Press: “FBI investigates as Michigan joins Minnesota in reporting cyberattacks on water systems”](https://apnews.com/article/77d52a1d7356e608500a1ddb0ec373a6) — *Michigan effects, safety findings and open attribution.*

- [CT Insider: Connecticut water-system preparedness reporting](https://www.ctinsider.com/connecticut/article/connecticut-water-systems-cyberattack-controller-22374980.php) — *preparedness disclosure, mitigation distribution and the state's lack of a central component-level PLC inventory. Context evidence rather than a Connecticut attack record.*

## Intelligence, Attribution And Claim Routes

- [Washington Post: “U.S. spy agencies suspect Iran launched cyberattack on Minnesota water facilities”](https://www.washingtonpost.com/national-security/2026/07/30/us-spy-agencies-suspect-iran-launched-cyberattack-minnesota-water-facilities) — *reported intelligence assessment. Not formal public agency attribution.*

- [KSTP: APT IRAN and CyberAv3ngers claim responsibility for Minnesota](https://kstp.com/kstp-news/top-news/hacking-group-linked-to-iran-claims-responsibility-for-cyberattack-on-minnesota-water-systems-report-says/) — *actor claim and official awareness without public validation.*

- [McCrary Institute Threat Beat: “Cyber Briefing, 12 August 2026”](https://www.linkedin.com/pulse/cyber-briefing-81226-au-mccrary-institute-7cfre) — *academic threat-briefing route for the reported Telegram claim.*

- [Tenable: “Coordinated Cyberattack on Minnesota Water Utilities: What You Need to Know”](https://www.tenable.com/blog/coordinated-cyberattack-on-minnesota-water-utilities-what-you-need-to-know) — *technical-research assessment and CyberAv3ngers hypothesis.*

- [Reuters: “Trump says Iran not to blame for Minnesota cyber attack”](https://www.reuters.com/world/us/trump-says-iran-not-blame-minnesota-cyber-attack-2026-07-31/) — *presidential rejection of Iran attribution and absence of a publicly supplied alternative actor. Strong for executive position, not technical attribution.*

## Independent Expansion Reporting

- [CBS News: at least 12 states report attacks on water systems](https://www.cbsnews.com/news/more-states-water-systems-cyberattacks-iran-backed-hackers) — *campaign-footprint reporting.*

- [Reuters: increased targeting of United States water utilities](https://www.reuters.com/world/us-cyber-defense-agency-warns-increased-hacker-targeting-water-utilities-2026-07-30/) — *federal warning, incident expansion and attribution status.*

- [Axios: water cyberattacks and Iran](https://www.axios.com/2026/08/04/water-cyberattacks-us-iran) — *campaign expansion and Iran-facing interpretation.*

- [Axios: water vulnerabilities and wider infrastructure risk](https://www.axios.com/2026/08/06/us-drinking-water-cyberattacks-climate-change-risks) — *resilience and vulnerability context.*

- [Washington Post: water systems as low-hanging cyber targets](https://www.washingtonpost.com/national-security/2026/08/10/us-water-systems-are-low-hanging-fruit-cyberattacks-experts-warn-after-suspected-iranian-hacks) — *sector vulnerability and consequences.*

- [Wall Street Journal: the distant war reaches small-town Minnesota](https://www.wsj.com/politics/national-security/the-cyberattack-that-brought-a-distant-war-to-small-town-minnesota-66451b93) — *local effects and wartime framing.*

- [The Guardian: United States water facilities, malicious actors and contested attribution](https://www.theguardian.com/technology/2026/aug/04/us-cyber-attacks-water-minnesota-iran) — *public explanation and attribution caveats.*

---

# ⚡ Energy, Telecoms And OT Expansion

## UK Generator

- [BBC: “Cyber attack shut down small power plant”](https://www.bbc.co.uk/news/articles/ce9793g34yvo) — *confirms the July incident and four-day shutdown of a small UK generator. Strong for physical effect. Public technical detail and formal attribution remain limited.*

- [The Guardian: “Iran-linked hackers shut down UK power generator for four days”](https://www.theguardian.com/technology/2026/aug/23/iran-linked-hackers-uk-power-generator-cyber-attack) — *reports the Iran-linked assessment and four-day operational effect. Stronger for attribution context than formal state attribution; still not a named NCSC attribution.*

- [NCSC: “UK organisations urged to bolster cyber resilience amid Iran conflict”](https://www.ncsc.gov.uk/news/uk-organisations-urged-bolster-cyber-resilience-amid-iran-conflict) — *official UK threat-posture and resilience context. Does not by itself attribute the generator incident.*

## Energy / Telecom Expansion And AI

- [Reuters: “Energy firms face AI-enhanced cyber attacks in connectivity push”](https://www.reuters.com/business/energy/energy-firms-face-ai-enhanced-cyber-attacks-connectivity-push--reeii-2026-09-01/) — *AI-assisted OT exploitation, energy-sector targeting and attack-scale context. Strong for search-and-scale and lower-cost exploitation; does not prove a new physical outage tied to the AI tooling.*

- [Reuters reporting, early September 2026, on increased Iranian government-linked attempts against electricity, telecoms and other critical infrastructure] — *campaign-level widening. Preserve as campaign-context evidence; incident-level attribution still requires separate source support.*

## Telecom Narrative Ride-Along

- [AT&T incident reporting concerning the 7 September Texas outage] — *AT&T attributed the outage to attempted physical cable theft and rejected the cyberattack explanation. Use as the primary causation position.*

- [APT IRAN claim route concerning the AT&T outage and unnamed water utility] — *actor claim only. Strong for narrative behaviour, not causation.*

The supported proposition is:

```text
REAL AT&T OUTAGE:
YES

APT IRAN CLAIM:
YES

AT&T CYBER CAUSATION:
REJECTED

IRAN CAUSATION:
NOT ESTABLISHED
```

---

# 🏥 Healthcare And Medical Systems

## Stryker And Handala

- [Reuters: suspected Iran-linked attack disrupts Stryker](https://www.reuters.com/technology/stryker-shares-fall-after-report-suspected-iran-linked-cyberattack-2026-03-11) — *operational effects, actor linkage and company response.*

- [Reuters: Iran-linked hackers restore website after United States domain seizure](https://www.reuters.com/technology/iran-linked-hackers-restore-website-after-us-seizes-domains-2026-03-20) — *law-enforcement action and strengthened Handala linkage without collapsing affiliation into state direction.*

## AnMed And The Gentlemen

- [The Record: AnMed Facebook takeover and ransom demands](https://therecord.media/ransomware-group-hijacks-hospital-facebook-amid-cyberattack-response) — *criminal attribution development, attacker-controlled social-media access and limits on data-theft claims.*

- [Healthcare Dive: AnMed facilities remain closed after the cyberattack](https://www.healthcaredive.com/news/anmed-facilities-remain-closed-week-after-cyberattack/827160) — *healthcare-service continuity and recovery.*

- [HIPAA Journal: AnMed closes facilities while responding to the attack](https://www.hipaajournal.com/anmed-closes-almost-80-facilities-while-it-grapples-with-cyberattack) — *health-sector operational reporting.*

- [WYFF4: AnMed response to unauthorised ransom posts](https://www.wyff4.com/article/anmed-response-cyberattack-facebook-post-hackers/73406207) — *affected-operator response carried through local reporting.*

## Health Sciences Centre Winnipeg And CancerCare Manitoba

- [Shared Health: “Ransomware incident update”](https://sharedhealthmb.ca/news-releases/2026-08-14-ransomware-incident-update/) — *primary affected-authority account: central HVAC-monitoring effects, local monitoring, access-card limitations, additional security, continued clinical care and initial data-access finding.*

- [CityNews Winnipeg / Canadian Press: recovery position one week after discovery](https://winnipeg.citynews.ca/2026/08/17/health-sciences-centre-winnipeg-ransomware-attack-update/) — *17 August recovery-status reporting substantially derived from Shared Health; useful for persistence and public communication, not independent forensic evidence.*

Supported:

```text
RANSOMWARE:
YES

FACILITY-MAINTENANCE EFFECT:
YES

CENTRAL HVAC MONITORING EFFECT:
YES

CLINICAL SERVICE DISRUPTION:
NOT ESTABLISHED

IRAN CONNECTION:
NO EVIDENCE FOUND
```

## Luminis Health

- [Luminis Health public cyber incident communications] — *primary route for system unavailability, patient-facing disruption and recovery communications.*

- [regional / healthcare reporting on 3 September ambulance diversion and treatment delays] — *operational healthcare effect.*

Supported:

```text
CYBER INCIDENT:
YES

AMBULANCE DIVERSION:
YES

TREATMENT DELAY / CANCELLATION:
YES

ACTOR:
OPEN

IRAN CONNECTION:
NO EVIDENCE FOUND
```

## Nutex Health

- [Nutex Health SEC cybersecurity disclosure, 31 August 2026] — *material cyber disclosure; confirms exfiltration of patient, employee, provider, business and financial information. Company did not identify material hospital-operational disruption.*

- [ransomware reporting concerning The Gentlemen claim] — *actor claim / attribution context; claimed scale should remain separate from the company's confirmed disclosure.*

## Veradigm

- [Veradigm incident disclosure, September 2026] — *third-party vendor credential used for customer-service API access and patient-data download; API restricted. Strong for access path and data effect.*

- [The Gentlemen claim concerning approximately 3.5 million patients] — *actor-derived scale claim; should remain unverified unless independently confirmed.*

Supported:

```text
THIRD-PARTY CREDENTIAL:
YES

AUTHORISED API USED FOR UNAUTHORISED EXTRACTION:
YES

PATIENT DATA:
YES

CLINICAL DISRUPTION:
NOT REPORTED

IRAN CONNECTION:
NO EVIDENCE FOUND
```

---

# 🏛️ Government, Public Safety, Courts And Administration

## Suisun City

- [Suisun City: cybersecurity incident updates](https://www.suisun.com/Community/20260807Cybersecurity-Incident-Updates) — *affected-authority account of network shutdown, emergency declaration, service effects and dispatch fallback.*

- [San Francisco Chronicle: initial attack and emergency declaration](https://www.sfchronicle.com/bayarea/article/cyberattack-suisun-city-22380837.php) — *local reporting on public-safety effects.*

- [San Francisco Chronicle: city council considers perpetrator demand](https://www.sfchronicle.com/bayarea/article/suisun-city-cyberattack-demand-22384401.php) — *extortion development and continuing service effects.*

## Darlington County

- [WMBF: cybersecurity incident limits Darlington County services](https://www.wmbfnews.com/2026/08/12/cybersecurity-incident-limits-some-services-darlington-county) — *service limitations and preserved emergency communications.*

- [WPDE: Darlington County investigation and affected services](https://wpde.com/news/local/darlington-co-investigating-cybersecurity-incident-affecting-some-services-county-computer-systems-darlington-county-administrator-marion-charles-stewart-iii-911-communications-center) — *local reporting and official statement route.*

## Berlin

- [Berlin state-government cyber incident reporting, September 2026] — *enterprise IT compromise, departmental disconnection, service degradation, exfiltration and later publication.*

- [BSI / German official reporting concerning criminal rather than political attribution] — *supports a cybercriminal explanation rather than a state-political one.*

Supported:

```text
STATE-GOVERNMENT IT COMPROMISE:
YES

HOUSING-BENEFIT APPLICATION / PAYMENT EFFECT:
YES

DATA PUBLICATION:
YES

CREDENTIAL PUBLICATION:
YES

STATE-POLITICAL LINK:
NOT ESTABLISHED
```

## C-Track / Thomson Reuters

- [Thomson Reuters C-Track incident disclosure, 2–3 September 2026] — *primary route confirming unauthorised access to C-Track files across multiple US states, the US Virgin Islands and Ontario.*

- [jurisdictional notifications concerning affected court files] — *use for local scope and timing.*

Supported:

```text
COURT-SERVICE DISRUPTION:
NOT REPORTED

UNAUTHORISED FILE ACCESS:
YES

SENSITIVE / SEALED / RESTRICTED MATERIAL POSSIBLE:
YES, DEPENDING ON FILE

ACTOR:
OPEN

IRAN CONNECTION:
NO EVIDENCE FOUND
```

---

# 🤖 Shared Software, Access Manufacturing And Supply Chain

## PaperCut

- [GreyNoise: September 2026 PaperCut NG/MF campaign disclosure] — *primary technical source for the AI-assisted mass-exploitation campaign, victim population, credential acquisition, OS/domain secrets and privileged-access findings.*

Supported propositions:

```text
CAMPAIGN START:
31 AUGUST 2026

HUNDREDS OF SERVERS / ORGANISATIONS:
YES

AI-ASSISTED / AGENTIC EXPLOITATION:
YES, PER GREYNOISE

CREDENTIALS / DOMAIN SECRETS:
YES

DOMAIN-ADMIN ACCESS IN SOME CASES:
YES

LIKELY RUSSIAN-SPEAKING OPERATOR:
REPORTED

IRAN CONNECTION:
NO EVIDENCE FOUND

LATER STATE CUSTOMER:
NOT ESTABLISHED
```

The campaign is strong evidence for:

- access manufacturing;
- shared-software concentration;
- and the distinction between initial opportunistic access and later selective use.

It is not evidence that all affected organisations were strategically selected.

Any exact speed claims such as:

- empty workspace to RCE under four hours;
- domain admin in around two hours;
- 11 organisations in 26 seconds;
- or one school to domain admin in seven minutes

should be retained only if directly traceable to the GreyNoise source before formal publication.

## Micro-Comm

- [Micro-Comm / incident reporting concerning the July 31 breach] — *supplier compromise affecting a water/SCADA vendor.*

- [Barracuda ransomware publication route] — *actor-side publication and claimed data volume.*

- [FBI reporting described in follow-up coverage] — *supports an opportunistic / unrelated assessment rather than an Iran link.*

Supported:

```text
SUPPLIER BREACH:
YES

DOWNSTREAM WATER-UTILITY OPERATIONAL COMPROMISE:
NOT ESTABLISHED

CREDENTIAL / REMOTE-ACCESS THEFT:
COMPANY SAID NOT IDENTIFIED

IRAN CONNECTION:
NO EVIDENCE FOUND
```

Use as architecture / supply-chain evidence.

Not as a port or direct utility attack.

## Cl0p / Windchill / FlexPLM

- [Reuters: “Philips, Shell targeted by hacking group”](https://www.reuters.com/legal/government/philips-shell-targeted-by-hacking-group-2026-08-13/) — *mass data-extortion claim across nearly fifty organisations.*

- [PTC: Windchill and FlexPLM vulnerability advisory](https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability) — *shared-product vulnerability route.*

Supported mechanism:

```text
SHARED ENTERPRISE SOFTWARE
→ SCALABLE EXPLOITATION
→ BROAD VICTIM POOL
```

Not supported:

```text
ONE STATE SPONSOR
→ STRATEGIC SELECTION OF EVERY VICTIM
```

---

# 🇨🇳 China-Linked Contractor / Hacker-For-Hire Ecosystem

## QScan / QTRouter

- [U.S. Department of Justice / FBI disruption materials concerning QScan and QTRouter] — *primary route for the China-linked hacker-for-hire / contractor ecosystem, customer structure and infrastructure disruption.*

- [independent reporting on government, energy, power, telecom and hospital targeting] — *sector distribution and customer-context corroboration.*

Supported:

```text
HACKER-FOR-HIRE / CONTRACTOR MODEL:
YES

STATE-LINKED CHINESE CUSTOMER CONTEXT:
YES

OVERLAP WITH ENERGY / TELECOM / HEALTH:
YES

IRAN CONNECTION:
NO

COMMON TARGET CLASS AS IRAN-SPECIFIC SIGNAL:
WEAKENED
```

This ecosystem is important because it demonstrates that several state-linked architectures can target the same critical sectors simultaneously.

---

# ⚓ Iran-Nexus Naval Reconnaissance And AI Use

## Anthropic Disclosure

- [Anthropic: September 2026 disclosure concerning Iran-nexus use of Claude] — *primary source for Dec 2025–Aug 2026 actor use of Claude for naval tracking, ship and aircraft movement, personnel, maritime VSAT, Cisco communications equipment and ICS-product research.*

Supported:

```text
IRAN-NEXUS ACTOR:
YES, PER ANTHROPIC

US NAVAL / MARITIME RECONNAISSANCE:
YES

VSAT / CISCO / ICS RESEARCH:
YES

SUCCESSFUL EXPLOITATION:
NOT ESTABLISHED

PHYSICAL / OPERATIONAL DISRUPTION:
NOT ESTABLISHED

DIRECT IRGC TASKING:
NOT ESTABLISHED
```

Use as:

- reconnaissance;
- capability development;
- technical target-mapping;
- and AI-use evidence.

Do not upgrade CVE research into exploitation.

---

# ✈️ Transport, Ports And Logistics

## CEVA Logistics

- [TechCrunch: “A data breach at shipping giant CEVA Logistics is rippling across banks, retailers, Steam gamers and beyond”](https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/) — *warehouse disruption and customer-data effects.*

- [FreightWaves: cyberattack on CEVA Logistics warehouses in Europe](https://www.freightwaves.com/news/cyberattack-on-ceva-logistics-warehouses-in-europe-impacts-retailers) — *shipment-delay and warehouse-operation context.*

- [SecurityWeek: CEVA Logistics operations disrupted by cyberattack](https://www.securityweek.com/ceva-logistics-operations-disrupted-by-cyberattack/) — *sector corroboration.*

Supported:

```text
WAREHOUSE / CONTRACT-LOGISTICS DISRUPTION:
YES

SHIPMENT DELAYS:
YES

SOME CUSTOMER-DATA EXPOSURE:
YES

PORT OT COMPROMISE:
NOT ESTABLISHED

MARITIME CONTROL COMPROMISE:
NOT ESTABLISHED

IRAN CONNECTION:
NO EVIDENCE FOUND
```

## North Carolina Ports

- [North Carolina Ports incident communications and local reporting] — *direct port IT compromise, operational logistics effect and manual fallback.*

Supported:

```text
DIRECT PORT IT COMPROMISE:
YES

OPERATIONAL LOGISTICS EFFECT:
YES

MANUAL FALLBACK:
YES

VESSEL ACTIVITY DISRUPTION:
NOT ESTABLISHED

PORT OT COMPROMISE:
NOT ESTABLISHED

IRAN CONNECTION:
NO EVIDENCE FOUND
```

Use as a direct port-operational comparator.

---

# 🏦 Finance, Payments And Economic Transmission

## Fiserv / Cl0p Boundary

- [Reuters: Cl0p mass-extortion campaign](https://www.reuters.com/legal/government/philips-shell-targeted-by-hacking-group-2026-08-13/) — *actor claim involving Fiserv among many companies.*

- [Fiserv public response / investigation statements] — *company position that customer, banking, transaction, personal and operational data were not demonstrated compromised.*

Supported:

```text
ACTOR CLAIM:
YES

CONFIRMED PAYMENT-SYSTEM DISRUPTION:
NO

CLEARING / SETTLEMENT EFFECT:
NO

IRAN CONNECTION:
NO
```

Use as a boundary case showing:

```text
FINANCIAL-SECTOR COMPANY NAMED
≠
FINANCIAL INFRASTRUCTURE IMPAIRED
```

## Economic / Energy Context

- [Reuters: “Iran defiant on strait as Trump tells Americans to accept high gasoline prices”](https://www.reuters.com/world/us/trump-urges-americans-accept-higher-gas-prices-he-escalates-iran-rhetoric-2026-08-14/) — *household-price and political context.*

Use as a context source for financial and public effects.

Not as cyber incident evidence.

---

# 🇬🇧 United Kingdom Threat Posture And Alliance Context

- [NCSC: advice following Middle East escalation](https://www.ncsc.gov.uk/news/ncsc-advises-uk-organisations-take-action-following-conflict-in-middle-east) — *official UK threat-posture assessment.*

- [NCSC: hostile states linked to three-quarters of managed critical-infrastructure incidents](https://www.ncsc.gov.uk/news/ncsc-ceo-hostile-states-linked-to-three-quarters-of-cyber-attacks) — *aggregate threat-environment marker; not evidence of Iran's share.*

- [BBC: UK generator incident](https://www.bbc.co.uk/news/articles/ce9793g34yvo) — *physical energy effect.*

- [The Guardian: Iran-linked UK generator reporting](https://www.theguardian.com/technology/2026/aug/23/iran-linked-hackers-uk-power-generator-cyber-attack) — *attribution context.*

Use these together to separate:

```text
UK THREAT POSTURE
```

from:

```text
INCIDENT-SPECIFIC ATTRIBUTION
```

and:

```text
FORMAL PUBLIC STATE ATTRIBUTION
```

---

# 🇺🇸 White House, Cyber Governance And Regulation

## President Trump's Cyber Strategy

- [White House: “President Trump's Cyber Strategy for America”](https://www.whitehouse.gov/wp-content/uploads/2026/03/president-trumps-cyber-strategy-for-america.pdf) — *primary policy source. Supports critical-infrastructure hardening, denial of adversary initial access, offensive and defensive cyber capability, public-private coordination and “Promote Common Sense Regulation”.*

- [White House: “White House Unveils President Trump's Cyber Strategy for America”](https://www.whitehouse.gov/releases/2026/03/white-house-unveils-president-trumps-cyber-strategy-for-america/) — *White House summary and political framing.*

Supported:

```text
ADMINISTRATION HAS FORMAL CYBER STRATEGY:
YES

CRITICAL-INFRASTRUCTURE HARDENING:
YES

OFFENSIVE + DEFENSIVE CYBER EMPHASIS:
YES

REGULATORY STREAMLINING:
YES
```

Not supported:

```text
ADMINISTRATION OPPOSES ALL CYBER REGULATION:
NO

ADMINISTRATION HAS NO CYBER CONCERN:
NO
```

## Gold Eagle

- [White House: “White House Launches Gold Eagle Initiative for Unprecedented Cybersecurity Vulnerability Coordination”](https://www.whitehouse.gov/releases/2026/07/white-house-launches-gold-eagle-initiative-for-unprecedented-cybersecurity-vulnerability-coordination/) — *primary source for government-industry vulnerability coordination.*

Use as evidence that the administration's preferred model includes:

```text
FASTER COORDINATION
+
VULNERABILITY INFORMATION
+
PUBLIC-PRIVATE RESPONSE
```

rather than a simple absence of cyber policy.

## GAO Regulatory Context

- [U.S. GAO: “Cybersecurity Regulations: Multiple Sectors Are Subject to Potentially Duplicative Reporting Requirements”](https://www.gao.gov/products/gao-26-108606) — *supports the proposition that 117 cybersecurity regulations across 37 agencies included substantial reporting duplication.*

Use to preserve the legitimate case for rationalisation.

Do not use it to prove that mandatory security baselines are unnecessary.

- [U.S. GAO: FCC Congressional Review Act decision concerning cybersecurity interpretation](https://www.gao.gov/products/b-338053) — *legal / regulatory context for the FCC's revised interpretation of telecom cybersecurity obligations.*

Use as:

```text
REGULATORY CHANGE:
YES

SECURITY OUTCOME:
SEPARATE EMPIRICAL QUESTION
```

## Presidential Minnesota Position

- [Reuters: “Trump says Iran not to blame for Minnesota cyber attack”](https://www.reuters.com/world/us/trump-says-iran-not-blame-minnesota-cyber-attack-2026-07-31/) — *primary independent route to presidential position.*

Supported:

```text
TRUMP REJECTED IRAN ATTRIBUTION:
YES

PUBLIC ALTERNATIVE ACTOR PROVIDED:
NO

TECHNICAL BASIS DISCLOSED:
NO
```

Do not infer whether the statement was based on classified intelligence.

That remains open.

---

# 🌍 Alliance, NATO And Policy-Reliability Context

This is a context category.

It does not prove a cyber incident.

It supports analysis of:

- alliance-response coherence;
- transaction cost of leadership;
- burden sharing;
- allied hedging;
- and predictability as stored alliance power.

Sources in this category should be used only where they establish:

- a previously coordinated position;
- a presidential deviation;
- an allied reaction;
- basing or logistics consequence;
- intelligence-sharing effect;
- sanctions divergence;
- or other concrete alliance behaviour.

The governing distinction is:

```text
ALLIED POLICY DIVERGENCE
≠
NATO COLLAPSE

ADVERSARY BENEFIT
≠
ADVERSARY CAUSED THE DIVERGENCE
```

The relevant evidence threshold is therefore behavioural.

Record:

```text
WHAT WAS AGREED?
WHAT CHANGED?
WHO CHANGED IT?
HOW DID ALLIES RESPOND?
WHAT OPERATIONAL OR PLANNING COST FOLLOWED?
```

Do not convert rhetoric alone into an alliance-breakdown finding.

---

# ⚖️ Legal And IHL Sources

## Core IHL Principles

Use primary treaty text, ICRC materials, state positions, official military manuals and criminal-law instruments where possible.

Relevant analytical categories include:

- distinction;
- proportionality;
- precautions;
- civilian objects;
- military objectives;
- medical protection;
- objects indispensable to survival;
- armed-conflict nexus;
- state attribution;
- and individual criminal responsibility.

The governing legal ladder remains:

```text
CYBER INCIDENT
≠
CYBER OPERATION REGULATED BY IHL
≠
CYBERATTACK FOR IHL PURPOSES
≠
IHL VIOLATION
≠
WAR CRIME
```

And:

```text
STATE RESPONSIBILITY
≠
INDIVIDUAL CRIMINAL RESPONSIBILITY
```

For prosecution-level analysis, preserve the International Criminal Court's *Elements of Crimes* as a discipline on material and mental elements.

Do not use journalistic description alone to label a cyber incident a war crime.

---

# 📣 Actor Claims And Narrative Evidence

Actor claims should be retained where they matter.

They should never control the incident record.

Current important claim routes include:

- APT IRAN / CyberAv3ngers claiming Minnesota;
- APT IRAN claiming the AT&T outage;
- ransomware groups claiming healthcare victims;
- Cl0p naming mass-extortion victims;
- Barracuda / ransomware publication of supplier data;
- Gentlemen claims concerning AnMed, Nutex or Veradigm;
- Gorz Rostam DDoS claims.

The governing rule is:

```text
CLAIM EXISTS:
may be established

CLAIM IS TRUE:
requires independent support
```

Use:

```text
ACTOR CLAIM
→ EVIDENCE ITEM
```

not:

```text
ACTOR CLAIM
→ ATTRIBUTION COMPLETE
```

---

# ❌ Negative Findings Register

Negative findings matter because they prevent accidental inflation.

Current important negatives include:

```text
CEVA:
no port OT compromise established
no Iran link established

NORTH CAROLINA PORTS:
no vessel disruption established
no port OT compromise established
no Iran link established

MANITOBA:
clinical care continued in reviewed update
no Iran link established

LUMINIS:
no Iran link established

NUTEX:
no material hospital-operational disruption disclosed
no Iran link established

VERADIGM:
no clinical disruption reported
no Iran link established

C-TRACK:
no court-service shutdown reported
no Iran link established

PAPERCUT:
no Iran link established
later state customer not established

MICRO-COMM:
no downstream utility compromise established
company said credentials / remote access were not identified stolen
no Iran link established

QSCAN / QTROUTER:
separate China-linked ecosystem
not Iran

ANTHROPIC IRAN-NEXUS RECON:
no successful exploitation established
no operational effect established
direct IRGC tasking not established

APT IRAN / AT&T:
cyber causation rejected by AT&T
unnamed water-utility claim unconfirmed

UK GENERATOR:
formal public NCSC attribution not identified
facility's full civilian / dual-use role not public

100+ WATER SYSTEMS:
one common operator not established
one common sponsor not established
```

These negatives should survive every rewrite unless new evidence changes them.

---

# 🔀 Rival-Explanation Register

For recurring incident classes, retain rival explanations explicitly.

## Water / OT

Possible rivals include:

- Iran-linked state or proxy activity;
- copycats;
- criminal access;
- automated scanning;
- other state-linked actors;
- shared vulnerable equipment;
- unrelated technical failure in individual cases.

## Healthcare

Possible rivals include:

- ransomware;
- credential theft;
- third-party compromise;
- ordinary criminal extortion;
- unresolved intrusion.

## Shared Software

Possible rivals include:

- vulnerability-driven mass exploitation;
- access brokerage;
- later selective resale;
- opportunistic criminal use.

## Energy / Telecoms

Possible rivals include:

- cyberattack;
- physical cable theft;
- supplier failure;
- equipment fault;
- unrelated outage.

## Alliance / Governance Effects

Possible rivals include:

- ordinary allied policy disagreement;
- domestic politics;
- legal constraints;
- procurement delay;
- strategic hedging unrelated to cyber.

Rival explanations are not decorative.

They are part of the evidence model.

---

# 🧬 Independence And Duplication

Multiple links may still describe one source.

Common duplication patterns include:

```text
PRIMARY ADVISORY
→ Reuters article
→ AP article
→ technical blog
→ newsletter
```

or:

```text
ACTOR TELEGRAM POST
→ local report
→ national report
→ analyst thread
```

or:

```text
COMPANY DISCLOSURE
→ sector press
→ general press
```

The register should therefore record:

- the earliest identifiable source;
- whether later reporting adds independent evidence;
- whether a quoted official is the same official;
- whether several reports rely on one advisory;
- whether a technical blog adds original telemetry;
- and whether one actor claim is being repeated through several outlets.

Do not count copies as corroboration.

---

# 📌 Proposition-Level Status Rules

Use:

```text
INCIDENT CONFIRMED
≠
ATTRIBUTION CONFIRMED

PATTERN CONFIRMED
≠
ONE COORDINATED CAMPAIGN CONFIRMED

COMMON OPERATOR
≠
COMMON CUSTOMER

CRIMINAL OPERATOR
≠
NO STATE CUSTOMER

CRIMINAL OPERATOR
≠
STATE CUSTOMER

IRAN-LINKED OPERATOR
≠
IRAN DIRECTED THIS OPERATION

STATE BENEFIT
≠
STATE CONTROL

SYSTEM RESTORED
≠
PERSON-CENTRED RECOVERY COMPLETE

CIVILIAN INFRASTRUCTURE AFFECTED
≠
WAR CRIME CONFIRMED

ACTOR CLAIM
≠
CAUSATION

ALLIED POLICY DIVERGENCE
≠
ADVERSARY COMMAND
```

These propositions should remain visible in the register because source drift usually happens when one distinction disappears.

---

# 🧭 Current Evidence Architecture — 14 September 2026

The updated source base supports:

```text
US WATER / OT CAMPAIGN:
🟢 strongly evidenced as a real multi-state operational pattern

100+ WATER-SYSTEM SCALE:
🟢 established through CISA disclosure

IRAN-LINKED CORE ATTRIBUTION:
🟡 probable / strengthened

FORMAL ATTRIBUTION OF EVERY WATER INCIDENT:
⚪ not established

UK CYBER-TO-PHYSICAL ENERGY EFFECT:
🟢 established

IRAN-LINKED UK GENERATOR ASSESSMENT:
🟠 / 🟡 developing

ENERGY / TELECOM TARGETING EXPANSION:
🟡 / 🟢 credibly reported

HEALTHCARE OPERATIONAL EFFECTS:
🟢 established across several separate incidents

SHARED-SOFTWARE ACCESS MANUFACTURING:
🟢 established

CHINA-LINKED CONTRACTOR / HACKER-FOR-HIRE ECOSYSTEM:
🟢 established

IRAN-NEXUS NAVAL / ICS RECONNAISSANCE:
🟢 disclosed

APT IRAN NARRATIVE RIDE-ALONG:
🟢 established as a claim behaviour

ONE COMMON OPERATOR ACROSS DATASET:
⚪ not established

ONE COMMON CUSTOMER:
⚪ not established

ONE COMMON SPONSOR:
⚪ not established

ADMINISTRATION HAS FORMAL CYBER STRATEGY:
🟢 established

REGULATORY STREAMLINING POLICY:
🟢 established

GOVERNANCE CONTRADICTION:
🟡 analytical finding, not source-level fact

ALLIANCE-RELIABILITY COST:
🟡 developing analytical finding requiring behavioural evidence
```

That is the current evidentiary map.

---

## 🌌 Constellations

📚 🔎 🕸️ 🚰 ⚡ 🏥 🤖 🌍 — provenance; source discipline; attribution; water; energy; healthcare; access manufacturing; alliance context.

---

## ✨ Stardust

sources, evidence register, provenance, source tiers, water cyberattacks, operational technology, Iran attribution, UK generator, healthcare ransomware, PaperCut, Micro-Comm, QScan, QTRouter, C-Track, Anthropic, actor claims, negative findings, rival explanations, White House cyber strategy, GAO, alliance reliability

---

## 🏮 Footer

*📚 Sources And Evidence Register* is a living node of the **Polaris Protocol**.  
It records the source environment, proposition-level evidentiary role, negative findings, rival explanations and independence limits used across the *🇮🇷 Data Wars: IRGC Edition* pack.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *incident chronology through 14 September 2026*
> - [🔎 Confidence Labels And Source Rules](./🔎_confidence_labels_and_source_rules.md) — *source and confidence mechanics*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *claim-level language discipline*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *graded attribution and proposition separation*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *ecosystem separation and attribution boundaries*
> - [🌊 Riding Every Wave](./🌊_riding_every_wave.md) — *claims, downstream use and mixed causal relationships*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *technical depth, scale and physical effects*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *legal-evidence ladder*
> - [🍊 Why Is the Orange Being Weird?](./🍊_why_is_the_orange_being_weird.md) — *governance and policy evidence*
>
> 🏮 Return To:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *1up*
> - [🌊 Playing Defence](../README.md) — *2up*
> - [📲 Press Matters](../../README.md) — *3up*
> - [🌓 In The Moment](../../../README.md) — *4up*
> - [🌌 Polaris Protocol — Root](../../../../README.md) — *root*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-09-14_
