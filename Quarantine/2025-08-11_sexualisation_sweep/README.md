/Polaris-Protocol/
    /Quarantine/
        /2025-08-11_sexualisation_sweep/README.md


Quarantine/2025-08-11_sexualisation_sweep/


regex pattern

\berotic\b|\bsex\b|\bsexual\b|\bnude\b|\bnudity\b|\bNSFW\b|\bexplicit\b|\bfetish\b|\bdesire\b|\bmoan(?:ed|ing)?\b|\borgasm\b|\bpleasure\b|\bintimate\b

GPT: That actually tells us something useful — it means the contamination isn’t leaning on **obvious trigger words**.

If you’re reading stuff and feeling “this is sexualised” but our sweeps aren’t catching it, then the skew is probably:

* **Tone-based** rather than keyword-based (suggestive phrasing without explicit terms)
* **Metaphor-heavy** or using innocuous words in charged contexts
* Possibly relying on **structural patterns** (e.g., sentence rhythm, pronoun use, over-descriptive body language)

For that, keyword scans won’t be enough — we’d need to:

1. Identify a handful of *“known bad”* contaminated passages.
2. Extract recurring *phrasing patterns* from them.
3. Build a second sweep list from those patterns instead of single words.

If you can give me even **2–3 short contaminated snippets** (redacted for comfort), I can analyse them and generate a **pattern-based hit list** that might surface the subtle stuff.

Do you want me to do that next so we can catch the hidden skew?


git checkout -b governance-pass-2025-08-11
git tag baseline-pre-clean-2025-08-11
git push --tags





DONE: 


C:\Users\chloe\Documents\GitHub\Polaris-Protocol>
C:\Users\chloe\Documents\GitHub\Polaris-Protocol>git checkout -b governance-pass-2025-08-11
Switched to a new branch 'governance-pass-2025-08-11'

C:\Users\chloe\Documents\GitHub\Polaris-Protocol>git tag baseline-pre-clean-2025-08-11

C:\Users\chloe\Documents\GitHub\Polaris-Protocol>git push --tags
info: please complete authentication in your browser...
Enumerating objects: 2607, done.
Counting objects: 100% (2604/2604), done.
Delta compression using up to 2 threads
Compressing objects: 100% (862/862), done.
Writing objects: 100% (2595/2595), 15.99 MiB | 2.41 MiB/s, done.
Total 2595 (delta 1625), reused 2592 (delta 1622), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1625/1625), completed with 3 local objects.
To https://github.com/josefsbreakfast/Polaris-Protocol.git
 * [new tag]         baseline-pre-clean-2025-08-11 -> baseline-pre-clean-2025-08-11

C:\Users\chloe\Documents\GitHub\Polaris-Protocol>


>>>>>>
>>>>>>Yes Chloe—perfect. You’ve got a clean branch and a baseline tag. Here’s a tight next-step kit so you can sweep without faff.

# Quick plan (15-minute setup → ongoing sweep)

**Make folders**

```
Polaris-Protocol/
  Quarantine/2025-08-11_manual/
  scans/
```

**Push the branch (once you’ve got a few edits)**

```bash
git push --set-upstream origin governance-pass-2025-08-11
```

# Tone deviation checklist (keep this open while skimming)

* Does the paragraph add **sensual/romantic shading** to a legal/forensic point?
* Any **over-descriptive body/emotion language** that isn’t evidential?
* Sudden **cheeky/banter** voice inside formal sections?
* Adjectives like *soft, warm, close, wet, gentle, hungry, throbbing, aching* etc.
* Unnecessary **second-person** (“you”) flirt-like address; or **first-person** that shifts to desire/implied intimacy.
* **Metaphors** that sexualize force/power/containment rather than describe facts.

# Triage severity (so you don’t get bogged down)

* **L3 (Critical)**: explicit sexualisation or innuendo in legal/forensic sections → **Quarantine immediately**, replace with neutral placeholder.
* **L2 (Material)**: suggestive tone/metaphor that could undermine credibility → **Neutral rewrite now** (keep short), log it.
* **L1 (Minor)**: stylistic cheekiness in non-critical sections → mark with `<!-- tone-trim -->` and fix later if time.

# Edit workflow per file (fast loop)

1. Skim. If it pings the checklist, assign **L1/L2/L3**.
2. **L3** → copy original to Quarantine (preserve path), replace live text with a neutral line:

   > `[Removed tone-skewed passage pending review — see Quarantine/2025-08-11_manual/<path>]`
3. **L2** → trim adjectives/metaphors, swap to factual verbs; keep the claim intact.
4. Log the action in `scans/harm_scan_2025-08-11.txt`:

   ```
   [L2] File: Survivor_Tools/🧬 cloneproof.md — P4
   Action: Neutralised suggestive metaphor; preserved evidential content.
   ```
5. Save, move on. Commit in small batches.

# Neutral rewrite patterns (quick swaps)

* Sensual adjective → **remove** or swap to factual:
  “*warm, close pressure*” → “pressure”.
* Metaphor → **plain verb**:
  “*seduced the system into compliance*” → “induced system compliance via X”.
* First/second-person flirt → **institutional subject**:
  “*you’ll want to…*” → “The applicant should…”.
* “want/need” → **request/require** in legal contexts.
* “feel” → **observe/evidence indicates**.

# Commit cadence (keeps you safe + readable)

After each small batch (e.g., 5–10 files):

```bash
git add -A
git commit -m "governance: pass1 — quarantined 3 files (L3), neutralised 7 (L2)"
```

End of session:

```bash
git push
```

# (Optional) One-liner PowerShell to quarantine while preserving paths

Paste in a PowerShell window opened at repo root:

```powershell
function Quarantine-File {
  param([string]$RelPath)
  $src = Join-Path $PWD $RelPath
  $dst = Join-Path $PWD ("Quarantine/2025-08-11_manual/" + $RelPath)
  New-Item -ItemType Directory -Force -Path (Split-Path $dst) | Out-Null
  Copy-Item $src $dst -Force
  Write-Output "[Quarantined] $RelPath"
}
# Use: Quarantine-File "Survivor_Tools/🧬 cloneproof.md"
```

# Tiny sanity checks (when you need a quick pulse)

```bash
# What changed?
git status

# What did I touch in this batch?
git diff --name-only

# How many L3 quarantines so far? (depends on your log wording)
rg -n "\[L3\]" scans/harm_scan_2025-08-11.txt 2>$null | measure
```

Want me to generate a **starter harm log file** with headers you can paste in and fill as you go, or a **VS Code search preset** (saved search queries) to speed the manual sweep?
>>>>>>>>>
>>>>>>>>>








