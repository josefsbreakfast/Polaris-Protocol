# 🛰️ OSINT for Anti-Palestinian Racism Detection — Using Social Media Responsibly  
**First created:** 2025-10-28 | **Last updated:** 2025-10-28  
*Practical, ethical guidance for using open-source social-media methods to surface patterns of anti-Palestinian racism, coordinated harassment, and signalling — without amplifying harm or doxxing individuals.*

---

## 🛰️ Orientation  
This node is a hybrid **OSINT + media-analysis** guide for researchers, survivors, and allies documenting anti-Palestinian racism online.  
It is explicitly **evidence-gathering, not vigilante**: the goal is to detect patterns and build safe, accountable records that can be used for institutional complaints, FOI/casework, platform reports, or academic analysis.

We centre two constraints at every step: **do no further harm** (no doxxing; minimise retraumatisation), and **preserve admissible evidence** (timestamped, verifiable captures, chain of custody).

---

## 🔬 Scope & Use Cases
- Detect coordinated harassment campaigns or repeated dog-whistle signalling aimed at Palestinians, Palestinian allies, or visibly racialised/ Muslim students.  
- Identify recurring performative acts (e.g., eviction paperwork handed out during commemorations, ritualised imagery) and their propagation across institutional channels.  
- Map networks of amplifiers (accounts, hashtags, PR/NGO scripts) and cross-reference sector coordination hypotheses.  
- Produce safe, redacted dossiers for FOI, ICO complaints, institutional escalation, or media briefing.

---

## 🧭 Ethics & Safety (non-negotiable)
1. **No doxxing.** Do not publish or circulate personal contact details, home addresses, or private identifiers. Never advise others to confront or harass.  
2. **Minimise amplification.** If content is harmful, capture and archive it for evidence — do **not** retweet/share materially. Use private, access-controlled evidence stores.  
3. **Consent & care.** Ask whether people filmed/photographed want their image used in a dossier. Prioritise the safety wishes of those most at risk (young women, visibly racialised activists).  
4. **Trauma-aware practice.** Working with this material can be triggering. Build breaks, peer review, and, where possible, survivor leadership into analysis.  
5. **Legal caution.** Avoid instructions that could be construed as facilitating illegal surveillance. If you suspect criminality, escalate to appropriate channels (police/ICO) rather than conducting intrusive probes yourself.

---

## 🛠️ Practical OSINT Methods (safe, non-invasive)
> Use the smallest effective toolset. Capture evidence; don’t escalate it.

### 1 — Constructive keyword & hashtag search  
- Start with obvious hashtags/keywords: e.g., `#GazaSolidarity`, `#Nakba`, `#FreePalestine`, plus local variants (`#UoBencampment`, `#NottinghamCamp`).  
- Search full phrases that reflect official lines to find template reuse: `"for reasons of safety and wellbeing"`, `"unauthorised encampment"`.  
- Use time filters (platform advanced search / native date range) to isolate the period of interest (e.g., 1 Apr — 31 Jul 2024).

### 2 — Account & network mapping (surface, don’t probe)  
- Identify recurring amplifiers: accounts reposting the same PR lines, or media outlets quoting identical phrases.  
- Use public follower/following lists and visible retweet/repost graphs to spot template propagation. Do **not** scrape private data.  
- Flag shared handles (PR firms, shared legal accounts, or NGO advocacy accounts) as nodes in the network — useful for FOI/sector-coordination lines.

### 3 — Visual & ceremonial pattern detection  
- Collect screenshots of ceremonial actions (timing of paperwork service, uniformed lines, symbolic gestures) — note date/time and source URL.  
- When symbolism appears (e.g., letters addressed to “Occupiers” handed out on Nakba Day), capture context: event name, who was present, whether a memorial was ongoing. These patterns are meaningful for interpretive analysis.

### 4 — Reverse-image & media validation (light touch)  
- Use reverse-image tools (e.g., Google reverse image / TinEye) to detect re-use of the same photos across multiple official statements. Don’t run deep image forensics unless you have training.  
- For videos: note visible clocks, weather, or identifiable landmarks to corroborate date/time. Do not attempt intrusive geolocation that could identify private residences.

### 5 — Archive & immutability  
- Save captures to a controlled archive (PDF export, screenshot with URL + visible timestamp, or an `eml` email export).  
- For legal traction, include: source URL, capture datetime (UTC), platform, screenshot, and a short provenance note (who posted it; if reposted, chain of reposts).  
- Keep originals in a read-only folder; make hashes (SHA256) of files for integrity proof.

