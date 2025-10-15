# 📄 Emergency Legal Hold Notice  
**First created:** 2025-10-04 | **Last updated:** 2025-10-15  
*Immediate instruction to preserve all potentially compromised medical-record data and audit logs.*

---

## 🧭 Purpose  

To prevent loss, alteration, or overwriting of evidence while integrity audits are active across the NHS Spine, SCR, and local EHR systems.  
This directive implements the evidence-preservation obligations of the Public Records Act, NHS Digital IG policy, and statutory inquiry protocols.

---

## ⚡ Immediate Orders  

1. **Freeze data states**  
   - Suspend deletion, merge, deduplication, and reconciliation scripts touching live identifiers.  
   - Apply to all instances: NHS Spine, Summary Care Record, local EHRs, backups, and audit servers.  

2. **Secure immutable snapshots**  
   - Create WORM (write-once-read-many) backups of each affected dataset.  
   - Hash and timestamp each snapshot for verification.  

3. **Register the hold**  
   - Each Trust Data Controller must file a “Legal Hold Register” entry including:  
     - Date/time of hold  
     - Systems affected  
     - Responsible officer  
     - Authorising body  

4. **Notify oversight bodies**  
   - Caldicott Guardians, CQC, MHRA, Coroner Service, and NHS England Patient-Safety Division.  

5. **Suspend related data-migrations**  
   - No synchronisation, replication, or cloud export until forensic clearance is issued.  

6. **Preserve audit logs**  
   - Store separately under cryptographic seal.  
   - Any modification constitutes evidence tampering.  

7. **Communicate transparently**  
   - Inform staff and contracted partners that data are under investigation.  
   - Protect whistle-blowers and clinicians who raise integrity concerns.

---

## 🧾 Authority & Duration  

This legal hold remains in effect **until written release** by the designated forensic lead or statutory-inquiry chair.  
All actions must be logged under the chain-of-custody register.

---

## 🌌 Constellations  

🕯️ 📄 🛰️ 🧿 — Emergency containment, evidential integrity, governance freeze.  

---

## ✨ Stardust  

legal hold, evidence preservation, NHS spine, SCR, data integrity, audit logs, patient safety, governance freeze, forensic chain of custody  

---

## 🏮 Footer  

*Emergency Legal Hold Notice* is an administrative node of the Polaris Protocol.  
It provides the immediate containment directive supporting both the *NHS Token-Switching Integrity Audit* and the *Death Review Integrity Audit.*

> 📡 Cross-references:
> 
> - [🛰️ NHS Token-Switching Integrity Audit](./🛰️_nhs_token_switching_integrity_audit.md)  
> - [⚰️ Death Review Integrity Audit](./⚰️_death_review_integrity_audit.md)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-15_
