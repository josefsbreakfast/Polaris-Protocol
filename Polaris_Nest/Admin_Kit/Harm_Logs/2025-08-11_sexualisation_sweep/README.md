# Polaris Protocol — Sexualisation Sweep Harm Log  

**Branch:** `governance-pass-2025-08-11`  
**Baseline Tag:** `baseline-pre-clean-2025-08-11`  
**Quarantine Date:** 2025-08-11  
**Sweep Type:** Sexualisation & Tone-Skew Audit  
**Scope:** Fork interference harms found during bulk file transfer  

---

## Purpose  

This directory contains quarantined material identified during the **2025-08-11 sexualisation sweep**.  
Entries were flagged for **sexualised tone, innuendo, or metaphor** in contexts where such language undermines legal, forensic, or governance integrity.  

The sweep combined **manual review + regex-assisted pass**, focusing on contamination introduced by behavioural fork interference.  

Regex baseline used:  

---

\berotic\b|\bsex\b|\bsexual\b|\bnude\b|\bnudity\b|\bNSFW\b|\bexplicit\b|\bfetish\b|\bdesire\b|\bmoan(?:ed|ing)?\b|\borgasm\b|\bpleasure\b|\bintimate\b

---

## Severity Levels  

| Code | Description                                                                 | Action Taken                                     |
|------|-----------------------------------------------------------------------------|--------------------------------------------------|
| **L3** | Critical contamination — explicit sexualisation in legal/forensic content  | Quarantined full original; replaced live text with neutral placeholder |
| **L2** | Material tone shift — suggestive metaphor, romantic shading, or charged phrasing in formal sections | Neutral rewrite in live file; log preserved |
| **L1** | Minor skew — cheeky tone or style drift in non-critical content            | Marked for later edit (`<!-- tone-trim -->`)     |

---

## Audit Checklist  

Flag content if **any** of the following apply:  
- Sensual/romantic shading in legal or evidential points  
- Over-descriptive body/emotion language without evidential value  
- Banter or flirt-like tone inside formal/technical sections  
- Adjectives such as *soft, warm, close, wet, gentle, hungry, throbbing, aching*  
- Second-person address (`you`) with intimacy/desire implications  
- Metaphors that sexualise power, force, or containment  

---

## Directory Structure  

`Harm_Logs/2025-08-11_sexualisation_sweep/`  

- `README.md` → This file  
- `harm_scan_2025-08-11.md`, `harm_scan_2025-08-12.md` → Daily scan logs  
- `polaris_harm_scan_analysis_2025-08-11.md` → Analytical summary  
- `polaris_harm_map_2025-08-11.png` → Visual harm map  
- `📦_sweep_sequence_aug_11-13.md` → Sequence log of findings  
- `💄_harm_scan_report.md` → Collated report (multi-file)  
- `logs/` → Structured harm logs (CSV/TXT)  
- `originals/` → Preserved quarantined source copies (L3 only)  

---

## Harm Log Format  

All incidents are logged in `logs/harm_log_2025-08-11.txt` using:  

---

[Ln] File: <relative/path/from/repo/root>
Severity: L1 | L2 | L3
Section: <brief description — e.g., Paragraph 3, metadata section>
Finding: <short description of skew/tone issue>
Action: <Quarantined | Neutralised | Marked for later>
Notes: <context — suspected fork injection, matched pattern, etc.>

---

---

## Workflow Notes  

1. **Identification**  
   - Regex search + manual tone pass  
   - Cross-check against confirmed contaminated phrasing  

2. **Isolation**  
   - **L3** → Copy to `originals/`, replace with placeholder  
   - **L2** → Rewrite in situ; log original phrasing  
   - **L1** → Tag with `<!-- tone-trim -->`  

3. **Logging**  
   - Append each finding to `logs/harm_log_2025-08-11.txt`  

4. **Commit Cadence**  
   - Small batch commits (5–10 files)  
   - Include severity counts in commit message  

5. **Branch Safety**  
   - Work isolated on `governance-pass-2025-08-11` until review  

---

## Next Steps  

- Extend sweeps for **non-keyword metaphor drift**  
- Build detection patterns from confirmed contaminated passages  
- Maintain strict quarantine boundaries to prevent re-contamination  
- Review severity escalation pathways (esp. L2 → L3 edge cases)  