---

## ✅ Verification checklist (to increase evidential quality)
- [ ] Source URL recorded and clickable.  
- [ ] Date/time of capture (UTC) recorded and visible in the capture.  
- [ ] Platform account handle + profile URL captured.  
- [ ] If video, record start/stop timestamps and any in-frame audio quotes.  
- [ ] Hash of the stored file computed and logged.  
- [ ] Short provenance note: who posted, what caption, whether it was shared by an institutional account.  
- [ ] Cross-check: does another independent source corroborate the same event/time? (e.g., two different eyewitness posts)

---

## 🔎 Indicators of Coordinated Anti-Palestinian Action (what to look for)
- **Lexical templates:** identical sentences appearing across multiple institutional press releases or multiple universities.  
- **Synchronized timing:** similar statements released within 24–48 hours across institutions.  
- **Symbolic actions at memorial times:** paperwork/service/dismantling timed to memorials (e.g., Nakba Day) or religious observances.  
- **Target mapping:** repeated filming of visibly Muslim or racialised activists, followed by online doxxing or complaint campaigns.  
- **Advocacy/PR overlap:** the same NGO or law-firm Twitter/LinkedIn posts cross-referenced by universities.  
- **Hashtag weaponisation:** creation of localised hashtags used to amplify complaint threads and identify organisers.

---

## 🧩 Symbolic Mirroring and Substantive Harm

> Across several UK encampments (2024), documented actions and communications employed **terminology and sequencing** that closely mirror techniques and symbolism associated with land seizure or annexation elsewhere — *“clearance,” “restoration of control,” “return of possession,”* and even paperwork addressed to *“Occupiers.”*  
> 
> Some incidents coincided with **Palestinian memorial or religious observance dates** (e.g., Nakba Day, Ramadan, Friday prayers), which magnified the emotional and cultural impact for participants.  
> 
> It is not necessary to assert intentional mimicry to recognise that these **performative parallels** reproduce the *psychological architecture* of occupation: forced visibility, public degradation, displacement enacted as spectacle.  
> 
> When institutional actions reproduce those frames — especially when timed to sacred or memorial observances — they risk constituting **psychological violence amounting to a breach of the peace**, even in the absence of physical harm.  
> 
> In evidential terms, this can be approached as a *pattern-of-conduct analysis*:  
> - repeated use of identical paperwork or phrasing across sites;  
> - staging of clearance operations during culturally or spiritually significant times;  
> - coercive tone or address (“Occupiers”) carrying racialised or political charge;  
> - symbolic gestures (cordons, fences, line formations) that replay imagery of occupation.  
> 
> Each element, on its own, may appear administrative; together, they form a recognisable **repertoire of domination** that warrants independent review.

---

## 📂 Documentation & Redaction (how to hold evidence safely)
- Use a private, encrypted folder (veracrypt / encrypted cloud with strong access controls).  
- Produce a single **evidence index** CSV with columns: `id, date_utc, platform, source_url, snapshot_filename, sha256, short_desc, tags, provenance_notes`.  
- Redact names/IDs of private individuals before sharing externally. Replace with unique codes (e.g., `subject_A`) and keep a separate key offline for legal counsel only.  
- When sharing with journalists, legal teams, or regulators, use secure transfer (passworded PDF / secure file share) and an accompanying custody note.

---

## 🔬 Methodological cautions & limits
- **Correlation ≠ intent.** Repetition of wording can be suggestive of coordination but isn’t proof of a central conspiracy. Use FOI to test the coordination hypothesis.  
- **False positives:** benign PR firms or legitimate safety alerts may reuse phrasing; always verify provenance.  
- **Data decay:** social posts can be removed; archive aggressively but ethically.  
- **Ethical partners:** when in doubt, engage a legal adviser, a survivor-led group, or a trusted researcher before publication.

---

## 🌌 Constellations  
🪄 Expression of Norms · 🧿 Watch the Watchers · 🍉 Academic Liberty · 🕊️ Civil Governance

---

## ✨ Stardust  
OSINT, social media, anti-Palestinian racism, harassment, doxxing, archive, ethical research, platform reporting, university governance

---

## 🏮 Footer  
*This node is a practical guide — not legal advice. It prioritises survivor safety and institutional accountability.*  
