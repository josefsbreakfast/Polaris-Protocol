# 🏛️ Archive Capture Template  
**First created:** 2025-11-02 | **Last updated:** 2025-12-09  
*Standard operating procedure for capturing, verifying, and mirroring linguistic-evidence files.*  

---

## 🧭 Orientation  

Every capture must be reproducible. This template defines the minimum metadata and file-handling protocol for evidence that may later be used in investigative, journalistic, or legal review.

---

## ✅ Capture Checklist  

1. **Screenshot + Context**  
   - Full-page screenshot (include thread or parent post).  
   - Save additional image of top comment chain if relevant.  

2. **Plain-Text Copy**  
   - Copy raw text into a `.txt` file.  
   - Preserve punctuation, spacing, and emoji exactly.  

3. **Timestamps**  
   - Record both *local* and *UTC* times of capture.  
   - Note publication timestamp if visible.  

4. **Source URLs**  
   - Include canonical URL and any mirrors.  
   - If content is later deleted, keep hash + archived copy.  

5. **Metadata Dump**  
   - Author handle / ID  
   - Platform  
   - Follower count (approx.)  
   - Engagement at capture time (likes / shares / comments).  

6. **Hash Verification**  
   ```bash
   shasum -a 256 capture.png > capture_hash.txt
   ```  
   Store the hash with the file; use same hash in cross-mirrors.  

7. **Mirroring**  
   - Maintain at least two off-platform copies.  
   - Save hashes in `archives/hash_manifest.csv`.  

8. **Notes**  
   - Summarise context or potential significance (≤ 50 words).  
   - Link to corresponding YAML entry if applicable.  

---

## 🧩 Example Entry (Markdown block)  

```markdown
### Capture ID: cap-2025-11-02-001
Source: twitter.com/example/status/123  
Captured: 2025-11-02 21:00 UTC  
Platform: Twitter/X  
Context: First emergence of euphemism “population adjustment.”  
SHA256: 1a3c9…f27b  
Mirrors: polaris-mirror1 / polaris-mirror2  
Linked Watchlist ID: df-0001  
Notes: Same phrasing later reused in three outlets within 24 h.
```

---

## 🌌 Constellations  

🧾 📡 ⚖️ 🛰️ — verification · traceability · accountability.

---

## ✨ Stardust  

archive integrity, capture protocol, digital verification, chain of custody, metadata preservation, survivor fidelity  

---

## 🏮 Footer  

*🏛️ Archive Capture Template* is a living procedural node of the Polaris Protocol.  
It ensures that captured linguistic evidence remains verifiable, reproducible, and admissible.  

> 📡 Cross-references:  
> - [📡 Language as Attack Surface] — source node  
> - [watchlist/frame_drift_watchlist.yaml] — referenced IDs  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-12-09_
