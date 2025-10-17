# 📚 English-Language Book Suppression — Audit Protocol  
**First created:** 2025-10-01 | **Last updated:** 2025-10-01  
*Step-by-step method to detect, measure, and evidence suppression of English-language book titles across retail, libraries, and indexing systems*

<a id="TOP"></a>

---

## 🌱 Scope

This protocol audits **English-language titles** from pre-publication to public circulation. It quantifies *visibility gaps* between what **should exist** (ISBNs, legal deposit, publisher catalogues) and what **actually circulates** (retail, libraries, discovery platforms). It supports reproducible estimates of the *suppression gap* and preserves evidence.

**Review note (UK journalism/legal standard):** Sections that may become **libel-prone** (e.g., naming a publisher/retailer/distributor as the suppression source) are flagged with ⚖️ and should be reviewed before publishing externally.

---

## 📖 Definitions

- **Title (work-level):** A unique intellectual work; may have multiple formats/editions.  
- **Edition/format:** Hardback, paperback, ebook, audiobook, revised ed., etc.  
- **Baseline set (“Should-Exist”):** Titles evidenced by at least one of: ISBN agency record, publisher catalogue/announcement, legal deposit registration, or copyright registration.  
- **Circulation set (“Is-Visible”):** Titles present in retail listings, library catalogues, or discovery/preview platforms.  
- **Suppression indicators:** Withdrawals, takedowns, regional unavailability, search erosion, metadata mismatches, or “instant out-of-print.”

---

## 🧭 Data sources (priority order)

1. **ISBN agencies:** Bowker (US), Nielsen (UK/IE), national ISBN databases (AU, NZ, IN, ZA, NG, CA).  
2. **Legal deposit / copyright:** British Library Legal Deposit, Library of Congress, national copyright registries.  
3. **Publisher signals:** Advance catalogues, ONIX feeds, publisher press pages, trade newsletters.  
4. **Retail platforms:** Waterstones, Blackwell’s, Bookshop.org, Amazon, Barnes & Noble, Kobo, Apple Books, Google Play Books.  
5. **Libraries & discovery:** WorldCat, British Library catalogue, Library of Congress, major university libraries, Google Books previews.  
6. **Distribution:** Ingram, Gardners, Baker & Taylor (presence/absence + status codes).  
7. **Moderation/takedown:** KDP policy notices, retailer “content guideline” removals, distributor refusal codes. ⚖️

---

## 🧪 Sampling frames

Choose one (or run multiple cohorts):

- **Random ISBN cohort:** N = 2,000 English-language ISBNs issued in a quarter.  
- **Announced-but-uncertain cohort:** Titles from advance catalogues tagged “TBC” / sensitive topics.  
- **Thematic cohort:** Titles on high-risk themes (e.g., state violence, racialised risk, sex work, trafficking, state corruption). ⚖️  
- **Small-press cohort:** Independent presses and self-publishing imprints (higher vulnerability to quiet throttling).

---

## 🔧 Step-by-step procedure

1. **Assemble baseline (“Should-Exist”)**  
   - Collect: ISBN, title, subtitle, author(s), publisher, imprint, pub date, BISAC/BC subject, region, language, edition/format, announced territories, ONIX status.  
   - Deduplicate at **work level** (title+author+publisher+year), preserve edition rows.

2. **Normalise metadata**  
   - Canonicalise author names; map publishers to parents; harmonise dates to ISO-8601 UTC.  
   - Store raw + cleaned fields (avoid destructive edits).

3. **Legal-deposit check**  
   - Query BL/LoC (and relevant national) for deposit presence + date. Record: present/missing/pending.  
   - Flag titles with **ISBN issued but no deposit** after 90 days of pub date.

4. **Retail discovery sweep**  
   - Query each retailer API/site for exact ISBN and title+author.  
   - Record: listing present, status (pre-order/available/out-of-stock/unavailable), price, format, territory blocks.  
   - Capture **canonical product URL** and **HTTP status**.

5. **Library holdings sweep**  
   - WorldCat + national libraries + 5 major universities per country.  
   - Record total holdings, first-seen date, shelf status (on order/processing/in stock).

6. **Search visibility test**  
   - Run controlled queries:  
     - `"<title>" "<author>"`  
     - `ISBN-13`  
     - `"<title>" book`  
   - Record **rank of first organic result** for (a) publisher page, (b) legitimate retail page, (c) library record.  
   - Note **search erosion** patterns (e.g., spam outranks publisher; publisher page deindexed).  

7. **Distributor presence**  
   - Check Ingram/Gardners catalogue status (if accessible).  
   - Record refusal/withdrawal codes; note POD availability vs blocked. ⚖️

8. **Takedown / withdrawal signals**  
   - Capture notices (policy, legal, “content guideline” emails), sudden status flips (live → unavailable), and edition deletions. ⚖️  
   - Preserve **full headers** and **screenshots** with timestamps.

9. **Triangulate circulation**  
   - For each work, compute presence across: retailers (count), libraries (count), discovery rank (score).  
   - Assign **Circulation Presence Score (CPS)**:  
     - Retail coverage (0–5) + Library coverage (0–5) + Discovery rank score (0–5; inverse-rank binned) = **0–15**.

