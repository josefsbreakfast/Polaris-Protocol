# 🚰 When Cyber Reaches The Machinery
**First created:** 2026-08-01 | **Last updated:** 2026-09-14  
*The threshold changes when a cyber incident begins reaching the systems that monitor, control, or physically alter water, energy, fuel, transport, healthcare-support, or other essential processes.*

---

## 🛰️ Orientation

A stolen database and a manipulated pump are both cyber incidents.

They are not the same kind of incident.

When cyber activity reaches operational technology, industrial control systems, programmable logic controllers, sensors, valves, pumps, substations, treatment equipment, building-management systems, access-control systems, or other physical processes, the consequences can move beyond:

- confidentiality;
- inaccessible files;
- public embarrassment;
- ordinary administrative disruption;
- or temporary website loss.

The attacker may begin moving towards the ability to change what the system does in the physical world.

That changes the risk.

It does not mean every operational-technology incident becomes catastrophic.

It does not mean every intrusion into an OT environment gives the attacker control of machinery.

And it does not mean that access proves destructive intent.

The analytical task is to establish **how far into the machinery the evidence says the attacker actually got**.

The critical questions become:

> Could they see the operational environment?

> Could they interact with it?

> Could they issue commands or alter configuration?

> Did the physical process actually change?

> Did operators have to take control back by hand?

> Did the attacker stop at enterprise IT because segmentation worked?

> Was the first actor only creating access for someone else?

Those are different thresholds.

They should be recorded separately.

---

## 🏭 Information Technology Is Not The Whole System

Most public discussion of cybersecurity focuses on information technology:

- email;
- databases;
- websites;
- identity systems;
- cloud platforms;
- office networks;
- and administrative software.

Operational technology is different.

It includes systems used to monitor or control physical processes:

- programmable logic controllers;
- supervisory control and data acquisition systems;
- human-machine interfaces;
- remote terminal units;
- industrial sensors;
- pumps;
- valves;
- treatment equipment;
- substations;
- generation controls;
- building-management systems;
- physical-access systems;
- and safety controls.

A simplified distinction is:

```text
INFORMATION TECHNOLOGY
→ records
→ communications
→ administration
→ identity
→ data

OPERATIONAL TECHNOLOGY
→ monitoring
→ commands
→ pumps
→ valves
→ pressure
→ treatment
→ generation
→ machinery
→ physical process
```

The distinction matters because compromise of operational technology can create a route from digital access to physical effect.

But the existence of that route does not establish how far along it the attacker travelled.

---

## 🪜 The Depth-Of-Access Ladder

The phrase:

> OT intrusion

can conceal several very different situations.

This pack should therefore record operational access by depth where the evidence allows.

A useful ladder is:

```text
LEVEL 0 — EXTERNAL RECONNAISSANCE
        ↓
LEVEL 1 — IT / ADMINISTRATIVE ACCESS
        ↓
LEVEL 2 — OT NETWORK VISIBILITY
        ↓
LEVEL 3 — HMI / CONTROL INTERFACE ACCESS
        ↓
LEVEL 4 — CONTROLLER OR CONFIGURATION ACCESS
        ↓
LEVEL 5 — COMMAND / SETTING MANIPULATION
        ↓
LEVEL 6 — OBSERVED PHYSICAL-PROCESS CHANGE
        ↓
LEVEL 7 — SAFETY / SERVICE / PHYSICAL HARM
```

These levels should not be inferred upwards.

Evidence that an attacker reached a human-machine interface does not prove that they changed a controller.

Evidence that they changed a controller does not automatically prove that the physical process changed.

Evidence of physical-process change does not automatically establish serious civilian harm.

The rule is:

```text
record the deepest demonstrated level
≠
assume every higher level
```

That makes movement deeper into operational systems visible without converting capability into consequence.

---

## 🧪 Access, Capability, Action And Effect Are Separate Columns

Depth of access is only one axis.

The record must also distinguish what the actor could do from what the actor actually did.

```text
ACCESS
→ what environment or interface was reached?

CAPABILITY
→ what functions did the access technically permit?

ACTION
→ what command, write, configuration change, or manipulation was observed?

PROCESS RESPONSE
→ what did the machinery or controlled process do?

SERVICE EFFECT
→ what changed for the utility, operator, dependent service, or public?

HUMAN CONSEQUENCE
→ who absorbed danger, labour, delay, deprivation, or physical harm?
```

These columns may stop at different points.

For example:

```text
tool supports read and write access
≠
write command observed at this facility

write command observed
≠
physical process changed

physical process changed
≠
civilian harm occurred

service maintained
≠
no operational or human cost
```

Capability evidence is strategically important.

It must not be rewritten as completed action.

Observed action is operationally important.

It must not be inflated into a consequence the evidence does not show.

---

## 👁️ Loss Of View Is Not The Same As Loss Of Control

Operational incidents should distinguish between several different forms of degradation.

An operator may lose:

- visibility;
- remote access;
- trusted telemetry;
- automated control;
- configuration integrity;
- or physical control of the process.

Those are not interchangeable.

For example:

```text
LOSS OF VIEW
→ operators cannot reliably see what the system is doing

LOSS OF REMOTE CONTROL
→ operators cannot safely command the system remotely

LOSS OF TRUST
→ operators can see data but cannot rely on its integrity

ATTACKER CONTROL CAPABILITY
→ attacker can issue or alter operational commands

PHYSICAL MANIPULATION
→ machinery or process actually changes
```

A loss of trusted telemetry can itself be operationally serious.

Operators may have to stop relying on automation because they no longer know whether:

- pressure readings are accurate;
- chemical measurements are genuine;
- alarms are real;
- valves are in the reported position;
- or configuration has been altered.

The physical service may continue while the operator's confidence in the control environment has already been damaged.

---

## 🚰 Water Is The Clearest Warning

Water and wastewater systems are especially important because many are:

- locally operated;
- lightly staffed;
- dependent on older equipment;
- connected through common vendors;
- exposed through remote-access tools;
- and expected to remain available continuously.

A compromised water system may experience:

- altered pressure;
- pump failure;
- lockout;
- flooding;
- treatment disruption;
- sensor uncertainty;
- changed passwords;
- forced shutdown;
- loss of trusted remote control;
- or movement to manual operation.

The absence of contamination does not make the incident trivial.

If operators can no longer trust the digital controls, the system has already been degraded.

Manual operation may preserve service.

It can also show that the normal digital control environment has become unreliable enough that operators no longer consider it safe to use normally.

