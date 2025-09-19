# Git Intake Drawer — README (purpose & governance)

## Purpose
The Git intake drawer is a staging area for nodes, drafts, and artifacts that may:
- Be vulnerable to device-level interference (e.g., mass-deletion, tampering), or
- Contain outputs that exhibit anomalous generation behavior (e.g., sexualized content, defamatory assertions, personal-identifying information).

It offers the author a controlled path to record material publicly while retaining review and mitigation controls before formal publication.

## Key Principles
1. **Assume risk.** Anything in this drawer should be treated as potentially risky. Review/cleanup should be prioritized.
2. **Minimize exposure.** Avoid linking or amplifying content from here; reference intake issue numbers instead.
3. **Scheduled review.** The author will perform intake reviews on a regular cadence (recommendation: 48–72 hours after submission, then weekly until cleared). If a second reviewer is available, add a sign-off.
4. **Redaction-first.** Prioritize removal/redaction of PII, business names, or sexualized/personalized content before transfer to main repo.
5. **Sanitized logs.** Keep minimal, privacy-respecting logs to aid triage; do not store full unredacted raw dumps in plaintext.

## How to use
- Upload drafts to `intake/` with a short manifest (title, author, date, sensitivity-tags).
- Open an intake issue and assign label `intake-waiting`.
- During review, if content is safe, move to `ready-for-review`; otherwise, `intake-quarantine` and redact.

## Legal presumption
Presence in the intake drawer is not an admission of wrongdoing by the author or any third party. It is an operational stance: a place to hold material suspected to be prone to interference or anomalous content generation, prioritized for removal/redaction if it contains defamatory or identifying details.