10. **Classify outcomes**  
    - **Normal circulation:** CPS ≥ 8 and ≥2 retailers and ≥2 library systems.  
    - **Shadowed:** CPS 4–7 or missing from either retail **or** libraries despite baseline evidence.  
    - **Suppressed (probable):** CPS ≤ 3 **and** at least one suppression indicator (takedown/withdrawal/refusal/regional block). ⚖️  
    - **Benign dropout:** Family vanity edition/local POD; document rationale.

---

## 📊 Metrics & thresholds

- **Suppression Gap % (work-level):**  
  \[
  \frac{\text{Shadowed} + \text{Suppressed (probable)}}{\text{All Baseline Works}} \times 100
  \]

- **Edition Attrition Rate:** editions per work announced vs editions with ≥1 retail or ≥1 library presence.

- **Time-to-Circulation (days):** Pub date → first retail listing; Pub date → first library holding.

- **Search Erosion Index (SEI, 0–10):** Composite penalty for absent publisher page, low organic rank, or spam outranking authoritative records.

- **Regional Availability Gini:** Inequality of holdings across regions (UK/US/CA/AU/IN/NG/ZA, etc.).

---

## 🧾 Evidence capture & reproducibility

- **Screenshots:** Filenames `YYYY-MM-DD_HHMM_UTC_platform_title_isbn.png`.  
- **Harvester logs:** Store query strings, timestamps, HTTP status, and user-agent.  
- **Hashing:** SHA-256 for all captured pages (where archived).  
- **Archival:** Save canonical URLs to the Wayback Machine + local PDF print.  
- **Chain of custody:** Record collector, method, and environment.

---

## 🗃️ Minimal data schema (CSV)

```csv
work_id,isbn13,title,author,publisher,imprint,lang,announced_pubdate,region_declared,baseline_source,bl_deposit,loc_deposit,retailers_present,retail_statuses,library_holdings,worldcat_count,discovery_rank_pub,discovery_rank_retail,discovery_rank_library,distributor_status,takedown_flag,notes,cps,class
```

- `class` ∈ {normal, shadowed, suppressed_probable, benign_dropout}.

---

## 🧮 Estimating the market-level impact

1. Compute **Suppression Gap %** over your cohort.  
2. Extrapolate to estimated annual English-language new works (document your denominator—e.g., Nielsen+Bowker title counts for the period).  
3. Present **low/central/high** scenarios:  
   - Low: treat all shadowed as benign.  
   - Central: 50% of shadowed + 100% suppressed.  
   - High: all shadowed are suppressed vectors.

---

## 🧑‍⚖️ Risk, ethics & legal review (UK-focused)

- **Attribution caution (⚖️):** Do **not** publicly name a suppressing party without strong evidence (e.g., a policy notice, refusal code, or consistent multi-platform pattern). Offer right of reply.  
- **Defamation risk (⚖️):** Keep factual, time-stamped records; separate fact from inference; avoid motive statements.  
- **Sexualised content review:** If examples involve sexual content (e.g., school library challenges), clearly label excerpts, minimise quotation, and consult safeguarding guidance before publication.  
- **Data protection:** Avoid processing special-category personal data in notes; redact where necessary.

---

## 🧰 Quick-use checklists

- **Field run setup**  
  - [ ] Define cohort & time window  
  - [ ] Build baseline from ≥2 sources  
  - [ ] Prepare schema + hashing  
  - [ ] Pre-register thresholds & classes

- **Per-title audit**  
  - [ ] Legal deposit check  
  - [ ] Retail sweep (≥5 platforms)  
  - [ ] Library sweep (WorldCat + nationals)  
  - [ ] Search visibility test (3 queries)  
  - [ ] Distributor status (if accessible)  
  - [ ] Evidence archived (screenshots + Wayback)  
  - [ ] CPS computed & class assigned

- **Reporting**  
  - [ ] Suppression Gap % + confidence bands  
  - [ ] Topic/region drill-downs  
  - [ ] Case studies with redactions (⚖️)  
  - [ ] Right-of-reply log (⚖️)

[✨ Back to top](#TOP)

---

## ✨ Constellations

- Links into:  
  - **🔮 Visibility Indexing Anomalies** — search erosion & ranking gaps  
  - **🪅 Platform Sabotage** — retailer/platform policy cascades  
  - **🧿 Watch The Watchers** — audits of oversight bodies  
  - **🐦‍🔥 Trauma Psychology & Medical Misuse** — thematics with higher suppression risk  
  - **📜 Statutes** — legal frameworks shaping removals (obscenity/terrorism/defamation)  
  - **💎 Resources** — ISBN/ONIX/WorldCat query tips

---

## 🏮 Footer

*📚 English-Language Book Suppression — Audit Protocol* is part of the Polaris Protocol diagnostics.  
It provides a reproducible method to **measure suppression gaps** and preserve **forensic evidence** for public accountability.

*Survivor authorship is sovereign. Containment is never neutral.*

_Last updated: 2025-10-01_
