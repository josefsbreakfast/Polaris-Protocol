# 🏗️ What Counts As State Infrastructure?  
**First created:** 2026-08-01 | **Last updated:** 2026-08-07  
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
- and private organisations performing public functions.

A privately owned system may therefore be part of the state's essential infrastructure.

The issue is function, dependency, and consequence.

Not branding.

---

## 🧭 The Functional Test  

A system belongs inside this pack where one or more of the following is true:

- the state relies on it to deliver an essential public function;
- ordinary life cannot continue normally without it;
- its failure would create a serious public-safety risk;
- its data is necessary for government, care, justice, education, or economic participation;
- it supports defence, emergency response, or national decision-making;
- it is a critical dependency for another essential system;
- or compromise would create substantial coercive, intelligence, or destabilising value.

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
state infrastructure
```

---

## 🚰 Water And Wastewater  

Water is one of the clearest examples.

Relevant systems include:

- drinking-water treatment;
- pumping and pressure control;
- reservoirs;
- wastewater treatment;
- sewage management;
- industrial control systems;
- remote monitoring;
- laboratory data;
- customer and site records;
- and emergency fallback arrangements.

An attack does not need to contaminate the water supply to matter.

Operational harm may include:

- altered settings;
- loss of pressure;
- flooding;
- system lockout;
- movement to manual operation;
- delayed treatment;
- increased staffing requirements;
- or loss of confidence in whether readings can be trusted.

Manual operation is resilience.

It is also evidence that the digital system has been degraded.

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
- billing and balancing systems;
- and the telecommunications supporting them.

An attack may aim to:

- interrupt supply;
- damage equipment;
- create unsafe conditions;
- force manual operation;
- obtain technical intelligence;
- pre-position for later disruption;
- or demonstrate access without immediately using it.

The absence of a blackout does not mean the operation lacked strategic value.

Persistent access may matter more than immediate spectacle.

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
- and pressure on already stretched services.

Medical supply chains also belong inside the perimeter where their failure affects the practical delivery of care.

The fact that the affected body is a company does not remove the public-health consequence.

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
- and communications linking individuals to public institutions.

They also support:

- schools;
- universities;
- student finance;
- qualifications;
- teacher administration;
- public grants;
- and international programmes.

A breach may not close every school.

It may still remove large quantities of sensitive public data from state custody and create lasting intelligence, fraud, coercion, or targeting value.

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
- and central-bank dependencies.

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
- and logistics supporting health, food, defence, and emergency response.

Disruption may affect:

- movement of people;
- movement of goods;
- military logistics;
- emergency services;
- food and medicine supply;
- industrial production;
- or evacuation and civil protection.

Transport systems are also highly dependent on telecommunications, energy, payments, and software suppliers.

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
- and the systems used to authenticate and route users.

It supports almost every other sector in this node.

A telecommunications incident may:

- interrupt service;
- expose location or identity data;
- enable interception;
- degrade emergency response;
- isolate public bodies;
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
- and outsourced administrative systems.

The public-private distinction is especially weak in defence.

A commercial supplier may hold data or operate a system whose compromise has direct military consequence.

This pack therefore follows function and dependency rather than limiting itself to formal military ownership.

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
- or prevents a person from obtaining an accountable state response.

Administrative data is not a bureaucratic side issue.

It is part of how the state recognises people, assigns rights, records risk, and exercises power.

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
- or represents a single point of failure.

Relevant examples may include:

- cloud providers;
- managed-service companies;
- help-desk platforms;
- identity-verification systems;
- medical suppliers;
- transport software;
- payment processors;
- and specialist defence or security firms.

The correct question is not:

> Is the contractor technically part of government?

It is:

> What public function becomes unavailable, unsafe, unreliable, or exposed if this contractor fails?

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
- and issue an accountable written position.

A blanket refusal to confirm, deny, explain, or coordinate may protect some operational details.

Used as the entire response, it can expose a governance failure.

It may advertise that:

- no body will accept ownership;
- the affected person will be left alone;
- institutional seams can be exploited;
- and further harm can continue below the threshold at which the state acts.

The protection pathway is therefore not separate from cyber resilience.

It is part of it.

---

## 🚫 What Does Not Automatically Belong  

Not every cyber incident belongs in this pack.

An incident may remain outside where:

- it affects an ordinary commercial service with no essential public role;
- the disruption is trivial;
- there is no meaningful operational, data, or public consequence;
- the claim is unsupported;
- or the only connection is dramatic timing.

Pure website defacement may not qualify.

A stolen logo or embarrassing message may matter politically but not constitute infrastructure disruption.

The inclusion test should ask:

```text
WHAT FUNCTION WAS AFFECTED?
WHO RELIED ON IT?
WHAT MATERIAL CONSEQUENCE FOLLOWED?
WHAT STATE OR SOCIAL CAPACITY WAS DEGRADED?
```

If those questions cannot be answered, the incident may not belong here.

---

## 🧭 Working Rule  

The working rule is:

> Include systems whose compromise materially affects governance, public safety, essential services, economic continuity, or the people whose data allows those systems to function.

That rule is deliberately broader than government ownership.

It is also narrower than including every large company or every cyberattack.

The perimeter follows consequence.

---

## 🌌 Constellations  

🏗️ 🚰 ⚡ 🏥 🏦 — essential infrastructure; water; energy; health; banking and public continuity.

## ✨ Stardust  

state infrastructure, critical infrastructure, essential services, public contractors, water, energy, health, education, banking, transport, telecommunications, government data

---

## 🏮 Footer  

*🏗️ What Counts As State Infrastructure* is a living node of the **Polaris Protocol**.  
It defines the functional perimeter for incidents included in the *🇮🇷 Data Wars: IRGC Edition* timeline.

> 📡 Cross-references:
>
> - [🇮🇷 Data Wars: IRGC Edition](./README.md) — *root orientation and pack map*
> - [🧭 What This Pack Is Tracking](./🧭_what_this_pack_is_tracking.md) — *scope and inclusion rules*
> - [📉 Small Disruptions Can Make A Campaign](./📉_small_disruptions_can_make_a_campaign.md) — *how limited incidents accumulate*
> - [🚰 When Cyber Reaches The Machinery](./🚰_when_cyber_reaches_the_machinery.md) — *operational technology and physical systems*
> - [🏥 Health, Education And Admin Are Not Soft Extras](./🏥_health_education_and_admin_are_not_soft_extras.md) — *civilian systems as state function*
> - [⏱️ Timeline Of Essential Infrastructure Attacks](./⏱️_timeline_of_essential_infrastructure_attacks.md) — *live incident chronology*

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2026-08-07_
