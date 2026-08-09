# 🏗️ What Counts As State Infrastructure  
**First created:** 2026-08-01 | **Last updated:** 2026-08-09  
*The test is what the system does, not whether the organisation running it is formally part of the state.*  

---

## 🛰️ Orientation  

This pack uses a functional definition of state infrastructure.

The question is not simply:

> Is this system owned by the government?

The better question is:

> Would compromise, disruption, manipulation, or loss of this system materially interfere with the state's ability to govern or with ordinary social life?

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
- or access to it could provide a route from digital intrusion to physical effect.

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

For some systems, a further question matters:

```text
CAN CYBER ACCESS CHANGE
WHAT THE PHYSICAL SYSTEM DOES?
```

Where the answer is yes, the incident deserves additional analytical weight.

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

## 🏦 Banks, Payments, And Financial Confidence  

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
- and logistics supporting health, food, defence, and emergency response.

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

## 📡 Telecommunications And State Connectivity  

Telecommunications infrastructure includes:

- mobile networks;
- fixed-line networks;
- internet exchange;
- data centres;
- emergency communications;
- government networks;
- satellite services;
- cloud infrastructure;
- undersea and terrestrial connectivity;
- and the systems used to authenticate and route users.

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

## 🏢 Government Administration, Policing, And Justice  

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
- or repeated access to systems capable of producing physical effect.

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

---

## 🚫 What Does Not Automatically Belong  

Not every cyber incident belongs in this pack.

An incident may remain outside where:

- it affects an ordinary commercial service with no essential public role;
- the disruption is trivial;
- there is no meaningful operational, data, physical, or public consequence;
- the claim is unsupported;
- or the only connection is dramatic timing.

Pure website defacement may not qualify.

A stolen logo or embarrassing message may matter politically but not constitute infrastructure disruption.

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
OPERATOR:
SYSTEM LAYER:
ESSENTIAL DEPENDENCY:
UPSTREAM DEPENDENCIES:
DOWNSTREAM DEPENDENCIES:
OPERATIONAL EFFECT:
PHYSICAL EFFECT:
MANUAL FALLBACK:
SHARED CONTRACTOR OR TECHNOLOGY:
CIVILIAN / MILITARY / DUAL-USE STATUS:
IHL REVIEW NEEDED:
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

And where the system is civilian:

> Do not confuse strategic importance with loss of legal protection.

---

## 🌌 Constellations  

🏗️ 🚰 ⚡ 🏥 🏦 🕸️ ⚖️ — essential infrastructure; water; energy; health; banking; shared dependencies; civilian protection.

## ✨ Stardust  

state infrastructure, critical infrastructure, essential services, public contractors, water, energy, health, education, banking, transport, telecommunications, government data, operational technology, industrial control systems, public function, civilian infrastructure, international humanitarian law

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
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *operational technology, control systems, and physical effects*
> - [👾 Cyber War Crimes](./👾_cyber_war_crimes.md) — *separate legal analysis for wartime cyber operations*
> - [🏥 Health, Education And Admin Are Not Soft Extras](./🏥_health_education_and_admin_are_not_soft_extras.md) — *civilian systems as state function*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *live incident chronology*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-09_
