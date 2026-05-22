
# 🛠️ Maintenance Scripts  

**First committed:** 2025-08-10 | **Last updated:** 2025-08-29
*Scripts for sweeps, consistency checks, and governance passes*  

---

## 📂 Folder Consistency Pass (`folder_consistency_pass.sh`)  

### ❓ Problem  
If you’re working **only in the web UI** (GitHub.com, GitLab.com, etc.), you can’t run `chmod +x`.  

### ✅ Solution  
You can still execute the script using one of two routes:  

---

### **Option A — GitHub Actions**  
1. Confirm `.github/workflows/folder-consistency.yml` exists.  
2. Go to **Actions** → **Folder Consistency Scan** → **Run workflow**.  
3. Download the report artifact when the workflow completes.  

---

### **Option B — Direct Bash Call**  
If you have *any* terminal access (Codespaces, local shell, VM):  

```bash
bash scripts/maintenance/folder_consistency_pass.sh
bash scripts/maintenance/folder_consistency_pass.sh --apply   # auto-fix mode

---

📜 **Script Index**  

- `folder_consistency_pass.sh` 🗂️ → Scan & auto-fix folder drift.  
- `governance_pass.ps1` ⚖️ → Batch governance pass runner (PowerShell).  
- `harm_scan.py` 🔍 → Regex + semantic harm scanner.  
- `merge_harm_log.ps1` 📑 → Merge multiple harm logs into one forensic record.  
- `new_harm_log.ps1` 🆕 → Spawn a timestamped harm log scaffold.  
- `template_entry.md` 🧩 → Standardised sweep/harm entry template.  

---

⚖️ **Protocol Notes**  

- Always run sweeps in **small batches** → prevents noisy commits.  
- Commit generated logs to a **quarantine branch** before merge.  
- Treat all outputs as **forensic artefacts** → never overwrite without log preservation.

---

🏮 [Return to repo root](https://github.com/josefsbreakfast/Polaris-Protocol/)

---
