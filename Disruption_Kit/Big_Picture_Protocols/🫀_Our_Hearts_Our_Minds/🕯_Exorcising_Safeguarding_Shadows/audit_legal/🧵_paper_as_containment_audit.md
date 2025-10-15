# 🧵 Paper as Containment — Mega Node
**First created:** 2025-10-04 | **Last updated:** 2025-10-15  
*Digitise liberty, not just crime: closing the UK’s Court of Protection / DoLS blind spot.*  

---

### 🔗 Quick Links
- [Executive Summary](#exec)  
- [System Map (What Could “Britney” Look Like Here?)](#map)  
- [Policy-First Plan](#policy)  
- [Investigation-First Plan (Journalism & OSINT)](#investigation)  
- [Tight Audit Pool](#auditpool)  
- [MVP Digital Spine](#mvp)  
- [Efficiency & Cost-Out Frame](#efficiency)  
- [90-Day Policy Rollout](#90policy)  
- [90-Day Investigation Timeline](#90invest)  
- [Templates](#templates)  
- [Tracker Fields](#tracker)  
- [Legal & Ethical Guardrails](#guardrails)  
- [Glossary](#glossary)  
- [Appendix: Talking Points & One-liners](#appendix)  
- [Next Actions](#todo)  

---

## ✨ Executive Summary {#exec}
The UK runs central, digital systems for the *most sensitive* domains (CPS disclosure, PNC, NHS Spine). 

In contrast, the Court of Protection (CoP) and DoLS/LPS ecosystem remains paper-bound and locally siloed. 

That design gap enables delay, error, and quiet control — making a UK analogue of a high-control conservatorship plausible via procedural fog rather than celebrity spectacle.

**Thesis:** 

Treat adult-safeguarding liberty like patient safety or serious crime: build a minimal digital spine, rotate oversight, guarantee advocacy, and enforce deadlines. 

This is targeted, fast and pays back in efficiency *and* harm reduction.

---

## 🧭 System Map — What a “Britney Repeat” Looks Like Here {#map}
- **Modality:** Older/disabled adult under a deputyship (CoP) and/or DoLS/LPS authorisation.  
- **Control mechanics (non-actionable):** opaque authorisations, familiar gatekeepers, delay as leverage, sidelined family/advocacy.  
- **Why it hides:** closed jurisdictions, paper bundles, privacy optics, boundary disputes (County A/B/C), fractured accountability (LA/NHS/CoP).

---

## 🏛️ Policy-First Plan {#policy}

### Where the Gaps Live {#gaps}
| Gap | What it looks like | How it’s exploited | Red flags |
|---|---|---|---|
| **Paper & local silos** | Bundles, PDFs, unlinked spreadsheets | “Lost”/late renewals; no audit trail | Expiry slips; no single timeline |
| **Familiarity/capture** | Repeat pairings judge↔counsel | Soft pressure; low escalation appetite | No rotation; thin conflict logs |
| **Ambiguous responsibility** | County/NHS/LA handoff limbo | Everybody waiting on “the other” | Referrals with no outcome entries |
| **Weak advocacy coverage** | IMCA inconsistent | Person/family sidelined | No named advocate at key points |
| **Hidden conflicts** | LA constitutions create bottlenecks | Advice defends system over person | Complaints loop to same actors |

### 🎯 The Tight Audit Pool {#auditpool}
1. **Renewal ledger** — DoLS/LPS start & expiry, outcomes.  
2. **Deputyship accounts & visit notes** — timeliness + advocacy presence (sampled).  
3. **Conflict-of-interest registers** — officers, panels, external counsel.  
4. **Case-handoff logs** — cross-boundary transfer timelines.  
5. **Advocacy coverage** — IMCA appointment rates & reasons for non-appointment.  

### 🧰 MVP Digital Spine (12-month build, phased) {#mvp}
- Central, encrypted registry keyed on NHS Number: status, start date, expiry/renewal due, owning authority.  
- Tiered access (status vs details); immutable audit logs; API-ready after pilot.  
- Automated renewal alerts; boundary resolver (OS AddressBase) to kill County A/B disputes.  
- Phases: 1) upload-only dashboard; 2) bi-directional APIs; 3) CoP case-management hooks.  

**Dashboard Mock (fields & CSV schema):**

**Renewals CSV**  

```
case_id,nhs_number_hash,authority_code,start_date,expiry_date,renewal_status,assigned_owner,last_action_at
RX-24-001,a9c1e6…d2,NOTTS,2024-12-01,2025-12-01,PENDING,jsmyth,2025-09-20T14:22:03Z
RX-24-002,bc77a4…90,LEICS,2025-01-15,2025-07-15,OVERDUE,amurphy,2025-10-03T09:12:44Z
```

**Advocacy CSV**  

```
case_id,imca_required,imca_assigned,imca_org,imca_assigned_at,reason_not_assigned
RX-24-001,Y,Y,Voice&Choice,2025-08-02,
RX-24-002,Y,N,, , “family-declined; urgent clinical decision”
```

Default KPIs: % renewals on time; avg days overdue; % cases with IMCA; transfer SLA compliance; unresolved conflicts >30 days.

### 🔄 Governance & Oversight {#governance}
- **Rotating oversight:** external monitoring-officer pool; randomised judicial allocation pilots.  
- **Guaranteed advocacy:** default IMCA; reasons required to opt-out; advocate gets ledger visibility.  
- **Hard deadlines & escalation:** statutory SLAs; miss twice → automatic external review.  
- **Transparency:** publish anonymised audit summaries; machine-readable conflict registers.  

### 📈 Efficiency & Cost-Out (frame) {#efficiency}
- Duplicate-work reduction: 20–40% fewer repeat assessments.  
- Hearings/adjournments down: 10–15%.  
- Cycle-time: 1–2 weeks saved per case.  
- Downstream savings: fewer damages, fewer Ombudsman remedies.  

### 🗺️ 90-Day Policy Rollout {#90policy}
1. Days 0–15: pull current renewal ledger; draft DPIA; define SLAs.  
2. Days 16–45: CSV ingest dashboard + boundary resolver; publish conflict register.  
3. Days 46–75: run live; measure baseline cycle-time; IMCA by default.  
4. Days 76–90: publish anonymised results; invite NAO/ministerial scale-up.  

---

## 🕵️ Investigation-First Plan (Journalism & OSINT) {#investigation}

### Why this works
FOIs create documents; OSINT maps context; journalists turn delays/redactions into stories. 
Survivor-centred ethics make it credible.

### 90-Day Investigation Timeline {#90invest}
- **Days 0–7:** tracker; pick 2–3 councils + 1 trust; line up reporters.  
- **Days 8–21:** FOI Tranche 1 (renewal ledger, contracts, IMCA rates); OSINT sweep (contracts, Companies House, council minutes).  
- **Days 22–40:** FOI Tranche 2 (audits, performance notices); embargo pack with FOIs + anonymised cases.  
- **Days 41–60:** publish if evidence strong; if not, file internal reviews + prep ICO appeals.  
- **Days 61–90:** escalate to MP, Ombudsman, ICO; release dossier + timeline.

### Templates {#templates}
- **FOI — Renewal Ledger:** request ledger, renewal due, IMCA coverage.  
- **FOI — Contracts & KPIs:** contract, KPI reports, notices, subcontractors.  
- **FOI — Advocacy Coverage:** aggregate data on IMCA usage, reasons.  
- **Monitoring-Officer Complaint:** formal review of contract and conflicts.  
- **MP Brief:** “If we digitise murder evidence, we can digitise liberty.”  

### Tracker Fields {#tracker}
Target body | FOI title | Date filed | Due date | Status | Review | ICO appeal | Docs received | Redactions | Follow-up | OSINT links | Press status  

### Legal & Ethical Guardrails {#guardrails}
- Protect survivors/whistleblowers.  
- No doxxing or harassment.  
- Focus on institutions, not individuals.  
- Libel/DP check before publication.  

---

## 📚 Glossary {#glossary}
- **CoP:** Court of Protection  
- **DoLS/LPS:** Deprivation of Liberty Safeguards / Liberty Protection Safeguards  
- **IMCA:** Independent Mental Capacity Advocate  
- **LGSCO / NAO / DLUHC:** Oversight and audit bodies  

---

## 🧩 Appendix: Talking Points {#appendix}
- “If we can digitise murder evidence, we can digitise liberty.”  
- “Privacy isn’t secrecy: tiered access beats lost paper.”  
- “Rotation is an anti-capture device, not a luxury.”  
- “This is rights-level plumbing: unclog the pipes, restore flow.”  

---

## ✅ Next Actions {#todo}
1. File FOI Tranche 1 for 2 councils + 1 trust.  
2. Prototype CSV dashboard with renewal alerts.  
3. Prep MP brief with 90-day pilot plan.  
4. Line up local journalist for embargo when FOIs land.  

---
