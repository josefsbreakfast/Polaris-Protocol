# ⚰️ Death Review Integrity Audit  
**First created:** 2025-10-04 | **Last updated:** 2025-10-15  
*Audit protocol for detecting suppression, bias, and procedural irregularities in death-review and coroner referral processes.*  

---

## 🚨 Evidence-Preservation Directive  

When credible suspicion arises that identity tokens or medical-record data have been tampered with, **immediate preservation of evidence** is mandatory.  
Without a full freeze on logs and audit trails, retrospective analysis becomes impossible.

1. **Issue a Legal Hold** — under the Public Records Act, NHS Digital Information Governance, and statutory inquiry rules.  
   - Apply to: NHS Spine, SCR, local EHRs, backup mirrors, audit logs.  
   - Suspend merges, deduplication, and deletions.  

2. **Notify Data Controllers and Caldicott Guardians** that affected records are potential evidence in a patient-safety investigation.  

3. **Snapshot and Hash** all systems under hold (WORM storage, immutable backups).  

4. **Chain-of-Custody Register** — record who initiated the hold, when, and by what authority.  

5. **Alert Oversight Bodies:** CQC, MHRA, Coroner Service, and NHS England Safety Investigations.  

6. **Protect Whistle-blowers and Families:** no retaliation, no access revocation, transparent communication of investigation status.

---

## ⚙️ Structural Process Audit  

The audit tracks how deaths move through **notification → review → coroner/inquest → closure**, identifying points where scrutiny may be suppressed or diverted.

### **A. Process Mapping**  
- Document the explicit and informal rules for referral to Coroner, Coronet, and Post-mortem.  
- Note who exercises discretion to downgrade cases and any variability between trusts or regions.  

### **B. Aberrant Process Detection**  
- Flag cases meeting mandatory criteria (sudden, unexplained, within 24 h of surgery/admission) that did **not** trigger review.  
- Compare discharge letters and condolence correspondence for **nudge language** (“We understand you may wish to proceed quickly with funeral arrangements”).  
- Record when families were **not informed** of their rights to post-mortem or inquest.  

### **C. Cultural & Religious Context**  
- Examine whether religious or cultural obligations (Muslim, Jewish, Sikh, Hindu, etc.) were used to justify *skipping scrutiny*.  
- Check if culturally-appropriate alternatives—rapid post-mortem followed by same-day burial—were offered.  
- Determine if “quick release” pathways were disproportionately applied to racialised or politicised families.  

---

## ⚖️ Structural Concentration & Bias Lens  

Token-switching and procedural downgrades are rarely random.  
Early indicators show concentration among **racialised populations** and **politically profiled individuals** (e.g., pro-Palestine supporters).  

These deaths risk being normalised because:  
- Diagnostic credibility is racially biased.  
- Reduced life-expectancy baselines disguise early mortality.  
- Review intensity is lower for non-white patients.

**Audit Requirements:**  
1. Bias-stratified sampling; minority and activist-adjacent cases receive full review.  
2. Disaggregate results by ethnicity, religion, and social index of deprivation.  
3. Report not just *how many* anomalies occurred, but *whose* records were affected.  

---

## 🧩 Linkage with Token-Switching Audit  

Each suspicious death should be cross-referenced with the live **🛰️ NHS Token-Switching Integrity Audit**:  
- Did the patient’s SCR or EHR show recent identifier anomalies?  
- Were allergy or blood-group fields altered prior to death?  
- Was a merge or deduplication event logged within 30 days of the incident?  

Scoring framework:  

| Dimension | 0 | 1 | 2 | 3 | 4 | 5 |
|------------|---|---|---|---|---|---|
| Record Integrity | None | Minor mismatch | Moderate | Major anomaly | Confirmed switch | Confirmed falsification |
| Process Integrity | None | Delay | Omission | Bypass | Active suppression | Coerced suppression |

**Combined “Suppressed-Scrutiny Index” = (Record + Process) / 2**

---

## 🧭 Ethical Prioritisation  

Under medical ethics and emergency-response doctrine:  
- **Priority 1 — Protect the living.**  Halt ongoing token-switching and restore integrity in active patient records.  
- **Priority 2 — Preserve evidence for the dead.**  Freeze and secure all logs.  
- **Priority 3 — Audit retrospectively** once live risk is contained.  

This sequencing aligns with the principles of beneficence, non-maleficence, and proportionality in incident triage.

---

## 🌌 Constellations  

🧿 ⚰️ 🕯️ 💉 — Forensic ethics, medical governance, and systemic bias containment.  

---

## ✨ Stardust  

death review, evidence preservation, coroner process, token switching, NHS spine, SCR, medical racism, cultural bias, suppressed scrutiny, patient-safety governance  

---

## 🏮 Footer  

*Death Review Integrity Audit* is a living node of the Polaris Protocol.  
It defines procedures for preserving evidence and detecting suppression in medical death-review systems, complementing the live-risk *NHS Token-Switching Integrity Audit.*  

> 📡 Cross-references:  
> - [🛰️ NHS Token-Switching Integrity Audit](./🛰️_nhs_token_switching_integrity_audit.md) — priority live-risk containment  
> - [🕯 Exorcising Safeguarding Shadows / 🛰 Token Switching Audit](./)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-15_
