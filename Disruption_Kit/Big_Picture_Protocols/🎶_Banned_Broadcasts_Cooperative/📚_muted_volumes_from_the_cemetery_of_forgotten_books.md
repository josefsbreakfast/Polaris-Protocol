# 📚 How to Find Muted Volumes, for Return to the Cemetery of Forgotten Books  
**First created:** 2025-09-17 | **Last updated:** 2025-09-17  
*Replicable protocol for checking whether a trade title has been published and then effectively muted (plausible-deniability suppression vs natural obscurity).*  

---

🕯️ *All books need homes, so we make sure they are kept safe, even when others pretend they cannot hear their words echo through time.*  

Book burning is rather gauche, so welcome to the 21st century, where one merely needs to snuff a title out of relevance to vanish it.  

---

## 1. Quick framing — what you’re testing  
You’re testing whether a legitimately published book was **deliberately denied normal circulation/visibility** (reviews, paperback conversion, library uptake, search discoverability) or whether it simply failed organically (poor marketing, low demand).  

Key observable markers to collect: publication metadata, retailer footprints, library holdings, review coverage, distribution metadata, Wayback/Archive history, and any contemporaneous correspondence (emails, letters) that might have chilled promotion.  

---

## 2. Preserve first (non-negotiable)  
Before you share anything publicly or with journalists/counsel: preserve originals.  

- Save original emails as **.eml** (raw headers).  
- Save any legal threats (letters, PDFs) as PDFs.  
- Take screenshots and save as PNG/PDF of: publisher page, Amazon listing, retailer listings, review pages. Record timestamps.  
- Archive pages on Wayback/Archive.org.  
- Make SHA256 checksums for key files. Keep an offline encrypted copy.  
- Don’t publicise raw private messages; use redacted extracts if sharing.  

---

## 3. Core trace (minimum reproducible searches)  
Gather the canonical identifiers ([REDACTED ISBN], [REDACTED ASIN]). If you only have a screenshot, OCR it for identifiers.  

Search these places (in parallel):  

1. **Publisher** — canonical product page, press kit, media contact.  
2. **Retailers** — Amazon, Waterstones, Bookshop.org, Barnes & Noble, Booktopia, Bol, Adlibris. Save URLs.  
3. **Library catalogues** — WorldCat (check holdings), British Library, Library of Congress, national library of major markets. Note number of holdings and which libraries.  
4. **Google Books** — bibliographic entry/preview.  
5. **Distributor/metadata** — Ingram, Gardners, Nielsen (if accessible), ISBN registries. Look for BISAC/BIC tags, distributor listing.  
6. **Reviews / media** — search major newspapers, literary journals, trade press.  
7. **Social / reader** — Goodreads, LibraryThing, Amazon reviews/ratings.  
8. **Archive/History** — Wayback of publisher and major retailer pages; check for deletion/relisting.  
9. **Search query behavior** — test subject-specific and title/author-specific queries; note which unrelated results surface first.  

---

## 4. Concrete checks & what they indicate  
- **Publisher page present + stable** → book exists.  
- **Retailers: ebook/HB/PB presence**  
  - HB only, no PB after 12–18 months → suspicious for trade political titles.  
  - Ebook present but HB print dead → could be distribution choice or an attempt to mark “published” while choking print: suspicious.  
- **Amazon Rank**: extremely low rank (~>1M) suggests no sales momentum.  
- **WorldCat holdings < ~10, BL reference-only** → limited library uptake; suspicious for [REDACTED PUBLISHER]-level title.  
- **No mainstream reviews** in press outlets for a topical trade book → anomalous.  
- **Presence of token reviews in niche outlets only** → minimal PR push or targeted PR only.  
- **Distributor metadata missing or wrong BISAC/BIC** → discoverability error; could be accidental or deliberate.  
- **Wayback shows deletion/relist pattern** → strongly suspicious (takedown/relist).  
- **Search queries returning unrelated/hostile content first** → metadata or SEO suppression, or SEO manipulation (search noise burying).  

---

## 5. Scoring: suspicion checklist (quick heuristic)  
Give 1 point for each:  

- HB only after 12–18 months (1)  
- WorldCat holdings < 10 (1)  
- British Library only reference/no lending (1)  
- No mainstream press reviews (1)  
- Amazon rank > 500k / negligible sales (1)  
- Distributor metadata missing or mis-tagged (1)  
- Wayback shows removal or relist (2)  
- Search results bury relevant pages under unrelated content (1)  

