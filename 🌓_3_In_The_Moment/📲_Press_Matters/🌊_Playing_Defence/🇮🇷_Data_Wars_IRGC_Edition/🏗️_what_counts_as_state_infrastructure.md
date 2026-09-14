# 🏗️ What Counts As State Infrastructure
**First created:** 2026-08-01 | **Last updated:** 2026-09-14  
*The test is what the system does, not whether the organisation running it is formally part of the state.*

---

## 🛰️ Orientation

This pack uses a functional definition of state infrastructure.

The question is not simply:

> Is this system owned by the government?

The better question is:

> Would compromise, disruption, manipulation, loss, or untrustworthiness of this system materially interfere with the state's ability to govern or with ordinary social life?

Modern states do not run only through ministries.

They run through:

- local authorities;
- hospitals;
- schools and universities;
- water companies;
- energy networks;
- banks and payment systems;
- transport operators;
- telecommunications providers;
- contractors;
- software platforms;
- outsourced databases;
- industrial-control systems;
- cloud infrastructure;
- and private organisations performing public functions.

A privately owned system may therefore be part of the state's essential infrastructure.

The issue is:

```text
function
+
dependency
+
consequence
```

Not branding.

But this pack also keeps another distinction explicit:

```text
essential to state function
≠
lawful military target
```

A civilian system does not lose its protection merely because the state depends heavily upon it.

Functional inclusion and legal targetability are separate questions.

---

## 🧭 The Functional Test

A system belongs inside this pack where one or more of the following is true:

- the state relies on it to deliver an essential public function;
- ordinary life cannot continue normally without it;
- its failure would create a serious public-safety risk;
- its data is necessary for government, care, justice, education, or economic participation;
- it supports defence, emergency response, or national decision-making;
- it is a critical dependency for another essential system;
- compromise would create substantial coercive, intelligence, or destabilising value;
- access to it could provide a route from digital intrusion to physical effect;
- or failure of the system would force exceptional human fallback to preserve continuity.

This produces a broader perimeter than:

```text
government-owned computer
=
state infrastructure
```

The real structure is closer to:

```text
public function
+
critical dependency
+
material consequence
=
essential state infrastructure
```

For some systems, two further questions matter:

```text
CAN CYBER ACCESS CHANGE
WHAT THE PHYSICAL SYSTEM DOES?

and

CAN FAILURE OF THIS SYSTEM
CAUSE ANOTHER ESSENTIAL SYSTEM TO FAIL?
```

Where the answer to either is yes, the incident deserves additional analytical weight.

The functional test is strongest when it asks:

```text
WHAT PUBLIC OR ESSENTIAL FUNCTION DOES THE SYSTEM PERFORM?
↓
WHO AND WHAT DEPEND ON IT?
↓
HOW DEEPLY DID THE INCIDENT REACH?
↓
WHAT ALTERNATIVE CAPACITY EXISTED?
↓
WHO ABSORBED THE FALLBACK?
↓
WHAT MATERIAL CONSEQUENCE FOLLOWED?
↓
WHAT OTHER SYSTEMS BECAME LESS RELIABLE BECAUSE OF IT?
```

This prevents size, ownership, sector label, dramatic timing, and political prominence from doing analytical work that belongs to evidence.

A large company may sit outside the perimeter where no essential function was affected.

A small contractor may sit inside it where several public services cannot operate safely without its software, access, records, or specialist labour.

The perimeter is therefore relational.

It follows the dependency between the system and the function.

---

## 🧩 Infrastructure Is More Than Machinery

Some infrastructure moves water, electricity, fuel, people, or goods.

Some infrastructure allows the state to know, decide, coordinate, pay, authenticate, and respond.

The pack should therefore distinguish at least five forms:

```text
PHYSICAL INFRASTRUCTURE
→ plant, pumps, power, transport, buildings

INFORMATION INFRASTRUCTURE
→ records, identity, telemetry, provenance

DECISION INFRASTRUCTURE
→ eligibility, authorisation, dispatch, legal process

COORDINATION INFRASTRUCTURE
→ communications, suppliers, staff, incident ownership

DEPENDENCY INFRASTRUCTURE
→ systems whose failure disables another essential function
```

These layers interact.

A pump may remain physically intact while its controller becomes untrusted.

A hospital may remain open while central monitoring, access control, or patient records require manual workarounds.

A benefit may remain legally due while the administrative system cannot authorise payment.

A port may keep its cranes while gate processing, customs or telecoms fail.

A court may remain physically open while a shared case-management provider exposes sensitive records.

The absence of damaged machinery does not establish the absence of infrastructure harm.

---

## ⚖️ State Infrastructure Is Not A Legal Target Category

The phrase **state infrastructure** is used functionally in this pack.

It should not be confused with an international humanitarian law classification.

Something can be:

- essential to governance;
- economically important;
- publicly owned;
- relied upon by the military;
- politically sensitive;
- or central to civilian life

without automatically becoming a lawful military objective.

Likewise:

```text
government ownership
≠
military objective

essential public function
≠
military objective

coalition-state infrastructure
≠
military objective
```

The legal status of a particular object depends on the applicable law and the facts concerning its nature, location, purpose, or use.

This distinction matters especially in this pack because many of the systems most valuable for strategic pressure are predominantly civilian.

That includes:

