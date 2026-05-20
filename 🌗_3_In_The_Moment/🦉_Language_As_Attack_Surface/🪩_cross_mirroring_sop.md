# 🪩 Cross-Mirroring SOP  
**First created:** 2025-11-02  |  **Last updated:** 2026-05-20  
*How to create, verify, and maintain redundant mirrors of captured linguistic evidence.*

---

## 🧭 Orientation  

Archival disappearance is a second-order form of censorship.  
Cross-mirroring ensures that no single host, platform, or account can silently erase evidence.  
This SOP defines the minimal redundancy protocol for all Polaris evidence and documentation nodes.

---

## ✅ Steps for Each Capture Set  

1. **Prepare source folder**  
   - Store original capture + plaintext + hash manifest.  
   - Folder name = `cap-YYYY-MM-DD-###`.  

2. **Create mirror copies**  
   - Minimum 2 independent locations (Example: academic archive + encrypted cloud).  
   - Optional third: offline cold-storage drive.  

3. **Generate and verify hashes**  
   ```bash
   shasum -a 256 * > hash_manifest.txt
   ```  
   - Compare hashes across all mirrors; they must match byte-for-byte.  

4. **Record mirrors**  
   - Add row to `archives/hash_manifest.csv`:  
     `capture_id, mirror_path, hash, verified_by, date`  

5. **Quarterly audit**  
   - Sample 10 % of entries and re-verify hashes.  
   - Log results in `archives/audit_log.md`.  

6. **Access controls**  
   - Read-only for mirrors; write access only to maintainers listed in audit log.  
   - Encrypt sensitive material with AES-256.  

---

## 🧱 Directory Layout Example  

```
archives/
 ├── cap-2025-11-02-001/
 │     ├── capture.png
 │     ├── capture.txt
 │     └── hash_manifest.txt
 ├── mirror-A/
 ├── mirror-B/
 ├── hash_manifest.csv
 └── audit_log.md
```

---

## 🧩 Verification Script Example  

```bash
for f in $(cat hash_manifest.txt | awk '{print $2}'); do
  shasum -a 256 -c $f
done
```

---

## 🌌 Constellations  

🪞 📡 🪩 🧾 ⚖️ — redundancy · verification · integrity  

---

## ✨ Stardust  

archival redundancy, data integrity, mirror verification, digital preservation, chain of custody  

---

## 🏮 Footer  

*🪩 Cross-Mirroring SOP* is a procedural node of the Polaris Protocol.  
It ensures archival redundancy and prevents silent erasure of evidence.  

> 📡 Cross-references:
> 
> - [🧾 Archive Capture Template] — source procedure  
> - [📡 Language as Attack Surface] — parent context  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-05-20_