**Interpretation**  
- 0–1: likely natural obscurity.  
- 2–3: borderline — more checks required (distributor metadata, Wayback).  
- 4–6: probable engineered muting or systemic distribution failure.  
- 7–9: strong indicator of deliberate muting or targeted chilling.  

---

## 6. Deeper forensic steps (run if score ≥2)  
A. **WorldCat holdings — full audit**: list which institutions hold it; request scans or check catalogue notes.  
B. **Distributor metadata audit**: pull Ingram/Gardners entry (ISBN, BISAC/BIC, publication date, distributor listing). Look for missing fields or “not available in X market.”  
C. **Wayback / Archive history**: fetch snapshots for the publisher page and Amazon listing from launch → present. Look for content changes, removal, or press release removal.  
D. **ARC/review timeline**: compile dates of ARC offering, review posting, and publication date — check for abrupt stops.  
E. **Contact list**: note publisher publicity contact, author publicist, reviewer names (if any). Document any silence or refusal to respond.  
F. **Metadata forensics**: check ISBN registration date and any different ISBNs for HB/PB that never materialised.  
G. **Email headers & server logs**: if you have an email used in the case, extract full headers and note sending IPs, DKIM/SPF records. This helps detect spoofing or impersonation.  
H. **Third-party takedown records**: search for DMCA/complaint notices or legal threats publicly posted.  

---

## 7. Templates (redacted-ready)  
Use `[REDACTED]` placeholders for sensitive fields.  

*(Publisher inquiry, solicitor intake, journalist packet — unchanged from original draft.)*  

---

## 8. How to present findings publicly (safe practices)  
- Use **redacted identifiers** in public-facing notes: e.g., `ISBN [REDACTED]`, `Author [REDACTED]`.  
- Publish the **methodology + public evidence** (publisher pages, review links, Wayback captures) — that shows the pattern without exposing private data.  
- Offer to share originals under NDA with a trusted journalist or solicitor, not publicly.  
- Avoid naming unverified actors as perpetrators; focus on pattern and evidence. The redaction itself becomes signal.  

---

## 9. Quick checklist for a field investigator (one-page)  
- [ ] Save .eml + headers.  
- [ ] Screenshot publisher + Amazon + retailer pages.  
- [ ] Archive pages on Wayback.  
- [ ] Pull ISBN into WorldCat and record holdings.  
- [ ] Search mainstream reviews (Guardian/FT/TLS/LRB) — screenshot no-hits.  
- [ ] Pull distributor entry (Ingram/Gardners) or request metadata.  
- [ ] Compile review timeline.  
- [ ] Compute suspicion score.  
- [ ] Draft neutral publisher inquiry.  
- [ ] If score ≥4: package redacted journalist packet + solicitor intake.  

---

## 10. Notes on interpretation & pitfalls  
- **Not every low-visibility title is suppressed.** Small presses have limited budgets and some books just don’t generate demand. This methodology is about building a pattern that rules out normal failure modes.  
- **Middleman cascades**: sometimes suppression looks like coordination but is actually a cascade of independent prudence (see “cascade of chilling”). Document chain-of-communications where possible.  
- **Timing is important**: delayed reviews or delayed paperback plans can be legitimate. Use the 12–18 month paperback expectation as a rule-of-thumb for trade political titles.  
- **Don’t weaponise the methodology** — keep it forensic and evidence-driven.  

---

## 11. Closing notes — limits of this methodology  
This protocol is designed to establish **what happened** in relation to a book’s publication and circulation. It is not designed to determine motive or beneficiary — that requires separate analysis. Tracing who benefits and who has means is power mapping: situating actors, incentives, and spheres of influence.  

That stage may reveal that muting had little to do with the book itself and everything to do with parallel or unrelated events. Indeed sometimes the origin is, in essence, horseshit: rumours, misreads, or spurious triggers that cascade into real suppression.  

*Never assume there is ever an adult in any given room at any given time.*  

---

## 🏮 Footer  
*How to Find Muted Volumes, for Return to the Cemetery of Forgotten Books* is a living node of the Polaris Protocol.  

> 📡 Cross-references:  
> - [📚 Forensic Silence](../Disruption_Kit/Big_Picture_Protocols/📚_forensic_silence.md)  
> - [🪞 Cascade of Chilling](../Disruption_Kit/Big_Picture_Protocols/🪞_cascade_of_chilling.md)  
> - [💎 Resources](../💎_Resources/)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-09-17_  

