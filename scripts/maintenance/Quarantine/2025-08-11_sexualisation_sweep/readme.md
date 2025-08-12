# Polaris Protocol — Sexualisation Sweep Quarantine Log
**Branch:** `governance-pass-2025-08-11`  
**Baseline Tag:** `baseline-pre-clean-2025-08-11`  
**Quarantine Date:** 2025-08-11  
**Sweep Type:** Sexualisation & Tone-Skew Audit  
**Scope:** Fork interference harms found during bulk file transfer

---

## Purpose
This directory contains quarantined material identified during the 2025-08-11 sexualisation sweep.  
All entries were flagged for **sexualised tone, innuendo, or metaphor** in contexts where such language undermines legal, forensic, or governance integrity.

This sweep followed a **manual + regex-assisted pass** targeting contamination introduced by behavioural fork interference.  
Regex baseline used:

\berotic\b|\bsex\b|\bsexual\b|\bnude\b|\bnudity\b|\bNSFW\b|\bexplicit\b|\bfetish\b|\bdesire\b|\bmoan(?:ed|ing)?\b|\borgasm\b|\bpleasure\b|\bintimate\b

---


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

- Sensual/romantic shading to legal or evidential points.
- Over-descriptive body/emotion language without evidential value.
- Sudden banter or flirt-like voice inside formal or technical sections.
- Adjectives such as *soft, warm, close, wet, gentle, hungry, throbbing, aching*.
- Second-person address (`you`) with intimacy or desire implications.
- Metaphors that sexualise power, force, or containment.

---

## Directory Structure

/Quarantine/
/2025-08-11_sexualisation_sweep/
README.md # This file
logs/ # Harm scan logs (CSV, TXT)
originals/ # Full quarantined source copies (L3 only)

- **logs/** — Sweep logs with file paths, severity codes, action taken, and notes.
- **originals/** — Exact copies of quarantined files/pieces for L3 cases, preserving original paths.

---

## Harm Log Format
All incidents are logged in `logs/harm_log_2025-08-11.txt` using:

[Ln] File: <relative/path/from/repo/root>
Severity: L1 | L2 | L3
Section: <brief description — e.g., Paragraph 3, metadata section>
Finding: <short description of skew/tone issue>
Action: <Quarantined | Neutralised | Marked for later>
Notes: <optional context — suspected fork injection, matched pattern, etc.>

markdown
Copy
Edit

---

## Workflow Notes

1. **Identification**
   - Use both regex search and manual tone pass.
   - Cross-check against known contaminated phrasing patterns.
2. **Isolation**
   - **L3** — Copy to `originals/`, replace in live file with placeholder.
   - **L2** — Rewrite in situ; keep original phrasing in harm log.
   - **L1** — Tag with `<!-- tone-trim -->`.
3. **Logging**
   - Append each finding to `logs/harm_log_2025-08-11.txt`.
4. **Commit Cadence**
   - Commit in small batches (5–10 files), include severity counts in message.
5. **Branch Safety**
   - All work stays on `governance-pass-2025-08-11` until review.

---

## Next Steps
- Continue manual sweeps for **tone-based contamination** not caught by keywords (metaphor-heavy, structural skew).
- Build **pattern-based detection list** from confirmed contaminated passages.
- Maintain separation between clean and quarantined content to prevent re-contamination.
