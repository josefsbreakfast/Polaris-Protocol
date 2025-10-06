# 🧾 Evidence & Visibility Toolkit  
**First created:** 2025-09-16 | **Last updated:** 2025-10-05  
*Practical templates and audit tools for correspondence, public documentation, and visibility testing.*

---

## 🌍 Purpose  

When a post, account, or project is shadow-muted, the burden of proof usually falls on the suppressed.  
This toolkit consolidates lightweight, **forensic templates** to help survivors gather verifiable evidence and maintain visibility integrity across platforms.  
Each format preserves metadata, timestamps, and tone neutrality suitable for public or legal submission.  

It also recognises that not everyone works digitally: **paper, handwriting, and low-tech records count.**  
If you need to print this and fill it in by hand, do it. Scanned or photographed later is fine — the goal is *traceable evidence you control.*  

---

## 1️⃣ Neutral Support Email Template  

```
Subject: Quick question about moderation/visibility action on [DATE]

Hello [Support / Trust & Safety],

On [DATE TIME UTC] my account/post [@handle or post URL] appeared to have reduced visibility.

Could you confirm:
1) Whether an automated action was applied?  
2) What the appeal/review route is?

Thank you,  
[Name / handle]
```

🪶 *Purpose:* Minimal emotional loading, maximises audit trail integrity.  
Use exact timestamps and URLs. Never phrase as accusation; request clarity.

---

## 2️⃣ Redacted Public Timeline Template  

```
- YYYY-MM-DD HH:MM UTC — Observed sudden drop in reach for Post A. Screenshot: s1.png.  
- YYYY-MM-DD HH:MM UTC — Identical post from control account; normal reach. Screenshot: s2.png.  
- YYYY-MM-DD HH:MM UTC — Contacted platform; no substantive reply.  
Evidence: `evidence_[date].zip`
```

🪶 *Purpose:* Enables public accountability without exposing sensitive metadata.  
Treat as an **external-facing transparency log** rather than a complaint.

---

## 3️⃣ Visibility Test Checklist  

- Create clean control account.  
- Prepare neutral test post + unique nonsense token.  
- Post simultaneously from main + control.  
- Record URLs, metrics after 24h / 48h.  
- Repeat 2–3 times at different intervals.  
- Save screenshots; log results in a structured table.

🪶 *Purpose:* Generates side-by-side metrics to demonstrate differential suppression between your main and control accounts.

---

### ⚠️ Integrity Note  

Automated visibility-audit tools and browser scripts can help — but they also create **new attack surfaces**.  
We’ve repeatedly seen scripts, dashboards, or scraping bots quietly **alter or misreport figures**: a single digit shift in impressions, reach, or timestamp is enough to discredit an entire dataset.  

That’s why this toolkit recommends **manual or semi-manual collection** — screenshots, CSV rows, and visible timestamps you control directly.  
It’s slower, but it’s harder to corrupt.  

This is also a standing **open call to independent developers, ethical hackers, and data-forensics volunteers**:  
design secure, offline-verifiable tools for visibility testing that ordinary users can trust.  
We shouldn’t need to code to prove we’re being silenced — but right now, we do.  

If that’s too technical — use pen and paper. Print this, fill it in, and photograph it.  
**A scrawled log is still evidence.**  

---

### Example Visibility Log Table  

| run_id | date | platform | main_account | main_post_url | control_account | control_post_url | token_phrase | 24h_reach_main | 24h_reach_control | 48h_reach_main | 48h_reach_control | notes |
|--------|-------|-----------|---------------|----------------|------------------|-------------------|----------------|----------------|------------------|----------------|------------------|-------|
| 1 | 2025-09-16 | PlatformX | @main | https://platformx/post/123 | @control | https://platformx/post/456 | #mellifluous-cactus-8271 | 120 | 320 | 150 | 360 | main low vs control normal |

🪶 *Tip:* Use a unique nonsense token (`#mellifluous-cactus-8271`) to identify your paired posts easily in searches or logs.

---

## 5️⃣ Escalation Chain Template  

```
1. Platform → initial contact (Trust & Safety)
2. Platform → formal appeal (include evidence.zip)
3. Regulator or ombudsman (if available)
4. Public redacted summary post (optional)
5. Archival upload to neutral repository
```

🪶 *Purpose:* Keeps escalation proportional and traceable.  
Each stage should be timestamped and mirrored in a second channel (email + post).

---

## 6️⃣ Data-Integrity Snapshot  

```
$ sha256sum evidence_2025-09-16.zip > evidence_2025-09-16.hash.txt
```

🪶 *Purpose:* Prevents post-tampering disputes by securing a cryptographic digest.  
Store hash separately in a trusted location.

---

## 🌌 Constellations  

🧾 🧿 🛰️ 🔮 — Sits in the **diagnostic + refusal** constellation, where forensic calm resists gaslighting.  
Bridges **Disruption_Kit → Survivor_Tools** and **Metadata_Sabotage_Network → Evidence_And_Anomalies.**

---

## ✨ Stardust  

shadowbanning, visibility testing, metadata suppression, forensic evidence, survivor tools, digital rights, platform accountability, audit trail, counter-nudge, public documentation

---

## 🏮 Footer  

*Evidence & Visibility Toolkit* is a living node of the Polaris Protocol.  
It consolidates survivor-facing templates for correspondence, redaction, and platform visibility testing, preserving both clarity and sovereignty of authorship.  


*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-05_