- drinking water;
- wastewater;
- hospitals;
- education;
- public administration;
- civilian banking;
- telecommunications;
- transport;
- and civilian energy infrastructure.

The fact that disruption would hurt the state is not itself enough to establish lawful targetability.

---

## 🚰 Water And Wastewater

Water is one of the clearest examples of essential civilian infrastructure.

Relevant systems include:

- drinking-water treatment;
- pumping and pressure control;
- reservoirs;
- wells;
- wastewater treatment;
- sewage management;
- desalination;
- industrial control systems;
- programmable logic controllers;
- supervisory control systems;
- remote monitoring;
- laboratory data;
- customer and site records;
- electricity supplying treatment and pumping;
- telecommunications supporting remote control;
- and emergency fallback arrangements.

An attack does not need to contaminate the water supply to matter.

Operational harm may include:

- altered settings;
- altered credentials;
- loss of remote control;
- loss of trusted monitoring;
- loss of pressure;
- flooding;
- system lockout;
- movement to manual operation;
- delayed treatment;
- increased staffing requirements;
- unreliable sensor data;
- or loss of confidence in whether readings can be trusted.

Manual operation is resilience.

It can also be evidence that the normal digital control environment has been degraded.

The relevant analytical question is therefore not only:

> Did the water continue flowing?

It is also:

> What had to change operationally to keep it flowing?

---

## 📈 Scale Can Turn Local Infrastructure Into A National Problem

By late August, CISA had publicly quantified July malicious activity at more than **100 internet-exposed US water and wastewater systems**.

That matters for infrastructure classification.

Each affected site may be locally operated.

The pattern is not therefore merely local.

A large number of small essential systems can create a national-resilience issue where they share:

- the same controller families;
- the same internet exposure;
- the same vendor practices;
- or the same defensive weakness.

The correct lesson is:

```text
LOCAL OWNERSHIP
≠
LOCAL SIGNIFICANCE
```

When a repeated weakness affects many small operators performing the same essential function, the aggregation itself becomes infrastructure significance.

This does not prove one attacker.

It does establish one systemic exposure.

---

## 🚰 Water Has A Control Layer

Water systems demonstrate why administrative IT and operational technology should not be treated as interchangeable.

A simplified distinction is:

```text
UTILITY IT
→ email
→ billing
→ customer records
→ payroll
→ administration

UTILITY OT
→ pumps
→ valves
→ pressure
→ treatment
→ sensors
→ controllers
→ physical process
```

A compromise of either layer can be serious.

But the second provides a more direct path from cyber access to physical effect.

That means the pack should record separately:

```text
IT COMPROMISED:
OT COMPROMISED:
CONTROL LOST:
MONITORING LOST:
PHYSICAL PROCESS CHANGED:
MANUAL FALLBACK REQUIRED:
```

where the information is available.

The significance is not simply that a water utility was hacked.

It is how far into the delivery process the intrusion reached.

---

## 🌊 Water Can Be Indispensable In More Than One Sense

Water is not merely economically useful.

Civilian populations require it to survive.

International humanitarian law therefore treats objects indispensable to the survival of the civilian population as a particularly important protected category, subject to the exact applicable legal framework and facts.

That makes cyber interference with civilian water infrastructure analytically distinct from disruption of an ordinary commercial service.

This does **not** mean:

```text
cyber incident against water
=
war crime
```

The legal analysis still requires the relevant armed-conflict nexus, conduct, effects, intent or knowledge, target status, attribution, and individual responsibility.

But it does mean that where cyber activity reaches civilian water-control systems during an armed conflict, the pack should flag the incident for separate IHL review.

The functional and legal questions should both be visible.

They should not be collapsed together.

---

## ⚡ Energy And Industrial Control

Energy infrastructure includes more than national electricity generation.

It includes:

- electricity production;
- transmission and distribution;
- gas networks;
- oil and fuel infrastructure;
- substations;
- storage;
- refineries;
- control-room systems;
- programmable logic controllers;
- supervisory control systems;
- billing and balancing systems;
- fuel logistics;
- and the telecommunications supporting them.

An attack may aim to:

- interrupt supply;
- damage equipment;
- create unsafe conditions;
- force manual operation;
- obtain technical intelligence;
- pre-position for later disruption;
- degrade confidence;
- or demonstrate access without immediately using it.

The absence of a blackout does not mean the operation lacked strategic value.

Persistent access may matter more than immediate spectacle.

So may the ability to manipulate rather than destroy.

---

## ⚡ A Small Generator Can Still Be Infrastructure

The July cyberattack on a small British power generator, disclosed in August, is a useful boundary case.

The generator was reportedly forced offline for four days.

Officials said it was too small to threaten the wider grid.

That does not remove its infrastructure status.

The correct test is not:

```text
DID THE NATIONAL GRID FAIL?
```

It is:

```text
DID A SYSTEM PERFORMING AN ESSENTIAL ENERGY FUNCTION
SUFFER A CYBER-INDUCED PHYSICAL EFFECT?
```

Here, the answer is yes.

That gives us:

```text
PHYSICAL GENERATION EFFECT:
🟢 ESTABLISHED IN PUBLIC REPORTING

NATIONAL GRID EFFECT:
❌ NOT REPORTED

STRATEGIC SIGNIFICANCE:
LOCAL PHYSICAL EFFECT
+
SECTOR-WIDE LEARNING VALUE
```