---

## 🇺🇸 The July–August Water Wave Crossed The Machinery Threshold

The July 2026 U.S. water incidents are no longer describable merely as:

> hackers targeted water utilities.

The joint FBI/EPA alert established several distinct steps along the operational control chain.

Utilities in multiple states reported incidents involving internet-facing programmable logic controllers.

Attackers remotely accessed devices and changed network or controller settings.

That caused loss of monitoring and control functionality.

Across the affected systems, public reporting recorded:

- loss of view;
- loss of function;
- modified PLC project files;
- ladder-logic discrepancies;
- loss of water pressure;
- flooding;
- and movement to manual operation.

That evidence maps onto the depth ladder as follows:

```text
LEVEL 0 — TARGET DISCOVERY
          internet-facing PLCs identified

LEVEL 3 — CONTROL-INTERFACE ACCESS
          remote access to operational devices demonstrated

LEVEL 4 — CONTROLLER / CONFIGURATION ACCESS
          PLC configuration and project-file access demonstrated

LEVEL 5 — COMMAND / SETTING MANIPULATION
          settings, IP addresses and passwords changed;
          ladder-logic discrepancies reported

LEVEL 6 — PHYSICAL-PROCESS CHANGE
          loss of pressure and flooding reported in parts of the wave

LEVEL 7 — SAFETY / SERVICE / PHYSICAL HARM
          operational degradation demonstrated;
          severity varied by controller function and fallback capacity
```

This does **not** mean every affected facility reached Level 6 or Level 7.

The correct unit of analysis remains both:

```text
THE WAVE
→ demonstrated repeated movement into controller configuration
→ included some physical-process effects
```

and:

```text
THE INDIVIDUAL FACILITY
→ deepest demonstrated access
→ exact equipment function
→ exact operational consequence
→ fallback outcome
```

Neither the worst consequence in the wave nor the least affected facility should be projected onto every other victim.

---

## 📈 The Scale Changed — More Than 100 Water Systems

By **26 August**, CISA had publicly quantified the July campaign at **more than 100 internet-exposed water and wastewater systems**.

That changes the machinery problem in an important way.

The earlier picture could still be read as:

```text
several utilities
→ several incidents
→ recurring weak configurations
```

The newer picture is:

```text
100+ internet-exposed water / wastewater systems
→ repeated contact with a common machinery layer
→ repeated opportunity to learn which configurations produce effect
→ repeated opportunity to observe fallback and response
```

This does **not** mean:

```text
100+ systems physically disrupted
```

or:

```text
100+ systems attributed to one operator
```

It means the attack surface itself was being encountered at scale.

That creates a second form of escalation.

The problem is not only:

```text
HOW DEEP DID THE ATTACKER GET?
```

It is also:

```text
HOW MANY MACHINES COULD THE ATTACKER FIND?
```

Those are separate variables.

A campaign can become more dangerous through:

- deeper access;
- wider access;
- more repeatable access;
- faster access;
- or more transferable access.

### Sources

