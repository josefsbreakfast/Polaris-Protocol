# 📥 Entry-Point Abuse in Automated Datasets  
**First created:** 2025-10-31  
*How local discretion and professional trust become attack surfaces inside national-scale automation.*

---

## 🛰️ Orientation  

**Entry-point abuse** is the moment a system of record mistakes authorisation for truth.  
Large research and security architectures rely on trusted local contributors — officers, contractors, analysts — to feed data upstream.  
Each contributor acts as both *witness* and *gatekeeper*.  
If even one abuses that privilege, the automation will faithfully replicate the lie.

> *When you trust the doorway too much, the lock becomes theatre.*

---

## 🧩 Key Features  

- **Discretionary access** — individuals or small teams with upload or referral rights.  
- **Professional trust** — status or clearance substitutes for verification.  
- **Referral gateways** — automated feeds that turn manual judgement into machine input.  
- **Schema inheritance** — downstream systems assume upstream validation.  
- **Accountability gap** — replication multiplies authority faster than oversight can follow.

---

## 🔍 Analysis  

### 1️⃣ Authorised entry  
In normal operation, ingestion systems accept structured submissions from recognised sources: local councils, research partners, contractors.  
Credentials verify *who* the user is, not *why* the entry is correct.  
The system records provenance but not motive.

### 2️⃣ Bad-faith use  
A local actor — angry, careless, or opportunistic — mislabels an entry, exaggerates a risk score, or inserts a name that doesn’t belong.  
Because the interface is routine, the action looks ordinary.  
Automation interprets it as *fact*.

### 3️⃣ Propagation  
Within hours, synchronisation pushes the record through mirrors and backups.  
Statistical tools ingest it for model-training; dashboards display it as part of a trend.  
By tomorrow, dozens of systems have seen it, none questioning the origin.

### 4️⃣ Discovery and accountability gap  
Audits can trace *where* a record came from but rarely *why* it was created.  
The log shows an authorised user acting within scope; intent is invisible.  
By the time the error is recognised, the actor may have left the role — leaving a phantom with credentials.

---

## ⚖️ Governance Implications  

Under the **Data Protection Act 2018** and **UK GDPR**, every data controller is responsible for ensuring that information collected is *accurate and obtained lawfully*.  
Delegating collection to local partners doesn’t transfer that duty.  
If an entry is malicious or negligent, liability travels upward with the data.

Ethically, entry-point abuse collapses the distinction between *mistake* and *manipulation*.  
A single falsified referral can alter allocation of funds, research direction, or even policing focus — yet remain invisible until audits surface it years later.

---

## 🛠 Counter-Measures  

| Layer | Preventive design |
|-------|-------------------|
| **Access control** | Dual sign-off for high-impact categories; rotate credentials; revoke on exit. |
| **Provenance tagging** | Every record stores “entered by / verified by / evidence type.” |
| **Automated expiry** | Unverified entries auto-delete after a review window. |
| **Audit rights** | Individuals can request inclusion provenance via SAR; regulators can compel disclosure. |
| **Cultural norm** | Treat data submission as authorship, not clerical work; make honesty reputationally safe. |

---

## 🌌 Constellations  

⚖️ 🧠 🛰️ 📥 — governance · cognition · automation · ingress  

---

## ✨ Stardust  

entry-point abuse · referral risk · ingestion integrity · provenance · front-door capture · discretionary power · trust architecture  

---

## 🏮 Footer  

*📥 Entry-Point Abuse in Automated Datasets* maps how good systems inherit bad intentions.  
It pairs with:  

- **📊 Crown-Service Flag and Metadata Drift** — how authority miscoding seeds confusion.  
- **📈 Escalation Drift in Complex Datasets** — how small entries amplify over time.  
- **🧠 Cognitive Feedback and Bureaucratic Amplification** — how belief protects bad data from deletion.  

> *Every system is only as honest as its first keystroke.*

---

**Last updated:** 2025-10-31  
