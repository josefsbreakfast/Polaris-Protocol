# Maintenance Scripts

## Running `folder_consistency_pass.sh` without chmod

If working **only in the web UI** (GitHub.com, GitLab.com, etc.) and not using a local terminal, you cannot run `chmod +x`.  
That’s fine — you can still run the script using either:

---

### **Option A – Run via GitHub Actions**
1. Make sure `.github/workflows/folder-consistency.yml` exists (see repo docs or workflow file for content).
2. Go to **Actions** tab → select **Folder Consistency Scan** → **Run workflow**.
3. Download the generated report artifact from the workflow run.

---

### **Option B – Use bash directly**
If you have *any* terminal access (Codespaces, local machine, etc.):
```bash
bash scripts/maintenance/folder_consistency_pass.sh
bash scripts/maintenance/folder_consistency_pass.sh --apply   # to auto-fix
