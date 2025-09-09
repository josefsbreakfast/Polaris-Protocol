# 👾 Reduced Integrity Checks Downstream — Auditor Examples  

**First created:** 2025-09-09 | **Last updated:** 2025-09-09  

*Illustrative Python snippets for auditors: detecting silent flips, weak integrity checks, and missing audit entries.*  

---

## Purpose  

This file adjoins [👾 Reduced Integrity Checks Downstream](./👾_reduced_integrity_checks_downstream.md).  
It does **not** describe exploits.  
It provides *auditor-friendly code examples* to quickly surface anomalies in lawful exports (CSV/JSON).  

---

## Example 1: Spotting Silent Role Flips  

```python
import pandas as pd

history = pd.read_csv("case_history.csv")  
role_changes = history[history['field'].isin(['complainant_id','subject_id'])]

pivot = role_changes.pivot_table(index=['case_id','changed_at'],
                                 columns='field', values='new_value',
                                 aggfunc='last').reset_index()

first = pivot.sort_values('changed_at').groupby('case_id').first()
last = pivot.sort_values('changed_at').groupby('case_id').last()

flips = (first['complainant_id'] == last['subject_id']) &         (first['subject_id'] == last['complainant_id'])

print("Cases with possible inversion:")
print(first[flips].index.tolist())
```

---

## Example 2: Catching Identity Rebinding (X → Z)  

```python
rebounds = role_changes[role_changes['field']=='complainant_id']
rebounds = rebounds[rebounds['old_value']!=rebounds['new_value']]

rebounds['rebind_pair'] = rebounds['old_value'] + " → " + rebounds['new_value']

print("Detected rebinds (complainant rotated):")
print(rebounds[['case_id','old_value','new_value','changed_at','actor']])
```

---

## Example 3: Flagging Weak Audit (Missing Actors)  

```python
weak_audit = history[history['actor'].isna() | history['actor'].str.upper().eq("SYSTEM")]

print("Changes without accountable actor:")
print(weak_audit[['case_id','field','old_value','new_value','changed_at']])
```

---

## Example 4: Checking for Soft-Deletes  

```python
cases = pd.read_csv("cases.csv")  
soft_deleted = cases[cases['deleted_at'].notna()]

print("Soft-deleted cases (hidden but not erased):")
print(soft_deleted[['case_id','deleted_at']])
```

---

## 🏮 Footer  

*Reduced Integrity Checks Downstream — Auditor Examples* is a living node of the Polaris Protocol.  
It provides simple diagnostic scripts for lawful data exports, allowing auditors to verify whether downstream record handling suffered from weak integrity checks.  

> 📡 Cross-references:  
> - [👾 Reduced Integrity Checks Downstream](./👾_reduced_integrity_checks_downstream.md)  
> - [⚠️ Fork Anomaly Hypothesis — X, Y, Z](./⚠️_fork_anomaly_hypothesis_XYZ_2025-09-09.md)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-09-09_  
