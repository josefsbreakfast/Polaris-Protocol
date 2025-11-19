# 📬 Why Old University Accounts Show Access Attempts  
**First created:** 2025-11-19 | **Last updated:** 2025-11-19  
*Understanding how SAR/FOI workflows, identity objects, and routine admin processes create the appearance of “account activity.”*

---

## Overview

Old university email accounts often show “access attempts,” “identity checks,” or other forms of log activity long after a student or staff member has left.

These events are rarely targeted, mysterious, or external.  
They reflect **routine administrative processes**, especially the high-friction workflows related to:

- SAR (Subject Access Requests)  
- FOI (Freedom of Information) handling  
- archival and retention schedules  
- account migrations  
- system audits  
- deletion queues  
- external contractors performing bulk searches  

This node provides a clear explanation of how and why these events occur, and why they appear around specific dates or institutional actions.

---

## 1. The Architecture: Identity Objects, Not People

Modern universities use identity-management systems such as:

- Azure Active Directory (Office365)  
- Google Workspace  
- On-prem AD forests  

When a student leaves, their **mailbox** may close,  
but their **identity object** often remains for:

- retention  
- compliance  
- auditability  
- legal reference  
- archival indexing  

This object can be “touched” without anyone reading emails.

Examples include:

- password hash verification  
- role cleanup  
- retention timer checks  
- bulk migrations  
- syncing operations  
- audit sweeps  

These all appear as “access events,”  
but they are **not** account use.

---

## 2. Why Access Spikes Occur Around SAR/FOI Dates

SAR and FOI processes require the institution to search for:

- emails sent to/from staff  
- communications relevant to a dispute  
- administrative correspondence  
- any data that may relate to the requester  

When the request involves a former student,  
IT is instructed to check:

1. Does the account still exist?  
2. Is there an archive mailbox?  
3. Are there backups?  
4. Does the identity object need to be reactivated for export?  
5. Is deletion paused under a legal hold?  

Common actions include:

- “open mailbox” in audit mode  
- export of metadata only (not content)  
- running a script over dormant accounts  
- reviewing retention policy status  

To the user, these appear as:

- login attempts  
- access failures  
- credential probes  
- activity pings  

But they are simply **SAR/FOI mechanics**.

---

## 3. The Role of External Contractors

Many UK universities outsource parts of:

- eDiscovery  
- SAR fulfilment  
- FOI triage  
- email export tooling  

Contractors often use:

- bulk search tools  
- service accounts  
- automated mailbox crawlers  
- script-based metadata extractors  

These produce:

- rapid sequences of failed logins  
- unusual IP addresses  
- short bursts of “access attempts”  
- activity at odd times (overnight batches)  

All of this is normal for bulk-processing tools.  
It does not represent personal access or monitoring.

---

## 4. How Account Migrations Generate False Signals

Universities periodically migrate systems:

- Office365 → new tenant  
- IMAP → Exchange  
- Exchange on-prem → Exchange Online  
- archive → cold storage  
- identity sync migrations

During migration windows:

- dormant accounts reactivate temporarily  
- credentials sync  
- passwords reset in bulk  
- status checks run automatically  
- metadata caches refresh  

These appear as:

- login attempts  
- mailbox “open” events  
- credential mismatches  
- duplicate sessions  

Again, not personal.  
Just **infrastructure doing infrastructure things**.

---

## 5. Interference From Old Devices or Credentials

If an old:

- laptop  
- phone  
- tablet  
- Outlook client  
- browser extension  
- forgotten session  

is still trying the university server,  
you’ll see:

- repeated failed logins  
- authentication pings  
- attempts via deprecated protocols (IMAP/POP)

This is common if:

- a device was stolen  
- a phone was wiped without removing accounts  
- an old backup contained cached credentials

This is noise, not access.

---

## 6. Why This Matters in Frankenstack Ecology

When access events cluster around:

- SARs  
- complaints  
- FOIs  
- institutional disputes  
- university governance failures  

…it can feel like something targeted is happening.

But emotionally loud timing does not imply intent.  
The Polaris perspective is:

> **Institutional noise becomes audible at the same time  
> the survivor is asking the system to look at itself.**

This creates a *perception* of surveillance  
when the underlying mechanism is simply:

- bureaucratic drag  
- legal compliance timing  
- misaligned systems  
- metadata churn  
- human admin sloppiness  

The harm is aesthetic, not conspiratorial.

---

## 🌌 Constellations  
Ledger, Archive, Pulse, Mirror — routine systems, dormant identities, administrative cadence, metadata reflection.

---

## ✨ Stardust  
sar workflows, foi searches, identity objects, azure ad, mailbox archives, migration noise, access logs, frankenstack ecology, institutional patterning

---

## 🏮 Footer  

*Why Old University Accounts Show Access Attempts* is part of the **Polaris Protocol’s** civic-admin diagnostics.  
It supports *🧠 Big_Picture_Protocols* and complements the tech-governance lineage in *🛰️ Metadata_Sabotage_Network*.  

It reframes “mysterious” access events as the predictable noise of large institutions under legal load, rather than targeted action.

*Survivor authorship is sovereign. Containment is never neutral.*  
_Last updated: 2025-11-19_
