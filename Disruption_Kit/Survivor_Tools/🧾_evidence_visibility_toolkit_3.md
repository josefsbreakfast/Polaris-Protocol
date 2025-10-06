# 🧾 Evidence & Visibility Toolkit  
**First created:** 2025-09-16 | **Last updated:** 2025-09-27  
*Practical templates: support emails, public timelines, and visibility test protocols.*

---

## 1. Neutral Support Email Template

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

---

## 2. Redacted Public Timeline Template

```
- YYYY-MM-DD HH:MM UTC — Observed sudden drop in reach for Post A. Screenshot: s1.png.  
- YYYY-MM-DD HH:MM UTC — Identical post from control account; normal reach. Screenshot: s2.png.  
- YYYY-MM-DD HH:MM UTC — Contacted platform; no substantive reply.  
Evidence: `evidence_[date].zip`
```

---

## 3. Visibility Test Checklist
- Create clean control account.  
- Prepare neutral test post + unique nonsense token.  
- Post simultaneously from main + control.  
- Record URLs, metrics after 24h/48h.  
- Repeat 2–3 times at different times.  
- Save screenshots, log in `visibility_tests.csv`.

---

## 4. visibility_tests.csv Template

```csv
run_id,date,platform,main_account,main_post_url,control_account,control_post_url,token_phrase,24h_reach_main,24h_reach_control,48h_reach_main,48h_reach_control,notes
1,2025-09-16,PlatformX,@main,https://platformx/post/123,@control,https://platformx/post/456,#mellifluous-cactus-8271,120,320,150,360,"main low vs control normal"
```

---

## 🏮 Footer
*Evidence & Visibility Toolkit* is a living node of the Polaris Protocol.  
It consolidates templates for correspondence, public redaction, and visibility testing.

> 📡 Cross-references:  
> - [Survivor Tools](../Survivor_Tools/)  
> - [Field Logs](../Field_Logs/)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-09-27_