- [SecurityWeek: “CISA: Over 100 Internet-Exposed Water Systems Targeted in July Cyberattacks”](https://www.securityweek.com/cisa-over-100-internet-exposed-water-systems-targeted-in-july-cyberattacks/)
- [TechCrunch: “CISA confirms hackers targeted over 100 US water systems during July”](https://techcrunch.com/2026/08/26/cisa-confirms-hackers-targeted-over-100-us-water-systems-during-july/)

---

## 🧭 Technical Confidence Remains Higher Than Attribution Confidence

The machinery finding and the actor finding are not at the same evidentiary stage.

### 1. Federal Technical Finding — Confirmed

Malicious remote access, configuration changes and operational effects across the multi-state wave are established in the public federal technical record.

### 2. Prior Iran-Linked Threat Pattern — Confirmed Context

US government reporting had already warned that Iranian-affiliated actors were exploiting internet-connected PLCs with the intent to cause disruption.

That is strong evidence of an active and relevant threat pattern.

It is not, by itself, attribution of every later incident using similar equipment.

### 3. Reported Investigative / Intelligence Assessment — Iran Favoured

High-quality reporting described US intelligence and investigative assessments as favouring Iranian responsibility for the Minnesota / core wave.

### 4. Actor Claim — Material Evidence, Not Independent Proof

APT IRAN later claimed the Minnesota operation had been conducted jointly with CyberAv3ngers.

US government reporting had previously described CyberAv3ngers as affiliated with the IRGC Cyber-Electronic Command.

That strengthens the Iran-linked assessment for the Minnesota core wave.

It does not independently prove:

- the claimants performed every intrusion;
- Iranian state direction for every incident;
- one common operator across every affected state;
- or that every superficially similar water incident belongs to the same campaign.

The current analytic separation is:

```text
OT MANIPULATION:
🟢 CONFIRMED

MULTI-STATE OPERATIONAL WAVE:
🟢 CONFIRMED

100+ SYSTEM SCALE:
🟢 CONFIRMED AS A CAMPAIGN-SCALE DISCLOSURE

MINNESOTA / CORE IRAN-LINKED CASE:
🟡 PROBABLE / STRENGTHENED

ACTOR RESPONSIBILITY CLAIM:
📣 CONFIRMED AS A CLAIM

FORMAL ATTRIBUTION OF EVERY INCIDENT:
⚪ NOT ESTABLISHED

COMMON ACTOR FOR EVERY SITE:
⚪ NOT ESTABLISHED
```

This is not timidity.

It is what allows the technical finding to remain firm even if the attribution picture changes.

---

## 🛡️ Siemens Expanded The Machinery Picture Beyond One Water Device Family

The 19 August joint advisory from NSA, CISA, FBI, DOE and EPA expanded the machinery picture.

The agencies warned of an active threat to Siemens S7-series programmable logic controllers across:

- manufacturing;
- energy;
- water and wastewater;
- chemical;
- food and agriculture;
- and other critical sectors.

The advisory described actors:

- scanning for exposed or poorly protected PLCs;
- using AI assistance to develop exploitation scripts;
- using public industrial-automation libraries to obtain read/write access;
- accessing memory, configuration data and ladder logic;
- testing and refining capabilities against particular PLC models;
- and preparing for possible future operational effects.

It also warned that organisations may not realise that third-party service providers or system integrators retain remote access to their PLCs.

The correct reading remains:

```text
ACTIVE THREAT TO SIEMENS S7 PLCs:
🟢 CONFIRMED BY JOINT FEDERAL WARNING

RECONNAISSANCE AND CAPABILITY DEVELOPMENT:
🟢 CONFIRMED AS THE ASSESSED ACTIVITY PATTERN

READ / WRITE TOOL CAPABILITY:
🟢 DESCRIBED

PREPARATION FOR POSSIBLE OPERATIONAL EFFECTS:
🟡 AGENCY ASSESSMENT

WRITE ACTION AT EVERY IDENTIFIED FACILITY:
⚪ NOT ESTABLISHED

PHYSICAL EFFECT AT EVERY TARGET:
⚪ NOT ESTABLISHED

FORMAL IRAN ATTRIBUTION OF THAT ACTIVE THREAT:
⚪ NOT MADE IN THE ADVISORY
```

This is exactly why capability, action, effect and attribution require separate columns.

The threat moved deeper.

The public evidence did not move every incident to the same depth.

### Sources

- [CISA: “Defending Against an Active Threat to Siemens S7 Series PLCs”](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a)
- [Reuters: “US warns Siemens devices can be hacked amid fears Iran is breaching water plants”](https://www.reuters.com/world/us-warns-siemens-devices-can-be-hacked-amid-fears-iran-is-breaching-water-plants-2026-08-19/)

---

## ⚡ The UK Generator Incident Crossed The Physical-Effect Threshold

The most important post-20-August machinery development outside the US water sector is the UK power-generator incident.

On **23 August**, British reporting disclosed that a cyberattack had forced a small-scale power generator offline for **four days in July**.

The facility was not publicly identified.

Officials said the site was too small to threaten the wider electricity system.

That still represents a real cyber-to-physical outcome.

The relevant ladder is:

```text
LEVEL 1 — ENTERPRISE / ADMINISTRATIVE ACCESS
          precise public path not established

LEVEL 2–5 — OT / CONTROL DEPTH
            public technical details remain limited

LEVEL 6 — PHYSICAL-PROCESS CHANGE
          electricity generation stopped

LEVEL 7 — SERVICE / PHYSICAL EFFECT
          facility offline for four days;
          no national-grid disruption reported
```

The key evidentiary point is unusual:

```text
PHYSICAL EFFECT:
🟢 ESTABLISHED

PRECISE PUBLIC TECHNICAL PATH:
⚪ LIMITED / NOT PUBLIC

FORMAL PUBLIC NCSC ATTRIBUTION:
⚪ NOT IDENTIFIED

IRAN-LINKED ASSESSMENT:
🟠 / 🟡 DEVELOPING
```

This is a useful reminder that depth evidence can sometimes be asymmetric.

We may know that the machinery stopped without knowing every technical step used to make it stop.

The absence of a public ladder trace does not erase the observed physical outcome.

It means the intermediate rungs remain less well evidenced.

### Sources

- [BBC: “Cyber attack shut down small power plant”](https://www.bbc.co.uk/news/articles/ce9793g34yvo)
- [The Guardian: “Iran-linked hackers shut down UK power generator for four days”](https://www.theguardian.com/technology/2026/aug/23/iran-linked-hackers-uk-power-generator-cyber-attack)
- [NCSC: “UK organisations urged to bolster cyber resilience amid Iran conflict”](https://www.ncsc.gov.uk/news/uk-organisations-urged-bolster-cyber-resilience-amid-iran-conflict)

---

## 🏥 Manitoba Shows A Different Machinery Boundary

The Manitoba hospital ransomware incident provides a useful intermediate case.

Ransomware affected the facilities-maintenance network supporting Health Sciences Centre Winnipeg and CancerCare Manitoba.

By the recovery update:

- central HVAC monitoring remained affected;
- local heating, ventilation and cooling continued operating;
- the security office could not issue or update access cards;
- clinical care continued.

That means:

```text
FACILITY-SUPPORT NETWORK:
🟢 COMPROMISED

CENTRAL HVAC MONITORING:
🟢 AFFECTED

LOCAL HVAC OPERATION:
🟢 CONTINUED

PHYSICAL-ACCESS ADMINISTRATION:
🟢 DEGRADED

ATTACKER MANIPULATION OF HVAC SETTINGS:
⚪ NOT ESTABLISHED

CLINICAL CARE:
REPORTED CONTINUING
```

This is machinery-adjacent without being a demonstrated physical-process takeover.

The correct lesson is not:

> ransomware controlled the hospital HVAC.

The correct lesson is:

> ransomware reached the systems used to monitor physical hospital operations and administer physical access, while local operational controls and care delivery remained functional.

That is exactly the sort of case the depth ladder exists to describe.

### Sources

- [Shared Health: “Ransomware incident update”](https://sharedhealthmb.ca/news-releases/2026-08-14-ransomware-incident-update/)
- [CityNews Winnipeg: “Health Sciences Centre ransomware attack update”](https://winnipeg.citynews.ca/2026/08/17/health-sciences-centre-winnipeg-ransomware-attack-update/)

---

## 🧱 Landsberg Shows What Successful Segmentation Looks Like

Stadtwerke Landsberg is one of the most useful controls in the current dataset.

Attackers encrypted central enterprise IT systems.

The utility disconnected internet links, shut affected systems down and rebuilt.

Administrative and communications functions were degraded.

But essential services continued:

- electricity;
- drinking water;
- wastewater;
- district heating;
- fibre infrastructure;
- and EV charging.

That gives us the counterfactual we usually lack.

```text
ENTERPRISE IT:
🟢 COMPROMISED

ADMINISTRATIVE FUNCTIONS:
🟢 DEGRADED

ESSENTIAL OT:
🟢 REMAINED OPERATIONAL

PHYSICAL SERVICE LOSS:
❌ NOT REPORTED
```

The analytical sequence is:

```text
attacker reaches enterprise IT
→ segmentation prevents propagation
→ OT remains trustworthy enough to continue
→ physical service survives
```

This is not merely an absence of harm.

It is evidence that architectural separation can change the consequence.

That means the node should now treat **segmentation quality** as an observed variable, not just a recommendation.

Record:

```text
IT COMPROMISED:
OT REACHED:
NETWORK SEGMENTATION PRESENT:
SEGMENTATION HELD:
REMOTE TRUST RETAINED:
ESSENTIAL SERVICE CONTINUED:
```

Landsberg makes one point very cleanly:

```text
CYBER INTRUSION
≠
MACHINERY COMPROMISE
```

And the difference can be engineered.

### Sources

- [Stadtwerke Landsberg: “Presse / incident updates”](https://www.stadtwerke-landsberg.de/presse/)
- [The Record: “Cyberattack encrypts systems at Bavarian municipal utility”](https://therecord.media/cyberattack-bavaria-germany-utility)

---

## 🤖 AI Changes The Scale Variable

The 19 August Siemens advisory already described AI assistance in exploitation-script development.

By 1 September, Reuters reporting added a stronger scaling picture.

Iranian-aligned actors were reported using AI-generated or AI-assisted scripts against OT assets including PLCs used in:

- power generation;
- substations;
- and other industrial environments.

The most important consequence is not:

> AI can magically operate industrial systems.

It is:

> AI can reduce the labour and expertise needed for some parts of discovery, sorting, scripting and repeated interaction.

That changes the machinery risk model.

The earlier sequence was:

```text
SEE THE SYSTEM
→ TOUCH THE SYSTEM
→ CHANGE WHAT THE SYSTEM DOES
```

The new sequence can also be:

```text
FIND HUNDREDS OF SYSTEMS
→ AUTOMATE TARGET SORTING
→ GENERATE OR ADAPT REUSABLE SCRIPTS
→ IDENTIFY WHICH SYSTEMS RESPOND
→ CONCENTRATE HUMAN ATTENTION ON PROMISING TARGETS
```

This is **search-and-scale**.

It increases expected volume without proving deeper access at any one target.

And it creates an attribution problem.

As AI-assisted tooling becomes easier to reproduce:

```text
MORE TECHNIQUE CONVERGENCE
→ LESS DISTINCTIVE TRADECRAFT
→ GREATER NEED FOR INFRASTRUCTURE, TASKING, TELEMETRY AND RELATIONSHIP EVIDENCE
```

The first effect increases defensive urgency.

The second raises the evidentiary bar.

### Source

- [Reuters: “Energy firms face AI-enhanced cyber attacks”](https://www.reuters.com/business/energy/energy-firms-face-ai-enhanced-cyber-attacks-connectivity-push--reeii-2026-09-01/)

---

## 🧰 Micro-Comm Shows That Machinery Risk Can Begin At The Supplier

The Micro-Comm breach adds another useful boundary.

Micro-Comm supplies PLC and SCADA technology used by water and wastewater facilities.

The company discovered a breach on 31 July.

Barracuda ransomware later published what it claimed was a large stolen dataset.

The reviewed record does **not** establish downstream utility compromise caused by that breach.

Micro-Comm said customer passwords, credentials and information enabling its own remote access to devices were not stolen.

That distinction matters.

```text
SUPPLIER COMPROMISED:
🟢 ESTABLISHED

DOWNSTREAM OT COMPROMISE:
⚪ NOT ESTABLISHED

CUSTOMER REMOTE-ACCESS CREDENTIALS STOLEN:
COMPANY SAYS NO

PRODUCT / CUSTOMER / DIAGRAM INFORMATION EXPOSED:
🟠 / 🟡 DEVELOPING
```

The strategic risk is therefore indirect.

A supplier breach may create:

- customer discovery;
- equipment knowledge;
- architecture clues;
- configuration clues;
- or information that makes later targeting cheaper.

The first actor may be criminal.

The later user may be someone else.

That is why machinery security must include:

```text
THE PLC
+
THE INTEGRATOR
+
THE SUPPORT CONTRACT
+
THE CREDENTIAL
+
THE VENDOR NETWORK
+
THE DOCUMENTATION
```

The machinery is only one part of the machinery ecosystem.

### Source

- [Reuters: “Hack of water-sector supplier draws FBI scrutiny”](https://www.reuters.com/world/hack-water-sector-supplier-draws-fbi-scrutiny-iran-linked-cyber-concerns-grow-2026-08-26/)

---

## ⚓ Naval Reconnaissance Shows The Machinery Question Starts Before Access

Anthropic's September disclosure provides a Level 0 case at the military end of the spectrum.

An Iran-nexus actor used Claude to assemble targeting material concerning US naval forces and research:

- ship and aircraft movements;
- personnel information;
- maritime VSAT terminals;
- Cisco communications equipment;
- and industrial-control products used in shipboard environments.

No successful compromise or control-system manipulation was publicly established.

This belongs at:

```text
LEVEL 0 — EXTERNAL RECONNAISSANCE
```

with some movement into:

```text
CAPABILITY DEVELOPMENT
→ equipment-specific vulnerability research
```

It does **not** move to:

```text
LEVEL 3+
→ operational access
```

without evidence.

That makes it a useful control case.

The machinery ladder starts before the attacker touches machinery.

It begins when the attacker learns:

- what equipment exists;
- where it is deployed;
- who maintains it;
- what communications systems it uses;
- and which vulnerabilities might create a route inside.

### Source

- [Anthropic: “Countering misuse of AI: September 2026”](https://www.anthropic.com/threat-intelligence-report-september-2026)

---

## 🚰 The Water-Control Question

For water incidents, the pack should resist collapsing everything into:

```text
WATER UTILITY HACKED
```

The more useful sequence is:

```text
CAN THEY SEE IT?
        ↓
CAN THEY CONTROL IT?
        ↓
DID THEY CHANGE IT?
        ↓
DID THE PHYSICAL PROCESS CHANGE?
        ↓
DID OPERATORS HAVE TO INTERVENE?
        ↓
DID CIVILIANS OR ESSENTIAL SERVICE SUFFER?
```

Those questions distinguish:

- reconnaissance;
- administrative compromise;
- operational visibility;
- control capability;
- attempted manipulation;
- successful manipulation;
- operational consequence;
- and civilian effect.

This is especially important when public reporting uses broad phrases such as:

- compromised;
- accessed;
- hacked;
- interfered with;
- manipulated;
- or took control.

Those words do not necessarily describe the same technical depth.

The timeline should preserve what is actually known.

---

## 🧯 Manual Operation Is Still Operational Harm

Public reporting often treats manual fallback as proof that nothing serious happened.

That is too generous.

Moving to manual operation may require:

- additional staff;
- emergency call-outs;
- physical presence;
- slower response;
- reduced efficiency;
- suspension of automated safeguards;
- higher error risk;
- and delayed work elsewhere.

Manual fallback is resilience.

It is not the same as normal operation.

A system that remains functional only because people have taken emergency control back by hand has experienced operational harm.

Manual fallback may transfer system risk into:

- operators called out at short notice;
- staff working longer or overnight shifts;
- engineers travelling to remote sites;
- people making safety-critical decisions with incomplete telemetry;
- neighbouring services absorbing diverted work;
- disabled, ill, elderly or isolated people less able to tolerate delay or uncertainty;
- and households expected to manage boil-water notices, pressure loss, interruption or contaminated trust.

The body becomes part of the redundancy plan.

That may be necessary.

It is not costless.

A resilience assessment should therefore ask both:

```text
DID THE SERVICE CONTINUE?

and

WHO ABSORBED THE WORK, RISK, DELAY AND UNCERTAINTY REQUIRED TO KEEP IT CONTINUING?
```

If continuity depends on exceptional human effort, that effort is part of the operational effect.

---

## 🧪 Manual Fallback Should Be Measured

Where information is available, machinery-linked incidents should record:

```text
MANUAL FALLBACK REQUIRED:
MANUAL FALLBACK SUCCESSFUL:
TIME TO MANUAL CONTROL:
SERVICE MAINTAINED:
NORMAL AUTOMATION RESTORED:
NORMAL REMOTE CONTROL RESTORED:
TIME TO RESTORE:
ADDITIONAL STAFF REQUIRED:
SHIFT EXTENSION / FATIGUE:
REMOTE SITE ATTENDANCE:
SAFETY-CRITICAL DECISIONS UNDER DEGRADED VISIBILITY:
PUBLIC ADVISORY OR BEHAVIOUR CHANGE REQUIRED:
DISPROPORTIONATE EFFECT ON HIGH-DEPENDENCY USERS:
```

This prevents:

> service continued

from becoming shorthand for:

> nothing operationally important happened.

Resilience can reduce harm.

It does not erase the intrusion that tested it.

---

## ⚡ Energy And Control Systems

Energy infrastructure creates similar risks.

Relevant systems may control:

- generation;
- substations;
- distribution;
- gas flow;
- fuel storage;
- refinery processes;
- balancing;
- industrial safety;
- and emergency shutdown.

An attacker may not need to cause a blackout to gain strategic value.

Access may be used to:

- map the system;
- test persistence;
- manipulate readings;
- create uncertainty;
- force emergency inspection;
- increase operating costs;
- or pre-position for future escalation.

The UK generator incident now shows that the higher threshold is not theoretical.

A cyber operation can reach:

```text
PHYSICAL GENERATION:
STOPPED
```

without producing:

```text
NATIONAL BLACKOUT:
YES
```

That matters.

Small facilities can be strategically useful because:

- they may be easier to reach;
- they demonstrate capability;
- they impose real local cost;
- and they signal access without triggering the consequences of national-scale destruction.

This is **demonstrative disruption**.

The effect is real.

The scale may be deliberately limited.

---

## 📡 Telecommunications Can Sit Upstream Of Machinery

Telecommunications should increasingly be treated as a machinery dependency.

Water and energy systems may depend on:

- cellular modems;
- remote telemetry;
- vendor VPNs;
- internet connectivity;
- field communications;
- satellite links;
- and managed network services.

That means:

```text
TELECOMS DISRUPTION
→ LOSS OF REMOTE VIEW

TELECOMS COMPROMISE
→ POSSIBLE ROUTE TO REMOTE ACCESS

TELECOMS UNCERTAINTY
→ OPERATORS MAY MOVE TO LOCAL CONTROL
```

The final PLC does not have to be compromised for the physical system to become harder to operate.

This is why the reported expansion of Iran-linked activity into telecommunications matters even where no major telecom outage has yet been attributed to the campaign.

The dependency can be operational before it is visibly physical.

---

## 📡 Remote Access Creates A Repeated Weakness

Operational systems are often connected remotely for legitimate reasons:

- maintenance;
- vendor support;
- monitoring;
- software updates;
- troubleshooting;
- and emergency response.

Those connections can become attack paths where:

- default passwords remain in use;
- remote-access tools are exposed;
- authentication is weak;
- vendors reuse credentials;
- legacy equipment cannot be patched easily;
- or responsibility is divided between operator and contractor.

A sophisticated attacker may target the weakest administrative seam rather than the best-defended control room.

The route into the machinery may begin with:

```text
help desk
→ contractor
→ remote account
→ management interface
→ control system
```

The physical system may be secure in one sense while remaining reachable through the people and suppliers around it.

---

## 🧅 Access To Machinery Can Change Hands

The person who first reaches an operational system may not be the actor who ultimately uses that access.

A possible chain is:

```text
exposed remote interface
→ opportunistic discovery
→ credential compromise
→ retained access
→ access broker
→ intermediary
→ commissioner or later customer
→ payer or procurement route
→ hands-on operator or end user
→ operational tasking or later exploitation
```

Or:

```text
criminal intrusion
→ persistence retained
→ access resold
→ wartime exploitation
```

This matters because the original purpose of the intrusion may differ from its later use.

The first operator may want:

- money;
- credentials;
- resale value;
- prestige;
- or proof of access.

A later actor may recognise strategic value in the same access.

That does not prove command.

It also does not erase the commissioning, payment, foreseeability or downstream-use questions.

The September PaperCut campaign makes this access-manufacturing problem harder to ignore.

Large numbers of privileged footholds can now be generated at machine speed.

The original operator and the eventual user may be different.

For machinery-linked analysis, therefore distinguish where possible:

```text
INITIAL ACCESS:
INITIAL OPERATOR:
ACCESS TRANSFER:
REQUIREMENT GENERATOR:
COMMISSIONER:
PAYER / PROCUREMENT ROUTE:
LATER OPERATOR:
LATER CUSTOMER:
END USER:
FOLLOW-ON USE:
```

The machinery may acquire strategic significance after the original breach.

---

## 🧱 Old Equipment Changes The Defence Problem

Industrial systems are often designed to last for decades.

That creates a mismatch.

The machinery may remain operational long after the security assumptions around it have become obsolete.

Older systems may depend on:

- unsupported software;
- insecure protocols;
- flat networks;
- hard-coded credentials;
- specialist vendor access;
- limited logging;
- and equipment that cannot be taken offline easily for updates.

The problem is not simply that the operator failed to install a patch.

The infrastructure may have been built in an era when remote hostile access was not treated as an ordinary wartime risk.

Defence therefore requires more than blaming local staff.

It requires:

- segmentation;
- access control;
- monitoring;
- manual fallback;
- vendor accountability;
- tested recovery;
- asset inventory;
- and national support for smaller operators.

---

## 🧬 Shared Technology Can Join Separate Incidents

One machinery-linked incident may be local.

Several incidents involving the same equipment family deserve a different question.

The pack should look for recurrence in:

- programmable logic controller models;
- human-machine interfaces;
- remote-access products;
- industrial protocols;
- integrators;
- maintenance contractors;
- authentication weaknesses;
- exposed interfaces;
- and configuration practices.

A pattern such as:

```text
same controller family
+
same remote-access weakness
+
several utilities
+
same operational effect
```

may indicate a shared vulnerability or common targeting logic.

It does not automatically establish a common attacker.

The rival explanations may include:

- one coordinated campaign;
- several actors exploiting the same weakness;
- mass internet scanning;
- common insecure deployment;
- copied techniques;
- AI-generated or AI-assisted tooling;
- or one compromised supplier.

Shared technology is therefore a clustering signal.

It is not attribution by itself.

---

## 🏘️ Local Systems Can Be Strategic Targets

A small local utility may look insignificant.

That can make it attractive.

Local systems may offer:

- weaker security;
- repeated technical similarities;
- visible public consequences;
- geographic spread;
- and lower political risk than attacking a national grid.

A campaign against many small systems can demonstrate reach without producing one nationally catastrophic event.

That pattern may create:

- public anxiety;
- national political pressure;
- expensive emergency support;
- repeated engineering burdens;
- and evidence that an attacker can reach physical processes across many places.

The strategic message may be:

> We do not need to defeat your most protected system. We can keep touching the machinery underneath ordinary life.

The 100+ water disclosure strengthens that interpretation.

The UK generator incident demonstrates the same logic in another sector.

---

## 🔗 Machinery Depends On Other Machinery

Operational systems should not be analysed as isolated sectors.

Water may depend on:

- electricity;
- telecommunications;
- treatment chemicals;
- transport;
- fuel;
- remote contractors;
- and payment or procurement systems.

Energy may depend on:

- telecommunications;
- fuel;
- transport;
- water;
- software;
- satellite services;
- and external maintenance.

Hospitals may depend on:

- HVAC monitoring;
- access-control systems;
- power;
- telecommunications;
- medical-device networks;
- identity systems;
- and external facilities contractors.

That means a cyber incident can produce second-order physical consequences without directly compromising the final machinery itself.

For example:

```text
telecommunications failure
→ remote monitoring lost
→ operators move locally

electricity disruption
→ water pumps move to backup power

transport disruption
→ repair crews or treatment chemicals delayed

facility-monitoring disruption
→ local staff perform more direct physical checks
```

The timeline should therefore distinguish:

```text
DIRECT OT COMPROMISE:
UPSTREAM DEPENDENCY FAILURE:
DOWNSTREAM PHYSICAL EFFECT:
```

A cross-sector campaign may emerge through dependencies rather than identical intrusions.

---

## 🧪 Safety, Availability And Integrity

Operational technology creates three overlapping risks.

### Availability

Can the system continue operating?

Examples include shutdown, lockout, loss of remote control or inability to access the interface.

### Integrity

Can operators trust what the system is doing and reporting?

Examples include altered settings, manipulated sensor readings, false alarms, hidden changes or uncertainty about whether the equipment remains in the intended state.

### Safety

Can the physical process operate without creating danger?

Examples include excessive pressure, unsafe chemical dosing, overheating, equipment damage, flooding or failure of protective controls.

A system may remain available while its integrity is doubtful.

That is still serious.

Operators may have to stop trusting automation before the public sees any visible failure.

---

## 🛑 Protective Controls Are Their Own Evidentiary Layer

The system controlling an ordinary process is not always the same system protecting it from unsafe operation.

Facilities may rely on:

- alarms;
- hard limits;
- interlocks;
- emergency shutdown systems;
- pressure-relief mechanisms;
- independent safety controllers;
- or human verification before dangerous changes take effect.

Compromise of a process controller does not automatically prove compromise of the protective layer.

Equally, the fact that a safeguard prevented harm does not make the attempted or completed manipulation trivial.

Record separately:

```text
PROCESS CONTROL AFFECTED:
PROTECTIVE CONTROL REACHED:
INTERLOCK OVERRIDDEN OR ALTERED:
ALARM RELIABLE:
SAFETY SYSTEM ACTIVATED:
SAFETY SYSTEM SUCCESSFUL:
HUMAN INTERVENTION REQUIRED:
RESIDUAL UNCERTAINTY:
```

The difference between changing the machinery and defeating the machinery’s defences may determine whether a disruptive incident becomes a safety event.

---

## 🕳️ The Attack May Be A Test

Not every intrusion is intended to cause immediate damage.

An operation may be designed to learn:

- how quickly the operator notices;
- whether the state coordinates;
- whether the incident becomes public;
- which agency responds;
- whether attribution is attempted;
- how quickly manual controls are activated;
- which technical mitigations are deployed;
- and which political thresholds trigger action.

That means a limited incident may function as reconnaissance against both the machinery and the state response.

The attacker may be testing:

```text
technical access
+
institutional reaction
+
political tolerance
```

At 100+ systems, the campaign can potentially learn across a population.

That matters.

The system may be doing two things at once:

```text
attacking infrastructure
+
measuring the defender
```

---

## 🤐 Silence Can Reveal The Response Threshold

Where a state refuses to say whether it recognises the incident, whether systems are linked or who owns the response, it may protect operational detail.

It may also reveal that the response architecture is fragmented.

For machinery-linked incidents, that matters because attackers may learn:

- which local operators are left alone;
- which contractors control access;
- which agencies do not share information;
- which events remain below national attention;
- how much disruption can occur without coordinated response;
- and how long executive-level uncertainty persists.

Silence does not prove weakness.

Repeated silence alongside repeated operational incidents can still advertise one.

The state needs a way to protect sensitive information without pretending that the affected operator or person requires no explanation, support or route of escalation.

---

## 🌊 Civilian Water Changes The Legal Question Too

Water infrastructure is not only technically important.

Civilian populations depend upon drinking water for survival.

That means interference with civilian water systems during an armed conflict may raise international humanitarian law questions beyond ordinary cybercrime analysis.

But the analytical sequence must remain disciplined.

The pack should not write:

```text
water system hacked
=
war crime
```

Instead it should ask separately:

```text
WAS THERE AN ARMED-CONFLICT NEXUS?
        ↓
WHAT OBJECT OR SYSTEM WAS AFFECTED?
        ↓
WAS IT CIVILIAN, MILITARY OR DUAL-USE?
        ↓
WHAT DID THE CYBER OPERATION ACTUALLY DO?
        ↓
WHAT PHYSICAL OR CIVILIAN EFFECT FOLLOWED?
        ↓
WHAT DID THE OPERATOR INTEND OR KNOW?
        ↓
CAN THE CONDUCT BE ATTRIBUTED?
        ↓
CAN INDIVIDUAL RESPONSIBILITY BE ESTABLISHED?
```

Those questions concern different legal issues.

They should not be collapsed.

---

## ⚖️ Essential Does Not Mean Targetable

The fact that water, energy, telecommunications, transport, healthcare-support, or another system is essential to the functioning of a state does not by itself make that system a lawful military target.

Likewise:

```text
strategically useful to disrupt
≠
lawfully targetable

state infrastructure
≠
military objective

OT access
≠
lawful attack

civilian harm
≠
automatically a war crime
```

The applicable legal analysis depends on the facts and legal framework.

For this pack, the important point is narrower:

> Once cyber activity reaches civilian machinery capable of affecting survival, safety or essential services, the incident may require both technical escalation analysis and separate IHL review.

The technical record should therefore preserve enough detail for the legal question to be asked later.

---

## 🇮🇷 Why This Matters In The Iran War

Iranian and Iran-linked cyber activity has long included interest in:

- industrial systems;
- water;
- energy;
- government administration;
- transportation;
- telecommunications;
- and other essential services.

That does not mean every machinery-linked incident during the war is Iranian.

It means that movement into operational technology should be treated as a meaningful escalation indicator where the evidence supports it.

By 14 September, the strongest Iran-facing machinery picture is:

```text
US WATER / WASTEWATER
→ repeated controller access
→ settings changes
→ pressure loss / flooding in parts of wave
→ 100+ systems encountered

SIEMENS S7 THREAT
→ broader cross-sector capability development
→ AI-assisted exploitation support
→ read / write capability described

UK ENERGY
→ real generation shutdown
→ four-day physical effect
→ Iran-linked assessment developing

US ENERGY / TELECOMS
→ reported expansion in attempted access / reconnaissance

NAVAL SYSTEMS
→ Iran-nexus equipment-specific reconnaissance
→ no confirmed exploitation
```

That is a broader machinery picture than existed on 20 August.

It is still not one single proven operation.

---

## 🧭 Current Machinery Assessment — 14 September 2026

The strongest current findings are:

```text
CYBER-TO-PHYSICAL EFFECT:
🟢 CONFIRMED IN MULTIPLE INCIDENT TYPES

US WATER OPERATIONAL MANIPULATION:
🟢 CONFIRMED

100+ WATER / WASTEWATER SYSTEM SCALE:
🟢 CONFIRMED AS CAMPAIGN-SCALE DISCLOSURE

UK POWER-GENERATION SHUTDOWN:
🟢 CONFIRMED IN PUBLIC REPORTING

MANITOBA FACILITY-SUPPORT SYSTEM EFFECT:
🟢 CONFIRMED
WITHOUT DEMONSTRATED HVAC PROCESS MANIPULATION

LANDSBERG IT/OT SEGMENTATION SUCCESS:
🟢 CONFIRMED

AI-ASSISTED OT SCALING:
🟡 / 🟢 CREDIBLY REPORTED

IRAN-LINKED CORE WATER ASSESSMENT:
🟡 PROBABLE

FORMAL ATTRIBUTION OF EVERY MACHINERY INCIDENT:
⚪ NOT ESTABLISHED

COMMON OPERATOR ACROSS WATER, ENERGY, TELECOMS AND OTHER OT:
⚪ NOT ESTABLISHED
```

The most important analytical change is now:

```text
DEPTH
+
SCALE
+
SEGMENTATION
+
ACCESS TRANSFER
```

not depth alone.

The defender needs to know:

```text
HOW FAR IN DID THEY GET?

HOW MANY SYSTEMS COULD THEY FIND?

DID THE NETWORK ARCHITECTURE STOP THEM?

AND COULD THE ACCESS LATER CHANGE HANDS?
```

Those four questions now belong together.

---

## 🔎 What Should Be Recorded

Each machinery-linked incident should record:

```text
DATE:
COUNTRY:
SECTOR:
OPERATOR:
SYSTEM TYPE:
SYSTEM / CONTROLLER FAMILY:
ENTRY POINT:
REMOTE OR LOCAL ACCESS:
THIRD-PARTY PROVIDER / INTEGRATOR ACCESS:

DEPTH-OF-ACCESS LEVEL:
IT ACCESS:
OT VISIBILITY:
HMI / CONTROL INTERFACE ACCESS:
CONTROLLER / CONFIGURATION ACCESS:
COMMAND CAPABILITY:
READ CAPABILITY:
WRITE CAPABILITY:
OBSERVED COMMAND OR WRITE ACTION:

WHAT WAS ALTERED:
CONFIGURATION CHANGE:
PROJECT / LOGIC FILE CHANGE:
MONITORING / VISIBILITY LOST:
CONTROL LOST:

PHYSICAL EFFECT:
PRESSURE / FLOW / LEVEL EFFECT:
GENERATION EFFECT:
FLOODING / RELEASE EFFECT:
BUILDING / FACILITY SUPPORT EFFECT:

MANUAL FALLBACK REQUIRED:
MANUAL FALLBACK SUCCESSFUL:
SAFETY IMPACT:
SAFETY INTERLOCK / PROTECTIVE CONTROL STATUS:
SERVICE IMPACT:
HUMAN CONSEQUENCE:
EXCEPTIONAL LABOUR / FATIGUE COST:

IT/OT SEGMENTATION PRESENT:
SEGMENTATION HELD:
SEGMENTATION FAILURE:
TRUST BOUNDARY CROSSED:

UPSTREAM DEPENDENCIES:
DOWNSTREAM EFFECTS:
SHARED CONTRACTOR OR TECHNOLOGY:
SUPPLIER COMPROMISE:
ASSET INVENTORY QUALITY:

CIVILIAN / MILITARY / DUAL-USE STATUS:
IHL REVIEW NEEDED:

ATTRIBUTION:
ACTOR CLAIM:
INITIAL OPERATOR:
ACCESS TRANSFER:
REQUIREMENT GENERATOR:
COMMISSIONER:
PAYER / PROCUREMENT ROUTE:
END USER / LATER BENEFICIARY:

REPORTED INVESTIGATIVE ASSESSMENT:
FORMAL PUBLIC ATTRIBUTION:
CONFIDENCE:
ORGANISING MECHANISM:
RIVAL EXPLANATIONS:

SCALE OF DISCOVERY / TARGETING:
AI-ASSISTED DISCOVERY OR SCRIPTING:
REPEATABILITY:
RECOVERY TIME:
SOURCES:
LAST REVIEWED:
```

Where possible, distinguish:

- confirmed physical effect;
- confirmed manipulation without demonstrated physical effect;
- demonstrated control capability;
- control-interface access;
- OT visibility;
- facilities-support compromise;
- attempted access;
- successful segmentation;
- and claims that remain unverified.

Do not turn a suspected control-system intrusion into a proven physical attack.

Do not turn visibility into control.

Do not turn control capability into demonstrated manipulation.

Do not reduce a forced manual fallback to “no disruption.”

Do not treat a successful segmentation boundary as evidence that the intrusion did not matter.

---

## 🚨 What Would Change The Trend

A machinery-linked pattern should be treated as escalating where there is credible evidence of:

- movement from IT into OT;
- movement from OT visibility into control access;
- movement from interface access into controller configuration;
- movement from access into command execution;
- repeated capability development or pre-positioning against specific controller families;
- confirmed physical-process manipulation;
- attempted or successful interference with alarms, interlocks, emergency shutdown or other protective controls;
- repeated manual fallback across several utilities;
- repeated compromise of the same controller family;
- geographic spread;
- cross-sector operational effects;
- attacks against water or other systems indispensable to civilian life;
- persistent access retained for later use;
- access transfer, procurement or later customer use involving operational systems;
- stronger evidence connecting previously separate incidents to a common operator or sponsor;
- rapid AI-assisted scaling of target discovery;
- repeated supplier or integrator compromise;
- or evidence that segmentation is failing across multiple operators.

The trend can therefore worsen without one spectacular outage.

The important change may be:

```text
more systems
```

or:

```text
deeper access
```

or:

```text
greater physical effect
```

or:

```text
faster access
```

or:

```text
weaker segmentation
```

or:

```text
more transferable access
```

or:

```text
stronger campaign linkage
```

Those are different forms of escalation.

---

## 🚫 What This Node Does Not Claim

This node does not claim that:

- every operational-technology intrusion is a state attack;
- every manual fallback means catastrophe was narrowly avoided;
- every local utility incident forms part of one campaign;
- shared technology proves shared sponsorship;
- HMI access proves controller manipulation;
- controller access proves physical effect;
- a tool’s read/write capability proves that a write occurred at a particular facility;
- an active threat warning proves every exposed controller was compromised;
- capability development identifies the operator of every resulting incident;
- AI-assisted tooling identifies a state sponsor;
- access automatically proves destructive intent;
- service continuity proves there was no exceptional labour, risk or human cost;
- supplier compromise proves downstream machinery compromise;
- facilities-monitoring compromise proves attacker control of physical plant;
- every commissioner controls the technical method;
- every civilian infrastructure incident during wartime violates international humanitarian law;
- or every cyber operation affecting water constitutes a war crime.

It argues that operational technology changes the stakes.

Once an attacker can affect machinery, the relevant question is no longer only what data was seen.

It is:

> How far into the physical control chain did they get?

And now also:

> How many systems could they find?

> Did segmentation stop them?

> Could access be transferred?

> What did the machinery actually do?

---

## 🧭 Working Rule

The working rule is:

> Treat demonstrated movement from information systems towards physical control as a meaningful escalation indicator, while recording each level of access separately and refusing to infer physical manipulation from access alone.

For each depth, separate:

> access → capability → observed action → process response → service effect → human consequence.

And now also separate:

> discovery scale → segmentation outcome → access transfer potential.

Record:

- what the attacker could see;
- what they could control;
- what they changed;
- what the machinery did;
- whether alarms, interlocks or protective controls remained trustworthy;
- what operators could still see;
- what operators could still control;
- whether manual fallback was required;
- whether the fallback worked;
- whether IT/OT segmentation held;
- who absorbed the exceptional labour, risk, delay or uncertainty;
- whether access changed hands or a later customer commissioned its use;
- which technology recurs elsewhere;
- how many systems were discoverable;
- which suppliers or integrators created shared exposure;
- which systems depend upon the affected machinery;
- what physical or civilian effect followed;
- and what remains unproven.

Record who had to take control back.

Record whether the boundary held.

Record how far into the machinery the evidence actually goes.

That is where cyber reaches the machinery.

---

## 🌌 Constellations

🚰 ⚡ 🏭 🧯 📡 🪜 🧱 🧅 — water; energy; operational technology; manual fallback; remote access; depth of control; segmentation; access transfer.

---

## ✨ Stardust

operational technology, industrial control systems, programmable logic controllers, water systems, energy infrastructure, telecommunications, hospital facilities, manual fallback, segmentation, physical disruption, cyber escalation, HMI, SCADA, controller access, ai-assisted exploitation, supplier compromise, access transfer, physical process, critical infrastructure, MicroLogix, Siemens S7, pressure loss, flooding, generation shutdown, CyberAv3ngers, APT IRAN

---

## 🏮 Footer

*🚰 When Cyber Reaches The Machinery* is a living node of the **Polaris Protocol**.  
It identifies and grades the threshold at which cyber activity moves from information systems into the monitoring, control, manipulation, protective systems, physical effects, segmentation boundaries, and human fallback labour of the machinery beneath ordinary life.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope, routing, scale and attribution rules*
> - [🏗️ What Counts As State Infrastructure](./🏗️_what_counts_as_state_infrastructure.md) — *functional infrastructure perimeter, dependencies and civilian status*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *cumulative operational pressure, clustering and depth of escalation*
> - [🌊 Riding Every Wave](./🌊_riding_every_wave.md) — *access markets, commissioned outcomes and later exploitation across successive waves*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *graded attribution and uncertainty*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *access brokerage, layered tasking and later operational use*
> - [🗺️ Who Iran Sees As Inside The War](./🗺️_who_iran_sees_as_inside_the_war.md) — *threat-exposure map and coalition context*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *separate legal analysis for wartime cyber operations*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *live chronology through 14 September 2026*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *separating the Iran-facing OT wave from simultaneous criminal and administrative incidents*
> - [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *claim-level evidence, provenance and source independence*
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