Small infrastructure can therefore matter through:

- function;
- repeatability;
- demonstrated exploitability;
- and what the incident teaches about the wider estate.

### Sources

- [BBC: “Cyber attack shut down small power plant”](https://www.bbc.co.uk/news/articles/ce9793g34yvo)
- [The Guardian: “Iran-linked hackers shut down UK power generator for four days”](https://www.theguardian.com/technology/2026/aug/23/iran-linked-hackers-uk-power-generator-cyber-attack)

---

## 🔗 Essential Systems Depend On Each Other

The pack should not analyse sectors as sealed boxes.

Modern infrastructure is interdependent.

For example:

```text
electricity
→ powers water pumps

telecommunications
→ carries control signals

banking
→ enables payroll and procurement

transport
→ delivers repair crews and chemicals

cloud services
→ host administrative systems

fuel
→ sustains backup generation

identity systems
→ permit staff and users to access services
```

That means an attack on one sector may create second-order effects elsewhere.

A useful record should therefore ask:

```text
PRIMARY SECTOR:
DEPENDENT SECTORS:
UPSTREAM DEPENDENCIES:
DOWNSTREAM EFFECTS:
```

This becomes particularly important where several sectors experience disruption in the same geography or narrow time window.

One isolated failure may be local.

Several interdependent failures may become a state-resilience problem.

---

## 📡 Telecommunications Are Dependency Infrastructure

Telecommunications infrastructure includes:

- mobile networks;
- fixed-line networks;
- internet exchange;
- data centres;
- emergency communications;
- government networks;
- satellite services;
- cloud connectivity;
- undersea and terrestrial links;
- and systems used to authenticate and route users.

It supports almost every other sector in this node.

A telecommunications incident may:

- interrupt service;
- expose location or identity data;
- enable interception;
- degrade emergency response;
- isolate public bodies;
- reduce visibility into operational systems;
- or provide access to other systems.

Connectivity is not merely a convenience.

It is a dependency layer beneath the modern state.

The September reporting on Iran-linked attempts against electricity and telecommunications therefore matters even where no major telecom outage is attached to the new tranche.

The strategic significance can sit in:

```text
RECONNAISSANCE
+
ACCESS
+
DEPENDENCY
```

before it sits in catastrophe.

---

## 🏥 Health And Medical Supply

Health infrastructure includes:

- hospitals;
- primary care;
- emergency services;
- pharmacies;
- laboratories;
- blood and transplant services;
- medical-device manufacturers;
- medicine supply;
- appointment and referral systems;
- patient records;
- safeguarding data;
- medical devices;
- and communications connecting care providers.

A health-sector incident may remain strategically serious even where hospitals stay open.

Effects may include:

- delayed treatment;
- unavailable records;
- disrupted diagnostic systems;
- cancelled procedures;
- medication delays;
- loss of staff time;
- unsafe manual workarounds;
- exposure of intimate data;
- disrupted devices;
- and pressure on already stretched services.

Medical supply chains also belong inside the perimeter where their failure affects the practical delivery of care.

The fact that the affected body is a company does not remove the public-health consequence.

The fact that a hospital remains open does not mean normal care continues.

---

## 🏨 The Hospital Building Is Part Of The Care System

Health infrastructure does not stop at clinical applications or medical devices.

It also includes facility systems that keep the care environment usable and secure, including:

- heating, ventilation and cooling;
- environmental monitoring;
- access control and identity cards;
- alarms and physical security;
- lifts and internal movement;
- power and backup generation;
- water and medical gases;
- and the staff who monitor or operate those systems locally when central control is unavailable.

The August ransomware incident affecting parts of Health Sciences Centre Winnipeg and CancerCare Manitoba's facility-maintenance environment remains a useful boundary case.

The reported effects included:

```text
RANSOMWARE INCIDENT:
🟢 ESTABLISHED

FACILITY-MAINTENANCE SYSTEM EFFECT:
🟢 ESTABLISHED

CENTRAL HVAC MONITORING AFFECTED:
🟢 ESTABLISHED

LOCAL MONITORING / ADDITIONAL SECURITY REQUIRED:
🟢 ESTABLISHED

CLINICAL SERVICE DISRUPTION:
NOT ESTABLISHED IN THE REVIEWED UPDATE

PERSONAL OR HEALTH-DATA ACCESS:
NOT DETERMINED; INITIAL REVIEW INDICATED NONE

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

The infrastructure lesson does not depend on claiming that patient care stopped.

It is that central monitoring, building access and environmental control are functional dependencies of care.

Continuity achieved through local monitoring and additional personnel demonstrates resilience while also revealing the labour and capacity required to replace the affected digital layer.

### Source

- [Shared Health: “Ransomware incident update”](https://sharedhealthmb.ca/news-releases/2026-08-14-ransomware-incident-update/)

---

## 🏥 Clinical Continuity Can Degrade Before A Hospital Closes

Luminis Health provides the opposite boundary.

The hospital system remained operational in some form.

But the incident still produced:

- non-critical ambulance diversion;
- treatment cancellations or delays;
- and system unavailability.

That belongs inside infrastructure analysis because:

```text
HOSPITAL OPEN
≠
NORMAL CARE

NO TOTAL OUTAGE
≠
NO ESSENTIAL-SERVICE EFFECT
```

The correct measure is function.

How much care became slower, less available, rerouted, or more labour-intensive?

That is the infrastructure effect.

---

## 🎓 Education And Public Records

Education is often treated as a soft sector.

That is a mistake.

Education systems hold:

- identity data;
- safeguarding records;
- disability information;
- immigration and nationality data;
- addresses;
- family relationships;
- examination records;
- disciplinary information;
- financial information;
- staff data;
- research;
- and communications linking individuals to public institutions.

They also support:

- schools;
- universities;
- student finance;
- qualifications;
- teacher administration;
- public grants;
- research systems;
- and international programmes.

A breach may not close every school.

It may still remove large quantities of sensitive public data from institutional custody and create lasting:

- intelligence;
- fraud;
- coercion;
- discrimination;
- identity misuse;
- or targeting value.

A person cannot restore a previous identity because the institution restored its server.

---

## 🏢 Government Administration, Policing And Justice

State administration includes:

- central government departments;
- local government;
- parliamentary systems;
- courts;
- prosecution;
- police;
- prisons;
- immigration;
- benefits;
- taxation;
- identity systems;
- legal databases;
- procurement;
- and public correspondence.

An attack may matter where it:

- removes data from state custody;
- disrupts decision-making;
- prevents access to records;
- exposes witnesses or vulnerable people;
- interferes with legal process;
- undermines confidence in evidence;
- corrupts data;
- or prevents a person from obtaining an accountable state response.

Administrative data is not a bureaucratic side issue.

It is part of how the state:

- recognises people;
- assigns rights;
- records risk;
- allocates resources;
- and exercises power.

Compromise can therefore produce direct personal harm as well as institutional disruption.

---

## ⚖️ Shared Court Software Can Be Infrastructure Even Without Court Closure

The C-Track incident adds an important shared-provider example.

Thomson Reuters disclosed unauthorised access to files held through the C-Track court case-management platform across multiple US jurisdictions, the US Virgin Islands and Ontario.

The reviewed record did not establish court-service disruption.

That does not make the incident infrastructurally irrelevant.

The system sits inside:

- judicial administration;
- case records;
- sensitive personal information;
- potentially sealed or restricted material;
- and the continuity of legal process.

This creates a useful distinction:

```text
SERVICE AVAILABILITY:
🟢 MAINTAINED

INFORMATION INFRASTRUCTURE:
🟢 COMPROMISED

DECISION INFRASTRUCTURE:
POTENTIALLY EXPOSED TO CONFIDENTIALITY / TRUST RISK

SHARED PROVIDER CONCENTRATION:
🟢 ESTABLISHED
```

A state can retain service availability while losing confidence in the confidentiality or provenance of records.

That still counts.

---

## 🏦 Banks, Payments And Financial Confidence

Banks are often private companies.

The banking system is nevertheless part of how the state and society continue to function.

Relevant infrastructure includes:

- retail banking;
- wholesale payments;
- card networks;
- cash access;
- clearing and settlement;
- payroll;
- benefits and pension payments;
- public-sector banking;
- financial-market infrastructure;
- identity and fraud systems;
- central-bank dependencies;
- and systemically important financial institutions.

The effect of an attack may be:

- inability to access money;
- delayed wages or benefits;
- interrupted payments;
- liquidity pressure;
- customer panic;
- fraud;
- loss of confidence;
- or increased pressure on government.

A banking attack does not need to destroy the financial system to have strategic effect.

Confidence is itself part of the infrastructure.

This is why the pack tracks systemically important banking rather than every financial-services incident.

---

## 🚆 Transport And Logistics

Transport infrastructure includes:

- rail;
- roads;
- ports;
- airports;
- public transit;
- freight;
- traffic management;
- ticketing;
- fleet control;
- customs systems;
- fuel supply;
- navigation;
- and logistics supporting health, food, defence and emergency response.

Disruption may affect:

- movement of people;
- movement of goods;
- military logistics;
- emergency services;
- food and medicine supply;
- industrial production;
- repair operations;
- or evacuation and civil protection.

Transport systems are also highly dependent on:

- telecommunications;
- energy;
- payments;
- satellite services;
- cloud systems;
- and software suppliers.

A breach in one contractor can therefore create consequences across several public functions.

---

## ✈️ CEVA — The Logistics Boundary Case

CEVA Logistics shows why a private transport company cannot be classified by brand or scale alone.

A cyberattack affected contract-logistics operations at eight CEVA warehouses in Europe.

Public reporting described shipment delays.

Affected-customer reporting later identified exposure of some delivery and contact data.

That establishes:

```text
PRIVATE LOGISTICS OPERATOR:
🟢 ESTABLISHED

OPERATIONAL WAREHOUSE DISRUPTION:
🟢 ESTABLISHED

SHIPMENT DELAYS:
🟢 ESTABLISHED

SOME CUSTOMER-DATA EXPOSURE:
🟢 ESTABLISHED
```

It does not establish:

```text
PORT-CONTROL COMPROMISE:
⚪ NO EVIDENCE FOUND

TRANSPORT OT COMPROMISE:
⚪ NO EVIDENCE FOUND

MILITARY-LOGISTICS TARGETING:
⚪ NO EVIDENCE FOUND

IRAN CONNECTION:
⚪ NO EVIDENCE FOUND
```

The correct classification is therefore:

> **adjacent essential logistics infrastructure, with significance dependent on the affected supply chains.**

CEVA's relevance would rise where evidence showed that the affected warehouses were necessary to:

- food distribution;
- medical or pharmaceutical supply;
- fuel or energy operations;
- defence logistics;
- emergency response;
- critical industrial production;
- or recovery of another essential system.

It would remain lower where the demonstrated effect was confined to ordinary discretionary retail shipments with adequate alternative capacity.

The inclusion test is:

```text
WHAT GOODS OR SERVICES WERE MOVING?
+
WHO DEPENDED ON THEM?
+
WHAT ALTERNATIVE CAPACITY EXISTED?
+
WHAT STOPPED OR BECAME UNSAFE?
```

Not:

```text
BIG LOGISTICS COMPANY
=
AUTOMATICALLY STATE INFRASTRUCTURE
```

---

## 🪜 A Graduated Logistics Perimeter

Logistics incidents should be placed on a graduated perimeter.

### Direct essential-function infrastructure

The affected system directly operates or controls:

- emergency transport;
- public transit;
- customs or border movement;
- fuel distribution;
- medical supply;
- food distribution;
- defence logistics;
- or another indispensable public function.

### Critical supply-chain dependency

The operator is private, but another essential service cannot continue normally without its warehouses, fleet, software, data or routing capacity.

### Adjacent essential-logistics watch

The operator has plausible essential-sector relevance, but the reviewed record does not yet show that the affected facilities served a critical function.

### Commercial disruption only

The incident delays ordinary commercial goods without demonstrated public-function, safety or strategic consequence.

This may still be a serious cybercrime incident.

It does not automatically belong in an essential-state infrastructure campaign.

---

## 🧬 A Large Corporate Victim Is Not Automatically An Infrastructure Event

The Cl0p campaign remains a useful boundary test.

Cl0p claimed data theft from major organisations including Shell, Philips, GE and Fiserv.

Those names sit in energy, medical-technology, industrial and financial ecosystems.

Their sectoral importance justifies scrutiny.

It does not establish an essential-service operational effect.

Therefore:

```text
ESSENTIAL-SECTOR COMPANY NAMED:
🟢 ESTABLISHED

ACTOR DATA-THEFT CLAIM:
📣 ESTABLISHED AS A CLAIM

ESSENTIAL PUBLIC FUNCTION DISRUPTED:
NOT GENERALLY ESTABLISHED

OPERATIONAL INFRASTRUCTURE COMPROMISED:
NOT GENERALLY ESTABLISHED
```

The pack may retain such cases as **exposure evidence** or a **shared-dependency campaign** without upgrading every corporate breach into an infrastructure outage.

That distinction protects the perimeter from becoming:

```text
LARGE COMPANY
+
IMPORTANT SECTOR
=
STATE INFRASTRUCTURE ATTACK
```

The missing question remains:

> **What essential function was actually affected?**

---

## 🧾 Contractors And Outsourced Systems

A government may outsource delivery.

It does not outsource strategic consequence.

A contractor belongs inside this pack where it:

- operates an essential public system;
- stores sensitive state data;
- provides software used across public bodies;
- controls access to a public service;
- supports a critical supply chain;
- operates operational technology;
- provides remote maintenance;
- or represents a single point of failure.

Relevant examples may include:

- cloud providers;
- managed-service companies;
- help-desk platforms;
- identity-verification systems;
- medical suppliers;
- transport software;
- payment processors;
- control-system integrators;
- remote-access providers;
- and specialist defence or security firms.

The correct question is not:

> Is the contractor technically part of government?

It is:

> What public function becomes unavailable, unsafe, unreliable, controllable, or exposed if this contractor fails?

The record should map roles rather than compress every participant into **the organisation**:

```text
PUBLIC AUTHORITY / FUNCTION OWNER:
COMMISSIONER / PAYER:
SERVICE OPERATOR:
TECHNICAL OPERATOR:
CONTRACTOR / SUPPLIER:
ACCESS PROVIDER:
END USER / BENEFICIARY:
```

Those roles may belong to one body.

They may also be distributed across several institutions that hold different evidence, duties, permissions, and incentives.

Mapping the relationship is therefore part of defining the infrastructure.

---

## 🕸️ Contractors Can Join Sectors Together

A contractor may serve several institutions or sectors at once.

That creates another type of infrastructure significance.

A single supplier may provide:

- remote access to several water utilities;
- identity systems across local government;
- software used by hospitals and schools;
- cloud hosting for multiple agencies;
- telecommunications to several essential services;
- court software across jurisdictions;
- or industrial-control support across geographically dispersed facilities.

Compromise of the supplier can therefore create:

```text
one access point
→ several institutions
→ several locations
→ several public functions
```

This is why the pack should track not only affected organisations but **shared dependencies**.

A pattern that appears distributed may have one common supplier underneath it.

The reverse is also possible.

Several incidents against the same product may reflect many unrelated attackers exploiting the same weakness.

Common technology is a lead.

It is not automatic proof of a common campaign.

---

## 🧰 Micro-Comm Shows Why Supplier Exposure Counts

The Micro-Comm breach is useful even though no downstream water-utility compromise was established.

A supplier of PLC and SCADA technology may hold:

- customer references;
- product diagrams;
- technical documentation;
- configuration knowledge;
- and remote-support relationships.

Even where credentials are not stolen, that information can reduce the cost of later targeting.

The infrastructure significance therefore lies in:

```text
SUPPLIER KNOWLEDGE
+
DOWNSTREAM ESSENTIAL CUSTOMERS
+
POTENTIAL REUSABILITY
```

Not in pretending that every customer was compromised.

The correct classification is:

```text
SUPPLIER INFRASTRUCTURE:
🟢 RELEVANT

DOWNSTREAM OT EFFECT:
⚪ NOT ESTABLISHED
```

That distinction matters.

---

## 🤖 Shared Software Can Manufacture Access At Scale

The September PaperCut campaign strengthens the case for treating some shared software as dependency infrastructure.

A likely Russian-speaking operator was reported to have used hundreds of AI agents to exploit PaperCut NG/MF vulnerabilities across hundreds of servers and organisations.

The campaign produced:

- credentials;
- operating-system and domain secrets;
- and privileged footholds.

This is not an Iran case.

Its infrastructure significance is structural.

It shows how one vulnerable product can generate access across:

- education;
- government;
- healthcare;
- industrial and energy organisations;
- finance;
- and other sectors.

The important distinction is:

```text
SHARED SOFTWARE
→ MASS ACCESS OPPORTUNITY

MASS ACCESS OPPORTUNITY
≠
ONE STRATEGIC CUSTOMER

but

MASS ACCESS OPPORTUNITY
→ MORE POSSIBLE DOWNSTREAM USERS
```

Shared software can therefore become infrastructure through concentration.

---

## 🛡️ Defence And Security Systems

Defence infrastructure includes obvious military systems:

- command and control;
- bases;
- logistics;
- weapons support;
- intelligence networks;
- personnel systems;
- communications;
- and defence contractors.

It also includes less visible dependencies:

- civilian airfields;
- commercial satellite services;
- cloud providers;
- ports;
- fuel supply;
- accommodation;
- transport;
- telecommunications;
- and outsourced administrative systems.

The public-private distinction is especially weak in defence.

A commercial supplier may hold data or operate a system whose compromise has direct military consequence.

But another distinction remains important:

> A civilian system supporting defence does not automatically become entirely military in legal character.

Shared or dual-use infrastructure requires more careful analysis than the functional inclusion test used by this pack.

The pack follows function and dependency.

Legal targeting analysis must go further.

---

## ⚓ Military Reconnaissance Can Reveal Civilian Dependencies Too

Anthropic's September disclosure concerning an Iran-nexus actor researching US naval movements, maritime VSAT, Cisco communications and industrial-control products illustrates another infrastructure boundary.

Military systems may rely on commercial or dual-use technologies.

That means:

```text
MILITARY FUNCTION
+
COMMERCIAL TECHNOLOGY
+
SHARED VENDOR
=
DEPENDENCY THAT CROSSES LEGAL AND ORGANISATIONAL BOUNDARIES
```

The reconnaissance itself does not establish exploitation.

It does show why infrastructure mapping must follow dependency rather than ownership.

---

## 🧍 People Are Part Of The Infrastructure

State systems are often discussed as though the data inside them is secondary to the machinery.

It is not.

The system has value because it contains information about people and because people rely on it.

That includes:

- identity;
- health;
- education;
- employment;
- legal status;
- family relationships;
- location;
- disability;
- safeguarding;
- political activity;
- and financial life.

Where data is stolen, the infrastructure incident does not end when the server is restored.

The effects may continue through:

- fraud;
- harassment;
- discrimination;
- stalking;
- coercion;
- intelligence exploitation;
- reputational damage;
- or interference by citizens and organisations inside the target country.

A state that restores the service but abandons the people exposed by the breach has restored only part of the infrastructure.

People also carry fallback.

When a system moves to manual operation, the cost may be absorbed by:

- clinicians and patients;
- engineers and operators;
- teachers, students and families;
- caseworkers and claimants;
- security staff and visitors;
- or communities asked to tolerate delay, uncertainty, travel, repeated disclosure, or reduced service.

The pack should record that burden, especially where high-dependency users cannot safely wait or substitute another service.

---

## 🤐 Silence Can Become An Infrastructure Failure

The response system is also part of state infrastructure.

Where an incident occurs, the state needs a way to:

- identify who owns the response;
- assess personal and systemic risk;
- coordinate across institutions;
- preserve evidence;
- notify affected people;
- provide protection;
- distinguish public from private disclosure;
- and issue an accountable written position.

A blanket refusal to confirm, deny, explain, or coordinate may protect some operational details.

Used as the entire response, it can expose a governance failure.

It may advertise that:

- no body will accept ownership;
- the affected person will be left alone;
- institutional seams can be exploited;
- public and private risk cannot be separated;
- and further harm can continue below the threshold at which the state acts.

The protection pathway is therefore not separate from cyber resilience.

It is part of it.

---

## 🧭 Alliance Systems Are Dependencies Too

The newer NATO and coalition question should be treated carefully.

NATO itself is not one technical infrastructure object.

But allied commitments, intelligence-sharing, basing, logistics and response assumptions can function as **coordination infrastructure**.

For Britain and the United States, this matters because:

```text
BASE ACCESS
+
INTELLIGENCE SHARING
+
LOGISTICS
+
JOINT ATTRIBUTION
+
POLITICAL COMMITMENT
=
COLLECTIVE CAPACITY
```

If one element becomes less reliable, the physical infrastructure may remain intact while the state has to spend more capacity recreating the same effect.

That makes alliance reliability a **dependency variable**.

It does **not** mean:

```text
NATO DISAGREEMENT
=
CYBER INCIDENT
```

or:

```text
ALLIANCE POLITICS
=
STATE INFRASTRUCTURE IN THE SAME SENSE AS A POWER GRID
```

The correct classification is narrower:

> alliance predictability is coordination infrastructure where essential defence and national-security functions depend on it.

That belongs in the dependency map, not the incident count.

---

## 🧬 Infrastructure Significance Can Emerge Through Clustering

Not every incident looks significant on its own.

The functional test should therefore be applied both to individual incidents and to patterns.

A cluster deserves additional scrutiny where it shows:

- several water systems affected;
- the same industrial controllers repeatedly targeted;
- several local utilities forced into manual operation;
- water and electricity disrupted in the same geography;
- telecommunications failure affecting several essential services;
- one supplier appearing across otherwise unrelated incidents;
- repeated access to systems capable of producing physical effect;
- or one shared platform appearing across several public functions.

The analytical progression may be:

```text
small local incident
→ repeated sector incident
→ shared dependency
→ cross-sector effect
→ national resilience problem
```

No individual event needs to collapse the state.

Infrastructure significance can emerge from accumulation.

But two propositions must remain separate:

```text
THE INCIDENTS COLLECTIVELY CREATE AN INFRASTRUCTURE PROBLEM
≠
THE INCIDENTS SHARE ONE OPERATOR, CUSTOMER, OR SPONSOR
```

Clustering can strengthen confidence in cumulative effect before it strengthens attribution.

The first conclusion requires evidence about dependencies and consequences.

The second requires evidence about provenance, technique, infrastructure, tasking, relationships, or other actor linkage.

---

## 🪞 Public Sympathy Is Not The Perimeter

Corporate legitimacy and public sympathy can affect how an incident is narrated, claimed, or politically received.

They do not decide whether a system is infrastructure.

A disliked company may operate a function on which water, energy, health, transport, payments, or defence depends.

A popular company may suffer a serious breach without any essential public function being affected.

The pack should therefore resist both shortcuts:

```text
UNPOPULAR VICTIM
=
NOT IMPORTANT
```

and:

```text
PROMINENT OR SYMPATHETIC VICTIM
=
ESSENTIAL INFRASTRUCTURE
```

Reputation may belong in the information-operations analysis.

Function, dependency, substitutability and consequence belong in the infrastructure classification.

---

## 🚫 What Does Not Automatically Belong

Not every cyber incident belongs in this pack.

An incident may remain outside where:

- it affects an ordinary commercial service with no essential public role;
- the disruption is trivial;
- there is no meaningful operational, data, physical or public consequence;
- the claim is unsupported;
- or the only connection is dramatic timing.

Pure website defacement may not qualify.

A stolen logo or embarrassing message may matter politically but not constitute infrastructure disruption.

Nor do the following automatically establish inclusion:

- a famous corporate name;
- an actor's claim of strategic importance;
- hostile rhetoric;
- wartime timing;
- an organisation appearing in an important sector;
- or the possibility that some undisclosed customer may have been affected.

Those facts may justify scrutiny.

The perimeter still requires a supported relationship between the affected system and a material public, social, operational, physical, data, decision or coordination consequence.

The inclusion test should ask:

```text
WHAT FUNCTION WAS AFFECTED?
WHO RELIED ON IT?
WHAT SYSTEM LAYER WAS REACHED?
WHAT MATERIAL CONSEQUENCE FOLLOWED?
WHAT OTHER SYSTEMS DEPENDED ON IT?
WHAT STATE OR SOCIAL CAPACITY WAS DEGRADED?
```

If those questions cannot be answered, the incident may not belong here.

---

## 📋 Infrastructure Record Template

Where useful, the pack should record infrastructure significance using:

```text
SECTOR:
PUBLIC FUNCTION:
OWNERSHIP:

PUBLIC AUTHORITY / FUNCTION OWNER:
COMMISSIONER / PAYER:
SERVICE OPERATOR:
TECHNICAL OPERATOR:
CONTRACTOR / SUPPLIER:
ACCESS PROVIDER:
END USER / BENEFICIARY:

HIGH-DEPENDENCY USERS:
SYSTEM LAYER:
INFRASTRUCTURE FORM — PHYSICAL / INFORMATION / DECISION / COORDINATION / DEPENDENCY:

ESSENTIAL DEPENDENCY:
UPSTREAM DEPENDENCIES:
DOWNSTREAM DEPENDENCIES:
SHARED PROVIDER / PLATFORM:
SHARED PRODUCT:
REMOTE-ACCESS RELATIONSHIP:

GEOGRAPHIC REACH:
EXPECTED DURATION:
SUBSTITUTABILITY:
ALTERNATIVE CAPACITY:

OPERATIONAL EFFECT:
PHYSICAL EFFECT:
DATA EFFECT:
DECISION EFFECT:
COORDINATION EFFECT:

MANUAL FALLBACK:
FALLBACK OWNER:
HUMAN / CAPACITY BURDEN:

ASSET INVENTORY QUALITY:
SEGMENTATION PRESENT:
SEGMENTATION HELD:
SUPPLIER COMPROMISE:
ACCESS TRANSFER POTENTIAL:

LOGISTICS PERIMETER LEVEL:
AFFECTED GOODS / SERVICES:
DOWNSTREAM ESSENTIAL-SERVICE EFFECT:

CIVILIAN / MILITARY / DUAL-USE STATUS:
CLAIMED ACTOR:
OFFICIAL ATTRIBUTION:
OTHER ATTRIBUTION:
COMMISSIONING / CUSTOMER EVIDENCE:
CONFIDENCE BY PROPOSITION:
RIVAL EXPLANATIONS:
IHL REVIEW NEEDED:

ALLIANCE / COORDINATION DEPENDENCY:
SOURCES:
LAST REVIEWED:
```

This helps prevent several different questions being collapsed into one.

In particular:

```text
belongs in this pack
≠
lawful target
≠
Iranian attack
≠
war crime
```

Each proposition needs its own evidence.

---

## 🧭 Working Rule

The working rule is:

> Include systems whose compromise materially affects governance, public safety, essential services, economic continuity, physical infrastructure, or the people whose data allows those systems to function.

That rule is deliberately broader than government ownership.

It is also narrower than including every large company or every cyberattack.

The perimeter follows consequence.

Map the function.

Map the dependency.

Map the roles.

Record how deep the incident reached, what alternative capacity existed, who absorbed continuity, and whether failure propagated through another system.

And where the system is civilian:

> Do not confuse strategic importance with loss of legal protection.

---

## 🧠 Current Perimeter — 14 September 2026

The newer incident set reinforces several propositions:

```text
SMALL LOCAL SYSTEM:
CAN BE ESSENTIAL INFRASTRUCTURE

PRIVATE COMPANY:
CAN OPERATE ESSENTIAL INFRASTRUCTURE

SHARED SOFTWARE:
CAN BECOME INFRASTRUCTURE THROUGH CONCENTRATION

SUPPLIER:
CAN BECOME INFRASTRUCTURE THROUGH DEPENDENCY

HOSPITAL FACILITY SYSTEM:
CAN BE PART OF CARE INFRASTRUCTURE

COURT PLATFORM:
CAN BE INFORMATION / DECISION INFRASTRUCTURE

TELECOMMUNICATIONS:
ARE CROSS-SECTOR DEPENDENCY INFRASTRUCTURE

ALLIANCE RELIABILITY:
CAN BE COORDINATION INFRASTRUCTURE
WITHOUT BECOMING A CYBER INCIDENT

LARGE CORPORATE BREACH:
IS NOT AUTOMATICALLY AN INFRASTRUCTURE EVENT
```

The defining question remains:

> **What function did society or the state rely on this system to perform?**

That is still the line.

---

## 🌌 Constellations

🏗️ 🚰 ⚡ 🏥 🏦 📡 🕸️ 🧭 — essential infrastructure; water; energy; health; banking; telecommunications; shared dependencies; coordination systems.

---

## ✨ Stardust

state infrastructure, critical infrastructure, essential services, public contractors, water, energy, health, hospital facility systems, education, banking, transport, logistics, telecommunications, government data, operational technology, shared software, suppliers, court systems, public function, dependency, substitutability, manual fallback, coordination infrastructure, alliance reliability, civilian protection

---

## 🏮 Footer

*🏗️ What Counts As State Infrastructure* is a living node of the **Polaris Protocol**.  
It defines the functional perimeter for incidents included in the *🇮🇷 Data Wars: IRGC Edition* timeline while keeping essential state function separate from lawful military targetability.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope and inclusion rules*
> - [🗺️ Who Iran Sees As Inside The War](./🗺️_who_iran_sees_as_inside_the_war.md) — *threat exposure without collapsing it into legal targetability*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *how limited incidents accumulate*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *operational technology, control systems and physical effects*
> - [⛴️ Do Ports Count?](./⛴️_do_ports_count.md) — *transport, logistics and dependency boundaries*
> - [🇬🇧 Britain Is Advertising An Exploitable Seam](./🇬🇧_britain_is_advertising_an_exploitable_seam.md) — *ownership, mitigation and alliance seams*
> - [🧅 The Operator May Not Know The Customer](./🧅_the_operator_may_not_know_the_customer.md) — *operator, intermediary, commissioner, payer and customer separation*
> - [🕸️ Attribution Is Not A Light Switch](./🕸️_attribution_is_not_a_light_switch.md) — *claim-level attribution and graded confidence*
> - [📰 How To Report Without Overclaiming](./📰_how_to_report_without_overclaiming.md) — *reporting the effect without upgrading the actor claim*
> - [📚 Sources And Evidence Register](./📚_sources_and_evidence_register.md) — *source provenance and evidence audit trail*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *separate legal analysis for wartime cyber operations*
> - [🏥 Health, Education And Admin Are Not Soft Extras](./🏥_health_education_and_admin_are_not_soft_extras.md) — *civilian systems as state function*
> - [🏦 Banks Are Part Of The Battlespace](./🏦_banks_are_part_of_the_battlespace.md) — *financial infrastructure and confidence*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *live incident chronology through 14 September 2026*
> - [🧬 One War, Many Threat Ecosystems](./🧬_one_war_many_threat_ecosystems.md) — *separating essential-function effects from shared-vulnerability and criminal exposure patterns*
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
